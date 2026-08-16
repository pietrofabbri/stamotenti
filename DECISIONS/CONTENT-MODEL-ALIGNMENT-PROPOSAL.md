# Proposta di allineamento — CONTENT-MODEL.md

**Stato**: Approvata e implementata
**Data approvazione/implementazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation
**Origine**: emerso durante l'analisi per DR-02 (Dataset ↔ Source ↔ Media)

## Esito dell'implementazione

Applicata come descritta di seguito, senza estensioni: §2 estesa da 8 a 10 voci (aggiunte `dataset` e `citazione`); nuova §12 "Dataset" inserita dopo l'ex §11 "Media"; sezioni successive rinumerate meccanicamente (ex §12→§13 … ex §21→§22, nessun contenuto alterato oltre al numero); §13 "Relazioni fondamentali" (ex §12) integrata con la riga `Articolo → utilizza → Dataset`. §8 "Citazione" non modificata nel contenuto, solo referenziata da §2 come già previsto dalla proposta. `DEPENDENCY-MAP.md` aggiornato aggiungendo `DATASET-SPEC.md` alle dipendenze di `CONTENT-MODEL.md` (unica modifica necessaria, come previsto al punto 3 della proposta originale). L'aggiunta opzionale a §18 "Contenuti derivati" (ex §17), segnalata come puramente esemplificativa nella proposta originale, non è stata applicata per mantenere il diff minimo.

---

## Problema osservato

CONTENT-MODEL.md §2 ("Entità principali") elenca: articolo, autore, fonte, tema, area editoriale, lingua, traduzione, media. **Dataset non compare in nessuna sezione del documento** (verificato leggendo il file per intero). **Citazione compare in §8** come concetto distinto da Fonte, ma non è inclusa nell'elenco di §2 — un'incoerenza interna al documento stesso, non solo un gap verso le SPEC specialistiche.

Questa proposta **non modifica CONTENT-MODEL.md**. Elenca solo cosa cambierebbe, per approvazione esplicita separata.

## 1. Quali entità aggiungere

- **Dataset**: da aggiungere all'elenco di §2 e da descrivere in una nuova sezione dedicata (posizione suggerita: dopo l'attuale §11 "Media", prima di §12 "Relazioni fondamentali"), riprendendo — senza inventare nuove regole — la distinzione già approvata in DR-02: Dataset come oggetto informativo distinto da Source (riferimento bibliografico) e da Media (file/distribuzione), con riferimenti opzionali alle altre due entità tramite ID.
- **Citazione**: da aggiungere esplicitamente all'elenco di §2 per coerenza con la sezione §8 già esistente (che già la tratta come concetto di prima classe, distinto da Fonte). Nessun contenuto nuovo da scrivere: §8 già descrive correttamente la citazione, servirebbe solo includerla nell'elenco introduttivo.

## 2. Quali sezioni aggiornare

- **§2 Entità principali**: estendere l'elenco da 8 a 10 voci (aggiungendo dataset e citazione).
- **§8 Citazione**: nessuna modifica di contenuto necessaria, solo referenziata da §2.
- **Nuova sezione Dataset** (numerazione da assegnare in sede di modifica, es. §11-bis o rinumerazione da §12 in poi): stessa struttura delle sezioni esistenti per Fonte (§7) e Media (§11) — cosa è, come si relaziona alle altre entità, rimando a DATASET-SPEC.md per la gestione dettagliata (stesso pattern usato per tutte le altre entità, es. "La gestione dettagliata delle fonti è definita in SOURCE-SPEC.md").
- **§12 Relazioni fondamentali**: aggiungere una riga `Articolo → utilizza → Dataset` (opzionale, sul modello di `Articolo → utilizza → Media`, già presente).
- **§17 Contenuti derivati**: eventualmente aggiungere "dataset utilizzati da un articolo" alla lista di esempi già presente (opzionale, valore puramente esemplificativo, non normativo).

## 3. Quali dipendenze cambiano

Secondo DEPENDENCY-MAP.md, oggi la dipendenza è **unidirezionale**: DATASET-SPEC.md → CONTENT-MODEL.md (DATASET-SPEC dipende da CONTENT-MODEL, non il contrario). Se Dataset viene aggiunto a CONTENT-MODEL §2, coerenza richiederebbe che DEPENDENCY-MAP.md registri anche **CONTENT-MODEL.md → DATASET-SPEC.md**, analogamente a come CONTENT-MODEL.md già dipende oggi da ARTICLE-SPEC, AUTHOR-SPEC, CITATION-SPEC, MEDIA-SPEC, MULTILINGUAL-SPEC, SOURCE-SPEC, TO-BE, VOCABULARY-SPEC (CITATION-SPEC è già presente in questo elenco, quindi per Citazione non servirebbe alcun cambiamento di dipendenza — solo l'allineamento testuale in §2).

**Nessuna modifica a DEPENDENCY-MAP.md è stata fatta**: anche questo resta oggetto di approvazione separata, coerente con "nessuna nuova regola" — si tratta di rendere esplicita una relazione già di fatto presente nel contenuto dei documenti, non di crearne una nuova.

## 4. Nessuna nuova regola

Questa proposta non introduce alcun vincolo, requisito o comportamento nuovo. Riguarda esclusivamente:
- allineamento testuale/di elenco (§2) rispetto a contenuto già esistente nel documento (§8) o già deciso altrove (DR-02);
- una sezione descrittiva per Dataset con lo stesso formato già usato per le altre 8 entità, senza inventare regole diverse da quelle già approvate in DATASET-SPEC.md e in DR-02;
- l'aggiunta di una singola riga relazionale (§12) analoga a una già esistente;
- l'aggiornamento di un riferimento di dipendenza in DEPENDENCY-MAP.md per riflettere una relazione testuale già presente.

## Domanda aperta per l'utente

Aggiungere Dataset e Citazione a CONTENT-MODEL §2 è di per sé una modifica a un documento fondativo (CONTENT-MODEL.md è esplicitamente elencato in BASELINE.md tra i documenti "mai modificabili autonomamente"). Questa proposta è pronta per essere implementata **solo su tua esplicita approvazione e solo da te o su tuo mandato diretto** — nessun agente procederà autonomamente, coerente con CHANGE-MANAGEMENT-SPEC §5 che classifica "modifica del modello dei contenuti" come modifica significativa.
