# StamoTenti — SEO SPECIFICATION

## 1. Scopo

Questo documento definisce i principi e i requisiti SEO e GEO di StamoTenti.

L'obiettivo è rendere i contenuti:

- facilmente individuabili dai motori di ricerca;
- correttamente indicizzabili;
- semanticamente comprensibili;
- correttamente collegati nelle diverse lingue;
- facilmente citabili e verificabili;
- rappresentati con metadata coerenti;
- condivisibili correttamente;
- accessibili ai sistemi di ricerca e, quando appropriato, agli agenti.

La SEO e la GEO non devono modificare arbitrariamente il contenuto editoriale.

La qualità, l'originalità, l'affidabilità e l'utilità del contenuto rimangono prioritarie rispetto all'ottimizzazione.

---

## 2. Principio editoriale

StamoTenti non deve produrre contenuti esclusivamente per ottenere traffico dai motori di ricerca o citazioni da sistemi AI.

Le pratiche SEO/GEO devono migliorare:

- comprensione;
- reperibilità;
- navigazione;
- accessibilità;
- verificabilità;
- collegamento tra contenuti;
- capacità del contenuto di essere correttamente interpretato e citato.

Non devono introdurre:

- keyword stuffing;
- titoli artificiali;
- contenuti duplicati creati soltanto per il ranking;
- testo nascosto;
- informazioni false;
- pagine generate senza valore editoriale;
- menzioni artificiali;
- contenuti costruiti esclusivamente per manipolare sistemi AI.

Le indicazioni ufficiali di Google confermano che non sono richieste tecniche SEO speciali per comparire nelle funzionalità generative e che le fondamenta della SEO rimangono centrali.

---

## 3. Contenuto people-first

Il contenuto deve essere scritto innanzitutto per il lettore.

Il sito deve privilegiare:

- contenuti originali;
- approfondimento reale;
- fonti verificabili;
- ragionamento;
- chiarezza;
- competenza;
- valore aggiunto rispetto a contenuti già disponibili.

L'uso degli agenti non deve trasformare il sito in una raccolta di contenuti generici prodotti automaticamente.

---

## 4. Indicizzazione

Ogni contenuto pubblico deve poter essere classificato come:

- indicizzabile;
- non indicizzabile;
- indicizzabile con condizioni particolari.

La decisione deve dipendere dalla natura del contenuto e dalla sua destinazione.

Contenuti privati o non destinati al pubblico non devono essere esposti ai motori di ricerca.

---

## 5. URL

Gli URL devono essere:

- stabili;
- leggibili;
- prevedibili;
- coerenti;
- indipendenti da dettagli tecnici interni.

La modifica del titolo non deve necessariamente modificare l'identità del contenuto.

Quando un URL cambia, devono essere considerate strategie di redirect o alias appropriate.

---

## 6. Canonical

Ogni pagina indicizzabile dovrebbe avere un URL canonico chiaramente
determinabile.

Il canonical deve rappresentare la risorsa corrente della stessa versione
linguistica e non deve essere utilizzato per sostituire una traduzione con
un'altra.

Il canonical deve:

- riferirsi alla versione primaria della stessa risorsa;
- utilizzare un URL corretto;
- evitare ambiguità tra URL equivalenti;
- essere coerente con il dominio ufficiale;
- non puntare accidentalmente a una traduzione diversa.

Le diverse versioni linguistiche dello stesso contenuto non devono essere trattate come duplicati da risolvere con un unico canonical.

Ogni traduzione deve avere il proprio URL canonico.

---

## 7. Multilingua

StamoTenti deve trattare italiano e inglese come versioni linguistiche dello stesso contenuto quando rappresentano una traduzione.

Ogni versione linguistica deve avere:

- lingua corretta;
- URL corretto;
- metadata nella lingua appropriata;
- titolo nella lingua appropriata;
- descrizione nella lingua appropriata;
- dati strutturati coerenti.

La gestione tecnica del multilingua è definita in MULTILINGUAL-SPEC.md.

---

## 8. hreflang

Quando esistono versioni linguistiche dello stesso contenuto, il sistema deve
poter indicare le relative alternative linguistiche tramite `hreflang`.

I riferimenti devono:

- indicare URL reali;
- essere coerenti tra le versioni;
- usare codici linguistici validi;
- rappresentare versioni equivalenti dello stesso contenuto.

L'implementazione deve preferire i meccanismi nativi di Hugo quando sufficienti.

I riferimenti devono:

- essere reciproci quando appropriato;
- utilizzare URL corretti;
- utilizzare codici linguistici validi;
- riferirsi alla versione corrispondente dello stesso contenuto.

---

## 9. Lingua della pagina

La lingua della pagina deve essere esplicitamente rappresentata nel documento HTML.

Il valore deve essere coerente con la lingua effettiva del contenuto.

---

## 10. Titolo

Ogni pagina indicizzabile deve avere un titolo significativo.

Il titolo deve:

- descrivere il contenuto;
- essere comprensibile fuori dal contesto;
- evitare formulazioni artificiali;
- essere coerente con il contenuto editoriale;
- essere tradotto nella lingua della pagina.

Il titolo SEO può essere distinto dal titolo editoriale soltanto quando esiste una motivazione concreta.

---

## 11. Meta description

Le pagine pubbliche principali dovrebbero avere una descrizione sintetica.

La descrizione deve:

- riassumere realmente il contenuto;
- essere leggibile;
- essere specifica;
- essere coerente con la lingua;
- evitare keyword stuffing.

Un agente può proporre una descrizione.

Il sistema deve poter utilizzare anche una descrizione fornita manualmente.

---

## 12. Struttura dei titoli

La struttura dei titoli HTML deve riflettere la struttura reale del contenuto.

Devono essere evitati:

- livelli utilizzati soltanto per effetti grafici;
- salti arbitrari;
- titoli privi di contenuto;
- titoli duplicati senza motivo.

La struttura semantica deve essere coerente con ARTICLE-SPEC.md.

---

## 13. Structured data

StamoTenti deve utilizzare dati strutturati quando questi migliorano la comprensione dei contenuti e/o l'idoneità a funzionalità dei motori di ricerca.

Il formato preferenziale è JSON-LD.

I dati strutturati devono descrivere informazioni effettivamente presenti nella pagina.

Non devono essere utilizzati per dichiarare informazioni che il contenuto non supporta.

Non deve essere creato uno schema speciale soltanto per la GEO.

---

## 14. JSON-LD

Il JSON-LD deve essere generato automaticamente quando possibile.

La struttura deve poter rappresentare, quando appropriato:

- sito;
- organizzazione/progetto;
- articolo;
- autore;
- datazione tecnica della risorsa quando realmente necessaria;
- lingua;
- editore;
- URL;
- immagini;
- descrizione;
- relazioni con altre risorse;
- identificativi esterni.

La presenza di metadata tecnici non implica che tali informazioni debbano essere mostrate come parte del contenuto editoriale.

Gli articoli di StamoTenti non devono essere obbligati a mostrare una data di pubblicazione o modifica.

---

## 15. Identità di StamoTenti

Il sito deve possedere una rappresentazione coerente della propria identità.

Quando appropriato, il JSON-LD deve permettere di collegare:

StamoTenti
→ sito
→ articoli
→ autori
→ fonti
→ dataset
→ media.

Gli identificativi devono essere stabili.

La stessa entità non deve essere rappresentata con identificativi arbitrariamente differenti in punti diversi del sito.

---

## 16. Organization / WebSite

Il sito dovrebbe poter esporre dati strutturati relativi a:

- `WebSite`;
- organizzazione o progetto responsabile;
- eventuali profili ufficiali;
- URL ufficiali;
- identificativi stabili.

Questi dati devono essere coerenti con le informazioni realmente disponibili sul sito.

---

## 17. Autore nei dati strutturati

Quando un articolo ha un autore identificato, il JSON-LD deve poter collegare l'articolo alla relativa entità `Person` o altro tipo appropriato.

Le informazioni dell'autore devono essere derivate dall'entità autore quando possibile.

Non devono essere duplicate inutilmente negli articoli.

---

## 18. Fonti e citazioni

Le fonti utilizzate negli articoli possono essere rappresentate nei dati strutturati quando lo schema e il caso d'uso lo rendono appropriato.

Il JSON-LD non deve sostituire il sistema di citazioni.

La citazione visibile e il riferimento bibliografico rimangono determinati da CITATION-SPEC.md.

La possibilità di risalire alla fonte primaria deve essere preservata.

---

## 19. Citabilità

La struttura degli articoli deve favorire la possibilità che singole affermazioni vengano:

- comprese;
- verificate;
- collegate alle fonti;
- citate;
- ricondotte al contesto originale.

Quando appropriato, devono essere chiaramente distinguibili:

- affermazione;
- evidenza;
- fonte;
- interpretazione;
- eventuale controversia.

La citabilità non deve diventare una frammentazione artificiale dell'articolo.

Google non richiede di suddividere i contenuti in piccoli blocchi per favorire la ricerca generativa.

---

## 20. Struttura della prima parte dell'articolo

La prima parte dell'articolo deve essere accessibile a un lettore non specialista.

Dovrebbe permettere di comprendere rapidamente:

- il problema;
- la domanda;
- il fenomeno;
- le principali conclusioni o questioni;
- il significato dell'approfondimento successivo.

Può anticipare alcuni elementi della parte accademica.

La seconda parte può essere più tecnica e accademica.

La struttura è definita in ARTICLE-SPEC.md.

---

## 21. Originalità e valore aggiunto

Gli articoli devono offrire valore oltre la semplice ricomposizione di fonti esistenti.

Il valore aggiunto può derivare da:

- collegamenti originali;
- confronto tra fonti;
- sintesi;
- confutazione;
- interpretazione;
- contestualizzazione;
- analisi di dataset;
- ragionamento;
- individuazione di contraddizioni;
- collegamento tra discipline o temi.

Gli agenti possono assistere questo lavoro, ma non devono trasformarlo in produzione automatica indiscriminata.

---

## 22. Pluralità delle interpretazioni

Quando un tema presenta posizioni o interpretazioni divergenti, l'articolo può rappresentare:

- posizione A;
- evidenze a sostegno;
- posizione B;
- evidenze a sostegno;
- eventuali altre posizioni;
- valutazione argomentata dell'autore.

La presenza di pluralità non implica che tutte le posizioni abbiano lo stesso valore probatorio.

---

## 23. Freschezza e attualità

Quando un contenuto dipende da informazioni suscettibili di cambiamento, il sistema deve poter verificare se le informazioni utilizzate sono ancora attuali.

Gli agenti possono segnalare:

- informazioni obsolete;
- fonti sostituite;
- dataset aggiornati;
- cambiamenti normativi;
- modifiche tecniche;
- nuove evidenze.

Gli articoli non devono essere obbligati a mostrare date di pubblicazione o modifica.

Le informazioni temporali possono essere mantenute nei metadata tecnici quando servono al sistema.

---

## 24. Identificativi esterni

Quando un contenuto o una fonte possiede un identificativo stabile, questo può essere incluso nei metadata e nei dati strutturati quando appropriato.

Esempi:

- DOI;
- ISBN;
- ORCID;
- URL canonico;
- identificativi di dataset;
- identificativi di catalogo.

Gli identificativi devono essere verificati prima di essere pubblicati.

---

## 25. Breadcrumb

Le pagine possono utilizzare dati strutturati relativi alla navigazione gerarchica quando la struttura editoriale lo giustifica.

Il breadcrumb deve riflettere la struttura reale del sito.

Non deve creare gerarchie SEO artificiali.

---

## 26. Open Graph

Le pagine pubbliche dovrebbero fornire metadata Open Graph coerenti.

Quando appropriato devono essere definiti:

- titolo;
- descrizione;
- URL;
- tipo;
- immagine;
- lingua;
- sito.

I valori devono essere coerenti con la versione linguistica corrente.

---

## 27. Social metadata

I metadata destinati alla condivisione devono essere generati dai metadata del contenuto quando possibile.

Non devono richiedere una seconda copia manuale delle informazioni.

Eventuali immagini specifiche per la condivisione possono essere definite separatamente.

---

## 28. Immagini

Le immagini pubbliche devono avere metadata appropriati quando disponibili.

Il sistema dovrebbe poter gestire:

- testo alternativo;
- titolo;
- didascalia;
- autore;
- fonte;
- licenza.

Il testo alternativo deve descrivere l'informazione visiva rilevante.

Non deve essere utilizzato per inserire parole chiave artificiali.

---

## 29. Sitemap

Il sito pubblico deve generare una sitemap appropriata.

La sitemap deve includere soltanto risorse che devono essere individuabili dai crawler.

Non devono essere incluse automaticamente:

- risorse private;
- file non pubblicabili;
- contenuti esclusi dall'indicizzazione;
- URL tecnici privi di valore.

La sitemap deve essere coerente con la struttura multilingue.

---

## 30. Robots

Il sistema deve poter controllare quali risorse possono essere sottoposte a crawling e indicizzazione.

`robots.txt` e metadata `robots` devono essere utilizzati in modo coerente.

Il sistema non deve affidarsi a `robots.txt` come unico meccanismo di protezione per contenuti privati.

---

## 31. Contenuti privati

I contenuti privati devono essere esclusi dalla superficie pubblica del sito.

`noindex` e `robots.txt` non devono essere utilizzati come sostituti del
controllo degli accessi.

Un contenuto realmente privato deve essere protetto a livello di distribuzione
e storage secondo SECURITY-SPEC.md e MEDIA-SPEC.md.

Non devono essere considerati sufficienti:

- `noindex`;
- `robots.txt`;
- URL non linkati.

La protezione dei contenuti privati appartiene a SECURITY-SPEC.md e MEDIA-SPEC.md.

---

## 32. Pagine di tassonomia

Le pagine relative a temi e tassonomie possono essere indicizzate quando hanno valore editoriale reale.

Una pagina di tassonomia non deve essere indicizzata automaticamente soltanto perché Hugo la genera.

Il sistema deve poter distinguere tra:

- tassonomia utile al lettore;
- pagina tecnica;
- pagina vuota;
- pagina con contenuto insufficiente.

---

## 33. Temi multilingue

I temi visibili devono rispettare il sistema multilingue.

La stessa classificazione concettuale può avere:

- termine italiano;
- termine inglese;
- eventuali localizzazioni future.

Le traduzioni non devono creare tassonomie concettualmente differenti soltanto per differenze linguistiche.

La classificazione interna deve mantenere un'identità coerente.

---

## 34. Autori multilingue

Le informazioni pubbliche relative agli autori devono poter essere localizzate quando necessario.

Il nome proprio non deve essere tradotto arbitrariamente.

Titoli, descrizioni e biografie possono avere versioni linguistiche differenti.

---

## 35. Traduzioni automatiche

Gli articoli in inglese possono essere prodotti tramite agenti secondo MULTILINGUAL-SPEC.md.

La SEO della traduzione non deve richiedere una nuova approvazione per ogni singolo metadata tecnico.

Gli agenti devono poter generare automaticamente:

- title;
- description;
- URL;
- lingua;
- hreflang;
- JSON-LD;
- metadata social;

coerentemente con la traduzione.

---

## 36. Coerenza tra lingue

Quando un contenuto viene tradotto, i metadata devono rimanere semanticamente coerenti.

Non è necessario che:

- titolo;
- description;
- slug;
- testo;

siano traduzioni letterali.

Devono però riferirsi allo stesso contenuto editoriale.

---

## 37. Collegamenti interni

Il sito deve utilizzare collegamenti interni quando migliorano:

- navigazione;
- comprensione;
- scoperta di contenuti;
- collegamento tra argomenti;
- accesso alle fonti.

I collegamenti automatici devono essere utilizzati soltanto quando la pertinenza è sufficientemente alta.

---

## 38. Contenuti correlati

Il sistema può generare automaticamente contenuti correlati utilizzando:

- temi;
- area editoriale;
- fonti condivise;
- relazioni esplicite;
- similarità;
- altri segnali approvati.

La qualità dei collegamenti è più importante della quantità.

---

## 39. Pagine orfane

Il sistema dovrebbe poter individuare pagine pubbliche che non ricevono collegamenti interni sufficienti.

Un agente può segnalarle.

Non deve creare automaticamente collegamenti irrilevanti soltanto per eliminare la condizione di pagina orfana.

---

## 40. Redirect

Quando un contenuto cambia URL, deve essere preservata per quanto possibile la raggiungibilità del vecchio indirizzo.

Gli strumenti di Hugo relativi agli alias e ai redirect possono essere utilizzati quando appropriato.

I redirect devono evitare catene inutili.

---

## 41. Duplicazione

Il sistema deve evitare contenuti duplicati non necessari.

La duplicazione linguistica prevista dal progetto non costituisce di per sé un errore.

Le traduzioni devono essere collegate correttamente.

Le copie tecniche della stessa risorsa non devono generare automaticamente pagine pubbliche multiple.

---

## 42. Pagine generate automaticamente

Le pagine generate dal sistema devono essere sottoposte agli stessi criteri di qualità delle pagine scritte manualmente.

La generazione automatica non implica automaticamente valore SEO o GEO.

Una pagina automatica priva di valore può essere esclusa dall'indicizzazione.

---

## 43. Performance

La SEO deve tenere conto delle prestazioni del sito.

Devono essere monitorati, quando appropriato:

- tempi di caricamento;
- peso delle immagini;
- JavaScript;
- CSS;
- font;
- numero di richieste;
- dimensione delle pagine.

Le ottimizzazioni non devono compromettere leggibilità e accessibilità.

---

## 44. Accessibilità

L'accessibilità deve essere considerata parte della qualità complessiva del sito.

Devono essere rispettati, quando applicabili:

- struttura semantica;
- testo alternativo;
- contrasto;
- navigazione da tastiera;
- elementi interattivi comprensibili;
- titoli coerenti;
- lingua della pagina.

L'accessibilità non deve essere ridotta a una tecnica SEO.

---

## 45. Agent-friendliness

Il sito deve essere facilmente interpretabile anche da sistemi automatizzati
che utilizzano:

- DOM;
- testo;
- struttura semantica;
- accessibilità;
- collegamenti;
- metadata.

Le informazioni importanti devono essere disponibili in forma testuale quando appropriato.

Non devono essere nascoste esclusivamente dentro immagini, script o interfacce difficili da interpretare.

La compatibilità con agenti non richiede necessariamente file o markup
speciali.

La priorità deve rimanere la qualità del contenuto, la struttura semantica,
l'accessibilità, la chiarezza e la verificabilità.

---

## 46. Monitoraggio SEO

Il sistema può monitorare:

- pagine indicizzate;
- errori;
- pagine escluse;
- query rilevanti;
- traffico organico;
- click;
- impression;
- cambiamenti anomali;
- broken links;
- problemi tecnici;
- performance;
- visibilità internazionale.

Il monitoraggio deve essere proporzionato ai costi e alla disponibilità dei dati.

---

## 47. Monitoraggio GEO

Il sistema deve poter monitorare, quando i dati disponibili lo consentono:

- citazioni del sito nelle risposte AI;
- pagine citate;
- query o temi associati alle citazioni;
- andamento nel tempo;
- differenze tra lingue;
- differenze tra sistemi;
- contenuti frequentemente citati;
- contenuti indicizzati ma raramente citati.

Le metriche GEO non devono essere interpretate automaticamente come ranking.

Una citazione indica utilizzo come fonte, non necessariamente maggiore autorevolezza.

Bing Webmaster Tools dispone già di strumenti che mostrano citazioni, pagine citate e grounding queries nelle esperienze AI supportate. Google ha introdotto report dedicati alla visibilità nelle funzionalità generative di Search.

---

## 48. Agente di aggiornamento SEO/GEO

StamoTenti deve prevedere un ruolo incaricato di monitorare periodicamente:

- aggiornamenti dei motori di ricerca;
- documentazione ufficiale;
- modifiche a schema.org;
- nuove funzionalità SEO;
- nuove funzionalità GEO;
- nuovi strumenti di monitoraggio;
- cambiamenti nei sistemi di indicizzazione;
- nuove pratiche relative agli agenti;
- cambiamenti rilevanti nei principali motori di ricerca.

Il ruolo deve operare con una periodicità sostenibile.

Non deve modificare automaticamente il sito soltanto perché individua una novità.

Deve produrre report sintetici contenenti:

1. cosa è cambiato;
2. quanto è affidabile l'informazione;
3. se riguarda StamoTenti;
4. quale parte del progetto potrebbe essere interessata;
5. eventuale proposta di modifica;
6. beneficio atteso;
7. costo e complessità;
8. livello di urgenza.

Le fonti ufficiali devono essere privilegiate.

Le fonti secondarie possono essere utilizzate per scoprire novità o interpretazioni, ma devono essere distinguibili dalle fonti primarie.

---

## 49. Agente SEO/GEO e approvazioni

L'agente SEO/GEO può:

- analizzare;
- confrontare;
- proporre;
- testare quando possibile;
- produrre report.

Non deve modificare autonomamente le specifiche architetturali o il contenuto editoriale.

Le modifiche strutturali devono seguire WORKFLOW-SPEC.md.

Il proprietario deve poter approvare, rifiutare o ignorare una proposta.

---

## 50. Analisi originale

Un agente può assistere il proprietario nell'analisi dei contenuti
individuando:

- connessioni originali;
- fonti apparentemente rilevanti;
- argomentazioni da approfondire;
- possibili confutazioni;
- interpretazioni alternative;
- lacune bibliografiche;
- contraddizioni tra fonti.

L'agente non decide autonomamente quale articolo debba essere scritto.

La decisione editoriale rimane del proprietario.

---

## 51. Budget computazionale

Le attività automatiche ricorrenti devono avere, quando possibile, un budget computazionale predefinito.

Il budget può comprendere:

- token;
- tempo;
- numero di ricerche;
- numero di pagine analizzate;
- numero di chiamate a servizi esterni;
- costo stimato.

Il budget deve essere proporzionato al tipo di attività.

Esempi:

- classificazione semplice → budget basso;
- controllo bibliografico → budget medio;
- ricerca approfondita → budget alto;
- analisi esplicitamente richiesta dal proprietario → budget definito caso per caso.

Il limite è un default operativo, non un limite imposto al proprietario.

Il proprietario deve poter richiedere esplicitamente un'analisi più onerosa.

Se un'attività rischia di superare significativamente il proprio budget, l'agente deve preferibilmente:

- fermarsi;
- fornire il risultato parziale;
- oppure chiedere se procedere con un budget maggiore,

secondo le regole di autorizzazione applicabili.

---

## 52. Manualità

Il proprietario deve poter modificare manualmente:

Gli override manuali sono autorevoli finché non vengono deliberatamente
modificati.

Le automazioni non devono entrare in cicli di sovrascrittura di una scelta
manuale.

- titolo SEO;
- description;
- immagine;
- canonical;
- impostazioni di indicizzazione;
- metadata;
- eventuali dati strutturati specifici.

Le automazioni devono rispettare gli override manuali espliciti.

Un agente può segnalare un'incongruenza, ma non deve sovrascrivere silenziosamente una decisione manuale.

---

## 53. Principio di semplicità

La SEO/GEO deve utilizzare, quando possibile:

- funzionalità native di Hugo;
- metadata già presenti;
- template riutilizzabili;
- dati strutturati generati automaticamente;
- semplici controlli automatizzati.

Non deve essere creato un sistema SEO/GEO parallelo quando le funzionalità native sono sufficienti.

Non devono essere introdotti file o protocolli speciali soltanto perché vengono temporaneamente considerati "ottimizzati per AI".

---

## 54. Aggiornabilità

Le specifiche SEO/GEO devono poter evolvere con:

- cambiamenti dei motori di ricerca;
- nuove versioni di Hugo;
- nuovi standard;
- nuovi schemi schema.org;
- nuove esigenze editoriali;
- nuove forme di ricerca AI.

Il ruolo di monitoraggio SEO/GEO deve aiutare a individuare quando una parte di questa specifica è diventata obsoleta.

Non devono essere introdotte modifiche soltanto perché una tecnica è temporaneamente di moda.

---

## 55. Principio di veridicità

I dati strutturati devono rappresentare ciò che esiste realmente nella pagina.

Non devono essere utilizzati per:

- gonfiare artificialmente l'importanza del contenuto;
- dichiarare recensioni inesistenti;
- inventare autori;
- dichiarare informazioni false;
- aggiungere informazioni non verificabili;
- manipolare sistemi AI.

La SEO/GEO non può prevalere sull'integrità editoriale.

---

## 56. Fonti delle decisioni SEO/GEO

Quando un agente propone una modifica rilevante, deve distinguere tra:

- documentazione ufficiale;
- dati osservati;
- analisi sperimentale;
- fonti secondarie;
- ipotesi dell'agente.

Le raccomandazioni devono essere proporzionate alla qualità delle evidenze.

Una singola osservazione non deve essere trasformata automaticamente in una regola generale.

---

## 57. Sperimentazione

Quando una modifica SEO/GEO non è sufficientemente certa, può essere proposta come esperimento.

Un esperimento dovrebbe specificare:

- ipotesi;
- modifica;
- durata prevista;
- metrica osservata;
- criterio di successo;
- criterio di annullamento.

Gli esperimenti non devono modificare contemporaneamente troppe variabili quando ciò rende impossibile interpretarne il risultato.

---

## 58. Nessuna data editoriale obbligatoria

Gli articoli di StamoTenti non devono essere obbligati a mostrare:

- data di pubblicazione;
- data di modifica;
- cronologia delle versioni.

Le informazioni temporali possono essere mantenute nei metadata tecnici quando servono a:

- monitoraggio;
- indicizzazione;
- gestione interna;
- verifica della freschezza;
- audit.

La loro eventuale visualizzazione al lettore è una decisione editoriale separata.

---

## 59. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi del progetto definiscono visione e vincoli fondamentali;
2. CONTENT-MODEL.md definisce entità e relazioni;
3. ARTICLE-SPEC.md definisce il contenuto degli articoli;
4. MULTILINGUAL-SPEC.md definisce la gestione delle lingue;
5. CITATION-SPEC.md definisce le citazioni;
6. MEDIA-SPEC.md definisce media e loro disponibilità;
7. SEO-SPEC.md definisce requisiti SEO e GEO;
8. WORKFLOW-SPEC.md definisce workflow e automazioni;
9. le specifiche tecniche definiscono l'implementazione;
10. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
