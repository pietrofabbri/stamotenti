# StamoTenti — Piano Fasi 3-5 (contenuti e automazione editoriale)

**Stato**: documento di lavoro persistente, non un documento fondativo (non è nell'elenco BASELINE.md dei documenti "mai modificabili autonomamente" — è un piano tecnico, aggiornabile man mano che si procede, analogo per natura a `DECISIONS/`/`MEMORY/`/`PHASE-2-PLAN.md` ma con funzione di piano macro anziché di tracker di tranche, dato che nessuna delle fasi qui descritte è ancora iniziata).

**Origine**: `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` dichiara esplicitamente di coprire solo le Fasi 0-2 e chiude con "Da questo punto inizia la roadmap dei contenuti e dell'automazione editoriale" — una roadmap futura, non ancora scritta al momento della chiusura del Gate 2 (`MEMORY/MEM-2026-08-19-01-gate2-approved-phase2-closed.md`). Questo documento registra il piano macro concordato con il proprietario in sessione (2026-08-20) per colmare quel vuoto, allo stesso livello di dettaglio con cui `PHASE-2-PLAN.md` ha registrato il piano della Fase 2.

**Cosa NON è questo documento**: non è un'autorizzazione a iniziare l'esecuzione della Fase 3. `CLAUDE.md` è esplicito — "Non iniziare autonomamente la fase successiva" — e questo vale anche qui: il piano macro è concordato, ma l'esecuzione di ciascun passo della Fase 3 richiederà comunque un'istruzione esplicita separata. Non è nemmeno un elenco di decisioni di contenuto: non propone un vocabolario Topic, non propone un font, non propone una sotto-area o un argomento per il primo articolo. Descrive il **processo** concordato, non i contenuti.

---

## Fase 3 — "Primo contenuto reale end-to-end"

### Obiettivo

Dimostrare l'intero processo editoriale su un primo contenuto **reale**, non una fixture tecnica (quelle esistono già, `content/fixtures/`, e hanno dimostrato che il modello dei contenuti funziona meccanicamente — DECISIONS/DR-08). La Fase 3 dimostra che il modello funziona anche nella pratica editoriale reale, con un articolo che sarà effettivamente pubblicato.

### Approccio concordato

- **Nessuna decisione preventiva separata sul vocabolario `data/topics.yaml`**. DR-04 (Approvata, Fase 1B) ha già stabilito lo schema tecnico del file (`id`/`label_it`/`label_en`/`description`/`status`/`notes`) e il vincolo "zero temi reali senza processo editoriale di approvazione separato" — questo resta valido. Ma non si fa, prima di scrivere il primo articolo, un esercizio a tavolino per popolare un vocabolario completo di temi: si parte con l'articolo, e i temi che servono davvero emergono da lì.
- **Si parte con un primo articolo reale, semi-automatizzato**: scritto con assistenza tecnica, ma con supervisione e approvazione del proprietario passo per passo — non un processo che produce un articolo pubblicato senza intervento umano nel mezzo (questo resta comunque il vincolo generale di `APPROVAL-SPEC.md`/`CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` su tutta la fase).
- **Si itera passo per passo**, non con un piano dettagliato scritto in anticipo per l'intero processo editoriale.
- **Solo dopo** — non prima — le azioni che si rivelano funzionare bene su questo primo articolo (e sui successivi) vengono codificate come linee guida per gli articoli che seguiranno. Le linee guida derivano dalla pratica osservata, non da una progettazione teorica preventiva.
- **D4 (font definitivo) resta rimandato**, coerente con la decisione già presa in Fase 2 (`PHASE-2-PLAN.md`, riga D4: "il font sarà riconsiderato quando si affronterà come presentare i primi contenuti reali"). Concordato ora, più precisamente: non al primo articolo, ma **dopo qualche articolo** — quando ci sarà contenuto reale sufficiente per valutare la scelta nel contesto in cui verrà effettivamente usata, non in astratto.

### Cosa non è ancora deciso (e non viene deciso da questo documento)

Quale sotto-area, quale argomento, quale titolo per il primo articolo; il vocabolario Topic; il font definitivo; il grado esatto di automazione del processo "semi-automatizzato"; quante iterazioni servano prima di considerare il processo "validato". Tutte queste sono decisioni del proprietario, da prendere quando si arriverà a quel punto, non da questo piano macro.

### Rischi residui ereditati dalla Fase 2, rilevanti per questa fase

- **#18** (`PHASE-2-PLAN.md`): le pagine di termine taxonomy delle entità fixture e `/sotto_area/sa-1-1/` restano indicizzabili — quest'ultima potrebbe risolversi da sé quando arriverà un primo articolo reale classificato in una sotto-area (non necessariamente `SA-1-1`), come già previsto nella decisione che ha accettato quel rischio.
- **#10** (`PHASE-2-PLAN.md`): la decisione se includere date tecniche nel JSON-LD è rimasta aperta proprio in attesa di un contenuto reale con una data editoriale deliberata — il primo articolo di questa fase è verosimilmente il momento naturale in cui questa domanda tornerà rilevante.
- **#17** (`PHASE-2-PLAN.md`): il collegamento diretto Article→Media resta indiretto — rilevante solo se il primo articolo reale userà un Media.
