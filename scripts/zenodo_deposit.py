#!/usr/bin/env python3
"""Deposito automatico su Zenodo (DOI) per articoli approvati (handoff
Cowork -> Claude Code, deposito Zenodo, 2026-09-22; deroga esplicita alla
soglia di Fase 4 di PHASE-3-PLAN.md, decisione registrata in
MEMORY/MEM-2026-09-22-01-zenodo-automation-phase-gate-override.md).

Cosa fa, per ogni voce di data/zenodo-deposits.yaml con `approved: true`
e `doi` ancora vuoto (idempotente: una voce con `doi` gia' valorizzato
viene sempre saltata):

1. Genera il PDF dell'articolo con un browser headless (Playwright/
   Chromium) puntato su una build locale del sito servita da un http
   server temporaneo su localhost -- non dipende dall'URL pubblico live
   (propagazione DNS, baseURL provvisorio vs definitivo).
2. Estrae i metadati dal front matter di
   content/biblioteca/<slug>/index.md (versione italiana, canonica):
   title, description, temi (mappati a label_it via data/topics.yaml per
   le keyword Zenodo).
3. Legge l'ORCID dell'autore "stamotenti" da data/authors.yaml.
4. Chiama l'API Zenodo (deposition classica: crea, carica il PDF nel
   bucket, imposta i metadati, esegue l'azione `publish` -- NON lascia
   una bozza).
5. Scrive doi/concept_doi/record_url/deposited_at nella voce
   corrispondente di data/zenodo-deposits.yaml.

Sandbox vs produzione: ogni voce ha un flag `sandbox` (bool). true ->
sandbox.zenodo.org, token ZENODO_SANDBOX_TOKEN; false -> zenodo.org,
token ZENODO_TOKEN. Stesso codice per entrambi, solo endpoint/token
cambiano -- vedi handoff, sezione "Sicurezza": un run riuscito su
sandbox e' un prerequisito non opzionale prima di abilitare una voce di
produzione per lo stesso slug.

Rischio noto, non eliminabile con un semplice retry (da documentare,
non da nascondere): se lo script si interrompe DOPO che la chiamata
`publish` e' andata a buon fine ma PRIMA di scrivere/committare il
registro, il DOI e' comunque stato creato in modo permanente su Zenodo,
ma data/zenodo-deposits.yaml continua a mostrare `doi: null` -- un run
successivo non lo saprebbe e proverebbe a ripubblicare, creando un
secondo DOI reale per lo stesso articolo. Per questo lo script fallisce
in modo rumoroso (non silenzioso) in quella finestra e NON scrive stato
parziale/ambiguo: in caso di fallimento dopo la pubblicazione, il
controllo va fatto a mano su Zenodo (cercare il deposito per titolo/data)
prima di rilanciare il job.

Uso:
    export ZENODO_TOKEN=...            # produzione (deposit:write + deposit:actions)
    export ZENODO_SANDBOX_TOKEN=...    # sandbox.zenodo.org (registrazione separata)
    python3 scripts/zenodo_deposit.py
    python3 scripts/zenodo_deposit.py --dry-run
        (--dry-run non chiama l'API Zenodo e non genera il PDF via
        browser: verifica solo parsing/metadati/payload, per validare
        la logica senza consumare un token -- stesso principio di
        scripts/translate-to-en.py)

Presuppone che il sito sia gia' buildato in ./public con baseURL sulla
radice (nessun sottopercorso: la generazione del PDF serve public/ da
un http server locale alla radice, un baseURL con sottopercorso -- come
quello del workflow interim GitHub Pages -- romperebbe i link assoluti,
stesso bug gia' corretto altrove per il deploy interim).
"""

from __future__ import annotations

import argparse
import datetime
import os
import subprocess
import sys
import time
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

import requests
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parent.parent
DEPOSITS_PATH = ROOT / "data" / "zenodo-deposits.yaml"
AUTHORS_PATH = ROOT / "data" / "authors.yaml"
TOPICS_PATH = ROOT / "data" / "topics.yaml"
PUBLIC_DIR = ROOT / "public"
PDF_OUT_DIR = ROOT / "zenodo-pdf"

# Costanti di metadato decise una volta sola (handoff 2026-09-22,
# registro-pubblicazioni.md v5) -- non riderivate per ogni deposito.
UPLOAD_TYPE = "other"
LICENSE_ID = "cc-by-nc-4.0"
LANGUAGE = "ita"
AUTHOR_NAME = "StamoTenti"
AUTHOR_ID = "stamotenti"

# Aggiornabile in futuro quando cambia il dominio -- nessuna correzione
# retroattiva automatica dei depositi gia' fatti (handoff, punto 3).
ARTICLE_BASE_URL = "https://pietrofabbri.github.io/stamotenti"

ZENODO_ENDPOINTS = {
    False: {  # produzione
        "api_base": "https://zenodo.org/api",
        "record_base": "https://zenodo.org/records",
        "token_env": "ZENODO_TOKEN",
    },
    True: {  # sandbox
        "api_base": "https://sandbox.zenodo.org/api",
        "record_base": "https://sandbox.zenodo.org/records",
        "token_env": "ZENODO_SANDBOX_TOKEN",
    },
}

HTTP_SERVER_PORT = 8123
HTTP_SERVER_STARTUP_TIMEOUT = 15


yaml_roundtrip = YAML()
yaml_roundtrip.preserve_quotes = True
# sequence=2/offset=0: "- slug:" a colonna 0, chiavi a colonna 2 -- stesso
# stile del resto del file (verificato con un round-trip di prova contro
# la formattazione scritta a mano).
yaml_roundtrip.indent(mapping=2, sequence=2, offset=0)


def _represent_none(representer, _data):
    # Default di ruamel.yaml per None e' uno scalare vuoto (es. "doi:"
    # invece di "doi: null") -- valido ma diverso dallo stile scritto a
    # mano in data/zenodo-deposits.yaml, verificato con un round-trip di
    # prova. "null" esplicito e' piu' leggibile in un diff di commit.
    return representer.represent_scalar("tag:yaml.org,2002:null", "null")


yaml_roundtrip.representer.add_representer(type(None), _represent_none)

yaml_safe = YAML(typ="safe")


def load_deposits():
    with DEPOSITS_PATH.open("r", encoding="utf-8") as f:
        return yaml_roundtrip.load(f)


def save_deposits(data):
    with DEPOSITS_PATH.open("w", encoding="utf-8") as f:
        yaml_roundtrip.dump(data, f)


def load_author_orcid(author_id: str) -> str:
    with AUTHORS_PATH.open("r", encoding="utf-8") as f:
        authors = yaml_safe.load(f)
    for entry in authors:
        if entry.get("id") == author_id:
            orcid = entry.get("orcid") or ""
            if not orcid:
                raise RuntimeError(
                    f"data/authors.yaml: voce '{author_id}' senza orcid -- "
                    f"deposito Zenodo richiede un ORCID valorizzato."
                )
            return orcid
    raise RuntimeError(f"data/authors.yaml: nessuna voce con id '{author_id}'")


def load_topic_labels() -> dict:
    with TOPICS_PATH.open("r", encoding="utf-8") as f:
        topics = yaml_safe.load(f)
    return {t["id"]: t.get("label_it", t["id"]) for t in (topics or [])}


def split_front_matter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("file senza front matter (deve iniziare con '---')")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("front matter non chiuso (manca il secondo '---')")
    return text[4:end], text[end + 5:]


def load_article_metadata(slug: str, topic_labels: dict) -> dict:
    md_path = ROOT / "content" / "biblioteca" / slug / "index.md"
    if not md_path.exists():
        raise RuntimeError(f"articolo non trovato: {md_path}")
    text = md_path.read_text(encoding="utf-8")
    front_matter_text, _ = split_front_matter(text)
    front_matter = yaml_safe.load(front_matter_text)

    title = front_matter.get("title")
    description = front_matter.get("description")
    temi = front_matter.get("temi") or []
    if not title or not description:
        raise RuntimeError(
            f"{md_path}: title/description mancanti nel front matter -- "
            f"richiesti per i metadati Zenodo."
        )
    keywords = [topic_labels.get(t, t) for t in temi]
    return {"title": title, "description": description, "keywords": keywords}


def start_local_server() -> subprocess.Popen:
    if not PUBLIC_DIR.exists():
        raise RuntimeError(
            f"{PUBLIC_DIR} non esiste -- buildare il sito (hugo --minify, "
            f"baseURL di default senza sottopercorso) prima di generare il PDF."
        )
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(HTTP_SERVER_PORT), "--directory", str(PUBLIC_DIR)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    deadline = time.monotonic() + HTTP_SERVER_STARTUP_TIMEOUT
    url = f"http://localhost:{HTTP_SERVER_PORT}/"
    while time.monotonic() < deadline:
        try:
            requests.get(url, timeout=1)
            return proc
        except requests.exceptions.ConnectionError:
            time.sleep(0.3)
    proc.terminate()
    raise RuntimeError(f"http.server locale non pronto entro {HTTP_SERVER_STARTUP_TIMEOUT}s ({url})")


def generate_pdf(slug: str) -> Path:
    from playwright.sync_api import sync_playwright

    PDF_OUT_DIR.mkdir(exist_ok=True)
    pdf_path = PDF_OUT_DIR / f"{slug}.pdf"
    url = f"http://localhost:{HTTP_SERVER_PORT}/biblioteca/{slug}/"

    server_proc = start_local_server()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            page.pdf(path=str(pdf_path), format="A4", print_background=True)
            browser.close()
    finally:
        server_proc.terminate()
        server_proc.wait(timeout=5)

    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        raise RuntimeError(f"PDF non generato o vuoto: {pdf_path}")
    return pdf_path


def build_zenodo_metadata(article_meta: dict, orcid: str, slug: str) -> dict:
    return {
        "upload_type": UPLOAD_TYPE,
        "title": article_meta["title"],
        "description": article_meta["description"],
        "creators": [{"name": AUTHOR_NAME, "orcid": orcid}],
        "keywords": article_meta["keywords"],
        "license": LICENSE_ID,
        "language": LANGUAGE,
        "publication_date": datetime.date.today().isoformat(),
        "related_identifiers": [
            {
                "identifier": f"{ARTICLE_BASE_URL}/biblioteca/{slug}/",
                "relation": "isIdenticalTo",
                "resource_type": "publication-article",
            }
        ],
    }


def zenodo_publish(pdf_path: Path, metadata: dict, sandbox: bool) -> dict:
    endpoint = ZENODO_ENDPOINTS[sandbox]
    token = os.environ.get(endpoint["token_env"])
    if not token:
        raise RuntimeError(
            f"{endpoint['token_env']} mancante nell'ambiente -- richiesto per "
            f"depositare su {'sandbox' if sandbox else 'produzione'}."
        )
    headers = {"Authorization": f"Bearer {token}"}
    api_base = endpoint["api_base"]

    # 1. Crea la deposition (bozza).
    resp = requests.post(f"{api_base}/deposit/depositions", json={}, headers=headers, timeout=30)
    resp.raise_for_status()
    deposition = resp.json()
    deposition_id = deposition["id"]
    bucket_url = deposition["links"]["bucket"]

    # 2. Carica il PDF nel bucket (API file moderna, non la /files legacy).
    with pdf_path.open("rb") as f:
        resp = requests.put(f"{bucket_url}/{pdf_path.name}", data=f, headers=headers, timeout=120)
    resp.raise_for_status()

    # 3. Imposta i metadati.
    resp = requests.put(
        f"{api_base}/deposit/depositions/{deposition_id}",
        json={"metadata": metadata},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()

    # 4. Pubblica -- azione irreversibile, nessuna bozza lasciata indietro.
    resp = requests.post(
        f"{api_base}/deposit/depositions/{deposition_id}/actions/publish",
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    published = resp.json()

    doi = published.get("doi")
    if not doi:
        # Non scrivere mai un risultato ambiguo nel registro: la
        # pubblicazione potrebbe essere comunque avvenuta (vedi rischio
        # noto nel docstring del modulo) -- fallire rumorosamente e
        # lasciare il controllo a un umano su Zenodo direttamente.
        raise RuntimeError(
            f"Risposta Zenodo senza 'doi' dopo publish (deposition {deposition_id}): "
            f"{published!r} -- verificare a mano su {endpoint['record_base']}/{deposition_id} "
            f"prima di rilanciare il job."
        )

    return {
        "doi": doi,
        "concept_doi": published.get("conceptdoi"),
        "record_url": published.get("links", {}).get("record_html")
        or f"{endpoint['record_base']}/{deposition_id}",
    }


def process_entry(entry, dry_run: bool, topic_labels: dict):
    slug = entry["slug"]
    sandbox = bool(entry.get("sandbox", False))
    label = "sandbox" if sandbox else "PRODUZIONE"

    article_meta = load_article_metadata(slug, topic_labels)
    orcid = load_author_orcid(AUTHOR_ID)
    metadata = build_zenodo_metadata(article_meta, orcid, slug)

    if dry_run:
        print(f"[dry-run] {slug} ({label}): metadati costruiti, nessuna chiamata API/PDF.")
        print(metadata)
        return

    pdf_path = generate_pdf(slug)
    print(f"{slug} ({label}): PDF generato -> {pdf_path}")

    result = zenodo_publish(pdf_path, metadata, sandbox)
    print(f"{slug} ({label}): pubblicato -- DOI {result['doi']}")

    entry["doi"] = result["doi"]
    entry["concept_doi"] = result["concept_doi"]
    entry["record_url"] = result["record_url"]
    entry["deposited_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Non genera il PDF ne' chiama l'API Zenodo: verifica solo parsing e payload dei metadati.",
    )
    args = parser.parse_args()

    deposits = load_deposits()
    topic_labels = load_topic_labels()

    pending = [e for e in deposits if e.get("approved") and not e.get("doi")]
    if not pending:
        print("Nessuna voce approvata in attesa di deposito (idempotente: nulla da fare).")
        return

    any_processed = False
    for entry in pending:
        process_entry(entry, args.dry_run, topic_labels)
        any_processed = any_processed or not args.dry_run

    if any_processed:
        save_deposits(deposits)
        print(f"{DEPOSITS_PATH} aggiornato.")


if __name__ == "__main__":
    main()
