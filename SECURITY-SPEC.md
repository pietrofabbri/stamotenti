# StamoTenti — SECURITY SPECIFICATION

## 1. Scopo

Questo documento definisce i principi di sicurezza di StamoTenti.

La sicurezza deve proteggere:

- contenuti;
- fonti;
- media;
- dati degli utenti;
- account;
- credenziali;
- repository;
- storage;
- email;
- agenti;
- workflow;
- approvazioni;
- sistemi di distribuzione;
- infrastruttura.

La sicurezza deve essere sufficientemente forte da proteggere il progetto senza rendere inutilmente difficile il lavoro degli agenti.

---

## 2. Principio fondamentale

Un agente deve poter fare ciò che gli serve per svolgere il proprio compito, ma non deve ricevere automaticamente capacità ulteriori.

I permessi devono essere determinati dalla capacità richiesta dall'azione.

Il ruolo dell'agente descrive una responsabilità.

La capacità autorizzata descrive ciò che può concretamente fare.

Questi due concetti non devono essere confusi.

Gli elenchi presenti in questa specifica sono normalmente esemplificativi e non esaustivi.
Una nuova capacità, risorsa, ambiente, strumento o categoria può essere introdotta senza modificare necessariamente i principi generali della specifica, purché rimanga coerente con essi.

Quando un elenco deve invece essere considerato chiuso, la specifica deve dichiararlo esplicitamente.

---

## 3. Capacità

Le capacità possono comprendere:

- leggere;
- cercare;
- classificare;
- creare;
- modificare;
- cancellare;
- pubblicare;
- distribuire;
- inviare;
- approvare;
- modificare configurazioni;
- modificare autorizzazioni;
- eseguire codice;
- accedere a servizi esterni.

Un agente può possedere una capacità soltanto quando il workflow la rende necessaria.

---

## 4. Principio del minimo necessario

Un ruolo dovrebbe ricevere il minimo insieme di capacità sufficiente per completare il proprio compito.

Questo non significa creare permessi estremamente granulari per ogni singola operazione.

La granularità deve essere proporzionata al rischio.

Un sistema troppo frammentato può diventare più difficile da comprendere e quindi meno sicuro.

---

## 5. Lettura

Il permesso di lettura consente di accedere al contenuto.

Non implica automaticamente:

- possibilità di citarlo;
- possibilità di modificarlo;
- possibilità di pubblicarlo;
- possibilità di redistribuirlo.

La distinzione è fondamentale per fonti e media.

---

## 6. Ricerca

Il permesso di ricerca consente di utilizzare una risorsa per attività di ricerca o analisi.

Può essere più ampio del semplice accesso a un file, ma non costituisce autorizzazione alla pubblicazione.

---

## 7. Citazione

Il permesso di citazione consente di utilizzare una fonte in un contesto citazionale appropriato.

Non implica che il contenuto completo possa essere riprodotto.

Le regole dettagliate sono definite in CITATION-SPEC.md.

---

## 8. Pubblicazione

Il permesso di pubblicazione consente di rendere un contenuto disponibile attraverso un canale pubblico autorizzato.

Non implica automaticamente:

- distribuzione su ogni canale;
- redistribuzione del file originale;
- invio email;
- pubblicazione su piattaforme esterne.

Ogni canale può avere requisiti differenti.

---

## 9. Redistribuzione

La redistribuzione è distinta dalla pubblicazione.

Un contenuto può essere pubblicabile sul sito ma non redistribuibile come file.

Esempio:

Un libro può essere citato in un articolo senza che il PDF acquistato possa essere allegato all'articolo.

---

## 10. Dati pubblici e privati

Ogni risorsa rilevante deve avere uno stato di visibilità o distribuzione coerente con MEDIA-SPEC.md e SOURCE-SPEC.md.

Gli stati possono comprendere:

- pubblico;
- privato;
- limitato;
- riservato;
- temporaneo.

Lo stato non deve essere interpretato da solo come un insieme completo di permessi.

---

## 11. Separazione delle condizioni

Il sistema deve distinguere sempre tra:

- posso leggere;
- posso usare per ricerca;
- posso citare;
- posso pubblicare;
- posso redistribuire.

Queste condizioni non sono equivalenti.

Una risorsa può avere qualsiasi combinazione coerente di queste proprietà.

---

## 12. Agenti

Un agente non deve essere considerato automaticamente affidabile soltanto perché utilizza un modello potente.

La sicurezza deve essere applicata alle capacità concesse all'agente.

Il modello utilizzato può cambiare.

---

## 13. Ruoli

I ruoli sono responsabilità operative.

Esempi:

- ricerca;
- scrittura;
- revisione;
- traduzione;
- gestione fonti;
- gestione email;
- monitoraggio comunità;
- SEO;
- sicurezza;
- backup;
- analytics.

Un ruolo non deve implicare automaticamente tutte le capacità tecniche necessarie.

Le capacità vengono assegnate dal workflow concreto.

---

## 14. Cloud Code

Cloud Code può svolgere più ruoli.

Non deve essere trattato come un singolo profilo di sicurezza immutabile.

Lo stesso ambiente può:

- leggere fonti;
- preparare articoli;
- analizzare email;
- preparare modifiche;
- eseguire controlli;
- produrre report.

Le capacità effettivamente utilizzabili devono essere limitate al compito in corso quando ciò è tecnicamente possibile.

---

## 15. Modelli locali

I modelli locali, inclusi eventuali modelli eseguiti tramite Ollama, possono essere utilizzati per compiti appropriati.

Il fatto che un modello sia locale non implica automaticamente autorizzazione completa.

Deve comunque rispettare:

- stato dei dati;
- permessi;
- workflow;
- sicurezza;
- privacy.

---

## 16. Segreti

Le credenziali non devono essere inserite:

- negli articoli;
- nelle specifiche pubbliche;
- nei prompt salvati;
- nei log non protetti;
- nei repository pubblici;
- nei file di configurazione versionati quando contengono valori sensibili.

I segreti devono essere conservati tramite meccanismi appropriati all'ambiente.

---

## 17. Token e chiavi API

Le chiavi API devono essere:

- conservate fuori dai file pubblici;
- sostituibili;
- revocabili;
- limitate quando possibile;
- utilizzate soltanto dai componenti che ne hanno bisogno.

Non devono essere condivise inutilmente tra agenti.

---

## 18. Credenziali di servizi esterni

Ogni integrazione esterna dovrebbe utilizzare credenziali dedicate quando ciò è ragionevole.

Esempi:

- GitHub;
- email;
- storage;
- analytics;
- servizi SEO;
- servizi di distribuzione;
- Telegram;
- altri servizi futuri.

La compromissione di una credenziale non dovrebbe comportare automaticamente la compromissione dell'intero progetto.

---

## 19. GitHub

L'accesso al repository deve essere limitato alle operazioni necessarie.

Le capacità possono comprendere:

- lettura;
- modifica;
- commit;
- push;
- gestione branch;
- gestione pull request;
- gestione configurazioni.

Non tutte devono essere concesse automaticamente allo stesso ruolo.

---

## 20. Commit

Gli agenti possono preparare commit quando autorizzati.

Il commit non equivale alla pubblicazione sul sito.

Il commit non equivale alla distribuzione pubblica.

Il workflow deve poter distinguere:

- modifica;
- commit;
- push;
- deploy;
- pubblicazione.

---

## 21. Push

Il push deve essere considerato un'operazione distinta dal commit.

Il fatto che un agente possa creare commit non implica automaticamente che possa fare push.

Quando il workflow lo consente, il push può essere automatizzato.

Quando l'operazione presenta un rischio significativo, deve essere sottoposta a controllo secondo APPROVAL-SPEC.md.

---

## 22. Deploy

Il deploy deve essere distinto dal push.

Una modifica presente nel repository non deve essere considerata automaticamente pubblicata.

Il sistema deve poter verificare:

- stato del repository;
- stato del build;
- test;
- configurazione;
- destinazione del deploy.

---

## 23. Pubblicazione

La pubblicazione deve avvenire soltanto attraverso percorsi autorizzati.

Un agente che può modificare un articolo non deve automaticamente poterlo rendere pubblico.

Quando possibile, il sistema deve utilizzare controlli tecnici che impediscano pubblicazioni accidentali.

---

## 24. Storage

Gli storage devono essere classificati in funzione della sensibilità dei dati.

Esempi:

- repository pubblico;
- repository privato;
- object storage pubblico;
- object storage privato;
- storage temporaneo;
- storage locale.

Un file privato non deve essere trasferito automaticamente in uno storage pubblico.

---

## 25. Media

I media devono rispettare MEDIA-SPEC.md.

In particolare, un agente deve poter sapere se un media è:

- pubblico;
- privato;
- leggibile;
- utilizzabile per ricerca;
- citabile;
- pubblicabile;
- redistribuibile.

L'agente non deve dover dedurre queste proprietà dal semplice nome del file.

---

## 26. Fonti

Le fonti devono rispettare SOURCE-SPEC.md.

La disponibilità di una fonte per la ricerca non implica la possibilità di pubblicare il file originale.

Le fonti acquistate o soggette a restrizioni devono essere trattate con particolare attenzione.

---

## 27. Email

L'accesso alle email deve essere limitato alle capacità necessarie.

Un agente che può leggere email non deve automaticamente poterle inviare.

Un agente che può preparare una risposta non deve automaticamente poterla spedire.

Le regole specifiche sono definite in EMAIL-SPEC.md.

---

## 28. Invio email

L'invio email è un'azione con effetti esterni.

Le email non devono essere inviate senza l'approvazione richiesta dal workflow.

L'approvazione deve essere distinta dalla semplice generazione della bozza.

---

## 29. Distribuzione esterna

La pubblicazione su servizi esterni deve essere trattata come azione con effetti esterni.

Esempi:

- Telegram;
- social network;
- piattaforme di distribuzione;
- repository pubblici;
- servizi di hosting.

Le capacità devono essere assegnate separatamente quando possibile.

---

## 30. Reddit e forum

Il monitoraggio di Reddit e forum non deve implicare capacità di pubblicazione.

Il ruolo di monitoraggio dovrebbe normalmente possedere:

- accesso alla ricerca;
- lettura;
- classificazione;
- capacità di generare notifiche.

Non dovrebbe possedere automaticamente:

- pubblicazione;
- risposta automatica;
- modifica dei contenuti della comunità.

---

## 31. Notifiche

La possibilità di generare notifiche è distinta dalla possibilità di compiere l'azione segnalata.

Un agente può notificare:

"Questa discussione è pertinente."

senza poter pubblicare una risposta.

Questo principio deve essere utilizzato sistematicamente.

---

## 32. Azioni ad alto impatto

Devono essere considerate ad alto impatto, quando applicabile:

- pubblicazione;
- redistribuzione;
- invio email;
- modifica di autorizzazioni;
- modifica di credenziali;
- cancellazione definitiva;
- modifica dell'infrastruttura;
- deploy;
- modifica delle configurazioni di sicurezza.

Queste azioni possono richiedere approvazione esplicita.

---

## 33. Azioni reversibili

Le operazioni reversibili possono essere automatizzate più facilmente quando il rischio è basso.

Esempi:

- classificare;
- aggiungere una nota;
- preparare una bozza;
- creare un report;
- creare un branch;
- preparare un commit.

La reversibilità deve comunque essere valutata nel contesto.

---

## 34. Azioni irreversibili

Le azioni irreversibili o difficili da annullare richiedono maggiore cautela.

Esempi:

- cancellazione definitiva;
- pubblicazione di dati privati;
- invio di informazioni riservate;
- revoca o modifica critica delle credenziali;
- distruzione di backup.

Il sistema deve preferire conferma e logging.

---

## 35. Cancellazione

La cancellazione deve distinguere:

- rimozione logica;
- rimozione dal sito;
- rimozione dal repository;
- cancellazione dello storage;
- cancellazione definitiva.

Non devono essere considerate equivalenti.

---

## 36. Backup

I backup devono essere protetti almeno quanto i dati che contengono.

Un backup non deve essere considerato automaticamente pubblico.

La strategia dettagliata appartiene a BACKUP-SPEC.md.

---

## 37. Logging

Le operazioni di sicurezza rilevanti devono poter essere ricostruite.

Quando appropriato devono essere registrati:

- chi o quale ruolo ha eseguito l'azione;
- quale risorsa è stata interessata;
- quale operazione è stata eseguita;
- risultato;
- eventuale approvazione;
- eventuale errore.

I log non devono contenere segreti inutilmente.

---

## 38. Audit

L'audit deve permettere di ricostruire almeno le azioni ad alto impatto.

Non è necessario registrare ogni operazione innocua con la stessa profondità.

Il livello di audit deve essere proporzionato al rischio.

---

## 39. Approvazioni

Le approvazioni devono poter essere collegate all'azione autorizzata.

Un'approvazione generica non dovrebbe essere interpretata come autorizzazione a qualunque operazione futura.

Le regole dettagliate sono definite in APPROVAL-SPEC.md.

---

## 40. Modifiche alle specifiche

Gli agenti possono proporre modifiche alle specifiche.

La modifica effettiva delle specifiche deve rispettare il workflow previsto.

Un agente non deve trasformare automaticamente una propria interpretazione in una nuova regola del progetto.

---

## 41. Aggiornamento delle specifiche

Un ruolo può:

- individuare una contraddizione;
- proporre una modifica;
- segnalare una lacuna;
- preparare una patch;
- produrre un report.

Il proprietario deve poter decidere se adottare la modifica.

Quando un aggiornamento è puramente correttivo e già autorizzato dal workflow, può essere automatizzato.

---

## 42. Prompt e istruzioni

Le istruzioni degli agenti non devono essere considerate un sostituto delle autorizzazioni tecniche.

Un prompt che dice:

"non pubblicare"

non è una protezione sufficiente se il sistema concede comunque capacità di pubblicazione senza controllo.

Le autorizzazioni devono essere applicate anche a livello tecnico quando possibile.

---

## 43. Difesa in profondità

Le operazioni sensibili dovrebbero essere protette da più livelli quando il rischio lo giustifica.

Esempi:

- istruzione dell'agente;
- controllo del workflow;
- permesso tecnico;
- verifica;
- approvazione;
- audit.

Non tutti i livelli sono necessari per ogni operazione.

---

## 44. Validazione prima dell'azione

Prima di un'azione ad alto impatto il sistema dovrebbe verificare, quando possibile:

- risorsa;
- destinatario;
- stato;
- permessi;
- approvazione;
- ambiente;
- eventuali condizioni di sicurezza.

Un errore di identificazione della risorsa deve impedire l'azione quando il rischio è significativo.

---

## 45. Protezione dei destinatari

Le azioni di distribuzione devono verificare il destinatario.

Questo è particolarmente importante per:

- email;
- materiali privati;
- guide a pagamento;
- file riservati;
- dati personali.

Un errore nel destinatario può trasformare un'operazione lecita in una divulgazione non autorizzata.

---

## 46. Separazione tra ambienti

Quando utile, devono essere distinti:

- sviluppo;
- test o preview;
- produzione;
- eventuali ulteriori ambienti necessari al progetto.

La separazione non implica necessariamente infrastrutture completamente indipendenti.

Per la configurazione iniziale può essere sufficiente un modello leggero:

- sviluppo sul computer locale e/o nell'ambiente di lavoro dell'agente;
- test o preview tramite build e controlli automatici, eventualmente associati a una pull request;
- produzione tramite il branch e il workflow di deploy autorizzati.

Il progetto non deve introdurre ambienti separati, server distinti o infrastrutture dedicate soltanto per rispettare formalmente questa distinzione.

La separazione deve crescere soltanto quando il rischio o la complessità del progetto lo rendono utile.

Le credenziali di produzione non devono essere utilizzate inutilmente negli ambienti di sviluppo.

I dati reali degli utenti non devono essere copiati negli ambienti di test senza una ragione appropriata.

Quando un ambiente di test utilizza dati reali, devono essere applicate le necessarie misure di protezione e minimizzazione.

---

## 47. Ambiente locale

Il lavoro locale può utilizzare:

- repository;
- cache;
- file temporanei;
- modelli locali;
- strumenti di analisi.

I dati sensibili presenti localmente devono essere trattati secondo la loro classificazione.

La presenza di un file sul computer non lo rende pubblico.

---

## 48. Trasferimento dei dati

Prima di trasferire dati a un servizio esterno, il sistema dovrebbe considerare:

- necessità del trasferimento;
- sensibilità;
- destinatario;
- retention;
- autorizzazione;
- eventuali implicazioni di privacy.

Non devono essere trasferiti dati sensibili soltanto per comodità.

---

## 49. Modelli esterni

Quando un modello esterno viene utilizzato per elaborare dati, il workflow deve considerare se il trasferimento è appropriato.

Dati privati o riservati non devono essere inviati automaticamente a servizi esterni.

Quando un modello locale è sufficiente e appropriato, può essere preferibile utilizzarlo.

---

## 50. Minimizzazione

Gli agenti devono ricevere soltanto i dati necessari per il compito quando ciò è tecnicamente ragionevole.

Non è necessario fornire l'intero archivio del progetto a un agente che deve svolgere una singola operazione.

La minimizzazione non deve però diventare così aggressiva da rendere il sistema inutilizzabile.

---

## 51. Sicurezza degli strumenti

Gli strumenti utilizzati dagli agenti devono essere trattati come componenti con capacità proprie.

Esempi:

- shell;
- Git;
- browser;
- API;
- email;
- storage;
- database;
- servizi esterni.

La sicurezza deve considerare la capacità effettiva dello strumento, non soltanto il ruolo nominale dell'agente.

---

## 52. Esecuzione di codice

L'esecuzione di codice può comportare rischi superiori alla semplice lettura.

Quando possibile devono essere utilizzati:

- ambienti isolati;
- directory appropriate;
- credenziali limitate;
- timeout;
- limiti di risorse;
- controlli sulle operazioni distruttive.

---

## 53. Comandi distruttivi

Comandi come:

- cancellazioni;
- reset;
- sovrascritture;
- modifiche massive;
- operazioni irreversibili;

devono essere trattati con cautela.

Gli agenti devono preferire operazioni reversibili quando possibile.

---

## 54. Dipendenze

Le dipendenze software devono essere considerate parte della superficie di sicurezza.

Quando possibile devono essere:

- identificabili;
- aggiornabili;
- verificabili;
- sostituibili.

Gli aggiornamenti automatici non devono rompere il progetto senza un meccanismo di verifica.

---

## 55. Aggiornamenti

Il sistema deve poter ricevere aggiornamenti di:

- software;
- dipendenze;
- strumenti;
- integrazioni;
- modelli;
- servizi.

Gli aggiornamenti importanti devono poter essere testati prima di essere utilizzati in produzione.

---

## 56. Monitoraggio della sicurezza

Un ruolo di sicurezza può controllare periodicamente:

- dipendenze;
- configurazioni;
- accessi;
- credenziali;
- repository;
- anomalie;
- log;
- esposizioni accidentali;
- permessi eccessivi.

Il monitoraggio deve avere una periodicità sostenibile.

---

## 57. Segnalazione di incidenti

Quando viene rilevato un possibile incidente, l'agente deve:

1. identificare il problema;
2. limitare l'azione se possibile;
3. evitare di peggiorare la situazione;
4. notificare il proprietario;
5. registrare le informazioni disponibili;
6. proporre una mitigazione.

L'agente non deve cancellare le evidenze soltanto per "ripulire" il sistema.

---

## 58. Compromissione

In caso di possibile compromissione di:

- credenziali;
- account;
- repository;
- storage;
- integrazioni;

il sistema deve poter isolare o revocare la capacità interessata quando tecnicamente possibile.

La revoca di una credenziale critica deve essere trattata come azione ad alto impatto.

---

## 59. Recupero

La sicurezza comprende anche la capacità di recuperare da un errore o incidente.

Devono essere considerate:

- backup;
- versionamento;
- copie indipendenti;
- possibilità di ripristino;
- documentazione minima delle procedure.

---

## 60. Principio di non-blocco

La sicurezza non deve impedire inutilmente il lavoro.

Quando un'azione è a basso rischio e reversibile, deve essere possibile automatizzarla.

Quando un'azione è ad alto rischio, deve essere aggiunto il controllo necessario.

L'obiettivo è ottenere il massimo livello di sicurezza compatibile con un workflow praticabile.

---

## 61. Eccezioni

Un'eccezione a una regola di sicurezza deve essere:

- esplicita;
- motivata;
- limitata;
- preferibilmente temporanea;
- registrabile.

Un'eccezione non deve diventare automaticamente una nuova regola generale.

---

## 62. Sostituibilità

La sicurezza non deve dipendere da un singolo modello o agente.

Cloud Code può essere sostituito.

Un modello locale può essere aggiunto.

Un servizio esterno può essere rimosso.

Le capacità e i vincoli devono rimanere applicabili.

---

## 63. Evoluzione

Il modello di sicurezza deve poter evolvere con il progetto.

Non è necessario progettare immediatamente un sistema enterprise.

Le misure devono crescere in proporzione a:

- quantità di dati;
- numero di utenti;
- numero di agenti;
- numero di integrazioni;
- valore dei materiali;
- rischio delle operazioni.

---

## 64. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. MEDIA-SPEC.md definisce media e visibilità;
4. SOURCE-SPEC.md definisce le fonti;
5. EMAIL-SPEC.md definisce la gestione email;
6. DISTRIBUTION-SPEC.md definisce la distribuzione;
7. APPROVAL-SPEC.md definisce le approvazioni;
8. SECURITY-SPEC.md definisce sicurezza e capacità;
9. WORKFLOW-SPEC.md definisce workflow e ruoli;
10. le specifiche tecniche definiscono l'implementazione;
11. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
