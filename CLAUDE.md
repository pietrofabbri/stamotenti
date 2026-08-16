# StamoTenti — Claude Code Instructions

## Missione corrente

La missione corrente è costruire l'infrastruttura tecnica del sito
StamoTenti partendo dallo stato di fatto del repository.

Siamo nella fase di sviluppo dell'impalcatura.

NON siamo ancora nella fase di produzione autonoma dei contenuti.

## Source of truth

Prima di modificare il progetto:

1. leggere PROJECT-MAP.md;
2. leggere il SUMMARY pertinente;
3. consultare DEPENDENCY-MAP.md;
4. leggere le SPEC pertinenti;
5. leggere il TECHNICAL pertinente;
6. ispezionare il codice reale.

Non reinventare regole già presenti nelle SPEC.

## Gerarchia

La documentazione opera secondo questa struttura:

TO-BE
→ PROJECT-MAP
→ SUMMARY
→ SPEC
→ TECHNICAL
→ CODE

I SUMMARY orientano ma non sostituiscono le SPEC.

Il codice implementa le regole approvate.

## Fasi correnti

La roadmap vincolante di sviluppo è:

CLAUDE-CODE-DEVELOPMENT-ROADMAP.md

Per ora il lavoro è limitato alle Fasi 0–2.

Non iniziare autonomamente la fase successiva.

## Regola fondamentale sui contenuti

Durante le Fasi 0–2 trattare i contenuti esistenti come fixture.

Non riscrivere articoli.

Non migliorare editorialmente i contenuti.

Non cambiare arbitrariamente fonti o autori.

Non modificare contenuti reali se una fixture tecnica separata può
dimostrare la funzionalità.

## Obiettivo tecnico

Costruire contenitori per contenuti:

- model;
- front matter;
- taxonomy;
- authors;
- sources;
- citations;
- media;
- translations;
- rendering;
- accessibility;
- SEO;
- design system.

Non costruire ancora il sistema completo di produzione autonoma.

## Prima di una modifica

Identificare:

- file coinvolti;
- SPEC applicabili;
- dipendenze;
- rischio;
- test necessari;
- eventuale impatto sui contenuti esistenti.

## Dopo una modifica

Eseguire quando pertinenti:

- git diff --check;
- Hugo build;
- controlli Markdown;
- controlli YAML;
- test relativi alla funzionalità modificata.

## Autonomia

Claude può lavorare autonomamente all'interno della fase autorizzata.

Non può assumere autorizzazione implicita a:

- pubblicare;
- fare deploy;
- pushare;
- inviare email;
- cancellare dati;
- modificare governance;
- modificare documenti fondativi.

## Checkpoint

Alla fine di ogni fase fermarsi e produrre un report con:

- cosa è stato fatto;
- cosa è stato modificato;
- test;
- problemi;
- decisioni;
- rischio residuo;
- criteri di completamento.

Non avanzare automaticamente alla fase successiva.

## Principio

Preferire:

- Hugo nativo;
- Markdown;
- YAML;
- template semplici;
- codice leggibile;
- modifiche reversibili.

Evitare infrastruttura complessa quando non necessaria.
