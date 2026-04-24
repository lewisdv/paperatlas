# Overview

This collection currently contains 96 active organoid-related source pages. All 96 are deep-ingested protocol pages, 0 remain at standard-ingest level, 0 remain queued, and 29 are pruned from the active corpus.

## What this collection is good for

- expanding organoid protocol coverage across developmental, patient-derived, assay-layer, transplantation, and engineering workflows
- comparing self-organization, directed patterning, and multi-lineage assembly strategies across organ systems
- treating the active corpus as a fully curated deep-ingested layer rather than a mix of curated and generic source pages
- keeping low-signal conference abstracts, cover pages, and review-only additions out of the active protocol corpus while retaining them for traceability
- navigating a now-better-linked concept layer for the refill cohort across adult or patient-derived access, coculture or transplantation, vascular induction, brain-subregion workflows, and engineering-on-chip stacks
- using the organoid collection as a practical protocol and assay-planning map rather than only a static bibliography
- using a new synthesis-level design playbook to jump from question type to baseline choice, assay layer, and escalation order

## Current source-page status

- Deep ingested: 96
- Standard ingested: 0
- Queued: 0

## Pruned source-page status

- Pruned from active corpus: 29

## Entity-page status

- Entity pages: 29
- Coverage now includes PDO, PDO-X, CRISPR editing, calcium imaging, host circuit engagement, MEA readouts, polarity inversion, microinjection, organ-on-chip, BBB spheroids, biobanking or freeze-thaw QC, stand-alone vascular organoids, ETV2-driven vascular induction, mesodermal progenitor mixing, stem-cell-derived islets, assembloids and regional fusion, single-cell atlas benchmarking, adult tissue-derived epithelial organoids, host-context transplantation and repair validation, nephron-patterning kidney organoids, whole-mount 3D clearing and imaging, morphology segmentation and descriptor analysis, reproductive mucosal epithelial organoids, distal lung organoids, heart-forming organoids, foregut-midgut regionalization from hPSCs, sensory ectoderm and appendage organoids, OCT, and NLRP3 inflammasome

## Largest organ/system clusters

- brain: 17
- colon-intestine: 6
- kidney: 5
- organoid-system: 5
- liver: 4
- pancreas: 4
- breast: 3
- heart: 3
- lung: 3
- midbrain: 3
- retina: 3
- tumor: 3

## Working note

- The active source layer is fully curated: all active source pages are deep-ingested, and the old generic placeholder tier is gone.
- Start from `wiki/index.md`, not from raw source pages. The index is now organized by browsing role across concepts, queries, syntheses, and entities.
- For branch choice, begin with the concept layer. Most concept pages now act as short branching maps rather than parallel mini-reviews.
- For decision support, the three best first syntheses are `wiki/syntheses/20260422_organoid-project-design-playbook.md`, `wiki/syntheses/20260423_organoid-assay-escalation-and-validation-playbook.md`, and `wiki/syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md`.
- The April 23 query burst has already been folded back into the syntheses and concept pages, so the saved queries are now better treated as drill-down pages than as the only place where decision rules live.
- A new developmental-baseline synthesis now separates baseline route choice from assay escalation: it compresses self-organization versus directed patterning, brain subregion choice, endodermal regionalization, sensory ectoderm branches, and early multi-lineage developmental baselines into one page.
- The entity layer is now operational, not decorative. Repeated platforms, access methods, readouts, and validation endpoints have dedicated pages and are grouped in the index as first-stop anchors, platform anchors, tools, readouts, and validation endpoints.
- Entity back-links now cover the highest-value translational, assay, brain, kidney, imaging, vascularization, and access branches; follow-up cleanups also threaded atlas-benchmarking links into more brain baseline and midbrain-screening pages, donor-baseline links into the tonsil immune branch, and new developmental anchors into endodermal and sensory-ectoderm pages, so remaining gaps are increasingly concentrated in only a few niche baselines.
- Pruned source pages remain in `wiki/sources/` with `status: pruned`, so older cross-links still resolve and pruning remains auditable.
- Use `python3 scripts/wiki.py --collection organoid resume` when context disappears or when you want the latest backlog, counts, and recent structural changes.
