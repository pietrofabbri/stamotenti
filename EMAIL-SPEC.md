# StamoTenti — EMAIL SPECIFICATION

## 1. Scopo

Questo documento definisce la gestione delle email di StamoTenti.

Le email possono essere utilizzate per:

- ricevere feedback;
- rispondere agli utenti;
- fornire assistenza;
- gestire richieste relative alle guide;
- comunicare con collaboratori;
- inviare materiali autorizzati;
- gestire comunicazioni operative;
- raccogliere informazioni utili al miglioramento del progetto.

Il sistema deve permettere agli agenti di assistere nella gestione delle email senza rendere obbligatorio l'intervento manuale per ogni attività di preparazione o analisi.

L'invio delle email rimane invece sempre subordinato all'approvazione del proprietario del progetto.

---

## 2. Principio generale

L'email è considerata sia una fonte di informazioni sia una superficie operativa del progetto.

Il sistema deve distinguere tra:

- ricezione;
- classificazione;
- analisi;
- proposta di risposta;
- revisione;
- approvazione;
- invio;
- archiviazione;
- analisi statistica.

Un agente può svolgere una o più di queste attività secondo il workflow e le autorizzazioni disponibili.

---

## 3. Provider

Il modello non deve dipendere da uno specifico provider email.

Il sistema deve poter funzionare con:

- Gmail;
- Outlook;
- altri provider compatibili;
- eventuali sistemi email proprietari.

L'implementazione concreta del provider appartiene alla parte tecnica.

Il modello concettuale deve rimanere indipendente dal provider.

---

## 4. Account e identità

Ogni identità email utilizzata dal progetto deve essere riconoscibile e distinguibile per funzione.

Quando esistono più indirizzi, devono essere distinguibili almeno per funzione.

Esempi:

- comunicazioni generali;
- assistenza;
- feedback;
- amministrazione;
- comunicazioni automatiche.

Non è necessario creare molti indirizzi quando un unico indirizzo è sufficiente.

La moltiplicazione degli account deve essere giustificata da esigenze reali.

---

## 5. Thread

Le conversazioni devono essere trattate come thread quando il provider lo consente.

Un thread deve mantenere, quando disponibili:

- identificativo del thread;
- messaggi appartenenti al thread;
- mittenti;
- destinatari;
- oggetti;
- riferimenti;
- eventuali allegati;
- stato operativo;
- collegamenti con entità StamoTenti.

L'identificativo del provider deve essere conservato quando utile.

---

## 6. Messaggio

Ogni messaggio deve poter essere distinto dal thread.

Quando disponibili devono essere preservati:

- identificativo del messaggio;
- identificativo del thread;
- mittente;
- destinatari;
- destinatari in copia;
- oggetto;
- corpo;
- data tecnica;
- allegati;
- riferimenti ad altri messaggi;
- header utili;
- provider di origine.

I dati tecnici non devono essere confusi con il contenuto editoriale.

---

## 7. Conversazione e contenuto

Il sistema deve poter collegare una conversazione a elementi del progetto quando esiste una relazione significativa.

Esempi:

Email → feedback → guida

Email → domanda → articolo

Email → richiesta → fonte

Email → richiesta → materiale privato

Questi collegamenti devono essere mantenuti soltanto quando risultano utili.

---

## 8. Feedback

Un'email può contenere feedback relativo a:

- una guida;
- un articolo;
- un dataset;
- un errore;
- una traduzione;
- un'esperienza d'uso;
- una richiesta;
- un problema tecnico;
- una proposta.

Il sistema dovrebbe poter classificare il feedback.

La classificazione non deve impedire all'agente di interpretare nuovamente il messaggio quando necessario.

---

## 9. Collegamento con le guide

Quando un utente risponde dopo aver utilizzato una guida, il sistema dovrebbe poter collegare il feedback alla guida pertinente.

Il collegamento può derivare da:

- riferimento esplicito dell'utente;
- oggetto dell'email;
- contenuto;
- identificativo della guida;
- percorso o pagina di provenienza quando disponibile;
- informazioni presenti nel messaggio;
- classificazione dell'agente.

Quando il collegamento è incerto, l'agente deve segnalarlo invece di inventarlo.

---

## 10. Domande degli utenti

Le email contenenti domande possono essere classificate come:

- domanda semplice;
- richiesta di chiarimento;
- richiesta tecnica;
- richiesta bibliografica;
- richiesta relativa a una guida;
- richiesta relativa a un articolo;
- richiesta fuori ambito;
- possibile richiesta da approfondire.

L'agente può proporre una risposta.

La risposta deve rispettare il livello di certezza delle informazioni disponibili.

---

## 11. Ruolo di assistenza email

Il sistema può utilizzare un ruolo incaricato di:

- leggere le nuove email;
- classificare i messaggi;
- identificare il tema;
- collegare il messaggio al contenuto pertinente;
- recuperare informazioni dal sito;
- recuperare informazioni dalle fonti autorizzate;
- proporre una risposta;
- individuare richieste che richiedono intervento umano;
- segnalare conversazioni problematiche.

Il ruolo non deve essere vincolato a un modello specifico.

---

## 12. Risposte automatiche

Gli agenti possono preparare automaticamente risposte.

Questo non autorizza l'invio automatico.

Nessuna risposta sostanziale deve essere inviata senza l'approvazione del proprietario del progetto.

Anche quando:

- la risposta è considerata sicura;
- la risposta è stata verificata da un altro agente;
- il contenuto è ricorrente;
- il programma email è già configurato;
- l'invio è programmato.

La preparazione automatica e l'invio sono due operazioni distinte.

---

## 13. Risposte proposte

Quando una risposta non può essere inviata automaticamente, l'agente deve poter preparare una bozza.

La bozza dovrebbe contenere:

- risposta proposta;
- eventuali fonti utilizzate;
- eventuali incertezze;
- eventuali elementi che richiedono verifica;
- eventuali collegamenti utili;
- eventuale motivo per cui è richiesta approvazione.

La bozza deve poter essere modificata manualmente.

---

## 14. Approvazione obbligatoria dell'invio

L'approvazione del proprietario è necessaria prima dell'invio.

L'approvazione deve poter essere registrata in modo persistente secondo APPROVAL-SPEC.md.

Una precedente approvazione non costituisce automaticamente un'autorizzazione permanente per messaggi futuri.

Una programmazione automatica non costituisce approvazione.

Eventuali eccezioni devono essere introdotte soltanto mediante una decisione esplicita del proprietario e documentate nel sistema.

---

## 15. Principio di non-sostituzione

Gli agenti non devono impedire al proprietario di:

- leggere direttamente le email;
- rispondere manualmente;
- modificare una bozza;
- ignorare una proposta;
- cambiare classificazione;
- cambiare priorità;
- gestire direttamente una conversazione;
- disattivare un'automazione.

L'automazione deve assistere il lavoro, non creare una dipendenza obbligatoria dal sistema.

---

## 16. Priorità

Le conversazioni possono avere una priorità.

Esempi:

- bassa;
- normale;
- alta;
- urgente.

La priorità può essere determinata da:

- natura della richiesta;
- presenza di un problema;
- necessità di risposta;
- valore per il progetto;
- rischio;
- eventuali scadenze.

La classificazione automatica deve essere modificabile manualmente.

---

## 17. Stato della conversazione

Un thread può assumere stati come:

- nuovo;
- classificato;
- da analizzare;
- risposta in preparazione;
- in attesa di approvazione;
- approvato;
- risposta inviata;
- in attesa dell'utente;
- risolto;
- archiviato.

L'elenco definitivo degli stati deve rimanere sufficientemente piccolo.

Non devono essere creati stati differenti per ogni possibile situazione.

---

## 18. Fonti utilizzate nelle risposte

Quando un agente utilizza informazioni esterne per preparare una risposta, deve poter registrare le fonti rilevanti.

Le fonti devono rispettare SOURCE-SPEC.md e CITATION-SPEC.md quando applicabili.

Una risposta email non deve necessariamente contenere una bibliografia formale.

Quando una fonte è importante per verificare una risposta, l'agente deve poterla indicare nella propria registrazione operativa.

---

## 19. Ricerca online

Gli agenti possono effettuare ricerche online per rispondere alle email quando:

- la domanda richiede informazioni aggiornate;
- le informazioni interne non sono sufficienti;
- è necessario verificare un'affermazione;
- è richiesta una fonte esterna.

Le ricerche devono rispettare i budget computazionali stabiliti dal workflow.

Le ricerche ricorrenti devono utilizzare, quando possibile, soglie di costo e profondità appropriate.

Una domanda esplicitamente richiesta dal proprietario può utilizzare un budget superiore.

---

## 20. Email e fonti private

Un'email può contenere o riferirsi a materiale privato.

Il fatto che un agente possa leggere il materiale non implica che possa:

- pubblicarlo;
- redistribuirlo;
- allegarlo a una risposta;
- caricarlo in uno storage pubblico.

Devono essere rispettate le distinzioni definite in MEDIA-SPEC.md.

---

## 21. Allegati

Gli allegati devono essere trattati come media.

Quando un allegato diventa una risorsa riutilizzabile, deve poter essere catalogato secondo MEDIA-SPEC.md e, quando appropriato, SOURCE-SPEC.md o DATASET-SPEC.md.

Gli allegati non devono essere automaticamente copiati nello storage pubblico.

---

## 22. Invio di materiali

Quando un utente richiede un file o un materiale, il sistema deve verificare:

- se può essere distribuito;
- a chi;
- attraverso quale canale;
- con quali eventuali limitazioni.

Il permesso di lettura da parte dell'agente non costituisce autorizzazione alla redistribuzione.

---

## 23. Programmi email

La newsletter deve essere distinta dalle altre possibili sequenze o programmi email.

Il modello deve poter distinguere almeno:

- newsletter;
- sequenze associate a guide;
- comunicazioni transazionali;
- assistenza individuale;
- eventuali futuri programmi email.

La creazione di nuovi programmi non deve richiedere una modifica del modello generale delle email.

---

## 24. Newsletter

La newsletter contiene principalmente un riepilogo degli articoli pubblicati dall'ultima uscita.

La newsletter non deve essere confusa con una sequenza automatica associata a una guida.

La frequenza deve essere sostenibile e non deve dipendere necessariamente dalla pubblicazione di un singolo articolo.

Il sistema dovrebbe poter individuare automaticamente gli articoli pubblicati dall'ultima newsletter e preparare una proposta editoriale.

La proposta deve comunque essere approvata prima dell'invio.

---

## 25. Sequenze

Le sequenze possono essere associate a specifiche esperienze, guide o prodotti.

Esempi:

- percorso settimanale associato a una guida;
- meditazione guidata audio;
- percorso didattico;
- follow-up relativo a un materiale richiesto.

Le sequenze non devono essere confuse con la newsletter.

Ogni programma può definire:

- pubblico;
- lingua;
- frequenza;
- contenuti;
- condizioni di ingresso;
- condizioni di uscita;
- stato;
- metriche.

L'automazione della sequenza non autorizza autonomamente l'invio.

---

## 26. Guide a pagamento

Le email possono essere utilizzate per distribuire materiali associati a guide a pagamento.

Questi materiali possono comprendere:

- audio;
- PDF;
- EPUB;
- dataset;
- altri file.

I materiali devono essere conservati in uno storage appropriato e non devono dipendere dal repository Git del progetto.

Le modalità tecniche di distribuzione appartengono a DISTRIBUTION-SPEC.md e MEDIA-SPEC.md.

---

## 27. Lingua del destinatario

Il sistema dovrebbe poter determinare la lingua preferita del destinatario senza richiederla esplicitamente nel modulo di iscrizione quando ciò non è necessario.

Le lingue inizialmente supportate sono:

- italiano;
- inglese.

La lingua può essere determinata utilizzando più segnali, ordinati per affidabilità.

Esempi:

1. lingua utilizzata dal destinatario nelle conversazioni precedenti;
2. lingua utilizzata esplicitamente in una risposta;
3. lingua del contenuto attraverso cui il destinatario è entrato nel programma;
4. preferenze eventualmente disponibili nella piattaforma email;
5. lingua del browser o altri segnali tecnici disponibili;
6. euristiche sull'indirizzo o sul dominio, soltanto come segnali deboli.

Il sistema dovrebbe poter conservare:

- lingua stimata;
- livello di confidenza;
- origine della stima.

La lingua stimata deve poter essere modificata quando emergono informazioni migliori.

Un segnale debole non deve prevalere su una preferenza linguistica esplicita o chiaramente osservata.

Quando la lingua non è sufficientemente determinabile, deve essere utilizzata una lingua di fallback definita dal programma email.

---

## 28. Link nei messaggi

I link inseriti nelle email devono essere verificati quando possibile.

Quando un link comporta un'azione con effetti sul sistema, deve essere protetto secondo SECURITY-SPEC.md.

Non devono essere inseriti automaticamente URL che consentano azioni sensibili senza adeguate protezioni.

---

## 29. Autenticazione email

La configurazione tecnica del sistema email deve prevedere, quando applicabile:

- SPF;
- DKIM;
- DMARC.

La configurazione concreta appartiene alla parte tecnica e all'infrastruttura.

La sicurezza del dominio email deve essere considerata parte della sicurezza complessiva del progetto.

---

## 30. Accesso ai provider

L'accesso degli agenti al provider email deve utilizzare meccanismi di autenticazione appropriati.

Quando sono disponibili autorizzazioni granulari, devono essere preferite autorizzazioni limitate alle funzioni realmente necessarie.

Non devono essere richiesti permessi più ampi soltanto per comodità.

Le autorizzazioni del provider devono essere coerenti con SECURITY-SPEC.md.

---

## 31. Privacy

Le email possono contenere informazioni personali o sensibili.

Il sistema deve evitare di:

- pubblicare automaticamente il contenuto delle email;
- inserire dati personali negli articoli;
- utilizzare informazioni private per scopi non necessari;
- trasferire email a servizi esterni senza una ragione operativa appropriata;
- conservare copie inutili.

La gestione concreta dei dati personali deve rispettare le regole applicabili al progetto.

---

## 32. Conservazione

Le email devono essere conservate secondo le esigenze operative.

Non è necessario duplicare indefinitamente ogni messaggio in sistemi differenti.

Quando il provider conserva già la conversazione e non esiste una necessità di copia locale, deve essere evitata una duplicazione inutile.

Devono però essere conservati i riferimenti necessari a mantenere:

- stato;
- classificazione;
- collegamenti;
- approvazioni;
- analytics;
- decisioni operative.

---

## 33. Backup

Le informazioni email necessarie al funzionamento del sistema devono rientrare nella strategia di backup.

Il backup non deve necessariamente contenere una copia integrale della casella se ciò non è necessario.

La strategia complessiva è definita in BACKUP-SPEC.md.

---

## 34. Analytics

Il sistema deve poter produrre statistiche sulle email quando i dati disponibili lo consentono.

Possono essere monitorati:

- numero di messaggi;
- numero di conversazioni;
- tempo medio di risposta;
- richieste per categoria;
- richieste per guida;
- richieste per articolo;
- tasso di risposta;
- richieste ricorrenti;
- problemi ricorrenti;
- feedback positivi;
- feedback negativi;
- richieste non risolte.

Le metriche devono essere interpretate nel loro contesto.

---

## 35. Analytics storiche

Le statistiche devono poter essere confrontate nel tempo.

Quando possibile il sistema deve conservare aggregati storici sufficienti a individuare:

- cambiamenti;
- stagionalità;
- aumento di richieste;
- diminuzione di richieste;
- problemi emergenti;
- effetti di modifiche al sito.

Non è necessario conservare indefinitamente ogni metrica grezza se gli aggregati sono sufficienti per gli scopi previsti.

---

## 36. Collegamento con analytics del sito

Le email devono poter essere analizzate insieme ai dati del sito quando esiste una relazione affidabile.

Esempi:

- aumento delle visite a una guida → aumento delle domande;
- pagina con molte visite → molte richieste di chiarimento;
- articolo con traffico elevato → feedback ricorrenti;
- modifica di una guida → cambiamento nel tipo di domande ricevute.

Il collegamento deve utilizzare soltanto dati sufficienti e appropriati.

Non deve essere creato un sistema di tracciamento invasivo soltanto per ottenere correlazioni.

---

## 37. Ruolo di coordinamento email e analytics

Il sistema può prevedere un ruolo incaricato di analizzare congiuntamente:

- email;
- feedback;
- analytics del sito;
- guide;
- articoli;
- dati di distribuzione.

Il ruolo deve produrre report periodici che evidenzino:

- problemi ricorrenti;
- domande frequenti;
- contenuti poco chiari;
- richieste non coperte;
- opportunità di miglioramento;
- anomalie;
- possibili correlazioni.

Il ruolo non decide autonomamente quali modifiche editoriali introdurre.

---

## 38. Feedback come segnale editoriale

Il feedback ricevuto via email può contribuire a individuare:

- parti poco comprensibili;
- errori;
- lacune;
- richieste di approfondimento;
- problemi nelle traduzioni;
- nuove fonti;
- nuovi dataset;
- nuove esigenze degli utenti.

Il feedback non deve essere considerato automaticamente corretto.

Quando contiene un'affermazione fattuale, deve poter essere verificato.

---

## 39. Risposte alle critiche

Le critiche ricevute via email devono essere trattate come informazioni da valutare, non come errori dell'utente.

Quando una critica è fondata, il sistema deve poter proporre:

- correzione;
- chiarimento;
- aggiunta di fonte;
- modifica dell'articolo;
- modifica della guida.

Quando una critica non è fondata, l'agente può proporre una risposta argomentata.

---

## 40. Tono

Il tono deve dipendere dal tipo di comunicazione.

### Assistenza e risposte individuali

Il tono dovrebbe essere:

- molto umano;
- caldo;
- materno;
- accogliente;
- colorato;
- spontaneo;
- rispettoso;
- non artificiosamente entusiasta.

La risposta non deve sembrare generata da un sistema automatico.

Il tono deve comunque adattarsi alla situazione.

Una comunicazione delicata, tecnica o problematica non deve essere resa artificialmente allegra.

### Newsletter

La newsletter può avere una voce personale e riconoscibile, coerente con l'identità di StamoTenti.

### Sequenze

Le sequenze possono avere una voce propria coerente con l'esperienza proposta.

Il tono non deve essere trasformato in una formula rigida.

---

## 41. Risposte generate dagli agenti

Quando un agente prepara una risposta, deve evitare di:

- inventare fatti;
- inventare fonti;
- attribuire intenzioni all'utente;
- promettere azioni non disponibili;
- dichiarare verifiche non effettuate.

Se non dispone di informazioni sufficienti, deve dichiararlo.

---

## 42. Casi che richiedono maggiore cautela

Devono essere trattati con maggiore attenzione:

- richieste legali;
- richieste mediche;
- richieste finanziarie;
- problemi di sicurezza;
- richieste relative a dati personali;
- richieste di accesso a materiali privati;
- richieste di rimborso o pagamenti;
- contestazioni rilevanti.

Il workflow deve poter richiedere intervento umano.

---

## 43. Limiti degli agenti

Un agente email non deve poter:

- modificare arbitrariamente le specifiche del progetto;
- pubblicare materiale privato;
- modificare autorizzazioni di sicurezza senza procedura;
- distribuire file non autorizzati;
- cancellare definitivamente informazioni senza autorizzazione;
- assumere impegni economici;
- modificare autonomamente decisioni editoriali fondamentali;
- inviare email senza approvazione del proprietario.

I permessi concreti sono definiti dal workflow e dalla sicurezza, non da questo singolo documento.

---

## 44. Intervento manuale

Il proprietario deve poter:

- rispondere direttamente;
- modificare una bozza;
- riassegnare una conversazione;
- cambiare priorità;
- cambiare classificazione;
- archiviare;
- riaprire;
- correggere metadata;
- disattivare un'automazione;
- modificare il contenuto di una newsletter;
- modificare una sequenza.

Le automazioni non devono creare dipendenze che rendano difficile l'intervento manuale.

---

## 45. Memoria operativa

Le esperienze ricorrenti nella gestione delle email possono produrre informazioni utili per il futuro.

Gli agenti possono registrare:

- risposte che hanno funzionato;
- errori ricorrenti;
- casi particolari;
- procedure utili;
- categorie difficili da classificare;
- richieste ricorrenti.

Queste informazioni devono essere mantenute nella memoria operativa secondo la relativa specifica.

Non devono essere trasformate automaticamente in regole rigide.

---

## 46. Budget computazionale

Le attività email ricorrenti devono utilizzare budget computazionali proporzionati.

Esempi:

- classificazione di un messaggio → budget basso;
- estrazione di informazioni → budget basso o medio;
- proposta di risposta → budget medio;
- ricerca bibliografica → budget medio o alto;
- analisi approfondita di una questione → budget alto.

Il budget è un limite operativo predefinito.

Il proprietario deve poter richiedere esplicitamente un'analisi più onerosa.

Quando un'attività supera significativamente il budget previsto, l'agente deve preferibilmente:

- fornire un risultato parziale;
- chiedere se procedere;
- utilizzare un percorso alternativo più economico.

---

## 47. Reporting

Il sistema deve poter produrre report periodici sulle email.

I report possono includere:

- volume;
- categorie;
- tempi di risposta;
- problemi ricorrenti;
- feedback;
- guide coinvolte;
- articoli coinvolti;
- correlazioni con analytics;
- richieste che richiedono intervento.

La periodicità deve essere sostenibile.

Non è necessario produrre report troppo frequenti quando non apportano informazioni nuove.

---

## 48. Notifiche

Le richieste che richiedono intervento del proprietario devono essere presentate in modo:

- sintetico;
- persistente;
- ricercabile;
- prioritizzato;
- facilmente distinguibile dalle notifiche ordinarie.

Il sistema non deve dipendere esclusivamente da notifiche effimere.

Le richieste importanti devono rimanere disponibili fino alla decisione.

La gestione generale delle approvazioni è definita in APPROVAL-SPEC.md.

---

## 49. Programmazione e invio

Un agente può:

- preparare una newsletter;
- assemblare gli articoli pubblicati dall'ultima uscita;
- preparare una sequenza;
- proporre una data di invio;
- verificare i destinatari;
- produrre un'anteprima;
- produrre un report di controllo.

Nessuna di queste attività equivale all'autorizzazione all'invio.

Prima dell'invio deve esistere una decisione approvativa del proprietario.

Una programmazione automatica non costituisce approvazione permanente.

---

## 50. Evoluzione del provider

Il sistema deve poter cambiare provider email senza richiedere una modifica del modello concettuale.

L'integrazione con un provider specifico deve essere isolata.

Il cambio di provider non deve modificare:

- modello delle conversazioni;
- classificazioni;
- collegamenti con guide;
- analytics;
- approvazioni;
- memoria operativa.

---

## 51. Semplicità

Il sistema email deve evitare complessità non necessarie.

Non devono essere introdotti:

- CRM completi;
- sistemi di ticketing complessi;
- automazioni eccessive;
- classificazioni inutilmente dettagliate;

finché le esigenze reali del progetto non li giustificano.

La complessità può essere introdotta progressivamente.

---

## 52. Principio di sostituibilità

I ruoli incaricati della gestione email possono cambiare.

Un ruolo può essere svolto da:

- Cloud Code;
- un altro agente;
- un modello locale;
- un servizio automatico;
- una combinazione di strumenti.

La specifica descrive responsabilità e vincoli, non l'implementazione del ruolo.

---

## 53. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. MEDIA-SPEC.md definisce i media;
4. SECURITY-SPEC.md definisce sicurezza e accessi;
5. APPROVAL-SPEC.md definisce approvazioni;
6. WORKFLOW-SPEC.md definisce workflow e ruoli;
7. EMAIL-SPEC.md definisce il comportamento specifico della gestione email;
8. le specifiche tecniche definiscono l'implementazione;
9. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
