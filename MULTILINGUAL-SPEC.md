# StamoTenti — MULTILINGUAL SPECIFICATION

## 1. Scopo

Questo documento definisce il comportamento multilingua di StamoTenti.

Il progetto deve supportare almeno:

- italiano;
- inglese.

L'italiano è la lingua primaria.

Il sistema deve utilizzare, quando possibile, le funzionalità native di Hugo per la gestione delle lingue e delle traduzioni.

---

## 2. Lingue del progetto

Le lingue ufficialmente supportate sono definite dalla configurazione del progetto.

L'aggiunta di una nuova lingua è una decisione editoriale e tecnica esplicita.

Gli agenti non devono aggiungere autonomamente nuove lingue.

---

## 3. Lingua primaria

L'italiano è la lingua primaria del progetto.

Il contenuto originale degli articoli viene normalmente prodotto in italiano.

L'assenza della traduzione inglese non deve impedire la pubblicazione dell'articolo italiano.

La disponibilità di una traduzione inglese può avvenire successivamente.

---

## 4. Articolo e traduzioni

Una traduzione rappresenta lo stesso contenuto editoriale in una lingua differente.

La traduzione:

- non costituisce un nuovo articolo indipendente;
- mantiene il collegamento con l'originale;
- mantiene la stessa identità editoriale;
- può avere titolo e testo differenti;
- può avere adattamenti linguistici necessari;
- deve mantenere il significato e il rigore dell'originale.

Le versioni linguistiche devono essere collegate utilizzando i meccanismi nativi di Hugo quando appropriato.

---

## 5. Produzione delle traduzioni

Le traduzioni degli articoli sono prodotte e mantenute dagli agenti.

La traduzione inglese non richiede una revisione o approvazione umana separata per ogni articolo.

Gli agenti devono essere in grado di:

- tradurre un nuovo articolo;
- aggiornare una traduzione quando cambia l'originale;
- mantenere la struttura editoriale;
- mantenere le citazioni;
- mantenere i riferimenti alle fonti;
- preservare il significato tecnico;
- adattare correttamente terminologia e stile alla lingua di destinazione.

Il proprietario del progetto non deve essere trasformato in un revisore obbligatorio di ogni traduzione.

---

## 6. Qualità delle traduzioni

La traduzione deve privilegiare:

1. correttezza del significato;
2. correttezza terminologica;
3. conservazione delle qualificazioni e delle cautele presenti nell'originale;
4. coerenza con la letteratura specialistica della lingua di destinazione;
5. leggibilità;
6. naturalezza linguistica.

La traduzione non deve introdurre nuove affermazioni scientifiche o filosofiche non presenti nell'originale.

Quando una formulazione italiana non ha un equivalente diretto, l'agente può utilizzare una formulazione idiomatica nella lingua di destinazione purché il significato rimanga fedele.

---

## 7. Terminologia specialistica

I termini specialistici devono essere tradotti secondo l'uso consolidato nella lingua di destinazione quando questo esiste.

Quando un termine non possiede un equivalente sufficientemente stabile, può essere mantenuto nella lingua originale e accompagnato da una spiegazione quando necessario.

Gli agenti non devono tradurre meccanicamente termini tecnici soltanto per ottenere una corrispondenza letterale.

---

## 8. Citazioni e fonti

Le fonti bibliografiche non vengono tradotte.

Una fonte mantiene la propria identità indipendentemente dalla lingua dell'articolo che la cita.

Titolo, autore, editore, DOI, URL e altri dati bibliografici devono essere conservati secondo i dati della fonte.

Eventuali traduzioni esplicative di titoli o descrizioni possono essere mostrate separatamente quando utili.

Le citazioni presenti nell'articolo tradotto devono continuare a riferirsi alle stesse fonti dell'originale.

---

## 9. Testi citati in lingue differenti

Un articolo può contenere citazioni in:

- italiano;
- inglese;
- latino;
- greco antico;
- sanscrito;
- pali;
- altre lingue pertinenti all'argomento.

La lingua dell'articolo non determina la lingua dei materiali citati.

Quando una traduzione di una citazione è necessaria, deve essere possibile indicare separatamente:

- testo originale;
- traduzione;
- autore;
- traduttore, quando rilevante.

La lingua originale della fonte non deve essere persa durante la traduzione dell'articolo.

---

## 10. Autori e traduttori

Autori e traduttori delle fonti sono gestiti secondo AUTHOR-SPEC.md e SOURCE-SPEC.md.

La traduzione dell'articolo non modifica l'identità delle persone associate alle fonti.

I nomi propri delle persone non devono essere tradotti arbitrariamente.

Possono essere utilizzate forme linguistiche o traslitterazioni appropriate quando esistono convenzioni consolidate.

---

## 11. Temi e identità editoriali

I temi possiedono una singola identità editoriale indipendente dalla lingua.

La traduzione di un tema non costituisce un nuovo tema.

Esempio concettuale:

attenzione

può essere rappresentato come:

Italiano: Attenzione

Inglese: Attention

Le due forme rappresentano lo stesso tema.

Gli agenti non devono creare due temi distinti soltanto perché le rispettive etichette sono tradotte.

---

## 12. Temi visibili all'utente

Quando un tema è mostrato pubblicamente, la sua etichetta deve essere localizzata nella lingua corrente del sito.

La localizzazione riguarda la rappresentazione visualizzata, non l'identità interna del tema.

Il sistema deve quindi mantenere separati:

- identificativo stabile del tema;
- etichetta italiana;
- etichetta inglese.

Una traduzione mancante deve essere gestita senza creare un nuovo tema.

---

## 13. Tassonomie

Le tassonomie utilizzate dal sito devono rispettare il principio di identità unica e rappresentazione localizzata.

Quando una tassonomia è visibile all'utente:

- il nome della tassonomia può essere localizzato;
- i termini possono essere localizzati;
- gli identificativi interni devono rimanere stabili;
- le traduzioni non devono generare duplicazioni semantiche.

La configurazione tecnica deve utilizzare, quando possibile, i meccanismi nativi di Hugo.

---

## 14. Interfaccia del sito

Gli elementi dell'interfaccia devono essere localizzati quando il sito è disponibile in più lingue.

Possono comprendere:

- menu;
- pulsanti;
- etichette;
- messaggi;
- categorie;
- temi;
- informazioni di navigazione;
- testi generati automaticamente;
- metadata visualizzati.

Le stringhe dell'interfaccia non devono essere duplicate manualmente nei template quando Hugo offre un sistema di localizzazione appropriato.

---

## 15. URL

Gli URL devono essere progettati tenendo conto della lingua del contenuto.

La soluzione deve utilizzare i meccanismi nativi di Hugo e mantenere URL stabili quando possibile.

La traduzione del contenuto non deve richiedere una struttura URL arbitraria o mantenuta manualmente.

Le modifiche agli URL devono essere considerate una decisione tecnica significativa.

---

## 16. Metadata

I metadata che hanno natura linguistica possono avere valori differenti per ciascuna lingua.

Esempi:

- titolo;
- descrizione;
- summary;
- testo alternativo quando specificamente linguistico;
- etichette visualizzate;
- menu.

I metadata che identificano un'entità non devono invece essere duplicati soltanto per ragioni linguistiche.

---

## 17. Contenuti non tradotti

Un contenuto può esistere in una sola lingua.

L'assenza della traduzione non deve produrre una copia artificiale o una traduzione vuota.

Il sito deve poter indicare o gestire in modo naturale l'assenza della versione inglese.

Quando la traduzione viene successivamente prodotta, deve essere collegata al contenuto originale.

---

## 18. Aggiornamento delle traduzioni

Quando l'originale viene modificato, la relativa traduzione può diventare non aggiornata.

Gli agenti devono poter rilevare questo stato e proporre o effettuare l'aggiornamento secondo le regole del workflow degli agenti.

L'aggiornamento della traduzione deve preservare le modifiche linguistiche valide già presenti.

Non deve essere necessario ricreare manualmente l'intera traduzione.

---

## 19. Traduzione e citazioni

Quando l'originale contiene una citazione:

- la fonte citata rimane la stessa;
- il riferimento bibliografico rimane lo stesso;
- l'eventuale numero o identificativo della citazione rimane coerente;
- il testo citato non deve essere tradotto automaticamente se rappresenta una citazione testuale della fonte.

Se viene mostrata una traduzione della citazione, questa deve essere chiaramente distinta dall'originale.

---

## 20. Traduzione e rigore scientifico

La versione inglese deve mantenere:

- le qualificazioni;
- i limiti delle evidenze;
- le distinzioni tra correlazione e causalità;
- le formulazioni probabilistiche;
- le controversie;
- le cautele metodologiche.

Una traduzione non deve rendere più forte un'affermazione rispetto all'originale.

---

## 21. Traduzione e rigore filosofico

I concetti filosofici devono essere tradotti mantenendo le distinzioni concettuali rilevanti.

Gli agenti devono evitare:

- equivalenze artificiali;
- traduzioni eccessivamente semplificate;
- perdita della terminologia originale quando essa è significativa;
- assimilazioni indebite tra tradizioni differenti.

Quando necessario, il termine originale può essere mantenuto insieme alla traduzione.

---

## 22. Traduzione automatica e intervento umano

Il proprietario del progetto non deve approvare individualmente ogni traduzione.

L'intervento umano rimane possibile in qualsiasi momento.

Il proprietario può:

- correggere una traduzione;
- sostituire una formulazione;
- correggere un termine;
- modificare un titolo;
- richiedere una nuova traduzione.

Gli agenti devono rispettare le modifiche manuali e non sovrascriverle arbitrariamente.

---

## 23. Semplicità

Il sistema multilingua deve rimanere il più semplice possibile.

Non devono essere introdotti prematuramente:

- database di traduzioni;
- sistemi proprietari;
- workflow separati per ogni lingua;
- grafi semantici multilingua;
- sistemi complessi di sincronizzazione.

Quando Hugo è sufficiente, deve essere preferito.

---

## 24. Regola per gli agenti

Quando un agente lavora su contenuti multilingua deve:

1. identificare la lingua del contenuto;
2. verificare se esiste una traduzione collegata;
3. mantenere il collegamento tra le versioni;
4. preservare fonti e citazioni;
5. preservare il significato;
6. localizzare ciò che è destinato all'utente;
7. non duplicare entità editoriali;
8. non creare nuovi temi per traduzioni di temi esistenti;
9. non richiedere approvazione umana per ogni traduzione;
10. segnalare soltanto problemi realmente ambigui o rilevanti.

---

## 25. Libertà operativa

Il proprietario deve poter modificare manualmente qualsiasi contenuto linguistico.

L'automazione non deve impedire:

- modifiche manuali;
- correzioni;
- sostituzioni;
- aggiunta di traduzioni;
- rimozione di traduzioni;
- modifica delle etichette localizzate.

Gli agenti devono assistere il lavoro editoriale senza creare dipendenza dal sistema automatico.

---

## 26. Gerarchia delle specifiche

In caso di conflitto:

1. TO-BE.md definisce la visione e i vincoli fondamentali;
2. CONTENT-MODEL.md definisce le entità e le relazioni;
3. MULTILINGUAL-SPEC.md definisce il comportamento multilingua;
4. le specifiche specialistiche definiscono il comportamento delle singole entità;
5. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.

