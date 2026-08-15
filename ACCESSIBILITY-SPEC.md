# StamoTenti — ACCESSIBILITY SPECIFICATION

## 1. Scopo

Questo documento definisce i principi e i requisiti di accessibilità
del sito e dei contenuti di StamoTenti.

L'obiettivo è rendere i contenuti utilizzabili dal maggior numero
possibile di persone, comprese persone con differenti capacità visive,
uditive, motorie, cognitive, linguistiche e di apprendimento.

La specifica deve essere interpretata insieme agli standard e alle
best practice pertinenti, senza trasformare ogni dettaglio tecnico in
un vincolo architetturale permanente.

---

## 2. Riferimento principale

StamoTenti utilizza le Web Content Accessibility Guidelines (WCAG) come
principale riferimento per l'accessibilità del web.

WCAG 2.2 costituisce il riferimento operativo di base per le decisioni
attuali. L'evoluzione futura degli standard deve essere monitorata senza
rendere automaticamente obsolete le scelte già valide.

WCAG 2.2 costituisce il riferimento di base per le decisioni attuali.

Il progetto deve seguire gli aggiornamenti rilevanti degli standard senza
assumere che un cambiamento di versione richieda automaticamente una
riscrittura dell'intera architettura.

Quando appropriato, il progetto deve tenere conto della versione
corrente e delle successive evoluzioni delle WCAG.

WCAG 2.2 costituisce il riferimento di base per le decisioni attuali.

La conformità formale a uno standard non deve essere considerata
equivalente alla garanzia di una buona esperienza per ogni persona.

---

## 3. Quattro principi

L'accessibilità deve essere considerata secondo quattro principi:

- percepibile;
- operabile;
- comprensibile;
- robusta.

Questi principi costituiscono una guida generale alla progettazione.

---

## 4. Liste aperte

Gli elenchi contenuti in questa specifica sono indicativi e non esaustivi.

Nuove esigenze possono essere aggiunte quando emergono:

- nuove tecnologie;
- nuovi contenuti;
- nuove esigenze degli utenti;
- nuove best practice;
- nuovi standard.

Gli elenchi non devono diventare colli di bottiglia.

---

## 5. Accessibilità come proprietà del progetto

L'accessibilità non deve essere trattata come una correzione applicata
soltanto alla fine.

Deve essere considerata:

- nella struttura delle pagine;
- nella scrittura;
- nella scelta dei media;
- nella navigazione;
- nella progettazione grafica;
- nella produzione degli articoli;
- nella pubblicazione.

---

## 6. Proporzionalità

Le misure adottate devono essere proporzionate:

La proporzionalità non autorizza però a ignorare un requisito accessibile
applicabile semplicemente perché la sua implementazione è scomoda.

- all'importanza del contenuto;
- al rischio di esclusione;
- alla complessità;
- al costo;
- alla disponibilità delle tecnologie;
- al beneficio atteso.

La ricerca della perfezione teorica non deve produrre un sistema
ingiustificatamente complesso.

---

## 7. Contenuto comprensibile

Il contenuto deve essere scritto in modo:

- chiaro;
- leggibile;
- strutturato;
- coerente.

La chiarezza non implica semplificazione indebita.

Gli articoli scientifici devono mantenere il rigore necessario anche
quando vengono resi più accessibili.

---

## 8. Struttura semantica

Le pagine devono utilizzare, quando appropriato:

- titoli gerarchici;
- paragrafi;
- liste;
- tabelle;
- citazioni;
- elementi semantici.

La struttura deve riflettere la struttura concettuale del contenuto.

---

## 9. Titoli

Ogni pagina significativa deve avere una gerarchia di titoli coerente.

I livelli dei titoli non devono essere scelti soltanto per ottenere
un determinato effetto grafico.

La presentazione visiva deve essere separabile dalla struttura semantica.

---

## 10. Navigazione

La navigazione deve essere:

- prevedibile;
- coerente;
- comprensibile;
- utilizzabile senza dipendere esclusivamente dal mouse.

---

## 11. Navigazione da tastiera

Le funzionalità interattive devono poter essere utilizzate tramite
tastiera quando la tecnologia e la natura della funzione lo richiedono.

Il focus deve essere:

- visibile;
- comprensibile;
- coerente.

---

## 12. Focus

Gli elementi interattivi devono avere uno stato di focus percepibile.

Il focus non deve essere nascosto o reso inutilizzabile da modifiche
grafiche.

---

## 13. Link

I link devono avere un significato comprensibile dal loro testo.

Quando possibile, il testo del link deve permettere di capire la
destinazione senza richiedere la lettura dell'intero paragrafo.

---

## 14. Contrasto

Testo e componenti dell'interfaccia devono mantenere un contrasto
sufficiente rispetto allo sfondo.

Il contrasto deve essere verificato secondo i criteri dello standard
di riferimento quando applicabile.

---

## 15. Colore

Il colore non deve essere l'unico mezzo utilizzato per comunicare
un'informazione essenziale.

Le informazioni importanti devono rimanere comprensibili anche senza
distinguere determinati colori.

---

## 16. Tipografia

La tipografia deve privilegiare:

- leggibilità;
- dimensioni adeguate;
- spaziatura;
- gerarchia;
- lunghezza ragionevole delle righe.

La scelta estetica non deve compromettere la leggibilità.

---

## 17. Ridimensionamento

Il contenuto dovrebbe rimanere utilizzabile quando l'utente aumenta
la dimensione del testo o utilizza impostazioni di visualizzazione
differenti.

---

## 18. Responsive design

Il sito deve essere utilizzabile su:

- desktop;
- tablet;
- smartphone;
- altri dispositivi supportati.

La riduzione delle dimensioni dello schermo non deve causare perdita
ingiustificata di contenuto o funzionalità.

---

## 19. Zoom

Il contenuto deve rimanere utilizzabile quando l'utente effettua
zoom o modifica le impostazioni di visualizzazione supportate.

---

## 20. Immagini

Le immagini devono essere utilizzate in modo significativo.

Quando un'immagine trasmette informazione necessaria alla comprensione,
deve essere disponibile un'alternativa testuale appropriata.

---

## 21. Immagini decorative

Le immagini puramente decorative non devono creare rumore inutile
per le tecnologie assistive.

---

## 22. Testo alternativo

Il testo alternativo deve descrivere lo scopo dell'immagine nel contesto.

Non deve necessariamente descrivere ogni dettaglio visivo.

Un'immagine complessa può richiedere una descrizione più approfondita
nel contenuto circostante.

---

## 23. Diagrammi e grafici

Diagrammi, grafici e visualizzazioni devono avere un'alternativa
comprensibile quando l'informazione che trasmettono è importante.

La rappresentazione visiva non deve essere l'unico modo per accedere
a un'informazione essenziale.

---

## 24. Tabelle

Le tabelle devono essere utilizzate quando esiste una relazione
tabellare reale.

Non devono essere utilizzate esclusivamente per ottenere layout.

Le intestazioni devono essere semanticamente identificabili.

---

## 25. Audio

Gli audio devono essere accompagnati, quando appropriato, da
informazioni testuali sufficienti a comprenderne il ruolo.

Per contenuti audio informativi può essere opportuno fornire una
trascrizione.

---

## 26. Video

I video devono essere valutati rispetto alla necessità di:

- sottotitoli;
- trascrizione;
- descrizione;
- alternative testuali.

Le esigenze dipendono dal contenuto effettivamente presente.

---

## 27. Guide audio

Le guide meditative audio possono essere utilizzate come contenuti
principali.

Quando il contenuto audio trasmette informazioni che l'utente deve
poter conoscere indipendentemente dall'ascolto, deve essere prevista
un'alternativa adeguata.

Una guida esclusivamente esperienziale non deve essere trasformata
artificialmente in un contenuto testuale equivalente quando ciò
altererebbe la natura della pratica.

---

## 28. Contenuti scientifici

Gli articoli scientifici devono mantenere:

- precisione;
- terminologia appropriata;
- riferimenti;
- struttura logica.

L'accessibilità non richiede di eliminare la complessità concettuale.

Può invece richiedere di:

- spiegare termini;
- migliorare la struttura;
- rendere esplicite relazioni;
- evitare formulazioni inutilmente oscure.

---

## 29. Prima parte degli articoli

La parte introduttiva e accessibile degli articoli deve privilegiare:

- chiarezza;
- naturalezza;
- leggibilità;
- orientamento del lettore.

Il revisore stilistico può intervenire per migliorare questi aspetti.

---

## 30. Parte accademica

La parte accademica deve mantenere un registro più rigoroso.

Le esigenze di accessibilità non devono produrre:

- eccessiva informalità;
- perdita di precisione;
- semplificazioni concettualmente scorrette.

---

## 31. Forme di interazione

Le interazioni devono essere comprensibili.

Quando esistono:

- pulsanti;
- controlli;
- filtri;
- menu;
- modali;
- elementi espandibili;

il loro comportamento deve essere prevedibile.

---

## 32. Etichette

I controlli che richiedono input dell'utente devono avere etichette
comprensibili.

Le etichette non devono dipendere soltanto da indicazioni visive.

---

## 33. Errori

Gli errori di compilazione o interazione devono essere comunicati
in modo comprensibile.

Quando possibile devono indicare:

- cosa è andato storto;
- quale campo o azione è coinvolto;
- come correggere il problema.

---

## 34. Form

I moduli devono essere progettati per essere utilizzabili senza
richiedere capacità visive o motorie specifiche.

Le informazioni necessarie alla compilazione devono essere accessibili.

---

## 35. Email

Le email inviate da StamoTenti devono, quando possibile, mantenere
una struttura leggibile anche senza dipendere da elementi grafici.

Le informazioni importanti non devono essere comunicate soltanto
attraverso immagini.

---

## 36. Multilinguismo

L'accessibilità deve essere considerata separatamente per le versioni
italiana e inglese.

La lingua principale della pagina deve essere identificabile
correttamente dal sistema.

---

## 37. Terminologia

La terminologia deve essere coerente con VOCABULARY-SPEC.md.

Quando un termine tecnico può risultare poco comprensibile, il contenuto
può fornire una spiegazione appropriata.

---

## 38. Linguaggio

Il linguaggio deve evitare complessità artificiale.

Questo non significa eliminare:

- termini tecnici necessari;
- concetti specialistici;
- argomentazioni complesse.

Significa evitare oscurità che non aggiunge valore.

---

## 39. Movimento

Animazioni e movimento devono essere utilizzati con moderazione.

Quando appropriato devono essere rispettate le preferenze dell'utente
relative alla riduzione del movimento.

---

## 40. Audio automatico

Il sito non dovrebbe riprodurre automaticamente audio con contenuto
sonoro senza un'azione appropriata dell'utente.

---

## 41. Tempo

Quando un'interazione è soggetta a un limite temporale, l'utente deve
avere, quando appropriato, un modo ragionevole per comprendere o
gestire il limite.

---

## 42. Interfacce complesse

Una funzionalità complessa non deve essere resa inutilmente complessa
per l'utente.

Quando una funzione può essere realizzata in modo semplice senza
perdere valore, deve essere preferita la soluzione più semplice.

---

## 43. Compatibilità

Il sito deve cercare di rimanere compatibile con:

- browser comuni;
- dispositivi diversi;
- tecnologie assistive;
- evoluzione degli standard.

---

## 44. Robustezza

La struttura del sito deve essere sufficientemente robusta da poter
essere interpretata correttamente da diversi user agent e tecnologie
assistive.

---

## 45. Accessibilità e JavaScript

JavaScript non deve essere utilizzato in modo da rendere inutilmente
inaccessibili contenuti o funzioni.

Quando una funzionalità richiede JavaScript, deve essere valutata la
possibilità di fornire un comportamento ragionevole in caso di
limitazioni o errori.

---

## 46. Accessibilità e performance

L'accessibilità e la performance devono essere considerate insieme.

Immagini, script e componenti pesanti non devono essere introdotti
senza una ragione proporzionata.

---

## 47. Accessibilità e SEO

Molte pratiche utili all'accessibilità possono migliorare anche la
comprensione del contenuto da parte dei motori di ricerca.

Non devono però essere applicate esclusivamente per SEO.

La priorità rimane l'utilizzabilità del contenuto.

---

## 48. Accessibilità e GEO

Una struttura semantica chiara e contenuti comprensibili possono
favorire anche l'interpretazione dei contenuti da parte dei sistemi
AI.

L'accessibilità non deve però essere trasformata in una tecnica di
ottimizzazione artificiale.

---

## 49. Test automatici

Quando appropriato possono essere utilizzati strumenti automatici per
individuare problemi di accessibilità.

I controlli automatici devono essere utilizzati come supporto e non come
prova completa di conformità.

Gli strumenti automatici devono essere considerati controlli di supporto e
non certificazioni automatiche di conformità.

I test automatici non dimostrano da soli che una pagina sia accessibile.

---

## 50. Test umano

Quando il contenuto o la funzionalità lo giustifica, devono essere
effettuati controlli umani.

La verifica umana è particolarmente importante quando il problema riguarda
comprensibilità, ordine logico, alternative testuali, esperienza reale o
contenuti complessi.

Il giudizio umano è particolarmente importante per:

- comprensibilità;
- ordine logico;
- chiarezza;
- alternative testuali;
- esperienza reale;
- contenuti complessi.

---

## 51. Agente accessibilità

Può esistere un ruolo dedicato alla verifica dell'accessibilità.

Il ruolo può:

- eseguire controlli automatici;
- analizzare la struttura;
- individuare problemi;
- verificare pagine modificate;
- proporre correzioni;
- monitorare regressioni.

Non deve modificare autonomamente contenuti o interfacce quando
l'intervento richiede una decisione editoriale.

---

## 52. Monitoraggio

Il monitoraggio dell'accessibilità è definito anche in
MONITORING-SPEC.md.

Può includere:

- regressioni;
- problemi ricorrenti;
- nuove pagine;
- modifiche ai componenti;
- problemi rilevati dagli utenti.

---

## 53. Segnalazioni degli utenti

Le segnalazioni di problemi di accessibilità devono essere considerate
informazioni importanti.

Quando una persona segnala un problema, la segnalazione non deve essere
scartata soltanto perché i test automatici non rilevano anomalie.

---

## 54. Priorità

I problemi possono essere classificati secondo:

- impatto;
- frequenza;
- gravità;
- numero di utenti coinvolti;
- difficoltà di correzione.

---

## 55. Regressioni

Una modifica al sito non dovrebbe introdurre regressioni note
nell'accessibilità.

Le componenti riutilizzate devono essere considerate particolarmente
importanti perché un errore può propagarsi a molte pagine.

---

## 56. Componenti

Quando una componente viene riutilizzata in più pagine, i suoi requisiti
di accessibilità dovrebbero essere verificati una volta in modo
accurato e poi monitorati nel tempo.

---

## 57. Contenuti di terzi

I contenuti incorporati o forniti da servizi esterni possono avere
limitazioni di accessibilità.

Quando possibile devono essere:

- valutati;
- sostituiti;
- accompagnati da alternative;
- utilizzati soltanto quando il loro valore giustifica la limitazione.

---

## 58. Media privati

La natura privata di un media non elimina l'esigenza di accessibilità
quando quel media viene effettivamente fornito a un utente.

Le alternative devono però rispettare le autorizzazioni e i diritti
associati al media.

---

## 59. Accessibilità dei contenuti acquistati

Quando StamoTenti utilizza contenuti acquistati o concessi in licenza,
non deve modificare o redistribuire tali contenuti per ottenere
l'accessibilità se ciò non è consentito dai relativi diritti.

Può invece fornire, quando legalmente possibile, informazioni o
alternative accessibili appropriate.

---

## 60. Accessibilità e privacy

Le soluzioni di accessibilità non devono introdurre raccolte di dati
personali non necessarie.

PRIVACY-SPEC.md definisce i principi relativi ai dati personali.

---

## 61. Accessibilità e sicurezza

Le misure di accessibilità non devono essere realizzate introducendo
rischi di sicurezza sproporzionati.

SECURITY-SPEC.md definisce i requisiti di sicurezza.

---

## 62. Accessibilità e semplicità

La soluzione più accessibile non è necessariamente quella con più
funzionalità.

Quando una struttura semplice permette una buona accessibilità,
deve essere preferita a una soluzione complessa.

---

## 63. Accessibilità e manutenibilità

Le soluzioni devono essere mantenibili.

Un'implementazione estremamente complessa che richiede manutenzione
continua può produrre regressioni nel tempo.

---

## 64. Accessibilità e durabilità

Le scelte devono cercare di rimanere valide nel tempo.

Quando possibile devono essere preferite:

- HTML semantico;
- standard aperti;
- strutture semplici;
- componenti riutilizzabili;
- tecnologie ampiamente supportate.

---

## 65. Dichiarazioni pubbliche

Il sito può dichiarare il proprio impegno verso l'accessibilità.

Le dichiarazioni pubbliche devono distinguere tra:

- impegno;
- stato attuale;
- eventuale livello di conformità verificato;
- limiti o eccezioni note.

Non devono suggerire una certificazione o conformità non verificata.

Le dichiarazioni devono essere accurate.

Non deve essere dichiarata una conformità formale che non sia stata
effettivamente verificata.

---

## 66. Conformità

Quando viene dichiarato un livello di conformità WCAG, devono essere
considerati:

- versione dello standard;
- livello;
- perimetro;
- data della verifica;
- eventuali eccezioni o limitazioni.

La dichiarazione deve essere verificabile.

---

## 67. Aggiornamento degli standard

Il ruolo di monitoraggio può segnalare:

- nuove versioni delle WCAG;
- nuove tecniche;
- nuovi problemi noti;
- cambiamenti nei browser;
- evoluzione delle tecnologie assistive.

L'aggiornamento della specifica segue il normale processo di revisione.

---

## 68. Miglioramento progressivo

Non è necessario raggiungere ogni obiettivo simultaneamente.

L'accessibilità deve migliorare progressivamente, dando priorità
agli ostacoli più significativi.

---

## 69. Nessuna perfezione dichiarata

Nessuna verifica automatica, certificazione o revisione singola può
garantire che StamoTenti sia accessibile a ogni persona in ogni
situazione.

Il progetto deve mantenere un atteggiamento di miglioramento continuo.

---

## 70. Principio di non regressione

Quando un contenuto o una componente è già accessibile, una modifica
non dovrebbe ridurne deliberatamente l'accessibilità senza una
ragione documentata e una decisione appropriata.

---

## 71. Responsabilità dell'autore

L'autore mantiene la responsabilità editoriale sui contenuti.

Il ruolo di accessibilità può:

- individuare problemi;
- spiegare il problema;
- proporre soluzioni;
- indicare priorità.

Non sostituisce automaticamente l'autore nelle decisioni editoriali.

---

## 72. Relazione con le altre specifiche

Questa specifica deve essere letta insieme a:

- ARTICLE-SPEC.md;
- MEDIA-SPEC.md;
- MULTILINGUAL-SPEC.md;
- SEO-SPEC.md;
- EMAIL-SPEC.md;
- MONITORING-SPEC.md;
- PRIVACY-SPEC.md;
- SECURITY-SPEC.md;
- WORKFLOW-SPEC.md.

La lista delle dipendenze può evolvere.

---

## 73. Separazione tra principio e implementazione

Questa specifica definisce principalmente:

I dettagli tecnici possono essere sostituiti senza modificare i requisiti di
accessibilità che intendono soddisfare.

- obiettivi;
- principi;
- requisiti;
- criteri di valutazione.

I dettagli relativi a:

- framework;
- CSS;
- JavaScript;
- componenti;
- tooling;
- test automatici;
- CI;

devono essere definiti nei documenti tecnici quando l'implementazione
sarà stabilita.

---

## 74. Flessibilità

Le indicazioni contenute in questa specifica non devono essere interpretate
come un obbligo di utilizzare una particolare tecnologia.

I requisiti di accessibilità devono rimanere stabili anche quando cambiano
framework, componenti o strumenti.

Quando una tecnologia cambia, i principi di accessibilità devono
rimanere validi anche se l'implementazione cambia.

---

## 75. Obiettivo finale

L'obiettivo dell'accessibilità di StamoTenti è permettere alle persone
di:

- trovare i contenuti;
- comprenderli;
- navigarli;
- utilizzarli;
- ascoltarli o leggerli;
- interagire con il sito;
- accedere alle informazioni importanti;

con il minor numero possibile di barriere evitabili.

---

## 76. Gerarchia delle specifiche

In caso di conflitto:

1. i documenti fondativi definiscono principi e vincoli superiori;
2. PRIVACY-SPEC.md definisce i vincoli relativi ai dati personali;
3. SECURITY-SPEC.md definisce i vincoli relativi alla sicurezza;
4. ACCESSIBILITY-SPEC.md definisce i principi di accessibilità;
5. le specifiche dei singoli contenuti definiscono le esigenze
   specifiche dei rispettivi domini;
6. i documenti tecnici definiscono l'implementazione;
7. il codice implementa le specifiche approvate.

Nessuna specifica tecnica può giustificare una regressione deliberata
rispetto a un requisito di accessibilità senza una decisione esplicita
e documentata.
