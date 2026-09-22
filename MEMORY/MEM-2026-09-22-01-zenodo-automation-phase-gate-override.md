# MEM-2026-09-22-01 — Automazione deposito Zenodo autorizzata in deroga esplicita al gate di Fase 4

**Identificativo**: MEM-2026-09-22-01
**Tipo**: Decisione (OPERATIONAL-MEMORY-SPEC.md §22 "Decisioni manuali", §23 "Override")
**Titolo**: Il proprietario autorizza esplicitamente un'automazione di pubblicazione (deposito Zenodo/DOI) prima della soglia di 2-3 articoli validati prevista da PHASE-3-PLAN.md per l'inizio della Fase 4
**Data**: 2026-09-22
**Origine**: decisione del proprietario (OPERATIONAL-MEMORY-SPEC.md §7), presa in risposta a una domanda esplicita di Claude Code
**Stato**: attiva
**Livello di affidabilità**: decisione approvata

---

## Contesto

Arrivato un handoff tecnico da Cowork (`handoff-github-actions-interim-2026-09-21.md` per il contesto di deploy, e un nuovo handoff dedicato per il deposito Zenodo, 2026-09-22) che chiede un meccanismo push-triggered: un articolo marcato `approved: true` in `data/zenodo-deposits.yaml` viene automaticamente impacchettato in PDF, arricchito di metadati dal front matter, e **pubblicato** (non bozza) su Zenodo via API, con scrittura del DOI risultante di nuovo nel registro — senza nessun checkpoint umano nel momento esatto della chiamata `publish` (azione irreversibile: un DOI pubblicato è permanente, si può solo "ritirare", mai cancellare).

Prima di costruire questo, ho verificato una tensione reale con le regole di fase di questo stesso repository:

- `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md`: esclude esplicitamente "pubblicazione automatica" dal proprio ambito e elenca "pubblicare"/"fare push" tra le capacità che Claude non può assumersi come autorizzazione implicita.
- `PHASE-3-PLAN.md` (fase attuale, un solo articolo reale pubblicato finora — `dalla-tradizione-al-secolare`): dichiara esplicitamente "non un processo che produce un articolo pubblicato senza intervento umano nel mezzo", e colloca qualunque automazione editoriale nella Fase 4, il cui innesco è "dopo che 2-3 articoli reali hanno validato il processo manualmente" — soglia non ancora raggiunta (1 solo articolo) — con il vincolo aggiuntivo "human-approval su ogni pubblicazione... non un controllo a campione o successivo".

Ho posto la domanda esplicitamente al proprietario (AskUserQuestion, tre opzioni: gate di approvazione manuale in CI via GitHub Environment; completamente automatico come da handoff, in deroga esplicita alle regole di fase; non costruire nulla ora e rispettare la soglia di Fase 4).

## Contenuto della decisione

Il proprietario ha scelto esplicitamente **"Completamente automatico, come da handoff"** — confermando di voler bypassare, per questo caso specifico, sia il vincolo di PHASE-3-PLAN.md ("non un processo che produce un articolo pubblicato senza intervento umano nel mezzo") sia la soglia di innesco della Fase 4 (2-3 articoli validati prima di automatizzare). Non ha chiesto un gate di approvazione manuale in CI (l'opzione con GitHub Environment/required reviewer, che avevo proposto come raccomandazione, non è stata scelta).

## Cosa NON significa questa decisione

Come da OPERATIONAL-MEMORY-SPEC.md §22, "una decisione manuale non deve diventare automaticamente una regola generale": questa nota autorizza **solo** il meccanismo di deposito Zenodo descritto nell'handoff del 2026-09-22, non una deroga generale al gate di Fase 4 per qualunque futura automazione editoriale. Ogni futura richiesta di automazione (es. pubblicazione automatica di nuovi articoli sul sito stesso, non solo il deposito Zenodo di un articolo già pubblicato) resta soggetta alle stesse regole di fase, da riverificare caso per caso.

La sicurezza operativa residua di questo meccanismo non deriva da un gate umano in CI (esplicitamente rifiutato), ma dalla sequenza verifica-poi-produzione richiesta dallo stesso handoff: prima un run di test su Zenodo Sandbox (token/endpoint separati), solo dopo un test riuscito l'abilitazione del deposito reale — implementata strutturalmente in `data/zenodo-deposits.yaml` popolando prima solo la voce `sandbox: true`, aggiungendo la voce `sandbox: false` (produzione) solo dopo aver verificato l'esito del run sandbox.

## Collegamenti

- `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md` — ambito dichiarato (Fasi 0-2), capacità vietate.
- `PHASE-3-PLAN.md` — Fase 4, soglia di innesco e vincolo "human-approval su ogni pubblicazione".
- `.github/workflows/zenodo-deposit.yml`, `scripts/zenodo_deposit.py`, `data/zenodo-deposits.yaml` — implementazione.
- `MEMORY/MEM-2026-08-19-01-gate2-approved-phase2-closed.md` — precedente checkpoint di fase, stesso formato di nota.
