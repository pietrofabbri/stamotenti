# DR-10 — Quarta Macroarea: Psicologia Clinica

**Stato**: Approvata
**Data approvazione**: 2026-09-10/2026-09-12 (decisione presa dal proprietario in sessione con Cowork il 2026-09-10, comunicata e implementata in questa sessione il 2026-09-12)
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation
**Origine**: comunicata tramite handoff dedicato di Cowork (accesso in lettura/scrittura solo a `stamotenti-editorial/`, non a `stamotenti/`), che chiude una lacuna segnalata in `enciclopedia-progettazione-2026-08-31.md` §5 (progetto Claude "Stamotenti", v10) e motivata da `clienti-psicologia-clinica-ipotesi-2026-08-31.md` (stesso progetto). Decisione già presa dal proprietario al momento della comunicazione a questa sessione — non rimessa in discussione qui, solo formalizzata e implementata, stesso pattern già usato per l'estensione di DR-04 in DR-09.

---

## Nota sui documenti sorgente

`enciclopedia-progettazione-2026-08-31.md` §5 e `clienti-psicologia-clinica-ipotesi-2026-08-31.md` vivono solo nel progetto claude.ai "Stamotenti" (documenti di lavoro di Cowork), non nel filesystem locale di nessuno dei due repository — stessa situazione già segnalata in DR-09 per il documento di progettazione dell'enciclopedia. Questa decisione si basa sul contenuto riportato nell'handoff (motivazione, struttura 3×3, riferimento alle "Tracce A/B" con 12+ idee-articolo ciascuna), non su lettura diretta dei due documenti. Se il testo esatto risultasse necessario in futuro, va richiesto a Cowork.

## Decisione

Approvata una **quarta macroarea** a sé stante, non una quarta sotto-area dentro "Scienza & Neuroscienze" (MA-1):

```yaml
id: MA-4
slug: psicologia-clinica
title: "Psicologia Clinica"
title_en: "Clinical Psychology"
```

Con tre sotto-aree, stesso schema 3×3 già in uso per MA-1/MA-2/MA-3:

```yaml
id: SA-4-1
slug: psicologia-clinica-basata-sullevidenza
title: "Psicologia Clinica Basata sull'Evidenza"
title_en: "Evidence-Based Clinical Psychology"
macroarea: MA-4

id: SA-4-2
slug: psicologia-della-richiesta-daiuto
title: "Psicologia della Richiesta d'Aiuto"
title_en: "Psychology of Help-Seeking"
macroarea: MA-4

id: SA-4-3
slug: altri-ambiti-della-psicologia-clinica
title: "Altri Ambiti della Psicologia Clinica (PROVVISORIO)"
title_en: "Other Areas of Clinical Psychology (PROVVISORIO)"
macroarea: MA-4
```

`SA-4-3` è dichiaratamente un segnaposto: il proprietario ha scelto esplicitamente di lasciarla generica, senza specializzarla su un tema preciso, finché non ci sarà contenuto sufficiente a giustificare un titolo più mirato. Il titolo "Altri Ambiti della Psicologia Clinica" è la proposta dell'handoff, accettata qui come ragionevole per riempire lo schema 3×3 senza inventare un contenuto editoriale non ancora deciso — resta esplicitamente rivedibile (vedi "Condizioni di rivalutazione").

## Contesto

Il documento di progettazione dell'enciclopedia (v10) segnala da tempo una lacuna: materiale pianificato su psicologia clinica (efficacia di ACT/MBCT/CFT, declino degli effect size, regolazione professionale psicologo/psicoterapeuta, come scegliere un terapeuta, stigma e barriere alla richiesta d'aiuto) non trova una collocazione pulita nelle tre macroaree esistenti. `clienti-psicologia-clinica-ipotesi-2026-08-31.md` articola questo materiale in due tracce (A: metodologia/evidenza; B: accesso alla cura/richiesta d'aiuto), ciascuna con 12+ idee-articolo già abbozzate — volume sufficiente a giustificare una macroarea propria, non solo una sotto-area.

## SPEC coinvolte

- TO-BE.md §3 ("Le macroaree e le sotto-aree sono definite esclusivamente in TO-BE.md. Gli agenti non possono crearne di nuove o modificarne autonomamente la struttura" — vincolo qui rispettato tramite decisione editoriale esplicita del proprietario, non aggirato).
- CONTENT-MODEL.md §4 (area editoriale = macrotema + sotto-area).
- DECISIONS/DR-03-macroarea-sottoarea-model.md, "Condizioni di rivalutazione": "Da rivalutare se TO-BE.md §3 venisse modificato in futuro con una decisione editoriale esplicita (nuove/modificate macroaree o sotto-aree) — in tal caso questa decisione e il file dati derivato andrebbero aggiornati di conseguenza." Questo è esattamente quel momento.

## Vincoli già approvati

- Gli ID tecnici e gli slug seguono la stessa regola già approvata in DR-03 (lowercase, ASCII, kebab-case, nessuna rimozione di stopword, nessun troncamento) — verificato che `psicologia-clinica-basata-sullevidenza` e `psicologia-della-richiesta-daiuto` rispettano la stessa convenzione delle sotto-aree esistenti (es. `fisiologia-integrata-e-pnei`, `ecologia-dell-attenzione-e-societa-digitale`: apostrofi ed elisioni sciolti senza apostrofo nello slug).
- `title_en` non fa parte del testo normativo di TO-BE.md (stesso principio già documentato nell'intestazione di `data/editorial-areas.yaml`): è una traduzione approvata esplicitamente dal proprietario, non generata autonomamente.

## Alternative considerate

- **A — Quarta macroarea a sé stante** (SCELTA APPROVATA): MA-4 "Psicologia Clinica", tre sotto-aree.
- **B — Quarta sotto-area dentro MA-1 "Scienza & Neuroscienze"** (scartata esplicitamente dal proprietario): il materiale pianificato (due tracce, 12+ idee-articolo ciascuna) non ci starebbe in modo pulito dentro una singola sotto-area — MA-1 già ha tre sotto-aree proprie con la stessa profondità di contenuto pianificato; comprimere psicologia clinica in una quarta rischierebbe di renderla eterogenea al suo interno (metodologia della ricerca clinica e psicologia della richiesta d'aiuto sono materie distinte, non un'unica sotto-area naturale) o di sbilanciare MA-1 rispetto alle altre macroaree (4 sotto-aree contro 3).

## Conseguenze

**Vantaggi**: dà una collocazione pulita e proporzionata (stesso schema 3×3 delle altre macroaree) a un volume di contenuto pianificato già sostanziale; non modifica nulla del contenuto esistente (nessun articolo reale è ancora assegnato).

**Rischi/limiti accettati**: `SA-4-3` resta un segnaposto dichiarato, non una categoria editoriale definitiva — un lettore futuro del file dati deve fare affidamento sulla nota "(PROVVISORIO)" nel titolo per capirlo, non c'è una garanzia strutturale diversa (stesso tipo di compromesso già accettato per la fixture tecnica di DR-08, sebbene qui la voce non sia tecnica ma editoriale-provvisoria).

## Impatto su Hugo

Nessuno in questa decisione: `data/editorial-areas.yaml` è un file dati indipendente da Hugo (stesso principio di DR-03). La taxonomy Hugo `sottoarea` (`hugo.toml`, già esistente) è generica e data-driven — legge da questo file, non richiede modifiche per accogliere nuovi id. Nessun template toccato.

## Impatto sul contenuto futuro

Nessun articolo esistente è coinvolto: il primo articolo pubblicato resta su MA-2/SA-2-3 com'è, invariato. La nuova macroarea e le sue sotto-aree sono disponibili per articoli futuri tramite il campo `sotto_area` già approvato (DR-06), validato automaticamente da `scripts/repository-doctor.py` (sezione 15) contro questo stesso file.

## Reversibilità

Alta: nessun contenuto reale referenzia ancora MA-4/SA-4-*, quindi la struttura resta modificabile o rimovibile senza impatti a valle. Il titolo provvisorio di SA-4-3 è esplicitamente destinato a cambiare.

## Note di implementazione

**Implementato in questa tranche**: aggiunta la macroarea MA-4 e le tre sotto-aree SA-4-1/2/3 a `data/editorial-areas.yaml`, stesso schema delle voci esistenti. Aggiunta la sottosezione `### 3.4 Psicologia Clinica` a TO-BE.md §3, stesso formato delle sezioni 3.1-3.3 (frase di inquadramento in grassetto, tre sottosezioni `#### 3.4.x` con descrizione e, per 3.4.1/3.4.2, elenco puntato "Comprende, tra gli altri"; 3.4.3 lasciata come paragrafo aperto, senza elenco vincolante, coerente con la sua natura di segnaposto). Nessuna modifica a `hugo.toml` o ai template.

## Condizioni di rivalutazione

Da rivalutare quando SA-4-3 riceverà un titolo definitivo (oggi "Altri Ambiti della Psicologia Clinica (PROVVISORIO)") — servirà almeno un addendum a questa DR che aggiorni sia `TO-BE.md` §3.4.3 sia `data/editorial-areas.yaml`, con lo stesso livello di approvazione esplicita di questa decisione, non una modifica tecnica silenziosa. Da rivalutare anche se il volume di contenuto reale in MA-4 dovesse in futuro suggerire una redistribuzione delle tre sotto-aree.
