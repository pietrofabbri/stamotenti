# StamoTenti — MONITORING SPECIFICATION

## 1. Scopo

Questo documento definisce i principi per il monitoraggio operativo di StamoTenti.

Il monitoraggio serve a individuare:

- problemi;
- regressioni;
- anomalie;
- opportunità di miglioramento;
- deterioramenti delle performance;
- errori nei workflow;
- problemi di sicurezza;
- problemi editoriali;
- problemi di distribuzione;
- problemi di qualità del sito.

Il monitoraggio non deve diventare una forma di complessità fine a sé stessa.

---

## 2. Principio fondamentale

Si monitora ciò che può produrre un'informazione utile per:

- intervenire;
- prevenire un problema;
- migliorare il sistema;
- valutare una decisione;
- proteggere persone, contenuti o infrastruttura.

Non si monitora qualcosa semplicemente perché è tecnicamente possibile farlo.

---

## 3. Liste aperte

Gli elenchi presenti in questa specifica sono esemplificativi e non esaustivi.

Nuove categorie di monitoraggio possono essere introdotte quando emergono esigenze reali.

Il sistema deve evitare di trasformare gli elenchi in vincoli che impediscano l'evoluzione.

---

## 4. Proporzionalità

Il livello di monitoraggio deve essere proporzionato:

- al rischio;
- all'importanza della risorsa;
- alla frequenza di modifica;
- al costo del monitoraggio;
- al valore dell'informazione ottenuta;
- alla possibilità di intervenire.

---

## 5. Monitoraggio continuo e periodico

Non tutto deve essere monitorato continuamente.

Quando è sufficiente un controllo periodico, deve essere preferito un controllo periodico.

Il monitoraggio continuo deve essere riservato soprattutto a ciò che richiede una reazione tempestiva.

---

## 6. Periodicità sostenibile

Le attività periodiche devono avere una frequenza sostenibile.

Un controllo troppo frequente può:

- consumare risorse;
- produrre rumore;
- generare falsi positivi;
- aumentare il carico sugli agenti;
- rendere il sistema difficile da mantenere.

La periodicità deve quindi essere rivalutata in base all'esperienza reale.

---

## 7. Segnalazioni

Una segnalazione dovrebbe essere generata quando esiste una ragionevole probabilità che richieda attenzione.

Il sistema deve evitare notifiche inutili.

Una buona segnalazione deve indicare, quando possibile:

- cosa è successo;
- perché può essere importante;
- quando è stato rilevato;
- quale risorsa è coinvolta;
- quale ruolo può occuparsene;
- quale azione potrebbe essere appropriata.

---

## 8. Severità

Gli eventi possono essere classificati, in modo non necessariamente rigido, secondo livelli di severità.

Un modello possibile è:

- informativo;
- basso;
- medio;
- alto;
- critico.

La classificazione deve essere usata per aiutare la priorità, non per creare burocrazia.

---

## 9. Salute del sito

Devono poter essere rilevati, quando appropriato:

- pagine non raggiungibili;
- errori HTTP;
- link rotti;
- risorse mancanti;
- immagini mancanti;
- problemi di rendering;
- problemi evidenti di navigazione;
- regressioni dopo modifiche.

---

## 10. Disponibilità

Il sistema può monitorare la disponibilità delle principali componenti pubbliche.

Non è necessario monitorare ogni singola risorsa con la stessa frequenza.

Le pagine e i servizi critici devono ricevere maggiore attenzione.

---

## 11. Link

I link interni ed esterni possono essere verificati periodicamente.

I link esterni devono essere trattati con particolare attenzione perché possono cambiare indipendentemente da StamoTenti.

Un link rotto non deve essere corretto automaticamente quando la sostituzione richiede una decisione editoriale.

---

## 12. Redirect

Devono essere monitorati i redirect rilevanti.

Quando una pagina viene spostata, il sistema dovrebbe cercare di evitare la perdita di riferimenti esistenti.

---

## 13. Sitemap

La sitemap può essere controllata periodicamente per verificare che rappresenti correttamente il contenuto pubblicabile.

---

## 14. Robots e indicizzazione

Le configurazioni che influenzano l'indicizzazione devono poter essere controllate.

Un cambiamento involontario che impedisca l'indicizzazione di contenuti importanti deve essere segnalato.

---

## 15. SEO tecnica

Il monitoraggio può includere:

- titoli;
- meta description;
- canonical;
- struttura degli heading;
- dati strutturati;
- sitemap;
- robots;
- link;
- performance;
- errori di indicizzazione.

SEO-SPEC.md definisce le strategie editoriali e tecniche relative alla ricerca.

Questa specifica definisce il monitoraggio.

---

## 16. GEO

Il monitoraggio può includere segnali relativi alla capacità dei contenuti di essere:

- trovati;
- compresi;
- citati;
- recuperati;
- sintetizzati;
- associati correttamente agli argomenti.

Il monitoraggio GEO deve rimanere orientato alla qualità e alla reperibilità delle informazioni, non alla manipolazione delle risposte dei sistemi AI.

---

## 17. Performance

Quando utile possono essere monitorati:

- tempi di caricamento;
- dimensioni delle pagine;
- immagini;
- script;
- richieste;
- errori;
- metriche Web Vitals o equivalenti.

Il monitoraggio deve privilegiare indicatori utili alla diagnosi.

---

## 18. Accessibilità

Il sito deve poter essere controllato periodicamente per problemi evidenti di accessibilità.

Il monitoraggio automatico non sostituisce la valutazione umana.

---

## 19. Coerenza grafica

Deve poter esistere un controllo periodico della coerenza visiva del sito.

Il relativo ruolo può verificare:

- tipografia;
- spaziature;
- gerarchia visiva;
- componenti;
- immagini;
- responsive behavior;
- coerenza tra pagine;
- anomalie introdotte da modifiche.

---

## 20. Contenuti

Il monitoraggio editoriale può individuare:

- pagine incomplete;
- contenuti duplicati;
- riferimenti mancanti;
- citazioni sospette;
- terminologia incoerente;
- problemi di traduzione;
- collegamenti interni mancanti.

Non deve però sostituire la decisione editoriale dell'autore.

---

## 21. Articoli

Un articolo può essere monitorato dopo la pubblicazione per:

- errori;
- link rotti;
- problemi tecnici;
- feedback;
- performance;
- reperibilità;
- aggiornamenti delle fonti.

Il monitoraggio non implica che l'articolo debba essere continuamente modificato.

---

## 22. Fonti

Le fonti possono essere monitorate per:

- disponibilità;
- cambiamenti;
- nuove edizioni;
- nuove pubblicazioni;
- correzioni;
- ritiro di contenuti;
- cambiamenti di URL.

Un cambiamento di una fonte non implica automaticamente una modifica dell'articolo.

---

## 23. Fonti scientifiche

Le fonti scientifiche possono essere monitorate per:

- nuove pubblicazioni;
- correzioni;
- retraction;
- aggiornamenti;
- nuove evidenze rilevanti.

La valutazione della rilevanza rimane distinta dal semplice rilevamento.

---

## 24. News e aggiornamenti tematici

StamoTenti può prevedere un monitoraggio periodico delle novità relative ai temi trattati.

La frequenza deve essere sostenibile.

L'obiettivo è fornire materiale utile all'autore, non generare automaticamente nuovi articoli.

---

## 25. Selezione delle news

Un agente può:

- cercare novità;
- filtrare risultati;
- raggruppare temi;
- evidenziare fonti rilevanti;
- segnalare possibili sviluppi.

L'agente non decide automaticamente che una novità debba diventare un articolo.

---

## 26. Forum e comunità

Possono essere monitorati forum, Reddit, Telegram e comunità pertinenti.

L'obiettivo principale è individuare:

- domande;
- discussioni;
- problemi ricorrenti;
- incomprensioni;
- richieste;
- temi emergenti.

---

## 27. Partecipazione alle comunità

Il monitoraggio non implica pubblicazione automatica.

StamoTenti non deve pubblicare automaticamente post promozionali su forum, Reddit o comunità simili.

L'agente può invece:

- segnalare una discussione;
- proporre una risposta;
- proporre un link;
- preparare materiale per l'utente.

La decisione di partecipare rimane umana salvo esplicita autorizzazione futura.

---

## 28. Telegram

I canali Telegram possono essere monitorati per individuare discussioni pertinenti.

La funzione primaria del monitoraggio è la segnalazione all'utente.

L'invio automatico di contenuti nei gruppi o canali non deve essere considerato comportamento predefinito.

---

## 29. Email

Il monitoraggio delle email può includere:

- volume;
- categorie;
- tempi di risposta;
- argomenti ricorrenti;
- feedback;
- problemi;
- andamento storico.

Il contenuto delle email deve rimanere soggetto alle regole di PRIVACY-SPEC.md.

---

## 30. Analytics email

I dati aggregati della mailing list possono essere utilizzati per comprendere:

- andamento delle iscrizioni;
- engagement;
- performance delle newsletter;
- differenze tra contenuti;
- andamento nel tempo.

Devono essere evitati collegamenti individuali non necessari.

---

## 31. Analytics del sito

I dati analitici possono essere confrontati con:

- pubblicazioni;
- newsletter;
- campagne;
- aggiornamenti;
- cambiamenti SEO;
- eventi esterni.

L'obiettivo è comprendere il comportamento complessivo del progetto.

---

## 32. Triangolazione

Quando utile, i dati possono essere triangolati tra:

- sito;
- email;
- feedback;
- fonti;
- performance;
- andamento delle ricerche;
- discussioni pubbliche.

La triangolazione deve produrre informazioni migliori, non aumentare inutilmente la raccolta di dati personali.

---

## 33. Report

I report devono essere orientati alle decisioni.

Un buon report dovrebbe distinguere:

- osservazione;
- interpretazione;
- ipotesi;
- raccomandazione.

Non deve presentare un'ipotesi come un fatto.

---

## 34. Report periodici

Possono essere prodotti report:

- tecnici;
- editoriali;
- SEO;
- GEO;
- email;
- performance;
- sicurezza;
- comunità;
- ricerca.

La frequenza deve essere adattata alla quantità di informazione realmente disponibile.

---

## 35. Agente performance

Un ruolo può raccogliere e sintetizzare dati relativi alle performance complessive.

Può confrontare:

- traffico;
- pubblicazioni;
- newsletter;
- engagement;
- conversioni eventualmente disponibili;
- feedback;
- andamento storico.

Non deve assumere che una correlazione costituisca causalità.

---

## 36. Agente SEO/GEO

Un ruolo può monitorare periodicamente:

- cambiamenti nei motori di ricerca;
- cambiamenti nei sistemi AI;
- pratiche SEO;
- pratiche GEO;
- evoluzione dei dati strutturati;
- nuove opportunità tecniche.

Il ruolo deve produrre raccomandazioni e non modificare automaticamente il sito salvo autorizzazione.

---

## 37. Agente news

Un ruolo può effettuare ricerche periodiche sulle novità relative ai temi di StamoTenti.

La frequenza deve essere sostenibile e può essere ridotta quando il rapporto segnale/rumore diventa basso.

---

## 38. Agente comunità

Un ruolo può monitorare discussioni pertinenti e inviare notifiche all'utente.

Può includere:

- forum;
- Reddit;
- Telegram;
- comunità tematiche;
- altre fonti pubbliche pertinenti.

Non deve rispondere automaticamente senza autorizzazione appropriata.

---

## 39. Agente grafico

Un ruolo può controllare periodicamente la coerenza grafica e la leggibilità del sito.

Può produrre:

- anomalie;
- screenshot o riferimenti alle pagine problematiche;
- suggerimenti;
- priorità.

---

## 40. Agente sicurezza

Un ruolo può monitorare:

- vulnerabilità;
- dipendenze;
- configurazioni;
- accessi anomali;
- segreti accidentalmente esposti;
- modifiche sospette.

Le procedure specifiche sono definite in SECURITY-SPEC.md.

---

## 41. Agente backup

Un ruolo può verificare che i backup previsti siano:

- eseguiti;
- accessibili;
- recenti;
- recuperabili quando richiesto.

Il backup non deve essere considerato valido soltanto perché il file esiste.

---

## 42. Test di ripristino

Quando proporzionato al rischio, devono essere effettuati test di ripristino.

Un backup mai verificato può essere considerato meno affidabile.

La frequenza dei test deve essere sostenibile.

---

## 43. Monitoraggio degli agenti

Il sistema può monitorare:

- esecuzioni;
- errori;
- durata;
- costi;
- risultati;
- fallimenti;
- interventi umani necessari.

Il monitoraggio degli agenti serve a migliorare il sistema.

---

## 44. Costi

Quando i costi sono significativi, devono poter essere monitorati:

- chiamate ai modelli;
- consumo;
- storage;
- servizi esterni;
- automazioni;
- frequenza dei workflow.

L'obiettivo è mantenere l'architettura economicamente sostenibile.

---

## 45. Token e contesto

Gli agenti devono evitare di utilizzare quantità di contesto sproporzionate quando il compito può essere svolto con meno informazioni.

Quando una domanda richiede un'analisi molto onerosa, l'agente dovrebbe poterlo segnalare.

Le domande operative ordinarie devono essere progettate per produrre risposte di dimensione ragionevole.

L'utente può comunque richiedere esplicitamente analisi più onerose.

---

## 46. Rumore

Il monitoraggio deve essere valutato anche in funzione del rumore prodotto.

Un sistema che genera troppe notifiche può diventare meno utile di un sistema che ne genera meno ma più pertinenti.

---

## 47. Priorità

Le segnalazioni possono essere ordinate secondo:

- urgenza;
- impatto;
- probabilità;
- reversibilità;
- costo;
- valore potenziale.

---

## 48. Nessuna azione automatica implicita

Il rilevamento di un problema non autorizza automaticamente una modifica.

Il monitoraggio produce evidenza o segnalazioni; l'azione successiva deve
seguire il workflow appropriato, salvo automazioni già esplicitamente
autorizzate per quel tipo di evento.

Il monitoraggio deve normalmente:

1. rilevare;
2. classificare;
3. spiegare;
4. proporre;
5. lasciare l'azione al workflow appropriato.

Le azioni automatiche devono essere definite separatamente.

---

## 49. Falsi positivi

Gli agenti devono poter segnalare un'incertezza.

Una segnalazione non deve essere formulata come certezza quando il sistema dispone soltanto di indizi.

---

## 50. Falsi negativi

L'assenza di una segnalazione non dimostra che non esista un problema.

I controlli automatici devono essere considerati strumenti di supporto.

---

## 51. Controllo umano

Il controllo umano rimane particolarmente importante quando:

- la decisione è editoriale;
- esiste rischio reputazionale;
- sono coinvolti dati personali;
- la modifica è difficile da reversibilizzare;
- la segnalazione è ambigua;
- il costo di un errore è elevato.

---

## 52. Privacy

Il monitoraggio deve rispettare PRIVACY-SPEC.md.

Non devono essere raccolti dati personali soltanto per migliorare il monitoraggio.

Il monitoraggio deve essere progettato secondo minimizzazione, limitazione delle finalità, conservazione proporzionata e accesso limitato. :contentReference[oaicite:1]{index=1}

---

## 53. Sicurezza

Il monitoraggio deve rispettare SECURITY-SPEC.md.

I log e i report non devono diventare una fonte alternativa di esposizione di informazioni riservate.

---

## 54. Backup

I risultati del monitoraggio che hanno valore storico possono essere conservati secondo BACKUP-SPEC.md.

Non tutto deve essere archiviato indefinitamente.

---

## 55. Memoria operativa

Le osservazioni utili e ricorrenti possono essere trasformate in conoscenza operativa secondo OPERATIONAL-MEMORY-SPEC.md.

Un evento isolato non deve diventare automaticamente una regola permanente.

---

## 56. Miglioramento del sistema

Quando una richiesta o un problema si presenta frequentemente, il sistema può valutare se automatizzarlo.

Esempi possibili:

- script;
- comando;
- controllo automatico;
- workflow;
- agente;
- report periodico.

L'automazione deve essere introdotta quando riduce realmente il lavoro o gli errori.

---

## 57. Stabilizzazione del codice

Può esistere un ruolo dedicato a individuare attività ripetitive che possono essere trasformate in strumenti permanenti.

Il ruolo può:

- individuare pattern;
- proporre automazioni;
- semplificare script;
- eliminare duplicazioni;
- migliorare la manutenibilità.

Non deve introdurre complessità soltanto per automatizzare attività rare.

---

## 58. Evoluzione degli strumenti

Gli strumenti di monitoraggio possono essere sostituiti.

Non deve essere costruita una dipendenza strutturale da un particolare provider.

---

## 59. Periodicità configurabile

Le frequenze definite dai workflow devono poter essere modificate senza riscrivere l'intero sistema.

La periodicità deve essere considerata un parametro operativo, non un principio architetturale.

---

## 60. Sostenibilità

Il sistema deve evitare:

- polling inutile;
- chiamate eccessive ai modelli;
- report ridondanti;
- notifiche ripetitive;
- controlli sovrapposti;
- storage inutile.

---

## 61. Conservazione dei risultati

I risultati del monitoraggio devono essere conservati soltanto quando hanno valore:

- operativo;
- storico;
- diagnostico;
- decisionale;
- di audit.

---

## 62. Audit

Quando una decisione importante deriva da un monitoraggio, dovrebbe essere possibile ricostruire almeno:

- quale segnale è stato osservato;
- quale interpretazione è stata data;
- quale decisione è stata presa.

Non è necessario conservare ogni dettaglio tecnico di ogni esecuzione.

---

## 63. Dashboard

Una dashboard può essere introdotta quando la quantità di informazioni lo giustifica.

Non è necessario creare una dashboard centralizzata all'inizio.

Report semplici possono essere sufficienti.

---

## 64. Notifiche

Le notifiche devono essere indirizzate al canale più appropriato.

Possibili canali includono:

- email;
- terminale;
- report;
- sistema di issue;
- messaggistica;
- altri strumenti futuri.

La lista è aperta.

---

## 65. Escalation

Un problema non risolto può essere progressivamente escalato.

La modalità di escalation deve essere proporzionata alla severità.

---

## 66. Fallimento del monitoraggio

Il fallimento di un controllo deve poter essere distinto dall'assenza di problemi.

Esempio:

- controllo riuscito → nessun problema;
- controllo riuscito → problema rilevato;
- controllo fallito → stato sconosciuto.

---

## 67. Dipendenze esterne

Quando un monitoraggio dipende da un servizio esterno, il sistema deve considerare la possibilità che quel servizio sia temporaneamente indisponibile.

Non devono essere generate conclusioni forti da dati incompleti.

---

## 68. Monitoraggio dei dati

I dati utilizzati per i report devono essere valutati per:

- completezza;
- qualità;
- coerenza;
- periodo;
- provenienza.

---

## 69. Correlazione e causalità

I report devono distinguere chiaramente:

- correlazione;
- causalità dimostrata;
- causalità ipotizzata;
- semplice coincidenza temporale.

Questo principio è particolarmente importante per performance, analytics e comportamento degli utenti.

---

## 70. Report per l'autore

I report devono essere utili all'autore.

Quando possibile devono terminare con:

- cosa è cambiato;
- cosa sembra importante;
- cosa richiede attenzione;
- cosa può essere ignorato;
- quali decisioni sono eventualmente richieste.

---

## 71. Nessun automatismo editoriale

Il monitoraggio non decide quali articoli pubblicare.

L'autore mantiene la decisione editoriale finale.

Gli agenti possono assistere:

- ricerca;
- confronto;
- confutazione;
- collegamento tra temi;
- aggiornamento delle fonti;
- individuazione di opportunità.

---

## 72. Aggiornamento delle specifiche

Il monitoraggio può individuare problemi nelle specifiche.

Un ruolo dedicato può proporre aggiornamenti quando:

- una regola viene frequentemente aggirata;
- una procedura è inutilmente complessa;
- emerge una nuova best practice;
- una tecnologia cambia;
- un principio è ambiguo.

La modifica effettiva delle specifiche segue il workflow di approvazione.

---

## 73. Agente di supporto alla revisione della Costituzione

Può esistere un agente di supporto alla revisione della Costituzione,
secondo la definizione stabilita nei documenti fondativi.

L'agente assiste l'autore nell'analisi della Costituzione di StamoTenti.

Non possiede autorità autonoma sulla Costituzione.

Può analizzare, criticare e proporre.

Non può approvare autonomamente modifiche ai documenti fondativi.

Il suo compito non è modificare autonomamente i documenti fondativi.

Il suo compito è rendere più facile una revisione consapevole quando emergono
tensioni, lacune o colli di bottiglia persistenti.

Il suo compito è:

- individuare tensioni tra principi;
- individuare regole che producono colli di bottiglia;
- individuare vincoli diventati inutilmente restrittivi;
- individuare lacune normative;
- individuare contraddizioni tra documenti;
- valutare se una procedura operativa sta rivelando un problema di principio;
- proporre modifiche;
- proporre semplificazioni;
- proporre nuove formulazioni;
- mantenere una visione storica delle modifiche già effettuate.

Il ruolo può inoltre tenere conto delle osservazioni provenienti da:

- workflow;
- agenti;
- errori;
- incidenti;
- richieste ricorrenti;
- revisioni;
- nuove esigenze del progetto;
- evoluzione tecnologica.

---

## 74. Colli di bottiglia costituzionali

Un collo di bottiglia è una regola, un principio o una relazione tra regole che impedisce frequentemente al sistema di svolgere un'attività ragionevole.

Non ogni difficoltà costituisce un collo di bottiglia.

Prima di proporre una modifica devono essere considerate, quando possibile:

- frequenza del problema;
- gravità;
- numero di workflow coinvolti;
- possibilità di risolverlo a livello operativo;
- costo della modifica;
- rischio introdotto dalla modifica;
- possibilità di mantenere il principio rendendo più flessibile la sua applicazione.

---

## 75. Livelli di intervento

Quando emerge un problema, il ruolo di revisione costituzionale dovrebbe considerare, in ordine preferenziale:

1. chiarimento operativo;
2. modifica di una procedura;
3. modifica di una specifica;
4. riorganizzazione delle specifiche;
5. modifica di un principio fondativo.

Non si dovrebbe modificare un principio fondativo quando il problema può essere risolto in modo sicuro a un livello inferiore.

---

## 76. Segnalazione di tensioni

Il ruolo può produrre segnalazioni quando due principi apparentemente legittimi producono conseguenze incompatibili.

La segnalazione dovrebbe distinguere:

- i principi coinvolti;
- il problema concreto;
- gli effetti osservati;
- le possibili interpretazioni;
- le possibili soluzioni;
- ciò che rimane incerto.

---

## 77. Proposte di emendamento

Una proposta di modifica dei documenti fondativi dovrebbe essere presentata come proposta non approvata.

Dovrebbe indicare, quando utile:

- testo attuale;
- problema individuato;
- motivazione;
- testo proposto;
- conseguenze previste;
- conseguenze indesiderate possibili;
- specifiche coinvolte;
- workflow che dovrebbero essere aggiornati.

La proposta non modifica automaticamente il documento.

---

## 78. Test degli emendamenti

Prima di approvare una modifica significativa, è opportuno verificare almeno alcuni casi concreti che abbiano prodotto il problema.

Quando possibile si dovrebbe verificare:

- comportamento precedente;
- comportamento con la modifica proposta;
- casi limite;
- eventuali nuovi comportamenti indesiderati.

---

## 79. Principio di minima modifica

Quando è necessario modificare una regola fondativa, deve essere preferita la modifica più piccola capace di risolvere il problema senza compromettere i principi che continuano a essere validi.

Una revisione non deve diventare una riscrittura generale senza necessità.

---

## 80. Nessuna auto-modifica della governance

Un agente non può modificare autonomamente le regole che definiscono la propria autorità.

Le proposte possono essere generate dagli agenti.

L'approvazione delle modifiche fondamentali rimane umana.

---

## 81. Memoria delle revisioni

Le revisioni importanti dovrebbero lasciare una traccia comprensibile di:

- problema che le ha motivate;
- decisione presa;
- motivazione;
- effetti attesi.

Questo permette di evitare che gli stessi problemi vengano riscoperti periodicamente.

---

## 82. Aggiornamento periodico

Il ruolo di revisione costituzionale non deve necessariamente essere eseguito con una periodicità fissa.

Può essere attivato:

- quando emergono colli di bottiglia;
- dopo incidenti significativi;
- dopo importanti cambiamenti architetturali;
- quando vengono introdotte nuove categorie di attività;
- durante la revisione generale del progetto.

Una revisione periodica può comunque essere utile quando la complessità del progetto aumenta.

---

## 83. Separazione dalla manutenzione ordinaria

Il ruolo costituzionale non deve occuparsi della normale manutenzione dei contenuti o del codice.

Il suo focus è verificare se il sistema di principi e specifiche continua a essere adeguato al progetto reale.

---

## 84. Evoluzione senza irrigidimento

L'esistenza di principi fondativi non deve impedire l'evoluzione del sistema.

Al contrario, il sistema deve poter riconoscere quando:

- una regola non serve più;
- una regola è troppo restrittiva;
- una regola è ambigua;
- una regola è duplicata;
- una regola è diventata obsoleta;
- una nuova esigenza richiede un principio non ancora esplicitato.

La stabilità deve derivare dalla chiarezza dei principi, non dalla difficoltà di modificarli.

---

## 73. Nuove best practice

Le best practice emerse dal monitoraggio possono essere raccolte nell'area prevista da OPERATIONAL-MEMORY-SPEC.md.

Devono essere separate dalle regole fondamentali.

---

## 85. Monitoraggio e flessibilità

Il monitoraggio non deve trasformare StamoTenti in un sistema rigidamente parametrizzato.

Il suo compito è fornire informazioni migliori per prendere decisioni migliori.

---

## 86. Obiettivo

Il sistema di monitoraggio deve permettere di:

- sapere quando qualcosa si rompe;
- capire quando qualcosa peggiora;
- individuare opportunità;
- ridurre lavoro ripetitivo;
- controllare costi;
- proteggere dati e infrastruttura;
- migliorare progressivamente il sito;
- mantenere il progetto sostenibile.

---

## 87. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi definiscono visione e principi;
2. PRIVACY-SPEC.md definisce i vincoli relativi ai dati personali;
3. SECURITY-SPEC.md definisce i principi di sicurezza;
4. MONITORING-SPEC.md definisce il monitoraggio;
5. le specifiche dei singoli domini definiscono i rispettivi workflow;
6. le specifiche tecniche definiscono l'implementazione;
7. il codice implementa le specifiche approvate.

Il monitoraggio non può autorizzare un trattamento vietato da una specifica superiore.
