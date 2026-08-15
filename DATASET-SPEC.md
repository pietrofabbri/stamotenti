# StamoTenti — DATASET SPECIFICATION

## 1. Scopo

Questo documento definisce la gestione dei dataset utilizzati da StamoTenti.

Il dataset è un'entità informativa distinta dal file, dalla fonte bibliografica
che lo descrive e dall'eventuale articolo che lo utilizza.

Un dataset è una raccolta strutturata di dati utilizzata per:

- ricerca;
- analisi;
- verifica;
- confronto;
- produzione di contenuti;
- visualizzazione;
- elaborazione statistica;
- supporto a conclusioni editoriali.

Un dataset può essere associato a una fonte, a un articolo, a un autore, a un tema o ad altri media.

Il dataset deve essere trattato come un'entità informativa distinta dal semplice file che lo contiene.

---

## 2. Dataset e file

Il dataset e il file che lo rappresenta non sono necessariamente la stessa cosa.

Un dataset può essere distribuito come:

- CSV;
- TSV;
- JSON;
- XML;
- XLSX;
- database;
- archivio compresso;
- API;
- raccolta di file;
- altro formato strutturato.

Il file costituisce una rappresentazione o un'istanza del dataset.

Quando possibile, il sistema deve distinguere:

- identità del dataset;
- versione;
- formato;
- file;
- URL;
- repository;
- data di acquisizione.

---

## 3. Identificativo

Ogni dataset gestito dal sistema deve possedere un identificativo stabile.

L'identificativo deve essere:

- univoco;
- leggibile;
- indipendente dal nome visualizzato;
- stabile nel tempo.

La modifica del nome del dataset non deve modificarne automaticamente l'identità.

Se il dataset proviene da un repository che fornisce un identificativo stabile, questo deve essere conservato nei metadata.

---

## 4. Provenienza

Il sistema deve conservare, quando disponibile:

- produttore;
- ente o organizzazione;
- autore;
- repository;
- URL originale;
- identificativo esterno;
- data di pubblicazione;
- data di acquisizione;
- versione;
- eventuale DOI;
- eventuale licenza;
- eventuale metodologia.

La provenienza deve essere distinta dalla copia locale eventualmente utilizzata dal sistema.

---

## 5. Versioni

Un dataset può avere versioni differenti.

Quando una nuova versione modifica sostanzialmente i dati, il sistema deve poter distinguere la versione utilizzata.

Un articolo o un'analisi che dipende da una specifica versione deve poter risalire a quella versione.

Non è necessario introdurre un sistema di versionamento complesso quando il produttore del dataset fornisce già identificativi o versioni affidabili.

---

## 6. Data di acquisizione

Quando un dataset viene acquisito dal sistema deve essere possibile registrare:

- data di acquisizione;
- fonte da cui è stato acquisito;
- versione disponibile;
- eventuale hash del file;
- eventuali trasformazioni effettuate.

La data di acquisizione non sostituisce la data di pubblicazione del dataset originale.

---

## 7. Integrità

Quando tecnicamente utile, il sistema può conservare un hash del file acquisito.

L'hash può essere utilizzato per:

- verificare l'integrità;
- identificare duplicati;
- verificare se un file è cambiato;
- verificare l'integrità dei backup.

L'hash non costituisce necessariamente l'identificativo editoriale del dataset.

---

## 8. Licenza

La licenza del dataset deve essere registrata quando disponibile.

Il sistema deve distinguere:

- licenza del dataset;
- licenza di eventuali trasformazioni;
- condizioni di utilizzo del repository;
- eventuali restrizioni ulteriori.

La presenza di un URL pubblico non implica automaticamente la possibilità di redistribuire il dataset.

---

## 9. Accessibilità e diritti

Il dataset deve rispettare la distinzione stabilita in MEDIA-SPEC.md:

- posso leggere;
- posso usare per ricerca;
- posso citare;
- posso pubblicare;
- posso redistribuire.

Queste condizioni non sono equivalenti.

Un dataset può essere accessibile tecnicamente ma non essere pubblicabile o redistribuibile.

I metadata devono rendere esplicite, quando note, queste condizioni.

---

## 10. Dataset pubblico e privato

Il sistema deve distinguere almeno tra:

- pubblico;
- privato;
- accesso controllato.

Un dataset pubblico può essere reso accessibile secondo la relativa licenza e le condizioni applicabili.

Un dataset privato non deve essere pubblicato o redistribuito soltanto perché è stato utilizzato nella ricerca.

Un dataset ad accesso controllato può essere utilizzato secondo autorizzazioni specifiche.

La classificazione deve essere coerente con MEDIA-SPEC.md.

---

## 11. Dati personali

I dataset possono contenere dati personali o informazioni sensibili.

Prima della pubblicazione o redistribuzione deve essere verificata la presenza di tali dati e la relativa base giuridica e autorizzazione.

Gli agenti non devono assumere che un dataset sia pubblicabile soltanto perché è tecnicamente accessibile.

Quando possibile devono essere preferiti:

- dati aggregati;
- dati anonimizzati;
- dati pseudonimizzati quando appropriato;
- dataset pubblicati direttamente dal titolare.

---

## 12. Qualità

Quando un dataset viene utilizzato in modo rilevante, il sistema dovrebbe poter registrare informazioni sulla qualità.

Possono essere considerate:

- completezza;
- accuratezza dichiarata;
- granularità;
- copertura temporale;
- copertura geografica;
- valori mancanti;
- duplicati;
- anomalie;
- metodologia di raccolta;
- eventuali limitazioni dichiarate.

L'agente non deve trasformare una valutazione preliminare della qualità in una garanzia scientifica.

---

## 13. Metodologia

Quando disponibile, deve essere conservata la metodologia utilizzata per produrre il dataset.

La metodologia può provenire da:

- documentazione ufficiale;
- paper;
- repository;
- documentazione tecnica;
- metadata del produttore.

La metodologia è particolarmente importante quando i dati vengono utilizzati per sostenere conclusioni quantitative.

---

## 14. Trasformazioni

Un dataset può essere trasformato prima dell'utilizzo.

Le trasformazioni rilevanti devono essere documentabili.

Esempi:

- filtraggio;
- aggregazione;
- normalizzazione;
- conversione di unità;
- eliminazione di record;
- correzione di errori;
- fusione con altri dataset;
- calcolo di variabili derivate.

Quando una trasformazione può modificare significativamente il risultato, deve essere conservata la relativa informazione.

---

## 15. Dataset derivati

Un dataset può essere derivato da uno o più dataset originali.

In questo caso devono essere mantenuti, quando possibile:

- dataset di origine;
- trasformazioni;
- versione;
- autore della trasformazione;
- data;
- eventuale script utilizzato;
- eventuale licenza applicabile.

Il dataset derivato non deve essere confuso con il dataset originale.

---

## 16. Dataset combinati

Quando più dataset vengono combinati, il sistema dovrebbe poter registrare le fonti di ciascun componente.

Questo permette di ricostruire:

- quali dati sono stati utilizzati;
- da quali fonti provengono;
- quali condizioni di utilizzo si applicano;
- quali trasformazioni sono state effettuate.

La combinazione di dataset con licenze differenti deve essere verificata prima della pubblicazione.

---

## 17. Citazione

Un dataset utilizzato in un articolo deve poter essere citato.

Quando il dataset possiede un identificativo persistente o una modalità
ufficiale di citazione, questi devono essere privilegiati.

La citazione deve riferirsi, quando possibile, alla versione effettivamente utilizzata.

Se il produttore fornisce una modalità ufficiale di citazione, questa dovrebbe essere preferita.

Quando disponibile, il sistema deve conservare:

- titolo;
- autore;
- ente;
- anno;
- versione;
- DOI;
- URL;
- repository;
- identificativo del dataset.

La modalità di rendering della citazione è definita in CITATION-SPEC.md.

---

## 18. Posizione nel dataset

Quando un articolo utilizza una porzione specifica del dataset, la citazione o la documentazione può indicare:

- tabella;
- variabile;
- colonna;
- riga;
- intervallo temporale;
- intervallo geografico;
- query;
- filtri;
- identificativi dei record;
- altra posizione pertinente.

Il livello di precisione deve essere proporzionato alla natura del dataset.

---

## 19. Dataset tramite API

Un dataset può essere accessibile tramite API anziché tramite un file statico.

In questo caso devono essere registrati, quando disponibili:

- endpoint;
- versione API;
- data di accesso;
- parametri rilevanti;
- query;
- identificativo della risorsa;
- documentazione ufficiale.

Quando il risultato dell'API può cambiare nel tempo, l'analisi dovrebbe conservare una rappresentazione dei dati effettivamente utilizzati quando i diritti e le condizioni lo consentono.

---

## 20. Snapshot

Quando un dataset remoto è soggetto a modifiche e viene utilizzato per un'analisi importante, può essere opportuno conservare uno snapshot.

Lo snapshot deve rispettare:

- licenza;
- diritti;
- condizioni di utilizzo;
- classificazione pubblico/privato.

La conservazione di uno snapshot non implica il diritto di pubblicarlo.

---

## 21. Dataset non pubblicabili

Un dataset può essere utilizzato internamente senza poter essere pubblicato.

In questo caso:

- può essere utilizzato per ricerca se autorizzato;
- può essere citato secondo le condizioni applicabili;
- non deve essere incluso automaticamente nel repository pubblico;
- non deve essere caricato automaticamente su repository pubblici;
- non deve essere redistribuito.

Gli articoli devono poter riferirsi a dataset non pubblicabili senza esporre il dataset stesso.

---

## 22. Dataset acquistati o concessi

Un dataset può essere:

- acquistato;
- concesso in licenza;
- ottenuto tramite abbonamento;
- fornito direttamente da un ente;
- ottenuto tramite accesso istituzionale.

In questi casi devono essere conservate, quando necessarie, le informazioni relative alle condizioni di utilizzo.

Il sistema non deve assumere che il pagamento per l'accesso implichi il diritto alla redistribuzione.

---

## 23. Repository esterni

I dataset possono provenire da repository differenti.

Il sistema non deve essere vincolato a un singolo servizio.

Possono essere utilizzati, quando appropriati:

- repository scientifici;
- archivi istituzionali;
- repository open data;
- repository di ricerca;
- repository gestiti direttamente dal produttore;
- altri servizi compatibili con i diritti del dataset.

La scelta del repository deve dipendere dalla natura del dataset, dai diritti e dalla necessità di conservazione.

---

## 24. Conservazione

I dataset importanti devono essere conservati in modo proporzionato al loro valore.

Quando il dataset è pubblico e redistribuibile, può essere conservata una copia in uno storage pubblico o archivistico appropriato.

Quando il dataset è privato o non redistribuibile, la copia deve essere conservata esclusivamente in uno storage compatibile con le relative condizioni.

La soluzione tecnica di storage non è definita da questo documento.

---

## 25. Backup

I dataset acquisiti e autorizzati alla conservazione devono essere inclusi nel sistema di backup appropriato.

Il backup deve rispettare la stessa classificazione di accesso del dataset originale, salvo ulteriori misure di sicurezza.

Un backup privato non deve essere trasformato in una copia pubblica.

---

## 26. Utilizzo negli articoli

Un dataset può contribuire a un articolo attraverso:

Il collegamento deve poter indicare, quando rilevante, la versione o lo
snapshot effettivamente utilizzato.

- dati quantitativi;
- statistiche;
- grafici;
- tabelle;
- confronti;
- verifiche;
- esempi;
- analisi esplorative.

L'articolo deve poter risalire al dataset e, quando rilevante, alla versione utilizzata.

---

## 27. Riproducibilità

Quando ragionevolmente possibile, le analisi quantitative importanti
dovrebbero essere riproducibili.

La riproducibilità non richiede necessariamente di conservare l'intero
ambiente tecnico: il livello di dettaglio deve essere proporzionato
all'importanza dell'analisi e alla possibilità effettiva di ricostruirla.

Possono essere conservati:

- dataset;
- snapshot;
- script;
- query;
- trasformazioni;
- parametri;
- ambiente di esecuzione;
- risultati intermedi.

La riproducibilità deve essere proporzionata all'importanza dell'analisi.

Non è necessario introdurre un'infrastruttura complessa per ogni semplice utilizzo di dati.

---

## 28. Dataset e agenti

Gli agenti possono:

- cercare dataset;
- valutarne la pertinenza;
- registrare metadata;
- classificare dataset;
- verificare la provenienza;
- proporre l'utilizzo;
- acquisire dataset quando autorizzati;
- eseguire trasformazioni autorizzate;
- produrre analisi.

Gli agenti non devono assumere automaticamente che un dataset sia pubblicabile o redistribuibile.

---

## 29. Validazione

Prima di utilizzare un dataset in un'analisi importante, l'agente dovrebbe verificare almeno:

- provenienza;
- versione;
- data;
- metodologia;
- licenza;
- qualità apparente;
- eventuali limitazioni;
- coerenza con la domanda di ricerca.

La profondità della verifica deve essere proporzionata all'importanza del dataset.

---

## 30. Classificazione per tema

I dataset possono essere classificati utilizzando il vocabolario approvato di StamoTenti.

La classificazione deve facilitare:

- ricerca;
- recupero;
- collegamento con articoli;
- individuazione di dataset pertinenti;
- analisi future.

Non devono essere creati nuovi termini autonomamente quando il vocabolario richiede approvazione.

---

## 31. Multilingua

I metadata visibili relativi ai dataset devono rispettare il sistema multilingue del progetto.

Il dataset mantiene una singola identità anche quando viene descritto in più lingue.

Titoli, descrizioni e informazioni editoriali possono avere traduzioni.

I termini tassonomici visibili devono rispettare le regole multilingue definite per il progetto.

---

## 32. Fonti e dataset

Un dataset può essere associato a una o più fonti.

Per esempio:

- paper che descrive il dataset;
- metodologia;
- documentazione ufficiale;
- repository;
- studio che ha prodotto i dati.

La fonte e il dataset rimangono entità distinte.

Una fonte può descrivere un dataset senza essere il dataset stesso.

---

## 33. Dataset e media

Il file che contiene un dataset può essere gestito anche come media secondo MEDIA-SPEC.md.

In questo caso:

- MEDIA-SPEC.md disciplina il file e la sua distribuzione;
- DATASET-SPEC.md disciplina il significato e l'utilizzo del dataset.

Le due specifiche devono essere applicate insieme quando necessario.

---

## 34. Non duplicazione

Lo stesso dataset non deve essere registrato più volte soltanto perché:

- viene utilizzato da articoli diversi;
- viene citato più volte;
- appartiene a più temi;
- viene utilizzato in più analisi.

Le relazioni devono essere mantenute separatamente dall'identità del dataset.

---

## 35. Dataset e temi multipli

Un dataset può appartenere a più temi.

La classificazione multipla è preferibile alla duplicazione dello stesso dataset.

La duplicazione fisica può essere utilizzata esclusivamente quando una specifica infrastruttura di conservazione lo rende utile e quando i diritti lo consentono.

La duplicazione non deve creare identità editoriali differenti.

---

## 36. Dati pubblicati da StamoTenti

StamoTenti può produrre dataset derivati da proprie elaborazioni.

In questo caso devono essere documentati, quando rilevanti:

- dati di origine;
- metodologia;
- trasformazioni;
- versione;
- data;
- autore o responsabile;
- licenza;
- modalità di citazione.

La pubblicazione di un dataset derivato non deve violare i diritti sui dataset originali.

---

## 37. Dataset e DOI

Quando un dataset possiede un DOI esterno, questo deve essere conservato come identificativo esterno.

Se StamoTenti pubblica autonomamente un dataset e ottiene un proprio DOI attraverso un repository o servizio archivistico, il DOI deve essere registrato separatamente dall'eventuale DOI della fonte originale.

I DOI non devono essere confusi.

---

## 38. Controllo delle fonti

Un agente può proporre un dataset individuato durante una ricerca.

La proposta deve distinguere chiaramente tra:

- pertinenza;
- provenienza;
- qualità apparente;
- licenza;
- possibilità di acquisizione;
- possibilità di redistribuzione.

Queste proprietà non devono essere trattate come equivalenti.

Quando il dataset non appartiene già al catalogo delle fonti e dei dati del progetto, può essere registrato come proposta.

La decisione di includerlo stabilmente nel patrimonio delle risorse di StamoTenti può richiedere approvazione.

L'agente può fornire:

- provenienza;
- motivazione;
- pertinenza;
- licenza;
- qualità apparente;
- eventuali rischi;
- proposta di classificazione.

---

## 39. Aggiornamento

Quando il produttore pubblica una nuova versione, il sistema può rilevarla.

L'agente può:

- segnalare la nuova versione;
- confrontare metadata;
- verificare cambiamenti rilevanti;
- proporre l'acquisizione;
- mantenere la versione precedente quando necessaria per la riproducibilità.

L'aggiornamento non deve sostituire automaticamente una versione utilizzata da un'analisi già pubblicata.

---

## 40. Economia delle risorse

La gestione dei dataset deve essere proporzionata al loro valore.

Non devono essere:

- scaricati ripetutamente senza necessità;
- duplicati inutilmente;
- elaborati con modelli costosi quando non serve;
- conservati indefinitamente senza valore;
- sincronizzati frequentemente senza motivo.

Gli agenti devono preferire strategie efficienti.

Le soglie operative possono essere definite nel workflow o nella memoria operativa e non devono essere fissate rigidamente da questa specifica.

---

## 41. Manualità

Gli agenti devono poter proporre e automatizzare la gestione dei dataset senza impedire la gestione manuale.

Il proprietario deve poter:

- aggiungere un dataset;
- correggere metadata;
- cambiare classificazione;
- sostituire una risorsa;
- indicare una fonte;
- modificare i permessi;
- indicare una versione;
- rifiutare una proposta automatica.

Le procedure automatiche devono rispettare le modifiche manuali esplicite.

---

## 42. Principio di semplicità

Non deve essere introdotto prematuramente un sistema complesso di gestione
dei dataset.

Quando un dataset può essere gestito con metadata, file, repository e
semplici script, questa soluzione è preferibile.

La complessità può crescere successivamente quando il volume, la frequenza
degli aggiornamenti o la necessità di riproducibilità lo giustificano.

Il modello deve poter funzionare con:

- Markdown;
- front matter;
- file;
- metadata;
- repository;
- semplici strutture dati.

Sistemi più sofisticati possono essere introdotti quando il volume dei dati lo giustifica.

---

## 43. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. SOURCE-SPEC.md definisce le fonti;
4. MEDIA-SPEC.md definisce la gestione dei file e dei media;
5. DATASET-SPEC.md definisce il modello dei dataset;
6. CITATION-SPEC.md definisce il loro utilizzo nelle citazioni;
7. WORKFLOW-SPEC.md definisce i workflow;
8. le specifiche tecniche definiscono l'implementazione;
9. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.
