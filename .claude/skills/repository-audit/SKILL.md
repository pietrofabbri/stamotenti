# Repository Audit

## Scopo

Eseguire una diagnosi del repository StamoTenti senza modificare il sito.

## Procedura

1. Leggere `CLAUDE.md`.
2. Leggere `CLAUDE-CODE-DEVELOPMENT-ROADMAP.md`.
3. Consultare `PROJECT-MAP.md`.
4. Consultare i SUMMARY pertinenti.
5. Consultare `DEPENDENCY-MAP.md`.
6. Consultare le SPEC pertinenti.
7. Consultare i documenti TECHNICAL pertinenti.
8. Eseguire `python3 scripts/repository-doctor.py`.
9. Analizzare Git status e diff.
10. Produrre un report.

## Divieti

La skill non deve:

- modificare `content/`;
- modificare `data/`;
- modificare `layouts/`;
- modificare `hugo.toml`;
- fare commit;
- fare push;
- fare deploy;
- inviare email;
- cancellare file.

## Output

Il report deve contenere:

- stato repository;
- build;
- struttura;
- problemi;
- warning;
- SPEC coinvolte;
- raccomandazione del prossimo passo.

Non applicare automaticamente la raccomandazione.
