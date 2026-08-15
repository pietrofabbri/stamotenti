# StamoTenti — OPERATIONAL MEMORY SPECIFICATION

## 1. Scopo

Questo documento definisce la memoria operativa persistente di StamoTenti.

La memoria operativa conserva informazioni utili per il lavoro futuro degli agenti che non appartengono necessariamente alle specifiche del progetto.

Può contenere:

- decisioni operative;
- best practice;
- errori già incontrati;
- procedure efficaci;
- procedure da evitare;
- problemi ricorrenti;
- soluzioni già verificate;
- soglie operative;
- strategie di ricerca;
- osservazioni sul comportamento degli strumenti;
- informazioni utili per ridurre costi e token;
- motivazioni di decisioni precedenti.

La memoria operativa non sostituisce i documenti fondativi o le specifiche approvate.

---

## 2. Distinzione dai documenti fondativi

I documenti fondativi del progetto definiscono principi e vincoli relativamente stabili.

Le specifiche definiscono requisiti e regole approvate.

La memoria operativa conserva esperienza pratica.

Per esempio:

Principio:
il sistema deve minimizzare la complessità.

Specifica:
le modifiche architetturali devono essere proposte e approvate.

Memoria operativa:
per questo tipo di task è risultato più efficace utilizzare una singola ricerca mirata invece di tre ricerche parallele.

La memoria operativa può cambiare frequentemente.

---

## 3. Distinzione dalle decisioni architetturali

Una decisione operativa non deve essere trasformata automaticamente in una regola architetturale.

Quando una pratica diventa sufficientemente stabile e generale, può essere proposta come modifica a una specifica.

La memoria operativa può quindi alimentare il processo di evoluzione delle specifiche.

Non può modificarle autonomamente.

---

## 4. Principio di utilità

Una nota deve essere conservata soltanto se è ragionevolmente utile in futuro.

Non devono essere memorizzati automaticamente:

- conversazioni irrilevanti;
- informazioni temporanee;
- risultati facilmente ricostruibili;
- dettagli privi di valore futuro;
- duplicazioni;
- informazioni personali non necessarie.

La memoria deve ridurre il lavoro futuro, non diventare un archivio indiscriminato.

---

## 5. Tipi di memoria

La memoria può contenere almeno le seguenti categorie.

### Decisione

Una scelta operativa effettuata per risolvere un problema.

### Best practice

Una procedura che ha dimostrato di funzionare bene.

### Anti-pattern

Una procedura o strategia che ha prodotto risultati scadenti o costi inutili.

### Errore

Un problema incontrato e la relativa soluzione.

### Vincolo operativo

Una limitazione pratica che deve essere tenuta presente.

### Strategia

Un metodo utile per affrontare una classe di task.

### Soglia

Un limite di costo, token, tempo, richieste o altre risorse.

### Eccezione

Un caso particolare che richiede un comportamento differente.

### Proposta

Un'osservazione che potrebbe diventare una modifica a una specifica.

---

## 6. Struttura minima

Ogni nota dovrebbe contenere, quando applicabile:

- identificativo;
- tipo;
- titolo;
- data;
- origine;
- contenuto;
- contesto;
- stato;
- livello di affidabilità.

La struttura concreta può essere rappresentata in Markdown, YAML, JSON o altro formato semplice.

Il formato può evolvere senza modificare il modello concettuale.

---

## 7. Origine

Una nota dovrebbe indicare da dove deriva.

Possibili origini:

- decisione del proprietario;
- esperienza di un agente;
- esecuzione di un workflow;
- errore;
- test;
- ricerca;
- analisi di performance;
- feedback utente;
- revisione di una specifica.

Le informazioni di origine permettono di valutare quanto una nota sia affidabile.

---

## 8. Affidabilità

La memoria deve distinguere almeno tra:

- osservazione;
- ipotesi;
- pratica sperimentata;
- pratica verificata;
- decisione approvata.

Una supposizione non deve essere presentata come fatto.

Una best practice non deve essere trattata come una regola assoluta.

---

## 9. Stato

Una nota può essere:

- proposta;
- attiva;
- superata;
- ritirata;
- incorporata in una specifica.

Quando una nota diventa obsoleta non deve necessariamente essere cancellata.

Può essere marcata come superata per mantenere la storia della decisione quando questa sia utile.

---

## 10. Memoria delle specifiche

Quando un agente individua una possibile modifica a una specifica deve poter registrare:

- problema;
- comportamento attuale;
- motivazione;
- evidenze;
- proposta;
- specifiche interessate.

La nota non modifica direttamente il documento.

La modifica viene effettuata soltanto attraverso il workflow previsto.

---

## 11. Best practice

Le best practice possono essere registrate quando una procedura:

- viene utilizzata più volte;
- produce risultati consistenti;
- riduce costi;
- riduce errori;
- riduce token;
- migliora la qualità;
- rende il workflow più semplice.

Una singola esperienza positiva non deve necessariamente diventare una best practice.

---

## 12. Anti-pattern

Gli errori utili da ricordare devono poter essere registrati.

Un anti-pattern dovrebbe descrivere:

- cosa è stato fatto;
- perché sembrava ragionevole;
- cosa è andato storto;
- quale conseguenza ha prodotto;
- quale comportamento preferire in futuro.

L'obiettivo è evitare la ripetizione dello stesso errore.

---

## 13. Token e costi

La memoria può conservare informazioni relative all'efficienza dei task.

Esempi:

- ricerca troppo ampia;
- query che producono risultati inutili;
- modelli sovradimensionati per task semplici;
- strategie che consumano troppi token;
- limiti che si sono dimostrati sufficienti.

Le soglie devono essere considerate configurabili e dipendenti dal modello.

Non devono essere trasformate automaticamente in valori fissi e universali.

---

## 14. Strategie di ricerca

Gli agenti possono registrare strategie di ricerca utili.

Per esempio:

- query efficaci;
- domini particolarmente affidabili;
- ordine consigliato delle verifiche;
- fonti utili per un determinato argomento;
- ricerche che hanno prodotto falsi positivi.

Le strategie devono essere considerate indicazioni operative, non garanzie di risultato.

---

## 15. Feedback degli utenti

I feedback ricevuti tramite email, guide o altri canali possono produrre memoria operativa.

Il sistema può registrare:

- problemi ricorrenti;
- domande frequenti;
- difficoltà;
- richieste;
- suggerimenti;
- possibili miglioramenti.

I feedback non devono diventare automaticamente contenuti pubblici.

La memoria deve rispettare le regole di privacy e conservazione applicabili alla relativa risorsa.

---

## 16. Performance

Il ruolo di analisi delle performance può produrre note operative relative a:

- contenuti con risultati anomali;
- strategie editoriali;
- comportamento degli utenti;
- campagne;
- email;
- canali di distribuzione;
- ipotesi da verificare.

I dati osservati devono essere distinti dalle interpretazioni.

Una correlazione non deve essere memorizzata come causalità.

---

## 17. Riutilizzo

Prima di svolgere un task significativo, l'agente può consultare la memoria operativa pertinente.

Non deve necessariamente caricare l'intera memoria.

La selezione deve essere:

- pertinente;
- economica;
- proporzionata al task.

Il sistema deve preferire il recupero mirato delle informazioni rispetto al caricamento indiscriminato della memoria.

---

## 18. Aggiornamento

Le note possono essere:

- create;
- aggiornate;
- consolidate;
- collegate;
- archiviate;
- ritirate.

La duplicazione deve essere evitata.

Quando due note descrivono sostanzialmente la stessa pratica, il sistema dovrebbe preferire il consolidamento.

---

## 19. Conflitti

Quando due note operative sono in conflitto:

1. verificare la data;
2. verificare l'origine;
3. verificare il contesto;
4. verificare se una nota è stata superata;
5. preferire una decisione esplicitamente approvata;
6. se necessario, chiedere una nuova decisione.

Una nota più recente non è automaticamente più corretta.

---

## 20. Conflitto con le specifiche

Se una nota operativa contraddice una specifica approvata:

la specifica prevale.

L'agente può registrare una proposta di revisione della specifica.

Non deve adattare silenziosamente il comportamento alla memoria operativa.

---

## 21. Conflitto con i documenti fondativi

Se una nota operativa contraddice un principio o un vincolo stabilito nei documenti fondativi del progetto:

il principio o vincolo prevale.

L'agente deve segnalare il conflitto.

Non deve utilizzare la memoria operativa come giustificazione per ignorare un vincolo approvato.

---

## 22. Decisioni manuali

Le decisioni manuali del proprietario possono essere registrate quando hanno valore futuro.

È utile conservare anche la motivazione quando questa permette di evitare richieste ripetitive o interpretazioni errate.

Una decisione manuale non deve diventare automaticamente una regola generale.

---

## 23. Override

Quando il proprietario effettua deliberatamente un'operazione diversa da una best practice memorizzata, la memoria non deve impedire l'operazione.

L'agente può segnalare la differenza se utile.

Non deve tentare di ripristinare automaticamente la best practice.

---

## 24. Conservazione

La memoria operativa deve essere conservata in una forma persistente e versionabile quando possibile.

La perdita della memoria non deve rendere inutilizzabile il sistema.

Le specifiche fondamentali devono comunque rimanere indipendenti dalla memoria operativa.

---

## 25. Versionamento

Le modifiche alla memoria possono essere versionate quando il sistema lo permette.

Non è necessario applicare alla memoria lo stesso livello di formalità previsto per i documenti fondativi o per le specifiche.

Il versionamento deve essere proporzionato al valore della memoria e al costo della sua gestione.

---

## 26. Privacy

La memoria non deve conservare dati personali non necessari.

I dati degli utenti devono essere minimizzati.

Le informazioni provenienti da email o altri canali devono essere trattate secondo le regole applicabili alla relativa risorsa.

La memoria operativa non deve diventare un archivio secondario incontrollato di dati personali.

---

## 27. Sicurezza

La memoria può contenere informazioni sensibili sul funzionamento del sistema.

Devono essere evitati:

- password;
- token;
- chiavi private;
- credenziali;
- segreti;
- dati di autenticazione.

La memoria deve contenere riferimenti a tali risorse soltanto quando necessario e senza esporre il segreto.

---

## 28. Ricerca della memoria

La memoria dovrebbe essere ricercabile attraverso elementi come:

- tipo;
- argomento;
- ruolo;
- task;
- data;
- stato;
- affidabilità;
- specifica interessata.

La ricerca deve essere preferibilmente semantica o indicizzata quando questo produce un vantaggio reale.

Non è necessario introdurre immediatamente un database vettoriale.

---

## 29. Collegamenti

Una nota può collegarsi a:

- altre note;
- specifiche;
- articoli;
- fonti;
- media;
- task;
- commit;
- issue;
- decisioni.

I collegamenti devono essere utilizzati quando migliorano la comprensione o il recupero futuro.

---

## 30. GitHub Issues

Quando un problema richiede lavoro futuro, può essere trasformato in una GitHub Issue.

La memoria può conservare il riferimento all'issue.

Le issue possono essere utilizzate per:

- problemi tecnici;
- decisioni da prendere;
- modifiche future;
- miglioramenti;
- verifiche;
- debito tecnico;
- idee da valutare.

Non ogni nota deve diventare un'issue.

---

## 31. Appunti degli agenti

Gli agenti possono lasciare appunti operativi al termine di un task quando questi abbiano valore futuro.

Un buon appunto dovrebbe essere:

- breve;
- specifico;
- verificabile;
- contestualizzato;
- utile a un agente successivo.

Non deve essere un resoconto completo della conversazione.

---

## 32. Consolidamento

Periodicamente il sistema può identificare:

- note duplicate;
- note obsolete;
- best practice consolidate;
- anti-pattern ricorrenti;
- proposte che meritano una specifica;
- informazioni non più utili.

Il consolidamento può essere svolto automaticamente con supervisione appropriata.

---

## 33. Promozione a specifica

Una pratica può essere proposta per diventare una specifica quando:

- è generale;
- è stabile;
- è stata verificata;
- riguarda più task;
- la sua applicazione è importante;
- la sua omissione produce rischi significativi.

La promozione richiede approvazione.

---

## 34. Declassamento

Una specifica può, in futuro, essere sostituita da una pratica più flessibile.

Questo processo deve avvenire attraverso la revisione delle specifiche.

La memoria operativa non può modificare direttamente la gerarchia delle regole.

---

## 35. Memoria e agenti sostituibili

La memoria non deve essere legata a un particolare modello.

Deve poter essere utilizzata da:

- Cloud Code;
- modelli remoti;
- modelli locali;
- altri agenti futuri.

Le note devono descrivere il problema e la soluzione, non dipendere inutilmente dall'identità del modello che le ha prodotte.

---

## 36. Memoria e ruoli

Le note possono essere associate a uno o più ruoli.

Per esempio:

- ricerca;
- bibliografia;
- scrittura;
- traduzione;
- email;
- sicurezza;
- performance;
- distribuzione.

L'associazione deve servire a recuperare informazioni pertinenti.

Non deve creare una separazione artificiale della memoria.

---

## 37. Principio di economia

La memoria deve ridurre il consumo futuro di risorse.

Prima di effettuare una ricerca o un'operazione costosa, l'agente dovrebbe verificare se esiste già una conoscenza operativa pertinente.

Non deve però fidarsi ciecamente della memoria quando il task richiede informazioni aggiornate.

La memoria è un acceleratore, non un sostituto della verifica.

---

## 38. Principio di aggiornamento

Quando una memoria operativa si dimostra errata, deve poter essere corretta rapidamente.

La correzione deve preferire:

- aggiornamento della nota;
- collegamento alla nuova informazione;
- marcatura della precedente come superata.

La storia può essere conservata quando è utile per comprendere l'errore.

---

## 39. Principio di semplicità

La memoria deve rimanere semplice.

Non devono essere introdotti prematuramente:

- knowledge graph complessi;
- sistemi ontologici;
- database sofisticati;
- pipeline autonome di autoapprendimento;
- sistemi di memoria difficili da ispezionare.

La complessità può essere introdotta quando la quantità reale di memoria la rende necessaria.

---

## 40. Principio finale

La memoria operativa deve permettere a StamoTenti di imparare dall'esperienza senza permettere agli agenti di riscrivere autonomamente le regole fondamentali del progetto.

Deve:

- ridurre il lavoro ripetitivo;
- ridurre i costi;
- conservare esperienza;
- evitare errori già commessi;
- rendere il sistema più coerente;
- facilitare l'evoluzione;
- mantenere separati principi, regole ed esperienza.

I documenti fondativi stabiliscono ciò che StamoTenti vuole essere.

Le specifiche stabiliscono come deve funzionare.

La memoria operativa conserva ciò che abbiamo imparato facendolo funzionare.

---

## 41. Gerarchia dei documenti

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. le specifiche specialistiche definiscono i requisiti delle singole entità;
4. WORKFLOW-SPEC.md definisce il workflow;
5. AGENT-ROLES-SPEC.md definisce i ruoli logici;
6. OPERATIONAL-MEMORY-SPEC.md definisce la memoria operativa;
7. le specifiche tecniche definiscono l'implementazione;
8. il codice implementa le specifiche approvate.

La memoria operativa non costituisce una fonte di autorità superiore alle specifiche approvate.
