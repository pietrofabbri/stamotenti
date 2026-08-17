---
title: "Fixture Article"
description: "Technical article demonstrating the content model (DECISIONS/DR-08). Not real editorial content."
authors:
  - fixture-autore
sources:
  - fixture-fonte
sotto_area: SA-1-1
temi:
  - fixture-tema-tecnico
---

# Fixture Article

This article is technical demonstration content (see `DECISIONS/DR-08-content-fixture-system-proposal.md`), not real editorial content. It demonstrates, with dedicated non-real data, how the content model entities work.

It references a fixture author, a fixture source with its citation {{< cite "fixture-fonte" >}}, a real sotto-area (`SA-1-1`, a reference to a value already approved in `DECISIONS/DR-03-macroarea-sottoarea-model.md`, not a newly invented classification) and a technical fixture topic (`fixture-tema-tecnico`, an exception explicitly authorized by DR-08 to DR-04's "zero real topics").

## Link to Media

DR-01 (as extended by DR-06) has no direct Article → Media field in the front matter (an open question, see `PHASE-2-PLAN.md`). This article therefore references `fixture-media` (`data/media.yaml`) only indirectly: `fixture-media` has an optional `source_id: fixture-fonte` field (schema approved in `DECISIONS/DR-07-media-infrastructure-proposal.md`), and this article references `fixture-fonte` through its own `sources` field. The Article → Source → Media chain is therefore demonstrated; a direct Article → Media link remains undemonstrated, because no approved field for it exists yet.

This page is the English translation of `content/fixtures/articolo-fixture.md`, linked by Hugo's native filename-pairing mechanism (same base filename, `.en` suffix) — no `translationKey` field is used, since DR-01 explicitly excludes that field from the approved front matter contract until a dedicated decision is made.
