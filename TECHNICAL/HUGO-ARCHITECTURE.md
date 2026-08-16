# StamoTenti — Hugo Architecture

## Scopo

Descrive l'implementazione tecnica corrente del sito Hugo.
Non introduce requisiti editoriali nuovi.

## Struttura

L'implementazione corrente utilizza:

- hugo.toml;
- content/;
- data/;
- i18n/;
- layouts/;
- assets/;
- static/;
- archetypes/.

## Flusso

Il flusso principale è:

sorgenti Markdown e dati
→ Hugo
→ template
→ output statico
→ public/

## Configurazione

La configurazione principale è in `hugo.toml`.

Sono configurate almeno le lingue:

- italiano;
- inglese.

L'italiano è la lingua predefinita.

## Contenuti

I contenuti del sito sono conservati in `content/`.

## Dati

I dati strutturati sono conservati in `data/`.

## Rendering

Il rendering è gestito dai template in `layouts/`.

## Principio

L'architettura deve utilizzare le funzionalità native di Hugo quando sono
sufficienti e non introdurre servizi o backend non necessari.
