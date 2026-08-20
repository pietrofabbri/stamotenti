# MEM-2026-08-19-01 — Gate 2 soddisfatto, chiusura Fase 2 approvata

**Identificativo**: MEM-2026-08-19-01
**Tipo**: Decisione (OPERATIONAL-MEMORY-SPEC.md §5, §22 "Decisioni manuali")
**Titolo**: Gate 2 (Complete Site Shell) soddisfatto dopo 3 audit e 4 correzioni; proprietario approva esplicitamente la chiusura della Fase 2
**Data**: 2026-08-19
**Origine**: decisione del proprietario (OPERATIONAL-MEMORY-SPEC.md §7)
**Stato**: attiva
**Livello di affidabilità**: decisione approvata

---

## Perché una nota di memoria operativa e non un Decision Record

Stesso ragionamento di `MEM-2026-08-16-02`: questo evento non è una decisione architetturale con alternative da confrontare, ma la conferma di un checkpoint di fase già previsto e strutturato da `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` ("Gate 2... Richiede approvazione umana"). DECISION-SPEC.md §55 esclude un decision record per l'applicazione di una regola già stabilita.

## Contenuto

### I tre audit

Il Gate 2 letterale ("contenitore editoriale completo, articolo aggiungibile senza ripensare l'architettura", risultato "READY FOR CONTENT") e le sotto-sezioni della Fase 2 (Design system, Typography, Multilingua, SEO/GEO, Accessibility, Content fixture system, Validation, "Stato finale Fase 2") sono stati verificati in tre passaggi successivi, ciascuno sul repository/build reale, non sulla narrazione della sessione:

- **Primo audit (2026-08-18)**: ha trovato 3 gap reali, mai segnalati prima — `description`/`og:description` vuoti su homepage e `content.md`; l'articolo fixture presente nel feed RSS (principale e di sezione), in tensione con la regola "le fixture devono essere separate"; `<h1>` duplicato sulle pagine articolo (template + `# Titolo` nel corpo Markdown). Il proprietario ha approvato la correzione di tutti e 3.
- **Secondo audit (2026-08-19)**: ha ri-verificato i 3 fix e trovato che 2 su 3 (description, H1) erano stati corretti solo nei file esplicitamente nominati, non nella causa sistemica — lo stesso difetto restava su altre pagine reali, inclusa la homepage. Trovato anche un problema nuovo: `<pubDate>` non valido (`0001-01-01`) nel feed RSS per contenuto privo di campo `date`. Il proprietario ha chiesto fix sistemici, non un altro giro file-per-file.
- **Terzo audit (2026-08-19)**: ha ri-verificato esaustivamente (non a campione) tutti e 4 i problemi dopo i fix sistemici — tutti reggevano. Ha cercato oltre, su categorie non ancora controllate esplicitamente (link interni rotti, meta tag duplicati/malformati, JSON-LD non valido, HTML non bilanciato, comportamento senza JavaScript, `lang`/hreflang, 404, cross-contaminazione fixture↔reale): tutto pulito. Trovata una sola cosa nuova, minore: un WARN di deprecazione Hugo (`.Language.LanguageCode`, introdotto dal fix del `pubDate`), corretto subito dopo (`.Language.Locale`).

### I 4 gap reali corretti (con verifica esaustiva finale)

1. **`description`/`og:description` vuoti** — causa: nessun `[params].description` di fallback in `hugo.toml`. Fix sistemico: aggiunto il fallback (testo fedele a TO-BE.md §1). Verificato: 0 pagine su tutto il sito con description vuota.
2. **`<h1>` duplicato** — causa: `single.html`/`list.html`/`home.html` rendono `<h1>{{ .Title }}</h1>`, e diversi contenuti (incluso l'unico articolo reale, `content/biblioteca/meditazione.md`) ripetevano il titolo come `# Titolo` nel corpo. Fix sistemico: rimossa la riga da tutti i file coinvolti; aggiunto un controllo permanente in `repository-doctor.py` ([17] REDUNDANT H1 IN BODY), verificato su un caso positivo e uno negativo. Verificato: tutte le pagine hanno esattamente 1 `<h1>`.
3. **`<pubDate>` RSS non valido** — causa: Hugo emette sempre `<pubDate>` nel template RSS di default, con data zero-value quando `.Date` è assente. Fix: `layouts/_default/rss.xml` custom che omette `<pubDate>` quando `.Date.IsZero` (RSS 2.0 lo rende opzionale) — **deliberatamente non risolto assegnando una data editoriale** a `meditazione.md`, perché sarebbe stata una decisione editoriale non tecnica, collegata alla domanda aperta #10. Verificato: nessun anno "0001" in nessuno dei 29 file `.xml` generati.
4. **Fixture nel feed RSS** — causa: `cascade.sitemap.disable` (DR-08) non copre l'output RSS di Hugo. Fix: `cascade.outputs: [html]` + `cascade.build.list: local` su `content/fixtures/_index.md` e `_index.en.md` (stesso cascade richiesto in entrambe le lingue, come già per la sitemap). Verificato: l'articolo fixture assente da tutti i feed RSS globali/di sezione, ma ancora visibile nell'elenco locale della propria sezione.

### La correzione minore

**Deprecazione Hugo**: `.Language.LanguageCode` (deprecata da Hugo v0.158.0) sostituita con `.Language.Locale` in `layouts/_default/rss.xml`, stessa proattività già applicata in sessione ad altre API deprecate (`.Site.Sites`→`hugo.Sites`, `.Language.LanguageName`→`.Language.Label`). Verificato: valore emesso invariato (`it-IT`/`en-US`), WARN sparito.

### Rischi residui, esplicitamente accettati dal proprietario (non risolti, e non richiesti dal Gate 2 letterale)

- **#17** (`PHASE-2-PLAN.md`): collegamento diretto Article → Media non esiste — dimostrato solo indirettamente (Article → Source → Media) dal Content Fixture System. Nessun campo proposto: DR-01 non lo prevede, non è stato esteso.
- **#18** (`PHASE-2-PLAN.md`): pagine di termine taxonomy delle entità di fixture (`/authors/fixture-autore/`, `/sources/fixture-fonte/`, `/temi/fixture-tema-tecnico/`) e la pagina reale `/sotto_area/sa-1-1/` (oggi popolata solo dalla fixture) restano indicizzabili/in sitemap — il meccanismo DR-08 copre solo `content/fixtures/`, non le pagine taxonomy generate altrove. Deciso esplicitamente di non intervenire (2026-08-18): rischio basso, da rivalutare se il contenuto editoriale reale tarda ad arrivare.
- **#10** (`PHASE-2-PLAN.md`): se includere date tecniche (`datePublished`/`dateModified`) nel JSON-LD — deliberatamente rimandata, nessun contenuto reale ha oggi un campo `date` editorialmente deliberato.
- **Link-checker permanente assente**: "Validation" nella roadmap elenca esplicitamente "link checks" — nessuno script li esegue in modo permanente e ripetibile. Un controllo una tantum nel terzo audit non ha trovato link rotti (127 controllati), ma resta un gap di processo, non di stato attuale.
- **Nessun favicon**: né referenziato né presente in `static/`. Non richiesto esplicitamente da alcuna sezione del roadmap letta verbatim nei tre audit — osservazione minore, non trattata come blocco.

### L'approvazione

Il proprietario del progetto (Pietro Fabbri) ha esaminato la proposta di chiusura fatta al termine del terzo audit (2026-08-19) e ha approvato esplicitamente, in pari data, la chiusura del Gate 2 — "Complete Site Shell" — di `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md`, con i rischi residui sopra elencati esplicitamente accettati come tali, non come problemi irrisolti da nascondere.

**Nota su cosa viene dopo**: a differenza della chiusura del Gate 1 (che apriva direttamente sulla Fase 2, già definita nella stessa roadmap), `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` dichiara esplicitamente nel proprio scopo di coprire soltanto le Fasi 0-2 ("Questa roadmap riguarda inizialmente soltanto: Fase 0... Fase 1... Fase 2") e chiude con "Da questo punto inizia la roadmap dei contenuti e dell'automazione editoriale" — una roadmap futura, non ancora scritta. La chiusura di Gate 2 non implica quindi l'inizio automatico di una "Fase 3" già definita: quella roadmap non esiste ancora in questo repository.

## Collegamenti

- `PHASE-2-PLAN.md`, sezioni "Gate 2 — primo audit", "Gate 2 — secondo audit", e "Gate 2 — CHIUSO" (aggiunta in pari data).
- Commit dei 4 fix: `a55f3be`/`d4e8d48` (description), `a6d8ff7`/`b4e2b3d` (H1 + controllo doctor), `217d824` (RSS pubDate), `c059392` (fixture da RSS); `eb50adb` (deprecazione).
- `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md`, sezioni "FASE 2 — COMPLETE SITE SHELL" e "Gate 2".
- `DECISIONS/DR-07-media-infrastructure-proposal.md`, `DECISIONS/DR-08-content-fixture-system-proposal.md` (origine dei rischi residui #17/#18).
- `MEMORY/MEM-2026-08-16-02-gate1-approved-phase2-start.md` (stesso formato, precedente checkpoint di fase).
