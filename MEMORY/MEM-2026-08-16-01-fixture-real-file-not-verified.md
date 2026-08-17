# MEM-2026-08-16-01 — File reale non verificato allegato a una entry fixture

**Identificativo**: MEM-2026-08-16-01
**Tipo**: Errore (OPERATIONAL-MEMORY-SPEC.md §5, §12)
**Titolo**: File reale non verificato allegato a una entry fixture di `data/sources.yaml`
**Data**: 2026-08-16
**Origine**: audit richiesto dal proprietario; correzione eseguita su decisione esplicita del proprietario
**Stato**: attiva
**Livello di affidabilità**: pratica verificata (fatto realmente accaduto e realmente corretto in questo repository, non un'ipotesi)

---

## Contesto

Nel commit iniziale del repository (`3e52807`, "Initial project setup"), la entry `documento2026` in `data/sources.yaml` era una fixture tecnica con metadata palesemente placeholder (titolo "Documento di esempio", autore/anno generici, nessun `doi`/`isbn`/`url`), ma il suo campo `file:` puntava a `static/sources/01_Olivola.pdf`, un file reale (slide di un corso universitario, non open access). `static/` è storage pubblico e il repository è pubblico su GitHub: il materiale era di fatto distribuito pubblicamente senza che i diritti di redistribuzione fossero mai stati verificati.

## Contenuto

### Cosa è successo

La creazione della fixture ha unito in un solo passaggio (a) una entry di metadata palesemente sintetica e (b) un file binario reale non sintetico, senza che nulla nel processo o negli strumenti automatici segnalasse l'incoerenza tra i due.

### Perché non era stato previsto

`scripts/repository-doctor.py`, al momento, verificava l'esistenza dei file e l'integrità dei riferimenti incrociati, ma non la plausibilità/coerenza tra i metadata di una fonte e il fatto che avesse un file reale allegato. Nessun controllo tecnico o processuale collegava esplicitamente "metadata da fixture" a "rischio se accompagnati da un file reale".

### Cosa è stato imparato

Una entry con metadata palesemente placeholder (nessun `doi`/`isbn`/`url`) ma con un `file:` verso `static/` è un segnale affidabile di possibile disallineamento: è esattamente il pattern osservato qui — le altre 3 fonti fixture del repository, tutte senza `file:`, hanno invece almeno uno tra `doi`/`isbn`/`url` compilato. Questo pattern è stato tradotto in un controllo automatico (vedi "Quale modifica è stata effettuata").

### Quale modifica è stata effettuata

- File rimosso dal working tree e dalla storia locale (`git filter-repo --path static/sources/01_Olivola.pdf --invert-paths`); storia riscritta e ripubblicata dal proprietario con force-push (hash radice `3e52807` → `35d406a`).
- Campo `file:` rimosso dalla entry `documento2026` in `data/sources.yaml` (mantenuta come fixture `type: report` senza file allegato).
- Aggiunto un controllo WARNING (non bloccante) in `scripts/repository-doctor.py`: segnala ogni entry di `data/sources.yaml` con un `file:` compilato ma priva di `doi`/`isbn`/`url` — vedi commit successivo a questa nota.

## Collegamenti

- Commit di rimozione: `remove non-open-access PDF (course slides) and its file reference`
- `DECISIONS/DR-05-dataset-visibility-proposal.md`, `DECISIONS/DR-06-frontmatter-classification-linking-proposal.md` (decisioni approvate nella stessa sessione, non direttamente collegate a questo errore ma coeve)
- `AGENTS.md` (regola preesistente: "I PDF di lavoro privati non devono essere inseriti in `static/`" — regola già scritta, non rispettata in questo caso specifico)
- `MEDIA-SPEC.md` §7 ("un media non deve essere inserito nello storage pubblico semplicemente perché è tecnicamente possibile farlo")
