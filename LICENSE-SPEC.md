# StamoTenti — LICENSE SPECIFICATION

## 1. Scopo

Questo documento definisce come StamoTenti identifica, assegna,
documenta e verifica le licenze applicabili ai diversi materiali del
progetto.

L'obiettivo è:

- rendere chiaro cosa può essere riutilizzato;
- distinguere i diversi tipi di materiale;
- rispettare i diritti di terzi;
- evitare ambiguità sulla licenza;
- mantenere il progetto facilmente manutenibile;
- permettere l'automazione dei controlli quando utile.

La specifica non determina necessariamente una singola licenza per
l'intero progetto.

---

## 2. Principio fondamentale

La licenza deve essere determinata in funzione dell'oggetto a cui si
applica.

In particolare possono avere regimi differenti:

- codice;
- documentazione;
- specifiche;
- articoli;
- dataset;
- immagini;
- fotografie;
- audio;
- video;
- altri media;
- materiali di terzi;
- dipendenze software;
- font;
- dati provenienti da fonti esterne.

Non si deve presumere che una licenza applicabile a una categoria si
applichi automaticamente alle altre.

---

## 3. Licenza del progetto

La licenza generale del progetto deve essere esplicitamente identificata.

Quando categorie differenti hanno licenze differenti, il progetto deve
rendere evidente quale licenza si applica a ciascuna categoria.

L'assenza di una licenza generale unica non costituisce un problema se le
licenze dei singoli materiali sono chiaramente identificabili.

Quando il progetto utilizza licenze differenti per categorie
differenti, questa distinzione deve essere resa comprensibile.

---

## 4. Nessuna licenza implicita

L'assenza di una licenza esplicita non deve essere interpretata come permesso
di riutilizzo.

Quando la licenza non è determinabile con sufficiente sicurezza, il materiale
deve essere trattato prudentemente e non deve essere distribuito o riutilizzato
in modo incompatibile con i diritti noti.

Quando non è possibile determinare la licenza applicabile, il materiale
deve essere trattato come non liberamente riutilizzabile fino a quando
la situazione non sia chiarita.

---

## 5. Codice

Il codice può avere una licenza specifica distinta da quella degli
altri materiali.

La licenza del codice deve essere identificabile in modo chiaro.

Quando appropriato, possono essere utilizzati identificatori SPDX.

---

## 6. Documentazione

La documentazione può avere una licenza distinta dal codice.

Rientrano nella documentazione, tra gli altri:

- README;
- guide;
- documentazione tecnica;
- documentazione progettuale.

---

## 7. Specifiche

Le SPEC costituiscono una categoria documentale distinta.

La loro licenza deve essere esplicitamente determinabile.

La scelta concreta della licenza viene definita nelle decisioni
appropriate e non deve essere inventata dagli agenti.

---

## 8. Articoli

Gli articoli possono avere condizioni di riutilizzo differenti rispetto
al codice.

La licenza applicabile deve essere individuabile senza ambiguità.

---

## 9. Dataset

I dataset possono richiedere licenze o condizioni differenti.

DATASET-SPEC.md definisce gli aspetti specifici della gestione dei
dataset.

La licenza deve essere conservata insieme ai relativi metadati quando
possibile.

---

## 10. Media

I media possono essere soggetti a diritti differenti.

MEDIA-SPEC.md definisce la gestione dei media.

Un'immagine disponibile tecnicamente non deve essere considerata per
questo motivo liberamente redistribuibile.

---

## 11. Materiali di terzi

I materiali provenienti da terzi devono conservare, quando disponibili:

- autore;
- titolare dei diritti;
- licenza;
- fonte;
- condizioni rilevanti;
- eventuali obblighi di attribuzione.

La loro presenza nel repository o nel sito non modifica automaticamente
la licenza originaria.

---

## 12. Dipendenze

Le dipendenze software devono essere considerate separatamente.

Per ciascuna dipendenza rilevante devono poter essere individuati:

- nome;
- versione;
- licenza;
- fonte;
- eventuali obblighi significativi.

---

## 13. Compatibilità delle licenze

Una dipendenza non deve essere utilizzata o distribuita senza aver
considerato la compatibilità della relativa licenza con il modo in cui
StamoTenti la utilizza.

Quando la compatibilità non è chiara, deve essere segnalata.

---

## 14. Nessuna interpretazione giuridica automatica

Gli agenti possono:

- identificare licenze;
- raccogliere evidenze;
- confrontare condizioni;
- individuare possibili conflitti;
- preparare proposte;
- segnalare quando è necessaria una verifica ulteriore.

Gli agenti non devono presentare come certe conclusioni giuridiche che
dipendono da interpretazioni non verificate.

- identificare licenze;
- trovare incongruenze;
- confrontare metadati;
- segnalare possibili conflitti;
- proporre verifiche.

Non devono trasformare automaticamente un'analisi tecnica in una
certezza giuridica.

---

## 15. SPDX

Quando applicabile, StamoTenti può utilizzare gli identificatori SPDX.

Gli identificatori SPDX sono brevi, standardizzati e machine-readable.
La SPDX License List fornisce identificatori standard per licenze ed
eccezioni. :contentReference[oaicite:1]{index=1}

Esempio:

    SPDX-License-Identifier: MIT

Quando sono applicabili più licenze, può essere utilizzata una
license expression SPDX.

---

## 16. Copyright e licenza

Il copyright notice e la licenza sono concetti distinti.

L'indicazione della licenza non deve comportare la rimozione di
copyright notice esistenti.

Gli identificatori SPDX servono a comunicare informazioni sulla
licenza e non sostituiscono automaticamente le informazioni sul
copyright. :contentReference[oaicite:2]{index=2}

---

## 17. File di licenza

Quando una licenza viene applicata a un progetto o a una categoria
significativa di file, il testo della licenza deve essere reso
facilmente reperibile.

Quando appropriato, il repository può contenere:

- LICENSE;
- LICENSES/;
- NOTICE;
- altri file necessari.

La struttura concreta può evolvere.

---

## 18. Attribuzione

Quando una licenza richiede attribuzione, l'attribuzione deve essere
conservata e resa disponibile secondo le condizioni applicabili.

---

## 19. Licenze dei media

L'attribuzione e le condizioni dei media devono essere preservate
quando richiesto.

Non devono essere rimossi metadati o informazioni di licenza senza
valutazione.

---

## 20. Contenuti generati

Il fatto che un contenuto sia stato prodotto con l'aiuto di un modello
AI non determina automaticamente la licenza applicabile.

Devono essere considerate:

- natura del materiale;
- diritti dell'autore;
- strumenti utilizzati;
- termini applicabili;
- eventuale materiale di terzi incorporato.

---

## 21. Font

I font devono essere trattati come dipendenze o materiali con condizioni
proprie.

La loro licenza deve essere verificata prima della distribuzione.

---

## 22. Codice copiato o adattato

Il codice copiato da terzi non deve essere incorporato senza aver
verificato la relativa licenza.

Devono essere conservate, quando necessarie:

- attribuzione;
- copyright notice;
- testo della licenza;
- eventuali modifiche richieste.

---

## 23. Snippet

Anche piccoli snippet di codice possono essere soggetti a condizioni
di licenza.

La dimensione non determina automaticamente l'assenza di obblighi.

---

## 24. Licenze incompatibili

Una potenziale incompatibilità deve essere segnalata prima della
distribuzione quando ragionevolmente rilevabile.

La risoluzione deve essere valutata caso per caso.

---

## 25. Materiali senza licenza nota

Quando la licenza non è nota:

- non deve essere inventata;
- non deve essere dedotta soltanto dall'accessibilità del file;
- deve essere segnalata;
- deve essere verificata prima di un riutilizzo che richieda
  autorizzazione.

---

## 26. Fonti web

La possibilità di visualizzare o scaricare un contenuto da un sito non
implica automaticamente il diritto di copiarlo o redistribuirlo.

SOURCE-SPEC.md e MEDIA-SPEC.md devono essere considerate insieme alla
presente specifica.

---

## 27. Ricerca automatica

Gli agenti possono effettuare controlli automatici sulle licenze.

Possono essere utilizzati:

- scanner;
- package manager;
- SBOM;
- strumenti SPDX;
- altri strumenti equivalenti.

L'automazione produce evidenze e segnalazioni, non necessariamente
decisioni definitive.

---

## 28. SBOM

Quando utile, il progetto può generare un Software Bill of Materials
(SBOM) contenente informazioni sulle dipendenze.

La generazione di un SBOM deve essere proporzionata alle dimensioni e
alle esigenze del progetto.

---

## 29. Aggiornamento delle dipendenze

Quando una dipendenza cambia versione, deve essere considerato se è
cambiata anche:

- licenza;
- copyright;
- obbligo di attribuzione;
- condizioni di distribuzione.

---

## 30. Licenze obsolete o ritirate

Se una licenza viene modificata, ritirata o sostituita, il progetto
deve valutare se ciò incide sui materiali già utilizzati.

Non deve essere modificata retroattivamente una licenza senza una base
appropriata.

---

## 31. Modifiche della licenza

La modifica della licenza di un materiale deve essere considerata una
modifica significativa quando può incidere sui diritti degli utenti o
sui diritti di terzi.

Deve essere gestita secondo CHANGE-MANAGEMENT-SPEC.md e
APPROVAL-SPEC.md quando applicabile.

---

## 32. Licenze multiple

Un progetto o un file può essere soggetto a più licenze.

La combinazione deve essere espressa in modo non ambiguo.

Quando possibile, deve essere utilizzata una forma standardizzata.

---

## 33. License expression

Quando più licenze sono applicabili e la situazione lo permette, può
essere utilizzata una SPDX license expression.

Esempio:

    MIT OR Apache-2.0

Le espressioni devono riflettere effettivamente i diritti disponibili
e non devono essere costruite arbitrariamente.

---

## 34. Licenze custom

Se una licenza non dispone di un identificatore SPDX appropriato, può
essere utilizzato un riferimento esplicito alla licenza.

Non deve essere inventato un identificatore apparentemente ufficiale.

---

## 35. Verifica umana

Le situazioni ambigue devono poter essere sottoposte a verifica umana.

Gli agenti non devono nascondere l'incertezza per produrre una risposta
più semplice.

---

## 36. Audit

Periodicamente può essere effettuato un controllo sulle licenze.

Il controllo può comprendere:

- dipendenze;
- codice;
- media;
- dataset;
- documentazione;
- font;
- materiali esterni.

La periodicità deve essere proporzionata al rischio e alla frequenza
delle modifiche.

---

## 37. Licenze e distribuzione

Prima della distribuzione di un nuovo tipo di materiale devono essere
considerate le relative condizioni di licenza.

DISTRIBUTION-SPEC.md definisce le modalità di distribuzione.

---

## 38. Licenze e pubblicazione

La pubblicazione sul sito non deve modificare automaticamente i diritti
di riutilizzo del materiale.

Il sito deve comunicare chiaramente le condizioni applicabili.

---

## 39. Licenze e privacy

La licenza non costituisce autorizzazione a pubblicare dati personali.

I vincoli di privacy rimangono applicabili indipendentemente dalla
licenza del materiale.

---

## 40. Licenze e sicurezza

Le informazioni di licenza non devono contenere o esporre segreti,
credenziali o altri dati sensibili.

---

## 41. Licenze e fonti scientifiche

Una fonte scientifica può essere citata senza che ciò significhi che
il relativo contenuto possa essere riprodotto integralmente.

CITATION-SPEC.md definisce il sistema delle citazioni.

---

## 42. Licenze e citazioni

La citazione di una fonte e la licenza del materiale utilizzato sono
concetti distinti.

Una citazione corretta non sostituisce automaticamente un'eventuale
autorizzazione necessaria.

---

## 43. Licenze e ricerca

L'accesso a una fonte per attività di ricerca non implica
automaticamente il diritto di redistribuirne copie.

SOURCE-SPEC.md e MEDIA-SPEC.md devono essere considerate quando il
materiale viene acquisito.

---

## 44. Nessun vincolo artificiale

Il sistema di licensing non deve introdurre vincoli più restrittivi
di quelli realmente necessari.

La finalità è chiarezza e rispetto dei diritti, non la creazione di
ostacoli arbitrari.

---

## 45. Modularità

La gestione delle licenze deve essere sufficientemente modulare da
permettere di:

- cambiare licenza;
- aggiungere nuove categorie;
- sostituire dipendenze;
- cambiare strumenti;
- aggiungere nuovi media.

---

## 46. Manutenibilità

Le informazioni di licenza devono essere mantenibili senza dover
ricostruire manualmente l'intero progetto.

Quando utile, possono essere mantenuti metadati strutturati.

---

## 47. Durabilità

Il modello di licensing non deve dipendere inutilmente da un singolo
strumento.

Gli identificatori standard possono facilitare la migrazione verso
strumenti diversi.

---

## 48. Economicità

I controlli automatici sulle licenze devono essere introdotti quando
producono un beneficio sufficiente rispetto al loro costo e alla loro
complessità.

---

## 49. Ruolo degli agenti

Gli agenti possono:

- identificare licenze;
- verificare metadati;
- cercare incompatibilità;
- controllare dipendenze;
- proporre correzioni;
- generare report.

Non possono decidere autonomamente di concedere nuovi diritti a terzi.

---

## 50. Ruolo dell'autore

L'autore mantiene il controllo sulle decisioni relative alla licenza
dei materiali di cui dispone dei relativi diritti.

---

## 51. Materiali di terzi

Quando StamoTenti utilizza materiali di terzi, l'agente o il processo
che li acquisisce deve conservare, quando possibile, le informazioni
necessarie a ricostruirne la provenienza e le condizioni d'uso.

---

## 52. Provenienza

Per materiali rilevanti è utile conservare:

- fonte originale;
- URL o identificatore;
- autore;
- licenza;
- data di acquisizione quando utile;
- eventuali trasformazioni.

---

## 53. Trasformazioni

Una trasformazione di un materiale di terzi non elimina
automaticamente i relativi obblighi.

---

## 54. Derivative works

Quando una licenza disciplina le opere derivate, la natura della
trasformazione deve essere considerata.

Gli agenti possono segnalare il problema ma non devono assumere
automaticamente una qualificazione giuridica definitiva.

---

## 55. Compatibilità con le specifiche

Le altre SPEC devono rispettare le condizioni di licensing applicabili.

In caso di conflitto, il problema deve essere segnalato e risolto
prima della distribuzione del materiale interessato.

---

## 56. Modifica delle licenze delle dipendenze

Un aggiornamento di dipendenza che cambia la licenza deve essere
considerato durante il processo di aggiornamento.

---

## 57. Archiviazione

Le informazioni sulle licenze devono essere conservate insieme ai
materiali o in un sistema chiaramente collegato.

---

## 58. Verificabilità

Deve essere possibile, quando ragionevolmente necessario, rispondere alla
domanda:

> "Quale licenza si applica a questo materiale e da dove deriva questa
> informazione?"

---

## 59. Incertezza

Quando l'informazione è incerta, deve essere indicata come tale.

È preferibile una segnalazione di incertezza a una classificazione
errata presentata come certa.

---

## 60. Evoluzione

La struttura delle licenze può evolvere insieme al progetto.

Nuove categorie possono essere introdotte quando diventano necessarie.

Gli elenchi presenti in questa specifica non sono esaustivi.

---

## 61. Principio finale

StamoTenti deve essere aperto e riutilizzabile quando ciò è compatibile
con i diritti e le scelte del progetto.

La gestione delle licenze deve quindi perseguire contemporaneamente:

- chiarezza;
- correttezza;
- interoperabilità;
- rispetto dei diritti;
- semplicità;
- manutenibilità;
- durabilità.

Non deve diventare un ostacolo burocratico alla ricerca e alla
pubblicazione.

---

## 62.1 Separazione tra licenza, privacy e autorizzazione

Una licenza non autorizza automaticamente:

- il trattamento di dati personali;
- la pubblicazione di informazioni riservate;
- l'accesso a un account o a uno storage;
- l'invio di comunicazioni;
- la redistribuzione di materiali acquistati;
- l'uso di una risorsa per finalità differenti da quelle consentite.

Quando più vincoli si applicano alla stessa risorsa, devono essere rispettati
congiuntamente.


## 62. Gerarchia

In caso di conflitto:

1. i documenti fondativi definiscono i principi superiori;
2. le decisioni approvate definiscono le scelte progettuali;
3. LICENSE-SPEC.md definisce il modello generale delle licenze;
4. le SPEC di dominio definiscono le esigenze specifiche;
5. le procedure operative implementano tali regole;
6. il codice e gli strumenti applicano quanto approvato.

La presente specifica non costituisce consulenza legale.
