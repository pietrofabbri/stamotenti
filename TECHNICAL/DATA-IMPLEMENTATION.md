# StamoTenti — Data Implementation

## Scopo

Descrive i dati strutturati presenti nella directory `data/`.

## Autori

`data/authors.yaml` contiene attualmente campi quali:

- name;
- full_name;
- affiliation;
- orcid.

Gli identificativi degli autori devono rimanere coerenti con AUTHOR-SPEC.md.

## Fonti

`data/sources.yaml` contiene attualmente campi quali:

- type;
- title;
- authors;
- year;
- journal;
- publisher;
- doi;
- isbn;
- url;
- file.

Le fonti devono rispettare SOURCE-SPEC.md.

## Hugo data

La directory `data/` costituisce una sorgente di dati strutturati utilizzabile
dai template Hugo.

## Evoluzione

L'aggiunta di nuovi campi deve derivare da esigenze reali del modello o
dell'implementazione.

I dati non devono essere duplicati inutilmente nei contenuti.
