# DR-03 — Sotto-proposta: ID tecnici e slug per macroaree/sotto-aree

**Stato**: Approvata
**Data approvazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Allegata a**: DR-03-macroarea-sottoarea-model.md
**Fase**: 1B — Site Foundation

---

Questa sotto-proposta esisteva perché DR-03 richiedeva che ID tecnici e slug fossero approvati separatamente prima di scrivere il file definitivo. **Approvata esattamente come proposta di seguito**, senza modifiche. I valori sono ora scritti in `data/editorial-areas.yaml`.

## Regola di derivazione dello slug (dichiarata esplicitamente, meccanica e verificabile)

1. Minuscolo.
2. Sostituzione lettere accentate: à→a, è/é→e, ì→i, ò→o, ù→u.
3. L'apostrofo (`'`) è trattato come separatore di parola (→ trattino).
4. Ogni carattere non alfanumerico (spazi, virgole, `&`, virgolette) è sostituito con un trattino.
5. Trattini consecutivi collassati in uno solo; trattini iniziali/finali rimossi.

Questa regola **non rimuove parole** (articoli, preposizioni, congiunzioni) per restare massimamente letterale e verificabile riga per riga contro il titolo originale — è una scelta di semplicità, non un giudizio editoriale. Uno schema alternativo che rimuove le stopword (es. "e", "del", "dell'") è possibile ma produrrebbe slug più corti e meno univocamente derivabili dal titolo; non è stato applicato qui.

## Regola di derivazione dell'ID tecnico

ID indipendente dal titolo (richiesto da CONTENT-MODEL §14), basato sulla posizione strutturale in TO-BE.md §3 (non sul testo del titolo, che potrebbe cambiare):

- Macroarea: `MA-<n>` dove `<n>` è 1, 2, 3 nell'ordine di TO-BE.md §3.1–3.3.
- Sotto-area: `SA-<macroarea>-<n>` dove `<macroarea>` è il numero della macroarea genitrice e `<n>` è la posizione della sotto-area al suo interno (1–3).

Alternativa non scelta qui ma segnalata: ID sequenziale piatto `SA-01`…`SA-09` indipendente dal raggruppamento per macroarea — più semplice ma perde la gerarchia nell'ID stesso.

## Macroaree — tabella proposta

| ID tecnico | Slug proposto | Titolo canonico (TO-BE §) |
|---|---|---|
| MA-1 | `scienza-neuroscienze` | Scienza & Neuroscienze (§3.1) |
| MA-2 | `filosofia-storia` | Filosofia & Storia (§3.2) |
| MA-3 | `critica-societa-educazione` | Critica, Società & Educazione (§3.3) |

## Sotto-aree — tabella proposta

| § TO-BE | ID tecnico | Slug proposto | Titolo canonico | Macroarea (parent) |
|---|---|---|---|---|
| 3.1.1 | SA-1-1 | `psicologia-cognitiva-dell-attenzione-e-metacognizione` | Psicologia Cognitiva dell'Attenzione e Metacognizione | MA-1 |
| 3.1.2 | SA-1-2 | `fisiologia-integrata-e-pnei` | Fisiologia Integrata e PNEI | MA-1 |
| 3.1.3 | SA-1-3 | `psicologia-degli-stati-profondi` | Psicologia degli Stati Profondi | MA-1 |
| 3.2.1 | SA-2-1 | `filosofia-comparata-e-interculturale` | Filosofia Comparata e Interculturale | MA-2 |
| 3.2.2 | SA-2-2 | `filosofia-del-linguaggio-del-silenzio-e-del-paradosso` | Filosofia del Linguaggio, del Silenzio e del Paradosso | MA-2 |
| 3.2.3 | SA-2-3 | `tra-tradizione-e-modernita` | Tra Tradizione e Modernità | MA-2 |
| 3.3.1 | SA-3-1 | `pedagogia-ed-educazione-contemplativa` | Pedagogia ed Educazione Contemplativa | MA-3 |
| 3.3.2 | SA-3-2 | `ecologia-dell-attenzione-e-societa-digitale` | Ecologia dell'Attenzione e Società Digitale | MA-3 |
| 3.3.3 | SA-3-3 | `critica-culturale-etica-e-lato-oscuro` | Critica Culturale, Etica e "Lato Oscuro" | MA-3 |

## Punti confermati (già aperti, ora risolti dall'approvazione)

1. **Schema ID**: confermato `MA-n` / `SA-m-n` come proposto, nessuna alternativa adottata.
2. **Regola slug**: confermata "letterale senza rimozione stopword" (lowercase, ASCII, kebab-case), nessuna alternativa più breve adottata.
3. **Lunghezza slug**: confermato nessun troncamento — gli slug lunghi (es. SA-1-1) restano come proposti, nessun limite di lunghezza introdotto.

Tutti i valori di questa tabella sono ora scritti in `data/editorial-areas.yaml`, esattamente come qui riportati.
