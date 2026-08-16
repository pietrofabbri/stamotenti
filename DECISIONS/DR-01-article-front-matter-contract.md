# DR-01 — Article Front Matter Contract

**Stato**: Approvata
**Data approvazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation

---

## Decisione

Il front matter contract di Article, per questa fase, è definito come segue:

| Campo | Obbligatorietà |
|---|---|
| `title` | obbligatorio |
| `description` | opzionale |
| `authors` | opzionale |
| `tags` | opzionale |
| `sources` | opzionale |
| `draft` | opzionale |
| `date` | opzionale |

Nessun altro campo è parte del contratto approvato in questa decisione.

**Esplicitamente esclusi** (dipendono da decisioni non ancora prese o da lavoro non ancora autorizzato): `topics`/`temi`, `macroarea`, `sotto-area`, uno stato di lifecycle editoriale, `translationKey` o equivalente multilingua. Questi campi potranno essere aggiunti solo tramite una nuova decisione dedicata, quando le rispettive infrastrutture (DR-03, DR-04, lifecycle, multilingua) saranno a loro volta approvate e implementate.

## Contesto

Non esisteva un contratto front matter formale per Article. ARTICLE-SPEC.md §23 delega il contratto a "modello del progetto" mai scritto; CONTENT-MODEL.md §16 conferma che "la struttura definitiva dei campi del front matter sarà definita nelle specifiche appropriate". I tre content file reali (`_index.md`, `content.md`, `biblioteca/meditazione.md`) usavano i campi in modo incoerente tra loro, e l'archetipo (`archetypes/default.md`) non copriva tutti i casi osservati.

## SPEC coinvolte

- ARTICLE-SPEC.md §23 (delega non risolta; divieto di introdurre campi arbitrari).
- CONTENT-MODEL.md §16 (metadata vs contenuto), §15 (identificatori stabili, indipendenti dal titolo), §2 (elenco entità).
- DEPENDENCY-MAP.md (ARTICLE-SPEC → TO-BE.md come unica dipendenza dichiarata).

## Vincoli già approvati

- Gli agenti "non devono introdurre arbitrariamente nuovi campi" (ARTICLE-SPEC §23).
- Campi aggiuntivi solo se "definiti dalla specifica tecnica del progetto".
- Il contenuto e i metadata restano concettualmente distinti (CONTENT-MODEL §16).

## Alternative considerate

- **A — Contratto minimale descrittivo** (SCELTA APPROVATA): formalizzare solo i campi già osservati in uso, tutti opzionali salvo `title`.
- **B — Contratto esteso anticipatorio** (non scelta): includeva campi dipendenti da decisioni non ancora prese (`temi`, stato lifecycle, `translationKey`) — scartata perché avrebbe anticipato DR-04 e altre decisioni non ancora approvate, contro il vincolo esplicito "non introdurre nuovi requisiti".
- **C — Nessun contratto formale** (non scelta): non soddisfaceva il criterio Gate 1 "il content contract è definito".

## Conseguenze

**Vantaggi**: non introduce requisiti nuovi; reversibile; testabile subito da `scripts/repository-doctor.py`; non dipende da altre decisioni pendenti; nessuna modifica ai contenuti reali esistenti necessaria (sono già conformi, essendo tutti i campi opzionali salvo `title` che è già presente ovunque).

**Rischi/limiti accettati**: non esaurisce da solo il punto "Front matter" della Fase 1 roadmap — servirà una revisione quando `temi`, lifecycle e multilingua saranno decisi separatamente.

## Impatto su Hugo

Nessuno in questa decisione: i campi sono già letti dai template esistenti (`bibliography.html`, `cite.html`, `single.html`, taxonomy `authors`/`sources` introdotta in Fase 1A). Nessuna modifica a `archetypes/default.md` è stata fatta né è richiesta da questa decisione (l'archetipo attuale è già coerente col contratto approvato).

## Impatto sul contenuto futuro

I nuovi articoli useranno solo campi già familiari e già supportati dai template. Nessun campo nuovo da compilare finché non saranno approvate le decisioni dipendenti.

## Reversibilità

Alta: un contratto minimale e additivo può sempre essere esteso in seguito senza rompere nulla di esistente.

## Note di implementazione

**Non ancora implementato.** Questa decisione autorizza il contratto concettuale; l'eventuale validazione automatica (es. estensione di `repository-doctor.py` per verificare `title` obbligatorio) resta un'attività tecnica separata, da eseguire solo su richiesta esplicita.

## Condizioni di rivalutazione

Questa decisione andrà rivista quando: DR-04 (Topic) porterà a decidere il nome e la forma del campo `temi`; una decisione separata — successiva a DR-03 e informata dal file dati che DR-03 produrrà, ma non presa da DR-03 stessa, che si limita alla rappresentazione machine-readable di macroarea/sotto-area e non tratta il front matter — stabilirà come rappresentare la classificazione editoriale nel front matter di Article; verrà presa una decisione sul lifecycle editoriale (CONTENT-LIFECYCLE-SPEC.md); verrà presa una decisione sulla struttura tecnica del multilingua (MULTILINGUAL-SPEC.md).
