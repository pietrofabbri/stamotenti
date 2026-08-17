# DR-08 — Content Fixture System

**Stato**: Approvata (decisione presa; implementazione rimandata a un prompt separato)
**Data approvazione**: 2026-08-17
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 2 — Complete Site Shell
**Origine**: roadmap Fase 2, area "Content fixture system"; risolve le domande aperte #12 e #13 di `PHASE-2-PLAN.md`

---

## Contesto

`CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` richiede, come area distinta della Fase 2: "Creare fixture tecniche, separate dai contenuti editoriali reali, che dimostrino: Article, Author, Source, Citation, Topic, Macroarea, Sotto-area, Media, Translation", verificate con "Hugo build; link checks; metadata checks; taxonomy checks; citation checks; multilingual checks; accessibility checks; SEO checks". La stessa roadmap impone altrove: "Le fixture devono essere separate e facilmente riconoscibili." Due domande restavano aperte in `PHASE-2-PLAN.md` (#12, #13): dove vivono le fixture e come escluderle dall'indicizzazione; come rappresentare un Topic senza violare "zero temi reali" di DR-04.

## SPEC/documenti coinvolti

- `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` (Fase 2 "Content fixture system" + "Validation"; regola trasversale "le fixture devono essere separate e facilmente riconoscibili").
- `DECISIONS/DR-04-topic-controlled-vocabulary.md` (Approvata: `data/topics.yaml` contenitore vuoto, "zero temi reali", nessun tema senza processo editoriale di approvazione separato).
- SEO-SPEC.md §29-32 (sitemap solo risorse indicizzabili; pagine di tassonomia non indicizzate automaticamente solo perché Hugo le genera — stesso principio applicabile a intere sezioni fixture).
- `DECISIONS/DR-07-media-infrastructure-proposal.md` (Proposta, non ancora approvata — la fixture Media dipende dal suo esito).
- BASELINE.md (contenuti reali esistenti trattati come fixture tecniche, non da riscrivere — principio distinto ma analogo: qui si tratta di NON confondere questo nuovo set con quello).

## Vincoli già approvati

- ARTICLE-SPEC §20/CONTENT-MODEL §4: la classificazione editoriale reale (macroaree/sotto-aree) non è modificabile autonomamente — ma può essere **referenziata** da una fixture senza modificarla.
- VOCABULARY-SPEC §11/§19: nessun nuovo termine nel vocabolario controllato senza processo di approvazione; ARTICLE-SPEC §19: gli agenti non creano autonomamente nuovi temi.
- DR-04: "Nessun tema reale sarà mai inserito da un agente senza approvazione editoriale esplicita, in ogni fase futura."

## Domanda #12 — Dove vivono le fixture, come si escludono dall'indicizzazione

### Percorso proposto

Sezione dedicata `content/fixtures/`, chiaramente separata da `content/biblioteca/` (contenuto reale). Il nome della sezione stessa è il primo segnale di riconoscibilità richiesto dalla roadmap.

**Entità della fixture — non riusare quelle reali**: si raccomanda che la fixture usi identità proprie e chiaramente sintetiche (es. autore `fixture-autore`, non `rossi`), non le entità reali esistenti (`rossi`, `bianchi`, `esempio2024`, `meditazione.md`). Motivazione: se un articolo-fixture usasse `authors: [rossi]`, comparirebbe nella pagina pubblica reale `/authors/rossi/` insieme all'unico articolo vero — mescolando dimostrazione tecnica e contenuto editoriale reale, esattamente ciò che la roadmap vuole evitare ("facilmente riconoscibili" implica anche "non mescolate"). Le SPEC di dominio (AUTHOR-SPEC, SOURCE-SPEC) non vietano fonti/autori dichiaratamente fittizi purché non spacciati per reali — una entry come `fixture-autore` con nome esplicito "Autore di Fixture (dato tecnico, non una persona reale)" è coerente con la stessa logica già usata per `rossi`/`esempio2024` (dati placeholder, mai presentati come persone/fonti reali).

### Esclusione dall'indicizzazione — meccanismo proposto

Meccanismo nativo Hugo, non un flag custom: **cascade** dal file di sezione `content/fixtures/_index.md`, impostando per tutte le pagine discendenti `sitemap.disable = true` (funzionalità nativa di Hugo, non un campo inventato) — così le fixture non compaiono mai nella sitemap generata (coerente con SEO-SPEC §29, "la sitemap deve includere soltanto risorse che devono essere individuabili dai crawler"). In aggiunta, `layouts/partials/seo.html` (già esistente, S1-S3 di questa Fase 2) dovrebbe emettere `<meta name="robots" content="noindex">` quando la pagina appartiene a questa sezione — coerente con SEO-SPEC §30 ("`robots.txt` e metadata `robots` devono essere utilizzati in modo coerente").

**Nota**: questo meccanismo (`cascade` + `sitemap.disable`) è documentato come funzionalità nativa di Hugo ma **non è stato verificato empiricamente in questa sessione** — qualunque implementazione futura dovrà validarlo in una fixture isolata prima di applicarlo, come da metodo già in uso in tutte le tranche precedenti.

### Alternativa scartata: `robots.txt` con `Disallow: /fixtures/`

Scartata come meccanismo primario: SEO-SPEC §30 dice esplicitamente che il sistema "non deve affidarsi a `robots.txt` come unico meccanismo" — qui il contesto originale è la protezione di contenuti privati, non l'esclusione SEO di pagine tecniche, ma il principio di non affidarsi a un solo meccanismo resta prudente da applicare anche qui. `Disallow` in `robots.txt` impedisce la scansione ma non garantisce la de-indicizzazione di URL già noti (a differenza di `noindex`, che la garantisce se la pagina viene comunque scansionata) — combinare `sitemap.disable` + `noindex` è più robusto e resta comunque coerente con l'`Allow: /` già presente in `layouts/robots.txt` da S4, senza doverlo modificare.

## Domanda #13 — Topic-fixture senza violare "zero temi reali"

Tre alternative valutate:

### A — Nessuna voce in `data/topics.yaml`; il meccanismo Topic non viene esercitato end-to-end dalla fixture

**Vantaggi**: rispetta alla lettera "zero temi reali", nessuna nuova approvazione necessaria.

**Rischi/limiti**: non soddisfa la richiesta esplicita della roadmap di "dimostrare" Topic — la fixture risulterebbe incompleta rispetto a Gate 2 ("un contenitore editoriale completo... senza ripensare l'architettura" presuppone che il meccanismo Topic sia stato davvero esercitato, non solo descritto).

### B — Una voce di fixture esplicitamente marcata in `data/topics.yaml` (SCELTA RACCOMANDATA)

Una singola voce, con id e forma inequivocabilmente tecnici (es. `id: fixture-tema-tecnico`, `label_it: "Tema di esempio (fixture tecnica, non un tema editoriale)"`, `label_en: "Example topic (technical fixture, not an editorial topic)"`, `status: proposto`, `notes: "Voce introdotta per DR-08 (Content Fixture System), non un tema del vocabolario editoriale — vedi DECISIONS/DR-08."`), inserita **solo con approvazione esplicita del proprietario**, con lo stesso livello di autorità con cui è stato approvato DR-04 stesso.

**Vantaggi**: dimostra realmente il meccanismo end-to-end (front matter `temi:` → taxonomy Hugo → `temi/term.html` → localizzazione `label_it`/`label_en` già implementata in M3); resta interamente dentro le regole di DR-04, perché non è un "tema reale" ma una voce tecnica dichiarata tale nei propri stessi metadata (`status: proposto`, `notes` esplicita); reversibile con una singola rimozione quando non più necessaria.

**Rischi/limiti — segnalati esplicitamente**: `data/topics.yaml` smette di essere letteralmente vuoto; un lettore futuro del file (umano o agente) deve fare affidamento sul commento/nota per capire che non è un tema editoriale — mitigato dal naming esplicito e dal campo `notes`, ma non è una garanzia strutturale (nessun campo booleano tipo `is_fixture` esiste oggi nello schema DR-04; introdurlo sarebbe un'estensione di schema che eccede lo scope di questa proposta).

### C — File dati separato per la fixture (es. `data/topics.fixture.yaml`)

**Vantaggi**: separazione strutturale netta, `data/topics.yaml` resta letteralmente vuoto.

**Rischi/limiti — motivo dello scarto**: `layouts/temi/term.html` legge da `hugo.Data.topics` (cioè da `data/topics.yaml`) in modo hardcoded; un file separato non verrebbe mai letto dal meccanismo reale senza modificare il template per unire due fonti dati — il che significherebbe testare un meccanismo diverso da quello che gli articoli reali useranno domani, vanificando parte del valore dimostrativo della fixture.

## Conseguenze (complessive)

**Vantaggi**: risponde a entrambe le domande aperte con meccanismi nativi Hugo, coerenti con quanto già costruito in Fase 2 (S1-S4, M1-M3); non richiede modifiche a `hugo.toml`; riusa esattamente i template già esistenti (nessun nuovo template per "vedere" le fixture, sono contenuti Markdown come gli altri).

**Rischi/limiti accettati**: la voce Topic-fixture (Alternativa B) resta un compromesso — non è "zero", ma è dichiaratamente non editoriale; richiede disciplina (naming, note) più che garanzie strutturali.

## Impatto su Hugo

Se approvata: nuova sezione `content/fixtures/` con proprio `_index.md` (cascade `sitemap.disable`); estensione condizionale di `layouts/partials/seo.html` per il `noindex`; nessuna modifica a `hugo.toml`. Dipende dall'esito di DR-07 per la parte Media della fixture.

## Impatto sul contenuto futuro

Nessuno sui contenuti reali esistenti — la fixture è per costruzione un insieme separato. Quando esisterà un vocabolario Topic reale (DR-04, processo editoriale), la voce fixture (Alternativa B) potrà restare (chiaramente distinta) o essere rimossa, a discrezione del proprietario.

## Reversibilità

Alta: sezione `content/` interamente nuova, rimovibile con una singola cancellazione; la voce Topic-fixture è una singola riga rimovibile da `data/topics.yaml` senza impatti su altro (nessun contenuto reale la referenzierebbe).

## Raccomandazione motivata

Percorso `content/fixtures/` con cascade `sitemap.disable` + `noindex` condizionale (domanda #12); Alternativa B per il Topic-fixture (domanda #13), con naming e `notes` che ne dichiarino esplicitamente la natura tecnica, approvata con lo stesso livello di autorità di DR-04. Entità fixture (autore, fonte) dedicate e distinte da quelle reali, per non mescolare dimostrazione tecnica e contenuto editoriale reale nelle pagine pubbliche già esistenti.

## Decisione presa

Approvata come proposto, su tutti e quattro i punti:

1. **Percorso e meccanismo (#12)**: approvato `content/fixtures/` con cascade `sitemap.disable` + `noindex` condizionale in `seo.html`, come proposto.
2. **Topic-fixture (#13)**: **Alternativa B approvata esplicitamente** — l'eccezione dichiarata a `data/topics.yaml` "zero temi reali" (DR-04) è autorizzata, con lo stesso livello di autorità con cui DR-04 stessa è stata approvata. La voce tecnica (`fixture-tema-tecnico` o id equivalente, `status: proposto`, `notes` che ne dichiara la natura non editoriale) potrà essere creata quando si implementerà il Content Fixture System.
3. **Entità fixture**: confermate **dedicate** — non riuso di `rossi`, `bianchi`, `esempio2024`, `libro2020` o altre entità reali esistenti.
4. **Sequenza Media/Fixture**: DR-07 approvata insieme a questa decisione (stesso commit di approvazione); l'implementazione della fixture resta rimandata a un prompt separato e potrà quindi collegarsi a un `data/media.yaml` già esistente.

## Note di implementazione

**Non implementato in questa decisione.** Nessun `content/fixtures/`, nessuna voce in `data/topics.yaml`, nessuna modifica a `seo.html` per il `noindex` condizionale: la decisione è presa, l'implementazione avverrà in un prompt separato, come richiesto esplicitamente dal proprietario. Il meccanismo cascade/`sitemap.disable` resta da verificare empiricamente in fixture isolata prima di essere applicato, come già segnalato in questa proposta.
