# StamoTenti

StamoTenti è una biblioteca editoriale digitale dedicata alla meditazione,
alla consapevolezza, all'attenzione e ai fenomeni ad esse collegati.

Il progetto mette in dialogo:

- scienza e neuroscienze;
- filosofia e storia;
- critica, società ed educazione.

L'obiettivo è costruire contenuti rigorosi, accessibili e interconnessi,
con supporto multilingue e una struttura editoriale mantenibile nel tempo.

## Stato del progetto

Il repository contiene già:

- il modello concettuale del progetto;
- le specifiche editoriali e operative;
- il sistema di approvazione;
- i documenti di orientamento;
- la mappa delle dipendenze;
- l'implementazione Hugo iniziale;
- dati strutturati per autori e fonti;
- template per contenuti, bibliografia, citazioni e SEO.

La build Hugo corrente è verificata localmente.

## Da dove iniziare

Per capire **che cosa deve essere StamoTenti**:

`TO-BE.md`

Per capire **dove trovare le informazioni**:

`PROJECT-MAP.md`

Per una sintesi rapida di un'area:

`SUMMARY/`

Per capire **quali documenti dipendono da quali altri**:

`DEPENDENCY-MAP.md`

Per le regole complete:

le `*-SPEC.md`

Per l'implementazione tecnica corrente:

`TECHNICAL/`

Per i principi visivi:

`DESIGN-SPEC.md`

## Struttura principale

### Documentazione di progetto

- `TO-BE.md` — visione e vincoli fondamentali.
- `CONTENT-MODEL.md` — entità e relazioni.
- `PROJECT-MAP.md` — mappa di orientamento.
- `DEPENDENCY-MAP.md` — dipendenze tra documenti.
- `SUMMARY/` — sintesi operative.
- `*-SPEC.md` — requisiti e regole approvate.
- `TECHNICAL/` — implementazione tecnica.
- `DESIGN-SPEC.md` — principi visivi e tipografici.

### Sito Hugo

- `content/` — contenuti del sito.
- `data/` — dati strutturati.
- `layouts/` — template.
- `i18n/` — tabelle di traduzione dell'interfaccia quando necessarie.
- `assets/` — risorse gestite dalla pipeline degli asset.
- `static/` — file copiati direttamente nell'output.
- `archetypes/` — template per nuovi contenuti.
- `hugo.toml` — configurazione Hugo.

`public/` e `resources/` sono artefatti generati dalla build e non sono la
fonte primaria dei contenuti.

## Contenuti e dati

Il contenuto editoriale vive in `content/`.

Le entità riutilizzabili vengono rappresentate nei dati strutturati,
attualmente soprattutto in:

- `data/authors.yaml`
- `data/sources.yaml`

Le regole relative a fonti, citazioni, autori, media, dataset, lingue e
vocabolario sono definite dalle rispettive SPEC.

## Multilingua

L'italiano è la lingua primaria.

L'inglese è supportato dalla configurazione Hugo.

La configurazione multilingue non implica che ogni contenuto sia già tradotto:
le traduzioni devono esistere come contenuti collegati secondo
MULTILINGUAL-SPEC.md.

## Build locale

Per verificare il sito localmente:

    hugo build --gc --minify --printPathWarnings --printUnusedTemplates

Per servire il sito durante lo sviluppo:

    hugo server

La build ricrea l'output generato quando necessario.

## Principi di modifica

Prima di cambiare un comportamento importante:

1. controllare `PROJECT-MAP.md`;
2. individuare la SPEC pertinente;
3. verificare eventuali dipendenze in `DEPENDENCY-MAP.md`;
4. controllare la documentazione tecnica;
5. modificare il codice soltanto dopo aver compreso il comportamento previsto.

Una modifica al codice non costituisce automaticamente una modifica alla
regola del progetto.

## Agenti

Gli agenti devono seguire le SPEC e il workflow approvato.

Preparazione, approvazione, pubblicazione e distribuzione sono operazioni
distinte.

La capacità tecnica di eseguire un'azione non costituisce automaticamente
autorizzazione a compierla.

## Semplicità

Il progetto preferisce:

- Hugo e Markdown;
- dati strutturati semplici;
- template leggibili;
- automazioni proporzionate;
- dipendenze ridotte;
- soluzioni sostituibili.

Non devono essere introdotti database, backend o sistemi complessi quando
una soluzione più semplice è sufficiente.

## Prossimi sviluppi

L'implementazione può evolvere verso:

- traduzioni complete italiano/inglese;
- gestione più completa di fonti, media e dataset;
- workflow degli agenti;
- approvazioni persistenti;
- distribuzione;
- monitoraggio;
- testing;
- deploy automatizzato.

Questi sviluppi devono rispettare il modello e le SPEC già approvate.

## Riferimenti principali

- `TO-BE.md`
- `PROJECT-MAP.md`
- `CONTENT-MODEL.md`
- `SUMMARY/`
- `DEPENDENCY-MAP.md`
- `TECHNICAL/`
- `DESIGN-SPEC.md`
