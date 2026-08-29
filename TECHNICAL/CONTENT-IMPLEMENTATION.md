# StamoTenti — Content Implementation

## Scopo

Descrive come il modello dei contenuti viene rappresentato nell'implementazione
Hugo corrente.

## Stato corrente

Il repository contiene attualmente:

- `content/_index.md` (home);
- `content/biblioteca/meditazione.md`;
- `content/privacy/_index.md`;
- `content/no-fuochi/_index.md`;
- `content/il-progetto/_index.md`.

`content/content.md` (placeholder Hugo iniziale del 12 agosto 2026, non
collegato a nessuna voce di menu) è stato rimosso il 2026-08-29 in
occasione dell'aggiunta delle pagine di shell sopra.

Le tre nuove pagine (`privacy/`, `no-fuochi/`, `il-progetto/`) esistono
oggi solo in italiano — nessuna traduzione EN. `header.html`/`footer.html`
linkano a queste con percorsi assoluti fissi (non `relLangURL`), proprio
per questo: da una pagina EN, `relLangURL` costruirebbe un percorso
`/en/...` inesistente. Rivedere quando esisteranno le traduzioni.

## Front matter

Il contenuto corrente utilizza campi come:

- title;
- description;
- date;
- draft;
- authors;
- sources;
- tags;
- temi.

I campi effettivamente utilizzati possono evolvere con il modello editoriale.

## Corpo del contenuto

Il titolo di una pagina è responsabilità del front matter (`title`) e del
template (`layouts/_default/single.html`/`list.html` rendono
`<h1>{{ .Title }}</h1>`).

Il corpo Markdown di un articolo **non deve ripetere il titolo come
intestazione di primo livello** (`# Titolo`): produrrebbe un secondo
`<h1>` identico sulla stessa pagina, in tensione con ACCESSIBILITY-SPEC.md
§9 ("ogni pagina significativa deve avere una gerarchia di titoli
coerente"). Il corpo deve iniziare direttamente dal testo o, se servono
sotto-sezioni, da `##` (H2) in giù.

Trovato e corretto il 2026-08-19 (audit Gate 2) sull'unico contenuto
reale esistente (`content/biblioteca/meditazione.md`) e sulla fixture
(`content/fixtures/articolo-fixture.md`/`.en.md`), che ripetevano
entrambi il titolo come `#` nel corpo.

## Relazione con il modello

CONTENT-MODEL.md e ARTICLE-SPEC.md definiscono il modello concettuale.

Questo documento descrive soltanto la sua rappresentazione tecnica corrente.

## Regola

Un campo deve essere introdotto nell'implementazione quando esiste una
necessità prevista dal modello o dal workflow.

La presenza di un campo nel codice non costituisce automaticamente una nuova
regola editoriale.
