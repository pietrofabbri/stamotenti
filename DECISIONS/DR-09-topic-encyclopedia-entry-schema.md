# DR-09 — Topic Encyclopedia Entry Schema and Public Page Mechanism

**Stato**: Approvata
**Data proposta**: 2026-09-07
**Data approvazione**: 2026-09-07 (comunicata via `stamotenti-editorial/enciclopedia/approvazione-dr09-2026-09-06.md`; quel file riporta la data del canale Cowork come 2026-09-06 — segnalata la discrepanza, non corretta silenziosamente — e usa qui la data non precedente a "Data proposta", come richiesto dallo stesso file)
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation
**Origine**: primo tema reale proposto tramite processo editoriale (5 voci enciclopediche, `stamotenti-editorial/enciclopedia/voci/*.md`, revisionate e approvate dal proprietario); handoff "prima integrazione tecnica dell'enciclopedia", 2026-09-06.

## Nota sull'approvazione

Approvati entrambi i punti aperti così come proposti (schema `voce_enciclopedica` a campo singolo; meccanismo a tassonomia Hugo nativa). Durante l'approvazione era emersa una riserva del proprietario sul punto 2 ("eviterei tassonomie, le voci enciclopediche possono essere molto trasversali"), risolta chiarendo che è vero il contrario: una tassonomia Hugo aggrega automaticamente qualunque articolo citi il tema, indipendentemente da dove l'articolo vive nel sito — più trasversale dell'alternativa scartata (`content/enciclopedia/`), non meno. Il ragionamento era già scritto per esteso nella sezione "Alternative considerate" sotto; nessuna modifica al testo della decisione è stata necessaria per questo scambio.

---

## Correzione preliminare a una premessa dell'handoff

L'handoff che origina questa DR afferma che il campo `temi` nel front matter di Article è "oggi escluso da DR-01 proprio in attesa di questo momento", e cita la clausola "Condizioni di rivalutazione" di DR-04 (2026-08-16) secondo cui `temi` sarebbe "escluso da DR-01 finché questa decisione non è a sua volta implementata".

Questo era vero al momento in cui DR-04 è stata scritta, ma non lo è più: **DR-01 è stata estesa lo stesso giorno** (2026-08-16, sezione "Estensione — 2026-08-16" del documento), a valle dell'approvazione di `DECISIONS/DR-06-frontmatter-classification-linking-proposal.md`. `temi` è oggi già un campo opzionale del contratto front matter di Article, con cardinalità lista-di-id già motivata da DR-06. `scripts/repository-doctor.py` valida già ogni valore di `temi` contro `data/topics.yaml` (sezione "15. sotto_area / temi cross-reference (DR-06)").

Le "Condizioni di rivalutazione" di DR-04 non sono state aggiornate dopo l'estensione di DR-01, ed è per questo che l'handoff — basandosi su quel testo — descrive come aperto un punto già chiuso.

**Conseguenza per lo scope di questa DR**: il punto 2 dell'handoff ("il campo `temi` ... va aggiunto [a DR-01] prima che qualunque articolo possa taggare un tema") **non richiede alcuna azione**: il campo esiste già, con lo schema corretto. Questa DR non modifica DR-01. Aggiorna invece la clausola di rivalutazione di DR-04, che è la parte effettivamente obsoleta.

Questa DR si occupa quindi solo dei due punti dell'handoff che sono realmente aperti:

1. lo schema `voce_enciclopedica` in `data/topics.yaml` (nessuno schema esistente lo copre);
2. dove vivono tecnicamente le pagine pubbliche di una voce enciclopedica.

---

## Decisione proposta

1. **Estensione di schema a `data/topics.yaml` (DR-04)**: aggiunta di un sotto-blocco opzionale `voce_enciclopedica` a ciascuna voce, con un solo campo, `stato`, a valori chiusi `da_scrivere | bozza | pubblicata | solo_tema` (enumerazione già proposta nel documento di progettazione citato dall'handoff, qui recepita as-is). Assenza del blocco ⇔ `solo_tema` (nessuna pagina pubblica prevista) — nessuna migrazione richiesta per le voci esistenti (oggi solo `fixture-tema-tecnico`).
2. **Meccanismo per le pagine pubbliche**: tassonomia Hugo nativa `temi` (già configurata in `hugo.toml`, mai finora popolata di contenuto), non una sezione parallela `content/enciclopedia/`. Piccola estensione additiva di `layouts/temi/term.html` per rendere `.Content` della pagina di termine, identica al pattern già in uso in `layouts/_default/list.html`.
3. **Aggiornamento della clausola di rivalutazione di DR-04**, per rimuovere il riferimento a `temi`/DR-01 (già risolto) e sostituirlo con un riferimento a questa decisione.

Nessuna modifica a DR-01.

## Contesto

Le 5 voci in `stamotenti-editorial/enciclopedia/voci/*.md` (`meditazione`, `mindfulness`, `mbsr`, `sila`, `upaya`) sono il primo caso reale in cui un tema del vocabolario controllato ha anche una prosa enciclopedica pronta per la pubblicazione, non solo un `id`/`label`/`description` sintetico. Lo schema approvato da DR-04 (`id`, `label_it`, `label_en`, `description`, `status`, `notes`) non prevede modo di rappresentare "questo tema ha (o avrà) una pagina pubblica propria, e a che punto è". Il documento di progettazione dell'enciclopedia (`enciclopedia-progettazione-2026-08-31.md`, non accessibile da questa sessione — vive solo in un progetto claude.ai, non nel filesystem locale; si veda nota sotto) propone un blocco `voce_enciclopedica` per questo scopo.

## SPEC coinvolte

- VOCABULARY-SPEC.md §15 (rendere pubblico un termine è una decisione editoriale distinta dalla capacità tecnica di Hugo di generare una pagina).
- VOCABULARY-SPEC.md §16 (le tassonomie Hugo sono un meccanismo di implementazione, non la fonte di verità; "il sistema non deve creare una tassonomia tecnica parallela quando le funzionalità native di Hugo sono sufficienti").
- VOCABULARY-SPEC.md §17 (metadata dei concetti: elenca esplicitamente "stato" tra i metadata rappresentabili; "non è necessario creare una pagina pubblica per ogni concetto").
- DECISIONS/DR-04-topic-controlled-vocabulary.md (schema approvato di `data/topics.yaml`, qui esteso).
- DECISIONS/DR-06-frontmatter-classification-linking-proposal.md (principio di non-duplicazione: `macroarea` non duplicato perché derivabile da `sotto_area`; applicato qui allo stesso modo per non introdurre un campo-percorso ridondante).

## Vincoli già approvati

- Nessun tema reale può essere inserito senza approvazione editoriale esplicita (DR-04, "Note di implementazione").
- Il vocabolario approvato resta la fonte di verità; Hugo è solo implementazione (VOCABULARY-SPEC §16).
- Non duplicare in un file dati un'informazione già derivabile meccanicamente da un'altra (principio applicato in DR-06 a `macroarea`/`sotto_area`).

## Schema proposto per `voce_enciclopedica`

```yaml
- id: meditazione
  label_it: "Meditazione"
  label_en: "Meditation"
  description: "..."
  status: approvato
  notes: "..."
  voce_enciclopedica:
    stato: pubblicata   # da_scrivere | bozza | pubblicata | solo_tema
```

Un solo campo, deliberatamente: **niente campo-percorso** (es. `pagina:` o `bozza_path:`). Il percorso della pagina pubblica, quando `stato: pubblicata`, è interamente derivabile in modo meccanico dall'`id` stesso via la convenzione di tassonomia già approvata (`content/temi/<id>/_index.md`) — duplicarlo in `data/topics.yaml` violerebbe lo stesso principio di non-duplicazione già applicato in DR-06 a `macroarea`. Non viene neppure tracciata la lingua pubblicata (oggi solo IT, EN in blocco più avanti per decisione del proprietario, §13 del documento di progettazione): è un fatto verificabile guardando quali file di lingua esistono sotto `content/temi/<id>/`, non un dato editoriale da duplicare in `topics.yaml`.

Il blocco è **opzionale**: una voce senza `voce_enciclopedica` equivale a `solo_tema` (VOCABULARY-SPEC §17, "non è necessario creare una pagina pubblica per ogni concetto"). Questo rende l'estensione non-invasiva: la voce fixture esistente (`fixture-tema-tecnico`, DR-08) resta valida senza modifiche.

`bozza_path` (usato in `stamotenti-editorial/enciclopedia/registro-candidati.yaml`) resta un dettaglio di lavorazione interno a quel repository, fuori dalla governance di questo sito — non viene replicato qui.

## Alternative considerate (schema)

- **A — Sotto-blocco `voce_enciclopedica: {stato}` in `data/topics.yaml`** (SCELTA RACCOMANDATA): come sopra. Coerente con VOCABULARY-SPEC §17 (stato è esplicitamente uno dei metadata elencati); minima estensione, non-invasiva, reversibile.
- **B — File dati separato** (es. `data/topics-enciclopedia.yaml`): scartata per lo stesso motivo per cui DR-08 ha scartato l'analoga alternativa C per il fixture di Topic — introdurrebbe una seconda fonte da tenere sincronizzata con `data/topics.yaml` senza un beneficio proporzionato, per un'informazione che riguarda direttamente l'esistenza di ciascuna voce.
- **C — Includere anche un campo-percorso esplicito**: scartata per violazione del principio di non-duplicazione (vedi sopra); il percorso è meccanicamente derivabile dall'`id`.

## Alternative considerate (meccanismo pagine pubbliche)

- **A — Tassonomia Hugo nativa `temi`, con `content/temi/<id>/_index.md` come pagina di prosa** (SCELTA RACCOMANDATA). Verificato in questa sessione: `hugo.toml` ha già `tema = 'temi'` in `[taxonomies]`; `layouts/temi/term.html` esiste già, legge `label_it`/`label_en` da `data/topics.yaml` per l'H1 e lista automaticamente gli articoli associati (`.Pages`), ma **non renderizza `.Content`** — quindi oggi non c'è modo di mostrare la prosa di una voce. `layouts/_default/list.html` ha già esattamente il pattern necessario (`{{ with .Content }}{{ . }}{{ end }}`, riga 7-9), usato per le pagine di sezione. Nessun `content/temi/` esiste ancora sul disco. Coerente 1:1 con VOCABULARY-SPEC §16: nessuna tassonomia tecnica parallela, si usa quella nativa già configurata.
- **B — Sezione parallela `content/enciclopedia/`** (ipotesi di lavoro del documento di progettazione, non confermata): scartata. Verificato che non è necessaria: la tassonomia nativa già copre esattamente lo stesso bisogno (una pagina pubblica per concetto, con elenco automatico degli articoli correlati) senza introdurre una seconda struttura di contenuto con relazioni da mantenere manualmente — esattamente ciò che VOCABULARY-SPEC §16 vieta quando "le funzionalità native di Hugo sono sufficienti". Avrebbe anche richiesto un meccanismo nuovo per collegare `content/enciclopedia/<id>` all'elenco degli articoli che citano quel tema, duplicando ciò che la tassonomia fa già automaticamente.

## Estensione tecnica associata (non normativa per il vocabolario, ma necessaria per l'Alternativa A)

`layouts/temi/term.html`: aggiungere, subito dopo il blocco `<h1>` esistente, lo stesso pattern già in uso in `layouts/_default/list.html`:

```html
{{ with .Content }}
    {{ . }}
{{ end }}
```

Nessuna altra modifica al template. Nessuna modifica a `hugo.toml` (la tassonomia `temi` esiste già).

## Conseguenze

**Vantaggi**: estensione minima e non-invasiva a uno schema già approvato; nessuna migrazione per le voci esistenti; riusa un meccanismo Hugo già configurato e un pattern di template già collaudato altrove nel sito; rispetta alla lettera VOCABULARY-SPEC §15/§16/§17; non introduce alcun campo ridondante.

**Rischi/limiti accettati**: il documento di progettazione originale (v6, `enciclopedia-progettazione-2026-08-31.md`) non è stato letto direttamente in questa sessione — non esiste come file locale, solo come progetto claude.ai "Stamotenti", inaccessibile agli strumenti di questa sessione. Questa proposta si basa sul contenuto dell'handoff (che ne riporta §3 e §13 esplicitamente) e sui file locali realmente presenti in `stamotenti-editorial/enciclopedia/`. Se il documento di progettazione contiene requisiti aggiuntivi per `voce_enciclopedica` non menzionati nell'handoff, andranno verificati separatamente.

## Impatto su Hugo

Una modifica additiva a `layouts/temi/term.html` (vedi sopra). Nessuna modifica a `hugo.toml`. Nessuna modifica ad altri template.

## Impatto sul contenuto futuro

Dopo approvazione: le 5 voci potranno essere aggiunte a `data/topics.yaml` con `status: approvato` e `voce_enciclopedica.stato: pubblicata`; ciascuna genererà un file `content/temi/<id>/_index.md` (solo italiano in questa tranche, per decisione già presa dal proprietario — §13 del documento di progettazione). Il corpo di ciascun file riprenderà **integralmente e senza alterazioni sostanziali** il testo di `stamotenti-editorial/enciclopedia/voci/<id>.md`, con un solo adattamento meccanico già imposto da una convenzione esistente del sito: l'intestazione H1 (`# Meditazione`, ecc.) va rimossa dal corpo, perché `layouts/temi/term.html` la genera già autonomamente da `label_it`/`label_en` — la stessa regola già documentata nel commento di `archetypes/default.md` ("non ripetere il titolo come intestazione di primo livello"). Nessun altro cambiamento al testo. Nessun articolo verrà collegato con `temi:` in questa tranche (l'unico articolo candidato non è ancora pubblicato).

## Reversibilità

Alta: il sotto-blocco `voce_enciclopedica` è opzionale e rimovibile senza impatto su voci che non lo usano; la riga aggiunta a `layouts/temi/term.html` è isolata e rimovibile; le pagine `content/temi/<id>/_index.md`, una volta create, sono normali contenuti Hugo rimovibili come qualsiasi altro.

## Note di implementazione

**Non ancora implementato.** In attesa di approvazione esplicita del proprietario su: (a) lo schema `voce_enciclopedica: {stato}` per `data/topics.yaml`; (b) il meccanismo a tassonomia nativa (Alternativa A) invece di `content/enciclopedia/`; (c) l'estensione di una riga a `layouts/temi/term.html`. Solo dopo approvazione verranno: aggiunte le 5 voci a `data/topics.yaml` (`status: approvato`, `voce_enciclopedica.stato: pubblicata`); creati i 5 file `content/temi/<id>/_index.md` in italiano; applicata la modifica al template. Nessuna modifica a DR-01 (il campo `temi` esiste già, vedi sezione iniziale di questa DR).

## Condizioni di rivalutazione

Da rivalutare quando la traduzione in blocco delle voci (EN) verrà effettuata, per decidere la struttura dei file di lingua (`content/temi/<id>/_index.en.md`) — probabilmente non richiede nuove decisioni, essendo il meccanismo multilingua di Hugo già usato altrove nel sito, ma va confermato quando il caso si presenterà. Da rivalutare se il documento di progettazione v6, una volta reso disponibile localmente, risultasse contenere requisiti su `voce_enciclopedica` non coperti da questa DR.

---

## Correzione proposta a DR-04 (clausola di rivalutazione)

Sostituire, in `DECISIONS/DR-04-topic-controlled-vocabulary.md`, la clausola "Condizioni di rivalutazione" attuale — che cita ancora `temi`/DR-01 come aperto, non più vero dal 2026-08-16 stesso — con:

> Da rivalutare quando il primo tema reale verrà proposto tramite processo editoriale, per verificare che lo schema approvato copra il caso reale — avvenuto il 2026-09-07, vedi `DECISIONS/DR-09-topic-encyclopedia-entry-schema.md`, che estende lo schema con `voce_enciclopedica`. Il riferimento al campo `temi` nel front matter di Article, presente nel testo originale di questa clausola, era già risolto lo stesso giorno dell'approvazione di questa decisione (2026-08-16) tramite l'estensione di DR-01 originata da DR-06, e non descriveva più correttamente lo stato del progetto dal momento stesso in cui è stato scritto.

Questa correzione **non modifica** la decisione originale di DR-04 (schema a 6 campi, zero temi reali all'approvazione) — corregge solo una clausola di rivalutazione che si è rivelata già disallineata al momento della sua stessa stesura.
