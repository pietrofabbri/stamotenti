# StamoTenti — TESTING SPECIFICATION

## 1. Scopo

Questo documento definisce come StamoTenti verifica che modifiche,
contenuti, automazioni e componenti tecnici funzionino in modo
sufficientemente affidabile.

Il testing deve ridurre:

- regressioni;
- errori;
- perdita di dati;
- problemi di sicurezza;
- problemi di privacy;
- problemi di accessibilità;
- errori editoriali;
- malfunzionamenti di distribuzione.

Non deve però trasformare il progetto in un sistema di test
sproporzionatamente complesso.

---

## 2. Principio di proporzionalità

Il livello di testing deve essere proporzionato a:

- rischio;
- impatto;
- complessità;
- reversibilità;
- frequenza della modifica;
- sensibilità dei dati;
- criticità della funzionalità.

Una modifica banale non richiede lo stesso testing di una migrazione
dati.

---

## 3. Tipi di test

Il progetto può utilizzare, quando utili:

- test unitari;
- test di integrazione;
- test end-to-end;
- test manuali;
- test editoriali;
- test di sicurezza;
- test di privacy;
- test di accessibilità;
- test di performance;
- test di build;
- test di distribuzione;
- controlli statici;
- smoke test.

L'elenco è aperto.

---

## 4. Test automatici

I test automatici sono preferibili quando:

- il controllo è ripetitivo;
- il comportamento è deterministico;
- il test è economico da mantenere;
- il rischio di regressione è significativo.

Non devono essere introdotti soltanto per aumentare il numero di test.

---

## 5. Test manuali

I test manuali rimangono appropriati quando:

- è necessario valutare leggibilità;
- è necessario valutare tono;
- è necessario valutare esperienza utente;
- il comportamento è difficile da automatizzare;
- il giudizio umano produce un valore significativo.

---

## 6. Test unitari

I test unitari possono verificare singole funzioni o componenti.

Sono particolarmente utili per logiche:

- deterministiche;
- riutilizzate frequentemente;
- critiche;
- soggette a regressioni.

---

## 7. Test di integrazione

I test di integrazione verificano il comportamento tra componenti.

Possono riguardare:

- Hugo;
- script;
- database o storage;
- email;
- API;
- analytics;
- sistemi di distribuzione;
- automazioni.

---

## 8. Test end-to-end

I test end-to-end possono verificare percorsi completi.

Devono essere utilizzati quando il valore del controllo giustifica il
costo di manutenzione.

---

## 9. Smoke test

Dopo una modifica significativa possono essere eseguiti controlli
rapidi per verificare che il sistema fondamentale funzioni.

Esempi:

- il sito viene generato;
- le pagine principali sono raggiungibili;
- non ci sono errori evidenti;
- i link fondamentali funzionano;
- gli asset principali vengono caricati.

---

## 10. Build

Una modifica al codice o alla configurazione deve essere sottoposta
alla build pertinente quando possibile.

Una build fallita deve essere segnalata.

---

## 11. Test della documentazione

Anche le SPEC possono essere sottoposte a controlli.

Possono essere verificati:

- Markdown;
- link;
- heading;
- duplicazioni;
- riferimenti a file inesistenti;
- blocchi di codice;
- errori evidenti.

---

## 12. Test dei contenuti

Gli articoli possono richiedere controlli su:

- struttura;
- fonti;
- citazioni;
- lingua;
- link;
- immagini;
- metadata;
- accessibilità;
- SEO;
- GEO.

---

## 13. Test delle citazioni

Quando un articolo viene modificato, devono essere considerati:

- presenza delle citazioni;
- corrispondenza con le fonti;
- correttezza dei riferimenti;
- eventuali link;
- eventuali posizioni specifiche nella fonte.

---

## 14. Test delle fonti

Le fonti possono essere controllate per:

- identificabilità;
- provenienza;
- metadati;
- accessibilità;
- coerenza con la citazione.

Un test automatico non può garantire la correttezza scientifica della
fonte.

---

## 15. Test multilingue

Quando un contenuto è disponibile in più lingue, possono essere
controllati:

- presenza delle versioni;
- link tra versioni;
- metadata;
- terminologia;
- coerenza strutturale.

Non si deve presumere che due traduzioni debbano essere letteralmente
identiche.

---

## 16. Test di accessibilità

Le modifiche al sito devono considerare l'accessibilità.

Possono essere utilizzati:

- controlli automatici;
- navigazione da tastiera;
- verifica del contrasto;
- verifica dei testi alternativi;
- verifica della struttura semantica;
- test manuali.

ACCESSIBILITY-SPEC.md definisce i requisiti specifici.

---

## 17. Test di sicurezza

Le modifiche che interessano sicurezza o infrastruttura devono essere
sottoposte a controlli appropriati.

Possono comprendere:

- scanning;
- dependency audit;
- controllo dei secret;
- verifica delle autorizzazioni;
- test di input;
- test delle configurazioni.

---

## 18. Test della privacy

Le modifiche che coinvolgono dati personali devono verificare che:

- i dati non vengano esposti;
- gli accessi siano appropriati;
- le informazioni non vengano loggate inutilmente;
- i dati non vengano distribuiti accidentalmente.

---

## 19. Test email

Le modifiche al sistema email devono essere testate senza inviare
automaticamente email reali non approvate.

Possono essere utilizzati:

- destinatari di test;
- preview;
- rendering locale;
- controlli dei link;
- controlli della lingua;
- controlli dei dati.

---

## 20. Approvazione delle email

Il superamento dei test non costituisce approvazione per l'invio.

Le regole di approvazione sono definite da EMAIL-SPEC.md e
APPROVAL-SPEC.md.

---

## 21. Test della distribuzione

I canali di distribuzione devono essere testati in modo da evitare:

- destinatari errati;
- contenuti errati;
- link errati;
- pubblicazioni duplicate;
- pubblicazioni non autorizzate.

---

## 22. Telegram, Reddit e forum

Il sistema può testare il monitoraggio di:

- Telegram;
- Reddit;
- forum;
- community.

Il monitoraggio non implica la pubblicazione automatica.

Il comportamento previsto è principalmente la segnalazione di
discussioni pertinenti all'autore.

---

## 23. Test dei link

Quando possibile, devono essere controllati:

- link interni;
- link esterni;
- redirect;
- link nelle email;
- link nei metadata.

I link esterni possono cambiare nel tempo e un errore temporaneo non
deve necessariamente essere interpretato come errore permanente.

---

## 24. Test delle immagini e dei media

Possono essere verificati:

- esistenza del file;
- formato;
- integrità;
- dimensioni;
- alt text;
- riferimenti;
- licenza quando pertinente.

---

## 25. Test dei dataset

I dataset possono richiedere controlli su:

- formato;
- schema;
- completezza;
- duplicati;
- valori anomali;
- metadata;
- provenienza.

DATASET-SPEC.md definisce le esigenze specifiche.

---

## 26. Test dei backup

I backup devono essere verificati periodicamente.

Un backup non deve essere considerato affidabile soltanto perché è
stato creato correttamente.

Quando utile devono essere eseguiti restore test.

BACKUP-SPEC.md definisce il sistema di backup.

---

## 27. Test di ripristino

Per sistemi o dati importanti deve essere possibile verificare che un
backup possa essere effettivamente utilizzato.

Il livello di test deve essere proporzionato all'importanza dei dati.

---

## 28. Test delle automazioni

Le automazioni devono essere testate prima di poter operare su dati o
canali reali quando il rischio lo richiede.

In particolare deve essere verificato che:

- non eseguano azioni fuori dal proprio scopo;
- rispettino le autorizzazioni;
- gestiscano gli errori;
- siano disattivabili.

---

## 29. Test degli agenti

Gli agenti o ruoli possono essere testati rispetto a:

- input;
- output;
- limiti;
- autorizzazioni;
- comportamento in caso di errore.

Il test non deve dipendere necessariamente da uno specifico modello AI.

---

## 30. Test dei modelli

Quando un modello AI viene sostituito, può essere eseguita una verifica
di regressione sui compiti rilevanti.

Non è necessario che il nuovo modello produca output identici.

Deve invece mantenere i requisiti funzionali e qualitativi pertinenti.

---

## 31. Test di stile

I controlli sullo stile possono verificare:

- chiarezza;
- leggibilità;
- coerenza;
- naturalezza;
- variabilità linguistica;
- assenza di pattern artificiali evidenti.

Un detector AI non deve essere considerato una misura definitiva
dell'umanità di un testo.

---

## 32. Prima parte degli articoli

La prima parte accessibile degli articoli può essere valutata per:

- chiarezza;
- naturalezza;
- accessibilità;
- capacità di introdurre il problema;
- collegamento alla parte più approfondita.

---

## 33. Seconda parte degli articoli

La parte più accademica deve mantenere:

- rigore;
- precisione;
- chiarezza;
- appropriatezza terminologica.

Il revisore stilistico non deve renderla artificialmente informale.

---

## 34. Test SEO

Possono essere verificati:

- title;
- description;
- heading;
- canonical;
- sitemap;
- link;
- structured data;
- metadata.

SEO-SPEC.md definisce i requisiti specifici.

---

## 35. Test GEO

Possono essere verificati:

- chiarezza delle entità;
- struttura delle informazioni;
- citabilità;
- coerenza terminologica;
- metadata;
- collegamenti tra concetti.

---

## 36. Test di performance

Quando rilevante possono essere controllati:

- tempo di build;
- dimensione delle pagine;
- dimensione degli asset;
- tempi di caricamento;
- consumo di risorse.

Non è necessario ottimizzare prematuramente ogni componente.

---

## 37. Test grafici

Il sito deve poter essere verificato anche visivamente.

Possono essere controllati:

- coerenza grafica;
- layout;
- responsive behavior;
- leggibilità;
- immagini;
- spaziature;
- componenti.

Il relativo ruolo di controllo può utilizzare screenshot o preview.

---

## 38. Test cross-browser

Quando necessario, il sito può essere verificato su più browser e
dispositivi.

La copertura deve essere proporzionata al pubblico e al rischio.

---

## 39. Test di regressione

Dopo una modifica significativa devono essere verificati i
comportamenti precedentemente funzionanti che potrebbero essere stati
influenzati.

---

## 40. Test prima del deploy

Il deploy deve essere preceduto dai test appropriati alla modifica.

Non è necessario eseguire sempre l'intera suite disponibile.

---

## 41. Test dopo il deploy

Dopo modifiche significative possono essere eseguiti:

- smoke test;
- controlli delle pagine;
- controlli dei link;
- controlli di monitoring;
- verifica degli errori.

---

## 42. Test in produzione

Quando possibile, i test distruttivi devono essere evitati in
produzione.

Devono essere preferiti:

- ambiente di test;
- preview;
- dati sintetici;
- staging;
- destinatari di test.

---

## 43. Dati di test

Quando possibile devono essere utilizzati dati sintetici.

Non devono essere utilizzati dati personali reali nei test se non
necessario.

---

## 44. Email di test

Le email di test devono evitare di coinvolgere utenti reali quando non
necessario.

---

## 45. Test di privacy con dati reali

L'utilizzo di dati reali nei test deve essere limitato e giustificato.

Quando possibile devono essere utilizzati dati anonimizzati o
sintetici.

---

## 46. Test falliti

Un test fallito deve essere interpretato nel contesto.

Può indicare:

- regressione;
- errore del test;
- ambiente non disponibile;
- dipendenza esterna;
- comportamento previsto ma non aggiornato nel test.

Non deve essere ignorato automaticamente.

---

## 47. Flaky tests

Un test instabile non deve essere considerato affidabile.

Quando un test fallisce in modo intermittente deve essere:

- corretto;
- isolato;
- sostituito;
- oppure documentato come instabile fino alla risoluzione.

---

## 48. Test troppo costosi

Un test che costa più del beneficio che produce deve essere rivalutato.

Il numero di test non è un obiettivo in sé.

---

## 49. Test mancanti

Se un bug si ripete, può essere opportuno introdurre un test che lo
rilevi in futuro.

---

## 50. Automazione delle richieste ricorrenti

Quando una verifica viene eseguita frequentemente, può essere
automatizzata.

La stabilizzazione del codice può individuare queste opportunità.

---

## 51. Test e change management

CHANGE-MANAGEMENT-SPEC.md determina il livello generale di controllo
delle modifiche.

TESTING-SPEC.md definisce come verificare il comportamento.

---

## 52. Test e approval

Il superamento dei test non sostituisce un'approvazione quando
APPROVAL-SPEC.md la richiede.

---

## 53. Test e sicurezza

Un test positivo non costituisce una garanzia assoluta di sicurezza.

La sicurezza deve essere trattata come processo continuo.

---

## 54. Test e privacy

Un test positivo non autorizza nuovi trattamenti di dati personali.

---

## 55. Test e monitoraggio

MONITORING-SPEC.md può individuare problemi che non sono emersi durante
i test.

Testing e monitoring sono complementari.

---

## 56. Test e memoria operativa

Quando un test rivela una lezione importante, questa può essere
conservata secondo OPERATIONAL-MEMORY-SPEC.md.

---

## 57. Test di compatibilità

Quando viene sostituito un componente, devono essere considerati gli
effetti sui componenti dipendenti.

---

## 58. Dipendenze esterne

I test che dipendono da servizi esterni possono fallire per ragioni
esterne al progetto.

Questo deve essere distinguibile quando possibile.

---

## 59. Mock

I mock possono essere utilizzati quando:

- il servizio reale è costoso;
- il servizio reale è instabile;
- il test deve essere deterministico;
- l'utilizzo reale comporterebbe rischi.

I mock non sostituiscono tutti i test reali.

---

## 60. Test reali

Quando il comportamento di integrazione è importante, devono essere
eseguiti anche test contro l'ambiente reale o un ambiente equivalente
quando il rischio lo giustifica.

---

## 61. Test distruttivi

I test distruttivi devono essere eseguiti soltanto in ambienti o dati
predisposti per questo scopo.

---

## 62. Test di rollback

Quando un cambiamento è ad alto rischio, può essere opportuno verificare
anche il meccanismo di rollback.

---

## 63. Test di recovery

Per componenti critici può essere utile verificare:

- backup;
- ripristino;
- riconfigurazione;
- recupero da errore.

---

## 64. Test di sicurezza delle autorizzazioni

Devono essere verificati, quando pertinenti:

- chi può leggere;
- chi può modificare;
- chi può approvare;
- chi può pubblicare;
- chi può inviare;
- chi può accedere a dati privati.

---

## 65. Agenti e autorizzazioni

Un agente non deve poter superare un test semplicemente perché il
proprio modello è considerato affidabile.

Le autorizzazioni devono essere controllate indipendentemente.

---

## 66. Test delle regole di approvazione

Le automazioni che richiedono approvazione devono essere testate anche
per verificare che non possano bypassarla.

---

## 67. Test dei log

Quando pertinente, deve essere verificato che i log:

- contengano informazioni utili;
- non contengano dati sensibili inutili;
- permettano di diagnosticare gli errori.

---

## 68. Test delle configurazioni

Le configurazioni devono essere validate quando una modifica può
comprometterne il funzionamento.

---

## 69. Test dei secret

I test e gli strumenti automatici devono evitare di stampare o
distribuire secret.

Può essere utilizzato un controllo automatico per rilevare possibili
secret accidentalmente presenti nel repository.

---

## 70. Test del repository

Quando utile possono essere verificati:

- file inattesi;
- secret;
- file temporanei;
- artefatti;
- grandi file;
- licenze;
- struttura.

---

## 71. Test prima del commit

Per modifiche rilevanti possono essere eseguiti controlli prima del
commit.

Non tutti i controlli devono necessariamente essere eseguiti a ogni
commit.

---

## 72. Test prima del merge

Quando si utilizza un processo di merge, possono essere richiesti
controlli automatici appropriati.

---

## 73. Test prima della pubblicazione

Una pubblicazione deve rispettare i controlli previsti dal relativo
workflow.

---

## 74. Evidenza dei test

Per modifiche significative deve essere possibile sapere quali test
sono stati eseguiti e con quale risultato.

Non è necessario conservare evidenze dettagliate per ogni modifica
minore.

---

## 75. Risultati dei test

I risultati possono essere:

- pass;
- fail;
- blocked;
- not applicable;
- inconclusive.

L'elenco è aperto.

---

## 76. Test non applicabili

Un test non pertinente non deve essere eseguito artificialmente solo
per soddisfare una checklist.

---

## 77. Test bloccati

Se un test non può essere eseguito per una dipendenza esterna o un
problema ambientale, deve essere indicato.

---

## 78. Decisioni basate sui test

I risultati dei test costituiscono evidenza per una decisione.

Non sostituiscono automaticamente il giudizio umano.

---

## 79. Nessuna falsa certezza

Il testing riduce il rischio ma non dimostra che il sistema sia privo
di errori.

---

## 80. Manutenibilità

I test devono essere mantenibili.

Un test fragile che richiede continue modifiche può produrre meno valore
di un controllo più semplice.

---

## 81. Modularità

I test devono essere quanto più possibile separabili dai componenti
che verificano.

La sostituzione di un modello o di un provider non dovrebbe richiedere
la riscrittura dell'intera strategia di test.

---

## 82. Economicità

Il costo dei test deve essere considerato insieme al rischio che
mitigano.

---

## 83. Durabilità

La strategia di testing deve continuare a funzionare anche quando
cambiano:

- modelli;
- agenti;
- provider;
- strumenti;
- infrastruttura.

---

## 84. Evoluzione

Nuovi test possono essere introdotti quando emergono nuovi rischi.

Test inutili possono essere rimossi.

---

## 85. Revisione

La strategia di testing deve essere periodicamente rivalutata.

Una revisione è particolarmente utile quando:

- cambiano architettura o workflow;
- aumentano le automazioni;
- emergono regressioni;
- aumentano i costi di test;
- cambiano i canali di distribuzione.

---

## 86. Principio finale

Il testing deve rendere più sicuro cambiare StamoTenti.

Non deve diventare un ostacolo all'evoluzione.

Il principio guida è:

> testare ciò che può ragionevolmente rompersi, con una profondità
> proporzionata a quanto sarebbe grave romperlo.

---

## 87. Gerarchia

In caso di conflitto:

1. i documenti fondativi definiscono i principi superiori;
2. SECURITY-SPEC.md e PRIVACY-SPEC.md definiscono i vincoli relativi
   a sicurezza e privacy;
3. le SPEC di dominio definiscono i requisiti da verificare;
4. TESTING-SPEC.md definisce la strategia generale di testing;
5. CHANGE-MANAGEMENT-SPEC.md determina il livello di controllo della
   modifica;
6. APPROVAL-SPEC.md determina le approvazioni necessarie;
7. WORKFLOW-SPEC.md definisce il workflow operativo;
8. gli strumenti e il codice implementano i test.
