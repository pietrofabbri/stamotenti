#!/usr/bin/env python3

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent

ERRORS = []
WARNINGS = []


def ok(label, message=""):
    print(f"OK      {label}" + (f": {message}" if message else ""))


def warn(label, message=""):
    WARNINGS.append(label)
    print(f"WARN    {label}" + (f": {message}" if message else ""))


def error(label, message=""):
    ERRORS.append(label)
    print(f"ERROR   {label}" + (f": {message}" if message else ""))


def run(cmd):
    return subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


print("=" * 72)
print("STAMOTENTI — REPOSITORY DOCTOR")
print("=" * 72)

# ---------------------------------------------------------------------
# 1. Git
# ---------------------------------------------------------------------

print("\n[1] GIT")

r = run(["git", "status", "--short"])

if r.returncode == 0:
    if r.stdout.strip():
        warn("Git working tree", "modifiche presenti")
        print(r.stdout.rstrip())
    else:
        ok("Git working tree", "clean")
else:
    error("Git", r.stderr.strip())

# ---------------------------------------------------------------------
# 2. Core documentation
# ---------------------------------------------------------------------

print("\n[2] CORE DOCUMENTATION")

required = [
    "CLAUDE.md",
    "CLAUDE-CODE-DEVELOPMENT-ROADMAP.md",
    "README.md",
    "TO-BE.md",
    "CONTENT-MODEL.md",
    "PROJECT-MAP.md",
    "DEPENDENCY-MAP.md",
    "DESIGN-SPEC.md",
    "APPROVAL-SPEC.md",
]

for name in required:
    p = ROOT / name
    if p.exists():
        ok(name)
    else:
        error(name, "mancante")

# ---------------------------------------------------------------------
# 3. Summary layer
# ---------------------------------------------------------------------

print("\n[3] SUMMARY")

summary_dir = ROOT / "SUMMARY"

expected_summary = [
    "00-CONSTITUTION-SUMMARY.md",
    "01-CONTENT-SUMMARY.md",
    "02-AGENTS-WORKFLOW-SUMMARY.md",
    "03-SOURCES-MEDIA-SUMMARY.md",
    "04-PUBLICATION-RISK-SUMMARY.md",
    "05-QUALITY-OPERATIONS-SUMMARY.md",
]

if not summary_dir.exists():
    error("SUMMARY", "directory mancante")
else:
    for name in expected_summary:
        if (summary_dir / name).exists():
            ok(f"SUMMARY/{name}")
        else:
            error(f"SUMMARY/{name}", "mancante")

# ---------------------------------------------------------------------
# 4. Technical documentation
# ---------------------------------------------------------------------

print("\n[4] TECHNICAL")

technical_dir = ROOT / "TECHNICAL"

expected_technical = [
    "HUGO-ARCHITECTURE.md",
    "CONTENT-IMPLEMENTATION.md",
    "DATA-IMPLEMENTATION.md",
    "TEMPLATE-AND-RENDERING.md",
    "DEPLOYMENT.md",
]

if not technical_dir.exists():
    error("TECHNICAL", "directory mancante")
else:
    for name in expected_technical:
        if (technical_dir / name).exists():
            ok(f"TECHNICAL/{name}")
        else:
            error(f"TECHNICAL/{name}", "mancante")

# ---------------------------------------------------------------------
# 5. Hugo
# ---------------------------------------------------------------------

print("\n[5] HUGO")

hugo = run(["hugo", "version"])

if hugo.returncode == 0:
    ok("Hugo", hugo.stdout.strip())
else:
    error("Hugo", hugo.stderr.strip())

# ---------------------------------------------------------------------
# 6. Hugo build
# ---------------------------------------------------------------------

print("\n[6] BUILD")

build = run([
    "hugo",
    "build",
    "--gc",
    "--minify",
    "--printPathWarnings",
    "--printUnusedTemplates",
])

if build.returncode == 0:
    ok("Hugo build")
else:
    error("Hugo build", build.stderr.strip() or build.stdout.strip())

# ---------------------------------------------------------------------
# 7. Markdown hygiene
# ---------------------------------------------------------------------

print("\n[7] MARKDOWN HYGIENE")

md_files = sorted(ROOT.rglob("*.md"))

for p in md_files:
    text = p.read_text()

    fences = len(re.findall(r"(?m)^```", text))
    if fences % 2:
        error(
            f"{p.relative_to(ROOT)}",
            "fence Markdown non bilanciate",
        )
        continue

    if r"\n" in text:
        error(
            f"{p.relative_to(ROOT)}",
            "sequenza letterale \\\\n",
        )
        continue

    if re.search(r"[ \t]+$", text, re.MULTILINE):
        error(
            f"{p.relative_to(ROOT)}",
            "trailing whitespace",
        )
        continue

ok("Markdown hygiene", f"{len(md_files)} file analizzati")

# ---------------------------------------------------------------------
# 8. Required Hugo directories
# ---------------------------------------------------------------------

print("\n[8] HUGO STRUCTURE")

for name in [
    "archetypes",
    "assets",
    "content",
    "data",
    "i18n",
    "layouts",
    "static",
]:
    if (ROOT / name).exists():
        ok(name)
    else:
        warn(name, "directory assente")

# ---------------------------------------------------------------------
# 9. Data files
# ---------------------------------------------------------------------

print("\n[9] DATA")

for name in [
    "data/authors.yaml",
    "data/sources.yaml",
]:
    if (ROOT / name).exists():
        ok(name)
    else:
        warn(name, "file assente")

# ---------------------------------------------------------------------
# 10. Content inventory
# ---------------------------------------------------------------------

print("\n[10] CONTENT")

content_files = sorted((ROOT / "content").rglob("*.md"))

ok("Content inventory", f"{len(content_files)} file")

for p in content_files:
    print(f"        {p.relative_to(ROOT)}")

# ---------------------------------------------------------------------
# 11. Multilingual baseline
# ---------------------------------------------------------------------

print("\n[11] MULTILINGUAL")

config = ROOT / "hugo.toml"

if config.exists():
    text = config.read_text()

    if re.search(r"\[languages\.it\]", text):
        ok("Italian language configuration")
    else:
        warn("Italian language configuration")

    if re.search(r"\[languages\.en\]", text):
        ok("English language configuration")
    else:
        warn("English language configuration")

    translated = [
        p for p in content_files
        if re.search(r"\.(en|it|en-us|it-it)\.md$", p.name, re.I)
    ]

    if translated:
        ok("Translated content", f"{len(translated)} file")
    else:
        warn(
            "Translated content",
            "nessun contenuto tradotto rilevato",
        )
else:
    error("hugo.toml", "mancante")

# ---------------------------------------------------------------------
# 12. Cross-reference integrity (authors/sources referenced by content)
# ---------------------------------------------------------------------

print("\n[12] CROSS-REFERENCE INTEGRITY")


def extract_data_ids(data_file):
    """Extract top-level `id: <value>` entries from a flat data/*.yaml list."""
    if not data_file.exists():
        return set()
    text = data_file.read_text()
    return set(re.findall(r'(?m)^-\s+id:\s*"?([\w.-]+)"?\s*$', text))


def extract_front_matter(md_file):
    text = md_file.read_text()
    m = re.match(r"(?s)^---\n(.*?)\n---\n", text)
    return m.group(1) if m else ""


def extract_list_refs(front_matter, key):
    """Extract id values listed under `key:` in a simple flat front matter block."""
    refs = []
    in_key = False
    for line in front_matter.splitlines():
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            in_key = True
            continue
        if in_key:
            item = re.match(r"^\s+-\s+(\S+)\s*$", line)
            if item:
                refs.append(item.group(1))
                continue
            if line.strip() == "":
                continue
            in_key = False
    return refs


author_ids = extract_data_ids(ROOT / "data/authors.yaml")
source_ids = extract_data_ids(ROOT / "data/sources.yaml")

referenced_authors = set()
referenced_sources = set()
broken_refs = 0

for p in content_files:
    front_matter = extract_front_matter(p)

    for ref in extract_list_refs(front_matter, "authors"):
        referenced_authors.add(ref)
        if ref not in author_ids:
            error(
                f"{p.relative_to(ROOT)}",
                f"autore referenziato non trovato in data/authors.yaml: {ref}",
            )
            broken_refs += 1

    for ref in extract_list_refs(front_matter, "sources"):
        referenced_sources.add(ref)
        if ref not in source_ids:
            error(
                f"{p.relative_to(ROOT)}",
                f"fonte referenziata non trovata in data/sources.yaml: {ref}",
            )
            broken_refs += 1

if broken_refs == 0:
    ok(
        "Cross-reference integrity",
        "tutti gli id di autori/fonti referenziati nei contenuti esistono",
    )

unused_authors = sorted(author_ids - referenced_authors)
unused_sources = sorted(source_ids - referenced_sources)

if unused_authors:
    warn("Autori non referenziati da alcun contenuto", ", ".join(unused_authors))

if unused_sources:
    warn("Fonti non referenziate da alcun contenuto", ", ".join(unused_sources))

# ---------------------------------------------------------------------
# 13. Static assets: large files
# ---------------------------------------------------------------------

print("\n[13] STATIC ASSETS")

LARGE_FILE_THRESHOLD_BYTES = 500 * 1024  # informativo, non bloccante

static_dir = ROOT / "static"
large_files = []

if static_dir.exists():
    for p in sorted(static_dir.rglob("*")):
        if p.is_file() and p.stat().st_size > LARGE_FILE_THRESHOLD_BYTES:
            large_files.append(p)

if large_files:
    for p in large_files:
        size_kb = p.stat().st_size / 1024
        warn(
            f"{p.relative_to(ROOT)}",
            f"{size_kb:.0f} KB — verificare classificazione (licenza/visibilità) "
            "secondo MEDIA-SPEC.md/BACKUP-SPEC.md",
        )
else:
    ok("Static assets", "nessun file di grandi dimensioni rilevato")

# ---------------------------------------------------------------------
# 14. Source file provenance (unverified real file attached to a fixture)
# ---------------------------------------------------------------------

print("\n[14] SOURCE FILE PROVENANCE")


def extract_source_entries(data_file):
    """Extract id/file/doi/isbn/url from each top-level entry of a flat
    data/sources.yaml-style list. Best-effort, not a full YAML parser."""
    if not data_file.exists():
        return []
    text = data_file.read_text()
    blocks = re.split(r"(?m)^-\s+id:", text)[1:]
    entries = []
    for block in blocks:
        m_id = re.match(r'\s*"?([\w.-]+)"?', block)
        entry = {"id": m_id.group(1) if m_id else "?"}
        for key in ("file", "doi", "isbn", "url"):
            m = re.search(rf'(?m)^\s+{key}:\s*"?([^"\n]*?)"?\s*$', block)
            if m and m.group(1).strip():
                entry[key] = m.group(1).strip()
        entries.append(entry)
    return entries


source_entries = extract_source_entries(ROOT / "data/sources.yaml")
provenance_warnings = 0

for entry in source_entries:
    file_field = entry.get("file")
    if not file_field:
        continue
    if entry.get("doi") or entry.get("isbn") or entry.get("url"):
        continue
    warn(
        f"{entry['id']}",
        f"file reale allegato ({file_field}) ma nessun doi/isbn/url — "
        "possibile fixture sintetica con file reale per errore; "
        "verificare i diritti di redistribuzione prima di considerarlo "
        "pubblicabile",
    )
    provenance_warnings += 1

if provenance_warnings == 0:
    ok(
        "Source file provenance",
        "nessuna fonte con file allegato priva di doi/isbn/url",
    )

# ---------------------------------------------------------------------
# 15. Final report
# ---------------------------------------------------------------------

print("\n" + "=" * 72)
print("DOCTOR RESULT")
print("=" * 72)

print(f"ERRORS : {len(ERRORS)}")
print(f"WARNINGS: {len(WARNINGS)}")

if ERRORS:
    print("RESULT : FAIL")
    sys.exit(1)

print("RESULT : PASS")

if WARNINGS:
    print("NOTE   : esistono warning non bloccanti")
