# StamoTenti — Claude Code Bootstrap Contract

## Scopo

Questo documento definisce il comportamento della prima sessione di Claude
Code nel repository StamoTenti.

La prima sessione serve a comprendere il progetto e preparare il piano
esecutivo della Fase 1.

Non serve ancora a sviluppare il sito.

## Regola principale

Durante il bootstrap:

- non modificare il sito;
- non modificare contenuti;
- non modificare dati reali;
- non modificare Hugo;
- non fare commit;
- non fare push;
- non fare deploy;
- non inviare email;
- non cancellare file.

## Ordine di lettura

Claude Code deve iniziare da:

1. CLAUDE.md;
2. CLAUDE-CODE-DEVELOPMENT-ROADMAP.md;
3. PROJECT-MAP.md;
4. SUMMARY pertinenti;
5. DEPENDENCY-MAP.md;
6. SPEC pertinenti;
7. TECHNICAL pertinenti;
8. stato reale del repository.

## Baseline

Eseguire:

`python3 scripts/repository-doctor.py`

La baseline deve essere conservata mentalmente durante la sessione e,
quando utile, riportata nel piano finale.

## Analisi richiesta

Claude deve produrre un report che descriva:

### Architettura attuale

- struttura Hugo;
- content;
- data;
- layouts;
- configurazione;
- multilingua;
- template;
- stato del design;
- stato SEO;
- stato accessibilità.

### Fase 1

Individuare:

- contenitori mancanti;
- contratti front matter mancanti;
- taxonomy infrastructure mancante;
- author/source/citation infrastructure mancante;
- media infrastructure mancante;
- page containers mancanti;
- test mancanti.

### Fase 1 — mappa delle modifiche

Per ogni blocco indicare:

- file da creare;
- file da modificare;
- file da lasciare intatti;
- dipendenze;
- test;
- rischio;
- ordine.

### Fase 1 — protezione

Devono essere esplicitamente identificati come protetti:

- contenuti editoriali esistenti;
- fonti reali;
- autori reali;
- testi;
- governance;
- SPEC fondative.

## Regola sulle SPEC

Una proposta tecnica deve essere ricondotta alle SPEC pertinenti.

Se una scelta tecnica sembra richiedere una modifica alla SPEC:

1. segnalarla;
2. spiegare il conflitto;
3. non modificare la SPEC;
4. non aggirare la SPEC nel codice.

## Output finale

Il risultato del bootstrap deve essere:

1. Architecture assessment;
2. Phase 1 implementation plan;
3. File impact map;
4. Test plan;
5. Risks;
6. Open questions;
7. Human approval checkpoint.

## Fine del bootstrap

Claude Code deve fermarsi dopo il report.

Non deve iniziare la Fase 1 automaticamente.

La Fase 1 inizia soltanto dopo approvazione umana esplicita.

## Criterio di successo

Il bootstrap è riuscito quando il report permette a una persona di capire:

- cosa verrà costruito;
- perché;
- con quali SPEC;
- quali file verranno toccati;
- quali resteranno intatti;
- come verrà verificato;
- dove serve approvazione.

