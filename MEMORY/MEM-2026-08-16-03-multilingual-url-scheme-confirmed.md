# MEM-2026-08-16-03 — Schema URL multilingua confermato (M1)

**Identificativo**: MEM-2026-08-16-03
**Tipo**: Decisione (OPERATIONAL-MEMORY-SPEC.md §5, §22 "Decisioni manuali")
**Titolo**: Schema URL multilingua confermato come scelta finale — italiano senza prefisso, inglese con `/en/`
**Data**: 2026-08-16
**Origine**: decisione del proprietario (OPERATIONAL-MEMORY-SPEC.md §7)
**Stato**: attiva
**Livello di affidabilità**: decisione approvata

---

## Contesto

Nel piano di Fase 2 ("Complete Site Shell"), la tranche Multilingua M1 identificava la conferma dello schema URL per l'inglese come la decisione a costo-di-ritardo più alto tra tutte le aree: `hugo.toml` ha già `defaultContentLanguageInSubdir = false` (italiano senza prefisso, inglese con `/en/`, coerente con `weight` in `[languages]`), ma non era mai stato confermato esplicitamente come scelta intenzionale piuttosto che valore ereditato di default. MULTILINGUAL-SPEC.md tratta le modifiche alla struttura URL come decisione tecnica significativa, a bassa reversibilità una volta che esistano contenuti reali indicizzati (nessuno oggi, ma il sito è già pubblico su GitHub).

## Contenuto

Il proprietario ha confermato lo schema URL attuale come scelta finale: `defaultContentLanguageInSubdir = false` resta invariato. **Nessuna modifica al codice/config è stata fatta**: il parametro era già nel valore desiderato, la decisione qui registrata è la conferma esplicita di intenzionalità, non un cambio di configurazione. Non è più da rivalutare senza un cambiamento sostanziale di contesto (es. un requisito editoriale o tecnico che renda necessario un prefisso esplicito anche per l'italiano).

## Collegamenti

- `hugo.toml` (`defaultContentLanguageInSubdir = false`, invariato).
- Piano di Fase 2 (turno precedente), area "Multilingua", tranche M1.
- `MULTILINGUAL-SPEC.md` (classificazione delle modifiche URL come decisione tecnica significativa).
- `MEMORY/MEM-2026-08-16-02-gate1-approved-phase2-start.md` (stesso formato, precedente checkpoint di decisione).
