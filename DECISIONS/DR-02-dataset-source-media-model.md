# DR-02 — Dataset ↔ Source ↔ Media Model

**Stato**: Approvata
**Data approvazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation

---

## Decisione

Dataset è un'entità dati **separata** da Source e da Media. Modello concettuale approvato:

- **Source** = riferimento bibliografico (schema esistente in `data/sources.yaml`, governato da SOURCE-SPEC.md, invariato).
- **Dataset** = oggetto informativo: provenienza, versione, metodologia — indipendente dal file che lo rappresenta e dal riferimento bibliografico che eventualmente lo descrive.
- **Media** = file/distribuzione (visibilità, permessi, formato — governato da MEDIA-SPEC.md).

I collegamenti tra le tre entità avvengono tramite **riferimenti a ID semplici** (non tramite duplicazione di campi), mantenendo il modello interamente su dati YAML locali — nessun database, nessun servizio esterno.

**Non ancora autorizzato**: la creazione effettiva di `data/datasets.yaml` o di qualunque implementazione Hugo (taxonomy, template) per Dataset. Questa decisione approva il **modello concettuale**, non la sua implementazione, che resta un'attività tecnica separata da autorizzare esplicitamente.

## Contesto

SOURCE-SPEC, MEDIA-SPEC e DATASET-SPEC trattavano l'area di sovrapposizione "Dataset" senza una gerarchia esplicita tra loro. DATASET-SPEC §1 dichiara Dataset "entità informativa distinta dal file, dalla fonte bibliografica che lo descrive e dall'articolo che lo utilizza" — la decisione formalizza questa distinzione a livello di modello dati.

## SPEC coinvolte

- SOURCE-SPEC.md §5 (campi minimi Source), §13 (dataset come `type` possibile di Source — non usato in questo modello).
- MEDIA-SPEC.md §1, §14, §3-4 (stati/permessi), §17 (metadata media).
- DATASET-SPEC.md §1-2 (dataset distinto da file e da fonte), §9 (permessi a 5 livelli), §26 (relazione con Article), §30 (classificazione per tema), §32-33 (le tre entità "gestite insieme" senza duplicare identità), §37 (DOI della fonte originale ≠ eventuale DOI StamoTenti).
- CONTENT-MODEL.md §2 e §12 (Dataset ora elencato tra le entità principali e descritto in sezione dedicata, a seguito dell'implementazione della proposta di allineamento — vedi `CONTENT-MODEL-ALIGNMENT-PROPOSAL.md`).

## Vincoli già approvati

- Non duplicare un'identità già rappresentata altrove (CONTENT-MODEL §19).
- "MEDIA-SPEC.md disciplina il file e la sua distribuzione; DATASET-SPEC.md disciplina il significato e l'utilizzo del dataset" (DATASET-SPEC §32-33).
- Priorità CONTENT-MODEL §21: DATASET-SPEC tratta esplicitamente Dataset come entità distinta, quindi il riuso puro di Source o Media non è sufficiente secondo la SPEC stessa — giustifica l'opzione "struttura dati semplice" (priorità 4).

## Alternative considerate

- **A — Dataset embedded in Source** (non scelta): `type: dataset` dentro `data/sources.yaml` con campi opzionali aggiuntivi. Scartata perché i campi specifici di Dataset (metodologia, data acquisizione, versione) non hanno una casa naturale nello schema bibliografico di Source, rischiando di forzare SOURCE-SPEC oltre il suo scopo dichiarato.
- **B — Dataset come entità dati separata** (SCELTA APPROVATA): nuovo file dati con id proprio, riferimenti opzionali (non obbligatori) a Source e a Media tramite ID.
- **C — Ibrido senza entità Dataset dedicata** (non scelta): scartata perché avrebbe lasciato permanentemente non rappresentati campi richiesti da DATASET-SPEC (rischio di non conformità silenziosa).

## Conseguenze

**Vantaggi**: fedele esplicitamente a DATASET-SPEC §1; nessun campo di DATASET-SPEC forzato dentro lo schema Source; relazioni pulite e opzionali; nessuna duplicazione di identità.

**Rischi/limiti accettati**: una struttura dati in più da mantenere in futuro; richiederà disciplina per evitare duplicazione di id tra `data/sources.yaml` e il futuro `data/datasets.yaml`.

## Impatto su Hugo

Nessuno per ora — nessuna implementazione autorizzata in questa decisione. Se in futuro si vorranno pagine dataset dedicate, il pattern già validato in Fase 1A (taxonomy nativa Hugo su `authors`/`sources`) è riutilizzabile in modo analogo, ma resta una decisione tecnica separata.

## Impatto sul contenuto futuro

Chi catalogherà un dataset reale dovrà capire quando compilare `data/sources.yaml` (per la citazione bibliografica), quando il futuro `data/datasets.yaml` (per provenienza/metodologia/versione), quando entrambi con riferimento incrociato via ID.

## Reversibilità

Alta: un file dati locale in più è facilmente rimuovibile/ristrutturabile senza impatti su Source o Media, che restano invariati in questo modello.

## Schema minimo proposto per `data/datasets.yaml` (derivato da DATASET-SPEC.md — file NON ancora creato)

**Obbligatorio** — DATASET-SPEC §3: "Ogni dataset gestito dal sistema deve possedere un identificativo stabile":
- `id`

**Opzionali** — DATASET-SPEC li introduce sempre con "quando disponibile"/"eventuale" (§4, §5-6, §7, §8, §13, §17, §37), nessuno di questi è mandatorio per la SPEC:
- `title` — proposta pragmatica per usabilità/citazione, analoga al minimo di SOURCE-SPEC §5 (id+type+title); non letteralmente "deve" in DATASET-SPEC §17, ma implicita per rendere il dataset citabile
- `producer` / `organization` / `author` (§4, provenienza)
- `repository` (§4)
- `url` (§4)
- `external_id` (§4)
- `publication_date` (§4)
- `acquisition_date` (§4, §6)
- `version` (§4, §5)
- `doi` (§4, §37 — distinto dall'eventuale DOI della fonte bibliografica che descrive il dataset)
- `license` (§4, §8)
- `methodology` (§13)
- `hash` (§7, integrità)
- `source_id` — riferimento opzionale a Source (§32, non duplicazione)
- `media_id` — riferimento opzionale a Media (§33, il file resta disciplinato da MEDIA-SPEC.md)

**Punto aperto, non risolto da questa nota**: DATASET-SPEC §9-10 richiede che il dataset "rispetti la distinzione" pubblico/privato/accesso-controllato di MEDIA-SPEC.md — non è chiaro se serva un campo di visibilità duplicato sul Dataset o se basti ereditarlo dal Media collegato tramite `media_id`. Resta un'ambiguità aperta per una futura decisione tecnica in sede di implementazione.

## Note di implementazione

**Implementato il 2026-08-16**: `data/datasets.yaml` creato, con lo schema minimo sopra documentato in commento YAML e **zero voci reali**. Nessuna voce di esempio inventata (solo un esempio commentato, non attivo). Il punto aperto su visibilità/permessi è stato risolto separatamente da `DECISIONS/DR-05-dataset-visibility-proposal.md` (Approvata): nessun campo di visibilità su Dataset, ereditata da Media tramite `media_id` quando presente — lo schema scritto nel file riflette questa scelta (nessun campo `visibility`/`status` di accesso). Non è stata fatta alcuna modifica a `hugo.toml`, `layouts/` o `archetypes/`: nessuna esposizione pubblica/taxonomy di Dataset, resta fuori scope come già stabilito da questa decisione.

Resta da autorizzare separatamente, quando si deciderà di procedere: il formato esatto dei riferimenti incrociati verso Source/Media in uso pratico (id semplice confermato; struttura interna già presente nello schema come `source_id`/`media_id`); eventuale esposizione pubblica (taxonomy/template Hugo) di Dataset; eventuale validazione automatica in `scripts/repository-doctor.py` (non presente oggi, per coerenza con "zero dataset reali").

## Condizioni di rivalutazione

Da rivalutare quando esisterà il primo dataset reale da catalogare, per verificare che lo schema scritto in `data/datasets.yaml` copra il caso reale. La proposta di allineamento di CONTENT-MODEL.md è stata implementata (Dataset ora in §2 e §12) — punto risolto, non più da rivalutare. Il punto aperto su visibilità/permessi è stato risolto da DR-05 — non più da rivalutare come punto aperto, resta solo come condizione di rivalutazione ordinaria (vedi DR-05, "Condizioni di rivalutazione").
