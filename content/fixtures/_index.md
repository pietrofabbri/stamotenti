---
title: "Fixture tecniche"
description: "Contenuti tecnici di dimostrazione (DECISIONS/DR-08). Non contenuto editoriale reale."
cascade:
  sitemap:
    disable: true
  outputs:
    - html
  build:
    list: local
---

# Fixture tecniche

Questa sezione contiene contenuti tecnici di dimostrazione, non contenuto editoriale reale.

Sono usati per verificare che il modello dei contenuti (Article, Author, Source, Citation, Topic, Macroarea, Sotto-area, Media, Translation) funzioni end-to-end, come richiesto da `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` (Fase 2, "Content fixture system").

Vedi `DECISIONS/DR-08-content-fixture-system-proposal.md` per la decisione che autorizza questa sezione e per la motivazione di ogni scelta tecnica.

Queste pagine sono escluse dalla sitemap (cascade `sitemap.disable`) e marcate `noindex` (`layouts/partials/seo.html`).

**Aggiornamento (2026-08-19, audit Gate 2)**: `sitemap.disable` non copre l'output RSS di Hugo — verificato che, senza ulteriori accorgimenti, l'articolo di fixture compariva sia nel feed RSS proprio di questa sezione sia nel feed RSS principale del sito (`/index.xml`), in tensione con la regola del roadmap "le fixture devono essere separate". Corretto con `cascade.outputs: [html]` (nessun output RSS per questa sezione) e `cascade.build.list: local` (le pagine restano visibili nell'elenco locale di questa sezione, come sopra, ma non compaiono più nelle collezioni globali come il feed RSS della home).
