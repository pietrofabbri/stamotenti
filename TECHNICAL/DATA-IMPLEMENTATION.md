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

## Dati organizzativi del sito

`data/site.yaml` (aggiunto 2026-08-29) contiene titolare del trattamento,
hosting, analytics, donazioni (Ko-fi) e contatti — campi consultati da
`content/privacy/_index.md` (tramite lo shortcode `sitedata.html`) e da
`layouts/partials/footer.html`/`analytics.html`, invece di essere ripetuti
come testo fisso. Due valori restano placeholder letterali, non inventati,
in attesa di un dato reale: `analytics.goatcounter_url` e `kofi.link`.

## Hugo data

La directory `data/` costituisce una sorgente di dati strutturati utilizzabile
dai template Hugo.

## Evoluzione

L'aggiunta di nuovi campi deve derivare da esigenze reali del modello o
dell'implementazione.

I dati non devono essere duplicati inutilmente nei contenuti.
