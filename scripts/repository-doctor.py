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
# 12. Final report
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
