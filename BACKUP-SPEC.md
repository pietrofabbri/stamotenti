# StamoTenti — BACKUP SPECIFICATION

## 1. Scopo

Questo documento definisce i principi e le regole generali per la conservazione delle copie di sicurezza dei dati di StamoTenti.

La specifica non prescrive una particolare infrastruttura, piattaforma, tecnologia, frequenza o architettura di backup.

Le soluzioni concrete devono essere proporzionate:

- al valore della risorsa;
- alla sua difficoltà di ricostruzione;
- al rischio di perdita;
- alla frequenza con cui cambia;
- ai costi;
- alla complessità operativa;
- alle esigenze reali del progetto.

Il sistema deve quindi mantenere una certa elasticità tecnica.

Questa elasticità non si applica però alla tutela dei dati personali, alla riservatezza e alle condizioni di accesso: tali vincoli devono essere rispettati indipendentemente dalla tecnologia o dallo storage utilizzato.

Il sistema di backup deve proteggere, quando rilevante:

- codice;
- specifiche;
- contenuti;
- fonti e relativi metadata;
- media;
- dataset;
- configurazioni;
- memoria operativa;
- dati necessari al ripristino;
- altri asset rilevanti del progetto.

L'obiettivo non è duplicare indiscriminatamente tutto, ma garantire la possibilità di recuperare ciò che sarebbe costoso o impossibile ricostruire.

---

## 2. Principio fondamentale

Un backup deve essere valutato in funzione del valore della risorsa, del costo della sua perdita e della possibilità di ricostruirla.

Non tutte le risorse richiedono la stessa frequenza, quantità di copie o durata di conservazione.

Il sistema deve quindi evitare sia:

- backup insufficienti;
- backup inutilmente complessi o costosi.

---

## 3. Liste aperte

Gli elenchi presenti in questa specifica sono normalmente esemplificativi e non esaustivi.

Nuove categorie di dati, storage, strategie o procedure possono essere introdotte senza modificare necessariamente i principi generali.

Quando un elenco deve essere considerato chiuso, deve essere dichiarato esplicitamente.

---

## 4. Cosa deve essere salvato

Devono essere considerati candidati al backup:

- contenuti difficili da ricostruire;
- configurazioni;
- specifiche;
- dati degli utenti;
- dati operativi;
- media;
- dataset;
- informazioni necessarie al funzionamento del sito;
- informazioni necessarie al ripristino.

I dati facilmente rigenerabili possono avere una strategia più leggera.

---

## 5. Codice

Il codice deve essere conservato attraverso il sistema di versionamento del progetto.

Quando possibile devono esistere copie indipendenti dal working copy locale.

Il repository non deve essere considerato l'unica forma di backup per dati critici.

---

## 6. Specifiche

Le specifiche devono essere versionate insieme al progetto.

Le modifiche devono poter essere ricostruite attraverso la storia del repository.

Le specifiche non devono essere conservate esclusivamente nella memoria contestuale degli agenti.

---

## 7. Media

I media devono essere sottoposti a backup secondo il loro valore e la loro difficoltà di ricostruzione.

Particolare attenzione deve essere prestata a:

- audio originali;
- video originali;
- immagini originali;
- file acquistati o ottenuti legittimamente;
- materiali prodotti direttamente;
- file necessari a prodotti o guide;
- asset che non possono essere recuperati facilmente.

La strategia deve rispettare MEDIA-SPEC.md e le condizioni di utilizzo della singola risorsa.

---

## 8. Fonti private

Una fonte privata non deve essere resa pubblica soltanto perché viene sottoposta a backup.

Il backup conserva la risorsa e le sue condizioni di accesso.

Le copie di sicurezza devono quindi mantenere, quando necessario, la classificazione della risorsa originale.

---

## 9. Dati pubblici e privati

Il backup deve preservare le informazioni necessarie a distinguere:

- pubblico;
- privato;
- limitato;
- riservato;
- altre eventuali condizioni di accesso.

Una copia privata non deve diventare pubblica soltanto perché è stata trasferita in un altro storage.

---

## 9-bis. Dati personali e contenuti riservati

Le informazioni relative alle persone devono essere trattate come dati riservati salvo diversa e legittima classificazione.

Rientrano in questa attenzione, tra gli altri:

- indirizzi email;
- messaggi ricevuti;
- risposte degli utenti;
- feedback;
- informazioni associate agli iscritti;
- dati analitici riconducibili a persone;
- preferenze;
- informazioni operative che permettano di identificare una persona;
- eventuali dati personali contenuti nei materiali inviati dagli utenti.

Il fatto che tali dati siano sottoposti a backup non ne modifica la natura.

Le copie devono mantenere livelli di protezione coerenti con quelli richiesti dai dati originali.

L'accesso deve essere limitato a chi ne ha effettivamente bisogno.

Gli agenti non devono utilizzare copie di backup di dati personali per finalità ulteriori rispetto a quelle autorizzate.

Le regole specifiche su raccolta, trattamento, conservazione, diritti degli interessati e obblighi normativi sono definite in PRIVACY-SPEC.md.

## 10. Backup e diritti

La possibilità di conservare una copia non implica automaticamente la possibilità di distribuirla.

Il sistema deve distinguere:

- conservazione;
- utilizzo per ricerca;
- citazione;
- pubblicazione;
- redistribuzione.

Queste condizioni devono rimanere coerenti con MEDIA-SPEC.md e SOURCE-SPEC.md.

---

## 11. Backup degli utenti

I dati personali devono essere sottoposti a backup soltanto quando necessario.

Devono essere applicati:

- minimizzazione;
- protezione degli accessi;
- conservazione proporzionata;
- eventuale cifratura;
- procedure di cancellazione coerenti con le regole applicabili.

Il backup non deve diventare un modo per conservare indefinitamente dati che il sistema non dovrebbe più mantenere.

---

## 12. Email

I dati email rilevanti possono richiedere backup.

La strategia deve distinguere tra:

- messaggi necessari alla continuità del servizio;
- dati analitici;
- preferenze;
- liste;
- configurazioni;
- materiale temporaneo.

Le copie devono mantenere le necessarie protezioni relative ai dati personali.

---

## 13. Memoria operativa

La memoria operativa deve essere conservata attraverso file versionati quando contiene decisioni o informazioni importanti per la continuità del progetto.

La memoria contestuale del modello non deve essere considerata un backup affidabile.

---

## 14. Configurazioni

Devono essere salvate le configurazioni necessarie al ripristino.

Non devono però essere inclusi nei backup pubblici:

- password;
- token;
- API key;
- segreti;
- credenziali;
- altri dati sensibili.

Quando una configurazione contiene segreti, il backup deve separare configurazione e credenziali.

---

## 15. Segreti

I segreti devono essere conservati tramite sistemi appropriati all'ambiente.

Una copia di backup dei dati non deve automaticamente contenere una copia inutilmente accessibile di tutte le credenziali.

Le credenziali devono poter essere sostituite o revocate.

---

## 16. Principio delle copie multiple

Per i dati critici è preferibile mantenere più copie indipendenti.

Come riferimento generale può essere utilizzato il principio 3-2-1:

- almeno tre copie complessive;
- almeno due forme o ambienti di conservazione differenti;
- almeno una copia separata dalla sede o dall'ambiente principale.

Questo principio è una linea guida, non un requisito matematico applicabile indistintamente a ogni risorsa.

La strategia concreta deve essere proporzionata al rischio.

---

## 17. Separazione delle copie

Le copie di backup devono essere sufficientemente indipendenti da ridurre il rischio che un singolo incidente le distrugga tutte.

La separazione può essere:

- fisica;
- logica;
- geografica;
- tramite account differenti;
- tramite storage differenti;
- tramite accessi differenti.

Non è necessario utilizzare contemporaneamente tutte queste forme.

---

## 18. Copia offline o isolata

Per i dati particolarmente critici può essere utile mantenere almeno una copia non continuamente accessibile dal sistema principale.

Questo riduce il rischio che un incidente comprometta contemporaneamente produzione e backup.

La soluzione concreta può cambiare nel tempo.

---

## 19. Storage cloud

Lo storage remoto può essere utilizzato per i backup.

La scelta dello storage deve considerare:

- costo;
- affidabilità;
- privacy;
- accessibilità;
- possibilità di esportazione;
- possibilità di recupero;
- rischio di lock-in;
- condizioni di utilizzo.

Non è necessario vincolare il progetto a un singolo provider.

---

## 20. Storage locale

Lo storage locale può essere utilizzato come una delle copie.

Non deve però essere considerato automaticamente sufficiente per i dati critici.

La perdita o compromissione del computer principale non deve comportare necessariamente la perdita dell'unica copia.

---

## 21. Repository

GitHub può rappresentare una copia del codice e delle specifiche.

Non deve essere considerato automaticamente un sistema universale di backup per:

- media;
- dati privati;
- dati degli utenti;
- file di grandi dimensioni;
- materiali soggetti a restrizioni.

La strategia deve essere definita in base al tipo di risorsa.

---

## 22. Storage dei media

I media che non possono essere conservati nel repository devono utilizzare uno storage appropriato.

Lo storage può essere:

- locale;
- remoto;
- object storage;
- cloud storage;
- altro sistema compatibile.

La scelta non deve essere fissata nella specifica fondativa.

---

## 23. Periodicità

La frequenza dei backup deve essere proporzionata al tasso di cambiamento e al costo della perdita.

Dati modificati frequentemente possono richiedere backup più frequenti.

Dati statici possono richiedere backup meno frequenti.

La periodicità deve essere sostenibile.

Un sistema di backup teoricamente perfetto ma troppo costoso o complesso da mantenere non è una buona soluzione.

---

## 24. Backup automatici

Quando una procedura di backup è stabile, ripetitiva e sufficientemente sicura, dovrebbe essere automatizzata.

L'automazione può essere implementata tramite:

- script;
- cron;
- workflow;
- GitHub Actions;
- servizi di storage;
- altri strumenti appropriati.

La tecnologia concreta può cambiare.

---

## 25. Backup manuali

I backup manuali possono essere utilizzati:

- prima di modifiche importanti;
- prima di migrazioni;
- prima di operazioni rischiose;
- durante la manutenzione;
- quando il sistema automatico non è disponibile.

Il backup manuale non deve sostituire automaticamente una strategia automatizzata quando il rischio lo rende necessario.

---

## 26. Verifica del backup

Un backup non verificato non deve essere considerato pienamente affidabile.

Quando possibile devono essere verificati:

- esistenza;
- integrità;
- accessibilità;
- completezza;
- leggibilità;
- possibilità di ripristino.

---

## 27. Test di ripristino

I dati critici devono essere sottoposti periodicamente a prove di ripristino.

Il test deve verificare che il backup non sia soltanto presente, ma effettivamente utilizzabile.

La periodicità deve essere proporzionata al valore del dato e al rischio.

---

## 28. Ripristino parziale

Il sistema deve preferire, quando possibile, il ripristino selettivo.

Non dovrebbe essere necessario ripristinare l'intero progetto per recuperare:

- un singolo file;
- un media;
- una configurazione;
- una versione precedente;
- un dataset.

---

## 29. Ripristino completo

Deve essere possibile definire, quando necessario, una procedura per ricostruire il progetto in caso di perdita grave.

La procedura dovrebbe includere almeno:

- codice;
- configurazioni;
- dipendenze;
- dati essenziali;
- media necessari;
- accesso agli strumenti;
- informazioni necessarie al deploy.

La documentazione dettagliata può essere tecnica e non deve essere inserita interamente in questa specifica.

---

## 30. Disaster recovery

Il disaster recovery riguarda la capacità di tornare a uno stato funzionante dopo un evento grave.

Non è necessario progettare inizialmente un'infrastruttura enterprise.

La strategia deve crescere con:

- valore del progetto;
- numero di utenti;
- quantità di dati;
- dipendenza da servizi esterni;
- rischio operativo.

---

## 31. Obiettivi di recupero

Quando il progetto crescerà può essere utile definire:

- quanto dato può essere perso;
- quanto tempo può essere necessario per il ripristino.

Questi obiettivi possono essere definiti in funzione delle diverse categorie di dati.

Non è necessario imporre un unico obiettivo a tutto il progetto.

---

## 32. Versionamento

Il versionamento e il backup hanno funzioni differenti.

Il versionamento permette di recuperare versioni precedenti.

Il backup protegge anche dalla perdita del sistema che contiene la cronologia.

Per i dati critici possono essere necessari entrambi.

---

## 33. Snapshot

Gli snapshot possono essere utilizzati quando lo storage lo consente.

Non devono essere considerati automaticamente un sostituto completo dei backup indipendenti.

Uno snapshot accessibile allo stesso sistema compromesso può essere compromesso insieme al sistema principale.

---

## 34. Cifratura

I backup contenenti dati sensibili dovrebbero essere protetti mediante cifratura appropriata.

Quando la cifratura è utilizzata, devono essere considerate anche:

- gestione delle chiavi;
- possibilità di recupero;
- accesso autorizzato;
- rischio di perdita delle chiavi.

Un backup cifrato senza possibilità di recuperare la chiave non costituisce un buon backup.

---

## 35. Accesso ai backup

L'accesso ai backup deve essere limitato.

Un agente deve poter accedere soltanto alle copie necessarie al proprio compito.

La capacità di leggere un backup non implica automaticamente la capacità di cancellarlo.

---

## 36. Cancellazione dei backup

La cancellazione deve essere trattata con particolare cautela.

Non deve essere possibile eliminare accidentalmente tutte le copie di una risorsa attraverso una singola operazione automatizzata.

Le copie devono essere protette da cancellazioni involontarie quando il rischio lo giustifica.

---

## 37. Retention

La durata della conservazione deve dipendere dal valore e dalla natura dei dati.

Non deve essere necessario conservare indefinitamente ogni versione.

Per i dati soggetti a obblighi di cancellazione o minimizzazione, la retention dei backup deve essere compatibile con tali obblighi.

---

## 38. Rotazione

Quando appropriato, le copie possono essere ruotate.

La rotazione può ridurre:

- costo;
- spazio;
- accumulo di versioni inutili.

La rotazione non deve eliminare prematuramente tutte le copie utili.

---

## 39. Backup prima delle modifiche rischiose

Prima di operazioni ad alto rischio può essere creato un backup o snapshot aggiuntivo.

Esempi:

- migrazione;
- modifica massiva;
- aggiornamento infrastrutturale;
- trasformazione dei dati;
- cambio di storage;
- modifica significativa delle configurazioni.

---

## 40. Backup e agenti

Gli agenti possono preparare o eseguire backup quando autorizzati.

Un agente non deve poter cancellare o sovrascrivere indiscriminatamente le copie esistenti soltanto perché dispone di accesso allo storage.

Le capacità devono essere proporzionate al compito.

---

## 41. Backup e approvazioni

Le operazioni ordinarie di backup possono essere automatizzate.

Le operazioni distruttive relative ai backup possono richiedere approvazione.

La distinzione deve seguire APPROVAL-SPEC.md.

---

## 42. Backup e sicurezza

La strategia deve rispettare SECURITY-SPEC.md.

In particolare:

- accesso minimo necessario;
- protezione dei segreti;
- separazione delle copie;
- logging delle operazioni rilevanti;
- possibilità di revoca;
- protezione da cancellazioni accidentali.

---

## 43. Backup e privacy

Il backup non deve essere utilizzato per aggirare le regole di privacy.

Quando una risorsa deve essere cancellata o resa non disponibile, occorre valutare anche le copie di backup secondo le regole applicabili.

---

## 44. Backup e media privati

Un PDF, EPUB, audio, video o altro media privato può essere conservato in backup privato quando ciò è consentito.

La copia di backup non deve essere pubblicata.

Il sistema deve mantenere la distinzione tra:

- accesso tecnico;
- utilizzo per ricerca;
- citazione;
- pubblicazione;
- redistribuzione.

---

## 45. Backup e prodotti a pagamento

I materiali destinati a prodotti o guide a pagamento devono essere conservati in uno storage appropriato.

Il sistema non deve dipendere dal repository pubblico per conservare tali materiali.

La disponibilità del prodotto deve essere separata dalla disponibilità del file originale.

---

## 46. Backup delle mailing list

Le informazioni necessarie alla gestione della mailing list possono richiedere backup.

Devono essere considerate separatamente:

- indirizzi;
- preferenze;
- lingua rilevata;
- storico rilevante;
- analytics;
- configurazioni.

I dati personali devono essere protetti.

---

## 47. Backup degli analytics

Gli analytics che non possono essere facilmente ricostruiti possono richiedere conservazione separata.

La retention deve essere proporzionata all'utilità storica e alle esigenze di privacy.

---

## 48. Backup dei report

I report storici possono essere conservati quando servono per:

- confronti nel tempo;
- analisi delle performance;
- valutazione delle campagne;
- analisi email;
- analisi SEO/GEO;
- decisioni operative.

Non è necessario conservare indefinitamente ogni report temporaneo.

---

## 49. Backup delle configurazioni di deploy

Le informazioni necessarie a ricostruire il deploy devono essere documentate e conservate.

I segreti non devono essere inclusi direttamente.

Devono invece essere documentati i riferimenti necessari a recuperarli in modo sicuro.

---

## 50. Dipendenze esterne

Il ripristino deve considerare eventuali dipendenze da:

- servizi cloud;
- provider email;
- storage;
- DNS;
- analytics;
- GitHub;
- sistemi di distribuzione;
- altri servizi esterni.

Quando possibile, il progetto deve evitare di dipendere da un'unica piattaforma senza possibilità di recupero dei dati.

---

## 51. Esportabilità

I dati importanti dovrebbero poter essere esportati in formati ragionevolmente aperti o facilmente recuperabili.

L'esportabilità riduce il rischio di lock-in.

Non è necessario evitare ogni formato proprietario, ma le informazioni importanti non dovrebbero essere impossibili da recuperare.

---

## 52. Dipendenza dal provider

La scelta di un provider di backup può cambiare.

Questa specifica non vincola StamoTenti a:

- Zenodo;
- GitHub;
- un particolare cloud;
- un particolare object storage;
- un particolare provider.

La soluzione concreta deve poter evolvere.

---

## 53. Backup multipiattaforma

Quando utile, possono essere utilizzati più sistemi di conservazione.

La diversificazione è particolarmente utile per dati critici.

Non è necessario moltiplicare i provider per dati a basso rischio.

---

## 54. Monitoraggio

Il sistema dovrebbe poter verificare periodicamente:

- ultimo backup riuscito;
- spazio disponibile;
- errori;
- accessibilità;
- integrità;
- eventuali backup mancanti.

Le anomalie devono generare una notifica quando necessario.

Il monitoraggio dettagliato appartiene a MONITORING-SPEC.md.

---

## 55. Fallimento del backup

Un backup fallito non deve essere trattato come se fosse riuscito.

Il sistema dovrebbe:

1. rilevare il fallimento;
2. registrarlo;
3. notificare quando rilevante;
4. ritentare quando appropriato;
5. evitare di eliminare prematuramente la copia precedente funzionante.

---

## 56. Costo

Il costo del backup deve essere proporzionato al valore del dato.

Possono essere utilizzate strategie differenti per:

- dati caldi;
- dati freddi;
- dati temporanei;
- dati critici;
- dati facilmente rigenerabili.

---

## 57. Performance

Il backup non deve rendere inutilizzabile il progetto.

Le operazioni possono essere:

- incrementali;
- differenziali;
- pianificate;
- compresse;
- eseguite in momenti appropriati.

La tecnologia concreta può cambiare.

---

## 58. Backup prima del deploy

Un backup aggiuntivo può essere utile prima di modifiche di produzione significative.

Non è necessario creare una copia completa prima di ogni deploy ordinario se il sistema dispone già di versionamento e procedure di rollback adeguate.

---

## 59. Rollback

Il rollback permette di tornare rapidamente a uno stato precedente.

Può utilizzare:

- Git;
- versioni precedenti;
- snapshot;
- backup;
- artifact di build.

Rollback e backup non sono equivalenti.

---

## 60. Artifact

Gli artifact generati durante build o deploy possono essere conservati quando servono a:

- riprodurre una release;
- effettuare rollback;
- diagnosticare un problema.

Non è necessario conservarli indefinitamente.

---

## 61. Verifica periodica della strategia

La strategia di backup deve essere rivalutata quando cambiano:

- infrastruttura;
- quantità di dati;
- valore dei dati;
- numero di utenti;
- media;
- servizi esterni;
- workflow degli agenti.

---

## 62. Automazione progressiva

Quando una procedura di backup viene eseguita frequentemente, può essere trasformata in un'automazione stabile.

Il ruolo di stabilizzazione può proporre:

- script;
- workflow;
- controlli;
- notifiche;
- procedure di ripristino.

L'automazione deve essere introdotta quando riduce realmente il rischio o il lavoro manuale.

---

## 63. Principio di semplicità

La strategia iniziale deve rimanere semplice.

È preferibile una soluzione:

- comprensibile;
- verificabile;
- sostenibile;
- ripristinabile;

rispetto a una soluzione teoricamente sofisticata ma difficile da mantenere.

---

## 64. Evoluzione

La strategia può crescere nel tempo.

Un progetto piccolo non deve essere costretto a utilizzare immediatamente infrastrutture enterprise.

L'aumento della complessità deve essere giustificato da un aumento del rischio o del valore dei dati.

---

## 65. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. SECURITY-SPEC.md definisce i principi di sicurezza;
3. MEDIA-SPEC.md definisce media e condizioni di accesso;
4. SOURCE-SPEC.md definisce le fonti;
5. DISTRIBUTION-SPEC.md definisce la distribuzione;
6. APPROVAL-SPEC.md definisce approvazioni e controlli;
7. BACKUP-SPEC.md definisce conservazione e ripristino;
8. MONITORING-SPEC.md definisce monitoraggio e segnalazioni;
9. le specifiche tecniche definiscono l'implementazione;
10. il codice implementa le specifiche approvate.

Questa gerarchia è operativa e potrà essere consolidata o modificata durante la revisione globale delle specifiche.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
