# DR-07 — Infrastruttura Media minima

**Stato**: Approvata
**Data approvazione**: 2026-08-17
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 2 — Complete Site Shell
**Origine**: gap ereditato dalla Fase 1 (area 6 della roadmap, mai colmata) + prerequisito del Content Fixture System (DR-08)

---

## Contesto

MEDIA-SPEC.md esiste dall'inizio del progetto ma nessuna infrastruttura tecnica per Media è mai stata costruita — né in Fase 1 (dove era un'area esplicita della roadmap) né finora in Fase 2. Nel frattempo DR-02 ha già assegnato a Media un ruolo preciso nel modello concettuale ("Media = file/distribuzione: visibilità, permessi, formato"), e DR-05 ha deciso che Dataset **non** ha un proprio campo di visibilità ma lo eredita da Media tramite `media_id` — il che rende Media, non più rimandabile, il luogo dove quel campo deve realmente esistere. Questa proposta copre solo lo schema dati e il meccanismo di collegamento, non l'esposizione pubblica.

## SPEC coinvolte

- MEDIA-SPEC.md §1 (tipi di media), §2-3 (stato di distribuzione: "ogni media deve avere uno stato di distribuzione" — non condizionato, a differenza di quasi tutti gli altri campi), §4 (permessi separati dalla visibilità, con l'esempio letterale `can_read/can_research/can_cite/can_publish/can_redistribute`), §11 (catalogazione obbligatoria minima), §17 (elenco completo metadata, "non tutti i campi sono obbligatori"), §24-25 (non duplicazione; catalogo separato dal file fisico).
- `DECISIONS/DR-02-dataset-source-media-model.md` (Media = file/distribuzione, riferimenti tramite ID semplici).
- `DECISIONS/DR-05-dataset-visibility-proposal.md` (Dataset eredita la visibilità da Media via `media_id`, mai duplicata — presuppone che Media abbia un campo `visibility` reale).
- `DECISIONS/DR-01-article-front-matter-contract.md` (esteso, `592040c`/`b46022a`/precedenti): **verificato** — non esiste alcun campo `media` nel contratto front matter di Article. Il collegamento Article↔Media oggi non ha alcuna via diretta approvata (vedi "Domanda aperta non risolta" sotto).

## Vincoli già approvati

- CONTENT-MODEL.md §12: relazione `Articolo → utilizza → Media` già presente nel modello concettuale (indipendentemente da questa proposta, preesistente).
- CONTENT-MODEL §19/§20: riuso prima di duplicazione, struttura semplice prima di infrastruttura complessa.
- MEDIA-SPEC §2: "il sistema non deve assumere che una risorsa sia pubblicabile semplicemente perché... è raggiungibile tramite URL... è disponibile online" — un default permissivo dedotto dalla sola presenza del file sarebbe una violazione diretta.
- MEDIA-SPEC §28 (principio di semplicità): niente DAM, niente database dedicato — "GitHub per codice/contenuti strutturati + object storage per i media + catalogo + metadata + Zenodo selettivo" è la base dichiarata sufficiente.

## Schema proposto per `data/media.yaml` (NON creato da questa proposta)

**Obbligatori**:
- `id` — identificativo stabile (pattern coerente con `sources`/`authors`/`datasets`/`topics`, mai messo in discussione finora).
- `type` — MEDIA-SPEC §1 elenca esplicitamente immagine/fotografia/diagramma/PDF/EPUB/audio/video/dataset/altro; nessun elenco chiuso dichiarato, coerente con SOURCE-SPEC che tratta i `type` come "lista estendibile via decisione editoriale".
- `visibility` — MEDIA-SPEC §3 lo rende **obbligatorio senza condizioni** ("ogni media deve avere uno stato di distribuzione"), a differenza di quasi ogni altro campo di questa SPEC. Valori ammessi, **esattamente e soltanto** quelli di MEDIA-SPEC §3: `public`, `private`, `controlled`, `pending_review`.

**Opzionali** (MEDIA-SPEC §17, "non tutti i campi sono obbligatori per ogni tipo di media"):
- `title`, `creator` (§17 "autore o creatore"), `date`, `language`, `provenance`, `license`, `doi`, `url` (URL originale), `checksum`, `size`, `format`, `storage_location`, `source_id` (riferimento opzionale a `data/sources.yaml`, §5 "fonte e media"), `topics` (§18, riferimento a `data/topics.yaml`, "quando applicabile"), `notes`.
- `can_read` / `can_research` / `can_cite` / `can_publish` / `can_redistribute` — booleani, MEDIA-SPEC §4, **asse separato da `visibility`**, non inferibile da esso.

**Regola esplicita proposta** (non lasciata implicita): quando i campi `can_*` sono assenti, un consumatore automatico (es. una futura estensione di `scripts/repository-doctor.py`) **non deve** inferirli favorevolmente dalla sola `visibility: public` — MEDIA-SPEC §2/§4 lo vietano esplicitamente ("il sistema non deve assumere... quando una condizione non è verificata, il sistema non deve inferirla in senso favorevole soltanto dallo stato public"). Assenza = sconosciuto, non permesso.

Nessun campo `article_id`/`content_id` diretto è proposto in questo schema — vedi "Domanda aperta" sotto sul perché.

## Alternative considerate

### A — `data/media.yaml` come solo lookup dati, nessuna taxonomy Hugo (SCELTA RACCOMANDATA)

Stesso pattern già adottato per Dataset in DR-02: file dati locale, nessuna esposizione pubblica automatica, nessuna pagina "hub" per media.

**Vantaggi**: coerente con CONTENT-MODEL §20 (priorità 4, struttura dati semplice, prima di introdurre meccanismi Hugo aggiuntivi); un Media non ha lo stesso valore di "hub bibliografico" che ha un Author o una Source — non è ovvio che meriti una pagina pubblica propria; minimizza la superficie di questa proposta, coerente con MEDIA-SPEC §28 (principio di semplicità).

**Rischi/limiti**: se in futuro servirà una pagina pubblica per media (es. una libreria di immagini/audio), andrà introdotta come decisione tecnica separata — nessun lavoro sprecato, ma un passaggio in più.

### B — Taxonomy Hugo nativa `media` (stesso pattern di `authors`/`sources`/`sottoarea`/`tema`)

Genererebbe automaticamente pagine `/media/<id>/` con elenco degli articoli collegati, usando lo stesso meccanismo già validato in Fase 1A/2.

**Vantaggi**: coerenza meccanica con le altre 4 taxonomy già esistenti; "gratis" in termini di pattern (stesso codice, stesso stile).

**Rischi/limiti — segnalati esplicitamente**: richiederebbe che ogni Media collegato a un contenuto compaia in un campo front matter (es. `media: [...]`) — ma questo campo non esiste ancora nel contratto DR-01 (vedi domanda aperta) e crearlo insieme a questa proposta anticiperebbe una decisione che riguarda il front matter di Article, fuori dallo scope stretto di "infrastruttura Media". Inoltre, una pagina pubblica per un PDF privato o `pending_review` rischierebbe di esporre l'esistenza della risorsa (anche se non il contenuto) prima che la sua classificazione sia stabile — MEDIA-SPEC §23 vuole che "la distinzione pubblico/privato sia evidente sia agli agenti sia al sistema", non che ogni media abbia comunque una superficie pubblica indipendentemente dalla sua visibilità.

## Collegamento Dataset ↔ Media

Nessuna decisione nuova necessaria: DR-02 ha già previsto `media_id` come campo opzionale dello schema di `data/datasets.yaml` (non ancora creato); questa proposta si limita a confermare che `media_id` referenzia l'`id` di una voce in questo futuro `data/media.yaml`, con lookup a runtime (nessuna duplicazione), esattamente come richiesto da DR-05.

## Domanda aperta non risolta da questa proposta

**Come un Article referenzia direttamente un Media (se mai)**: verificato che DR-01 (anche esteso da DR-06) non prevede alcun campo `media` nel front matter. Oggi l'unico collegamento indiretto passa per `Source` (MEDIA-SPEC §5, "fonte e media" — già informalmente usato: `data/sources.yaml` ha un campo `file:`) o per un futuro `Dataset.media_id`. Se il Content Fixture System (DR-08) deve "dimostrare" Media collegato a un Article in modo diretto, servirà una futura estensione di DR-01 (stesso pattern di DR-06 per `sotto_area`/`temi`) — **non proposta né decisa qui**, segnalata soltanto.

## Conseguenze

**Vantaggi**: colma un gap ereditato dalla Fase 1 con lo sforzo minimo necessario; sblocca DR-05 (che presuppone Media abbia `visibility`) e DR-08 (fixture); nessuna modifica a `hugo.toml`/`layouts/` in questa proposta.

**Rischi/limiti accettati**: senza taxonomy (Alternativa A), non esiste ancora un modo pubblico di "sfogliare" i media — accettabile perché nessun media reale esiste oggi e nessuna richiesta editoriale lo impone.

## Impatto su Hugo

Nessuno in questa proposta — nessuna modifica a `hugo.toml`, `layouts/`, `archetypes/`. Solo un futuro `data/media.yaml`, se approvata.

## Impatto sul contenuto futuro

Chi catalogherà il primo media reale dovrà compilare almeno `id`/`type`/`visibility`; tutto il resto resta opzionale finché non serve. Un PDF già presente nel progetto in passato (rimosso per decisione del proprietario, vedi `MEMORY/MEM-2026-08-16-01`) sarebbe stato un caso d'uso reale di questo schema, se fosse esistito allora.

## Reversibilità

Alta: file dati locale in più, nessuna modifica a struttura URL o a contenuti reali. Passare da Alternativa A a B in futuro è additivo (aggiungere la taxonomy non richiede toccare lo schema dati).

## Raccomandazione motivata

**Alternativa A** (solo lookup dati, nessuna taxonomy) con lo schema sopra. Priorità CONTENT-MODEL §20 e principio di semplicità MEDIA-SPEC §28 convergono sulla stessa conclusione: costruire solo ciò che è necessario ora (un catalogo con visibilità reale, per sbloccare DR-05) senza anticipare un'esposizione pubblica che nessuna SPEC richiede esplicitamente oggi.

## Decisione presa

**Approvata l'Alternativa A**: `data/media.yaml` come solo lookup dati, **nessuna taxonomy Hugo** per Media. Lo schema proposto sopra (obbligatori `id`/`type`/`visibility`; opzionali come elencato; `can_*` come asse separato dalla visibilità, mai inferito favorevolmente) è approvato così com'è.

La domanda aperta sul collegamento diretto Article↔Media (nessun campo `media` in DR-01) **resta non risolta**, come previsto — da affrontare quando il Content Fixture System (DR-08) dimostrerà collegamenti reali, non in questa decisione.

## Note di implementazione

**Implementato il 2026-08-17**: `data/media.yaml` creato con lo schema sopra documentato in commento YAML, zero voci reali (stesso trattamento già dato a `data/datasets.yaml`). Nessuna taxonomy aggiunta a `hugo.toml`, nessuna modifica a `layouts/`, coerente con l'Alternativa A.
