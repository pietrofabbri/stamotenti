#!/usr/bin/env python3
"""Allineamento IT->EN via l'API di DeepL (handoff-allineamento-en-deepl-
2026-09-10.md): traduzione automatica, non manuale/LLM, per esplicita
richiesta del proprietario, pensata come passo riusabile per ogni
articolo/voce futura (non solo per questo giro).

Cosa fa:
- Legge un file Markdown IT (front matter + corpo).
- Nel front matter traduce SOLO i campi testuali `title`/`description`;
  ogni altro campo (authors, sources, temi, sotto_area, id, ecc.) resta
  invariato byte per byte, riga per riga -- non e' testo, e' un
  riferimento a un vocabolario controllato o a un identificativo stabile.
- Nel corpo protegge da DeepL, con un placeholder non traducibile:
    - ogni shortcode Hugo ({{< cite "..." >}}, {{< audio-pratica ... >}},
      {{< invito-contatto >}}, {{< accademico-inizio >}}/-fine, ecc.);
    - il target di ogni link Markdown ([testo](target)) -- solo il testo
      del link viene tradotto, mai l'URL.
  Dopo la traduzione, i target dei link interni assoluti (che iniziano per
  "/", esclusi quelli gia' sotto "/en/" e i "mailto:") vengono ri-scritti
  con il prefisso "/en" -- coerente con hugo.toml
  (defaultContentLanguageInSubdir = false, IT senza prefisso, EN sotto
  /en/). Verificato nel routing reale in una build di prova, non solo
  dedotto da config -- vedi il commento su INTERNAL_LINK_PREFIXES sotto.
- Scrive il file di output con lo stesso nome ma suffisso di lingua Hugo
  (_index.md -> _index.en.md, pagina.md -> pagina.en.md).

Cosa NON fa (deliberatamente, fuori scope di questo script):
- Non gestisce le citazioni dirette da fonte primaria (es. i passi del
  Cetana Sutta, le citazioni di Gethin) in modo speciale: DeepL le traduce
  come il resto del testo italiano. Se il testo IT include una citazione
  diretta gia' tradotta altrove da una fonte primaria in inglese (come nel
  caso dell'articolo "Dalla tradizione al secolare"), la ri-traduzione
  meccanica del parafrasato italiano NON riproduce necessariamente la
  stessa dicitura della traduzione accademica originale -- e' una
  ri-traduzione di una traduzione, non un recupero della fonte. Prima di
  usare l'output su un file con citazioni dirette, un controllo umano
  mirato solo su quelle frasi resta necessario: lo script non lo fa da
  solo, e non e' un compito che DeepL possa risolvere.

Uso:
    export DEEPL_API_KEY=...   # o .env nella root del progetto (mai in git)
    python3 scripts/translate-to-en.py content/temi/upaya/_index.md [altri file...]
    python3 scripts/translate-to-en.py --dry-run content/temi/upaya/_index.md
        (--dry-run non chiama l'API: verifica solo che protezione/
        ripristino di shortcode e link funzionino, per validare la
        logica senza consumare quota -- stesso principio di verifica in
        isolamento gia' usato altrove nel progetto prima di toccare
        contenuto reale)

Richiede DEEPL_API_KEY nell'ambiente (o in un .env alla root del progetto,
mai committato: .gitignore lo esclude gia').
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
except ImportError:
    pass

import requests

DEEPL_ENDPOINT = "https://api-free.deepl.com/v2/translate"
SOURCE_LANG = "IT"
# EN-US, non EN-GB: verificato per grep sui file EN gia' esistenti
# (spelling "organization"/"program"/"practiced", non "organisation"/
# "programme"/"practised" -- convenzione americana gia' in uso nel sito).
TARGET_LANG = "EN-US"

# Prefissi di path interni del sito (content/, non data/): un link a uno di
# questi, nella versione EN, deve puntare sotto /en/. "/en/" stesso escluso
# (gia' corretto se capita di comparire pre-tradotto). Percorsi assoluti
# senza dominio, coerenti con come i link sono scritti in questo codebase
# (mai URL assoluti con https://, sempre path relativi al sito).
INTERNAL_LINK_PREFIXES = (
    "/temi/",
    "/biblioteca/",
    "/il-progetto/",
    "/no-fuochi/",
    "/privacy/",
)

SHORTCODE_RE = re.compile(r"\{\{[<%].*?[%>]\}\}")
# Solo il target del link (tra parentesi tonde), non il testo tra quadre.
LINK_TARGET_RE = re.compile(r"(?<=\]\()([^)\s]+)(?=\))")

# Placeholder deliberatamente fatto di caratteri rari in prosa italiana/
# inglese (parentesi quadre matematiche unicode, non usate altrove in
# questo codebase) + un indice numerico: DeepL tratta token sconosciuti
# come testo non-lessicale e tende a lasciarli invariati, ma il controllo
# esplicito dopo la traduzione (vedi _restore) non si affida a questo,
# verifica sempre che il numero di placeholder attesi torni.
PLACEHOLDER_TEMPLATE = "⟦{tag}{index}⟧"
SHORTCODE_TAG = "SC"
LINK_TAG = "LK"


def _protect(text, pattern, tag):
    matches = []

    def _sub(m):
        matches.append(m.group(0))
        return PLACEHOLDER_TEMPLATE.format(tag=tag, index=len(matches) - 1)

    protected = pattern.sub(_sub, text)
    return protected, matches


def _restore(text, matches, tag, rewrite=None):
    for i, original in enumerate(matches):
        token = PLACEHOLDER_TEMPLATE.format(tag=tag, index=i)
        value = rewrite(original) if rewrite else original
        if token not in text:
            raise RuntimeError(
                f"placeholder {token} mancante nel testo tradotto: la "
                f"traduzione ha probabilmente alterato o rimosso un "
                f"segmento protetto ({tag}). Non scrivo output parziale/"
                f"corrotto -- controllare manualmente."
            )
        text = text.replace(token, value, 1)
    return text


def _rewrite_internal_link(url: str) -> str:
    if url.startswith("mailto:") or url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("/en/"):
        return url
    if url.startswith(INTERNAL_LINK_PREFIXES) or url == "/":
        return "/en" + url
    return url


def _deepl_translate(text: str, api_key: str) -> str:
    if not text.strip():
        return text
    response = requests.post(
        DEEPL_ENDPOINT,
        headers={"Authorization": f"DeepL-Auth-Key {api_key}"},
        data={
            "text": text,
            "source_lang": SOURCE_LANG,
            "target_lang": TARGET_LANG,
            # "text" (non "xml"): il markdown non e' XML, la protezione
            # di shortcode/link e' gestita a monte con i placeholder,
            # non delegata a ignore_tags/tag_handling di DeepL.
        },
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    return data["translations"][0]["text"]


def translate_body(body: str, api_key: str | None, dry_run: bool) -> str:
    protected, shortcodes = _protect(body, SHORTCODE_RE, SHORTCODE_TAG)
    protected, links = _protect(protected, LINK_TARGET_RE, LINK_TAG)

    if dry_run:
        translated = protected  # nessuna chiamata API: verifica solo placeholder
    else:
        translated = _deepl_translate(protected, api_key)

    translated = _restore(translated, shortcodes, SHORTCODE_TAG)
    translated = _restore(translated, links, LINK_TAG, rewrite=_rewrite_internal_link)
    return translated


FRONT_MATTER_FIELD_RE = re.compile(r'^(title|description):\s*"(.*)"\s*$')


def translate_front_matter(front_matter_lines, api_key, dry_run):
    out = []
    for line in front_matter_lines:
        m = FRONT_MATTER_FIELD_RE.match(line)
        if not m:
            out.append(line)
            continue
        field, value = m.group(1), m.group(2)
        if dry_run:
            translated_value = value
        else:
            translated_value = _deepl_translate(value, api_key)
        # Virgolette doppie escapate se DeepL ne restituisse (raro per
        # frasi brevi come title/description, ma non ci si affida a questo).
        translated_value = translated_value.replace('"', '\\"')
        out.append(f'{field}: "{translated_value}"')
    return out


def split_front_matter(text: str):
    if not text.startswith("---\n"):
        raise ValueError("file senza front matter (deve iniziare con '---')")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("front matter non chiuso (manca il secondo '---')")
    front_matter = text[4:end].split("\n")
    body = text[end + 5 :]
    return front_matter, body


def en_path_for(it_path: Path) -> Path:
    if it_path.stem.endswith(".en"):
        raise ValueError(f"{it_path} sembra gia' un file EN, non lo tratto come sorgente IT")
    return it_path.with_name(it_path.stem + ".en" + it_path.suffix)


def translate_file(it_path: Path, api_key, dry_run: bool) -> Path:
    text = it_path.read_text(encoding="utf-8")
    front_matter_lines, body = split_front_matter(text)

    translated_front_matter = translate_front_matter(front_matter_lines, api_key, dry_run)
    translated_body = translate_body(body, api_key, dry_run)

    out_path = en_path_for(it_path)
    out_text = "---\n" + "\n".join(translated_front_matter) + "\n---\n" + translated_body
    out_path.write_text(out_text, encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="+", help="File Markdown IT da tradurre in EN")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Non chiama l'API DeepL: verifica solo la protezione/ripristino di shortcode e link",
    )
    args = parser.parse_args()

    api_key = os.environ.get("DEEPL_API_KEY")
    if not args.dry_run and not api_key:
        parser.error(
            "DEEPL_API_KEY mancante (variabile d'ambiente o .env nella root "
            "del progetto). Usa --dry-run per verificare la logica senza chiave."
        )

    for file_arg in args.files:
        it_path = Path(file_arg)
        if not it_path.exists():
            parser.error(f"file non trovato: {it_path}")
        out_path = translate_file(it_path, api_key, args.dry_run)
        label = "[dry-run] " if args.dry_run else ""
        print(f"{label}{it_path} -> {out_path}")


if __name__ == "__main__":
    main()
