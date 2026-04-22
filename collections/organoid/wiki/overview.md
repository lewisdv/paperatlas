# Overview

This collection currently contains 100 active organoid-related source pages. 78 are deep-ingested protocol pages, 22 are standard ingested pages, 0 remain queued, and 25 are pruned from the active corpus.

## What this collection is good for

- expanding organoid protocol coverage across developmental, patient-derived, assay-layer, transplantation, and engineering workflows
- comparing self-organization, directed patterning, and multi-lineage assembly strategies across organ systems
- identifying which papers are already deeply curated versus which newer additions still need a later deep-ingest pass
- keeping low-signal conference abstracts, cover pages, and review-only additions out of the active protocol corpus while retaining them for traceability
- navigating a now-better-linked concept layer for the refill cohort across adult or patient-derived access, coculture or transplantation, vascular induction, brain-subregion workflows, and engineering-on-chip stacks
- using the organoid collection as a practical protocol and assay-planning map rather than only a static bibliography

## Current source-page status

- Deep ingested: 78
- Standard ingested: 22
- Queued: 0

## Pruned source-page status

- Pruned from active corpus: 25

## Largest organ/system clusters

- brain: 21
- organoid-system: 8
- colon-intestine: 6
- kidney: 5
- tumor: 5
- liver: 4
- lung: 3
- midbrain: 3
- pancreas: 3
- brain assembloid: 2

## Working note

- New standard ingests are grounded in article metadata, abstract text, and raw-PDF scope extraction.
- Use the deep-ingested pages first when you need the most curated cross-paper framing.
- Recent concept-linking pulled the newest standard ingests into the concept pages, so `wiki/concepts/` is now a better first stop before browsing refill-era source pages one by one.
- A new manual deep-ingest pass promoted five refill-era papers into the curated tier, covering adult-organoid CRISPR engineering, South African intestinal PDO establishment, targeted viral delivery in midbrain organoids, orthogonal vascular programming, and Kupffer-integrated liver organoids.
- A second manual deep-ingest pass promoted six additional concept-anchor pages into the curated tier, covering prostate lentiviral perturbation, intestinal organ-on-chip, endometrial stromal coculture, multimodal-specimen PDO generation, esophageal organoid-initiated cancer models, and intestinal MSC-mediated repair assays.
- A third manual deep-ingest pass promoted six brain or immune concept anchors into the curated tier, covering murine cerebral baseline morphology, tonsil immune organoids, vaginal TRM coculture, eye-primordia forebrain organoids, cortico-striatal assembloids, and serotonergic neuromodulatory assembloids.
- A fourth manual deep-ingest pass promoted six adult-platform, imaging, and non-brain assay anchors into the curated tier, covering cholangiocyte-to-biliary-graft engineering, adult thymic TEC organoids, trophoblast CRISPR screening, MSI-ready organoid preparation, whole-mount clearing and 3D imaging, and Oropouche liver-organoid antiviral assays.
- A fifth manual deep-ingest pass promoted five adult-platform and assay papers into the curated tier, covering disease-stratified adult liver biobanking, primary placental trophoblast organoids, cervical epithelial niche divergence plus infection modeling, Toxoplasma sexual-stage induction on retinal or intestinal epithelial hosts, and monocyte-supported kidney differentiation.
- Pruned source pages remain in `wiki/sources/` with `status: pruned` so older cross-links do not break.
- Use `python3 scripts/wiki.py --collection organoid resume` to see the current backlog and latest query work.
