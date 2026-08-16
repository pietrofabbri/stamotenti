# StamoTenti — CONTENT MODEL

## 1. Scopo

Questo documento definisce il modello concettuale dei contenuti di StamoTenti.

Stabilisce:

- quali entità esistono;
- quali informazioni fondamentali le descrivono;
- come le entità sono collegate;
- quali relazioni sono editorialmente significative;
- quali responsabilità spettano al contenuto e quali al sistema.

Non definisce i dettagli grafici del sito né le modalità operative degli agenti.

Quando possibile, il modello deve essere implementato utilizzando i meccanismi nativi di Hugo e strutture semplici come Markdown, front matter e YAML.

---

## 2. Entità principali

Il sistema comprende principalmente:

- articolo;
- autore;
- fonte;
- citazione;
- tema;
- area editoriale;
- lingua;
- traduzione;
- media;
- dataset.

Non tutte queste entità devono necessariamente diventare pagine autonome del sito.

La loro esistenza nel modello concettuale non implica automaticamente una specifica pagina pubblica.

---

## 3. Articolo

L'articolo è l'unità editoriale principale di StamoTenti.

Un articolo:

- affronta un problema, una domanda o un fenomeno;
- appartiene a una sotto-area editoriale;
- può essere associato a uno o più temi;
- può avere uno o più autori;
- può utilizzare una o più fonti;
- appartiene a una lingua;
- può avere una o più traduzioni;
- può essere collegato ad altri articoli.

L'articolo contiene il testo editoriale e i relativi metadata.

La struttura interna del testo è definita da ARTICLE-SPEC.md.

---

## 4. Area editoriale

Ogni articolo appartiene a una struttura editoriale composta da:

- macrotema;
- sotto-area.

Le macroaree e le sotto-aree sono definite esclusivamente in TO-BE.md.

Gli agenti non possono crearne di nuove o modificarne autonomamente la struttura.

Un articolo ha normalmente una sola sotto-area principale.

La classificazione editoriale principale non deve essere sostituita dai temi trasversali.

---

## 5. Temi

I temi sono classificazioni trasversali.

Un articolo può avere zero, uno o più temi.

I temi permettono di collegare contenuti appartenenti a differenti sotto-aree.

I temi non costituiscono automaticamente una gerarchia.

Il vocabolario dei temi è definito separatamente in VOCABULARY-SPEC.md.

Gli agenti devono utilizzare esclusivamente termini presenti nel vocabolario approvato.

---

## 6. Autore

Un autore è una persona o entità responsabile della produzione di un contenuto
editoriale o associata bibliograficamente a una fonte.

Per le fonti, il ruolo specifico della persona è una proprietà della relazione
con la fonte e non dell'identità generale della persona.

Gli autori sono identificati tramite un identificativo stabile.

Per gli articoli di StamoTenti l'autore editoriale è normalmente il proprietario
del progetto, salvo decisione editoriale esplicita diversa.

Il modello deve comunque poter rappresentare uno o più autori quando una
futura esigenza editoriale lo richieda.

Le informazioni dell'autore non devono essere duplicate all'interno degli
articoli o delle fonti quando possono essere richiamate dall'entità autore.

Un autore può essere associato a:

- uno o più articoli;
- una o più fonti.

La gestione dettagliata degli autori è definita in AUTHOR-SPEC.md.

---

## 7. Fonte

Una fonte è una risorsa bibliografica o documentale utilizzata per sostenere, approfondire o contestualizzare un contenuto.

Una fonte:

- possiede un identificativo stabile;
- è definita una sola volta;
- può essere utilizzata da più articoli;
- può avere uno o più autori;
- può contenere informazioni bibliografiche;
- può avere DOI, ISBN, URL o file associati quando disponibili.

La gestione dettagliata delle fonti è definita in SOURCE-SPEC.md.

Una fonte non deve essere duplicata perché utilizzata da articoli differenti.

---

## 8. Citazione

La citazione rappresenta l'utilizzo di una fonte all'interno di un articolo.

È importante distinguere:

Fonte:
il documento bibliografico esistente nel sistema.

Citazione:
il riferimento a quella fonte effettuato da uno specifico articolo.

Un articolo può citare più volte la stessa fonte.

Una fonte può essere citata da molti articoli.

La modalità di rappresentazione e rendering delle citazioni è definita in CITATION-SPEC.md.

---

## 9. Lingua

Ogni articolo appartiene a una lingua.

La lingua primaria del progetto è l'italiano.

L'inglese è la seconda lingua prevista.

La lingua è una proprietà editoriale del contenuto e non costituisce una categoria tematica.

---

## 10. Traduzione

Una traduzione è una versione linguistica dello stesso contenuto editoriale.

Le traduzioni:

- rappresentano lo stesso articolo concettuale;
- mantengono la stessa identità editoriale;
- possono avere titolo e testo differenti;
- appartengono a lingue differenti;
- devono poter essere collegate reciprocamente.

Una traduzione non deve essere trattata come un articolo indipendente ai fini della classificazione editoriale.

La gestione tecnica del multilingua è definita in MULTILINGUAL-SPEC.md.

---

## 11. Media

Un media è una risorsa associata a un contenuto.

Può comprendere, tra gli altri:

- immagini;
- fotografie;
- diagrammi;
- PDF;
- audio;
- video.

I media devono essere associati al contenuto quando il loro rapporto con esso è specifico.

La gestione dettagliata dei media è definita in MEDIA-SPEC.md.

---

## 12. Dataset

Un dataset è un'entità informativa distinta dal file che lo rappresenta e dalla fonte bibliografica che eventualmente lo descrive.

Un dataset:

- possiede un identificativo stabile;
- può essere associato a una o più fonti che lo descrivono;
- può essere associato a uno o più media che lo distribuiscono come file;
- può essere utilizzato da uno o più articoli.

La gestione dettagliata dei dataset è definita in DATASET-SPEC.md.

Un dataset non deve essere confuso né con la fonte che lo descrive né con il file che lo distribuisce.

---

## 13. Relazioni fondamentali

Le relazioni principali sono:

Le relazioni inverse devono essere derivate automaticamente quando il sistema
può farlo in modo affidabile.

Articolo → appartiene a → Area editoriale

Articolo → ha → Temi

Articolo → ha → Autori

Articolo → cita → Fonti

Articolo → appartiene a → Lingua

Articolo → ha → Traduzioni

Articolo → utilizza → Media

Articolo → utilizza → Dataset

Articolo → si collega a → altri articoli

Le relazioni inverse devono essere ottenute automaticamente quando possibile.

Per esempio, se un articolo utilizza una fonte, il sistema dovrebbe poter individuare gli articoli che utilizzano quella stessa fonte senza richiedere una seconda relazione mantenuta manualmente.

---

## 14. Relazioni tra articoli

Gli articoli possono essere collegati attraverso:

- stessa area editoriale;
- temi condivisi;
- fonti condivise;
- argomenti affini;
- approfondimenti;
- traduzioni.

I collegamenti automatici devono essere preferiti quando producono risultati sufficientemente affidabili.

I collegamenti editoriali espliciti possono essere utilizzati quando una relazione specifica è significativa e non può essere dedotta automaticamente.

Non deve essere introdotto un sistema complesso di grafi semantici senza una successiva decisione editoriale.

---

## 15. Identificativi

Le entità riutilizzabili devono possedere identificativi stabili.

Gli identificativi devono essere:

- semplici;
- leggibili;
- coerenti;
- stabili nel tempo;
- indipendenti dal titolo visualizzato.

La modifica del titolo di un contenuto non dovrebbe richiedere la modifica dell'identità dell'entità.

Gli identificativi non devono essere creati arbitrariamente in modi differenti dalle diverse parti del sistema.

Le regole specifiche per ciascuna entità possono essere definite nelle relative specifiche.

---

## 16. Metadata e contenuto

Il contenuto editoriale e i metadata devono rimanere concettualmente distinti.

Il testo dell'articolo appartiene al contenuto.

Informazioni come:

- titolo;
- data;
- lingua;
- area;
- temi;
- autori;
- stato;
- riferimenti;

appartengono ai metadata.

Hugo utilizza il front matter per rappresentare metadata e relazioni del contenuto.

La struttura definitiva dei campi del front matter sarà definita nelle specifiche appropriate.

Non devono essere introdotti nel testo dati che il sistema può rappresentare correttamente come metadata.

---

## 17. Tassonomie

Le tassonomie native di Hugo possono essere utilizzate per rappresentare classificazioni editoriali e temi quando risultano appropriate.

Non deve essere creato un sistema tassonomico parallelo se Hugo è sufficiente.

La classificazione editoriale principale e i temi trasversali devono comunque rimanere concettualmente distinti.

Una tassonomia tecnica non modifica la struttura editoriale definita da TO-BE.md.

---

## 18. Contenuti derivati

Il sistema può generare automaticamente pagine o liste derivate dalle relazioni tra contenuti.

Esempi:

- articoli di una determinata sotto-area;
- articoli associati a un tema;
- articoli associati a un autore;
- articoli che utilizzano una fonte;
- traduzioni disponibili;
- contenuti correlati.

Questi contenuti derivati non devono essere mantenuti manualmente quando possono essere generati in modo affidabile.

---

## 19. Principio di non duplicazione

Una stessa informazione deve essere mantenuta in un solo luogo quando può
essere rappresentata come entità riutilizzabile.

La non duplicazione riguarda soprattutto identità e metadata condivisi.
Non impedisce copie tecniche quando servono per backup, cache, distribuzione
o altre esigenze infrastrutturali.

In particolare:

- un autore non deve essere duplicato;
- una fonte non deve essere duplicata;
- un tema non deve essere duplicato con sinonimi;
- una traduzione non deve diventare un secondo articolo indipendente;
- una relazione derivabile non deve essere mantenuta manualmente senza necessità.

Questo principio riduce errori, incoerenze e costi di manutenzione.

---

## 20. Principio di semplicità

Il modello deve rappresentare soltanto relazioni che abbiano un'utilità editoriale o tecnica reale.

Quando Hugo può derivare una relazione in modo affidabile, la relazione non
deve essere duplicata manualmente. Questo vale in particolare per tassonomie,
contenuti correlati e relazioni multilingue.

Non devono essere introdotti:

- grafi semantici complessi;
- database;
- sistemi di alias generici o non necessari;
- ontologie;
- livelli gerarchici artificiali;
- relazioni duplicate;

quando il problema può essere risolto con una struttura più semplice.

La complessità può essere introdotta in futuro se la crescita del progetto ne dimostrerà la necessità.

---

## 21. Regola per gli agenti

Gli agenti devono considerare questo documento come il modello concettuale del
progetto.

Prima di introdurre una nuova entità o relazione devono preferire, nell'ordine:

1. riuso di un'entità esistente;
2. relazione derivata automaticamente;
3. meccanismo nativo di Hugo;
4. struttura semplice nei dati locali;
5. proposta di modifica architetturale quando nessuna delle soluzioni
   precedenti è sufficiente.

Prima di introdurre una nuova entità o relazione devono verificare se:

1. l'entità è già rappresentata;
2. la relazione può essere ottenuta automaticamente;
3. una struttura Hugo esistente è sufficiente;
4. la modifica è compatibile con TO-BE.md;
5. la modifica richiede una decisione architetturale.

Se la risposta all'ultima domanda è sì, l'agente deve fermarsi e proporre la modifica invece di introdurla autonomamente.

---

## 22. Gerarchia delle specifiche

In caso di conflitto:

1. TO-BE.md definisce la visione e i vincoli fondamentali;
2. CONTENT-MODEL.md definisce le entità e le relazioni;
3. le specifiche specialistiche definiscono il comportamento delle singole entità;
4. il codice implementa tali specifiche;
5. i contenuti devono rispettare il modello.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.
