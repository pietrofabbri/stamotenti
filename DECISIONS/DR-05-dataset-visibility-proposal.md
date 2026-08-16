# DR-05 — Visibilità di Dataset (risolve il punto aperto di DR-02)

**Stato**: Approvata
**Data approvazione**: 2026-08-16
**Approvato da**: proprietario del progetto (Pietro Fabbri)
**Fase**: 1B — Site Foundation
**Origine**: punto aperto segnalato in `DECISIONS/DR-02-dataset-source-media-model.md` ("Punto aperto, non risolto da questa nota")

---

## Contesto

DR-02 ha stabilito che Dataset è un'entità dati separata da Source e Media, con riferimento opzionale a Media tramite `media_id` per il file che lo distribuisce. DATASET-SPEC §9-10 richiede che il dataset "rispetti la distinzione" pubblico/privato/accesso-controllato già definita in MEDIA-SPEC.md, ma non specifica se questo richieda un campo di visibilità proprio su Dataset o se basti ereditarlo dal Media collegato. DR-02 ha lasciato il punto esplicitamente aperto. Questa proposta lo risolve, senza creare `data/datasets.yaml` né modificare `hugo.toml`.

## SPEC coinvolte

- DATASET-SPEC.md §9 ("Il dataset deve rispettare la distinzione stabilita in MEDIA-SPEC.md: posso leggere; posso usare per ricerca; posso citare; posso pubblicare; posso redistribuire... I metadata devono rendere esplicite, quando note, queste condizioni").
- DATASET-SPEC.md §10 ("Il sistema deve distinguere almeno tra: pubblico; privato; accesso controllato... La classificazione deve essere coerente con MEDIA-SPEC.md").
- MEDIA-SPEC.md (stati `public/private/controlled/pending_review` e permessi granulari `can_read/can_research/can_cite/can_publish/can_redistribute`, già il modello adottato per Media).
- CONTENT-MODEL.md §19 "Principio di non duplicazione" e §20 "Principio di semplicità" (citati esplicitamente come criteri di valutazione da questa richiesta).

## Vincoli già approvati

- DR-02: Media = file/distribuzione (visibilità, permessi, formato — governato da MEDIA-SPEC.md); Dataset = oggetto informativo, indipendente dal file.
- CONTENT-MODEL §19: "una relazione derivabile non deve essere mantenuta manualmente senza necessità".
- CONTENT-MODEL §20: "quando Hugo può derivare una relazione in modo affidabile, la relazione non deve essere duplicata manualmente... non devono essere introdotti... relazioni duplicate... quando il problema può essere risolto con una struttura più semplice".

## Alternative

### A — Nessun campo di visibilità proprio su Dataset; ereditata da Media quando presente

Finché un Dataset non ha un `media_id` collegato, è pura metadata catalografica (provenienza, versione, metodologia) e non distribuisce nulla: la domanda "è pubblico?" non si applica a quello stadio. Quando `media_id` è presente, la visibilità del dataset **è sempre quella del Media collegato**, letta da lì al momento della lettura/rendering, mai copiata o duplicata sul record Dataset.

**Vantaggi**: aderente alla lettera a CONTENT-MODEL §19 (nessuna duplicazione di un'informazione derivabile) e §20 (nessuna relazione duplicata quando una struttura più semplice basta); un solo luogo di verità per la visibilità (Media), impossibile che diverga da sé stesso; coerente con DR-02 che assegna esplicitamente "visibilità, permessi, formato" a Media, non a Dataset.

**Rischi/limiti**: un Dataset senza `media_id` (solo metadata di provenienza, nessun file ancora acquisito/distribuito localmente) non avrebbe alcuna rappresentazione esplicita delle condizioni d'uso concettuali menzionate da DATASET-SPEC §9 ("posso citare", "posso usare per ricerca") — che secondo una lettura letterale di §9 sembrano proprietà del dataset come concetto (conosco i miei diritti su questi dati) e non solo della sua eventuale distribuzione come file locale. Questo è un caso limite reale: si può sapere, per un dataset non ancora acquisito, che è ad esempio "citabile ma non ridistribuibile" sulla base delle condizioni della fonte originale, prima ancora di avere un file/Media associato.

### B — Dataset ha un campo di visibilità proprio, sincronizzato manualmente con quello del Media

Dataset porta un proprio campo (es. `visibility`) con gli stessi valori di MEDIA-SPEC, aggiornato a mano quando cambia quello del Media collegato.

**Vantaggi**: rappresenta esplicitamente le condizioni d'uso del dataset come concetto anche quando non esiste ancora un Media collegato (copre il caso limite di A).

**Rischi/limiti — segnalati esplicitamente come richiesto**: rischio concreto e reale di disallineamento manuale rispetto al Media collegato — se il Media viene riclassificato (es. da `controlled` a `public`, o viceversa da `public` a `private` per un errore corretto successivamente) e il campo duplicato su Dataset non viene aggiornato nello stesso momento, il sistema conterrebbe due fonti di verità in conflitto sulla stessa domanda ("è pubblico?"). Data la sensibilità della domanda (DATASET-SPEC §10: "un dataset privato non deve essere pubblicato o redistribuito soltanto perché è stato utilizzato nella ricerca"), un disallineamento non è un rischio cosmetico ma un rischio di conformità reale. Viola direttamente CONTENT-MODEL §19/§20 (duplica manualmente una relazione che il sistema potrebbe derivare).

## Conseguenze

- **A**: nessuna nuova struttura dati per la visibilità; coerente con i principi già approvati; lascia scoperto solo il caso limite "dataset senza media_id con diritti concettuali noti" — caso raro nella fase attuale (`data/datasets.yaml` non esiste ancora, zero dataset reali).
- **B**: copre il caso limite ma introduce un rischio di conformità strutturale (disallineamento) che nessuna delle SPEC coinvolte richiede di accettare.

## Impatto su Hugo

Nessuno in entrambe le alternative: nessuna modifica a `hugo.toml` o ai template è proposta né richiesta da questa decisione, coerente con il vincolo di questo turno.

## Impatto sul contenuto futuro

Quando `data/datasets.yaml` verrà eventualmente creato (soggetto a decisione separata, non anticipata qui), lo schema minimo già presentato in DR-02 dovrà includere, secondo l'alternativa scelta: (A) nessun campo di visibilità, solo `media_id` opzionale con lookup a runtime; oppure (B) un campo `visibility` con valori coerenti a MEDIA-SPEC, più una procedura (non automatizzata da questa proposta) per tenerlo sincronizzato.

## Reversibilità

Alta per entrambe: nessun dato reale esiste ancora, quindi la scelta non ha costo di migrazione oggi. Cambiare da A a B in futuro richiederebbe solo aggiungere un campo; cambiare da B ad A richiederebbe rimuovere un campo e verificare che nessun consumatore dei dati lo referenziasse — A è quindi la scelta "meno impegnativa da abbandonare" delle due.

## Raccomandazione motivata

**Alternativa A**, con il caso limite esplicitamente accettato come rischio residuo minore e non come punto cieco: CONTENT-MODEL §19 e §20 sono chiari nel preferire una relazione derivata a una duplicata quando una struttura più semplice è sufficiente, e qui lo è (Media è già la fonte di verità per visibilità/permessi secondo DR-02). Il rischio di disallineamento manuale di B è un rischio di conformità concreto, non teorico, dato quanto DATASET-SPEC §10 è esplicito sul danno di un dataset privato trattato come pubblico per errore. Il caso limite di A (dataset senza media_id con diritti concettuali noti) può essere gestito in futuro, se e quando emergerà un caso reale, tramite i campi opzionali già previsti nello schema minimo di DR-02 (`license`, note testuali) senza bisogno di un secondo asse di visibilità strutturato — oppure con una revisione mirata di questa decisione, non con l'introduzione preventiva di B oggi.

## Decisione presa

**Approvata l'alternativa A**: Dataset non ha mai un campo di visibilità proprio. Finché non esiste un `media_id` collegato, la domanda "è pubblico?" non si applica (pura metadata catalografica). Quando `media_id` è presente, la visibilità è sempre quella del Media collegato, letta da lì, mai duplicata.

Questa decisione riguarda solo il **modello concettuale**: `data/datasets.yaml` non viene creato da questa approvazione. La sua implementazione (schema effettivo, eventuale campo `media_id`, eventuale lookup a runtime) resta un'attività tecnica separata, da autorizzare esplicitamente a parte, che dovrà tenere conto anche dello schema minimo già presentato in DR-02.
