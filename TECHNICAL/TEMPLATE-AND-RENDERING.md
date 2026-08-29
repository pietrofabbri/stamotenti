# StamoTenti — Template and Rendering

## Scopo

Descrive il ruolo dei template Hugo attualmente presenti.

## Template principali

L'implementazione corrente utilizza:

- `layouts/_default/baseof.html`;
- `layouts/_default/list.html`;
- `layouts/_default/single.html`;
- `layouts/home.html`.

## Partial

Sono presenti partial in:

`layouts/partials/`

tra cui:

- header;
- footer;
- SEO;
- bibliografia;
- debug;
- analytics (`analytics.html`, aggiunto 2026-08-29 — legge il provider da
  `data/site.yaml` invece di uno script incollato nei template; emette lo
  script solo se `analytics.goatcounter_url` non è più il placeholder).

## Shortcode

Sono presenti shortcode in `layouts/shortcodes/`:

- `cite.html`, per le citazioni;
- `sitedata.html` (aggiunto 2026-08-29), lookup generico a percorso
  puntato su `data/site.yaml` per il contenuto Markdown (es.
  `{{% sitedata "titolare.email" %}}`), cosi' i valori organizzativi
  citati nelle pagine (Privacy) non sono ripetuti come testo fisso.

## Compatibilità con la versione di Hugo

Il progetto attuale utilizza la struttura dei template compatibile con la
versione di Hugo installata nel repository.

Le versioni recenti di Hugo utilizzano una struttura aggiornata con
`layouts/_partials/` e `layouts/_shortcodes/`.

La build corrente passa senza errori con Hugo 0.164.0, quindi non è necessario
migrare immediatamente la struttura.

Un'eventuale migrazione deve essere trattata come modifica tecnica separata,
con test della build e verifica dei template.

La documentazione tecnica descrive quindi lo stato reale corrente e non
anticipa una migrazione non ancora effettuata.

## Responsabilità

I template trasformano dati e contenuti in HTML.

Le regole editoriali non devono essere ricostruite arbitrariamente dai template.

Quando il comportamento del template deve cambiare per rispettare una SPEC,
si modifica l'implementazione, non il principio documentato.

## Principio di semplicità

Il sistema deve preferire template leggibili e riutilizzabili a logiche
duplicate o framework non necessari.
