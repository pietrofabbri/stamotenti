# StamoTenti — CITATION SPECIFICATION

## 1. Scopo

Questo documento definisce il modello delle citazioni utilizzate negli articoli di StamoTenti.

La citazione deve permettere di:

- identificare con precisione la fonte;
- risalire alla fonte originale;
- distinguere fonti differenti;
- riutilizzare la stessa fonte in più articoli;
- mantenere le informazioni bibliografiche in un unico luogo;
- supportare fonti scientifiche, filosofiche, storiche e documentali;
- supportare dataset e altri research object;
- indicare una posizione precisa all'interno della fonte quando necessario;
- permettere al lettore di approfondire autonomamente.

Il sistema deve rimanere semplice, leggibile e indipendente dal particolare formato grafico utilizzato nel sito.

---

## 2. Fonte e citazione

Fonte e citazione sono concetti distinti.

La fonte è l'entità bibliografica o documentale presente nel sistema.

La citazione è l'utilizzo di quella fonte all'interno di uno specifico articolo.

La stessa fonte può essere citata da molti articoli.

La stessa fonte può inoltre essere citata più volte nello stesso articolo.

---

## 3. Identità della fonte

Ogni fonte deve possedere un identificativo stabile.

L'identificativo deve essere indipendente:

- dal titolo;
- dall'URL;
- dalla lingua dell'articolo;
- dalla posizione della citazione.

Quando esiste un identificatore autorevole deve essere registrato.

Esempi:

- DOI;
- ISBN;
- PMID;
- identificativi di repository;
- identificativi di dataset;
- altri identificativi persistenti.

L'URL non costituisce automaticamente l'identità della fonte.

---

## 4. DOI

Il DOI della fonte originale deve essere conservato come identificativo della fonte originale.

StamoTenti non deve sostituire o duplicare il DOI della fonte.

Quando StamoTenti pubblica una propria risorsa su un repository come Zenodo, l'eventuale DOI assegnato a quella risorsa identifica la risorsa StamoTenti e non la fonte originale.

Devono quindi poter coesistere:

- DOI della fonte originale;
- DOI della risorsa derivata o pubblicata da StamoTenti.

Le due identità non devono essere confuse.

---

## 5. Una fonte, un record

Una fonte deve essere rappresentata una sola volta.

Se due articoli utilizzano la stessa fonte, devono riferirsi allo stesso record.

Prima di creare una nuova fonte devono essere verificati, quando disponibili:

- DOI;
- ISBN;
- PMID;
- altri identificativi;
- titolo;
- autore;
- anno;
- editore;
- URL.

In caso di dubbio sulla duplicazione, l'agente deve segnalare il possibile duplicato invece di crearne automaticamente uno nuovo.

---

## 6. Informazioni bibliografiche

Una fonte può contenere, quando disponibili:

- titolo;
- autori;
- traduttori;
- curatori;
- anno;
- data;
- rivista;
- libro;
- capitolo;
- editore;
- volume;
- numero;
- pagine;
- DOI;
- ISBN;
- PMID;
- URL;
- repository;
- identificativi esterni;
- tipo di documento;
- lingua;
- licenza;
- dataset associati;
- altre informazioni pertinenti.

Gli agenti non devono inventare informazioni bibliografiche.

Quando un dato non è verificabile deve essere lasciato assente o segnalato come incerto.

---

## 7. Tipologie di fonte

Il sistema deve poter rappresentare almeno:

- articolo scientifico;
- studio sperimentale;
- review;
- meta-analisi;
- libro;
- capitolo di libro;
- tesi;
- report;
- documento istituzionale;
- pagina web;
- documento storico;
- testo filosofico;
- opera antica;
- dataset;
- repository;
- software;
- altro research object pertinente.

Non deve essere creato un modello completamente diverso per ogni tipologia quando il modello generale della fonte è sufficiente.

---

## 8. Fonti online

Quando possibile devono essere privilegiate fonti provenienti da contesti autorevoli.

Esempi:

- editori scientifici;
- riviste accademiche;
- università;
- enti di ricerca;
- istituzioni pubbliche;
- biblioteche;
- archivi;
- repository scientifici;
- organizzazioni riconosciute;
- fonti primarie.

L'autorevolezza del dominio non è sufficiente da sola.

Devono essere considerati anche:

- autore;
- provenienza;
- data;
- metodologia;
- natura della fonte;
- rapporto con l'affermazione sostenuta.

---

## 9. Ricerca online

Gli agenti possono utilizzare la ricerca online per:

- identificare fonti;
- verificare metadata;
- verificare DOI;
- risolvere ambiguità;
- trovare versioni ufficiali;
- trovare dataset;
- verificare informazioni bibliografiche;
- confrontare più record.

La ricerca deve essere proporzionata al compito.

Gli agenti non devono effettuare ricerche indefinitamente.

Le attività di ricerca devono poter essere sottoposte a un budget massimo di risorse definito dal sistema operativo degli agenti.

Se il budget viene raggiunto senza una conclusione sufficientemente affidabile, l'agente deve fermarsi e segnalare il problema.

---

## 10. Fonti fornite manualmente

Il proprietario può fornire direttamente:

- una fonte;
- un DOI;
- un URL;
- una bibliografia;
- un PDF;
- un EPUB;
- un altro documento.

L'agente deve poter:

- identificare la fonte;
- verificare i metadata;
- individuare eventuali duplicati;
- classificarla;
- inserirla nel sistema;
- collegarla agli articoli pertinenti.

Una fonte fornita manualmente non deve essere scartata soltanto perché non proviene da uno dei domini normalmente utilizzati dagli agenti.

---

## 11. Fonti private

Alcune fonti possono essere legalmente accessibili al proprietario ma non redistribuibili pubblicamente.

Esempi:

- libri acquistati;
- EPUB acquistati;
- PDF acquistati;
- documenti ottenuti tramite abbonamenti personali;
- materiali soggetti a restrizioni di distribuzione.

Questi materiali possono essere utilizzati come fonti di lavoro senza essere pubblicati.

Il sistema deve distinguere tra:

- metadata pubblicabili;
- riferimento bibliografico;
- file pubblico;
- file privato.

Un file privato non deve essere copiato automaticamente in un repository pubblico.

Il riferimento bibliografico può comunque essere utilizzato negli articoli.

Quando il file privato è utile al lavoro degli agenti, il sistema può mantenere un riferimento locale al file senza pubblicarne il contenuto.

---

## 12. Archiviazione pubblica

Quando un documento può essere redistribuito legalmente, StamoTenti può conservarne una copia in un repository pubblico.

L'obiettivo è favorire nel tempo:

- accessibilità;
- preservazione;
- citabilità;
- riproducibilità;
- disponibilità dei materiali.

Zenodo è una possibile infrastruttura per questo scopo.

Zenodo associa ai record pubblicati un DOI e conserva metadata pubblicamente accessibili. :contentReference[oaicite:1]{index=1}

L'utilizzo di Zenodo non implica che ogni fonte debba essere caricata.

---

## 13. Zenodo e Communities

Le risorse pubblicate da StamoTenti su Zenodo possono essere organizzate attraverso Communities.

Le Communities devono essere utilizzate principalmente per migliorare:

- scoperta;
- organizzazione;
- curatela;
- accessibilità tematica.

Una risorsa può essere associata a più Communities senza creare necessariamente copie della stessa risorsa.

Zenodo supporta l'inclusione dei record in più Communities. :contentReference[oaicite:2]{index=2}

La classificazione tematica delle Communities deve essere definita dal progetto e non deve necessariamente coincidere con la tassonomia editoriale del sito.

---

## 14. Archiviazione per tipologia e tema

Quando utile, le risorse pubblicate possono essere organizzate secondo:

- tipologia;
- disciplina;
- argomento;
- tema;
- area editoriale.

La stessa risorsa può appartenere a più contesti tematici.

Non devono essere create copie fisiche della stessa risorsa soltanto per renderla visibile in più categorie.

La classificazione deve essere ottenuta attraverso metadata e Communities quando possibile.

---

## 15. File e diritti

Prima di archiviare pubblicamente un file, l'agente deve verificare che la redistribuzione sia appropriata.

In caso di dubbio:

- non pubblicare il file;
- conservare i metadata;
- conservare il riferimento alla fonte;
- segnalare il problema.

Non deve essere considerato sufficiente il semplice fatto che un file sia tecnicamente scaricabile.

La possibilità tecnica di scaricare una risorsa non implica automaticamente il diritto di redistribuirla.

---

## 16. Dataset

I dataset sono particolarmente importanti per StamoTenti.

Un dataset può essere:

- citato;
- associato a uno studio;
- associato a una pubblicazione;
- classificato per argomento;
- collegato a un repository;
- identificato tramite DOI o altro identificatore persistente.

Quando possibile, deve essere collegato alla pubblicazione o allo studio che ne descrive l'utilizzo.

I dataset pubblicabili possono essere archiviati in repository appropriati.

---

## 17. Research object

Una risorsa digitale può essere trattata come research object quando possiede una rilevanza autonoma.

Esempi:

- dataset;
- software;
- materiali supplementari;
- raccolte di dati;
- archivi digitali.

Prima di introdurre una nuova entità tecnica deve essere verificato se il modello generale delle fonti è sufficiente.

---

## 18. Classificazione delle fonti

Le fonti devono poter essere classificate per argomento.

La classificazione serve a permettere agli agenti di individuare più facilmente fonti pertinenti durante la preparazione di nuovi articoli.

La classificazione può utilizzare:

- macroarea;
- sotto-area;
- temi;
- disciplina;
- tipologia;
- argomento specifico.

La classificazione non modifica l'identità bibliografica della fonte.

Gli agenti possono proporre una classificazione.

La modifica del vocabolario o della struttura tassonomica deve rispettare le regole editoriali del progetto.

---

## 19. Autorevolezza e pertinenza

Autorevolezza e pertinenza sono proprietà differenti.

Una fonte deve essere valutata considerando separatamente:

1. autorevolezza;
2. qualità metodologica;
3. pertinenza;
4. attualità quando rilevante;
5. natura primaria o secondaria;
6. adeguatezza rispetto all'affermazione sostenuta.

Una fonte autorevole ma non pertinente non deve essere utilizzata soltanto per aumentare il numero delle citazioni.

---

## 20. Citazione nel testo

Una citazione deve permettere al lettore di comprendere che una determinata affermazione, dato, interpretazione o passaggio è collegato a una fonte.

Il formato visuale può essere:

- autore-data;
- numerico;
- nota;
- altro formato appropriato.

Il formato definitivo sarà deciso dal sistema di rendering.

Il modello interno della citazione deve rimanere indipendente dal formato visualizzato.

---

## 21. Localizzazione della citazione

Una citazione può riferirsi all'intera fonte oppure a una posizione precisa.

Il modello deve poter rappresentare, quando pertinente:

- pagina;
- intervallo di pagine;
- capitolo;
- sezione;
- paragrafo;
- figura;
- tabella;
- timestamp;
- verso;
- strofa;
- canto;
- sutra;
- sloka;
- altra unità testuale pertinente.

La posizione appartiene alla citazione e non necessariamente alla fonte generale.

Il sistema non deve richiedere una struttura filologica complessa finché i casi reali non la rendono necessaria.

---

## 22. Opere antiche

Le opere antiche devono poter essere citate anche quando:

- l'autore è storico;
- esistono più edizioni;
- esistono più traduzioni;
- esiste una lingua originale;
- la fonte utilizzata è una specifica edizione moderna.

Quando necessario deve essere possibile distinguere:

- opera;
- edizione;
- traduzione;
- traduttore;
- curatore;
- posizione nel testo;
- identificativi dell'edizione.

---

## 23. Traduzioni

Una traduzione della fonte non deve essere confusa con la fonte originale.

Quando una specifica traduzione viene utilizzata, deve essere possibile identificarla.

Il traduttore può essere rappresentato come autore associato alla fonte secondo AUTHOR-SPEC.md.

Il traduttore non deve necessariamente essere rappresentato attraverso un sistema tecnico separato di ruoli.

---

## 24. Citazioni testuali

Una citazione testuale deve essere distinta da una parafrasi.

Quando viene riportato testo letterale deve essere possibile identificare:

- fonte;
- autore;
- traduttore quando pertinente;
- lingua originale;
- posizione nella fonte;
- eventuale edizione utilizzata.

Le citazioni testuali devono rispettare le norme applicabili sul copyright.

---

## 25. Lingua della fonte

La lingua dell'articolo non modifica la lingua originale della fonte.

Un articolo italiano può citare fonti:

- italiane;
- inglesi;
- greche;
- latine;
- sanscrite;
- pali;
- tibetane;
- o appartenenti ad altre lingue.

Una traduzione può essere mostrata al lettore quando utile senza sostituire automaticamente il testo o il dato originale della fonte.

---

## 26. Fonti senza DOI

Non tutte le fonti possiedono un DOI.

L'assenza di DOI non rende una fonte inutilizzabile.

Possono essere utilizzati, quando appropriati:

- ISBN;
- URL;
- PMID;
- identificativi di catalogo;
- handle;
- repository ID;
- altri identificatori stabili.

Le fonti prive di identificatori persistenti devono comunque poter essere rappresentate.

---

## 27. URL

Quando una fonte dispone di un URL ufficiale, questo deve essere registrato.

Quando possibile devono essere privilegiati URL:

- ufficiali;
- stabili;
- istituzionali;
- del publisher;
- del repository;
- del DOI resolver.

L'URL è un dato di accesso alla fonte e non necessariamente la sua identità.

---

## 28. Citazioni multiple

Una singola affermazione può essere sostenuta da più fonti.

Il sistema deve poter associare più fonti alla stessa citazione.

Una fonte può inoltre essere citata più volte nello stesso articolo.

---

## 29. Bibliografia finale

Un articolo può mostrare una bibliografia finale.

Quando possibile la bibliografia deve essere generata automaticamente dalle fonti effettivamente utilizzate.

Non devono essere mantenute manualmente copie delle stesse informazioni bibliografiche nel testo e nella bibliografia.

---

## 30. Ordine della bibliografia

L'ordine della bibliografia deve essere determinato dal sistema di rendering o dallo stile bibliografico scelto.

Il contenuto editoriale non deve dipendere dalla numerazione manuale delle fonti.

Se una fonte viene aggiunta o rimossa, la numerazione eventualmente visualizzata deve poter essere rigenerata automaticamente.

---

## 31. Stile bibliografico

Il progetto può utilizzare uno stile bibliografico appropriato alla natura degli articoli.

La scelta deve tenere conto di:

- leggibilità;
- rigore accademico;
- compatibilità con le tipologie di fonte;
- leggibilità nella parte divulgativa;
- esigenze della parte accademica.

Lo stile visuale non deve modificare il modello interno delle fonti.

---

## 32. Collegamenti

Quando appropriato, una citazione può collegarsi:

- alla scheda della fonte;
- al DOI;
- alla pagina ufficiale;
- al repository;
- al dataset;
- ad altri identificativi pertinenti.

Il collegamento deve favorire l'accesso alla fonte originale o alla risorsa pubblicamente disponibile.

---

## 33. Relazioni tra fonti

Il sistema deve poter rappresentare relazioni semplici tra fonti quando utili.

Esempi:

- studio e dataset associato;
- pubblicazione e materiale supplementare;
- opera originale e traduzione;
- opera e specifica edizione;
- dataset e software utilizzato;
- articolo e preprint.

Non deve essere introdotto un grafo bibliografico complesso senza una necessità reale.

---

## 34. Provenienza dei metadata

Quando possibile, i metadata bibliografici devono essere verificabili.

L'agente dovrebbe poter distinguere tra:

- informazione direttamente verificata;
- informazione ottenuta da metadata autorevoli;
- informazione ottenuta da una fonte secondaria;
- informazione non ancora verificata.

Non devono essere presentate come certe informazioni che non sono state adeguatamente verificate.

---

## 35. Fonti nella parte divulgativa

La parte divulgativa deve essere rigorosa senza trasformarsi necessariamente in una sequenza di riferimenti bibliografici.

Le citazioni devono essere utilizzate quando servono a:

- sostenere un'affermazione;
- permettere una verifica;
- approfondire;
- indirizzare verso la letteratura.

Il numero di citazioni non costituisce di per sé una misura della qualità dell'articolo.

---

## 36. Fonti nella parte accademica

La parte accademica deve poter offrire un accesso più approfondito alla letteratura.

Quando pertinente può includere:

- studi originali;
- review;
- meta-analisi;
- dataset;
- lavori fondamentali;
- lavori recenti;
- fonti primarie;
- controversie metodologiche.

L'obiettivo è permettere al lettore interessato di entrare direttamente nella letteratura.

---

## 37. Agenti

Gli agenti possono:

- cercare fonti;
- verificare metadata;
- identificare duplicati;
- classificare fonti;
- proporre fonti;
- inserire fonti fornite dal proprietario;
- associare fonti agli articoli;
- individuare citazioni mancanti;
- controllare la coerenza bibliografica;
- verificare DOI e altri identificativi;
- proporre materiali pubblicabili;
- proporre l'archiviazione di materiali in repository.

Gli agenti non devono:

- inventare dati bibliografici;
- creare duplicati deliberatamente;
- sostituire una fonte con un'altra senza motivo;
- eliminare una fonte utilizzata senza motivazione;
- pubblicare file privati o non redistribuibili;
- considerare automaticamente autorevole una fonte soltanto perché trovata online.

---

## 38. Approvazione

Le fonti o le operazioni bibliografiche possono richiedere approvazione umana secondo il workflow generale del progetto.

Il sistema deve permettere al proprietario di:

- approvare;
- rifiutare;
- correggere;
- sostituire;
- aggiungere manualmente;
- modificare.

L'automazione non deve impedire l'intervento manuale.

---

## 39. Budget delle operazioni bibliografiche

Le operazioni bibliografiche devono poter essere soggette a un budget massimo di risorse.

Il budget può dipendere:

- dal modello utilizzato;
- dal tipo di task;
- dalla complessità della fonte;
- dal numero di fonti;
- dalla quantità di ricerca necessaria.

Il raggiungimento del budget deve produrre un arresto controllato o una richiesta di intervento.

Non deve essere consentita una ricerca indefinita che produca costi inutili.

I valori numerici dei budget saranno definiti nella configurazione operativa degli agenti e non in questa specifica.

---

## 40. Libertà manuale

Il proprietario deve poter modificare direttamente i dati bibliografici e le citazioni.

Deve essere sempre possibile:

- aggiungere una fonte;
- modificare una fonte;
- correggere una citazione;
- modificare una posizione;
- correggere un autore;
- aggiungere un identificativo;
- aggiungere un dataset;
- sostituire una fonte;
- indicare manualmente una fonte trovata autonomamente.

Gli agenti devono assistere il lavoro editoriale senza creare dipendenza dal sistema automatico.

---

## 41. Implementazione

La rappresentazione tecnica delle citazioni deve essere scelta dopo aver definito il modello editoriale.

Quando possibile devono essere preferiti:

- Markdown;
- front matter;
- dati strutturati semplici;
- Hugo;
- template;
- render hook;
- strumenti bibliografici standard.

Non deve essere introdotto un motore bibliografico complesso soltanto per ottenere funzionalità che possono essere implementate semplicemente.

---

## 42. Semplicità

Il sistema non deve introdurre prematuramente:

- database bibliografici complessi;
- ontologie;
- grafi semantici;
- workflow manuali per ogni citazione;
- duplicazioni dei metadata;
- sistemi proprietari quando una soluzione standard è sufficiente.

La complessità può essere introdotta successivamente quando la crescita reale del progetto la giustificherà.

---

## 43. Gerarchia delle specifiche

In caso di conflitto:

1. TO-BE.md definisce la visione e i vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. SOURCE-SPEC.md definisce il modello delle fonti;
4. CITATION-SPEC.md definisce l'utilizzo delle fonti negli articoli;
5. ARTICLE-SPEC.md definisce il comportamento editoriale degli articoli;
6. le specifiche operative definiscono workflow e automazioni;
7. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
