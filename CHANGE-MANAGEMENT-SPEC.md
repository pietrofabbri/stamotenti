# StamoTenti — CHANGE MANAGEMENT SPECIFICATION

## 1. Scopo

Questo documento definisce come StamoTenti gestisce le modifiche
significative al progetto.

L'obiettivo è permettere al progetto di evolvere senza introdurre:

- modifiche accidentali;
- incoerenze tra documenti;
- regressioni;
- perdita di dati;
- violazioni di privacy;
- vulnerabilità;
- dipendenze inutili;
- burocrazia sproporzionata.

Il change management deve proteggere la durabilità del progetto senza
ostacolarne l'evoluzione.

---

## 2. Principio di proporzionalità

Non tutte le modifiche richiedono lo stesso livello di controllo.

Una modifica deve essere gestita in modo proporzionato a:

- impatto;
- rischio;
- reversibilità;
- superficie interessata;
- sensibilità dei dati;
- possibilità di interrompere il servizio;
- conseguenze sulla sicurezza;
- conseguenze sulla privacy;
- conseguenze editoriali;
- costo di errore.

Una modifica semplice non deve essere trasformata in un processo pesante
soltanto perché esiste un sistema formale di change management.

---

## 3. Tipi generali di modifica

Le modifiche possono essere considerate, in modo non necessariamente
rigido:

- ordinarie;
- significative;
- ad alto rischio;
- urgenti.

L'elenco è aperto.

La classificazione serve a scegliere il livello di attenzione
appropriato, non a creare una burocrazia permanente.

---

## 4. Modifica ordinaria

È normalmente ordinaria una modifica che:

- è facilmente reversibile;
- ha impatto limitato;
- applica regole già esistenti;
- non modifica principi o architettura;
- non coinvolge dati particolarmente sensibili;
- non modifica autorizzazioni significative.

Esempi possono comprendere:

- correzioni di testo;
- piccoli miglioramenti grafici;
- manutenzione ordinaria;
- aggiornamenti documentali minori;
- correzioni tecniche a basso rischio.

---

## 5. Modifica significativa

Una modifica è significativa quando può modificare in modo rilevante
il comportamento del sistema.

Esempi:

- modifica di una SPEC;
- modifica del workflow;
- modifica dei ruoli degli agenti;
- modifica del modello dei contenuti;
- introduzione di una nuova integrazione;
- modifica dello storage;
- modifica significativa del sito;
- modifica dei meccanismi di distribuzione.

---

## 6. Modifica ad alto rischio

Una modifica può essere considerata ad alto rischio quando può:

- esporre dati privati;
- compromettere la sicurezza;
- alterare dati in modo irreversibile;
- inviare comunicazioni non autorizzate;
- rendere pubblico un contenuto privato;
- modificare significativamente l'infrastruttura;
- compromettere backup;
- compromettere l'integrità del repository;
- introdurre conseguenze difficili da invertire.

Queste modifiche richiedono particolare attenzione e, quando previsto,
approvazione esplicita.

---

## 7. Modifica urgente

Una modifica urgente può essere necessaria per:

- vulnerabilità;
- perdita di dati;
- esposizione accidentale;
- malfunzionamento grave;
- errore di distribuzione;
- interruzione significativa.

L'urgenza non elimina i requisiti superiori di sicurezza o privacy.

Quando non è possibile seguire il processo ordinario, la modifica deve
essere documentata e verificata successivamente per quanto praticabile.

---

## 8. Chi può proporre una modifica

Una modifica può essere proposta da:

- autore;
- agente;
- processo automatico;
- attività di monitoraggio;
- feedback ricevuto via email;
- revisione;
- test;
- controllo di sicurezza;
- controllo di accessibilità;
- analisi delle performance.

Una proposta non equivale a un'approvazione.

---

## 9. Proposte degli agenti

Gli agenti possono individuare problemi e proporre modifiche.

Devono poter spiegare, quando utile:

- problema osservato;
- modifica proposta;
- motivazione;
- impatto previsto;
- rischio;
- alternative;
- necessità di approvazione.

Non devono presumere che una proposta sia automaticamente autorizzata.

---

## 10. Modifiche ricorrenti

Se una modifica viene richiesta frequentemente, può essere opportuno
valutare:

- documentazione migliore;
- una procedura standard;
- un comando;
- uno script;
- un'automazione;
- una modifica dell'architettura.

Il ripetersi di una modifica può indicare un'opportunità di
semplificazione.

---

## 11. Stabilizzazione del codice

Il ruolo di stabilizzazione può individuare operazioni ricorrenti che
potrebbero essere automatizzate.

L'obiettivo è ridurre lavoro ripetitivo senza trasformare ogni attività
in un sistema automatico.

---

## 12. Prima della modifica

Quando una modifica è significativa, dovrebbe essere valutato:

- cosa cambia;
- perché cambia;
- quali componenti sono coinvolti;
- quali SPEC sono interessate;
- quali rischi esistono;
- come può essere verificata;
- come può essere annullata.

Non è necessario compilare una scheda formale per ogni piccola modifica.

---

## 13. Impatto

L'analisi dell'impatto può comprendere:

- contenuti;
- codice;
- dati;
- fonti;
- media;
- email;
- distribuzione;
- privacy;
- sicurezza;
- accessibilità;
- SEO;
- GEO;
- performance;
- costi;
- manutenzione.

L'elenco è aperto.

---

## 14. Dipendenze

Prima di una modifica significativa devono essere considerate le
dipendenze rilevanti.

In particolare:

- SPEC dipendenti;
- workflow;
- agenti;
- codice;
- dati;
- servizi esterni;
- storage;
- automazioni;
- documentazione.

---

## 15. Decisione

Quando una modifica rappresenta una scelta architetturale o progettuale
significativa, può essere necessario documentarla secondo
DECISION-SPEC.md.

Non ogni modifica richiede un decision record separato.

---

## 16. Modifica delle specifiche

Quando una SPEC viene modificata, deve essere verificato se la modifica
entra in conflitto con:

- documenti fondativi;
- altre SPEC;
- decisioni approvate;
- workflow;
- privacy;
- sicurezza.

---

## 17. Coerenza tra specifiche

Una modifica a una SPEC può rendere obsolete parti di altre SPEC.

Quando ciò accade, le SPEC interessate devono essere individuate e
aggiornate in modo coerente.

---

## 18. Modifica dei documenti fondativi

Una modifica ai documenti fondativi richiede particolare attenzione.

Non deve essere effettuata semplicemente per rendere compatibile il
sistema con una modifica operativa.

Quando emerge una tensione tra principio fondativo e implementazione,
deve essere valutato prima se correggere l'implementazione.

---

## 19. Revisione dei documenti fondativi

Quando una modifica richiede una revisione dei principi fondativi,
deve essere coinvolto, quando appropriato, l'agente di supporto alla revisione
della Costituzione.

Il ruolo assiste l'autore nell'analisi dei principi, nell'individuazione dei
colli di bottiglia e nella valutazione delle alternative.

Non possiede autorità autonoma di modifica o approvazione dei documenti
fondativi.

Il ruolo fornisce analisi e proposte.

L'autorità decisionale rimane quella definita dai documenti superiori.

---

## 20. Modifica del modello degli agenti

La sostituzione di un agente o di un modello non deve essere considerata
necessariamente una modifica architetturale.

Il sistema deve essere progettato affinché:

- modelli possano cambiare;
- agenti possano cambiare;
- ruoli possano essere riorganizzati;
- provider possano cambiare;

senza richiedere la riscrittura dell'intero progetto.

---

## 21. Ruoli e implementazioni

Le SPEC descrivono soprattutto responsabilità e capacità.

Non devono essere inutilmente legate:

- a un particolare modello;
- a un particolare provider;
- a un particolare agente;
- a un particolare software.

---

## 22. Test

Quando una modifica può produrre regressioni, deve essere verificata
prima della distribuzione.

Il livello di verifica deve essere proporzionato al rischio e può utilizzare
TESTING-SPEC.md.

Il livello di test deve essere proporzionato al rischio.

Possono essere utilizzati:

- controlli automatici;
- test manuali;
- preview;
- confronti;
- lint;
- validazioni;
- controlli sui dati;
- verifiche di sicurezza;
- verifiche di accessibilità.

---

## 23. Verifica dei contenuti

Una modifica al contenuto deve essere verificata secondo la natura
del contenuto.

Per un articolo possono essere rilevanti:

- correttezza;
- fonti;
- citazioni;
- lingua;
- struttura;
- leggibilità;
- accessibilità;
- SEO;
- GEO.

Per un media possono essere più importanti:

- integrità;
- diritti;
- formato;
- metadati;
- accessibilità.

---

## 24. Verifica di sicurezza

Le modifiche che interessano:

- autenticazione;
- autorizzazioni;
- dati;
- storage;
- infrastruttura;
- integrazioni;
- segreti;
- distribuzione;

devono essere sottoposte a verifiche di sicurezza proporzionate.

---

## 25. Verifica della privacy

Una modifica deve essere valutata sotto il profilo della privacy quando
può influire sul trattamento di dati personali.

In particolare devono essere considerate:

- raccolta;
- conservazione;
- accesso;
- elaborazione;
- trasferimento;
- distribuzione;
- eliminazione.

---

## 26. Verifica dell'accessibilità

Le modifiche all'interfaccia o ai contenuti pubblici devono considerare
l'accessibilità.

Una modifica non dovrebbe introdurre nuove barriere senza che ciò sia
stato individuato e valutato.

---

## 27. Verifica SEO e GEO

Le modifiche che interessano:

- struttura del sito;
- URL;
- metadata;
- heading;
- collegamenti;
- contenuti;
- sitemap;
- dati strutturati;

devono considerare eventuali effetti su SEO e GEO.

---

## 28. Verifica delle email

Le modifiche ai sistemi email devono essere verificate con particolare
attenzione.

Una modifica non deve causare automaticamente:

- invii indesiderati;
- perdita di iscritti;
- perdita di preferenze;
- esposizione di indirizzi;
- risposta nella lingua sbagliata quando evitabile.

Le email devono comunque rispettare EMAIL-SPEC.md.

---

## 29. Nessun invio automatico non autorizzato

Una modifica tecnica non può aggirare il requisito secondo cui le email
che devono essere approvate dall'autore non vengono inviate senza
approvazione.

---

## 30. Verifica della distribuzione

Una modifica a Telegram, newsletter o altri canali deve verificare
almeno:

- destinatari;
- contenuto;
- autorizzazione;
- lingua;
- link;
- privacy;
- possibilità di errore.

Il monitoraggio dei forum e delle community non implica automaticamente
la pubblicazione automatica.

---

## 31. Forum e community

StamoTenti può monitorare:

- Telegram;
- Reddit;
- forum;
- community;
- altri spazi pertinenti.

Il sistema può segnalare all'autore discussioni pertinenti.

Il monitoraggio non implica automaticamente la pubblicazione di post o
risposte.

---

## 32. Commenti sul sito

Il sito non prevede un sistema pubblico di commenti degli utenti.

Il feedback può essere ricevuto, tra gli altri canali, tramite email,
in particolare come risposta alla newsletter.

Questa distinzione deve essere mantenuta anche durante modifiche future
al sito.

---

## 33. Rollback

Una modifica significativa dovrebbe avere una strategia di ritorno
quando il rischio lo rende utile.

Il rollback può consistere in:

- ripristino Git;
- ripristino di un file;
- ripristino di dati;
- ripristino di una configurazione;
- disattivazione di una funzionalità;
- ripristino di un backup.

Non tutte le modifiche richiedono un piano di rollback formalizzato.

---

## 34. Modifiche irreversibili

Le modifiche difficili da invertire richiedono maggiore attenzione.

Esempi:

- eliminazione di dati;
- migrazione distruttiva;
- modifica di schema;
- eliminazione di storage;
- modifica irreversibile di diritti;
- invio di comunicazioni.

Quando possibile, devono essere precedute da backup o verifiche.

---

## 35. Backup prima delle modifiche

BACKUP-SPEC.md definisce il sistema generale dei backup.

Prima di una modifica ad alto rischio deve essere valutato se è
necessario un backup specifico.

---

## 36. Deploy

Il passaggio in produzione deve essere proporzionato alla modifica.

Una modifica semplice può essere applicata direttamente.

Una modifica significativa può richiedere:

- ambiente di test;
- preview;
- verifica;
- approvazione;
- deploy;
- controllo successivo.

---

## 37. Separazione degli ambienti

Quando utile, devono essere distinti:

- sviluppo;
- test;
- produzione.

La separazione deve rimanere semplice.

Non è necessario introdurre infrastruttura complessa se il progetto
può ottenere un livello sufficiente di sicurezza con soluzioni più
semplici.

---

## 38. Verifica post-modifica

Dopo una modifica significativa dovrebbe essere verificato che:

- il sistema funzioni;
- i contenuti siano corretti;
- non siano comparsi errori;
- non siano state introdotte vulnerabilità;
- non siano stati esposti dati;
- le funzionalità interessate funzionino.

---

## 39. Monitoraggio successivo

Quando una modifica ha un impatto significativo, MONITORING-SPEC.md può
definire controlli successivi.

Il monitoraggio può individuare:

- regressioni;
- problemi di performance;
- errori;
- anomalie;
- effetti inattesi.

---

## 40. Modifiche che falliscono

Quando una modifica produce un risultato negativo, si deve valutare:

- rollback;
- correzione;
- ulteriore test;
- modifica della specifica;
- nuova decisione.

L'errore non deve essere nascosto.

---

## 41. Lezioni apprese

Un problema significativo può produrre una lezione utile.

Questa può essere registrata secondo OPERATIONAL-MEMORY-SPEC.md.

Se diventa una regola stabile, può essere incorporata nella SPEC
appropriata.

---

## 42. Modifiche di emergenza

In caso di emergenza può essere necessario agire prima di completare
tutta la documentazione.

La sicurezza e la protezione dei dati hanno priorità.

Dopo l'intervento deve essere ricostruito, quando possibile:

- cosa è stato modificato;
- perché;
- chi o quale ruolo ha agito;
- quale verifica è stata effettuata;
- se sono necessarie ulteriori modifiche.

---

## 43. Modifiche fallite parzialmente

Se una modifica viene applicata solo in parte, lo stato deve essere
reso comprensibile prima di procedere con altre modifiche.

Non si deve presumere che il sistema sia nello stato previsto.

---

## 44. Concorrenza

Quando più modifiche vengono sviluppate contemporaneamente, devono
essere considerate eventuali incompatibilità.

Git e il sistema di versionamento costituiscono strumenti principali
per rendere visibili le differenze.

---

## 45. Modifiche tramite Git

Quando possibile, le modifiche al codice e alla documentazione devono
essere tracciate attraverso Git.

Il commit dovrebbe descrivere sufficientemente la natura della modifica.

---

## 46. Commit

I commit devono essere abbastanza piccoli da rendere comprensibile
cosa è cambiato quando ciò è utile.

Non è necessario applicare una convenzione eccessivamente rigida ai
commit se il valore prodotto non giustifica la complessità.

---

## 47. Branch

I branch possono essere utilizzati quando:

- la modifica è significativa;
- è necessario sperimentare;
- più modifiche devono essere isolate;
- è necessario effettuare una revisione prima del merge.

Per modifiche banali non è necessario introdurre un workflow complesso.

---

## 48. Pull request

Una pull request o meccanismo equivalente può essere utilizzata quando
una modifica beneficia di:

- revisione;
- confronto;
- discussione;
- test automatici;
- controllo di sicurezza.

Non deve diventare obbligatoria per ogni modifica futura se ciò
rallenta inutilmente il progetto.

---

## 49. Documentazione della modifica

Per una modifica significativa dovrebbe essere possibile ricostruire
almeno:

- cosa è cambiato;
- perché;
- cosa è stato verificato;
- quale approvazione era necessaria;
- quale risultato ha prodotto.

---

## 50. Modifiche alle specifiche

Quando una modifica a una SPEC è approvata:

1. la SPEC viene aggiornata;
2. eventuali decision record vengono aggiornati o collegati;
3. le SPEC dipendenti vengono controllate;
4. eventuale codice interessato viene aggiornato;
5. i controlli pertinenti vengono eseguiti.

---

## 51. Modifiche al codice

Quando il codice viene modificato:

1. deve essere compreso l'impatto;
2. devono essere eseguiti i test pertinenti;
3. devono essere verificati eventuali effetti sul comportamento;
4. deve essere verificato che il codice rimanga coerente con le SPEC.

---

## 52. Modifiche ai contenuti

Quando un contenuto viene modificato:

1. deve essere rispettato il relativo lifecycle;
2. devono essere considerate fonti e citazioni;
3. devono essere considerate lingua e accessibilità;
4. devono essere applicate le approvazioni necessarie;
5. deve essere verificata la distribuzione successiva quando rilevante.

---

## 53. Modifiche ai dati

Le modifiche ai dati devono essere trattate con particolare attenzione
quando sono:

- massive;
- irreversibili;
- personali;
- necessarie per il funzionamento del sistema.

Quando possibile devono essere verificabili e reversibili.

---

## 54. Modifiche ai media

Le modifiche ai media devono considerare:

- formato;
- integrità;
- diritti;
- accessibilità;
- riferimenti;
- contenuti derivati.

---

## 55. Modifiche alle fonti

La modifica o sostituzione di una fonte può avere effetti su:

- citazioni;
- articoli;
- contenuti derivati;
- conclusioni;
- metadata.

Quando rilevante, tali effetti devono essere individuati.

---

## 56. Modifiche alle integrazioni

Una modifica a un servizio esterno deve considerare:

- disponibilità;
- costo;
- privacy;
- sicurezza;
- dipendenza;
- possibilità di sostituzione.

La modularità deve essere preservata quando possibile.

---

## 57. Provider sostituibili

Le modifiche non devono rendere inutilmente StamoTenti dipendente da un
singolo:

- provider AI;
- provider email;
- provider storage;
- servizio analytics;
- servizio di distribuzione.

---

## 58. Economicità

Una modifica deve considerare non soltanto il costo iniziale, ma anche:

- costo ricorrente;
- manutenzione;
- complessità;
- lock-in;
- consumo di risorse.

---

## 59. Manutenibilità

Una modifica che risolve un problema locale ma introduce una grande
quantità di complessità deve essere valutata criticamente.

La semplicità è un requisito progettuale.

---

## 60. Durabilità

Le modifiche dovrebbero, quando possibile, mantenere il sistema
comprensibile anche dopo la sostituzione degli strumenti che lo
implementano.

---

## 61. Modifiche sperimentali

Una modifica può essere introdotta come esperimento.

In tal caso deve essere possibile distinguere:

- ciò che è sperimentale;
- ciò che è approvato;
- ciò che è diventato parte stabile del sistema.

---

## 62. Feature temporanee

Una funzionalità temporanea non deve diventare accidentalmente una
dipendenza permanente.

Quando possibile deve essere chiaro:

- perché esiste;
- cosa dovrebbe sostituirla;
- quali condizioni ne determinano la rimozione.

---

## 63. Automazioni

Le automazioni devono essere introdotte quando riducono lavoro o errori
senza introdurre rischi sproporzionati.

Un'automazione deve poter essere disattivata quando necessario.

---

## 64. Modifiche automatiche

Un sistema automatico può applicare modifiche solo entro i limiti
della propria autorizzazione.

La capacità tecnica di modificare qualcosa non equivale
all'autorizzazione a farlo.

---

## 65. Approvazione

APPROVAL-SPEC.md stabilisce quali modifiche richiedono approvazione.

Questa specifica non deve duplicare tutte le regole di approvazione.

---

## 66. Privacy come vincolo superiore

Una modifica non può essere giustificata soltanto dalla comodità
operativa quando compromette la privacy.

PRIVACY-SPEC.md e SECURITY-SPEC.md definiscono i relativi vincoli.

---

## 67. Nessun sistema eccessivamente rigido

Il change management deve evitare di trasformare il progetto in una
sequenza di autorizzazioni necessarie per ogni operazione.

La classificazione di una modifica serve a determinare il livello di
controllo appropriato, non a imporre formalità uniformi.

Quando una modifica è piccola, reversibile e chiaramente autorizzata,
deve poter seguire un percorso leggero.

La finalità è controllare le modifiche importanti, non impedire
l'evoluzione quotidiana.

---

## 68. Eccezioni

Quando una situazione non è prevista, deve essere applicato il
principio di proporzionalità.

Se la decisione può creare un precedente importante, può essere
documentata secondo DECISION-SPEC.md.

---

## 69. Revisione delle regole

Il processo di change management stesso può essere modificato.

Quando diventa:

- troppo lento;
- troppo complesso;
- insufficiente;
- ridondante;

deve poter essere semplificato o rafforzato.

---

## 70. Colli di bottiglia

Un numero eccessivo di approvazioni o controlli può diventare un
collo di bottiglia.

Il monitoraggio deve permettere di individuare questi problemi.

Gli agenti possono proporre semplificazioni.

---

## 71. Flessibilità dei ruoli

Non è necessario mantenere per sempre gli stessi ruoli o agenti.

Il sistema deve permettere di ridistribuire le responsabilità senza
modificare necessariamente il modello generale di change management.

---

## 72. Tracciabilità

Per modifiche significative deve essere possibile ricostruire,
quando necessario:

- origine;
- motivazione;
- modifica;
- verifica;
- approvazione;
- risultato.

La tracciabilità deve essere proporzionata al rischio.

---

## 73. Nessun obbligo di formalizzazione assoluta

Se una modifica è chiaramente:

- piccola;
- reversibile;
- a basso rischio;
- coerente con regole esistenti;

non è necessario creare un processo formale soltanto per documentare
che è stata fatta.

---

## 74. Miglioramento continuo

Il change management deve utilizzare l'esperienza reale.

Quando una modifica rivela:

- un difetto di progettazione;
- un'automazione utile;
- una regola mancante;
- un controllo inutile;
- un rischio sottovalutato;

l'informazione può essere utilizzata per migliorare il sistema.

---

## 75. Relazione con CONTENT-LIFECYCLE-SPEC.md

CONTENT-LIFECYCLE-SPEC.md definisce come i contenuti possono evolvere.

CHANGE-MANAGEMENT-SPEC.md definisce come vengono gestite le modifiche
significative al sistema e ai suoi artefatti.

Le due specifiche devono rimanere distinte.

---

## 76. Relazione con DECISION-SPEC.md

DECISION-SPEC.md conserva il ragionamento dietro le decisioni
significative.

CHANGE-MANAGEMENT-SPEC.md definisce il processo con cui le modifiche
vengono valutate e applicate.

---

## 77. Relazione con WORKFLOW-SPEC.md

WORKFLOW-SPEC.md descrive il workflow operativo.

CHANGE-MANAGEMENT-SPEC.md stabilisce come il workflow stesso può essere
modificato quando necessario.

---

## 78. Relazione con OPERATIONAL-MEMORY-SPEC.md

Le lezioni apprese durante le modifiche possono essere conservate
nella memoria operativa.

Quando diventano regole stabili, devono essere riflesse nella
specifica appropriata.

---

## 79. Relazione con MONITORING-SPEC.md

MONITORING-SPEC.md può individuare effetti inattesi delle modifiche.

Il monitoraggio non modifica automaticamente il sistema.

Può generare una segnalazione o una proposta.

---

## 80. Relazione con BACKUP-SPEC.md

BACKUP-SPEC.md definisce il backup.

CHANGE-MANAGEMENT-SPEC.md definisce quando una modifica richiede di
considerare un backup o una possibilità di ripristino.

---

## 81. Principio finale

Il sistema deve permettere di cambiare StamoTenti.

Deve essere possibile:

- correggere;
- migliorare;
- sperimentare;
- sostituire;
- semplificare;
- automatizzare;
- ritirare;
- ripristinare.

Il change management esiste per rendere queste trasformazioni più
sicure e comprensibili, non per impedirle.

La domanda fondamentale non deve essere:

> "Abbiamo seguito abbastanza passaggi?"

ma:

> "Abbiamo applicato il livello di controllo adeguato alla modifica?"

---

## 82. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi definiscono principi e vincoli superiori;
2. PRIVACY-SPEC.md e SECURITY-SPEC.md definiscono i vincoli relativi
   a privacy e sicurezza;
3. le SPEC di dominio definiscono il comportamento specifico;
4. CHANGE-MANAGEMENT-SPEC.md definisce la gestione delle modifiche;
5. APPROVAL-SPEC.md definisce le autorizzazioni e approvazioni;
6. WORKFLOW-SPEC.md definisce le procedure operative;
7. i documenti tecnici definiscono l'implementazione;
8. il codice implementa quanto approvato.

Il change management non può essere utilizzato per aggirare una regola
superiore.
