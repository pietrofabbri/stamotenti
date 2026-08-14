# StamoTenti — MEDIA-SPEC

## 1. Scopo

Questo documento definisce la gestione dei media di StamoTenti.

Per media si intendono, tra gli altri:

- immagini;
- fotografie;
- diagrammi;
- PDF;
- EPUB;
- audio;
- video;
- dataset;
- altri file associati a contenuti, fonti o utenti.

Il modello deve distinguere chiaramente tra accessibilità tecnica, utilizzo editoriale e possibilità di distribuzione.

StamoTenti deve distinguere sempre tra:

- posso leggere;
- posso usare per ricerca;
- posso citare;
- posso pubblicare;
- posso redistribuire.

Queste condizioni non sono equivalenti.

---

## 2. Principi fondamentali

Un media deve essere classificato in modo esplicito.

Il sistema non deve assumere che una risorsa sia pubblicabile semplicemente perché:

- è raggiungibile tramite URL;
- è disponibile online;
- può essere scaricata;
- è leggibile da un agente;
- è stata utilizzata durante una ricerca.

L'accesso tecnico non costituisce autorizzazione alla pubblicazione.

---

## 3. Stato di distribuzione

Ogni media deve avere uno stato di distribuzione.

Gli stati principali sono:

- `public`
- `private`
- `controlled`
- `pending_review`

### public

Il media può essere distribuito pubblicamente, nei limiti della relativa licenza o autorizzazione.

### private

Il media può essere utilizzato internamente ma non deve essere pubblicato o redistribuito.

### controlled

Il media può avere un utilizzo controllato ma non deve essere trattato come pubblico.

Può essere utilizzato, per esempio, per materiali destinati a specifici utenti o a distribuzioni autorizzate.

### pending_review

Il media non deve essere pubblicato finché diritti, provenienza o condizioni di utilizzo non sono stati verificati.

---

## 4. Permessi di utilizzo

Lo stato di distribuzione non sostituisce la descrizione dei permessi.

Quando necessario, un media può avere permessi espliciti:

visibility: private

can_read: true
can_research: true
can_cite: true
can_publish: false
can_redistribute: false

Questi valori descrivono ciò che StamoTenti può fare con la risorsa e non devono essere dedotti esclusivamente dalla visibilità.

Un media può quindi essere privato ma perfettamente utilizzabile per ricerca e citazione.

---

## 5. Fonte e media

La fonte bibliografica e il file non sono la stessa entità.

Una fonte può essere:

- disponibile tramite URL;
- identificata da DOI;
- disponibile pubblicamente;
- disponibile solo privatamente;
- priva di una copia locale;
- rappresentata da più file;
- rappresentata da un file pubblico e da una copia privata.

Il media deve quindi poter essere collegato alla relativa fonte senza sostituirla.

Esempio:

Fonte:
un libro scientifico.

Media:
una copia EPUB acquistata privatamente.

La fonte può essere citata.

L'EPUB può essere utilizzato per ricerca.

L'EPUB non può essere redistribuito.

---

## 6. Ambienti di storage

Il repository del progetto e lo storage dei media hanno responsabilità differenti.

### Repository del progetto

GitHub deve contenere principalmente:

- codice;
- Markdown;
- specifiche;
- configurazioni;
- template;
- script;
- metadata appropriati.

Git non deve essere utilizzato come biblioteca generale di PDF, EPUB, audio o altri file binari di grandi dimensioni.

### Object storage

I media devono essere conservati in object storage.

L'architettura deve distinguere almeno logicamente:

- ambiente pubblico;
- ambiente privato;
- eventuale distribuzione controllata.

La separazione può essere realizzata tramite bucket distinti o tramite meccanismi equivalenti.

La scelta tecnica definitiva deve mantenere evidente la distinzione tra contenuti pubblicabili e materiali privati.

---

## 7. Storage pubblico

Lo storage pubblico contiene esclusivamente media che possono essere distribuiti secondo i relativi diritti.

Può comprendere:

- immagini pubblicabili;
- audio pubblici;
- video pubblici;
- dataset pubblici;
- PDF pubblicabili;
- materiali didattici pubblicabili;
- altri file destinati agli utenti.

Un media non deve essere inserito nello storage pubblico semplicemente perché è tecnicamente possibile farlo.

La pubblicazione richiede che il relativo stato sia compatibile con la distribuzione.

---

## 8. Storage privato

Lo storage privato contiene materiali che StamoTenti può utilizzare internamente ma che non devono essere distribuiti pubblicamente.

Può comprendere:

- PDF acquistati;
- EPUB acquistati;
- articoli scientifici acquistati;
- libri digitali;
- documenti di ricerca;
- materiali forniti privatamente;
- file di lavoro;
- materiali con diritti limitati.

Questi file:

- non devono essere pubblicati dal sito;
- non devono essere inseriti nel repository Git pubblico;
- non devono essere caricati automaticamente in archivi pubblici.

---

## 9. Media per utenti autorizzati

Alcuni media possono essere destinati a utenti che hanno ricevuto accesso specifico.

Esempi:

- guide audio;
- meditazioni guidate;
- corsi;
- materiali allegati a una mailing list;
- materiali acquistati;
- contenuti riservati.

Questi media non devono essere classificati semplicemente come `public`.

Devono essere trattati come risorse a distribuzione controllata.

Il sistema potrà utilizzare URL temporanei, token o altri meccanismi di autorizzazione quando necessari.

La soluzione tecnica specifica sarà definita nella relativa architettura di distribuzione.

---

## 10. Accesso degli agenti

Gli agenti autorizzati devono poter leggere e scrivere sia nello storage pubblico sia nello storage privato quando necessario al loro lavoro.

L'accesso tecnico non equivale però all'autorizzazione editoriale.

Un agente può avere permesso tecnico di scrittura nello storage pubblico senza essere autorizzato a rendere pubblico autonomamente un nuovo media.

Le procedure devono distinguere:

permesso tecnico di accesso

da

autorizzazione editoriale alla pubblicazione.

Gli agenti devono poter, secondo i rispettivi permessi:

- leggere media pubblici;
- leggere media privati;
- caricare nuovi media;
- aggiornare metadata;
- spostare media;
- creare proposte;
- preparare materiali per la pubblicazione.

Gli agenti non devono autonomamente modificare lo stato di un media da privato a pubblico quando ciò richiede una decisione editoriale.

---

## 11. Catalogazione obbligatoria

Ogni media gestito dal sistema deve essere classificato almeno secondo:

- identità;
- tipo;
- fonte quando disponibile;
- stato di distribuzione;
- permessi di utilizzo quando necessari;
- provenienza;
- eventuale licenza;
- relazione con contenuti o fonti.

L'agente deve essere in grado di determinare immediatamente se il media è:

- pubblico;
- privato;
- in attesa di verifica;
- destinato a utenti autorizzati.

Un media privo di classificazione sufficiente non deve essere trattato come pubblico.

---

## 12. Diritti e licenze

Quando disponibili devono essere registrati:

- titolare dei diritti;
- licenza;
- URL della licenza;
- condizioni di attribuzione;
- eventuali restrizioni;
- fonte della licenza;
- eventuali autorizzazioni specifiche.

Gli agenti non devono inventare licenze.

Se la licenza non è verificabile, il media deve essere trattato con cautela e, quando necessario, come `pending_review`.

---

## 13. PDF ed EPUB privati

I PDF e gli EPUB acquistati o comunque non redistribuibili possono essere conservati nello storage privato.

Il sistema deve conservare anche il riferimento bibliografico alla relativa fonte.

Esempio:

Fonte:
libro scientifico X

Media:
EPUB acquistato

visibility: private

can_read: true
can_research: true
can_cite: true
can_publish: false
can_redistribute: false

La disponibilità del file privato permette agli agenti autorizzati di utilizzare la risorsa per ricerca e verifica senza trasformarla in materiale pubblico.

---

## 14. Dataset

I dataset sono una categoria importante per StamoTenti.

Un dataset pubblico può essere:

- citato;
- archiviato;
- collegato agli articoli;
- utilizzato per analisi;
- redistribuito quando la licenza lo consente.

Quando appropriato, i dataset prodotti da StamoTenti possono essere archiviati in repository persistenti come Zenodo.

I dataset privati o non redistribuibili devono invece rimanere nello storage privato.

Devono essere conservati almeno:

- provenienza;
- versione quando rilevante;
- descrizione;
- licenza;
- fonte;
- eventuale DOI;
- relazione con gli articoli.

---

## 15. Zenodo

Zenodo non costituisce lo storage generale dei media di StamoTenti.

Può essere utilizzato selettivamente per:

- dataset pubblicabili;
- output scientifici;
- materiali di ricerca pubblicabili;
- documentazione;
- versioni archiviate di risorse;
- altri materiali per i quali StamoTenti dispone dei diritti necessari.

Zenodo deve essere considerato principalmente un archivio persistente e citabile, non una sostituzione dello storage operativo.

Una risorsa può quindi:

1. essere prodotta o gestita nello storage di StamoTenti;
2. essere sottoposta a verifica;
3. essere approvata;
4. essere pubblicata;
5. essere successivamente archiviata in Zenodo quando ciò è utile.

---

## 16. Conservazione

Lo storage operativo non deve essere considerato automaticamente un sistema completo di backup.

Per i materiali importanti devono essere valutate copie o archiviazioni indipendenti quando il valore della risorsa lo giustifica.

Per i materiali pubblici di particolare importanza può essere utilizzato Zenodo o un altro archivio persistente appropriato.

Per i materiali privati deve essere mantenuta una strategia di backup separata.

La perdita del repository Git non deve comportare automaticamente la perdita della biblioteca privata.

La perdita dello storage dei media non deve comportare automaticamente la perdita del catalogo bibliografico.

---

## 17. Metadata dei media

Un media può avere metadata quali:

- identificativo stabile;
- titolo;
- tipo;
- autore o creatore;
- data;
- lingua;
- fonte;
- provenienza;
- licenza;
- DOI;
- URL originale;
- stato di distribuzione;
- permessi;
- checksum;
- dimensione;
- formato;
- posizione nello storage;
- articolo associato;
- fonte associata;
- temi;
- note editoriali.

Non tutti i campi sono obbligatori per ogni tipo di media.

Il modello deve comunque permettere di aggiungerli quando necessari.

---

## 18. Temi dei media

I media possono essere associati a uno o più temi.

Questa classificazione è utile soprattutto per:

- dataset;
- studi;
- documenti;
- materiali di ricerca;
- immagini scientifiche;
- audio;
- video.

La classificazione dei media deve utilizzare il vocabolario controllato del progetto quando applicabile.

Un agente può proporre nuovi temi ma non modificare autonomamente il vocabolario approvato.

---

## 19. Agenti e classificazione

Quando un agente acquisisce o riceve un nuovo media deve, quando possibile:

1. identificarlo;
2. verificare la fonte;
3. determinare la provenienza;
4. verificare la licenza;
5. determinare i diritti utilizzabili;
6. classificare lo stato di distribuzione;
7. proporre i temi pertinenti;
8. collegarlo alla fonte;
9. collegarlo agli eventuali articoli;
10. conservarlo nell'ambiente corretto.

Se una decisione richiede approvazione umana, l'agente deve creare una proposta invece di prendere autonomamente la decisione.

---

## 20. Verifica online

Gli agenti possono effettuare ricerche online per verificare:

- provenienza;
- DOI;
- licenza;
- autore;
- metadata;
- disponibilità pubblica;
- fonte originale;
- condizioni di distribuzione.

Le ricerche devono essere proporzionate al compito.

Gli agenti devono evitare ricerche inutilmente estese quando una verifica semplice è sufficiente.

Quando una verifica non è conclusiva, il media deve rimanere in uno stato prudenziale e può essere sottoposto all'approvazione del proprietario del progetto.

---

## 21. Approvazione

Le decisioni che richiedono il giudizio del proprietario del progetto devono essere rappresentate come proposte persistenti.

Una proposta dovrebbe contenere almeno:

- media interessato;
- decisione richiesta;
- motivazione;
- evidenze utilizzate;
- eventuali fonti consultate;
- azione proposta;
- stato della proposta.

Gli stati minimi possono essere:

- `pending`;
- `approved`;
- `rejected`.

Una decisione approvata deve poter essere registrata nei metadata o nel sistema di gestione senza dipendere dalla memoria della conversazione con l'agente.

Il sistema di approvazione potrà essere implementato nella futura applicazione di gestione delle fonti e dei media.

---

## 22. Regola per la pubblicazione

Un agente può pubblicare o rendere accessibile un media soltanto quando:

1. il media è stato classificato;
2. i diritti sono compatibili con l'azione;
3. lo stato di distribuzione lo consente;
4. eventuali approvazioni necessarie sono state ottenute.

La possibilità tecnica di scrivere nello storage pubblico non costituisce da sola autorizzazione alla pubblicazione.

---

## 23. Media pubblici e privati

La distinzione pubblico/privato deve essere evidente sia agli agenti sia al sistema.

Un agente che recupera una risorsa deve poter sapere immediatamente se:

- può essere pubblicata;
- può essere utilizzata soltanto internamente;
- richiede verifica;
- è destinata a utenti autorizzati.

Il sistema non deve affidarsi esclusivamente al percorso fisico del file per determinare questa informazione.

Lo storage e i metadata devono fornire una seconda forma di protezione contro classificazioni errate.

---

## 24. Non duplicazione

Lo stesso media non deve essere duplicato inutilmente.

Quando una risorsa è già disponibile in uno storage appropriato, il sistema dovrebbe preferire:

- riferimento;
- collegamento;
- metadata condivisi;
- copia solo quando esiste una ragione concreta.

Una duplicazione può essere giustificata per:

- backup;
- conservazione;
- accessibilità;
- distribuzione;
- sicurezza;
- indipendenza infrastrutturale.

---

## 25. Separazione tra catalogo e file

Il catalogo dei media deve essere separato concettualmente dai file stessi.

Il catalogo deve poter continuare a esistere anche se:

- un file viene spostato;
- un file viene sostituito;
- un file viene archiviato;
- un file viene eliminato;
- una copia pubblica non è più disponibile.

Il catalogo deve conservare l'identità e la storia editoriale della risorsa senza dipendere esclusivamente dalla sua posizione fisica.

---

## 26. Audio e guide

Gli audio prodotti da StamoTenti possono essere destinati a:

- pubblicazione gratuita;
- articoli;
- podcast;
- meditazioni guidate;
- mailing list;
- contenuti riservati;
- prodotti a pagamento.

Gli audio destinati a utenti autorizzati non devono essere conservati nel repository Git.

Devono essere conservati nello storage dei media e distribuiti attraverso un sistema che permetta di controllare l'accesso quando necessario.

Il sistema deve permettere di modificare successivamente il meccanismo di distribuzione senza cambiare l'identità del media.

---

## 27. Media generati da StamoTenti

Quando StamoTenti produce direttamente un media, devono essere registrati quando pertinenti:

- autore;
- data;
- versione;
- licenza;
- stato di distribuzione;
- relazione con il contenuto che lo ha generato.

La pubblicazione deve rispettare le regole generali della presente specifica.

---

## 28. Principio di semplicità

La gestione dei media deve rimanere proporzionata alla scala del progetto.

Non devono essere introdotti prematuramente:

- sistemi DAM complessi;
- database dedicati ai file;
- pipeline di elaborazione distribuite;
- sistemi proprietari di storage;
- infrastrutture cloud inutilmente complesse.

La combinazione di:

- GitHub per il codice e i contenuti strutturati;
- object storage per i media;
- catalogo dei media;
- metadata di diritti e distribuzione;
- Zenodo per l'archiviazione persistente selettiva;

costituisce una base sufficiente per la crescita iniziale del progetto.

---

## 29. Regola per gli agenti

Gli agenti devono considerare questa specifica insieme a:

- TO-BE.md;
- CONTENT-MODEL.md;
- SOURCE-SPEC.md;
- AUTHOR-SPEC.md;
- MULTILINGUAL-SPEC.md;
- ARTICLE-SPEC.md.

In caso di conflitto, devono essere rispettate le regole di gerarchia definite dalla costituzione del progetto.

Gli agenti non devono modificare autonomamente le regole fondamentali di accesso, distribuzione o pubblicazione.

Possono invece:

- catalogare;
- verificare;
- proporre;
- preparare;
- archiviare;
- aggiornare metadata;
- eseguire operazioni già autorizzate.

La decisione editoriale e legale sulla distribuzione rimane distinta dal semplice potere tecnico dell'agente di accedere al file.

---

## 30. Evoluzione

L'architettura può evolvere in futuro verso una vera applicazione di gestione delle fonti e dei media.

Questa applicazione potrà fornire:

- catalogo centralizzato;
- ricerca;
- classificazione;
- gestione delle fonti;
- gestione dei media;
- gestione delle autorizzazioni;
- coda delle approvazioni;
- collegamento con gli articoli;
- gestione dello storage;
- integrazione con GitHub;
- integrazione con Zenodo;
- audit delle decisioni.

La progettazione iniziale non deve però dipendere dalla disponibilità immediata di tale applicazione.

Il modello deve essere abbastanza semplice da poter essere implementato progressivamente.
