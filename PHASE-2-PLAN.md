# StamoTenti — Piano Fase 2 "Complete Site Shell"

**Stato**: documento di lavoro persistente, non un documento fondativo (non è nell'elenco BASELINE.md dei documenti "mai modificabili autonomamente" — è un piano tecnico, aggiornabile man mano che le tranche procedono, analogo per natura a `DECISIONS/`/`MEMORY/` ma con funzione di tracker anziché di record puntuale).

**Origine**: pianificato in una sessione precedente (fork paralleli su DESIGN-SPEC/ACCESSIBILITY-SPEC e SEO-SPEC/MULTILINGUAL-SPEC + CHANGE-MANAGEMENT-SPEC), mai scritto su file fino ad ora — colmato questo gap su richiesta esplicita del proprietario.

**Ordine di dipendenza** (diverso dall'ordine con cui la roadmap elenca le 6 aree): la tranche M1 va decisa per prima (costo di ritardo più alto); Design e Accessibility condividono lo stesso CSS quindi vanno coordinate; SEO dipende in parte da Multilingua (hreflang); il Content Fixture System dipende da tutte le altre aree più da un'infrastruttura Media che non esiste ancora.

---

## Stato di avanzamento

| # | Tranche | Descrizione | Stato | Commit |
|---|---|---|---|---|
| 1 | **M1** | Conferma schema URL multilingua (`defaultContentLanguageInSubdir=false`, IT senza prefisso/EN con `/en/`) — sola decisione, zero codice | ✅ Fatto | `646ac11` |
| 2 | **D1** | Fondamenta pipeline CSS: `assets/css/main.css` (reset minimo) collegato via Hugo Pipes in `baseof.html` | ✅ Fatto | `f13d9fb` |
| 3 | **D2+A2** | Token colore/spacing/tipografia (palette placeholder verificata per contrasto WCAG, font-stack system-first) con accessibilità incorporata (`:focus-visible`, `prefers-reduced-motion`) nello stesso passaggio | ✅ Fatto | `276e314` |
| 4 | **A1** | Audit read-only pre-CSS (lang corretto, landmark impliciti, zero controllo contrasto/focus prima di D2) | ✅ Fatto (audit, incluso nel report, nessun commit dedicato essendo sola lettura) | — |
| 5 | **D3** | Layout responsive: classi condivise `.wrapper`/`.flow` su 6 template (baseof/header/footer/list/single/taxonomy), nessuna logica Go toccata | ✅ Fatto | `0a03532` |
| 6 | *(fuori piano)* | Fix `debug.html`: testo diagnostico leakava come body visibile in `hugo server` — bug trovato durante il lavoro, non era una tranche pianificata | ✅ Fatto | `fffe6c7` |
| 7 | **S1** | JSON-LD `WebSite` minimo su ogni pagina (solo dati certi da `hugo.toml`), niente Organization/Person/Article | ✅ Fatto | `dcff039` |
| 8 | **M2** | Stringhe di interfaccia via `i18n/it.toml`+`i18n/en.toml` (9 stringhe di chrome) + partial selettore lingua (`.IsTranslated`/`.Translations`, fallback a home altra lingua) | ✅ Fatto | `69a2f06`, `0f4bd26` |
| 9 | **S2** | JSON-LD `Article`/`Person` per pagine articolo, solo da dati realmente presenti (no invenzione) | ✅ Fatto | `5c2bdd0` |
| 10 | **S3** | `hreflang` nel `<head>`, solo quando esiste realmente una traduzione | ✅ Fatto | `5ec53c7` |
| 11 | **M3** | Localizzazione etichette taxonomy visibili quando il sito è in inglese | ✅ Fatto | `5d6d996`, `592040c`, `b46022a` |
| 12 | **S4** | Verifica sitemap/robots.txt di default Hugo | ✅ Fatto (sitemap già conforme; aggiunto `robots.txt` esplicito) | `b52f697` |
| 13 | **M4** | `translationKey` applicato a un contenuto reale/fixture — dipende dal Content Fixture System | ⏸️ Non iniziata (bloccata da #16) |  |
| 14 | **D4** | Font definitivo — decisione del proprietario (system-stack vs self-hosted vs CDN), non presa | ⏸️ Non iniziata (decisione aperta) |  |
| 15 | **A3** | Struttura `alt`-text obbligatorio (shortcode/partial `figure.html`) — dipende da un Media reale | ⏸️ Non iniziata (bloccata da #17) |  |
| 16 | **A4** | Strumento di test accessibilità automatico — decisione del proprietario su quale/se integrarlo | ⏸️ Non iniziata (decisione aperta) |  |
| 17 | **Media** | Infrastruttura Media minima (`data/media.yaml` + eventuale taxonomy) — gap ereditato dalla Fase 1, mai colmato, prerequisito nascosto del Content Fixture System | ⏸️ Non iniziata |  |
| 18 | **Fixture** | Content Fixture System — dimostra le 9 entità (Article/Author/Source/Citation/Topic/Macroarea/Sotto-area/Media/Translation) — dipende da tutte le altre aree | ⏸️ Non iniziata (per ultimo) |  |

---

## Domande aperte non ancora risolte dal proprietario

1. Font definitivo (D4).
2. Palette colori/spacing/breakpoint definitivi (oggi solo placeholder, D2).
3. Supporto formule/notazione scientifica reale — dentro o fuori scope.
4. Wordmark/identità visiva oltre al testo.
5. Strumento di test accessibilità automatico (A4).
6. Se serve una dichiarazione pubblica di accessibilità già in Fase 2.
7. ~~Schema URL EN~~ — risolta (M1).
8. Quali pagine tradurre per prime nel fixture (M4/Fixture).
9. ~~Schema JSON-LD esatto per Article/Person~~ — risolta (S2, `5c2bdd0`): solo headline/description/url/inLanguage/author.name, nessuna data.
10. **Se includere date tecniche nel JSON-LD** — non risolta: nessun contenuto reale ha un campo `date` editorialmente deliberato oggi; S2 ha deliberatamente omesso `datePublished`/`dateModified` in attesa di questa decisione.
11. ~~Quando attivare `robots.txt` custom~~ — risolta (S4, `b52f697`): attivato subito, additivo e a basso rischio (Allow: /, punta al sitemap), non collegato ai blocchi/restrizioni per fixture ancora inesistenti (fuori scope di S4).
12. Dove vivono le fixture nel sito e se escluderle dall'indicizzazione (Fixture).
13. Come rappresentare un Topic-fixture senza violare "zero temi reali" di DR-04 (Fixture).
14. ~~Etichetta inglese per macroaree/sotto-aree~~ — risolta (M3, `592040c`+`b46022a`): 12 traduzioni approvate esplicitamente dal proprietario in sessione (2026-08-17), aggiunte come `title_en` in `data/editorial-areas.yaml`; `sotto_area/term.html` ora localizza sia la sotto-area sia la macroarea genitrice.
15. **[NUOVA] Pagine di tassonomia vuote incluse nella sitemap** (S4, trovata in questo turno): `/sotto_area/` e `/temi/` (entrambe con zero termini reali oggi) compaiono già nella sitemap generata di default da Hugo, in tensione con SEO-SPEC §32 ("una pagina di tassonomia non deve essere indicizzata automaticamente soltanto perché Hugo la genera... pagina vuota"). Escluderle richiederebbe un template sitemap custom o un `cascade` con `sitemap.disable` mirato per `kind` — nessuna delle due verificata, entrambe più complesse del "basso rischio" richiesto per S4. Non implementato, solo segnalato. Si risolverà probabilmente da sé quando `sotto_area`/`temi` avranno termini reali (Content Fixture System / produzione editoriale), ma se resta vuoto a lungo prima di allora vale la pena riconsiderarlo.
14. Se costruire l'infrastruttura Media come parte del fixture system o come tranche/decisione a sé (Media/Fixture).

---

## Gate 2 (promemoria da CLAUDE-CODE-DEVELOPMENT-ROADMAP.md)

La Fase 2 è completata quando esiste un contenitore editoriale completo nel quale sia possibile aggiungere un nuovo articolo senza ripensare l'architettura. Risultato atteso: "READY FOR CONTENT", non "READY FOR AUTONOMOUS PUBLISHING". Richiede approvazione umana esplicita — non viene dichiarata raggiunta automaticamente da questo documento.
