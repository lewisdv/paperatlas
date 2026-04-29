---
title: How to build the virtual cell with artificial intelligence: Priorities and opportunities
kind: paper
status: ingested
added: 2026-04-29T16:04:55+09:00
raw_source: raw/sources/bunne_2024_how_to_build_the_virtual.pdf
---

# How to build the virtual cell with artificial intelligence: Priorities and opportunities

## Source

- File: [raw/sources/bunne_2024_how_to_build_the_virtual.pdf](../../raw/sources/bunne_2024_how_to_build_the_virtual.pdf)
- Added: 2026-04-29T16:04:55+09:00
- Venue/status: Cell perspective; published 12 December 2024
- Authors: Charlotte Bunne, Yusuf Roohani, Yanay Rosen, Ankit Gupta, Xikun Zhang, Marcel Roed, Theo Alexandrov, Mohammed AlQuraishi, Patricia Brennan, Daniel B. Burkhardt, Andrea Califano, and many co-authors
- DOI: `10.1016/j.cell.2024.11.015`

## Summary

This perspective argues that recent advances in AI plus rapidly expanding omics data make it plausible to build an AI virtual cell (AIVC): a multi-scale, multi-modal, large-neural-network-based model that can represent and simulate molecules, cells, and tissues across diverse states. Rather than presenting one finished benchmarked system, the paper lays out a roadmap for how such a model should be designed, what data and architectures it may need, which scientific capabilities matter most, and which technical, social, and ethical bottlenecks still block progress. In this collection, the paper is important because it reframes many narrower foundation-model efforts as partial ingredients for a broader virtual-cell stack.

## Methods

- The paper proposes an AIVC architecture with two main components: a universal representation (UR) of biological state and a family of virtual instruments (VIs) that decode or manipulate that representation.
- URs are proposed to span three physical scales: molecular, cellular, and multicellular, while integrating multiple modalities and contexts into one shared embedding space.
- Decoder VIs are proposed to map URs into human-readable outputs such as labels, images, structures, or predicted readouts, whereas manipulator VIs are proposed to transform one UR into another to simulate perturbations, trajectories, or interventions.
- The source surveys candidate AI building blocks rather than selecting one final architecture, including transformers and LLM-style sequence models, CNNs and vision transformers, diffusion and flow-matching models, and graph neural networks.
- The roadmap also emphasizes active lab-in-the-loop refinement, uncertainty-aware prediction, cross-modal evaluation, and open collaborative infrastructure as part of the design rather than as afterthoughts.

## Key Claims

- Biology is now approaching a stage where a learned, data-driven virtual cell is more plausible than past rule-based or narrowly mechanistic whole-cell models alone.
- A useful AIVC must be multi-scale, multi-modal, and self-consistent across contexts rather than optimized only for one assay, one tissue, or one benchmark task.
- The core value of an AIVC lies not only in prediction but in enabling in silico experimentation, prioritizing wet-lab studies, and narrowing mechanistic hypothesis space.
- Progress will require open science, better multimodal data generation, broader benchmarking frameworks, and careful attention to interpretability, privacy, and equitable data representation.

## Evidence

- The source grounds the proposal in current data trends, stating that high-throughput reference datasets across cell and tissue systems have been doubling roughly every six months in recent years and are increasingly paired with systematic perturbations.
- It contrasts the AIVC vision with earlier virtual-cell efforts, summarizing existing rule-based, differential-equation, stochastic, agent-based, and whole-cell models as useful but insufficient for multi-scale nonlinear human-cell biology.
- The paper specifies three target capabilities for an AIVC: building universal representations across contexts, predicting function and dynamics, and supporting in silico experiment design plus adaptive data generation.
- It also specifies three physical scales for representation learning: molecular, cellular, and multicellular, and ties each scale to candidate data modalities and model families.
- Box 1 identifies concrete grand challenges: capability definition and evaluation, self-consistency across contexts and modalities, balancing interpretability with utility, collaborative modeling infrastructure, responsible and ethical use, and prioritization of large-scale data generation.
- Box 2 gives practical use-case vignettes rather than benchmark scores, including phenotypic drug discovery, cell-based therapeutics, pan-cancer tumor-microenvironment analysis, and personalized diagnostic or digital-twin scenarios.

## Limitations

- This is a perspective article, not an end-to-end AIVC implementation, so it does not provide one integrated model, training recipe, or comparative benchmark proving that the full vision already works.
- The source explicitly notes that dynamic molecular processes, transient weak interactions, and other time-resolved mechanisms remain hard even for current foundation-model approaches.
- The roadmap depends on enormous, diverse, cross-scale multimodal datasets plus expensive shared infrastructure, making data quality, representation bias, privacy, and compute access central unresolved constraints.
- The paper also treats interpretability, trust, and benchmarking as open research problems, which means many proposed capabilities are still aspirational rather than operational.

## Related Pages

- [AIVC](../entities/AIVC.md)
- [Universal Representation](../concepts/universal-representation.md)
- [Virtual Instruments](../concepts/virtual-instruments.md)

## Open Questions

- Which AIVC capability appears most reachable first from the models already represented in this collection: universal embeddings, perturbation simulation, or cross-scale multimodal integration?
- How much of the AIVC roadmap could be assembled from modular combinations of existing systems in this collection rather than from one monolithic model?
- As more perspective and review papers are ingested, does this collection need a dedicated synthesis on virtual-cell roadmaps versus already implemented foundation models?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T16:05:08+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/bunne_2024_how_to_build_the_virtual.pdf -o /tmp/odl-check-virtual-cell -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/bunne_2024_how_to_build_the_virtual/opendataloader-run.json](../../raw/derived/opendataloader/bunne_2024_how_to_build_the_virtual/opendataloader-run.json)
- Output: [raw/derived/opendataloader/bunne_2024_how_to_build_the_virtual/bunne_2024_how_to_build_the_virtual.md](../../raw/derived/opendataloader/bunne_2024_how_to_build_the_virtual/bunne_2024_how_to_build_the_virtual.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
