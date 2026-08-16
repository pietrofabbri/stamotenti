# StamoTenti — Quality & Operations Summary

## Scopo

Questo documento riassume testing, monitoring, qualità, manutenzione e
gestione operativa.

Non sostituisce TESTING-SPEC.md, MONITORING-SPEC.md, BACKUP-SPEC.md,
CHANGE-MANAGEMENT-SPEC.md, DECISION-SPEC.md, SEO-SPEC.md o
OPERATIONAL-MEMORY-SPEC.md.

## Testing

Si testa ciò che può ragionevolmente rompersi.

La profondità è proporzionata a:

- rischio;
- impatto;
- complessità;
- sensibilità dei dati;
- reversibilità.

Possono essere usati:

- test automatici;
- test manuali;
- smoke test;
- test di integrazione;
- test end-to-end;
- test privacy;
- test sicurezza;
- test accessibilità;
- test SEO/GEO;
- restore test.

Un test riuscito riduce il rischio ma non equivale ad approvazione.

## Monitoring

Si monitora ciò che può produrre un'informazione utile.

Il monitoraggio deve evitare:

- polling inutile;
- rumore;
- notifiche ripetitive;
- raccolta personale non necessaria;
- conclusioni eccessive da dati incompleti.

Un controllo fallito deve essere distinto da un controllo riuscito senza problemi.

## SEO e GEO

SEO e GEO devono favorire:

- reperibilità;
- comprensione;
- accessibilità;
- verificabilità;
- correttezza dei metadata;
- collegamenti tra contenuti.

Non devono manipolare motori di ricerca o sistemi AI.

## Backup e recovery

Un backup non è considerato affidabile soltanto perché esiste.

I dati importanti devono poter essere ripristinati quando necessario.

La protezione del backup deve essere coerente con quella dei dati originali.

## Decisioni

Le decisioni importanti devono conservare il perché.

Le decisioni superate non devono essere cancellate quando la loro storia
rimane utile.

## Memoria operativa

La memoria conserva esperienza pratica.

Può alimentare proposte di modifica alle SPEC.

Non può modificarle autonomamente.

## Change management

Una modifica significativa deve poter essere:

- identificata;
- valutata;
- testata;
- approvata quando necessario;
- applicata;
- verificata.

Il controllo deve essere proporzionato al rischio.

## Principio operativo

La qualità serve a rendere più sicuro cambiare StamoTenti, non a impedire
l'evoluzione del progetto.
