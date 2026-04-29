---
title: Predicting transcriptional outcomes of novel multigene perturbations with GEARS
kind: paper
status: ingested
added: 2026-04-29T21:44:37+09:00
raw_source: raw/sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.pdf
---

# Predicting transcriptional outcomes of novel multigene perturbations with GEARS

## Source

- File: [raw/sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.pdf](../../raw/sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.pdf)
- Added: 2026-04-29T21:44:37+09:00
- Venue/status: Nature Biotechnology article; received 9 July 2022, accepted 12 July 2023, published online 17 August 2023
- Authors: Yusuf Roohani, Kexin Huang, and Jure Leskovec
- DOI: `10.1038/s41587-023-01905-6`

## Summary

This paper presents GEARS, a graph-enhanced deep learning model for predicting the transcriptional outcomes of single-gene, two-gene, and broader multigene perturbations from perturbational single-cell RNA-seq data. The key contribution is that GEARS can predict combinations containing genes that were never individually perturbed during training by injecting prior biological knowledge through gene-relationship graphs. In this collection, the paper matters because it sharpens the combinatorial perturbation branch and gives a strong non-foundation-model baseline for reasoning about unseen intervention combinations.

## Methods

- GEARS represents each gene with two learned embeddings: a gene embedding for baseline transcriptional context and a perturbation embedding for the effect of perturbing that gene.
- It learns these embeddings through two knowledge graphs: a gene coexpression graph for gene embeddings and a Gene Ontology-derived perturbation relationship graph for perturbation embeddings.
- A graph neural network propagates information across both graphs, then combines the perturbation set with a cross-gene layer and gene-specific MLP output heads to predict post-perturbation expression.
- The model is trained on Perturb-seq-style single-cell perturbation screens and explicitly evaluated under harder generalization classes where one or both perturbed genes are unseen during training.
- GEARS also outputs a Bayesian uncertainty estimate to flag cases where graph connectivity is too weak for confident prediction.

## Key Claims

- Prior biological knowledge lets GEARS generalize to unseen perturbation genes and unseen multigene combinations that existing perturbation models cannot reliably handle.
- GEARS can model non-additive interactions rather than only summing single-gene effects, making it useful for synergy and epistasis discovery.
- The method can rank high-value candidate perturbation pairs for experimental follow-up with materially higher precision than existing baselines.
- Knowledge-graph guidance is not only a small performance booster; it is central to enabling combinatorial generalization.

## Evidence

- On held-out single-gene perturbations, the source reports `30`- to `50`-percent improvements in mean squared error over baselines and more than `2x` better Pearson-correlation performance in both RPE-1 and K562 screens.
- On multigene generalization, GEARS improves performance by more than `30%` across all unseen-gene cases, with the best case reaching `53%` improvement when both perturbed genes are unseen during training.
- For top differentially expressed genes, the paper reports `50%` greater enrichment of the most significant predicted genes than baseline methods.
- For genetic interaction discovery, GEARS improves `precision@10` by more than `40%` for four of five interaction subtypes, exceeds `90%` improvement for redundancy and epistasis, and shows a twofold increase in top-ten interaction accuracy.
- In two-gene interaction scoring, the paper reports `R2` values around `0.4` for synergy, neomorphism, and redundancy, whereas CPA is reported near `0.0` on those same interaction types.

## Limitations

- The same knowledge graphs that enable GEARS also constrain it: prediction quality drops for previously unperturbed genes that are poorly connected in the graph.
- The paper is tightly centered on genetic perturbation transcriptomics and does not address broader multimodal or tissue-level state modeling.
- Although GEARS supports uncertainty estimation, its core prediction still depends on how well graph priors align with the biological system under study.
- The method is strongest for combinatorial perturbation outcome prediction, not for open-ended biological interpretation or broad foundation-model-style reuse across unrelated tasks.

## Related Pages

- [GEARS](../entities/GEARS.md)
- [Combinatorial Perturbation Generalization](../concepts/combinatorial-perturbation-generalization.md)
- [CellOT](../entities/CellOT.md)
- [Tahoe-x1](../entities/Tahoe-x1.md)

## Open Questions

- How much of GEARS's advantage persists when perturbation datasets become much larger and less graph sparse, reducing the need for strong prior structure?
- Would GEARS-style graph priors still help if combined with a much larger perturbation-trained foundation model rather than a smaller task-specific architecture?
- Which later papers in this collection treat multigene perturbation as a compositional reasoning problem versus a large-scale pretraining problem?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T21:43:47+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.pdf -o /tmp/odl-check-gears -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/roohani_2024_predicting_transcriptional_outcomes_of_novel/opendataloader-run.json](../../raw/derived/opendataloader/roohani_2024_predicting_transcriptional_outcomes_of_novel/opendataloader-run.json)
- Output: [raw/derived/opendataloader/roohani_2024_predicting_transcriptional_outcomes_of_novel/roohani_2024_predicting_transcriptional_outcomes_of_novel.md](../../raw/derived/opendataloader/roohani_2024_predicting_transcriptional_outcomes_of_novel/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->

## Open Questions

- Pending ingest.
