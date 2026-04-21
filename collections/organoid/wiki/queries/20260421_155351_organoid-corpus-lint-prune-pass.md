---
title: "Organoid corpus lint and prune pass"
status: active
created: 2026-04-21T15:53:51+09:00
---

# 100편 organoid corpus lint/prune pass

## Scope

- Goal: remove low-signal additions from the active organoid corpus without deleting raw PDFs.
- Rule: keep raw sources for traceability, but mark non-primary or non-article items as `status: pruned` so they drop out of the active source list and manifest.
- Run date: 2026-04-21

## Result

- Pruned in this pass: 3
- Active source pages remaining: 81
- Raw PDFs retained: yes

## Pruned sources

- [#17: Disease and Immunoprophylaxis Model of Human Nose Organoids to Study SARS-CoV-2 and RSV Infection](../sources/17_2021_17-disease-and-immunoprophylaxis-model-of-human-nose-organoids-to-study-sars-cov-2-and-rsv.md) - conference abstract supplement; evidence: `^#\d+:`
- [Application of an iPSC-Derived Organoid Model for Localized Scleroderma Therapy (Adv. Sci. 16/2022)](../sources/application_2022_application-of-an-ipsc-derived-organoid-model-for-localized-scleroderma-therapy-adv-sci-16.md) - cover or promotional blurb; evidence: `www.advancedscience.com`, `vol. issue cover without article body`
- [Brain Organoids to Study SARS-Cov-2 Infection of Developing CNS](../sources/l_2021_brain-organoids-to-study-sars-cov-2-infection-of-developing-cns.md) - conference abstract supplement; evidence: `abstracts\s*/`, `^[A-Z]{2,}\d{2}-\d{2}\b`

## Decision rule used in this pass

- Prune conference-supplement abstracts, poster/podium abstracts, and non-archival abstract pages.
- Prune review/minireview pages that do not function as primary evidence in this protocol-heavy corpus.
- Prune cover or promotional blurbs that are not the actual article text.

## What remains to watch

- Some retained papers may still be weak fits for a protocol-focused corpus even if they are full articles.
- Query and concept pages may still cite pruned source pages; the pages remain on disk so those links do not break, but they should not be used as first-choice evidence.
