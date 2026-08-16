# StamoTenti — Claude Code Development Roadmap

## Scopo

Questa roadmap definisce come Claude Code deve trasformare l'attuale
repository StamoTenti in un'infrastruttura editoriale completa, pronta
a ricevere e gestire contenuti.

Questa roadmap riguarda inizialmente soltanto:

- Fase 0 — Foundation;
- Fase 1 — Site Foundation;
- Fase 2 — Complete Site Shell.

La roadmap non riguarda ancora la produzione autonoma dei contenuti,
la pubblicazione automatica o l'orchestrazione multi-agente completa.

## Stato iniziale

Il repository contiene già:

- Hugo funzionante;
- contenuti di esempio;
- dati per autori e fonti;
- template Hugo;
- SPEC;
- SUMMARY;
- PROJECT-MAP;
- DEPENDENCY-MAP;
- TECHNICAL;
- DESIGN-SPEC;
- README.

Lo stato iniziale del sito deve essere considerato una baseline.

## Regola fondamentale

Durante le Fasi 0–2 Claude Code deve trattare i contenuti editoriali
esistenti come fixture e non come materiale da riscrivere.

Non modificare contenuti, fonti o autori esistenti salvo quando una
modifica è indispensabile per una necessità infrastrutturale esplicita
e verificata.

Quando possibile, utilizzare fixture o contenuti temporanei separati
per testare nuove funzionalità.

---

# FASE 0 — CLAUDE CODE FOUNDATION

## Obiettivo

Permettere a Claude Code di comprendere il progetto, seguire la
gerarchia documentale, diagnosticare il repository e lavorare entro
limiti controllati.

## Deliverable

- CLAUDE.md;
- configurazione minima `.claude/`;
- istruzioni di orientamento;
- baseline automatica del repository;
- comandi standard di verifica;
- policy esplicita sui file modificabili;
- checkpoint umano.

## Claude deve imparare

Ordine di lettura standard:

1. CLAUDE.md;
2. PROJECT-MAP.md;
3. SUMMARY pertinente;
4. DEPENDENCY-MAP.md;
5. SPEC pertinenti;
6. TECHNICAL pertinente;
7. repository e codice.

## Capacità consentite

Claude può:

- leggere file;
- cercare nel repository;
- leggere Git status;
- leggere diff;
- eseguire Hugo build;
- eseguire controlli Markdown/YAML;
- analizzare template;
- produrre report;
- proporre modifiche.

## Capacità vietate nella Fase 0

Claude non deve:

- modificare contenuti editoriali;
- pubblicare;
- fare deploy;
- inviare email;
- modificare documenti fondativi senza processo;
- fare push;
- cancellare risorse;
- modificare arbitrariamente governance o SPEC.

## Baseline

Prima di procedere deve poter produrre un report contenente almeno:

- stato Git;
- build Hugo;
- struttura del repository;
- principali entità del modello;
- principali SPEC pertinenti;
- stato multilingua;
- stato template;
- eventuali problemi rilevati.

## Gate 0

La Fase 0 è completata quando:

- CLAUDE.md è presente;
- configurazione Claude Code minima è presente;
- baseline completata;
- build passa;
- working tree è pulito;
- nessun contenuto è stato modificato;
- Claude sa indicare le SPEC pertinenti a task esemplificativi.

Richiede approvazione umana per passare alla Fase 1.

---

# FASE 1 — SITE FOUNDATION

## Obiettivo

Tradurre le SPEC in una prima infrastruttura tecnica coerente.

Non produrre contenuti editoriali sostanziali.

## Aree

### Content model

Implementare i contenitori tecnici necessari per:

- Article;
- Author;
- Source;
- Citation;
- Topic;
- Macroarea;
- Sotto-area;
- Dataset;
- Media;
- Language;
- Translation.

Non creare sistemi custom quando Hugo o strutture semplici sono sufficienti.

### Front matter

Definire un contratto coerente con CONTENT-MODEL.md e ARTICLE-SPEC.md.

Il contratto deve essere:

- documentato;
- validato;
- testabile;
- utilizzabile da nuovi contenuti.

### Taxonomy

Implementare l'infrastruttura per:

- macroarea;
- sotto-area;
- temi trasversali.

Usare le funzionalità native di Hugo quando sufficienti.

### Authors

Rendere `data/authors.yaml` utilizzabile dai template.

### Sources

Rendere `data/sources.yaml` utilizzabile da:

- articoli;
- citazioni;
- bibliografia.

### Media

Predisporre l'infrastruttura per:

- public;
- private;
- controlled;
- pending_review.

### Page containers

Predisporre template e routing per le superfici richieste dalle SPEC,
almeno:

- home;
- section;
- article;
- author;
- source;
- taxonomy;
- taxonomy term;
- 404.

Aggiungere altre superfici soltanto quando motivate dalle SPEC.

## Regola

La Fase 1 costruisce contenitori.

Non deve trasformarsi in una fase di produzione editoriale.

## Gate 1

La Fase 1 è completata quando:

- il content contract è definito;
- taxonomy infrastructure funziona;
- author/source infrastructure funziona;
- citation/bibliography infrastructure funziona;
- le superfici fondamentali renderizzano;
- i test di integrazione passano;
- gli articoli esistenti rimangono semanticamente invariati.

Richiede approvazione umana.

---

# FASE 2 — COMPLETE SITE SHELL

## Obiettivo

Rendere il sito tecnicamente pronto a ricevere contenuti reali.

## Design system

Implementare DESIGN-SPEC.md:

- minimalismo;
- pochi colori;
- gerarchia visiva;
- spacing coerente;
- responsive;
- accessibilità;
- tipografia leggibile.

## Typography

Predisporre:

- Unicode;
- caratteri accentati;
- Latin Extended;
- Greek;
- simboli scientifici;
- caratteri storici quando necessari;
- fallback tipografico.

La scelta concreta dei font deve restare una decisione di design.

## Multilingua

Implementare l'infrastruttura per:

- IT;
- EN;
- language switcher;
- translation linking;
- canonical;
- hreflang;
- URL coerenti.

Non è necessario tradurre l'intero corpus in questa fase.

## SEO/GEO

Predisporre:

- title;
- description;
- canonical;
- hreflang;
- Open Graph;
- structured data;
- sitemap;
- robots;
- RSS quando previsto.

## Accessibility

Implementare almeno:

- semantic HTML;
- heading hierarchy;
- landmarks;
- keyboard navigation;
- focus;
- contrast;
- reduced motion;
- struttura per alt text;
- mobile accessibility.

## Content fixture system

Creare fixture tecniche, separate dai contenuti editoriali reali, che
dimostrino:

1. Article;
2. Author;
3. Source;
4. Citation;
5. Topic;
6. Macroarea;
7. Sotto-area;
8. Media;
9. Translation.

## Validation

Ogni fixture deve essere verificata con:

- Hugo build;
- link checks;
- metadata checks;
- taxonomy checks;
- citation checks;
- multilingual checks;
- accessibility checks;
- SEO checks.

## Gate 2

La Fase 2 è completata quando esiste un contenitore editoriale
completo nel quale sia possibile aggiungere un nuovo articolo senza
ripensare l'architettura.

Il risultato deve essere:

"READY FOR CONTENT"

e non ancora:

"READY FOR AUTONOMOUS PUBLISHING".

Richiede approvazione umana.

---

# Regola sui checkpoint

Claude Code può lavorare autonomamente all'interno di una fase.

Non deve passare automaticamente alla fase successiva.

Alla fine di ogni fase deve produrre:

- modifiche effettuate;
- test eseguiti;
- problemi residui;
- decisioni prese;
- file toccati;
- rischio residuo;
- criterio di completamento;
- richiesta esplicita di passaggio alla fase successiva.

---

# Regola sui contenuti

Fino alla fine della Fase 2:

- non ottimizzare editorialmente articoli esistenti;
- non riscrivere contenuti;
- non generare nuove fonti reali;
- non pubblicare;
- non modificare arbitrariamente autori;
- non alterare la classificazione reale senza necessità tecnica.

Le fixture devono essere separate e facilmente riconoscibili.

---

# Criterio generale

Claude Code deve massimizzare:

- autonomia;
- verificabilità;
- reversibilità;
- semplicità;
- tracciabilità.

Deve minimizzare:

- richieste di conferma premature;
- modifiche ai contenuti;
- duplicazione di logica;
- infrastruttura superflua;
- nuove convenzioni non documentate.

## Stato finale Fase 2

Quando la Fase 2 termina:

- l'architettura editoriale è implementata;
- il sito è tecnicamente pronto;
- il design system è applicato;
- il multilingua è predisposto;
- font e Unicode sono predisposti;
- le fonti e citazioni sono gestibili;
- taxonomy e authors sono gestibili;
- QA automatico minimo è disponibile;
- il sito può ricevere contenuti.

Da questo punto inizia la roadmap dei contenuti e dell'automazione editoriale.
