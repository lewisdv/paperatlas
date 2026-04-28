# Workflow Checkpoint

Read this file first when chat context disappears.

## Mission

Keep `paper_collect` usable as a persistent LLM-maintained research wiki:

- `raw/` stays immutable
- `wiki/` is the maintained knowledge layer
- collection work stays collection-scoped unless the user explicitly asks for outside knowledge
- good answers should be saved back into `wiki/queries/` or `wiki/syntheses/`

## What Already Works

- `scripts/wiki.py` manages collection scaffolding, source registration, OpenDataLoader parsing, query creation, status checks, and context recovery via `resume`.
- `scripts/render_wiki_html.py`, `scripts/serve_wiki_html.py`, `scripts/watch_wiki_html.py`, and `scripts/site_runtime.py` support HTML rendering plus local browsing.
- `scripts/export_github_pages.py` supports static export for GitHub Pages.
- `AGENTS.md` already encodes the knowledge-base-first ingest/query/lint workflow.
- `collections/Organoid/` is the most mature collection and is the current best place to continue building the workflow.

## Current State As Of 2026-04-24

Main active collection: `collections/Organoid`

- 125 raw sources
- 125 OpenDataLoader-derived helper folders
- 96 active source pages
- 29 pruned source pages retained for traceability
- 96 deep-ingested active source pages
- 0 standard-ingested active source pages
- 12 concept pages
- 29 query pages
- 4 synthesis pages
- 29 entity pages

Recent organoid progress:

- 2026-04-09: deep ingest completed for the main protocol corpus and gap-filling rounds.
- 2026-04-10 to 2026-04-12: pending brain-subregion sources were parsed and folded into the wiki.
- 2026-04-20: the collection shifted from pure ingest into decision-oriented query synthesis, adding 15 new query pages around platform choice, assay layering, vascularization, translational screening, escalation, and recovery logic.
- 2026-04-21: the corpus was first expanded from 58 to 100 raw/source-page entries, all 100 PDFs were parsed with OpenDataLoader, and the organoid manifest was rebuilt to 100 rows.
- 2026-04-21: a lint/prune pass marked 21 low-signal additions as `status: pruned` while keeping their raw PDFs and source pages for traceability; the active manifest temporarily dropped to 79 sources.
- 2026-04-21: `scripts/expand_organoid_to_100.py` was fixed to use Europe PMC open-access PDF discovery without the over-restrictive `SRC:PMC` filter, which restored many missed MED-indexed but PMCID-backed papers.
- 2026-04-21: the active corpus was refilled from 79 to 100 with additional protocol-heavy full-text papers across intestinal, retinal, endometrial, pancreatic, prostate, thymic, vascular, cerebral, midbrain, liver, trophoblast, tonsil immune, and vaginal epithelial organoid settings.
- 2026-04-21: a second prune pass removed one new conference-abstract supplement, then one replacement paper was added and parsed; the current state is 125 raw / 125 parsed / 100 active / 25 pruned.
- 2026-04-22: a manual deep-ingest pass promoted 5 refill-era protocol pages from generic summaries into curated protocol notes, raising the active corpus to 55 deep-ingested pages and reducing standard-ingested pages to 45.
- 2026-04-22: a second manual deep-ingest pass promoted 6 additional concept-anchor refill pages, raising the active corpus to 61 deep-ingested pages and reducing standard-ingested pages to 39.
- 2026-04-22: a third manual deep-ingest pass promoted 6 brain and immune concept-anchor pages, raising the active corpus to 67 deep-ingested pages and reducing standard-ingested pages to 33.
- 2026-04-22: a fourth manual deep-ingest pass promoted 6 adult-platform, imaging, and non-brain assay anchors, raising the active corpus to 73 deep-ingested pages and reducing standard-ingested pages to 27.
- 2026-04-22: a fifth manual deep-ingest pass promoted 5 adult translational and infection-assay anchors, raising the active corpus to 78 deep-ingested pages and reducing standard-ingested pages to 22.
- 2026-04-22: a sixth manual deep-ingest pass promoted 5 barrier and imaging readout anchors, raising the active corpus to 83 deep-ingested pages and reducing standard-ingested pages to 17.
- 2026-04-22: a seventh manual deep-ingest pass promoted 4 neural disease and regeneration anchors, raising the active corpus to 87 deep-ingested pages and reducing standard-ingested pages to 13.
- 2026-04-22: an eighth manual deep-ingest pass promoted 5 translational cancer and PDO-X anchors, raising the active corpus to 92 deep-ingested pages and reducing standard-ingested pages to 8.
- 2026-04-22: a ninth manual deep-ingest pass promoted 3 additional anchors, raising the active corpus to 95 deep-ingested pages and reducing standard-ingested pages to 5.
- 2026-04-22: a targeted cleanup pass pruned 4 remaining low-signal standard pages and deep-ingested the retained heart macrophage assembloid paper, leaving the active corpus at 96 deep-ingested pages and 0 standard pages.
- 2026-04-22: a synthesis pass added `collections/Organoid/wiki/syntheses/20260422_organoid-project-design-playbook.md`, consolidating the design-oriented query burst into one baseline-selection, assay-layer, complexity, and escalation playbook.
- 2026-04-22: a first entity pass added 5 entity pages for repeated platforms and tools, covering PDO-X, CRISPR editing, MEA readouts, OCT, and the NLRP3 inflammasome.
- 2026-04-22: an entity-threading pass linked those entity pages back into representative source pages and the project-design playbook, making the entity layer usable from normal browsing flows.
- 2026-04-23: a second entity pass added 4 more pages for PDO baselines, organ-on-chip, calcium imaging, and host-circuit engagement, then threaded them into brain-readout, screening, escalation, and representative source pages.
- 2026-04-23: a follow-up source-threading pass linked those newer entities into additional patient-derived cancer, multimodal-specimen PDO, gastrointestinal access, kidney perfusion-chip, and brain benchmarking source notes.
- 2026-04-23: a new saved query added an access-route decision page comparing when to use polarity inversion, standard microinjection, organ-on-chip, or BBB spheroids for barrier and infection studies.
- 2026-04-23: a second new saved query added a PDO-readiness rubric for treatment-guidance screening, connecting specimen logistics, bankability, thaw recovery, fidelity checks, and endpoint credibility into one operational gate set.
- 2026-04-23: a third new saved query separated donor-derived cancer escalation into compact ex vivo validation, immune reconstruction, and PDO-X, clarifying when each branch is the right stopping point.
- 2026-04-23: a fourth new saved query compared screening-stack design across pancreas, intestine, BBB, and lung systems, showing that each organ's first bottleneck differs.
- 2026-04-23: a fifth new saved query mapped vascularization routes by organ and endpoint, separating flow, TF-driven vascularization, mesodermal mixing, stand-alone vessel baselines, and host transplantation.
- 2026-04-23: a consolidation pass folded the new April 23 query burst back into the project-design playbook plus the adult-platform, engineering-screening, functional-assay, gastrointestinal, and vascularization concept pages.
- 2026-04-23: a third entity pass added four more pages for polarity inversion, microinjection, BBB spheroids, and biobanking or freeze-thaw QC, then threaded them into the access-route and PDO-readiness branches.
- 2026-04-23: a fourth entity pass added `stand-alone vascular organoids`, `ETV2-driven vascular induction`, `mesodermal progenitor cell mixing`, and `stem-cell-derived islets`, pushing the entity layer farther into older canonical vascularization and pancreas-screening source pages.
- 2026-04-23: a fifth entity pass added `assembloids and regional fusion` plus `single-cell atlas benchmarking`, pushing the entity layer farther into older brain patterning, circuit-assembly, and fidelity-benchmark source pages.
- 2026-04-23: a sixth entity pass added `adult tissue-derived epithelial organoids` plus `host-context transplantation and repair validation`, pushing the entity layer farther into older liver, biliary, placental, intestinal, and host-escalation source pages.
- 2026-04-23: a seventh entity pass added `nephron-patterning kidney organoids`, `whole-mount 3D clearing and imaging`, and `morphology segmentation and descriptor analysis`, pushing the entity layer farther into older kidney baselines and readout-heavy imaging sources.
- 2026-04-23: an eighth entity pass added `reproductive mucosal epithelial organoids`, `distal lung organoids`, and `heart-forming organoids`, pushing the entity layer farther into older reproductive-tract, lung, and cardiac baseline sources.
- 2026-04-23: a long-tail cleanup pass then threaded existing entities into additional source pages for canine epithelial disease induction, early pancreas morphogenesis, tumor-T-cell coculture, monocyte-supported kidney differentiation, esophageal organoid-initiated mouse models, liver antiviral assays, vaginal T-cell coculture, and NSCLC PDO modeling without adding more entity pages.
- 2026-04-23: two additional long-tail cleanup passes threaded existing entities into brain infection, regenerative transplantation, cervical cancer escalation, adult thymic TEC, inner-ear imaging, Kupffer-bearing liver, foundational cerebral baseline, precursor-state cerebral, intestinal repair, and host-pathogen access pages, reducing the remaining no-entity active pages to a smaller niche baseline set.
- 2026-04-23: a new synthesis page added `collections/Organoid/wiki/syntheses/20260423_organoid-assay-escalation-and-validation-playbook.md`, compressing maturity rescue, access fixes, coculture, host validation, and donor-derived cancer escalation into one narrower decision ladder.
- 2026-04-24: consolidation passes shortened most major concept pages into cleaner entry points and reorganized `collections/Organoid/wiki/index.md` by browsing role across concepts, queries, syntheses, and entities.
- 2026-04-24: `collections/Organoid/wiki/overview.md` was compressed to foreground the current entry layer and live navigation rules rather than carrying the full historical buildout as one long note.
- 2026-04-24: two new entity pages, `foregut-midgut regionalization from hPSCs` and `sensory ectoderm and appendage organoids`, were added to absorb long-tail developmental baselines across gastric, intestinal, hepato-biliary-pancreatic, retinal, inner-ear, and skin branches.
- 2026-04-24: a fourth synthesis page, `collections/Organoid/wiki/syntheses/20260424_organoid-developmental-baseline-and-regionalization-playbook.md`, was added to compress developmental route selection across self-organization, directed patterning, brain subregions, endodermal regionalization, sensory ectoderm, and early multi-lineage baselines.
- 2026-04-24: a follow-up consolidation pass added direct synthesis links back into the brain-patterning, brain-subregion, self-organization, GI-endoderm, and multi-lineage concept pages, plus the most relevant developmental query pages, so the new developmental playbook now acts as the first-stop page for that branch.
- 2026-04-21: helper scripts were added for context recovery and batch expansion:
  - `scripts/expand_organoid_to_100.py`
  - `scripts/generic_ingest_organoid_sources.py`
  - `scripts/lint_prune_organoid_corpus.py`
  - `scripts/rebuild_organoid_manifest.py`
  - `scripts/wiki.py ... resume`

Other collections:

- `collections/Multi_Omics/` now holds the former long-read starter corpus and is the next-best candidate for expansion beyond the Organoid reference collection.
- `collections/Deeplearning_Model/` is still scaffold-level and not yet the current focus.

## Resume In 60 Seconds

1. Run `python3 scripts/wiki.py --collection Organoid resume`
2. Read `collections/Organoid/wiki/overview.md`
3. Read `collections/Organoid/wiki/index.md`
4. Read `collections/Organoid/wiki/log.md`
5. Open the newest query pages if continuing synthesis:
   - `collections/Organoid/wiki/queries/20260423_1626_vascularization-routes-by-organ-and-question.md`
   - `collections/Organoid/wiki/queries/20260423_1620_organ-specific-screening-stacks-pancreas-intestine-bbb-lung.md`
   - `collections/Organoid/wiki/queries/20260423_1600_compact-ex-vivo-vs-immune-reconstruction-vs-pdo-x.md`
   - `collections/Organoid/wiki/queries/20260423_1554_pdo-readiness-rubric-for-treatment-guidance-screening.md`
   - `collections/Organoid/wiki/queries/20260423_1408_access-route-selection-for-barrier-and-infection-studies.md`
   - `collections/Organoid/wiki/queries/20260422_185044_organoid-corpus-lint-prune-pass.md`
   - `collections/Organoid/wiki/queries/20260421_203208_organoid-corpus-lint-prune-pass.md`
   - `collections/Organoid/wiki/queries/20260420_191749_coculture-vs-host-validation-for-interaction-questions.md`
   - `collections/Organoid/wiki/queries/20260420_191750_organ-specific-assay-recovery-playbook.md`
   - `collections/Organoid/wiki/queries/20260420_191751_disease-specific-organoid-escalation-ladders.md`
6. Stay inside `collections/Organoid/wiki/` and `collections/Organoid/raw/` unless the user explicitly asks for outside knowledge or web research.

## Known Organoid Backlog

There is no raw-source backlog right now:

- every `raw/sources/*.pdf` file has a matching `wiki/sources/*.md` page
- every source has an OpenDataLoader helper folder under `raw/derived/opendataloader/`

Current backlog is quality-oriented rather than ingestion-oriented:

- the first weak-candidate prune pass is now saved in `collections/Organoid/wiki/queries/20260421_153718_organoid-corpus-lint-prune-pass.md`
- `scripts/expand_organoid_to_100.py` now counts only non-pruned source pages toward the target when future quality passes reduce the active set
- raw-source growth now outpaces concept/entity maintenance, so the main gap is linking and consolidation rather than ingestion
- the active source layer is now fully deep-ingested, so backlog has shifted from source-page cleanup to concept/entity consolidation
- the most recent cleanup rationale is saved in `collections/Organoid/wiki/queries/20260422_185044_organoid-corpus-lint-prune-pass.md`
- the decision-query burst is now also condensed into `collections/Organoid/wiki/syntheses/20260422_organoid-project-design-playbook.md`
- the entity layer now covers two passes and is threaded into representative source and query pages, but broader back-link coverage across the full corpus is still incomplete
- the entity layer now covers three passes and includes access-route and PDO-operations entities, but broader back-link coverage across older source pages is still incomplete
- the entity layer now covers four passes and now includes older canonical vascularization and pancreas-screening methods, but many active source pages still lack explicit `Related entities` sections
- the entity layer now covers five passes and now includes dedicated brain assembly and atlas-benchmark entities, but many active source pages still lack explicit `Related entities` sections outside the best-developed branches
- the entity layer now covers six passes and now includes mature epithelial baseline and cross-domain host-validation entities, but many active source pages still lack explicit `Related entities` sections outside the best-developed branches
- the entity layer now covers seven passes and now includes kidney baseline and imaging-stack shortcuts, but many active source pages still lack explicit `Related entities` sections outside the best-developed branches
- the entity layer now covers eight passes and now includes lighter reproductive, lung, and cardiac baseline anchors, but many active source pages still lack explicit `Related entities` sections outside the best-developed branches
- after that expansion, cleanup has shifted toward threading existing entities into the remaining long-tail source pages rather than minting new entity pages for every niche branch
- the long-tail cleanup pass now also covers brain infection, regenerative transplantation, cervical cancer escalation, adult thymic TEC, inner-ear imaging, and Kupffer-bearing liver pages, so the remaining browsing gap is narrower and increasingly concentrated in niche baseline protocols rather than major active branches
- a follow-up cleanup pass now also covers foundational cerebral baselines, precursor-state cerebral assays, intestinal repair, and host-pathogen access papers, so most of the remaining no-entity pages are lightweight developmental baselines rather than translational or assay-anchor sources
- a further cleanup pass now threads `single-cell atlas benchmarking` into additional brainstem, cerebral, hippocampal, telencephalic, hindbrain, and midbrain baseline pages, so the remaining no-entity set is narrower and even more concentrated in niche non-anchor baselines
- another selective cleanup pass now threads `single-cell atlas benchmarking` into murine cerebral and cerebellar baseline pages and connects the donor-built tonsil immune organoid page to `adult tissue-derived epithelial organoids`, narrowing the remaining no-entity set without expanding the taxonomy
- a final long-tail entity pass now adds `foregut-midgut regionalization from hPSCs` and `sensory ectoderm and appendage organoids`, which absorb six lingering developmental baseline pages and leave only a very small residual no-entity set
- synthesis work has now expanded beyond general design and assay escalation into developmental baseline choice itself, so the synthesis layer is becoming a fuller first-stop browsing surface rather than just a summary of April 20-23 decision queries
- the developmental branch is now partially folded back into the synthesis layer: the older platform-selection, brain-subregion, brain-benchmarking, and complexity queries remain useful as drill-down pages, but the default starting point is now the developmental-baseline playbook
- recent work improved source-page back-links in the patient-derived cancer, GI access-device, and brain benchmarking branches, but many older source pages still lack entity shortcuts
- the newest saved query now covers access-route choice for barrier and infection studies, reducing overlap between ad hoc conversations about polarity inversion, chip systems, BBB spheroids, and microinjection
- the newest two saved queries now also cover treatment-guidance PDO readiness and barrier or infection access-route choice, so the current backlog is shifting from basic decision rules toward more comparative translational strategy pages
- the newest five saved queries now cover treatment-guidance PDO readiness, donor-derived cancer escalation stops, barrier or infection access-route choice, organ-specific screening-stack design, and vascularization-route choice, so the current backlog is shifting away from high-value missing query pages and back toward consolidation
- that consolidation has now started: the new decision rules have been folded into the playbook and several concept pages, making `wiki/concepts/` and the main synthesis more useful starting points again
- a narrower synthesis now also exists for assay escalation itself: `collections/Organoid/wiki/syntheses/20260423_organoid-assay-escalation-and-validation-playbook.md` compresses maturity rescue, access fixes, coculture, host validation, and donor-derived cancer escalation into one reusable decision ladder
- the next consolidation step has also started: the adult-platform, functional-assay, and engineering-screening concept pages have been shortened so they work more like distinct entry points into the escalation playbook rather than parallel full-length summaries of the same query set
- a second consolidation step has now done the same for the brain-patterning, brain-benchmarking, GI-endoderm, vascularization, self-organization, and multi-lineage concept pages, so most major concept pages now act as concise branching maps into the syntheses rather than overlapping mini-reviews
- an index cleanup pass now matches that structure: `collections/Organoid/wiki/index.md` groups concepts, queries, and syntheses by browsing role, so the entry layer is no longer a flat archive and instead points readers first toward the most reusable decision pages
- the same browsing-order cleanup now also covers entities: `collections/Organoid/wiki/index.md` separates first-stop entities, platform anchors, engineering tools, readout entities, and validation endpoints, so the entry layer is now consistently role-based across the wiki
- `collections/Organoid/wiki/overview.md` is now compressed around the current entry layer and live workflow state, so it is again a useful first read after `resume` instead of mostly serving as a long historical changelog

## Good Next Moves

- Continue selective entity back-link cleanup for the remaining niche baseline source pages, but avoid minting new entity pages unless a branch clearly repeats across multiple sources.
- Consider one more synthesis-level consolidation if several saved queries still feel more useful than the current playbooks.
- Consider folding the remaining high-value developmental queries more explicitly into the new developmental-baseline synthesis if the query layer still feels more detailed than the synthesis layer in that branch.
- Keep `wiki/overview.md`, `wiki/index.md`, and `wiki/log.md` synchronized after each consolidation or entity-threading batch.

## Good Query Candidates

- No obvious high-priority missing query page remains in the original backlog; the next step is more likely consolidation, entity expansion, or synthesis folding rather than another first-order decision query.

## Prompt Pattern For Future Codex

```text
Read WORKFLOW_CHECKPOINT.md, then run `python3 scripts/wiki.py --collection Organoid resume`.
Use only collections/Organoid/wiki and collections/Organoid/raw unless I explicitly ask for outside knowledge.
If the wiki is incomplete, open the relevant raw source files, repair the wiki, and then answer.
When the answer is substantial, save it back into wiki/queries/ or wiki/syntheses/.
```
