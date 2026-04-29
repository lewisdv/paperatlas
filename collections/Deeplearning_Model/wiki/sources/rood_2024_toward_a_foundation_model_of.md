---
title: Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas
kind: paper
status: ingested
added: 2026-04-29T21:53:45+09:00
raw_source: raw/sources/rood_2024_toward_a_foundation_model_of.pdf
---

# Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas

## Source

- File: [raw/sources/rood_2024_toward_a_foundation_model_of.pdf](../../raw/sources/rood_2024_toward_a_foundation_model_of.pdf)
- Added: 2026-04-29T21:53:45+09:00
- Venue/status: Cell leading-edge review; Cell 187, published 22 August 2024
- Authors: Jennifer E. Rood, Anna Hupalowska, and Aviv Regev
- DOI: `10.1016/j.cell.2024.07.035`

## Summary

This review argues that high-content pooled perturbation screens, when combined with AI and active experimental iteration, can support a `Perturbation Cell Atlas` that functions as a causal and generative foundation model for cell and tissue biology. Rather than presenting one finished model, the paper reframes perturbation modeling as an atlas-building problem that must combine molecular, imaging, spatial, organoid, animal, and human-genetics evidence across scales. In this collection, the paper matters because it turns the existing perturbation-model thread into a broader causal-roadmap and data-infrastructure agenda.

## Methods

- The review synthesizes recent perturbation-screening modalities, especially Perturb-seq and optical pooled screens, across cell lines, primary cells, organoids, animal models, and natural human genetic variation.
- It distinguishes several model semantics that are often conflated: representational, biologically causal, statistically causal, predictive or generative, and mechanistic.
- It surveys computational analysis goals spanning gene-level effects, programs, regulators, full-cell-state modeling, mechanism, perturbation combinations, natural genetic variation, experiment design, and correction of technical confounders.
- It proposes a phased roadmap for a `Perturbation Cell Atlas`, combining in vitro systems, organoids, animal models, and native human tissues rather than relying on one system class alone.
- The proposed workflow is explicitly iterative: perturbation data should feed models, models should guide active-learning-style next experiments, and the loop should progressively refine a queryable causal map of phenotypic space.

## Key Claims

- Exhaustively measuring combinatorial perturbation space is experimentally impossible, so causal and generative models must be part of the solution rather than only a downstream convenience.
- High-content pooled perturbation screens now provide enough molecular and phenotypic richness to make biologically useful causal foundation models plausible.
- A `Perturbation Cell Atlas` should complement the observational Human Cell Atlas by learning from perturbations, compressed screens, and natural genetic variation across multiple biological systems.
- Organoids, animal models, and tissue-context assays are essential because many biologically important effects are non-cell-autonomous and cannot be recovered from cell culture alone.

## Evidence

- The review makes the combinatorial barrier concrete: for roughly `20,000` human genes it estimates nearly `200` million two-gene combinations, `1.33` trillion three-gene combinations, `6.63 x 10^15` four-gene combinations, and `2.67 x 10^19` five-gene combinations.
- It cites optical pooled screening of more than `5,000` human genes across `31` million cells as evidence that high-content phenotypic screening is already operating at scales relevant to atlas construction.
- The source highlights early multi-system perturbation-atlas ingredients such as iMAP in mouse, which perturbed `90` genes across `39` tissues.
- It argues that rich readouts unlock qualitatively different biological analysis goals, including co-functional module discovery, genetic-interaction categorization, and non-cell-autonomous effect measurement, which scalar readouts cannot capture.
- The roadmap repeatedly emphasizes that compressed screens, active learning, and cross-system iteration are what make atlas construction tractable rather than requiring full combinatorial exhaustiveness.

## Limitations

- This is a review and strategic proposal, not an implemented perturbation-atlas foundation model with standardized quantitative benchmarks.
- The paper explicitly warns that representational or statistically causal models do not automatically recover genetically causal semantics, so the desired model properties cannot be assumed from predictive accuracy alone.
- The roadmap depends on large community coordination, multi-system data generation, assay standardization, and new algorithmic infrastructure that are not yet complete.
- Generalization across cell culture, organoids, animal models, and native human tissue is proposed as a goal, but the source does not claim that this transfer problem is already solved.

## Related Pages

- [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [Perturbation-Trained Foundation Models](../concepts/perturbation-trained-foundation-models.md)
- [GEARS](../entities/GEARS.md)
- [Tahoe-x1](../entities/Tahoe-x1.md)
- [AIVC](../entities/AIVC.md)

## Open Questions

- Which currently ingested perturbation models in this collection look most compatible with the `Perturbation Cell Atlas` vision, and which remain too task-local to serve as atlas components?
- What should count as the minimum causal unit in a perturbation atlas here: genes, programs, cell states, tissue microenvironments, or all of them at once?
- How should a future synthesis in this collection compare perturbation-atlas roadmaps against actual predictive models such as GEARS, CellOT, Tahoe-x1, and Squidiff?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T21:53:02+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/rood_2024_toward_a_foundation_model_of.pdf -o /tmp/odl-check-rood -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/rood_2024_toward_a_foundation_model_of/opendataloader-run.json](../../raw/derived/opendataloader/rood_2024_toward_a_foundation_model_of/opendataloader-run.json)
- Output: [raw/derived/opendataloader/rood_2024_toward_a_foundation_model_of/rood_2024_toward_a_foundation_model_of.md](../../raw/derived/opendataloader/rood_2024_toward_a_foundation_model_of/rood_2024_toward_a_foundation_model_of.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
