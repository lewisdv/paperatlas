---
title: Modeling Atrial Fibrillation in a Human Heart Macrophage Assembloid
kind: paper
status: ingested
added: 2026-04-21T15:48:23+09:00
raw_source: raw/sources/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12413170/
published_date: 2025-11-19
organ: heart
protocol_focus: inflammation-driven atrial fibrillation modeling in a human heart macrophage assembloid
ingest_method: generic-auto
ingested: 2026-04-21
deep_ingested: 2026-04-22
---

# Modeling Atrial Fibrillation in a Human Heart Macrophage Assembloid

## Source

- PDF: [raw/sources/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.pdf](../../raw/sources/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12413170/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12413170/)
- Status: deep ingested on 2026-04-22
- Organ focus: immune-bearing human heart assembloid rather than a neural or generic multi-lineage organoid
- Protocol focus: use inflammatory NLRP3 activation in a macrophage-integrated cardiac assembloid to induce and read atrial-fibrillation-like electrical instability

## Study design

- Starting material: pluripotent-stem-cell-derived human heart macrophage assembloids with integrated tissue-resident macrophages and atrial cardiomyocyte readouts
- Protocol stages:
  - establish or maintain hHMAs as immune-bearing heart organoids rather than macrophage-free cardiac spheroids
  - trigger inflammation with physiological-range NLRP3 activators including `LPS`, `IFN-g`, and `IL-1B`
  - assess inflammasome activation by `RT-qPCR` plus confocal localization of NLRP3-pathway protein components
  - quantify electrophysiologic consequences with `FluoVolt` live-cell imaging of atrial conductance and use phase-contrast microscopy to assess morphology and contractility
- Key validation: inflammatory stimulation drives spontaneous irregular rhythms and irregular atrial conductance patterns while showing NLRP3-pathway activation in arrhythmic assembloids
- Distinct protocol emphasis: this is not a cardiac differentiation paper; it is an immune-enabled disease-assay paper that links inflammatory signaling to rhythm dysfunction inside a multicellular heart model

## Key findings

- Adds a cardiac counterpart to the corpus's immune-bearing or inflammasome-aware organoid assays: macrophages are built into the model rather than bolted on as a late coculture.
- Makes the experimental chain explicit from inflammatory trigger to molecular activation to rhythm phenotype, which is what gives the assembloid translational value.
- Shows why extra cellular complexity matters here: the biological question is not cardiac morphogenesis alone but whether inflammatory tissue context can precipitate atrial-fibrillation-like behavior.

## Distinctive contribution in this corpus

- Extends the cardiac branch beyond developmental heart-forming organoids into mechanistic disease modeling with an explicit immune compartment.
- Gives the functional-assay branch a heart-specific inflammation-to-electrophysiology example, not only infection, barrier, or epithelial-immune exposure systems.
- Sits between the cardiac morphogenesis papers and the cerebral NLRP3 assay paper as a cross-organ example of inflammasome logic inside multicellular organoid systems.

## Limitations and caveats

- The article is short-form `Research Symposium` reporting, so the exact upstream hHMA generation details are compressed compared with a full Nature Protocols-style paper.
- The induced phenotype is an acute inflammatory AF model, not a full chronic remodeling or fibrosis model of human atrial fibrillation.
- The assay becomes persuasive because macrophages are included, but that same complexity can make benchmarking against simpler cardiomyocyte-only systems essential.

## Relevance to corpus

- Converts the cardiac branch from mostly developmental morphogenesis and imaging protocols into a disease-assay branch with explicit immune context.
- Useful when the question is not how to make cardiac tissue, but how to test whether inflammatory signaling can destabilize cardiac rhythm inside a human multicellular model.
- Worth retaining despite the shorter article format because the corpus otherwise has very little direct coverage of macrophage-integrated cardiac organoid assays.

## Related concepts

- [Cardiac and hematoendothelial organoids](../concepts/cardiac-and-hematoendothelial-organoids.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related entities

- [NLRP3 inflammasome](../entities/nlrp3-inflammasome.md)

## Related sources

- [Generation of heart-forming organoids from human pluripotent stem cells under defined conditions](drakhlis_2021_generation_of_heart-forming_organoids_from.md) - the developmental baseline for this cardiac branch before immune-bearing disease assays are layered on top.
- [Production of human blood-generating heart-forming organoids and sample preparation for advanced imaging](dardano_2025_production_of_human_blood-generating_heart-forming.md) - a later cardiac-complexity comparator that adds hematoendothelial richness and imaging depth rather than inflammatory rhythm readouts.
- [A Dynamic Protocol to Explore NLRP3 Inflammasome Activation in Cerebral Organoids](d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.md) - the closest same-pathway assay comparator elsewhere in the corpus, but in astrocyte-rich cerebral organoids rather than cardiac assembloids.

## Open questions

- How much of the AF-like phenotype depends specifically on integrated macrophages rather than direct cytokine exposure to cardiomyocytes alone?
- Which interventions best test the model mechanistically: upstream inflammasome blockade, macrophage depletion, or classic anti-arrhythmic rescue?
- What benchmark is needed before this system can serve as a preclinical drug-screening gate rather than a mechanistic proof-of-concept assay?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T15:48:31+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid -f json,markdown`
- Manifest: [raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid/opendataloader-run.json](../../raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid/opendataloader-run.json)
- Output: [raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.json](../../raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.json)
- Output: [raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.md](../../raw/derived/opendataloader/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
