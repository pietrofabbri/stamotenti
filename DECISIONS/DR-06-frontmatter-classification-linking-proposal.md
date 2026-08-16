# DR-06 — Collegamento della classificazione editoriale nel front matter

**Stato**: Approvata
**Data approvazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation
**Origine**: punto lasciato esplicitamente aperto in `DECISIONS/DR-01-article-front-matter-contract.md`, sezione "Condizioni di rivalutazione"

---

## Contesto

DR-01 ha approvato un contratto front matter minimale per Article, escludendo esplicitamente `topics`/`temi`, `macroarea`, `sotto-area` in attesa di questa decisione. `data/editorial-areas.yaml` (DR-03) e `data/topics.yaml` (DR-04, oggi vuoto) esistono già come contenitori dati, ma nessun meccanismo collega ancora un Article a una sotto-area o a temi. Questa proposta definisce come, senza modificare ARTICLE-SPEC.md, CONTENT-MODEL.md, l'archetipo o il contratto già approvato in DR-01 (che resta invariato finché questa proposta non è a sua volta approvata).

## Vincoli da rispettare (già approvati altrove, non rimessi in discussione da questa proposta)

- Un articolo ha normalmente una sola sotto-area principale (CONTENT-MODEL §4).
- I temi sono opzionali, zero-o-più, e devono referenziare solo id già presenti nel vocabolario approvato (ARTICLE-SPEC §19). Oggi `data/topics.yaml` è vuoto: qualunque valore in `temi` sarebbe strutturalmente un riferimento rotto finché non esiste un vocabolario reale approvato tramite DR-04/processo editoriale.
- Gli identificativi vanno referenziati per id stabile, non per titolo (CONTENT-MODEL §15).
- La classificazione editoriale principale non deve essere modificata autonomamente dagli agenti (ARTICLE-SPEC §20) — questa proposta riguarda solo il meccanismo tecnico di collegamento, non assegna né modifica la classificazione di alcun articolo reale.

## SPEC coinvolte

- ARTICLE-SPEC.md §19 (temi da vocabolario controllato), §20 (classificazione non modificabile autonomamente), §23 (front matter, nessun campo arbitrario).
- CONTENT-MODEL.md §4 (area editoriale = macrotema + sotto-area), §15 (identificativi stabili), §19 (non duplicazione), §20 (semplicità, preferire relazione derivata a duplicata).
- `DECISIONS/DR-01-article-front-matter-contract.md` (contratto da estendere, non modificato da questa proposta).
- `DECISIONS/DR-03-macroarea-sottoarea-model.md` e `DR-03-sottoarea-slug-proposal.md` (fonte degli id `SA-m-n`).
- `DECISIONS/DR-04-topic-controlled-vocabulary.md` (fonte degli id di `data/topics.yaml`, oggi vuoto).

## Proposta di campi

| Campo | Tipo | Cardinalità | Esempio |
|---|---|---|---|
| `sotto_area` | stringa (id) | 0 o 1 (opzionale in questa fase, vedi "Obbligatorietà" sotto) | `sotto_area: SA-1-2` |
| `temi` | lista di stringhe (id) | 0 o più | `temi: []` |

**Naming**: `sotto_area` (snake_case, italiano) segue il termine già usato in TO-BE.md/CONTENT-MODEL.md ("sotto-area") reso in snake_case per compatibilità YAML/front matter, analogo a come gli altri campi del contratto DR-01 sono parole singole in minuscolo. `temi` riprende direttamente la terminologia di VOCABULARY-SPEC.md, che usa sempre "temi" (non "topics") nel testo italiano della SPEC.

**Perché non un campo `macroarea` separato**: la macroarea è già derivabile automaticamente dalla sotto-area tramite il campo `macroarea` presente su ogni voce di `data/editorial-areas.yaml` (es. `SA-1-2 → macroarea: MA-1`). Aggiungere un secondo campo `macroarea` nel front matter duplicherebbe manualmente una relazione già derivabile, in tensione diretta con CONTENT-MODEL §19/§20 (lo stesso principio già applicato in DR-05 per la visibilità di Dataset). La macroarea di un articolo si ottiene sempre a runtime risalendo da `sotto_area` al dato collegato, mai da un secondo campo front matter.

## Relazione con il contratto DR-01

DR-01 esclude oggi esplicitamente questi due campi. Se questa proposta viene approvata, **non modifica automaticamente DR-01**: servirebbe un passaggio separato ed esplicito (fuori scope di questo turno) per aggiungere `sotto_area` e `temi` alla tabella dei campi opzionali di DR-01, coerente con la sua stessa clausola "questi campi potranno essere aggiunti solo tramite una nuova decisione dedicata". Questa proposta prepara il contenuto di quel passaggio, senza eseguirlo.

## Obbligatorietà — punto aperto, non deciso da questa proposta

Due opzioni realistiche, entrambe compatibili con quanto già approvato:
- **Opzionale** (coerente con lo spirito minimale di DR-01: "non introdurre nuovi requisiti"): un articolo può esistere temporaneamente senza `sotto_area` durante la scrittura; nessuna fixture esistente verrebbe invalidata retroattivamente (`meditazione.md` non ha oggi questo campo).
- **Obbligatorio per nuovi articoli** (coerente con CONTENT-MODEL §4 "un articolo ha normalmente una sola sotto-area principale", che suggerisce che nella pratica editoriale a regime il campo dovrebbe sempre essere presente): richiederebbe però una regola esplicita su come trattare i contenuti già esistenti che ne sono privi (fixture tecniche, `content/_index.md`, `content/content.md`), per non romperli retroattivamente.

Questa proposta non sceglie tra le due: la raccomandazione (sotto) è di partire opzionale in questa fase e valutare l'obbligatorietà solo quando inizierà la produzione editoriale reale (fuori Fase 1B/1C secondo la roadmap).

`temi` resta comunque sempre opzionale (0 o più), come già stabilito da ARTICLE-SPEC §19 e CONTENT-MODEL §5, non è oggetto di questa scelta.

## Validazione proposta (NON implementata da questa proposta)

Se approvata, l'estensione naturale di `scripts/repository-doctor.py` (stesso pattern già usato per il controllo incrociato autori/fonti introdotto in Fase 1A) sarebbe:
- se `sotto_area` è presente in un contenuto, il suo valore deve esistere come `id` in `sottoaree` di `data/editorial-areas.yaml` (altrimenti ERROR, riferimento rotto);
- se `temi` è presente e non vuoto, ogni valore deve esistere come `id` in `data/topics.yaml` (altrimenti ERROR) — oggi, essendo `data/topics.yaml` vuoto, **qualunque valore non vuoto in `temi` fallirebbe sempre questo controllo**, comportamento corretto e voluto finché non esiste un vocabolario reale approvato;
- nessun controllo di obbligatorietà su `sotto_area` finché non sarà deciso il punto sopra.

Questa logica non viene scritta in `scripts/repository-doctor.py` in questa proposta.

## Conseguenze

**Vantaggi**: chiude un gap esplicitamente segnalato da DR-01 senza toccare DR-01 stesso; riusa esclusivamente meccanismi e dati già approvati (nessuna nuova entità, nessun nuovo file dati); coerente con lo schema di validazione già collaudato in Fase 1A.

**Rischi/limiti**: finché l'obbligatorietà di `sotto_area` non è decisa, i nuovi articoli potrebbero essere scritti senza classificazione senza che nulla lo segnali — rischio basso in questa fase (nessuna produzione editoriale autorizzata prima di Fase 2/READY FOR CONTENT).

## Impatto su Hugo

Nessuno in questa proposta: nessuna modifica a `hugo.toml`, `layouts/` o `archetypes/default.md` è inclusa o richiesta. L'eventuale aggiunta dei campi all'archetipo sarebbe un passo tecnico separato, successivo a un'approvazione sia di questa proposta sia dell'estensione di DR-01.

## Impatto sul contenuto futuro

Nessun contenuto reale esistente verrebbe modificato da questa proposta. I nuovi articoli, una volta approvata l'estensione di DR-01, potrebbero opzionalmente dichiarare `sotto_area` e `temi`; questi ultimi resterebbero comunque vuoti finché non esisterà un vocabolario reale.

## Reversibilità

Alta: due campi opzionali aggiuntivi sono facilmente reversibili (rimuovibili senza rompere contenuti che non li usano). La decisione sull'obbligatorietà è quella con minore reversibilità nel tempo (rendere un campo obbligatorio dopo che esistono contenuti senza è più costoso che il contrario) — motivo per cui questa proposta raccomanda di partire opzionale.

## Raccomandazione motivata

Approvare i nomi di campo `sotto_area` (stringa singola, opzionale in questa fase) e `temi` (lista, sempre opzionale) come estensione futura di DR-01; non introdurre un campo `macroarea` separato (derivabile); rimandare la decisione sull'obbligatorietà di `sotto_area` a quando inizierà la produzione editoriale reale; estendere `scripts/repository-doctor.py` solo dopo approvazione, con la logica descritta sopra.

## Decisione presa

**Approvata come proposto**: campi confermati `sotto_area` (stringa singola, opzionale in questa fase) e `temi` (lista, sempre opzionale); nessun campo `macroarea` separato (resta derivabile da `sotto_area` tramite `data/editorial-areas.yaml`). L'obbligatorietà di `sotto_area` resta rimandata, come raccomandato, a quando inizierà la produzione editoriale reale.

**Restano DA FARE, come passaggi separati NON autorizzati in questo turno**:
- (a) l'estensione formale della tabella campi di `DECISIONS/DR-01-article-front-matter-contract.md` per includere `sotto_area`/`temi` come campi opzionali — `DR-01` non è stata toccata da questa approvazione;
- (b) l'estensione di `scripts/repository-doctor.py` con la logica di validazione descritta sopra.

Nessuno dei due punti è stato eseguito.
