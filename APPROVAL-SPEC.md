# StamoTenti — APPROVAL SPECIFICATION

## 1. Scopo

Questo documento definisce il modello generale delle approvazioni di
StamoTenti.

L'approvazione serve a distinguere:

- attività che un agente può eseguire autonomamente;
- attività che possono essere preparate ma richiedono una decisione;
- attività che possono essere eseguite soltanto dopo un'approvazione;
- attività che non possono essere eseguite dall'agente.

Le regole devono rimanere proporzionate al rischio e non devono
trasformare il progetto in un sistema burocratico.

---

## 2. Principio fondamentale

La capacità tecnica di eseguire un'azione non costituisce
automaticamente autorizzazione a eseguirla.

L'approvazione è una decisione distinta dall'esecuzione.

In particolare:

- una proposta non è un'approvazione;
- una bozza non è un'approvazione;
- il superamento di un test non è un'approvazione;
- una precedente approvazione non costituisce automaticamente
  autorizzazione permanente per azioni future differenti.

---

## 3. Azioni autonome

Le attività a basso rischio, reversibili e già autorizzate dal workflow
possono essere eseguite autonomamente.

Esempi possono comprendere:

- classificazione;
- ricerca;
- verifica;
- preparazione di bozze;
- traduzione;
- controlli automatici;
- produzione di report;
- manutenzione ordinaria.

La registrazione del risultato può essere richiesta quando ha valore
operativo.

---

## 4. Azioni soggette ad approvazione

Un'azione può richiedere approvazione quando presenta uno o più dei
seguenti elementi:

- pubblicazione;
- distribuzione esterna;
- invio di email;
- accesso o modifica di dati sensibili;
- modifica significativa delle autorizzazioni;
- modifica architetturale;
- operazione irreversibile;
- cambiamento rilevante di diritti o licenze;
- pubblicazione di materiali precedentemente privati;
- modifica di una regola fondamentale;
- costo superiore alle soglie operative;
- rischio significativo per sicurezza o privacy.

L'elenco è aperto.

La necessità di approvazione deve essere valutata in funzione
dell'azione concreta e del contesto.

---

## 5. Proposta

Quando è richiesta un'approvazione, l'agente deve preparare una proposta
sufficientemente concreta da permettere una decisione informata.

Quando rilevante, la proposta dovrebbe contenere:

- identificativo;
- azione richiesta;
- risorsa interessata;
- motivazione;
- evidenze;
- fonti;
- livello di certezza;
- rischi;
- alternative;
- conseguenze;
- costo previsto;
- eventuale strategia di rollback.

Una proposta incompleta può essere restituita all'agente per integrazione.

---

## 6. Coda persistente

Le richieste di approvazione devono poter essere conservate in una forma
persistente.

Ogni elemento dovrebbe contenere almeno:

- id;
- tipo;
- stato;
- priorità;
- data;
- proponente;
- risorsa interessata;
- proposta;
- motivazione.

Quando utile possono essere conservati anche:

- evidenze;
- riferimenti;
- dipendenze;
- scadenza;
- decisione;
- motivazione della decisione;
- timestamp dell'approvazione.

La coda non deve dipendere dalla memoria temporanea della conversazione.

---

## 7. Stati

Una richiesta di approvazione può avere stati come:

- pending;
- approved;
- rejected;
- modified;
- expired;
- superseded;
- cancelled.

Lo stato deve essere sufficientemente chiaro da distinguere una
decisione ancora pendente da una decisione già conclusa.

---

## 8. Decisione del proprietario

Quando l'approvazione è riservata al proprietario, il proprietario può:

- approvare;
- rifiutare;
- modificare;
- rimandare;
- chiedere ulteriori informazioni.

L'approvazione può riguardare l'azione proposta oppure una versione
modificata della proposta.

---

## 9. Approvazione contestuale

Un'approvazione deve essere collegata, quando rilevante, a:

- azione;
- risorsa;
- versione;
- destinatario;
- ambiente;
- condizioni applicabili.

Questo riduce il rischio che un'approvazione venga riutilizzata
impropriamente per un'azione differente.

---

## 10. Approvazioni di gruppo

Quando più richieste sono sostanzialmente equivalenti, possono essere
raggruppate.

Il raggruppamento non deve però nascondere differenze rilevanti di:

- rischio;
- destinatari;
- contenuto;
- diritti;
- costo;
- reversibilità.

Quando le condizioni differiscono in modo sostanziale, le richieste
devono poter essere valutate separatamente.

---

## 11. Approvazione delle email

L'invio di email che richiede approvazione non deve essere effettuato
senza una decisione approvativa valida.

Questo vale anche quando:

- la bozza è stata generata automaticamente;
- la risposta è stata verificata;
- l'invio era già programmato;
- la stessa tipologia di messaggio è stata approvata in precedenza.

Le regole specifiche delle email sono definite in EMAIL-SPEC.md.

---

## 12. Approvazione della distribuzione

La pubblicazione o distribuzione esterna deve rispettare i requisiti
specifici del canale.

La possibilità tecnica di pubblicare non costituisce approvazione.

Le regole di distribuzione sono definite in DISTRIBUTION-SPEC.md.

---

## 13. Approvazione dei media

Quando un media passa da:

- privato a pubblico;
- pending_review a pubblico;
- accesso controllato a distribuzione pubblica;

l'operazione può richiedere approvazione.

La decisione deve considerare:

- diritti;
- licenza;
- provenienza;
- destinatari;
- eventuali dati personali;
- condizioni d'uso.

MEDIA-SPEC.md definisce la gestione specifica dei media.

---

## 14. Approvazione delle modifiche

Le modifiche significative alle specifiche, al workflow, ai permessi o
all'architettura devono seguire CHANGE-MANAGEMENT-SPEC.md.

Questa specifica definisce il meccanismo generale di approvazione e non
sostituisce il processo di change management.

---

## 15. Sicurezza e privacy

Le approvazioni non possono autorizzare un trattamento che una regola
superiore vieta.

Un'approvazione deve quindi essere considerata valida soltanto se
l'azione rimane compatibile con:

- documenti fondativi;
- privacy;
- sicurezza;
- diritti;
- altre regole superiori applicabili.

L'approvazione non costituisce una deroga automatica a tali vincoli.

---

## 16. Approvazioni e testing

Il superamento dei test non equivale ad approvazione.

Un test fornisce evidenza.

L'approvazione costituisce invece una decisione autorizzativa.

Le due funzioni devono rimanere distinte.

---

## 17. Approvazioni e monitoring

Il monitoraggio può generare una proposta di intervento.

Il rilevamento di un problema non costituisce automaticamente
autorizzazione alla modifica.

---

## 18. Approvazioni e memoria operativa

Una decisione approvativa con valore futuro può essere registrata nella
memoria operativa quando appropriato.

La memoria operativa non sostituisce però il record persistente
dell'approvazione.

---

## 19. Scadenza

Un'approvazione può avere condizioni o una durata limitata quando:

- la situazione è temporanea;
- i diritti scadono;
- il contesto può cambiare;
- l'azione deve essere eseguita entro un intervallo specifico.

Quando una scadenza è rilevante, deve essere conservata nel record.

---

## 20. Revoca

Un'approvazione può essere revocata quando:

- emergono nuove informazioni;
- cambiano i diritti;
- cambiano i destinatari;
- cambiano le condizioni;
- emergono rischi;
- la decisione precedente non è più appropriata.

La revoca non deve essere utilizzata per alterare retroattivamente la
storia della decisione.

---

## 21. Override manuale

Il proprietario deve poter modificare una decisione precedentemente
proposta o approvata quando il workflow lo consente.

Gli agenti non devono tentare di ripristinare automaticamente una
decisione precedente contro un override manuale intenzionale.

---

## 22. Audit

Le approvazioni rilevanti devono poter essere ricostruite.

Quando appropriato devono essere registrati:

- chi ha deciso;
- quale azione è stata autorizzata;
- quale risorsa era interessata;
- quale versione era coinvolta;
- quando è stata presa la decisione;
- eventuali condizioni;
- eventuale motivazione.

Il livello di dettaglio deve essere proporzionato al rischio.

---

## 23. Fallimento dell'approvazione

Un'approvazione non disponibile deve produrre uno stato esplicito.

L'agente deve:

1. conservare il lavoro già valido;
2. lasciare la richiesta nello stato appropriato;
3. indicare cosa è ancora necessario;
4. continuare il lavoro indipendente quando possibile.

Una richiesta pendente non deve bloccare attività non dipendenti.

---

## 24. Approvazioni duplicate

Prima di creare una nuova richiesta, il sistema dovrebbe verificare
se esiste già una richiesta relativa alla stessa azione e alle stesse
condizioni.

Quando una richiesta precedente è ancora valida, deve essere
riutilizzata invece di crearne una duplicata.

L'idempotenza è particolarmente importante per automazioni periodiche.

---

## 25. Semplicità

Il sistema di approvazione deve rimanere semplice.

Non devono essere introdotti prematuramente:

- workflow complessi;
- sistemi multilivello di firma;
- motori di regole proprietari;
- code distribuite;
- sistemi di ticketing dedicati;

quando una struttura persistente semplice è sufficiente.

La complessità può crescere successivamente quando il volume o il
rischio del progetto lo richiederanno.

---

## 26. Principio finale

L'approvazione deve svolgere una funzione precisa:

permettere al sistema di automatizzare il lavoro ordinario mantenendo
il controllo umano sulle decisioni realmente importanti.

Non deve diventare:

- un ostacolo alla ricerca;
- una duplicazione del workflow;
- una richiesta di conferma per ogni operazione;
- un'autorizzazione generale e indefinita.

La regola guida è:

> controllare le decisioni ad alto impatto, lasciare autonomo il resto.

---

## 27. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi definiscono principi e vincoli superiori;
2. PRIVACY-SPEC.md e SECURITY-SPEC.md definiscono i relativi vincoli;
3. le specifiche di dominio definiscono i requisiti specifici;
4. APPROVAL-SPEC.md definisce il modello generale delle approvazioni;
5. CHANGE-MANAGEMENT-SPEC.md definisce la gestione delle modifiche;
6. WORKFLOW-SPEC.md definisce le procedure operative;
7. le specifiche tecniche definiscono l'implementazione;
8. il codice implementa quanto approvato.

L'approvazione non può essere utilizzata per aggirare una regola
superiore.
