# StamoTenti — AUTHOR SPECIFICATION

## 1. Scopo

Questo documento definisce la gestione delle persone associate ai contenuti e alle fonti di StamoTenti.

Il modello deve permettere di identificare in modo stabile le persone associate alle fonti, evitando duplicazioni e mantenendo correttamente le informazioni bibliografiche.

La stessa persona può svolgere ruoli differenti in fonti differenti.

---

## 2. Autore degli articoli

L'autore editoriale degli articoli di StamoTenti è, salvo decisione esplicita diversa, il proprietario del progetto.

Non è quindi necessario creare un'entità autore separata per ogni articolo.

Se in futuro un'altra persona dovesse pubblicare un articolo, questa modifica deve essere una decisione editoriale esplicita.

Gli agenti non devono modificare autonomamente l'autore degli articoli.

---

## 3. Persone associate alle fonti

Le persone associate alle fonti sono entità riutilizzabili.

Una stessa persona può essere associata a molte fonti.

Le informazioni relative alla persona devono essere mantenute una sola volta quando ciò è possibile.

Le fonti devono quindi riferire le persone tramite identificativi stabili invece di duplicarne i dati.

---

## 4. Identificativo

Ogni persona deve possedere un identificativo stabile.

L'identificativo deve essere:

- semplice;
- leggibile;
- coerente;
- stabile nel tempo;
- indipendente dal nome visualizzato.

Il nome della persona può essere corretto o modificato senza modificare necessariamente l'identità dell'entità.

---

## 5. Nome

Una persona può possedere:

- nome completo;
- nome visualizzato;
- forma bibliografica;
- eventuali forme alternative del nome.

La forma bibliografica può essere diversa dal nome visualizzato.

Il sistema deve conservare, quando disponibile, la forma utilizzata dalla fonte originale.

---

## 6. Alias

Una persona può essere conosciuta attraverso più forme del nome.

Gli alias possono comprendere:

- pseudonimi;
- varianti ortografiche;
- traslitterazioni;
- forme abbreviate;
- differenti convenzioni bibliografiche;
- nomi in differenti alfabeti;
- variazioni dovute a differenti sistemi di romanizzazione.

Gli alias devono essere associati alla stessa persona quando esistono evidenze sufficienti.

Gli agenti non devono creare automaticamente una nuova persona soltanto perché incontrano una variante del nome.

Allo stesso tempo, non devono unire automaticamente due persone differenti soltanto perché i nomi sono simili.

In caso di dubbio, l'agente deve proporre l'associazione e richiedere una decisione.

---

## 7. Verifica dell'identità

Quando un agente incontra una persona non ancora presente nel sistema, deve verificare se:

1. la persona esiste già nel repository;
2. il nome corrisponde a un alias esistente;
3. si tratta effettivamente di una nuova persona.

La verifica deve utilizzare le informazioni disponibili nella fonte e, quando necessario, ulteriori fonti affidabili.

---

## 8. Ricerca online

Quando esiste un dubbio sull'identità di una persona o sulla validità di un alias, l'agente può effettuare una ricerca online.

La ricerca deve privilegiare, quando disponibili:

- siti istituzionali;
- università;
- istituti di ricerca;
- ORCID;
- editori;
- DOI e metadati bibliografici;
- cataloghi bibliografici autorevoli;
- siti ufficiali della persona.

La ricerca online serve a raccogliere evidenze.

Non autorizza automaticamente l'agente a modificare l'entità.

Quando le evidenze non sono sufficienti, l'agente deve segnalare il caso per una decisione umana.

Le ricerche online devono essere proporzionate al problema e non devono consumare risorse inutilmente.

---

## 9. Informazioni biografiche

Le informazioni biografiche devono essere raccolte soltanto quando hanno un'utilità editoriale o bibliografica.

Non è necessario creare una biografia completa per ogni persona.

Quando sono necessarie, le informazioni devono essere ricavate preferibilmente da:

1. fonti primarie o istituzionali;
2. università o istituti di ricerca;
3. ORCID o registri professionali riconosciuti;
4. editori o cataloghi bibliografici autorevoli;
5. altre fonti secondarie affidabili.

È preferibile omettere un'informazione biografica piuttosto che introdurre un'informazione non verificata.

Informazioni fornite direttamente dal proprietario del progetto possono essere utilizzate come input senza effettuare nuovamente una ricerca quando questa non è necessaria.

---

## 10. Identificatori esterni

Quando disponibili, possono essere registrati identificatori esterni affidabili.

Esempi:

- ORCID;
- identificativi bibliografici;
- identificativi di cataloghi autorevoli;
- identificativi istituzionali.

Gli identificatori esterni non sostituiscono necessariamente l'identificativo interno del progetto.

Servono a facilitare disambiguazione e verifica.

---

## 11. Autori e traduttori

Una persona associata a una fonte può svolgere differenti ruoli bibliografici.

Tra questi possono rientrare:

- autore;
- curatore;
- traduttore;
- editore;
- altri ruoli bibliograficamente significativi.

Il ruolo è una proprietà della relazione tra persona e fonte, non dell'identità della persona.

Un traduttore non deve quindi essere trasformato in una categoria di persona separata.

Per StamoTenti è importante poter dare visibilità anche a chi ha tradotto un'opera, soprattutto nel caso di:

- testi filosofici;
- testi religiosi;
- testi storici;
- testi in lingue antiche;
- edizioni critiche;
- traduzioni accademiche.

Quando appropriato, la rappresentazione bibliografica deve poter mostrare sia l'autore dell'opera sia il traduttore.

Esempio concettuale:

Platone — traduzione di Mario Rossi

Platone e Mario Rossi rimangono due persone distinte, ma entrambe possono essere associate alla stessa fonte con ruoli differenti.

---

## 12. Più autori

Una fonte può avere più autori.

L'ordine degli autori deve essere preservato quando è significativo per la corretta rappresentazione bibliografica.

Gli agenti non devono riordinare arbitrariamente gli autori.

---

## 13. Autori anonimi o non identificati

Una fonte può non avere una persona identificabile come autore.

In questi casi non deve essere inventata una persona.

La fonte deve essere rappresentata secondo le informazioni bibliografiche effettivamente disponibili.

---

## 14. Identità incerte

Quando l'identità di una persona non può essere determinata con sufficiente sicurezza, l'agente deve mantenere l'incertezza invece di forzare un'identificazione.

La situazione può essere segnalata per revisione umana.

Non devono essere create relazioni definitive sulla base di una semplice somiglianza del nome.

---

## 15. Modifica manuale

Il proprietario del progetto deve poter modificare manualmente le informazioni sulle persone.

Deve poter:

- creare una persona;
- modificare un nome;
- aggiungere un alias;
- correggere un alias;
- collegare o scollegare un identificatore esterno;
- correggere informazioni biografiche;
- correggere una relazione con una fonte;
- correggere il ruolo di una persona.

Gli agenti non devono rendere obbligatorio il proprio utilizzo.

---

## 16. Informazioni fornite direttamente dal proprietario

Il proprietario può fornire direttamente:

- nome;
- alias;
- identificativi;
- informazioni biografiche;
- collegamenti;
- fonti;
- ruoli bibliografici;
- correzioni.

Quando queste informazioni sono sufficienti per risolvere il problema, l'agente non deve effettuare ricerche online inutili.

---

## 17. Principio di non duplicazione

Prima di creare una nuova persona, il sistema deve verificare se esiste già un'entità compatibile.

Prima di creare un nuovo alias, deve verificare se la variante è già presente.

Non devono essere create duplicazioni soltanto per differenze di:

- maiuscole/minuscole;
- ordine del nome;
- punteggiatura;
- traslitterazione;
- forma bibliografica;
- lingua.

Le differenze reali di identità devono invece essere preservate.

---

## 18. Persone e fonti

Una fonte deve riferire le persone tramite le entità definite nel sistema.

Le informazioni relative alle persone non devono essere duplicate nella scheda della fonte quando possono essere richiamate.

La fonte mantiene invece le informazioni specifiche dell'edizione o del documento e i ruoli bibliografici delle persone associate.

---

## 19. Persone e articoli

Gli articoli di StamoTenti sono normalmente attribuiti al proprietario del progetto.

Le persone associate alle fonti utilizzate negli articoli non devono essere trattate come autori dell'articolo.

Il sistema deve mantenere chiaramente distinti:

- autore dell'articolo;
- persone associate alle fonti;
- relativi ruoli bibliografici.

---

## 20. Regola per gli agenti

Quando un agente incontra una persona:

1. verifica se la persona esiste già;
2. verifica gli alias conosciuti;
3. verifica le informazioni disponibili nella fonte;
4. effettua una ricerca online solo quando utile;
5. privilegia fonti autorevoli;
6. evita di creare duplicati;
7. non forza un'identificazione incerta;
8. segnala i casi ambigui;
9. non modifica autonomamente informazioni controverse.

Quando il proprietario fornisce direttamente una soluzione, questa deve essere considerata un'informazione editoriale esplicita.

---

## 21. Principio di semplicità

Il sistema delle persone deve rimanere semplice.

Non devono essere introdotti prematuramente:

- ontologie delle persone;
- grafi genealogici;
- sistemi complessi di disambiguazione;
- database esterni obbligatori;
- servizi proprietari indispensabili.

La complessità può essere introdotta in futuro se la crescita del progetto ne dimostrerà la necessità.

---

## 22. Intervento umano

L'automazione deve assistere il proprietario del progetto, non sostituirlo.

Ogni informazione gestita dagli agenti deve poter essere verificata e modificata manualmente.

Il proprietario deve poter fornire direttamente informazioni o correggere il lavoro dell'agente senza essere vincolato al sistema automatico.

Quando l'agente non dispone di evidenze sufficienti, deve preferire una proposta da sottoporre al proprietario rispetto a una decisione irreversibile.

Il repository deve rimanere sempre utilizzabile anche senza gli agenti.

---

## 23. Gerarchia delle specifiche

In caso di conflitto:

1. TO-BE.md definisce la visione e i vincoli fondamentali;
2. CONTENT-MODEL.md definisce le entità e le relazioni;
3. AUTHOR-SPEC.md definisce la gestione delle persone;
4. SOURCE-SPEC.md definisce la gestione delle fonti;
5. le altre specifiche definiscono i comportamenti specialistici;
6. il codice implementa le specifiche approvate.

Il codice esistente non costituisce automaticamente una regola architetturale.

Se il codice contraddice una specifica approvata, deve essere considerato il codice da correggere, non la specifica.

