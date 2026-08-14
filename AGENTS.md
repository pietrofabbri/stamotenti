# StamoTenti

## Struttura

- Hugo genera il sito.
- I contenuti sono scritti in Markdown.
- I dati strutturati sono nella cartella `data/`.
- Le fonti sono in `data/sources.yaml`.
- Gli autori sono in `data/authors.yaml`.
- I template Hugo sono in `layouts/`.
- I file pubblici statici sono in `static/`.

## Contenuti

- Gli articoli devono essere scritti in Markdown.
- Non inserire HTML quando Markdown o Hugo possono svolgere lo stesso compito.
- Non inserire dati bibliografici direttamente nel testo dell'articolo.
- Le fonti devono essere referenziate tramite il loro `id`.

## Fonti

Ogni fonte deve avere almeno:

- `id`
- `type`
- `title`

Quando disponibili, aggiungere:

- `authors`
- `year`
- `doi`
- `isbn`
- `url`
- `file`

Tipi di fonte supportati:

- `paper`
- `review`
- `meta-analysis`
- `book`
- `web`
- `report`
- `chapter`
- `thesis`
- `dataset`

Regole:

- Non duplicare una fonte già presente.
- Non creare un nuovo `id` per una fonte già esistente.
- Non inventare dati bibliografici.
- Se un DOI è disponibile, conservarlo.
- Un PDF non determina necessariamente il `type`: un paper PDF resta `type: paper`.
- `file` indica un file pubblicato dal sito e deve puntare a un file presente in `static/`.
- I PDF di lavoro privati non devono essere inseriti in `static/`.

## Autori

Gli autori sono definiti in `data/authors.yaml`.

Gli articoli e le fonti devono usare l'`id` dell'autore, non ripetere il nome.

Non creare duplicati dello stesso autore.

## Citazioni

Le fonti devono essere citate nel testo tramite:

`{{< cite "source-id" >}}`

Per più fonti:

`{{< cite "source-id-1" "source-id-2" >}}`

Non scrivere manualmente la citazione bibliografica nel testo.

## Verifica

Dopo modifiche significative:

1. eseguire `hugo`;
2. verificare che non ci siano errori;
3. controllare il risultato nel browser;
4. non considerare il lavoro concluso se Hugo non compila correttamente.

## Principio generale

Preferire soluzioni semplici, leggibili, portabili e facilmente modificabili.

Non aggiungere database o servizi esterni quando Hugo, Markdown, YAML o un semplice script sono sufficienti.