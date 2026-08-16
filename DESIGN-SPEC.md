# StamoTenti — DESIGN SPECIFICATION

## Scopo

Questa specifica definisce i principi visivi e tipografici di StamoTenti.

Non definisce un particolare font, framework CSS o sistema di componenti.
L'implementazione concreta appartiene ai documenti tecnici e al codice.

## Principio visivo

Il sito deve essere:

- minimalista;
- pulito;
- regolare;
- leggibile;
- sobrio;
- coerente;
- privo di ornamenti gratuiti.

La forma deve sostenere la lettura e la comprensione del contenuto.

## Colori

La palette deve essere contenuta.

I colori devono avere una funzione chiara e non devono essere introdotti
soltanto per decorazione.

Contrasto e leggibilità hanno priorità sull'effetto visivo.

## Tipografia

La tipografia deve privilegiare:

- leggibilità;
- gerarchia chiara;
- ritmo regolare;
- dimensioni coerenti;
- buona resa su schermi differenti.

La scelta concreta dei font è un dettaglio tecnico e può evolvere senza
modificare questi principi.

## Lingue e caratteri

Il sito deve poter rappresentare correttamente testo Unicode.

La soluzione tipografica deve tenere conto anche di:

- alfabeti diversi dall'italiano e dall'inglese;
- caratteri accentati e diacritici;
- greco;
- latino esteso;
- sistemi di scrittura antichi quando pertinenti;
- altri caratteri necessari ai contenuti futuri.

Quando un font principale non contiene un glifo necessario, il sistema deve
poter utilizzare font di fallback appropriati.

La scelta dei font deve quindi essere valutata anche in funzione della
copertura Unicode, non soltanto dell'estetica.

## Fallback

La tipografia tecnica dovrebbe utilizzare stack di font con fallback
espliciti.

Un carattere non deve diventare illeggibile soltanto perché non appartiene
al repertorio del font principale.

## Testo scientifico e storico

La resa tipografica deve supportare anche:

- simboli scientifici;
- formule quando presenti;
- citazioni in lingue diverse;
- traslitterazioni;
- diacritici;
- caratteri storici rilevanti.

## Responsive

La struttura deve rimanere leggibile su:

- desktop;
- tablet;
- dispositivi mobili.

La responsive behavior deve essere semplice e prevedibile.

## Accessibilità

Le scelte grafiche devono rispettare ACCESSIBILITY-SPEC.md.

Il design non deve ridurre accessibilità o leggibilità per ottenere un effetto
visivo.

## Identità

Il sito deve mantenere un'identità riconoscibile senza dipendere da elementi
decorativi complessi.

## Evoluzione

La specifica definisce principi duraturi.

I valori concreti di colori, font, spacing e componenti appartengono
all'implementazione.
