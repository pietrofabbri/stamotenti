# StamoTenti — SOURCE SPECIFICATION

## 1. Scopo

Questo documento definisce come StamoTenti gestisce le fonti utilizzate negli articoli.

Le fonti costituiscono una parte fondamentale del rigore editoriale del progetto.

Il sistema deve permettere di:

- identificare correttamente le opere utilizzate;
- evitare duplicazioni;
- conservare i dati bibliografici disponibili;
- collegare le fonti agli articoli che le utilizzano;
- distinguere fonti scientifiche, accademiche, storiche, filosofiche, divulgative e web;
- valorizzare i dataset come risorse informative autonome;
- rendere facilmente individuabili le versioni legalmente accessibili delle fonti;
- classificare le fonti per argomento;
- permettere agli agenti di individuare rapidamente le fonti pertinenti a un nuovo articolo;
- mantenere il sistema leggibile e sostenibile nel tempo.

La gestione delle citazioni all'interno degli articoli è definita separatamente in CITATION-SPEC.md.

---

## 2. Principio fondamentale

Una fonte deve essere definita una sola volta.

Gli articoli non devono contenere copie indipendenti dei dati bibliografici di una fonte quando questa è già presente nel sistema.

L'articolo deve riferirsi all'identificativo della fonte.

Una stessa fonte può essere utilizzata da un numero indefinito di articoli.

Questo principio evita:

- duplicazioni;
- errori bibliografici;
- informazioni divergenti;
- aggiornamenti ripetuti;
- aumento inutile della manutenzione.

---

## 3. Identità della fonte

Ogni fonte deve possedere un identificativo stabile.

L'identificativo deve essere:

- univoco;
- leggibile;
- stabile nel tempo;
- coerente con le altre fonti;
- indipendente dal titolo visualizzato.

L'identificativo non deve essere modificato senza una ragione concreta.

La modifica dell'identificativo di una fonte può rompere i riferimenti presenti negli articoli e deve quindi essere considerata una modifica strutturale.

---

## 4. Tipi di fonte

Il sistema deve supportare almeno le seguenti categorie:

- paper;
- book;
- book-chapter;
- thesis;
- report;
- web;
- dataset;
- conference;
- other.

La categoria deve descrivere il tipo reale della risorsa.

Gli agenti non devono scegliere una categoria soltanto in base alla forma dell'URL.

Quando una risorsa non rientra chiaramente nelle categorie esistenti, l'agente deve segnalarlo invece di creare autonomamente una nuova categoria.

L'insieme definitivo dei tipi può essere esteso con una decisione editoriale.

---

## 5. Informazioni fondamentali

Ogni fonte deve contenere almeno:

- id;
- type;
- title.

Quando disponibili e verificabili, possono essere presenti:

- authors;
- year;
- journal;
- volume;
- issue;
- pages;
- publisher;
- edition;
- DOI;
- ISBN;
- URL;
- file;
- access date;
- abstract;
- description;
- license;
- access status;
- repository;
- dataset identifier;
- other bibliographic metadata pertinenti.

I campi devono essere utilizzati soltanto quando rappresentano informazioni reali della fonte.

Non è necessario compilare artificialmente campi non disponibili.

---

## 6. Accuratezza bibliografica

Gli agenti non devono inventare dati bibliografici.

In particolare non devono inventare:

- autori;
- date;
- DOI;
- ISBN;
- titoli;
- riviste;
- numeri di volume;
- numeri di fascicolo;
- pagine;
- URL;
- editori;
- file;
- identificativi di dataset.

Quando un'informazione non può essere verificata, deve essere omessa oppure segnalata come informazione da verificare.

L'assenza di un dato è preferibile a un dato inventato.

---

## 7. DOI

Quando una fonte possiede un DOI verificabile, il DOI deve essere conservato.

Il DOI deve essere trattato come identificativo bibliografico della fonte e non come semplice URL.

Non deve essere creato o ricostruito per supposizione.

Se esistono più riferimenti apparentemente diversi alla stessa pubblicazione e uno di essi contiene un DOI verificato, il DOI può essere utilizzato per aiutare a determinare l'identità della fonte.

---

## 8. ISBN

Quando una fonte libraria possiede un ISBN verificabile, questo può essere conservato.

L'ISBN non deve essere inventato.

Edizioni differenti dello stesso libro possono avere ISBN differenti.

Una differenza di ISBN non implica automaticamente che si tratti di opere differenti.

Quando l'edizione specifica è rilevante per l'articolo, l'edizione deve essere rappresentata correttamente.

---

## 9. URL e autorevolezza

Le fonti web devono essere valutate non soltanto in base all'esistenza o alla raggiungibilità dell'URL, ma anche in base al contesto nel quale l'informazione viene pubblicata.

Quando pertinenti, devono essere preferite fonti provenienti da:

- istituzioni pubbliche;
- università;
- enti di ricerca;
- riviste scientifiche;
- editori accademici;
- organizzazioni professionali riconosciute;
- istituzioni culturali;
- organizzazioni autorevoli nel proprio ambito;
- studiosi qualificati;
- progetti di ricerca riconosciuti;
- repository accademici o istituzionali.

Le fonti divulgative qualificate possono essere utilizzate quando appropriate.

Le fonti web generiche devono essere utilizzate con maggiore cautela.

Non deve essere introdotta una whitelist rigida di domini: l'autorevolezza deve essere valutata in relazione alla fonte, al contesto e all'affermazione sostenuta.

L'URL deve essere verificato quando possibile.

Non devono essere utilizzati URL temporanei, tracciati o inutilmente dipendenti da parametri di navigazione quando esiste un riferimento più stabile.

Per le pubblicazioni accademiche deve essere preferito, quando disponibile, un identificativo bibliografico stabile come il DOI.

Per le fonti esclusivamente web l'URL costituisce normalmente un'informazione essenziale.

---

## 10. Accessibilità delle fonti

StamoTenti deve favorire l'accesso gratuito e legale alle fonti quando questo è disponibile.

Quando esistono più versioni legalmente accessibili di una stessa fonte, deve essere preferita una versione stabile e autorevole.

Possono essere utilizzati:

- versioni open access;
- repository istituzionali;
- repository accademici;
- archivi riconosciuti;
- pagine ufficiali degli autori o delle istituzioni;
- altre risorse legalmente accessibili.

La scheda della fonte può indicare lo stato di accesso.

Gli stati possono comprendere:

- open;
- repository;
- publisher;
- restricted;
- unknown.

L'accessibilità della fonte deve essere distinta dalla sua qualità scientifica o accademica.

Una fonte accessibile gratuitamente non è per questo automaticamente autorevole.

Una fonte autorevole non deve essere esclusa soltanto perché sottoposta a restrizioni di accesso.

StamoTenti non deve aggirare paywall, licenze, DRM, restrizioni di accesso o copyright.

---

## 11. File locali

Una fonte può avere associato un file locale, per esempio un PDF.

Il file deve esistere realmente nel progetto.

Il riferimento al file non deve puntare a una risorsa inesistente.

I file devono essere conservati soltanto quando il loro utilizzo e la loro redistribuzione sono compatibili con la relativa licenza e con le regole del progetto.

La presenza di un file locale non sostituisce necessariamente i dati bibliografici della fonte.

Il progetto non deve diventare automaticamente un archivio locale di tutte le pubblicazioni utilizzate.

---

## 12. Repository esterni e Zenodo

Quando sia utile conservare e distribuire legalmente un materiale, StamoTenti può utilizzare repository esterni appropriati.

Zenodo costituisce una possibile infrastruttura preferenziale per:

- dataset;
- materiali open access;
- documentazione;
- dati associati agli articoli;
- materiali prodotti dal progetto;
- altri oggetti digitali che richiedano conservazione e identificazione persistente.

Zenodo assegna DOI ai record pubblicati e supporta il versionamento dei materiali. Questo lo rende particolarmente adatto alla conservazione di dataset e altri oggetti di ricerca. 

L'utilizzo di Zenodo non deve però diventare una dipendenza necessaria per il funzionamento del sito.

StamoTenti deve poter funzionare anche nel caso in cui venga utilizzato un repository differente.

Quando viene utilizzato Zenodo, la relativa scheda deve conservare il DOI e gli eventuali identificativi della risorsa originale.

Non deve essere creato un nuovo DOI per una pubblicazione già dotata di un DOI proprio soltanto perché viene collegata o depositata in un repository.

---

## 13. Dataset

I dataset costituiscono una categoria di fonte di primo livello.

Un dataset può essere:

- associato a una pubblicazione scientifica;
- indipendente da una pubblicazione;
- prodotto da un'istituzione;
- prodotto da un progetto di ricerca;
- longitudinale;
- comportamentale;
- neuroscientifico;
- epidemiologico;
- sociologico;
- educativo;
- ambientale;
- storico;
- di altra natura pertinente al progetto.

La scheda di un dataset deve conservare, quando disponibili:

- identificativo;
- titolo;
- creatori;
- anno;
- descrizione;
- DOI;
- URL;
- repository;
- licenza;
- stato di accesso;
- versione;
- relazione con eventuali pubblicazioni associate.

Un dataset deve poter essere collegato agli articoli che lo utilizzano o lo discutono.

Quando un dataset possiede una propria identità bibliografica, deve essere trattato come risorsa distinta dalla pubblicazione che ne descrive i risultati.

---

## 14. Versioni delle fonti e dei dataset

Quando una fonte o un dataset possiede versioni differenti, la versione pertinente deve essere rappresentata quando è rilevante per la riproducibilità o per l'interpretazione dell'articolo.

Una versione aggiornata non deve essere considerata automaticamente identica a una versione precedente.

Per i dataset, in particolare, deve essere possibile identificare la versione utilizzata quando questa è disponibile.

Quando un repository assegna identificativi persistenti distinti alle versioni, devono essere conservati gli identificativi pertinenti.

---

## 15. Classificazione per argomento

Ogni fonte approvata può essere classificata per argomento.

La classificazione serve a permettere agli agenti di individuare rapidamente le fonti pertinenti a un articolo senza dover analizzare l'intero corpus bibliografico.

Gli argomenti devono utilizzare, quando possibile, il vocabolario editoriale controllato del progetto.

La classificazione può comprendere più argomenti.

Una fonte può quindi essere associata, per esempio, a:

- attenzione;
- mind-wandering;
- metacognizione;
- meditazione;
- stress;
- regolazione fisiologica.

La classificazione deve descrivere ciò che la fonte tratta realmente.

Gli agenti non devono assegnare argomenti soltanto sulla base del titolo.

Quando una fonte richiede un argomento non presente nel vocabolario controllato, l'agente deve segnalarlo come proposta senza modificare autonomamente il vocabolario.

---

## 16. Classificazione e qualità della fonte

La classificazione tematica non equivale a una valutazione di qualità.

Una fonte può essere:

- altamente pertinente ma metodologicamente debole;
- metodologicamente forte ma solo parzialmente pertinente;
- autorevole ma non direttamente utile a una determinata domanda;
- utile come contesto ma non sufficiente per sostenere una specifica affermazione.

Le informazioni relative a pertinenza e qualità devono quindi rimanere concettualmente distinte.

---

## 17. Fonti candidate

Una fonte individuata automaticamente non diventa automaticamente una fonte editoriale approvata.

Il sistema può prevedere un'area di fonti candidate nella quale inserire risorse ancora sottoposte a verifica.

Una fonte candidata può essere:

- identificata;
- deduplicata;
- schedata;
- classificata;
- valutata;
- proposta per l'approvazione.

Finché non viene approvata, una fonte candidata non deve essere considerata parte del corpus editoriale definitivo utilizzabile per la produzione degli articoli.

---

## 18. Approvazione umana

L'approvazione finale delle nuove fonti appartiene al proprietario del progetto, salvo delega esplicita.

Gli agenti possono preparare una scheda completa e proporre una fonte.

Non devono trasformare autonomamente una fonte candidata in fonte approvata quando il processo richiede una revisione umana.

Il sistema deve poter distinguere almeno concettualmente tra:

- candidate;
- approved;
- rejected.

La modalità tecnica con cui questi stati vengono implementati può evolvere nel tempo.

---

## 19. Agente bibliografico

Il progetto può utilizzare un agente specializzato nella gestione delle fonti.

Il suo compito può comprendere:

1. identificazione della fonte;
2. ricerca dei dati bibliografici;
3. verifica degli identificativi;
4. ricerca di duplicati;
5. classificazione del tipo;
6. classificazione per argomento;
7. identificazione di versioni open access;
8. identificazione di repository;
9. identificazione di eventuali dataset associati;
10. preparazione della scheda;
11. segnalazione delle incertezze;
12. preparazione della fonte per la revisione umana.

L'agente non deve inventare dati mancanti.

L'agente non deve approvare autonomamente una fonte quando è richiesta l'approvazione umana.

---

## 20. Pipeline delle fonti

Il sistema può adottare la seguente pipeline:

ricerca
→ identificazione
→ deduplicazione
→ scheda bibliografica
→ classificazione
→ verifica accessibilità
→ revisione umana
→ approvazione oppure scarto

L'automazione può essere introdotta progressivamente.

La pipeline inizialmente può essere eseguita anche manualmente o semi-automaticamente.

Non deve essere introdotto un sistema automatico complesso finché il volume delle fonti non ne giustifica l'utilità.

---

## 21. Sandbox delle fonti

Il progetto può prevedere una sandbox automatica o semi-automatica per le fonti candidate.

La sandbox deve permettere di separare:

- fonti individuate dagli agenti;
- fonti verificate;
- fonti approvate;
- fonti scartate.

La sandbox non deve essere considerata parte del corpus bibliografico definitivo.

La sua implementazione può rimanere semplice nelle prime fasi del progetto e può essere automatizzata successivamente quando il volume delle fonti lo renda utile.

---

## 22. Fonti scientifiche e accademiche

Quando un articolo presenta affermazioni scientifiche o accademiche, devono essere utilizzate fonti adeguate alla natura dell'affermazione.

Quando disponibili e pertinenti, devono essere considerate:

- studi originali;
- review;
- systematic review;
- meta-analisi;
- libri accademici;
- pubblicazioni istituzionali;
- fonti primarie storiche o filosofiche;
- dataset e repository associati alla ricerca.

La fonte più autorevole disponibile non deve essere scelta automaticamente se non è pertinente alla specifica affermazione.

La qualità di una fonte deve essere valutata anche in relazione alla domanda che si sta cercando di sostenere.

---

## 23. Fonti primarie e secondarie

Quando è rilevante, l'agente deve distinguere tra:

- fonte primaria;
- fonte secondaria;
- fonte terziaria.

Una fonte secondaria non deve essere presentata come se fosse la fonte primaria dell'informazione.

Quando una fonte primaria è facilmente verificabile e costituisce il riferimento appropriato, deve essere preferita quando possibile.

---

## 24. Fonti divulgative e web

Le fonti web possono essere utilizzate quando sono pertinenti e sufficientemente affidabili per l'affermazione sostenuta.

Devono essere valutate considerando:

- autorevolezza;
- autore;
- istituzione responsabile;
- data;
- qualità editoriale;
- stabilità della risorsa;
- relazione con l'affermazione sostenuta.

Una pagina web non deve essere utilizzata come sostituto automatico di una fonte primaria o accademica quando quest'ultima è necessaria e disponibile.

Le fonti web possono tuttavia essere appropriate per:

- informazioni istituzionali;
- documentazione;
- dati aggiornati;
- comunicazioni ufficiali;
- risorse divulgative qualificate;
- materiale non disponibile in forma accademica.

---

## 25. Fonti storiche e filosofiche

Per gli articoli di filosofia e storia devono essere considerate, quando pertinenti:

- testi originali;
- edizioni critiche;
- traduzioni autorevoli;
- studi accademici;
- monografie;
- fonti storiche affidabili.

Una fonte secondaria non deve essere utilizzata per attribuire direttamente a un autore un'affermazione quando il testo primario è disponibile e rilevante.

Le traduzioni devono essere considerate come opere specifiche quando l'edizione o il traduttore sono rilevanti.

---

## 26. Fonti relative alle pratiche contemplative

Le pratiche contemplative possono essere documentate attraverso fonti appartenenti a discipline differenti.

Gli articoli possono utilizzare:

- ricerca scientifica;
- testi filosofici;
- fonti storiche;
- testi tradizionali;
- studi antropologici;
- studi sociologici;
- fonti cliniche;
- fonti educative.

La presenza di una fonte tradizionale o filosofica non deve essere interpretata come prova scientifica.

La presenza di uno studio scientifico non deve essere utilizzata per confermare automaticamente un'interpretazione filosofica o spirituale.

La natura della fonte deve rimanere esplicita.

---

## 27. Fonti e livello dell'articolo

La parte divulgativa e la parte tecnica dello stesso articolo possono utilizzare le stesse fonti.

La parte tecnica può richiedere fonti più specialistiche o ulteriori riferimenti.

La bibliografia deve sostenere effettivamente il contenuto dell'articolo e non deve essere separata artificialmente in una bibliografia "semplice" e una "accademica" se la stessa fonte serve entrambe.

---

## 28. Relazione con gli autori

Gli autori delle fonti devono utilizzare le entità autore definite dal sistema quando appropriato.

Una fonte può avere più autori.

Le informazioni sugli autori non devono essere replicate manualmente in ogni articolo.

La gestione delle identità, delle varianti bibliografiche e degli alias degli autori è definita in AUTHOR-SPEC.md.

---

## 29. Relazione con gli articoli

Un articolo può utilizzare una o più fonti.

Una fonte può essere utilizzata da uno o più articoli.

La relazione tra articolo e fonte deve essere rappresentata attraverso l'identificativo della fonte.

Non deve essere duplicata l'intera scheda bibliografica all'interno dell'articolo.

La modalità con cui il riferimento viene visualizzato nel testo è definita in CITATION-SPEC.md.

---

## 30. Fonti non sufficienti

L'esistenza di una fonte non implica automaticamente che essa sia sufficiente a sostenere una determinata affermazione.

Gli agenti devono valutare la relazione tra:

- affermazione;
- tipo di evidenza necessaria;
- qualità della fonte;
- pertinenza della fonte.

Una fonte deve essere utilizzata soltanto quando è effettivamente pertinente.

Non devono essere aggiunte fonti soltanto per aumentare artificialmente il numero dei riferimenti bibliografici.

---

## 31. Gerarchia delle evidenze

Quando appropriato, gli articoli devono preferire fonti che permettano di ricostruire direttamente l'evidenza.

In generale, quando pertinenti:

- studi originali e fonti primarie hanno maggiore valore per risultati specifici;
- review e meta-analisi sono utili per sintetizzare la letteratura;
- testi accademici sono utili per concetti e contesto;
- fonti istituzionali sono utili per informazioni ufficiali;
- fonti divulgative sono utili per spiegazioni e contesto;
- fonti web generiche devono essere utilizzate con maggiore cautela.

Questa non è una graduatoria assoluta.

La fonte appropriata dipende sempre dalla domanda e dall'affermazione.

---

## 32. Aggiornamento delle fonti

Le fonti non devono essere aggiornate automaticamente soltanto perché esistono nuove informazioni.

Un aggiornamento deve essere motivato da una necessità reale.

Per le fonti web particolarmente soggette a cambiamento, può essere utile conservare la data di accesso quando appropriato.

Per le pubblicazioni scientifiche e accademiche, i dati bibliografici fondamentali devono rimanere quelli relativi all'opera citata.

Per dataset e risorse versionate deve essere conservata, quando disponibile, la versione effettivamente utilizzata.

---

## 33. Architettura tecnica

Il sistema delle fonti deve utilizzare, quando sufficiente, i meccanismi nativi di Hugo e i dati strutturati locali del progetto.

La struttura deve rimanere semplice, leggibile e portabile.

Non devono essere introdotti database, servizi bibliografici obbligatori o sistemi esterni complessi quando una struttura basata su dati locali e identificativi stabili è sufficiente.

La possibilità di utilizzare repository esterni come Zenodo non modifica questo principio.

---

## 34. Efficienza per gli agenti

Il sistema delle fonti deve essere progettato anche per ridurre il consumo inutile di contesto e token.

Un agente che prepara un articolo non deve analizzare l'intero corpus bibliografico quando è possibile selezionare un sottoinsieme pertinente.

La classificazione per argomento deve permettere di filtrare preliminarmente le fonti.

Quando possibile, la selezione deve privilegiare:

- fonti approvate;
- fonti pertinenti;
- fonti di qualità adeguata;
- fonti primarie quando appropriate;
- fonti open access o legalmente accessibili quando disponibili;
- review e meta-analisi quando utili alla sintesi;
- dataset pertinenti.

La scheda bibliografica deve contenere informazioni sufficienti a effettuare una prima selezione senza dover leggere ogni fonte integralmente.

---

## 35. Responsabilità degli agenti

Prima di creare una fonte, l'agente deve:

1. verificare se esiste già;
2. verificare l'identità della risorsa;
3. raccogliere soltanto dati verificabili;
4. scegliere il tipo corretto;
5. utilizzare gli autori esistenti quando appropriato;
6. conservare gli identificativi stabili disponibili;
7. verificare l'eventuale accessibilità legale;
8. classificare la fonte per argomento;
9. evitare duplicati;
10. segnalare le incertezze.

Se non può verificare con sufficiente sicurezza l'identità o i dati bibliografici, deve fermarsi e segnalarlo.

Non deve inventare una fonte per completare un articolo.

---

## 36. Principio di trasparenza

Quando una fonte presenta limiti rilevanti, l'articolo deve poterli rappresentare correttamente.

La bibliografia non deve creare un'apparenza di certezza maggiore rispetto alla qualità effettiva delle evidenze.

La selezione delle fonti deve contribuire alla trasparenza del progetto.

---

## 37. Principio di semplicità

Il sistema delle fonti deve rimanere semplice.

Non devono essere introdotti prematuramente:

- database bibliografici complessi;
- sistemi automatici di deduplicazione opachi;
- metadati non utilizzati;
- classificazioni bibliografiche inutili;
- servizi esterni obbligatori;
- sistemi semantici complessi;

quando una struttura basata su dati locali, classificazione controllata e identificativi stabili è sufficiente.

Le automazioni devono essere introdotte quando riducono realmente il lavoro o aumentano la qualità.

---

## 38. Regola finale

Una fonte deve essere:

- reale;
- identificabile;
- verificabile;
- pertinente;
- non duplicata;
- classificata;
- riutilizzabile;
- legalmente accessibile quando viene distribuita.

Una fonte candidata deve essere distinguibile da una fonte approvata.

Quando uno di questi requisiti non può essere soddisfatto con sufficiente sicurezza, l'agente deve preferire segnalare il problema piuttosto che inventare o assumere informazioni.

La correttezza bibliografica ha priorità sulla velocità di completamento.
