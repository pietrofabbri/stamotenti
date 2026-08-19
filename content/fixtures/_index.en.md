---
title: "Technical fixtures"
description: "Technical demonstration content (DECISIONS/DR-08). Not real editorial content."
cascade:
  sitemap:
    disable: true
  outputs:
    - html
  build:
    list: local
---

# Technical fixtures

This section contains technical demonstration content, not real editorial content.

It is used to verify that the content model (Article, Author, Source, Citation, Topic, Macroarea, Sotto-area, Media, Translation) works end-to-end, as required by `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` (Phase 2, "Content fixture system").

See `DECISIONS/DR-08-content-fixture-system-proposal.md` for the decision that authorizes this section and the reasoning behind each technical choice.

These pages are excluded from the sitemap (`sitemap.disable` cascade) and marked `noindex` (`layouts/partials/seo.html`).

Note: this section index (`content/fixtures/_index.en.md`) restates the same `cascade` block as the Italian one. This is required, not redundant — verified empirically in an isolated fixture site before touching this repository: without a language-specific `_index.en.md` carrying its own `cascade`, Hugo does not propagate the Italian section's cascade to this language's page tree, and the English fixture pages would still appear in `en/sitemap.xml`.

**Update (2026-08-19, Gate 2 audit)**: the same applies to `cascade.outputs`/`cascade.build.list`, added below to keep the fixture article out of RSS feeds (`sitemap.disable` alone does not affect Hugo's RSS output) — verified this needs restating here too, not just on the Italian `_index.md`, for the same cross-language-cascade reason.
