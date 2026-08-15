# StamoTenti — DISTRIBUTION SPECIFICATION

## 1. Scopo

Questo documento definisce la distribuzione e la diffusione dei contenuti di StamoTenti.

La distribuzione comprende:

- pubblicazione sul sito;
- pubblicazione delle traduzioni;
- newsletter;
- sequenze email;
- distribuzione di materiali agli utenti autorizzati;
- condivisione su canali esterni;
- eventuale pubblicazione su social network;
- eventuale partecipazione a comunità online;
- monitoraggio di forum e discussioni;
- distribuzione di contenuti audio, video, documenti e altri media.

La distribuzione deve rispettare i diritti, i permessi e lo stato di visibilità dei contenuti e dei media.

---

## 2. Principio fondamentale

Il fatto che un contenuto sia disponibile nel sistema non significa che possa
essere distribuito.

Il sistema deve distinguere sempre tra:

- contenuto disponibile internamente;
- contenuto utilizzabile per ricerca;
- contenuto citabile;
- contenuto pubblicabile;
- contenuto redistribuibile.

Queste condizioni sono indipendenti.

In particolare:

- la leggibilità tecnica non implica pubblicabilità;
- la pubblicabilità sul sito non implica redistribuzione del file originale;
- la possibilità di citare una fonte non implica il diritto di riprodurla;
- la disponibilità pubblica di un contenuto non implica che ogni forma di
  riutilizzo sia autorizzata.

La gestione dettagliata dei permessi dei media è definita in MEDIA-SPEC.md.

---

## 3. Proprietà della distribuzione

La pubblicazione e la distribuzione devono essere considerate azioni distinte dalla preparazione del contenuto.

Un agente può:

- preparare un contenuto;
- adattarlo a un canale;
- verificare i requisiti;
- produrre un'anteprima;
- proporre una data;
- proporre un pubblico;
- produrre un report.

Queste attività non costituiscono automaticamente autorizzazione alla pubblicazione.

---

## 4. Approvazione

La distribuzione di contenuti pubblici deve rispettare APPROVAL-SPEC.md.

In particolare, gli agenti non devono pubblicare autonomamente contenuti quando l'azione richiede l'approvazione del proprietario.

L'approvazione deve poter essere registrata in modo persistente.

Una precedente approvazione non costituisce automaticamente autorizzazione permanente per contenuti differenti.

---

## 5. Sito

Il sito è il principale canale editoriale di StamoTenti.

La pubblicazione sul sito deve essere considerata distinta dalla distribuzione su canali esterni.

Il contenuto pubblicato deve rispettare:

- ARTICLE-SPEC.md;
- CONTENT-MODEL.md;
- VOCABULARY-SPEC.md;
- MULTILINGUAL-SPEC.md;
- SEO-SPEC.md;
- eventuali altre specifiche pertinenti.

---

## 6. Lingue

La distribuzione deve rispettare la lingua del contenuto.

Le lingue iniziali sono:

- italiano;
- inglese.

Quando un contenuto possiede traduzioni, le versioni linguistiche devono essere collegate secondo MULTILINGUAL-SPEC.md.

Gli elementi visibili associati alla distribuzione devono essere localizzati quando appropriato.

Questo comprende, quando visibili:

- titoli;
- descrizioni;
- categorie;
- temi;
- tag;
- menu;
- call to action;
- metadata;
- elementi di navigazione.

Le tassonomie e le classificazioni non devono assumere automaticamente che un termine italiano possa essere mostrato invariato nella versione inglese.

---

## 7. Traduzioni

La pubblicazione di una traduzione deve mantenere il collegamento con il contenuto originale.

Gli agenti possono preparare le traduzioni senza richiedere una revisione manuale dell'intero articolo quando il workflow lo consente.

Il proprietario non deve essere obbligato ad approvare individualmente ogni traduzione ordinaria.

Eventuali controlli automatici possono verificare:

- completezza;
- coerenza;
- presenza di elementi mancanti;
- corretto collegamento;
- eventuali anomalie.

---

## 8. Newsletter

La newsletter è un canale di distribuzione distinto dal sito.

La newsletter contiene principalmente un riepilogo degli articoli pubblicati dall'ultima uscita.

Il sistema può preparare automaticamente:

- elenco degli articoli;
- sintesi;
- struttura;
- collegamenti;
- versione italiana;
- versione inglese.

L'invio richiede comunque l'approvazione del proprietario secondo EMAIL-SPEC.md e APPROVAL-SPEC.md.

---

## 9. Sequenze email

Le sequenze email sono distinte dalla newsletter.

Possono essere utilizzate per:

- guide;
- percorsi didattici;
- meditazioni guidate;
- materiali audio;
- follow-up;
- esperienze a pagamento;
- altre future attività.

Le sequenze devono poter evolvere senza modificare il modello generale della newsletter.

L'invio resta subordinato alle regole di EMAIL-SPEC.md.

---

## 10. Distribuzione di materiali privati

I materiali privati possono essere distribuiti soltanto quando esiste un'autorizzazione appropriata.

Esempi:

- audio allegati a guide a pagamento;
- PDF acquistati dagli utenti;
- materiali riservati;
- file disponibili soltanto a specifici destinatari.

Un agente che può leggere un materiale non è automaticamente autorizzato a distribuirlo.

Il sistema deve verificare almeno:

- stato del materiale;
- destinatario;
- motivo della distribuzione;
- eventuali limitazioni;
- canale di distribuzione.

---

## 11. Materiali non pubblicabili

Alcuni materiali possono essere utilizzabili internamente ma non pubblicabili.

Esempi:

- libri acquistati in formato digitale;
- PDF con diritti limitati;
- EPUB acquistati;
- documenti forniti privatamente;
- materiali soggetti a licenze restrittive.

Questi materiali possono essere utilizzati dagli agenti per attività autorizzate, ma non devono essere copiati automaticamente nel repository pubblico o in uno storage pubblico.

---

## 12. Storage

Il sistema può utilizzare più ambienti di storage.

Gli ambienti possono comprendere:

- repository Git;
- storage pubblico;
- storage privato;
- storage temporaneo;
- servizi specializzati;
- eventuali repository di ricerca;
- eventuali servizi di archiviazione a lungo termine.

La scelta dello storage non deve essere vincolata a un singolo servizio.

L'importante è mantenere la distinzione tra:

- materiale pubblico;
- materiale privato;
- materiale temporaneo.

---

## 13. Distribuzione di audio e video

Audio e video possono essere:

- pubblici;
- privati;
- riservati a utenti autorizzati;
- allegati a guide;
- distribuiti tramite email;
- ospitati su servizi esterni.

Il sistema deve scegliere il canale in funzione dello stato del media e dell'utilizzo previsto.

Non devono essere utilizzati GitHub o il repository principale come storage obbligatorio per file di grandi dimensioni o materiali riservati quando esistono soluzioni più appropriate.

---

## 14. Canali esterni

I canali esterni possono essere utilizzati per:

- far conoscere gli articoli;
- condividere contenuti;
- raggiungere nuovi lettori;
- partecipare a discussioni;
- intercettare domande pertinenti;
- monitorare interessi e problemi degli utenti.

Ogni canale deve essere trattato secondo le proprie caratteristiche.

Non deve essere applicata automaticamente la stessa strategia a tutti i canali.

---

## 15. Telegram

Telegram può essere utilizzato come canale di distribuzione quando appropriato.

La distribuzione su Telegram deve essere considerata separata dal monitoraggio
delle comunità.

Il sistema può preparare contenuti per Telegram, ma la pubblicazione deve
rispettare le autorizzazioni previste dal workflow.

Gli agenti possono preparare:

- post;
- riassunti;
- collegamenti;
- risposte proposte;
- messaggi adattati al canale.

La pubblicazione automatica non è prevista come comportamento predefinito.

Il proprietario può utilizzare l'assistenza degli agenti per preparare manualmente i messaggi.

---

## 16. Reddit e forum

Reddit, forum e comunità analoghe non devono essere trattati principalmente come canali di autopubblicazione.

Il sistema deve privilegiare il monitoraggio delle discussioni.

Un ruolo di monitoraggio può:

- osservare comunità pertinenti;
- individuare discussioni rilevanti;
- riconoscere domande attinenti agli argomenti di StamoTenti;
- identificare opportunità di intervento;
- segnalare discussioni interessanti;
- fornire un breve riassunto;
- indicare il motivo della rilevanza;
- proporre, quando utile, una possibile risposta.

Il ruolo non deve pubblicare automaticamente.

---

## 17. Notifica delle discussioni pertinenti

Quando viene individuata una discussione pertinente, il sistema dovrebbe notificare il proprietario.

La notifica dovrebbe essere sintetica e contenere almeno:

- comunità;
- discussione;
- motivo della rilevanza;
- sintesi della questione;
- eventuale collegamento con un articolo;
- eventuale collegamento con una guida;
- eventuale possibilità di fornire una risposta utile.

La notifica non deve essere generata per ogni discussione vagamente correlata.

Il sistema deve privilegiare precisione e utilità rispetto al volume.

---

## 18. Assistenza alla risposta nei forum

Quando una discussione è pertinente, l'agente può aiutare il proprietario a:

- comprendere il problema;
- verificare le informazioni;
- trovare fonti;
- individuare articoli pertinenti;
- trovare collegamenti originali;
- preparare una risposta;
- verificare che la risposta sia appropriata alla comunità.

La pubblicazione rimane manuale.

L'agente non deve simulare una partecipazione umana automatizzata.

---

## 19. Principio anti-spam

StamoTenti non deve utilizzare sistemi automatici per produrre una presenza artificiale nelle comunità.

Non devono essere introdotti comportamenti come:

- pubblicazione indiscriminata;
- risposte automatiche a discussioni;
- inserimento sistematico di link;
- messaggi ripetitivi;
- autopromozione fuori contesto;
- generazione di discussioni artificiali.

La partecipazione deve essere pertinente e utile.

---

## 20. Link al sito

Quando il proprietario decide di partecipare a una discussione esterna, può essere utile collegare un articolo del sito.

Il link deve essere utilizzato quando:

- è realmente pertinente;
- aggiunge valore;
- risponde alla domanda;
- non costituisce semplice promozione.

Il sistema deve evitare di trasformare la distribuzione in un'attività di link dropping.

---

## 21. Canali social

Eventuali social network possono essere utilizzati per:

- annunciare nuovi articoli;
- condividere approfondimenti;
- distribuire estratti;
- presentare materiali;
- comunicare novità.

Il contenuto deve essere adattato al canale.

La pubblicazione automatica deve essere subordinata alle autorizzazioni stabilite dal workflow.

---

## 22. Monitoraggio delle comunità

Il monitoraggio può essere periodico.

La frequenza deve essere sostenibile rispetto a:

- volume delle comunità;
- numero di discussioni;
- costi computazionali;
- utilità delle notifiche;
- capacità del proprietario di intervenire.

Non è necessario controllare ogni comunità continuamente.

La periodicità deve essere adattata al valore reale del monitoraggio.

---

## 23. Monitoraggio delle novità

Il sistema può monitorare:

- nuove discussioni;
- nuove domande;
- nuove fonti;
- nuove pubblicazioni;
- novità nei temi di interesse;
- cambiamenti nelle comunità.

Il monitoraggio deve essere distinto dalla pubblicazione.

Un ruolo che osserva una comunità non riceve automaticamente il permesso di pubblicarvi.

---

## 24. Rilevanza

La rilevanza di una discussione può essere valutata in base a:

- corrispondenza con i temi del sito;
- corrispondenza con articoli esistenti;
- corrispondenza con guide;
- possibilità di fornire un contributo concreto;
- qualità della discussione;
- presenza di una domanda reale;
- possibilità di correggere un errore;
- possibilità di individuare un nuovo problema di ricerca.

Una semplice coincidenza lessicale non è sufficiente.

---

## 25. Nuove opportunità editoriali

Il monitoraggio esterno può produrre segnali utili per il progetto.

Gli agenti possono segnalare:

- domande ricorrenti;
- incomprensioni;
- controversie;
- argomenti emergenti;
- nuove fonti;
- lacune del sito;
- possibili collegamenti tra temi.

Questi segnali non determinano automaticamente la creazione di un articolo.

La decisione editoriale rimane del proprietario.

---

## 26. Distribuzione multilingue

Quando un contenuto viene distribuito in più lingue, ogni versione deve essere coerente con la relativa lingua.

Gli agenti possono preparare versioni italiane e inglesi.

Quando un canale utilizza una lingua specifica, il sistema deve preferire il contenuto nella lingua appropriata.

Non deve essere tradotto automaticamente un contenuto quando il canale non lo richiede.

---

## 27. Localizzazione

La distribuzione multilingue può richiedere adattamenti oltre alla semplice traduzione.

Possono essere adattati:

- titolo;
- descrizione;
- call to action;
- tono;
- esempi;
- riferimenti culturali;
- hashtag;
- testo dei link;
- metadata.

Gli adattamenti non devono alterare il significato del contenuto originale.

---

## 28. Identità editoriale

La distribuzione deve mantenere riconoscibile l'identità di StamoTenti.

Tuttavia ogni canale può utilizzare una forma espressiva appropriata.

Il sistema non deve produrre lo stesso testo identico per tutti i canali quando un adattamento migliora la comunicazione.

---

## 29. SEO e distribuzione

La distribuzione esterna può contribuire alla scoperta dei contenuti.

Gli agenti possono utilizzare le informazioni provenienti dai canali esterni per:

- individuare domande frequenti;
- migliorare titoli;
- individuare terminologia utilizzata dagli utenti;
- scoprire nuovi argomenti;
- migliorare collegamenti;
- individuare opportunità di contenuto.

La distribuzione non deve essere progettata esclusivamente per manipolare il posizionamento.

SEO-SPEC.md definisce le strategie specifiche.

---

## 30. Analytics

Il sistema deve poter monitorare, quando i dati sono disponibili:

- visite provenienti dai canali;
- click;
- iscrizioni;
- conversioni;
- interazioni;
- contenuti più efficaci;
- discussioni che hanno prodotto visite;
- performance delle newsletter;
- performance delle sequenze.

Le metriche devono essere interpretate insieme agli analytics del sito.

---

## 31. Attribuzione

Quando possibile, il sistema dovrebbe distinguere la provenienza del traffico.

Possono essere utilizzati:

- parametri di campagna;
- URL dedicati;
- referrer;
- dati della piattaforma;
- altre informazioni disponibili.

L'attribuzione deve essere sufficientemente semplice da poter essere mantenuta nel tempo.

---

## 32. Privacy nella distribuzione

La distribuzione non deve esporre dati personali non necessari.

Gli agenti non devono pubblicare:

- indirizzi email;
- informazioni private;
- contenuti di conversazioni private;
- dati identificativi non necessari;
- materiali privati.

Le conversazioni private possono essere utilizzate internamente quando autorizzato, ma non devono diventare automaticamente contenuto pubblico.

---

## 33. Distribuzione di fonti

Una fonte utilizzata da un articolo non diventa automaticamente redistribuibile.

Il sistema deve distinguere:

- fonte utilizzabile per ricerca;
- fonte citabile;
- fonte collegabile;
- fonte pubblicabile;
- fonte redistribuibile.

La gestione dettagliata è definita in SOURCE-SPEC.md, CITATION-SPEC.md e MEDIA-SPEC.md.

---

## 34. Distribuzione di contenuti derivati

Un contenuto derivato può avere condizioni differenti dal materiale originale.

Esempi:

- una sintesi di un libro;
- un diagramma derivato da una fonte;
- un dataset trasformato;
- un estratto;
- una traduzione;
- un'immagine modificata.

La possibilità di distribuire il derivato deve essere verificata separatamente quando necessario.

---

## 35. Contenuti a pagamento

I contenuti associati a prodotti o guide a pagamento possono avere una distribuzione limitata.

Il sistema deve poter distinguere:

- contenuto pubblico;
- contenuto per iscritti;
- contenuto per utenti autorizzati;
- contenuto acquistato;
- contenuto riservato.

Un contenuto a pagamento non deve essere inserito automaticamente nei canali pubblici.

---

## 36. Scadenza dei diritti

Quando una risorsa possiede limiti temporali o condizioni specifiche di distribuzione, tali condizioni devono poter essere registrate.

Un agente non deve presumere che un'autorizzazione rimanga valida indefinitamente.

Quando la situazione non è chiara, deve segnalare la necessità di verifica.

---

## 37. Audit

Le azioni di distribuzione rilevanti devono poter essere ricostruite.

Quando appropriato devono essere registrati:

- contenuto distribuito;
- canale;
- data tecnica;
- agente o ruolo che ha preparato l'azione;
- approvazione;
- eventuale risultato;
- eventuali anomalie.

La registrazione deve essere proporzionata all'importanza dell'azione.

---

## 38. Errori di distribuzione

Quando una distribuzione fallisce, il sistema deve distinguere tra:

- errore tecnico;
- contenuto non valido;
- autorizzazione mancante;
- canale non disponibile;
- problema di autenticazione;
- problema di formato;
- errore di configurazione.

Gli errori devono poter essere notificati senza perdere la richiesta originale.

---

## 39. Retry

Le operazioni tecniche fallite possono essere ripetute automaticamente quando il rischio è basso.

Le operazioni che comportano una nuova pubblicazione devono evitare duplicazioni.

Il sistema deve poter riconoscere, quando possibile, se un contenuto è già stato pubblicato.

---

## 40. Cancellazione o ritiro

Quando un contenuto deve essere ritirato da un canale, il sistema deve poter registrare:

- contenuto;
- canale;
- motivo;
- decisione;
- eventuale sostituzione;
- eventuali conseguenze.

La cancellazione da un canale non implica automaticamente la cancellazione della fonte o del contenuto originale nel sistema.

---

## 41. Sostituibilità dei canali

Un canale esterno può essere sostituito o abbandonato.

Il modello non deve dipendere da una piattaforma specifica.

L'aggiunta o rimozione di un canale non deve richiedere la modifica del modello generale di distribuzione.

---

## 42. Sostituibilità dei ruoli

I ruoli incaricati della distribuzione e del monitoraggio possono cambiare.

Un ruolo può essere svolto da:

- Cloud Code;
- un altro agente;
- un modello locale;
- un servizio automatico;
- una combinazione di strumenti.

La specifica definisce responsabilità e vincoli, non l'identità del modello.

---

## 43. Budget computazionale

Le attività di distribuzione e monitoraggio devono utilizzare budget computazionali proporzionati.

Esempi:

- verifica di una pubblicazione → budget basso;
- preparazione di un post → budget basso o medio;
- monitoraggio di una comunità → budget basso o medio;
- analisi di una discussione complessa → budget medio;
- ricerca approfondita derivata da una discussione → budget più alto.

Le attività ricorrenti devono avere soglie sostenibili.

Il proprietario può richiedere esplicitamente un'analisi più onerosa.

Quando un'attività supera significativamente il budget previsto, l'agente dovrebbe preferire:

- risultato parziale;
- sintesi;
- richiesta di conferma;
- percorso più economico.

---

## 44. Notifiche

Le notifiche relative alla distribuzione devono essere:

- sintetiche;
- persistenti quando richiedono un'azione;
- prioritizzate;
- ricercabili;
- distinguibili dalle notifiche informative.

Una discussione esterna pertinente deve poter generare una notifica senza richiedere automaticamente una risposta.

---

## 45. Semplicità

Il sistema deve evitare di trasformare la distribuzione in una piattaforma complessa di social media management quando non è necessario.

Non devono essere introdotti automaticamente:

- pubblicazione su decine di piattaforme;
- automazioni di engagement;
- sistemi complessi di scheduling;
- CRM sociali;
- automazioni di risposta.

La complessità deve essere introdotta soltanto quando il progetto dimostra di averne bisogno.

---

## 46. Principio di intervento umano

Il sistema deve favorire un utilizzo umano dei canali esterni.

Le automazioni possono assistere il proprietario nella preparazione,
verifica, programmazione e analisi.

Non devono però trasformare automaticamente il monitoraggio in partecipazione
pubblica né la preparazione in pubblicazione autorizzata.

In particolare:

- Reddit e forum devono essere principalmente monitorati;
- Telegram può essere assistito ma non deve diventare un canale di autopubblicazione indiscriminata;
- le risposte alle comunità devono poter essere preparate dagli agenti;
- la decisione di partecipare rimane del proprietario.

Gli agenti devono aiutare il proprietario a intervenire meglio, non sostituirlo nella partecipazione alle comunità.

---

## 47. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. MEDIA-SPEC.md definisce i media;
4. SOURCE-SPEC.md definisce le fonti;
5. CITATION-SPEC.md definisce le citazioni;
6. MULTILINGUAL-SPEC.md definisce il multilingua;
7. EMAIL-SPEC.md definisce le email;
8. APPROVAL-SPEC.md definisce le approvazioni;
9. SECURITY-SPEC.md definisce sicurezza e accessi;
10. DISTRIBUTION-SPEC.md definisce distribuzione e monitoraggio;
11. WORKFLOW-SPEC.md definisce workflow e ruoli;
12. le specifiche tecniche definiscono l'implementazione;
13. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
