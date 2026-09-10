# DR-04 — Topic / Controlled Vocabulary Model

**Stato**: Approvata
**Data approvazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation

---

## Decisione

Approvata l'alternativa **A**: predisporre `data/topics.yaml` come contenitore del vocabolario controllato dei temi, con schema aderente a VOCABULARY-SPEC.md §6 e §10, ma con **zero temi reali**. Nessun tema, sinonimo o relazione viene creato da questa decisione.

I nomi delle chiavi YAML proposte (`id`, `label_it`, `label_en`, `description`, `status`, `notes`) sono **approvati come convenzione tecnica**. Il file `data/topics.yaml` è stato creato, vuoto, con lo schema documentato in commento.

## Contesto

Non esisteva alcun vocabolario controllato dei temi (Topic). Il campo `temi` era citato in TECHNICAL/CONTENT-IMPLEMENTATION.md ma assente da ogni contenuto reale e dall'archetipo. Serviva un modello — non i temi stessi.

## SPEC coinvolte

- VOCABULARY-SPEC.md §3 (temi non gerarchici), §6 (modello concettuale per voce: id, forma canonica IT/EN, descrizione, stato, note), §10 (stati: proposto/approvato/deprecato/ritirato), §16 ("le tassonomie di Hugo sono un meccanismo di implementazione. Non costituiscono la fonte di verità editoriale del vocabolario"), §18 (relazioni broader/narrower/related/synonym opzionali).
- ARTICLE-SPEC.md §19 ("i temi devono provenire dal vocabolario editoriale controllato... l'agente deve segnalarlo come proposta. Non deve creare autonomamente un nuovo termine").
- CONTENT-MODEL.md §5 (temi trasversali, distinti dalla classificazione principale).

## Vincoli già approvati

- I temi "non costituiscono automaticamente una gerarchia" (CONTENT-MODEL §5, VOCABULARY-SPEC §3).
- La fonte di verità del vocabolario resta separata dalla taxonomy Hugo (VOCABULARY-SPEC §16).
- Nessun nuovo termine può essere introdotto autonomamente dagli agenti (ARTICLE-SPEC §19).

## Schema approvato per `data/topics.yaml`

I concetti dei campi derivano direttamente da VOCABULARY-SPEC §6: identificativo stabile, forma canonica in italiano, forma canonica in inglese, descrizione, stato, **note editoriali**. Questi sei concetti sono testualmente presenti in VOCABULARY-SPEC §6.

I nomi di chiave YAML (`id`, `label_it`, `label_en`, `description`, `status`, `notes`) sono approvati come **convenzione tecnica** — VOCABULARY-SPEC non specifica una sintassi YAML, quindi questa resa letterale è una decisione tecnica (non editoriale) ora presa esplicitamente.

I **valori** dello stato (`status`) derivano letteralmente dal testo della SPEC e sono gli unici ammessi: uno tra `proposto`, `approvato`, `deprecato`, `ritirato` (VOCABULARY-SPEC §10).

Relazioni broader/narrower/related/synonym (VOCABULARY-SPEC §18) **non incluse** in questa fase, da introdurre solo se necessario.

Il file è stato creato e contiene **zero voci** — è un contenitore vuoto, non un vocabolario compilato.

## Alternative considerate

- **A — `data/topics.yaml` vuoto/placeholder come fonte di verità** (SCELTA APPROVATA).
- **B — Taxonomy Hugo `topics` senza data file separato** (non scelta): scartata perché contraddice direttamente VOCABULARY-SPEC §16 e rischierebbe che chiunque scriva `temi: [nuovo-termine]` nel front matter crei implicitamente un termine "esistente" senza approvazione, violando ARTICLE-SPEC §19.
- **C — Rimandare l'intero vocabolario** (non scelta): scartata perché non soddisfa il criterio Fase 1 "taxonomy... infrastruttura per... temi trasversali".

## Conseguenze

**Vantaggi**: fedele a VOCABULARY-SPEC §16; pronto a ricevere temi reali quando approvati tramite processo editoriale separato, senza ulteriore lavoro architetturale; stati proposto/approvato/deprecato/ritirato già rappresentabili.

**Rischi/limiti accettati**: lo schema dei campi è comunque una scelta tecnica approvata ora, aderente 1:1 a VOCABULARY-SPEC §6/§10.

## Impatto su Hugo

Nessuno in questa decisione: il file dati è indipendente da Hugo. Un'eventuale taxonomy Hugo per esporre i temi pubblicamente resta una decisione tecnica successiva, non autorizzata qui, analoga al pattern già validato in Fase 1A per authors/sources.

## Impatto sul contenuto futuro

Quando un vocabolario reale sarà proposto e approvato tramite processo editoriale, gli articoli potranno referenziare temi con la garanzia che ogni id esista nel file — validabile con lo stesso pattern già introdotto per authors/sources in `repository-doctor.py`.

## Reversibilità

Alta: un file vuoto/placeholder non impegna a nessun contenuto specifico ed è facilmente esteso o ristrutturato.

## Note di implementazione

**Implementato in questa tranche**: `data/topics.yaml` creato, vuoto (`[]`), con lo schema documentato in commento YAML. Nessun tema reale inserito. Nessuna modifica a `hugo.toml` o ai template in questa tranche — il file non è ancora collegato a nessuna taxonomy o pagina pubblica. Nessun tema reale sarà mai inserito da un agente senza approvazione editoriale esplicita, in ogni fase futura.

## Condizioni di rivalutazione

Da rivalutare quando il primo tema reale verrà proposto tramite processo editoriale, per verificare che lo schema approvato copra il caso reale — avvenuto il 2026-09-07, vedi `DECISIONS/DR-09-topic-encyclopedia-entry-schema.md`, che estende lo schema con `voce_enciclopedica`. Il riferimento al campo `temi` nel front matter di Article, presente nel testo originale di questa clausola, era già risolto lo stesso giorno dell'approvazione di questa decisione (2026-08-16) tramite l'estensione di DR-01 originata da DR-06, e non descriveva più correttamente lo stato del progetto dal momento stesso in cui è stato scritto.
