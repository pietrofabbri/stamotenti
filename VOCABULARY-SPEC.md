# StamoTenti — VOCABULARY SPECIFICATION

## 1. Scopo

Questo documento definisce la gestione del vocabolario controllato utilizzato da StamoTenti.

Il vocabolario controllato mantiene coerente nel tempo la classificazione dei contenuti e permette agli agenti di utilizzare termini approvati senza introdurre autonomamente varianti, sinonimi o nuove categorie.

Il vocabolario riguarda principalmente i temi trasversali degli articoli, ma può essere esteso in futuro ad altri insiemi terminologici quando ciò produca un'utilità editoriale reale.

---

## 2. Principio fondamentale

Un termine utilizzato per classificare i contenuti deve avere un'identità editoriale stabile.

Il sistema deve evitare che concetti equivalenti vengano rappresentati casualmente attraverso termini differenti.

Se il vocabolario contiene il tema "attenzione", un agente non deve introdurre autonomamente varianti equivalenti come:

- attenzione mentale;
- capacità attentiva;
- attenzione cognitiva;
- attentional focus.

La presenza di termini differenti è appropriata quando essi rappresentano realmente concetti differenti.

La distinzione deve essere una decisione editoriale e non una conseguenza casuale della formulazione utilizzata da un agente.

---

## 3. Temi trasversali

I temi sono classificazioni trasversali che permettono di collegare articoli appartenenti a differenti sotto-aree editoriali.

Un tema:

- può essere associato a molti articoli;
- può collegare sotto-aree differenti;
- non modifica la sotto-area principale dell'articolo;
- non costituisce necessariamente una gerarchia;
- non deve sostituire la classificazione editoriale principale.

La struttura delle macro-aree e delle sotto-aree rimane quella definita da TO-BE.md.

---

## 4. Identità concettuale

Il vocabolario deve distinguere tra:

- concetto editoriale;
- forma linguistica del termine;
- identificativo stabile del concetto.

L'identità principale appartiene al concetto.

Le diverse forme linguistiche dello stesso concetto non costituiscono termini editoriali indipendenti.

Per esempio, il concetto di attenzione può essere rappresentato da:

- italiano: attenzione;
- inglese: attention.

Le due forme devono riferirsi alla stessa identità concettuale.

Questo principio è particolarmente importante per mantenere coerenti le classificazioni tra le versioni linguistiche dello stesso articolo.

---

## 5. Coerenza tra lingue

Le versioni linguistiche dello stesso articolo devono normalmente ereditare la stessa classificazione concettuale.

La traduzione inglese non deve essere riclassificata autonomamente come se fosse un articolo indipendente.

L'agente incaricato della traduzione deve mantenere i temi concettuali dell'originale e verificare che le relative forme linguistiche siano corrette.

Una differenza di terminologia tra italiano e inglese può essere introdotta quando riflette una reale differenza concettuale o terminologica, ma deve essere trattata come una decisione editoriale e non come una divergenza casuale delle classificazioni.

Questo principio evita che versioni linguistiche dello stesso contenuto finiscano in insiemi tematici sostanzialmente differenti.

---

## 6. Vocabolario controllato

Il vocabolario approvato costituisce la fonte di verità editoriale per i termini utilizzabili dagli agenti.

Ogni concetto approvato dovrebbe possedere almeno:

- identificativo stabile;
- forma canonica per ciascuna lingua supportata;
- descrizione;
- stato;
- eventuali note editoriali.

Il modello può essere implementato inizialmente con semplici file strutturati.

Non deve essere introdotto un database esclusivamente per gestire il vocabolario.

---

## 7. Identificativo del concetto

Ogni concetto deve avere un identificativo stabile e indipendente dalla forma visualizzata.

L'identificativo:

- deve essere semplice;
- deve essere leggibile;
- deve rimanere stabile nel tempo;
- non deve dipendere necessariamente dal titolo visualizzato;
- non deve essere modificato soltanto perché cambia la formulazione editoriale del termine.

La forma visualizzata può cambiare con una decisione editoriale senza necessariamente modificare l'identità interna del concetto.

---

## 8. Forme linguistiche

Ogni concetto può avere una o più forme linguistiche.

Per le lingue principali del progetto devono essere previste almeno:

- forma italiana;
- forma inglese.

Una forma linguistica deve rappresentare lo stesso concetto quando ha lo stesso significato editoriale.

Le forme linguistiche possono differire anche sensibilmente nella formulazione quando la lingua richiede una resa terminologica differente.

Non è necessario che italiano e inglese siano traduzioni letterali.

È necessario che rappresentino lo stesso concetto editoriale.

---

## 9. Terminologia scientifica e accademica

Quando un termine appartiene a un ambito scientifico, filosofico, storico o accademico, la forma linguistica deve essere scelta tenendo conto della terminologia effettivamente utilizzata nella letteratura pertinente.

Gli agenti possono effettuare ricerche online o bibliografiche per verificare:

- terminologia prevalente;
- significato del termine;
- differenze tra traduzioni;
- eventuali ambiguità;
- uso disciplinare.

La scelta finale di una forma terminologica significativa può richiedere una decisione editoriale.

---

## 10. Stato dei concetti

Un concetto può trovarsi, almeno concettualmente, in uno dei seguenti stati:

- proposto;
- approvato;
- deprecato;
- ritirato.

### Proposto

Il concetto è stato suggerito da un agente o dal proprietario ma non è ancora parte del vocabolario ufficiale.

Un concetto proposto non deve diventare stabilmente parte della classificazione editoriale senza approvazione quando l'approvazione è richiesta dal workflow.

### Approvato

Il concetto può essere utilizzato dagli agenti e dagli articoli.

### Deprecato

Il concetto non dovrebbe essere utilizzato per nuovi contenuti, ma può essere mantenuto temporaneamente per compatibilità con contenuti esistenti.

Quando appropriato, può indicare il concetto approvato che deve sostituirlo.

### Ritirato

Il concetto non deve più essere utilizzato.

La rimozione effettiva di un concetto già utilizzato deve essere gestita con attenzione per evitare perdita di informazioni o rottura delle relazioni esistenti.

---

## 11. Creazione di nuovi concetti

Gli agenti possono individuare la necessità di un nuovo concetto.

Non possono però aggiungerlo autonomamente al vocabolario ufficiale quando la modifica richiede approvazione.

Devono invece poter produrre una proposta che includa, quando possibile:

- concetto proposto;
- forma italiana;
- forma inglese;
- descrizione;
- motivazione;
- articoli interessati;
- termini esistenti potenzialmente affini;
- eventuali sinonimi;
- evidenze terminologiche;
- motivazione per cui i termini esistenti non sono sufficienti.

La proposta viene gestita dal workflow delle autorizzazioni.

Il sistema deve comunque evitare di bloccare inutilmente il lavoro degli agenti: quando una classificazione può essere effettuata correttamente utilizzando concetti già approvati, l'agente deve procedere autonomamente.

---

## 12. Ricerca e validazione

Quando un agente sospetta che sia necessario un nuovo concetto o una nuova forma linguistica, può effettuare una ricerca online o bibliografica per verificare:

- se il concetto è realmente distinto;
- quale terminologia sia maggiormente utilizzata;
- quali termini siano prevalenti nella letteratura;
- se esistano ambiguità;
- se il termine proposto possa creare conflitti con concetti esistenti.

La ricerca deve essere proporzionata al problema.

Non è necessario effettuare ricerche estese quando il problema è già sufficientemente chiaro.

Le ricerche devono rispettare i limiti di costo e di utilizzo stabiliti dal sistema.

Il sistema dovrà prevedere limiti di utilizzo appropriati ai diversi task e ai diversi modelli utilizzati dagli agenti, così da evitare costi inutili senza impedire ricerche realmente necessarie.

I risultati della ricerca possono motivare una proposta ma non costituiscono automaticamente un'approvazione editoriale.

---

## 13. Sinonimi e varianti

I sinonimi non devono diventare automaticamente concetti distinti.

Quando più espressioni indicano sostanzialmente lo stesso concetto, il sistema deve preferire una forma canonica per ciascuna lingua.

Eventuali sinonimi o varianti possono essere conservati come informazioni ausiliarie per:

- ricerca interna;
- riconoscimento della terminologia nelle fonti;
- comprensione degli agenti;
- migrazione dei contenuti;
- compatibilità futura.

La presenza di un sinonimo non implica che esso possa essere utilizzato come termine editoriale indipendente.

---

## 14. Distinzione tra concetti simili

Il sistema non deve unificare automaticamente concetti soltanto perché semanticamente vicini.

Per esempio, concetti come:

- attenzione;
- concentrazione;
- consapevolezza;
- metacognizione;
- mind-wandering;

possono essere collegati ma non devono essere trattati come sinonimi.

La distinzione deve essere mantenuta quando possiede una reale utilità editoriale o scientifica.

Gli agenti devono segnalare i casi realmente ambigui invece di risolverli arbitrariamente.

---

## 15. Termini visibili al pubblico

Un concetto può essere utilizzato internamente senza essere necessariamente mostrato all'utente.

Il sistema deve distinguere, quando necessario, tra:

- classificazione interna;
- termine mostrato pubblicamente;
- termine utilizzato nei dati strutturati;
- termine utilizzato per ricerca o indicizzazione.

La decisione di rendere pubblica una classificazione non deve essere determinata esclusivamente dalla capacità tecnica di Hugo di generare una pagina per quel termine.

---

## 16. Relazione con Hugo

Quando appropriato, il vocabolario dei temi deve essere rappresentato attraverso le tassonomie native di Hugo.

Hugo permette di associare contenuti a termini di una tassonomia e di generare automaticamente le relative relazioni e pagine di tassonomia.

Concettualmente, una struttura come:

topics → attenzione → articoli associati

permette al sistema di ricavare automaticamente l'insieme degli articoli associati al tema.

Queste relazioni inverse non devono essere mantenute manualmente.

Le tassonomie di Hugo sono però un meccanismo di implementazione.

Non costituiscono la fonte di verità editoriale del vocabolario.

La fonte di verità è il vocabolario approvato e le relative identità concettuali.

Il sistema non deve creare una tassonomia tecnica parallela quando le funzionalità native di Hugo sono sufficienti.

---

## 17. Metadata dei concetti

Quando un concetto necessita di informazioni aggiuntive, tali informazioni possono essere associate al concetto stesso.

Possono comprendere:

- definizione;
- descrizione editoriale;
- note;
- forme linguistiche;
- sinonimi;
- relazioni;
- stato;
- data di approvazione;
- eventuali fonti utilizzate per definirlo.

Non è necessario creare una pagina pubblica per ogni concetto.

---

## 18. Relazioni tra concetti

Il modello non deve introdurre automaticamente una gerarchia tra tutti i concetti.

Relazioni più sofisticate possono essere introdotte in futuro quando la quantità dei contenuti ne dimostrerà l'utilità.

Possono eventualmente essere rappresentate relazioni come:

- concetto più generale;
- concetto più specifico;
- concetto correlato;
- sinonimo;
- variante linguistica.

Queste relazioni non devono diventare un'ontologia complessa senza una necessità concreta.

---

## 19. Uso da parte degli agenti

Gli agenti che classificano gli articoli devono consultare il vocabolario approvato prima di assegnare i temi.

Il comportamento preferito è:

1. leggere il vocabolario disponibile;
2. individuare i concetti pertinenti;
3. utilizzare concetti approvati;
4. utilizzare la forma linguistica appropriata;
5. evitare sinonimi arbitrari;
6. segnalare eventuali lacune;
7. proporre nuovi concetti soltanto quando necessario.

L'agente non deve creare una nuova variante semplicemente perché il termine approvato non coincide perfettamente con la formulazione utilizzata nella fonte.

---

## 20. Classificazione automatica

La classificazione automatica deve essere conservativa ma non paralizzante.

Quando un articolo può essere classificato correttamente utilizzando concetti già approvati, l'agente deve procedere senza richiedere un'approvazione umana.

Quando la corrispondenza è incerta, l'agente deve:

- evitare classificazioni eccessive;
- valutare le evidenze disponibili;
- segnalare l'incertezza quando rilevante;
- proporre un nuovo concetto solo se realmente necessario.

Il sistema deve privilegiare l'autonomia operativa degli agenti entro confini sicuri.

---

## 21. Autonomia degli agenti

Le regole del vocabolario non devono trasformarsi in un sistema che impedisce agli agenti di lavorare.

Il principio generale è:

> Gli agenti devono avere la massima autonomia compatibile con l'integrità editoriale del vocabolario.

In particolare, un agente deve poter autonomamente:

- leggere il vocabolario;
- utilizzare concetti approvati;
- classificare contenuti;
- verificare terminologia;
- effettuare ricerche necessarie;
- proporre nuovi concetti;
- correggere classificazioni chiaramente errate quando il workflow lo consente.

L'approvazione umana deve essere richiesta soprattutto per decisioni che modificano il vocabolario ufficiale o che presentano conseguenze editoriali rilevanti.

Il workflow delle autorizzazioni deve definire le condizioni precise.

---

## 22. Autorizzazioni basate sulle azioni

Le autorizzazioni non devono essere definite rigidamente in funzione dell'identità dell'agente.

Devono essere definite principalmente in funzione:

- dell'azione;
- delle condizioni;
- del rischio;
- dell'impatto della modifica.

Per esempio:

- classificare con un concetto già approvato può essere autonomo;
- proporre un nuovo concetto può essere autonomo come proposta;
- approvare definitivamente un nuovo concetto può richiedere autorizzazione;
- modificare la struttura del vocabolario può richiedere autorizzazione.

Questo modello permette di cambiare agente o modello senza dover ridefinire l'intera governance.

---

## 23. Proposte provenienti dal proprietario

Il proprietario può proporre direttamente:

- nuovi concetti;
- modifiche a concetti esistenti;
- nuove forme linguistiche;
- deprecazioni;
- correzioni;
- relazioni tra concetti.

Il sistema deve permettere di fornire tali modifiche direttamente agli agenti o attraverso gli strumenti di gestione previsti.

Gli agenti devono poter trasformare una proposta fornita manualmente in una modifica strutturata del vocabolario senza impedire l'intervento manuale.

---

## 24. Fonti e vocabolario

Le fonti possono essere classificate anche per argomento.

La classificazione delle fonti e quella degli articoli devono poter utilizzare le stesse identità concettuali quando appropriato.

Questo permette al sistema di individuare fonti potenzialmente pertinenti quando viene progettato un nuovo articolo.

Una fonte può appartenere a più concetti.

La classificazione di una fonte non implica che essa debba essere utilizzata in un articolo.

La gestione dettagliata delle fonti è definita in SOURCE-SPEC.md.

---

## 25. Approvazione

Le modifiche al vocabolario ufficiale devono essere tracciabili quando richiedono un'approvazione.

Il sistema dovrebbe conservare almeno:

- proposta;
- autore della proposta;
- data;
- decisione;
- eventuale motivazione;
- versione del vocabolario interessata.

Il sistema di approvazione dettagliato è definito in WORKFLOW-SPEC.md.

Il vocabolario non deve dipendere dalla memoria della conversazione tra il proprietario e un agente.

---

## 26. Non duplicazione

Il sistema deve evitare duplicazioni concettuali.

Prima di proporre un nuovo concetto, un agente deve verificare se esiste già un concetto sufficientemente adeguato.

Quando un nuovo concetto viene approvato, eventuali concetti precedenti equivalenti devono essere gestiti attraverso una decisione esplicita di deprecazione o consolidamento.

Non devono essere mantenuti simultaneamente più concetti equivalenti soltanto per comodità dell'agente.

---

## 27. Modifiche al vocabolario

Le modifiche al vocabolario devono essere compatibili con gli articoli già pubblicati.

Quando un concetto viene modificato o deprecato, il sistema dovrebbe poter individuare automaticamente i contenuti interessati.

Le modifiche non devono richiedere una revisione manuale di tutti gli articoli quando la trasformazione può essere eseguita automaticamente in modo sicuro.

Le operazioni irreversibili devono invece richiedere una decisione esplicita.

---

## 28. Coerenza multilingue dopo le modifiche

Quando cambia la forma linguistica di un concetto, l'identità concettuale rimane invariata.

Quando cambia il significato editoriale del concetto, la modifica deve essere trattata come una decisione sul concetto stesso e non come una semplice traduzione.

Le forme italiana e inglese devono essere verificate insieme quando una modifica può alterarne la corrispondenza.

Una modifica a una forma linguistica non deve creare automaticamente un nuovo concetto.

---

## 29. Ricerca interna

Il vocabolario può essere utilizzato per migliorare la ricerca interna del sito.

I sinonimi e le varianti linguistiche possono essere utilizzati per aiutare il riconoscimento delle query.

I meccanismi di ricerca non devono però modificare il vocabolario.

Un termine trovato attraverso una ricerca può essere utilizzato come suggerimento, ma non deve diventare automaticamente un concetto approvato.

---

## 30. Principio di semplicità

Il vocabolario deve rimanere semplice.

Non devono essere introdotti senza necessità:

- ontologie;
- knowledge graph;
- gerarchie complesse;
- sistemi di inferenza;
- alias multilivello;
- database dedicati;
- sistemi semantici esterni.

Queste tecnologie possono essere introdotte in futuro quando la scala e la complessità dei contenuti ne dimostreranno l'utilità.

---

## 31. Principio di evoluzione

Il vocabolario deve poter crescere insieme al progetto.

La crescita deve essere guidata dai contenuti reali e dalle esigenze editoriali.

Non è necessario prevedere oggi tutti i concetti che potranno comparire in futuro.

È preferibile aggiungere un concetto quando esiste una reale necessità editoriale piuttosto che costruire anticipatamente un vocabolario estremamente ampio.

---

## 32. Regola per gli agenti

Gli agenti devono considerare il vocabolario approvato come vincolante per la classificazione editoriale, senza interpretare tale vincolo come un divieto generale di iniziativa.

Gli agenti:

- non possono modificare autonomamente il significato dei concetti approvati;
- non devono creare arbitrariamente nuovi concetti;
- possono classificare autonomamente con concetti approvati;
- possono verificare la terminologia;
- possono effettuare ricerche;
- possono proporre nuovi concetti;
- possono proporre modifiche;
- devono poter continuare il lavoro sulle parti non controverse anche quando una decisione richiede approvazione.

Una richiesta di approvazione non deve bloccare automaticamente l'intero task quando l'agente può procedere in sicurezza sulle altre parti.

---

## 33. Gerarchia delle specifiche

In caso di conflitto:

1. TO-BE.md definisce la visione e i vincoli fondamentali;
2. CONTENT-MODEL.md definisce le entità e le relazioni;
3. VOCABULARY-SPEC.md definisce il vocabolario e le regole terminologiche;
4. le altre specifiche definiscono l'utilizzo del vocabolario nelle rispettive aree;
5. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
