# DR-03 — Macroarea ↔ Sotto-area Machine-readable Model

**Stato**: Approvata (completa: struttura + ID tecnici + slug)
**Data approvazione**: 2026-08-16 (struttura); confermata con ID/slug il 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation

---

## Decisione

Approvata l'alternativa **A — file dati puramente derivato** da TO-BE.md §3: `data/editorial-areas.yaml`, rappresentazione machine-readable di macroaree e sotto-aree, derivata esclusivamente dal testo già approvato in TO-BE.md §3, **senza inventare nuovi valori editoriali**.

Gli ID tecnici e gli slug proposti in `DR-03-sottoarea-slug-proposal.md` sono stati **approvati esattamente come proposti** (regola: lowercase, ASCII, kebab-case, nessuna rimozione di stopword, nessun troncamento). I titoli restano verbatim rispetto a TO-BE.md §3. Il file `data/editorial-areas.yaml` è stato creato con questi valori.

## Contesto

Macroaree e sotto-aree esistevano solo come prosa in TO-BE.md §3, senza rappresentazione machine-readable né una entry propria in DEPENDENCY-MAP.md, pur essendo richieste come "contenitore tecnico" dalla Fase 1 della roadmap.

## SPEC coinvolte

- TO-BE.md §3 (unica fonte, gerarchia chiusa: 3 macroaree × 3 sotto-aree, "controllata editorialmente, non modificabile autonomamente dagli agenti").
- CONTENT-MODEL.md §4 (area editoriale = macrotema + sotto-area, "definite esclusivamente in TO-BE.md"), §17 (la taxonomy Hugo non sostituisce la struttura editoriale), §15 (identificatori indipendenti dal titolo).
- ARTICLE-SPEC.md §20 (classificazione non modificabile autonomamente).

## Vincoli già approvati

- "Le macroaree e le sotto-aree sono definite esclusivamente in TO-BE.md. Gli agenti non possono crearne di nuove o modificarne autonomamente la struttura" (CONTENT-MODEL §4).
- Un articolo ha "normalmente una sola sotto-area principale" (CONTENT-MODEL §4).

## Contenuto esatto già approvato in TO-BE.md §3 (riportato senza modifiche)

| Macroarea (TO-BE §) | Sotto-area (TO-BE §) |
|---|---|
| 3.1 Scienza & Neuroscienze — "la dimensione empirica" | 3.1.1 Psicologia Cognitiva dell'Attenzione e Metacognizione |
| | 3.1.2 Fisiologia Integrata e PNEI |
| | 3.1.3 Psicologia degli Stati Profondi |
| 3.2 Filosofia & Storia — "la dimensione concettuale" | 3.2.1 Filosofia Comparata e Interculturale |
| | 3.2.2 Filosofia del Linguaggio, del Silenzio e del Paradosso |
| | 3.2.3 Tra Tradizione e Modernità |
| 3.3 Critica, Società & Educazione — "la dimensione applicata e sistemica" | 3.3.1 Pedagogia ed Educazione Contemplativa |
| | 3.3.2 Ecologia dell'Attenzione e Società Digitale |
| | 3.3.3 Critica Culturale, Etica e "Lato Oscuro" |

Nessun titolo qui riportato è modificato rispetto a TO-BE.md.

## Alternative considerate

- **A — File dati puramente derivato** (SCELTA APPROVATA, completa con ID/slug).
- **B — Nessun file dati** (non scelta): stringa libera nel front matter, zero validazione possibile — scartata perché non soddisfa il criterio "contenitore tecnico" della Fase 1.
- **C — Taxonomy Hugo dedicata senza data file** (non scelta): scartata perché richiederebbe modifica a `hugo.toml` (fuori scope di questa decisione) e rischierebbe di far diventare la taxonomy la fonte di verità de facto, in tensione con CONTENT-MODEL §17.

## Conseguenze

**Vantaggi**: rende la classificazione validabile automaticamente in futuro (stesso pattern già introdotto in Fase 1A per authors/sources in `repository-doctor.py`); riduce il rischio di typo/varianti nel front matter.

**Rischi/limiti accettati**: assegnare ID/slug è di per sé una micro-decisione tecnica-editoriale che richiede un passaggio di approvazione separato (vedi sotto-proposta) prima di poter scrivere il file definitivo.

## Impatto su Hugo

Nessuno in questa decisione: il file dati è indipendente da Hugo. Un'eventuale esposizione tramite taxonomy Hugo (`hugo.toml`) resta una decisione tecnica successiva, non autorizzata qui.

## Impatto sul contenuto futuro

I nuovi articoli potranno in futuro referenziare la sotto-area tramite ID stabile (`data/editorial-areas.yaml`) invece che tramite testo libero — nessun contenuto reale è stato modificato in questa decisione per farne uso: il collegamento nel front matter di Article resta un punto aperto (vedi DR-01, "Condizioni di rivalutazione").

## Reversibilità

Alta per la struttura del file (rimovibile/ristrutturabile senza impatti su altre entità). Gli ID e gli slug sono ora canonizzati per decisione esplicita: una loro modifica futura richiederebbe una nuova decisione, non una semplice correzione tecnica.

## Note di implementazione

**Implementato in questa tranche**: `data/editorial-areas.yaml` è stato creato con le 3 macroaree e le 9 sotto-aree, ID e slug esattamente come approvati in `DR-03-sottoarea-slug-proposal.md`. Non è stata fatta alcuna modifica a `hugo.toml` o ai template (nessuna taxonomy, nessuna pagina pubblica collegata a questi dati in questa tranche).

## Condizioni di rivalutazione

Da rivalutare se TO-BE.md §3 venisse modificato in futuro con una decisione editoriale esplicita (nuove/modificate macroaree o sotto-aree) — in tal caso questa decisione e il file dati derivato andrebbero aggiornati di conseguenza.
