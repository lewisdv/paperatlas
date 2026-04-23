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

- Entity pages: 9
- Coverage now includes PDO, PDO-X, CRISPR editing, calcium imaging, host circuit engagement, MEA readouts, organ-on-chip, OCT, and NLRP3 inflammasome

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

- The active source layer is now fully deep-ingested; generic auto-ingest placeholders have either been promoted or pruned.
- Use the deep-ingested pages first when you need the most curated cross-paper framing.
- Earlier concept-linking pulled the refill-era source pages into the concept pages, so `wiki/concepts/` is now a better first stop before browsing source pages one by one.
- A new manual deep-ingest pass promoted five refill-era papers into the curated tier, covering adult-organoid CRISPR engineering, South African intestinal PDO establishment, targeted viral delivery in midbrain organoids, orthogonal vascular programming, and Kupffer-integrated liver organoids.
- A second manual deep-ingest pass promoted six additional concept-anchor pages into the curated tier, covering prostate lentiviral perturbation, intestinal organ-on-chip, endometrial stromal coculture, multimodal-specimen PDO generation, esophageal organoid-initiated cancer models, and intestinal MSC-mediated repair assays.
- A third manual deep-ingest pass promoted six brain or immune concept anchors into the curated tier, covering murine cerebral baseline morphology, tonsil immune organoids, vaginal TRM coculture, eye-primordia forebrain organoids, cortico-striatal assembloids, and serotonergic neuromodulatory assembloids.
- A fourth manual deep-ingest pass promoted six adult-platform, imaging, and non-brain assay anchors into the curated tier, covering cholangiocyte-to-biliary-graft engineering, adult thymic TEC organoids, trophoblast CRISPR screening, MSI-ready organoid preparation, whole-mount clearing and 3D imaging, and Oropouche liver-organoid antiviral assays.
- A fifth manual deep-ingest pass promoted five adult-platform and assay papers into the curated tier, covering disease-stratified adult liver biobanking, primary placental trophoblast organoids, cervical epithelial niche divergence plus infection modeling, Toxoplasma sexual-stage induction on retinal or intestinal epithelial hosts, and monocyte-supported kidney differentiation.
- A sixth manual deep-ingest pass promoted five barrier and imaging readout papers into the curated tier, covering BBB permeability organoids, printed-tumor OCT growth tracking, 13-day breast-cancer OCT tracking, convexity-preserving PDAC segmentation, and cross-system shape-factor morphology analysis.
- A seventh manual deep-ingest pass promoted four neural disease and regeneration anchors into the curated tier, covering a cerebral NLRP3 inflammasome slice assay, a Down-syndrome choroid-plexus SARS-CoV-2 model, retinal injury-induced hNRSC isolation with rd10 transplantation, and cerebral pNSC or dNSC precursor-state assays.
- An eighth manual deep-ingest pass promoted five translational cancer and PDO-X anchors into the curated tier, covering cervical SCNEC tri-model derivation, MALAT1-targeted breast PDO-X escalation, osteosarcoma immune-reconstructed iOS biobanking, metastatic PDO kinome restoration after host engraftment, and XIAP-targeted cisplatin sensitization in colon cancer organoids.
- A ninth manual deep-ingest pass promoted three protocol-and-assay pages into the curated tier, covering Th2-driven canine epidermal disease induction, an imageable Matrigel-overlay pancreas morphogenesis system, and ODE-based quantitative modeling of NSCLC patient-derived organoid composition.
- A final remaining-standard cleanup pass pruned four low-signal leftovers and deep-ingested one retained heart macrophage assembloid paper, so the active corpus now sits at 96 deep-ingested pages with no standard pages left.
- A new synthesis page now condenses the 2026-04-20 decision-query burst into one project-design playbook covering baseline choice, compensation priority, complexity control, organ-specific recovery, and disease-specific escalation.
- A new access-route query now separates four often-confused assay choices: polarity inversion, standard microinjection, organ-on-chip, and BBB spheroids are now framed as different answers to different barrier or infection bottlenecks rather than interchangeable technologies.
- A first entity pass now captures repeated platforms and tools as dedicated pages, so the collection no longer relies only on source, concept, query, and synthesis layers.
- A follow-up entity-threading pass now links those entity pages back into representative source notes and the project-design playbook, making the entity layer useful during normal browsing rather than only from the index.
- A second entity pass now fills a more practical middle layer: donor-preserving PDO baselines, organ-on-chip access devices, calcium-imaging functional readouts, and host-circuit validation now have dedicated landing pages and are threaded into the brain and translational-screening queries.
- A second source-threading pass now pushes those newer entities farther into patient-derived cancer, specimen-logistics PDO, gastrointestinal access-device, kidney perfusion-chip, and brain benchmarking source pages, so entity browsing no longer depends on only the first representative set.
- Pruned source pages remain in `wiki/sources/` with `status: pruned` so older cross-links do not break.
- Use `python3 scripts/wiki.py --collection organoid resume` to see the current backlog and latest query work.
