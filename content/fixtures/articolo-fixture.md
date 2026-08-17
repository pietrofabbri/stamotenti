---
title: "Articolo di Fixture"
description: "Articolo tecnico che dimostra il modello dei contenuti (DECISIONS/DR-08). Non un contenuto editoriale reale."
authors:
  - fixture-autore
sources:
  - fixture-fonte
sotto_area: SA-1-1
temi:
  - fixture-tema-tecnico
---

# Articolo di Fixture

Questo articolo è un contenuto tecnico di dimostrazione (vedi `DECISIONS/DR-08-content-fixture-system-proposal.md`), non un contenuto editoriale reale. Dimostra, con dati dedicati e non reali, il funzionamento delle entità del modello dei contenuti.

Referenzia un autore di fixture, una fonte di fixture con relativa citazione {{< cite "fixture-fonte" >}}, una sotto-area reale (`SA-1-1`, riferimento a un valore già approvato in `DECISIONS/DR-03-macroarea-sottoarea-model.md`, non una nuova classificazione inventata) e un tema tecnico di fixture (`fixture-tema-tecnico`, eccezione esplicitamente autorizzata da DR-08 a "zero temi reali" di DR-04).

## Collegamento a Media

DR-01 (anche esteso da DR-06) non prevede un campo diretto Article → Media nel front matter (domanda aperta, vedi `PHASE-2-PLAN.md`). Questo articolo referenzia quindi `fixture-media` (`data/media.yaml`) solo indirettamente: `fixture-media` ha un campo opzionale `source_id: fixture-fonte` (schema approvato in `DECISIONS/DR-07-media-infrastructure-proposal.md`), e questo articolo referenzia `fixture-fonte` tramite il proprio campo `sources`. La catena Article → Source → Media è quindi dimostrata; un collegamento diretto Article → Media resta non dimostrato, perché non esiste ancora un campo approvato per farlo.

Lo shortcode `figure` (A3, `layouts/shortcodes/figure.html`) referenzia lo stesso `fixture-media` solo concettualmente, tramite un `src` esplicitamente marcato come placeholder — nessun file reale è coinvolto, coerente con `fixture-media` stessa (nessun `storage_location`/`url` in `data/media.yaml`):

{{< figure src="https://example.org/fixture-media-placeholder.svg" alt="Immagine di fixture (dato tecnico, non un file reale) — placeholder concettuale per la voce fixture-media in data/media.yaml" caption="Didascalia di fixture, a scopo dimostrativo." >}}
