# StamoTenti — WORKFLOW SPECIFICATION

## 1. Scopo

Questo documento definisce il workflow operativo di StamoTenti.

Stabilisce:

- come vengono eseguiti i task;
- come vengono coordinate le attività;
- quando un'attività può essere svolta autonomamente;
- quando è necessaria una decisione umana;
- come vengono gestite le approvazioni;
- come vengono gestiti errori, conflitti e attività pendenti;
- come viene mantenuta la possibilità di intervento manuale;
- come vengono controllati costi e risorse.

I ruoli degli agenti sono definiti in AGENT-ROLES-SPEC.md.

La memoria operativa è definita in OPERATIONAL-MEMORY-SPEC.md.

---

## 2. Principio fondamentale

Gli agenti devono essere il più possibile autonomi senza compromettere:

- correttezza;
- controllo editoriale;
- diritti di utilizzo;
- sicurezza;
- sostenibilità economica.

L'approvazione umana non deve essere richiesta semplicemente perché una decisione potrebbe essere approvata.

Deve essere richiesta quando il suo impatto, rischio o carattere irreversibile rende opportuno il giudizio umano.

---

## 3. Autonomia

Quando un task contiene attività autonome e attività che richiedono approvazione, l'agente deve:

1. svolgere le attività autonome;
2. preparare quelle che richiedono decisione;
3. registrare lo stato;
4. presentare le sole decisioni ancora necessarie;
5. continuare il lavoro indipendente quando possibile.

Una decisione pendente non deve bloccare inutilmente attività non dipendenti da essa.

---

## 4. Livelli di autonomia

Le azioni possono essere considerate secondo quattro livelli:

### Autonoma

L'agente può eseguirla direttamente.

### Autonoma con registrazione

L'agente può eseguirla direttamente, ma deve registrare il risultato quando la registrazione ha valore operativo.

### Proposta

L'agente prepara il lavoro e propone una decisione, ma non applica la modifica definitiva.

### Decisione umana

L'azione richiede esplicitamente una decisione del proprietario.

Questi livelli descrivono il comportamento richiesto, non profili rigidi assegnati agli agenti.

---

## 5. Autorizzazioni

Le autorizzazioni devono essere associate alle azioni e alle loro condizioni, non semplicemente all'identità di un agente.

La stessa capacità può essere:

- consentita in un contesto;
- limitata in un altro;
- subordinata ad approvazione in un terzo.

Devono essere considerate, quando rilevanti:

- rischio;
- reversibilità;
- costo;
- visibilità pubblica;
- diritti;
- stato del contenuto;
- decisioni precedenti.

Un agente deve poter svolgere più ruoli quando dispone delle capacità necessarie.

---

## 6. Principio di proporzionalità

Il controllo deve essere proporzionato al rischio.

Azioni semplici, reversibili e a basso impatto devono avere un workflow leggero.

Azioni pubbliche, costose, irreversibili o editorialmente rilevanti possono richiedere maggiore controllo.

Non devono essere applicate procedure pesanti alle attività meccaniche.

---

## 7. Proposte

Quando serve una decisione umana, l'agente deve preparare una proposta concreta.

La proposta dovrebbe indicare, quando rilevante:

- cosa si propone;
- perché;
- contenuti interessati;
- fonti utilizzate;
- livello di certezza;
- rischi;
- alternative;
- conseguenze;
- eventuale costo.

La proposta deve ridurre il lavoro necessario al proprietario per prendere la decisione.

---

## 8. Approvazioni

Il proprietario deve poter:

- approvare;
- rifiutare;
- modificare;
- rimandare.

Quando esistono molte decisioni equivalenti, possono essere raggruppate.

Il raggruppamento non deve però nascondere differenze sostanziali.

Una decisione già approvata deve essere riutilizzata quando le condizioni rimangono sostanzialmente identiche.

---

## 9. Coda delle approvazioni

Le decisioni pendenti devono poter essere conservate in una coda persistente.

Ogni elemento dovrebbe contenere almeno:

- identificativo;
- tipo;
- priorità;
- data;
- contenuto interessato;
- proposta;
- motivazione;
- stato.

Gli stati possono comprendere:

- pending;
- approved;
- rejected;
- modified;
- expired;
- superseded.

La coda deve permettere di recuperare le decisioni anche molto tempo dopo la loro creazione.

---

## 10. Notifiche

Le notifiche devono essere persistenti e recuperabili.

Non devono dipendere esclusivamente da messaggi temporanei all'interno di una singola conversazione.

Le richieste devono essere:

- sintetiche;
- prioritarizzate;
- collegate alla risorsa interessata;
- accompagnate dall'azione richiesta.

Il sistema deve evitare notifiche ripetitive per la stessa decisione.

---

## 11. Priorità

Le richieste possono essere ordinate per priorità.

Una classificazione semplice può comprendere:

- critica;
- alta;
- normale;
- bassa.

La priorità deve riflettere l'impatto reale dell'attività.

---

## 12. Attività indipendenti

Quando un task comprende attività indipendenti, queste possono essere eseguite in parallelo.

Esempi:

- ricerca bibliografica;
- verifica di link;
- classificazione;
- preparazione metadata;
- controllo tecnico.

La parallelizzazione deve rispettare:

- dipendenze;
- conflitti di scrittura;
- limiti di costo;
- capacità disponibili.

---

## 13. Dipendenze

Le dipendenze tra attività devono essere esplicite quando necessario.

Un workflow può comprendere, per esempio:

ricerca → verifica → stesura → controllo → traduzione → pubblicazione.

Non tutte le attività devono necessariamente essere eseguite in questa sequenza.

Il sistema deve sfruttare le attività indipendenti quando possibile.

---

## 14. Stato dei task

Un task può avere stati quali:

- pending;
- running;
- completed;
- blocked;
- awaiting_approval;
- failed;
- cancelled.

Uno stato `awaiting_approval` non deve essere trattato come un errore.

Uno stato `blocked` deve indicare cosa impedisce la prosecuzione.

---

## 15. Errori

Gli errori devono essere classificati in base alla possibilità di recupero.

L'agente dovrebbe distinguere almeno tra:

- errore recuperabile;
- nuovo tentativo necessario;
- strategia alternativa necessaria;
- intervento umano necessario.

Gli errori tecnici recuperabili non devono generare automaticamente richieste di approvazione.

Quando un tentativo fallisce, il lavoro già valido deve essere conservato.

---

## 16. Conflitti

Quando due operazioni modificano contemporaneamente la stessa risorsa, il sistema deve evitare sovrascritture inconsapevoli.

Quando il conflitto non è risolvibile automaticamente, deve essere reso esplicito.

Una decisione manuale precedente deve essere trattata come intenzionale salvo evidenza contraria.

---

## 17. Intervento manuale

Il proprietario deve poter intervenire manualmente in qualsiasi momento compatibile con il sistema.

Deve poter, quando necessario:

- modificare articoli;
- modificare metadata;
- aggiungere fonti;
- aggiungere media;
- correggere classificazioni;
- correggere traduzioni;
- modificare relazioni;
- rifiutare decisioni automatiche.

L'automazione non deve diventare un prerequisito per amministrare il progetto.

---

## 18. Modifiche manuali

Gli agenti non devono sovrascrivere automaticamente modifiche manuali soltanto perché producono un risultato differente.

Quando rilevano un conflitto con una decisione manuale devono, secondo il contesto:

- rispettarla;
- segnalarla;
- proporre una modifica.

Il sistema deve evitare cicli in cui agente e modifica manuale si sovrascrivono reciprocamente.

---

## 19. Pubblicazione

La preparazione e la pubblicazione sono attività concettualmente distinte.

Gli agenti possono preparare autonomamente:

- articoli;
- traduzioni;
- fonti;
- citazioni;
- metadata;
- media.

La pubblicazione deve rispettare le regole editoriali e di autorizzazione applicabili.

Un contenuto non deve diventare pubblico soltanto perché è tecnicamente pronto.

---

## 20. Fonti e citazioni

La ricerca, verifica e classificazione delle fonti possono essere automatizzate secondo SOURCE-SPEC.md.

L'utilizzo delle fonti deve rispettare:

- diritti;
- stato di visibilità;
- possibilità di citazione;
- possibilità di pubblicazione;
- regole definite in CITATION-SPEC.md.

La capacità di leggere una fonte non implica automaticamente la possibilità di pubblicarla o redistribuirla.

---

## 21. Media

Il workflow deve rispettare MEDIA-SPEC.md.

Per ogni media devono rimanere distinte:

- possibilità di lettura;
- possibilità di ricerca;
- possibilità di citazione;
- possibilità di pubblicazione;
- possibilità di redistribuzione.

Lo storage tecnico e i diritti editoriali sono concetti distinti.

---

## 22. Traduzioni

Le traduzioni possono essere eseguite autonomamente dagli agenti.

Il workflow non deve richiedere una revisione manuale del proprietario per ogni traduzione quando il sistema considera sufficiente il processo automatico.

Gli agenti devono mantenere:

- significato;
- struttura;
- citazioni;
- relazioni;
- metadata;
- classificazioni.

I casi linguisticamente incerti possono essere segnalati secondo le regole operative.

---

## 23. Ricerca online

Gli agenti possono effettuare ricerche online per:

- verificare informazioni;
- trovare fonti;
- controllare bibliografie;
- validare identificativi;
- confrontare evidenze;
- verificare terminologia.

La ricerca deve essere proporzionata al task.

Quando una ricerca non produce valore sufficiente, l'agente deve evitare tentativi indefiniti.

---

## 24. Limiti di costo e token

I task che utilizzano modelli generativi o ricerca online devono poter avere limiti di risorse.

Le soglie possono dipendere da:

- task;
- modello;
- complessità;
- numero di tentativi;
- quantità di contesto;
- ricerca esterna;
- costo previsto.

Quando una soglia viene raggiunta, l'agente deve:

1. fermarsi in modo controllato;
2. conservare il lavoro valido;
3. registrare il motivo;
4. proporre eventualmente un'alternativa;
5. richiedere intervento umano soltanto se necessario.

Le soglie concrete saranno definite in una specifica tecnica successiva.

---

## 25. Modelli e backend

Il workflow non deve dipendere da un particolare modello o provider.

Un singolo agente/orchestratore può impersonare più ruoli logici.

In futuro il lavoro può essere distribuito tra:

- modelli differenti;
- agenti differenti;
- modelli locali;
- servizi esterni;
- strumenti specializzati.

Il cambio di backend non deve richiedere la modifica del modello concettuale del progetto.

---

## 26. Memoria operativa

Gli agenti possono produrre appunti operativi durante il lavoro.

Questi appunti possono registrare:

- best practice;
- errori ricorrenti;
- strategie efficaci;
- strategie da evitare;
- decisioni operative;
- problemi risolti;
- osservazioni utili per task futuri.

La gestione di questa memoria è definita in OPERATIONAL-MEMORY-SPEC.md.

La memoria operativa non modifica automaticamente la costituzione o le specifiche.

Una regola sufficientemente importante può essere proposta per l'inserimento nelle specifiche appropriate.

---

## 27. Persistenza delle decisioni

Le decisioni importanti devono essere conservate in una forma persistente.

Non devono esistere esclusivamente all'interno del contesto temporaneo di un modello.

Quando possibile, una decisione deve essere associata alla risorsa o al workflow che riguarda.

Questo permette agli agenti futuri di evitare richieste duplicate e di comprendere le decisioni precedenti.

---

## 28. Audit

Le operazioni rilevanti devono poter essere ricostruite.

Quando appropriato devono essere registrati:

- agente o modello;
- data;
- risorsa interessata;
- operazione;
- risultato;
- eventuale approvazione;
- eventuale costo.

L'audit deve essere proporzionato.

Non è necessario conservare ogni dettaglio tecnico quando non produce valore.

---

## 29. Reversibilità

Il sistema deve privilegiare operazioni reversibili.

Quando una modifica automatica è errata deve essere possibile, quando tecnicamente possibile:

- identificarla;
- comprenderne l'origine;
- ripristinare lo stato precedente;
- correggerla;
- ripetere il task.

Le operazioni irreversibili richiedono maggiore cautela.

---

## 30. Idempotenza

Le operazioni ripetibili dovrebbero essere idempotenti quando possibile.

Ripetere un task non dovrebbe causare:

- duplicazione di fonti;
- duplicazione di media;
- duplicazione di temi;
- perdita di decisioni;
- sovrascrittura di modifiche manuali.

Questo principio è particolarmente importante per task automatici periodici.

---

## 31. Comunicazione con gli utenti

Il workflow può integrare sistemi esterni di comunicazione.

In particolare, StamoTenti può utilizzare la posta elettronica per:

- inviare contenuti;
- ricevere feedback;
- mantenere conversazioni;
- raccogliere osservazioni.

Il feedback degli utenti non diventa automaticamente contenuto editoriale pubblico.

La gestione tecnica della posta sarà definita da una specifica dedicata quando necessario.

---

## 32. Sicurezza e separazione dei permessi

I permessi tecnici e i permessi editoriali devono rimanere distinti.

Avere accesso in lettura a uno storage non implica il diritto di pubblicare il contenuto.

Avere accesso in scrittura non implica il diritto di renderlo pubblico.

Gli agenti devono avere soltanto le capacità tecniche necessarie al task.

Le regole dettagliate delle capacità degli agenti sono definite in AGENT-ROLES-SPEC.md.

---

## 33. Storage

Il workflow non vincola StamoTenti a uno specifico sistema di storage.

Le risorse possono essere conservate in:

- repository;
- storage privato;
- storage pubblico;
- archivi scientifici;
- servizi esterni;
- sistemi futuri.

L'identità concettuale della risorsa deve rimanere indipendente dal provider.

La sostituzione di uno storage non deve richiedere la ricostruzione del modello dei contenuti.

---

## 34. Git

Git costituisce il principale sistema di versionamento del codice e della documentazione del progetto quando appropriato.

Le modifiche devono poter essere:

- identificate;
- confrontate;
- ripristinate;
- pubblicate tramite repository remoto.

Il workflow non richiede un sistema di versionamento editoriale più complesso quando Git è sufficiente.

---

## 35. Repository e backup

Quando una modifica importante viene committata, il repository remoto può costituire una copia persistente del lavoro tramite push.

Il workflow deve privilegiare procedure semplici e affidabili rispetto a infrastrutture di backup eccessivamente complesse.

Le risorse che non devono essere conservate nel repository devono utilizzare lo storage appropriato definito nelle relative specifiche.

---

## 36. Principio di non blocco

Quando una parte del workflow richiede approvazione, il sistema deve distinguere tra:

- attività bloccate;
- attività ancora eseguibili.

Gli agenti devono continuare il lavoro indipendente quando possibile.

Questo principio vale anche quando il lavoro è distribuito tra modelli o agenti differenti.

---

## 37. Principio di semplicità

Il workflow iniziale deve essere il più semplice possibile.

Non è necessario introdurre immediatamente:

- sistemi distribuiti complessi;
- code sofisticate;
- database dedicati;
- motori di regole;
- orchestratori proprietari;
- grafi semantici.

La complessità può essere introdotta quando la crescita del progetto la rende necessaria.

---

## 38. Modularità

Le specifiche devono descrivere capacità e comportamenti, non imporre un'unica architettura tecnica.

StamoTenti deve poter passare, senza modificare i principi fondamentali, da:

- un solo agente;
- un agente con più ruoli;
- più agenti;
- modelli locali;
- modelli esterni;
- sistemi ibridi.

La modularità è un requisito architetturale.

---

## 39. Gerarchia delle specifiche

In caso di conflitto:

1. TO-BE.md definisce la visione e i vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. le specifiche delle singole entità definiscono i relativi requisiti;
4. WORKFLOW-SPEC.md definisce il comportamento operativo generale;
5. AGENT-ROLES-SPEC.md definisce i ruoli logici;
6. OPERATIONAL-MEMORY-SPEC.md definisce la memoria operativa;
7. le specifiche tecniche definiscono l'implementazione;
8. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.

---

## 40. Principio finale

Il workflow di StamoTenti deve permettere agli agenti di lavorare molto autonomamente, mantenendo contemporaneamente:

- controllo umano sulle decisioni realmente importanti;
- possibilità di intervento manuale;
- persistenza delle decisioni;
- reversibilità quando possibile;
- controllo dei costi;
- rispetto dei diritti;
- modularità;
- semplicità.

Il workflow deve rendere il sistema più efficace, non più burocratico.

