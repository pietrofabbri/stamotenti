# StamoTenti — Deployment

## Scopo

Descrive il percorso tecnico di build e pubblicazione.

## Stato corrente

La build locale è verificata con Hugo.

La directory `public/` viene generata dalla build e non costituisce la fonte
primaria dei contenuti.

## Build

Il processo corrente è:

repository
→ Hugo build
→ public/

## Produzione

Il provider di hosting è GitHub Pages (deciso dal proprietario, registrato
in `data/site.yaml` il 2026-08-29 — citato dalla pagina Privacy). Questo
fissa il **provider**, non ancora il **workflow** di deploy (CI, build
automatica, rollback): quello resta da definire.

La scelta del workflow dovrà essere compatibile con:

- versionamento Git;
- build riproducibile;
- possibilità di rollback;
- costi sostenibili;
- sostituibilità del provider.

## Regola

Non introdurre una pipeline di deploy più complessa della necessità reale del
progetto.
