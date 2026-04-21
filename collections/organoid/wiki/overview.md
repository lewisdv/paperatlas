# Overview

This collection currently contains 79 active organoid-related source pages. 50 are deep-ingested protocol pages, 29 are standard ingested pages, 0 remain queued, and 21 are pruned from the active corpus.

## What this collection is good for

- expanding organoid protocol coverage across developmental, patient-derived, assay-layer, transplantation, and engineering workflows
- comparing self-organization, directed patterning, and multi-lineage assembly strategies across organ systems
- identifying which papers are already deeply curated versus which newer additions still need a later deep-ingest pass
- keeping low-signal conference abstracts, cover pages, and review-only additions out of the active protocol corpus while retaining them for traceability
- using the organoid collection as a practical protocol and assay-planning map rather than only a static bibliography

## Current source-page status

- Deep ingested: 50
- Standard ingested: 29
- Queued: 0

## Pruned source-page status

- Pruned from active corpus: 21

## Largest organ/system clusters

- brain: 18
- organoid system: 9
- kidney: 5
- tumor: 4
- colon intestine: 3
- liver: 3
- lung: 3
- breast: 2
- cancer: 2
- cervix: 2

## Working note

- New standard ingests are grounded in article metadata, abstract text, and raw-PDF scope extraction.
- Use the deep-ingested pages first when you need the most curated cross-paper framing.
- Pruned source pages remain in `wiki/sources/` with `status: pruned` so older cross-links do not break.
- Use `python3 scripts/wiki.py --collection organoid resume` to see the current backlog and latest query work.
