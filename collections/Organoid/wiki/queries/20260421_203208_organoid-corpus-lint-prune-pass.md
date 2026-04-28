---
title: "Organoid corpus lint and prune pass"
status: active
created: 2026-04-21T20:32:08+09:00
---

# 100편 organoid corpus lint/prune pass

## Scope

- Goal: remove low-signal additions from the active organoid corpus without deleting raw PDFs.
- Rule: keep raw sources for traceability, but mark non-primary or non-article items as `status: pruned` so they drop out of the active source list and manifest.
- Run date: 2026-04-21

## Result

- Pruned in this pass: 1
- Active source pages remaining: 99
- Raw PDFs retained: yes

## Pruned sources

- [Protocol for establishing genetically engineered murine lung organoids mimicking cell plasticity and regeneration.](../sources/b_2025_protocol-for-establishing-genetically-engineered-murine-lung-organoids-mimicking-cell-plas.md) - conference abstract supplement; evidence: `^[A-Z]{2,4}\d{2,}(?:\s+\|\s+[A-Z]{2,8}\d{2,})?\s+[A-Z]`

## Decision rule used in this pass

- Prune conference-supplement abstracts, poster/podium abstracts, and non-archival abstract pages.
- Prune review/minireview pages that do not function as primary evidence in this protocol-heavy corpus.
- Prune cover or promotional blurbs that are not the actual article text.

## What remains to watch

- Some retained papers may still be weak fits for a protocol-focused corpus even if they are full articles.
- Query and concept pages may still cite pruned source pages; the pages remain on disk so those links do not break, but they should not be used as first-choice evidence.
