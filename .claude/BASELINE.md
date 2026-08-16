# StamoTenti — Baseline Protection

## Scopo

Definisce ciò che costituisce la baseline tecnica di StamoTenti durante
le Fasi 0–2 della Claude Code Development Roadmap.

La baseline deve essere compresa prima di essere modificata.

## Aree protette durante il bootstrap

Finché la Fase 1 non è esplicitamente autorizzata, Claude Code non deve
modificare:

- `content/`
- `data/`
- `layouts/`
- `hugo.toml`

## Contenuti esistenti

Gli articoli, gli autori e le fonti già presenti nel repository sono
considerati fixture reali del sistema.

Durante le Fasi 0–2:

- non devono essere riscritti;
- non devono essere ottimizzati editorialmente;
- non devono essere sostituiti;
- non devono essere usati come pretesto per cambiare il modello.

Quando serve testare una nuova funzionalità, utilizzare fixture tecniche
separate quando possibile.

## Modifiche tecniche consentite dopo autorizzazione

Una volta autorizzata la Fase 1, Claude Code potrà modificare le aree
necessarie all'implementazione dell'impalcatura, tra cui:

- template;
- CSS/assets;
- configurazione Hugo;
- struttura tecnica;
- front matter contract;
- taxonomy infrastructure;
- rendering;
- test;
- componenti tecnici.

Le modifiche devono sempre essere ricondotte alla SPEC pertinente.

## Modifiche alla governance

Claude Code non deve modificare autonomamente:

- TO-BE.md;
- CONTENT-MODEL.md;
- APPROVAL-SPEC.md;
- PROJECT-MAP.md;
- SPEC approvate;
- CLAUDE.md;
- CLAUDE-CODE-DEVELOPMENT-ROADMAP.md.

Quando l'implementazione sembra richiedere una modifica a uno di questi
documenti, deve fermarsi e proporre la modifica.

## Principio

La baseline è un riferimento operativo.

Una modifica tecnica deve essere:

- intenzionale;
- tracciabile;
- motivata;
- testabile;
- reversibile quando possibile.
