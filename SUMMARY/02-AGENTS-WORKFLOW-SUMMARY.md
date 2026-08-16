# StamoTenti — Agents & Workflow Summary

## Scopo

Questo documento riassume il funzionamento degli agenti e del workflow.
Non sostituisce WORKFLOW-SPEC.md, AGENT-ROLES-SPEC.md, SECURITY-SPEC.md o
APPROVAL-SPEC.md.

## Principio

Gli agenti devono essere autonomi quanto possibile senza compromettere:

- correttezza;
- controllo editoriale;
- diritti;
- privacy;
- sicurezza;
- sostenibilità economica.

## Quattro livelli operativi

Un'attività può essere:

1. autonoma;
2. autonoma con registrazione;
3. proposta;
4. soggetta a decisione umana.

L'approvazione si applica soprattutto alle azioni ad alto impatto,
rischiose, pubbliche o difficili da reversibilizzare.

## Workflow

Un task può includere:

- ricerca;
- verifica;
- classificazione;
- produzione;
- revisione;
- test;
- traduzione;
- preparazione alla pubblicazione;
- distribuzione.

Le attività indipendenti possono essere eseguite in parallelo quando
non creano conflitti.

Un'attività in attesa di approvazione non deve bloccare attività indipendenti.

## Approvazioni

Una proposta non è un'approvazione.

Una bozza non è un'approvazione.

Un test riuscito non è un'approvazione.

L'approvazione deve essere persistente, contestuale e associata all'azione
che autorizza.

## Sicurezza

Il ruolo descrive responsabilità.

Le capacità tecniche descrivono ciò che un agente può fare.

Un agente non deve ricevere capacità ulteriori soltanto perché potrebbe
tecnicamente utilizzarle.

## Memoria operativa

Gli agenti possono conservare:

- best practice;
- errori;
- strategie;
- vincoli operativi;
- osservazioni;
- proposte.

La memoria operativa non prevale sulle SPEC.

## Costi

Ricerca, contesto, modelli e automazioni devono utilizzare budget
proporzionati al task.

Quando un budget viene raggiunto, l'agente deve conservare il lavoro valido
e interrompere o ridurre l'operazione in modo controllato.

## Principio di non blocco

Il sistema deve continuare automaticamente tutto ciò che è indipendente
da una decisione ancora pendente.
