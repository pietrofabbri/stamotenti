# StamoTenti — TO-BE

## 1. Visione

StamoTenti è una biblioteca editoriale digitale dedicata alla meditazione, alla consapevolezza, all'attenzione e ai fenomeni ad esse collegati.

Il progetto esplora questi temi attraverso tre prospettive complementari:

1. Scienza & Neuroscienze — la dimensione empirica;
2. Filosofia & Storia — la dimensione concettuale;
3. Critica, Società & Educazione — la dimensione applicata e sistemica.

StamoTenti non è un semplice blog sulla meditazione.

L'obiettivo è costruire nel tempo un patrimonio di contenuti rigorosi, accessibili e interconnessi, capace di mettere in dialogo esperienza contemplativa, psicologia, neuroscienze, filosofia, storia, educazione, società, cultura ed etica.

Il progetto deve essere comprensibile a chi si avvicina per la prima volta a questi argomenti, senza rinunciare alla possibilità di approfondire gli aspetti scientifici, filosofici e accademici.

---

## 2. Principio editoriale

Gli articoli devono svolgere contemporaneamente due funzioni.

### Livello divulgativo

La prima parte deve essere comprensibile a un lettore interessato ma privo di formazione specialistica.

Deve:

- introdurre il problema;
- spiegare i concetti fondamentali;
- fornire esempi concreti;
- evitare il gergo non necessario;
- mantenere rigore e precisione;
- distinguere fatti, interpretazioni e ipotesi.

Il lettore deve poter comprendere il fenomeno senza conoscere preventivamente la letteratura specialistica.

### Livello tecnico e accademico

L'articolo deve poter offrire un approfondimento per lettori dotati degli strumenti necessari.

Questa parte può comprendere:

- terminologia specialistica;
- teorie;
- metodologia degli studi;
- risultati sperimentali;
- discussione della letteratura;
- limiti delle evidenze;
- controversie;
- studi originali;
- review;
- meta-analisi;
- riferimenti bibliografici.

La parte tecnica deve aggiungere profondità e non limitarsi a ripetere la parte divulgativa in forma più complessa.

---

## 3. Architettura editoriale

La classificazione principale è costituita da macrotemi e sotto-temi.

Questa struttura è controllata editorialmente e non deve essere modificata autonomamente dagli agenti.

### 3.1 Scienza & Neuroscienze

**La dimensione empirica**

#### 3.1.1 Psicologia Cognitiva dell'Attenzione e Metacognizione

Studio della mente dal punto di vista psicologico.

Comprende, tra gli altri:

- attenzione;
- mind wandering;
- dialogo interiore;
- metacognizione;
- flessibilità cognitiva;
- capacità della mente di osservare i propri processi.

#### 3.1.2 Fisiologia Integrata e PNEI

Studio delle relazioni mente-corpo e degli aspetti fisiologici associati alle pratiche contemplative.

Comprende, tra gli altri:

- sistema nervoso autonomo;
- regolazione fisiologica;
- tono vagale;
- stress;
- biologia della calma;
- invecchiamento cellulare;
- epigenetica.

Gli articoli devono mantenere particolare attenzione alla qualità e ai limiti delle evidenze scientifiche.

#### 3.1.3 Psicologia degli Stati Profondi

Studio empirico e psicologico di particolari stati di esperienza e coscienza.

Comprende, tra gli altri:

- flow;
- assorbimento;
- concentrazione profonda;
- insight;
- iper-focus;
- stati di coscienza non ordinari.

### 3.2 Filosofia & Storia

**La dimensione concettuale**

#### 3.2.1 Filosofia Comparata e Interculturale

Confronto rigoroso tra tradizioni e correnti differenti.

Esempi:

- Stoicismo e Buddhismo;
- Esistenzialismo e non-dualità;
- pratiche monastiche occidentali e meditazione orientale.

I confronti devono evitare semplificazioni arbitrarie o equivalenze artificiali.

#### 3.2.2 Filosofia del Linguaggio, del Silenzio e del Paradosso

Comprende:

- ineffabile;
- silenzio;
- linguaggio;
- paradosso;
- Koan;
- teologia apofatica;
- Wu Wei;
- agire senza sforzo.

#### 3.2.3 Tra Tradizione e Modernità

Studio della trasformazione delle pratiche contemplative nel passaggio dalle tradizioni antiche e dai contesti rituali alla modernità, alla secolarizzazione e alla società contemporanea.

### 3.3 Critica, Società ed Educazione

**La dimensione applicata e sistemica**

#### 3.3.1 Pedagogia ed Educazione Contemplativa

Comprende:

- pratiche contemplative nell'educazione;
- scuole;
- università;
- apprendimento esperienziale;
- attenzione;
- formazione del pensiero critico.

#### 3.3.2 Ecologia dell'Attenzione e Società Digitale

Studio del rapporto tra attenzione, tecnologia e società.

Comprende:

- economia dell'attenzione;
- media digitali;
- distrazione;
- iperconnessione;
- presenza mentale;
- rapporto tra individuo e ambiente informativo.

#### 3.3.3 Critica Culturale, Etica e "Lato Oscuro"

Affronta criticamente:

- mercificazione della meditazione;
- McMindfulness;
- trasformazione delle pratiche contemplative in prodotti;
- effetti psicologici avversi;
- limiti delle pratiche;
- responsabilità etiche;
- rischi di semplificazione o appropriazione.

---

## 4. Temi trasversali

Gli articoli possono essere associati a temi trasversali.

I temi servono a classificare i contenuti e a favorire il collegamento tra articoli appartenenti a differenti aree editoriali.

Un tema non costituisce un'entità autonoma e non richiede un sistema separato di relazioni semantiche.

Un articolo può quindi appartenere a una determinata sotto-area e condividere uno o più temi con articoli appartenenti ad altre sotto-aree.

Esempio:

```yaml
temi:

  - attenzione
  - mind-wandering
  - metacognizione
```
Il tema "attenzione" può quindi collegare articoli di psicologia cognitiva, ecologia dell'attenzione, educazione contemplativa o filosofia.

La classificazione deve essere semplice e utilizzabile automaticamente dal sistema.

---

## 5. Vocabolario controllato

I temi utilizzati negli articoli devono appartenere a un vocabolario editoriale controllato.

Gli agenti:

- possono utilizzare temi già esistenti;
- non devono creare autonomamente nuove varianti;
- non devono introdurre sinonimi arbitrari;
- non devono creare alias;
- non devono modificare autonomamente il vocabolario.

Se un nuovo articolo richiede un tema non rappresentabile adeguatamente dai termini esistenti, l'agente deve segnalarlo come proposta senza modificare autonomamente il sistema.

Il vocabolario può essere modificato solo attraverso una decisione editoriale esplicita.

---

## 6. Relazioni tra contenuti

Gli articoli devono poter essere collegati attraverso:

- macrotema;
- sotto-tema;
- temi condivisi;
- autori;
- fonti;
- lingua e traduzioni.

Quando possibile, le relazioni devono essere generate automaticamente dal sistema invece di essere mantenute manualmente.

Il progetto deve preferire i meccanismi nativi di Hugo rispetto a sistemi personalizzati quando questi sono sufficienti.

---

## 7. Articoli

Un articolo deve:

1. affrontare un problema, una domanda o un fenomeno riconoscibile;
2. essere comprensibile al lettore generale;
3. essere rigoroso;
4. distinguere evidenza e interpretazione;
5. utilizzare fonti adeguate;
6. offrire, quando pertinente, un approfondimento tecnico;
7. essere classificato secondo la struttura editoriale;
8. poter essere collegato ad altri contenuti.

La struttura tecnica dettagliata degli articoli sarà definita in una specifica separata.

---

## 8. Fonti

Le fonti sono entità indipendenti dagli articoli.

Una fonte deve essere definita una sola volta e può essere utilizzata da più articoli.

Gli articoli devono referenziare le fonti attraverso il sistema bibliografico previsto dal progetto.

Non devono essere duplicate fonti già esistenti.

Gli agenti non devono inventare informazioni bibliografiche.

---

## 9. Autori

Gli autori sono entità riutilizzabili.

Gli articoli e le fonti devono utilizzare gli identificativi degli autori definiti dal sistema, evitando di duplicare manualmente le informazioni.

---

## 10. Multilingua

StamoTenti è progettato per supportare almeno:

- italiano;
- inglese.

Le versioni linguistiche dello stesso articolo rappresentano lo stesso contenuto editoriale.

Una traduzione non costituisce un nuovo articolo indipendente.

L'italiano costituisce la lingua primaria del progetto.

L'assenza di una traduzione inglese non deve impedire la pubblicazione della versione italiana.

Il sistema deve utilizzare le funzionalità multilingua native di Hugo.

---

## 11. Architettura tecnica

Hugo deve rimanere il motore principale di generazione del sito.

Il flusso fondamentale è:

contenuto Markdown + metadata
→ Hugo
→ template
→ HTML
→ sito pubblicato

Il progetto deve mantenere un'architettura semplice, leggibile, portabile e facilmente modificabile.

Non devono essere introdotti database, backend o servizi esterni quando una soluzione basata su Hugo, Markdown, YAML o semplici script è sufficiente.

---

## 12. Vincoli per gli agenti

Gli agenti operano all'interno dell'architettura definita da questo documento.

Non possono autonomamente:

- cambiare macrotemi;
- cambiare sotto-temi;
- creare nuove strutture editoriali;
- introdurre nuovi sistemi di classificazione;
- creare un database;
- sostituire Hugo;
- introdurre framework non necessari;
- modificare arbitrariamente il modello bibliografico;
- creare duplicati;
- modificare autonomamente il vocabolario dei temi.

Quando una richiesta sembra richiedere una modifica architetturale o editoriale non prevista, l'agente deve segnalarla come decisione da sottoporre al proprietario del progetto.

---

## 13. Principio di evoluzione

StamoTenti deve essere progettato per poter crescere senza richiedere una complessità prematura.

Le funzionalità non necessarie all'attuale scala del progetto non devono essere introdotte anticipatamente.

In particolare, sistemi semantici avanzati, grafi di concetti, alias complessi, database o automazioni sofisticate potranno essere introdotti in futuro solo quando la quantità e la complessità dei contenuti ne giustificheranno l'utilità.

La semplicità dell'architettura attuale non deve impedire un'evoluzione futura.