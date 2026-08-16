# StamoTenti — PROJECT MAP

## Scopo

Questo documento è la mappa di orientamento del progetto.

Gli agenti dovrebbero consultare prima questa mappa, poi il summary
pertinente e infine soltanto le SPEC necessarie al task.

## Livelli di consultazione

1. TO-BE.md
2. PROJECT-MAP.md
3. SUMMARY/*.md
4. SPEC specifiche del dominio
5. documenti tecnici
6. codice

I SUMMARY sono documenti di orientamento e sintesi.
Non introducono nuove regole e non prevalgono sulle SPEC.

## Summary

- SUMMARY/00-CONSTITUTION-SUMMARY.md
- SUMMARY/01-CONTENT-SUMMARY.md
- SUMMARY/02-AGENTS-WORKFLOW-SUMMARY.md
- SUMMARY/03-SOURCES-MEDIA-SUMMARY.md
- SUMMARY/04-PUBLICATION-RISK-SUMMARY.md
- SUMMARY/05-QUALITY-OPERATIONS-SUMMARY.md

## Documenti fondativi

- TO-BE.md
- CONTENT-MODEL.md

## Specifiche principali

- ARTICLE-SPEC.md
- ACCESSIBILITY-SPEC.md
- AUTHOR-SPEC.md
- BACKUP-SPEC.md
- CHANGE-MANAGEMENT-SPEC.md
- CITATION-SPEC.md
- CONTENT-LIFECYCLE-SPEC.md
- DATASET-SPEC.md
- DECISION-SPEC.md
- DISTRIBUTION-SPEC.md
- EMAIL-SPEC.md
- LICENSE-SPEC.md
- MEDIA-SPEC.md
- MONITORING-SPEC.md
- MULTILINGUAL-SPEC.md
- OPERATIONAL-MEMORY-SPEC.md
- PRIVACY-SPEC.md
- SECURITY-SPEC.md
- SEO-SPEC.md
- SOURCE-SPEC.md
- TESTING-SPEC.md
- VOCABULARY-SPEC.md
- WORKFLOW-SPEC.md
- AGENT-ROLES-SPEC.md

## Mappa delle dipendenze

- DEPENDENCY-MAP.md

La mappa delle dipendenze è uno strumento di orientamento e manutenzione.
Non introduce nuove regole e non modifica la gerarchia delle specifiche.

## Documenti tecnici

La documentazione tecnica descrive l'implementazione corrente senza
sostituire le SPEC.

- TECHNICAL/HUGO-ARCHITECTURE.md
- TECHNICAL/CONTENT-IMPLEMENTATION.md
- TECHNICAL/DATA-IMPLEMENTATION.md
- TECHNICAL/TEMPLATE-AND-RENDERING.md
- TECHNICAL/DEPLOYMENT.md

## Design

- DESIGN-SPEC.md

## Documento di approvazione

APPROVAL-SPEC.md è una dipendenza concettuale richiamata da più SPEC
ma non viene ricostruita automaticamente da questa mappa.

Prima di considerare il corpus completo, il documento deve essere
presente e coerente con WORKFLOW-SPEC.md, SECURITY-SPEC.md e
CHANGE-MANAGEMENT-SPEC.md.

## Principio

Il codice non costituisce la fonte primaria dell'architettura.

Le SPEC approvate definiscono le regole che il codice deve implementare.
