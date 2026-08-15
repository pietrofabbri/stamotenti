# StamoTenti — DECISION SPECIFICATION

## 1. Scopo

Questo documento definisce come StamoTenti conserva e utilizza le
decisioni significative che riguardano il progetto.

Lo scopo principale è preservare il motivo per cui una scelta è stata
fatta, evitando che decisioni già prese debbano essere continuamente
riconsiderate senza nuove informazioni.

La documentazione delle decisioni deve essere leggera.

Non ogni scelta richiede un record.

---

## 2. Decisione

Una decisione è una scelta consapevole tra due o più possibilità che
produce conseguenze rilevanti per il progetto.

Possono essere documentate, tra le altre:

- decisioni architetturali;
- decisioni organizzative;
- decisioni relative agli agenti e ai ruoli;
- decisioni relative ai workflow;
- decisioni relative a storage e infrastruttura;
- decisioni relative alla gestione dei contenuti;
- decisioni relative a privacy e sicurezza;
- decisioni relative a strumenti e tecnologie;
- decisioni relative a principi operativi.

L'elenco è aperto.

---

## 3. Non tutte le decisioni richiedono documentazione

Una decisione può essere lasciata al normale workflow quando:

- è facilmente reversibile;
- non produce conseguenze significative;
- deriva direttamente da una specifica già approvata;
- è una normale scelta di implementazione;
- non modifica l'architettura o il comportamento generale del sistema.

La documentazione deve concentrarsi sulle decisioni il cui contesto
potrebbe essere importante in futuro.

---

## 4. Il valore del perché

Il valore principale di un decision record non è registrare soltanto
cosa è stato scelto.

Il record deve essere sufficientemente breve da spiegare la scelta senza
trasformarsi in una seconda SPEC.

Deve rendere comprensibile, quando utile:

- quale problema esisteva;
- quali alternative erano considerate;
- perché è stata scelta una soluzione;
- quali compromessi sono stati accettati;
- quali conseguenze erano previste.

Una decisione priva del proprio contesto può diventare difficile da
interpretare quando cambiano le condizioni del progetto.

---

## 5. Relazione con le specifiche

Le specifiche descrivono lo stato attuale approvato del sistema.

I decision record conservano il ragionamento che ha portato a quello
stato.

Pertanto:

- una SPEC dice principalmente cosa vale;
- un decision record spiega perché è stato scelto;
- il codice implementa quanto approvato;
- il workflow stabilisce come viene applicato.

Il decision record non sostituisce una SPEC.

---

## 6. Relazione con la Costituzione

Una decisione non può contraddire i principi fondativi di StamoTenti.

Quando una decisione sembra richiedere una modifica di un principio
fondativo, il problema deve essere trattato secondo il processo di
revisione della Costituzione.

La decisione operativa non può modificare implicitamente un principio
fondativo.

---

## 7. Relazione con la memoria operativa

La memoria operativa conserva osservazioni, lezioni e best practice
emerse durante il lavoro.

Un'osservazione può successivamente portare a una decisione.

Quando ciò accade:

- la memoria conserva l'esperienza;
- il decision record conserva la scelta effettuata;
- la SPEC viene aggiornata se la scelta modifica una regola corrente.

---

## 8. Decisioni già prese

Quando una questione è già stata decisa e non sono emerse nuove
informazioni rilevanti, gli agenti dovrebbero evitare di riaprire
inutilmente la discussione.

Possono segnalare la decisione esistente.

La questione può essere riaperta quando:

- cambiano i vincoli;
- emergono nuove informazioni;
- la decisione produce conseguenze inattese;
- la decisione entra in conflitto con una nuova esigenza;
- la tecnologia o il contesto cambiano significativamente.

---

## 9. Nuove informazioni

Una decisione non deve essere considerata intoccabile.

Il fatto che una scelta sia stata documentata non significa che sia
necessariamente ottimale per sempre.

Quando emergono nuove informazioni significative, il sistema deve poter
rivalutare la decisione.

---

## 10. Decisioni reversibili

Le decisioni facilmente reversibili richiedono meno formalità.

Quando il costo di tornare indietro è basso, non è necessario creare
processi pesanti per documentare ogni scelta.

---

## 11. Decisioni difficilmente reversibili

Le decisioni difficili da modificare successivamente meritano maggiore
attenzione.

Sono particolarmente rilevanti le decisioni che riguardano:

- struttura dei dati;
- privacy;
- sicurezza;
- storage;
- dipendenze esterne;
- infrastruttura;
- distribuzione;
- architettura;
- formato dei contenuti;
- compatibilità futura.

---

## 12. Contenuto minimo

Un decision record dovrebbe contenere, quando rilevante:

- titolo;
- stato;
- contesto;
- decisione;
- alternative considerate;
- conseguenze;
- eventuali condizioni che potrebbero richiedere una rivalutazione.

Non tutti i campi devono essere compilati quando non sono utili.

---

## 13. Contesto

Il contesto deve spiegare brevemente il problema che ha reso necessaria
la decisione.

Non è necessario ricostruire ogni discussione preliminare.

Il contesto deve contenere soltanto le informazioni utili a comprendere
la scelta.

---

## 14. Alternative

Quando esistono alternative significative, devono essere indicate.

Non è necessario elencare ogni possibilità teorica.

È sufficiente registrare le alternative realisticamente considerate.

---

## 15. Conseguenze

Devono essere considerate, quando rilevanti:

- vantaggi;
- svantaggi;
- costi;
- nuove dipendenze;
- limitazioni;
- rischi;
- opportunità future.

Le conseguenze inattese possono essere aggiunte successivamente alla
memoria operativa o a una nuova decisione.

---

## 16. Stato

Una decisione può essere indicata come:

- proposta;
- approvata;
- superata;
- ritirata.

L'elenco è aperto.

Lo stato deve essere sufficientemente chiaro da evitare ambiguità.

---

## 17. Decisioni superate

Una decisione superata non deve essere cancellata quando la sua storia
rimane utile.

Deve essere possibile capire:

- quale decisione l'ha sostituita;
- perché è stata sostituita;
- quale parte della decisione precedente non è più valida.

---

## 18. Nuova decisione

Quando una decisione precedente viene sostanzialmente modificata,
è preferibile registrare una nuova decisione collegata alla precedente.

Non è necessario riscrivere retroattivamente la storia.

---

## 19. Decisioni concorrenti

Quando esistono più proposte ancora non approvate, devono essere
chiaramente distinguibili.

Una proposta non deve essere interpretata come una regola già vigente.

---

## 20. Proposte degli agenti

Gli agenti possono proporre decisioni.

Una proposta generata da un agente non diventa automaticamente una
decisione approvata.

Il livello di approvazione necessario dipende dalla natura della scelta
e dalle regole definite da APPROVAL-SPEC.md.

---

## 21. Decisioni dell'autore

L'autore mantiene l'autorità sulle decisioni che le specifiche o i
documenti fondativi riservano esplicitamente a lui.

Un agente può preparare analisi, alternative e una proposta completa, ma
questa preparazione non costituisce automaticamente approvazione.

Gli agenti possono fornire:

- analisi;
- alternative;
- conseguenze;
- raccomandazioni;
- proposte.

Non devono trasformare automaticamente una raccomandazione in una
decisione dell'autore.

---

## 22. Decisioni tecniche

Le decisioni tecniche significative possono essere documentate prima
o dopo l'implementazione.

Quando una scelta tecnica ha conseguenze architetturali importanti,
il record dovrebbe essere creato prima dell'implementazione definitiva
quando ciò è praticabile.

---

## 23. Decisioni editoriali

Le decisioni editoriali significative possono essere documentate quando
producono una regola riutilizzabile.

Non è necessario documentare ogni scelta stilistica relativa a un
singolo articolo.

---

## 24. Decisioni relative alle fonti

Quando viene stabilita una regola generale relativa a:

- gerarchia delle fonti;
- utilizzo di una categoria di fonte;
- criteri di citazione;
- diritti;
- redistribuzione;

la decisione può essere registrata e successivamente riflessa nelle
specifiche appropriate.

---

## 25. Decisioni relative ai media

Lo stesso principio vale per:

- PDF;
- audio;
- immagini;
- video;
- dataset;
- altri media.

Una scelta generale sul loro trattamento può essere documentata come
decisione e poi applicata da MEDIA-SPEC.md, DATASET-SPEC.md o dalle
altre specifiche pertinenti.

---

## 26. Decisioni relative agli agenti

Quando viene introdotto, modificato o eliminato un ruolo significativo,
può essere documentata la motivazione.

Il record dovrebbe chiarire, quando utile:

- quale problema risolve il ruolo;
- quali attività svolge;
- perché non è sufficiente un ruolo esistente;
- quali rischi introduce;
- quali limiti sono necessari.

---

## 27. Decisioni relative ai permessi

Le modifiche significative al modello di autorizzazione devono essere
trattate con particolare attenzione.

Una decisione relativa ai permessi dovrebbe considerare:

- capacità richiesta;
- rischio;
- reversibilità;
- necessità di approvazione;
- possibilità di separare lettura e scrittura;
- possibilità di applicare il principio del minimo privilegio senza
  rendere il sistema inutilmente rigido.

---

## 28. Decisioni relative alla privacy

Le decisioni che riguardano dati personali o comunicazioni private
devono essere coerenti con PRIVACY-SPEC.md e SECURITY-SPEC.md.

La comodità operativa non costituisce da sola una ragione sufficiente
per ridurre le protezioni della privacy.

---

## 29. Decisioni relative ai costi

Poiché economicità e sostenibilità sono principi importanti di
StamoTenti, le decisioni infrastrutturali possono considerare:

- costo economico;
- consumo di risorse;
- costi di manutenzione;
- dipendenza da servizi esterni;
- costi di migrazione;
- costo cognitivo.

La soluzione tecnicamente più sofisticata non deve essere considerata
automaticamente migliore.

---

## 30. Decisioni e modularità

Una decisione non dovrebbe introdurre dipendenze non necessarie.

Quando possibile deve essere preferita una soluzione che permetta di
sostituire:

- strumenti;
- provider;
- modelli;
- agenti;
- servizi;
- storage;

senza dover riscrivere l'intero sistema.

---

## 31. Decisioni e durabilità

Le decisioni devono considerare, quando appropriato, la loro validità
nel tempo.

Una soluzione temporanea può essere perfettamente corretta se è
esplicitamente trattata come tale.

Non deve però diventare accidentalmente un vincolo permanente.

---

## 32. Decisioni e manutenibilità

La complessità introdotta da una decisione deve essere proporzionata
al valore prodotto.

Una scelta che funziona oggi ma richiede una manutenzione sproporzionata
può essere una scelta peggiore di una soluzione più semplice.

---

## 33. Decisioni e semplicità

Quando due soluzioni soddisfano ragionevolmente gli stessi requisiti,
deve essere considerata con particolare favore quella più semplice da:

- comprendere;
- implementare;
- verificare;
- mantenere;
- sostituire.

---

## 34. Decisioni e sperimentazione

Non tutte le scelte sperimentali devono diventare decisioni permanenti.

Un esperimento può essere registrato come tale.

La decisione definitiva può essere presa dopo aver osservato i risultati.

---

## 35. Decisioni temporanee

Una soluzione temporanea deve essere identificabile come temporanea
quando esiste il rischio che venga interpretata come architettura
definitiva.

Quando possibile deve essere indicato cosa potrebbe determinarne
la revisione.

---

## 36. Decisioni e metriche

Quando una decisione dipende da un risultato misurabile, può essere
utile indicare:

- quale risultato si vuole osservare;
- come verrà misurato;
- quale condizione potrebbe giustificare una rivalutazione.

Non è necessario trasformare ogni decisione in un sistema di metriche.

---

## 37. Decisioni e monitoraggio

MONITORING-SPEC.md può individuare situazioni in cui una decisione
sembra produrre risultati inattesi.

Il monitoraggio non modifica automaticamente la decisione.

Può generare una segnalazione o una proposta di revisione.

---

## 38. Decisioni e memoria operativa

Quando un'esperienza operativa produce una conseguenza importante,
può essere registrata nella memoria operativa.

Quando l'esperienza porta a una modifica stabile del comportamento,
può essere necessario:

1. registrare l'esperienza;
2. prendere una decisione;
3. aggiornare la specifica pertinente.

---

## 39. Decisioni e revisione costituzionale

Quando una decisione mette in discussione un principio fondativo,
non deve essere risolta semplicemente modificando una specifica
operativa.

Può essere coinvolto l'agente di supporto alla revisione della Costituzione,
che analizza il problema e prepara eventuali proposte.

L'autorità sulla modifica dei documenti fondativi rimane quella prevista
dalla governance del progetto.

Deve essere valutata attraverso il processo di revisione costituzionale
definito nei documenti fondativi e di monitoraggio.

---

## 40. Decisioni e cambiamenti

CHANGE-MANAGEMENT-SPEC.md definisce il processo generale per applicare
modifiche.

DECISION-SPEC.md definisce invece come preservare il ragionamento che
ha portato a una scelta.

I due documenti devono rimanere distinti.

---

## 41. Decisioni e workflow

WORKFLOW-SPEC.md stabilisce come le attività vengono eseguite.

Quando una modifica al workflow deriva da una scelta significativa,
il relativo decision record può conservarne la motivazione.

---

## 42. Decisioni e codice

Il codice non deve essere considerato la fonte primaria del perché
di una scelta architetturale.

Il codice mostra ciò che è stato implementato.

Le decisioni documentano perché è stato scelto quel comportamento.

---

## 43. Decisioni e documenti tecnici

I documenti tecnici devono implementare le decisioni approvate.

Se una decisione cambia, devono essere individuati i documenti tecnici
interessati.

---

## 44. Verifica di coerenza

Quando una decisione significativa viene approvata, deve essere
valutato se esistono:

- SPEC da aggiornare;
- workflow da aggiornare;
- codice da modificare;
- documenti tecnici da modificare;
- decisioni precedenti da superare.

---

## 45. Dipendenze

Un decision record può indicare le specifiche o decisioni da cui
dipende.

Non è necessario creare una rete completa di dipendenze per ogni
decisione.

Devono essere indicate soprattutto le dipendenze che aiutano a
comprendere o mantenere la scelta.

---

## 46. Decisioni storiche

La storia delle decisioni ha valore anche quando la decisione non è
più attiva.

Può spiegare:

- perché una tecnologia è stata utilizzata;
- perché un'alternativa è stata scartata;
- perché una struttura appare insolita;
- perché una certa regola esiste.

---

## 47. Decisioni da non riaprire inutilmente

Gli agenti non devono proporre nuovamente una questione soltanto perché
non condividono personalmente una decisione già approvata.

Devono distinguere tra:

- disaccordo con una decisione;
- nuove informazioni rilevanti;
- cambiamento del contesto.

Solo gli ultimi due costituiscono normalmente una ragione per proporre
una rivalutazione.

---

## 48. Decisioni errate

Una decisione può rivelarsi errata.

Questo non rende inutile il suo record.

La documentazione deve permettere di capire perché la decisione sembrava
ragionevole al momento in cui è stata presa.

---

## 49. Errori e apprendimento

Quando una decisione produce un errore significativo, il progetto può
registrare:

- cosa è successo;
- perché non era stato previsto;
- cosa è stato imparato;
- quale modifica è stata effettuata.

Questo può alimentare OPERATIONAL-MEMORY-SPEC.md.

---

## 50. Decisioni duplicate

Prima di creare un nuovo decision record, dovrebbe essere verificato
se esiste già una decisione relativa allo stesso problema.

Quando esiste, è preferibile:

- collegarsi alla decisione esistente;
- aggiornarne lo stato;
- oppure creare una nuova decisione che la supera.

---

## 51. Decisioni e richieste frequenti

Quando una stessa decisione viene richiesta ripetutamente, può essere
un segnale che:

- la decisione non è facilmente reperibile;
- la documentazione è insufficiente;
- il workflow è troppo complesso;
- potrebbe essere utile un'automazione.

Il problema può essere segnalato al ruolo di stabilizzazione e
manutenzione del sistema.

---

## 52. Decisioni e automazione

Una decisione ripetuta frequentemente può essere candidata a
automazione quando:

- la regola è sufficientemente stabile;
- il comportamento è prevedibile;
- l'automazione riduce lavoro ripetitivo;
- non introduce rischi sproporzionati.

L'automazione non deve eliminare una revisione umana quando questa è
richiesta da una regola superiore.

---

## 53. Formato libero controllato

I decision record devono rimanere leggibili come Markdown semplice.

Non è necessario introdurre YAML o altri formati strutturati quando
questi non aggiungono valore.

Eventuali metadati possono essere rappresentati in modo semplice e
leggibile.

---

## 54. Brevità

Un decision record dovrebbe essere il più breve possibile senza perdere
il contesto necessario.

La documentazione delle decisioni non deve diventare una seconda
specifica.

---

## 55. Quando non scrivere

Non creare un decision record soltanto per:

- cambiare una parola;
- correggere un refuso;
- eseguire una normale manutenzione;
- applicare una regola già stabilita;
- scegliere un dettaglio implementativo irrilevante.

---

## 56. Quando scrivere

È opportuno considerare un decision record quando una scelta:

- è difficile da invertire;
- riguarda più parti del sistema;
- crea una nuova dipendenza;
- modifica un workflow;
- modifica il modello degli agenti;
- modifica la gestione dei dati;
- modifica la sicurezza;
- modifica la privacy;
- modifica l'architettura;
- risolve un problema ricorrente;
- stabilisce una nuova convenzione importante.

---

## 57. Revisione

I decision record non devono essere periodicamente riscritti soltanto
per mantenere il repository "pulito".

Quando una decisione rimane valida, non è necessario modificarla.

Quando non è più valida, deve essere indicato il suo nuovo stato.

---

## 58. Nessuna burocrazia

Il sistema delle decisioni deve rimanere leggero.

Il costo di documentare una decisione non dovrebbe superare
sistematicamente il valore della memoria che produce.

L'obiettivo è risparmiare tempo futuro, non creare lavoro amministrativo.

---

## 59. Relazione con PROJECT-MAP.md

PROJECT-MAP.md dovrà indicare:

- dove vengono conservate le decisioni;
- come si collegano alle specifiche;
- quando devono essere consultate.

La struttura concreta del repository potrà essere definita nella fase
tecnica.

---

## 60. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi definiscono principi e vincoli superiori;
2. le specifiche definiscono il comportamento corrente;
3. i decision record spiegano le decisioni che hanno portato al
   comportamento corrente;
4. i workflow definiscono le procedure operative;
5. i documenti tecnici definiscono l'implementazione;
6. il codice implementa quanto approvato.

Un decision record non può essere utilizzato per giustificare un
comportamento contrario a una regola superiore attualmente valida.

---

## 61. Principio finale

Le decisioni devono essere abbastanza documentate da permettere a una
persona o a un agente futuro di capire:

- cosa è stato deciso;
- perché;
- quali alternative esistevano;
- quali compromessi sono stati accettati;
- quando potrebbe essere ragionevole riconsiderare la scelta.

Il sistema deve preservare la memoria delle decisioni senza trasformare
la memoria in rigidità.
