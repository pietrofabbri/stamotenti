# StamoTenti — Content Implementation

## Scopo

Descrive come il modello dei contenuti viene rappresentato nell'implementazione
Hugo corrente.

## Stato corrente

Il repository contiene attualmente:

- `content/_index.md`;
- `content/content.md`;
- `content/biblioteca/meditazione.md`.

## Front matter

Il contenuto corrente utilizza campi come:

- title;
- description;
- date;
- draft;
- authors;
- sources;
- tags;
- temi.

I campi effettivamente utilizzati possono evolvere con il modello editoriale.

## Relazione con il modello

CONTENT-MODEL.md e ARTICLE-SPEC.md definiscono il modello concettuale.

Questo documento descrive soltanto la sua rappresentazione tecnica corrente.

## Regola

Un campo deve essere introdotto nell'implementazione quando esiste una
necessità prevista dal modello o dal workflow.

La presenza di un campo nel codice non costituisce automaticamente una nuova
regola editoriale.
