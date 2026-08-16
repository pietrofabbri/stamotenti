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

Il provider e il workflow definitivo di deploy non sono ancora fissati in
questo documento.

La scelta dovrà essere compatibile con:

- versionamento Git;
- build riproducibile;
- possibilità di rollback;
- costi sostenibili;
- sostituibilità del provider.

## Regola

Non introdurre una pipeline di deploy più complessa della necessità reale del
progetto.
