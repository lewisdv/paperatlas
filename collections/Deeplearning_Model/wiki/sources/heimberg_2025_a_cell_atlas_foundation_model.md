---
title: A cell atlas foundation model for scalable search of similar human cells
kind: paper
status: ingested
added: 2026-04-29T10:56:57+09:00
raw_source: raw/sources/heimberg_2025_a_cell_atlas_foundation_model.pdf
---

# A cell atlas foundation model for scalable search of similar human cells

## Source

- File: [raw/sources/heimberg_2025_a_cell_atlas_foundation_model.pdf](../../raw/sources/heimberg_2025_a_cell_atlas_foundation_model.pdf)
- Added: 2026-04-29T10:56:57+09:00
- Venue/status: Nature paper; published online 20 November 2024
- Authors: Graham Heimberg, Tony Kuo, Daryle J. DePianto, Omar Salem, Tobias Heigl, Nathaniel Diamant, Gabriele Scalia, Tommaso Biancalani, Shannon J. Turley, Jason R. Rock, Hector Corrada Bravo, Josh Kaminker, Jason A. Vander Heiden, Aviv Regev
- DOI: `10.1038/s41586-024-08411-y`

## Summary

This paper introduces SCimilarity, a deep metric-learning foundation model for single-cell profiles that supports rapid search for transcriptionally similar cells across a very large human atlas. Instead of generating new profiles, the model learns a representation in which biologically similar cells are nearby and can therefore be retrieved quickly from a 23.4-million-cell reference. The paper positions this as a scalable route to cross-study cell-state search, cell-type annotation, confidence-aware transfer to new datasets, and discovery links between in vivo disease states and in vitro models.

## Methods

- SCimilarity jointly optimizes a supervised triplet loss and an unsupervised reconstruction loss so that matching cell types move closer together while subtle within-type expression differences are preserved.
- Triplets are sampled from author-provided Cell Ontology labels, but ancestor-descendant ontology relationships are excluded as ambiguous rather than being forced into similar or dissimilar classes.
- Training uses `7,886,247` single-cell profiles from `56` studies and `50,000,000` hard-mined triplets, while `15` validation studies with `1,415,962` cells are held out for evaluation.
- Querying and annotation are implemented as nearest-neighbour retrieval in precomputed hnswlib indices: one annotated reference for cell-type assignment and one `23.4`-million-cell reference for large-scale state search.

## Key Claims

- A pretrained similarity model can generalize across tissues, diseases, and profiling settings well enough to support large-scale pan-body cell-state retrieval without per-dataset retraining.
- Retrieval-oriented metric learning better captures fine-grained query cell states than the paper's compared single-cell foundation models on the reported fibrosis-oriented search tasks.
- The learned representation can support multiple downstream tasks from one embedding space, including annotation, outlier/confidence detection, and in vivo to in vitro model matching.

## Evidence

- Atlas scale: the reference corpus comprises `412` studies, `23,381,150` cells, `5,142` tissue samples, `184` Tissue Ontology terms, and `132` Disease Ontology terms.
- Query efficiency: the paper reports that finding `10,000` similar cells from the full `23.4`-million-cell reference takes `0.05` seconds, while scoring a fibrosis-associated macrophage query over `2,507,171` monocyte and macrophage profiles takes `2` seconds.
- Query quality: for the fibrosis-associated macrophage query, SCimilarity's similarity ranking tracks the retrieval signature better than the reported comparators, with `Spearman rho = 0.77` versus `0.54` for scFoundation and `0.59` for scGPT.
- Second query benchmark: for a fibrosis-associated myofibroblast query, SCimilarity reports `rho = 0.36`, compared with `-0.19` for scGPT and `-0.17` for scFoundation.
- Representation confidence: `79.5%` of in vivo holdout cells are reported to have high representation confidence, whereas `43.8%` of in vitro profiles fall into low-confidence territory because those contexts were poorly represented in training.
- Annotation benchmarking: on a held-out healthy kidney dataset, SCimilarity matches author labels for `86.5%` of cells, compared with `85.2%` for scANVI, `90.4%` for CellTypist, and `87.2%` for TOSICA; on a held-out PBMC CITE-seq dataset, SCimilarity reports `75.3%` accuracy versus `52.2%`, `59.1%`, and `44.4%` for those same baselines.
- Biological validation: the highest-scoring in vitro hit for the fibrosis-associated macrophage query is a `3D` hydrogel culture system, and the paper reports experimental validation that this system reproduces the queried cell state.

## Limitations

- The source emphasizes that representation confidence drops in tissues or contexts that were absent or weakly represented in training, such as stomach, bladder, fetal gut, and many in vitro samples.
- Training was limited to 10x Genomics Chromium scRNA-seq and snRNA-seq studies, so the authors explicitly caution that cross-technology integrations should still be interpreted carefully.
- Tumours, cell lines, and induced pluripotent stem cell-derived cells were excluded from training and validation because their identities were considered ambiguous, which narrows the directly validated scope.
- The paper notes that duplicated samples remain inside the full public reference corpus even though train-test duplication was removed.

## Related Pages

- [SCimilarity](../entities/SCimilarity.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)

## Open Questions

- How stable are SCimilarity's confidence scores when the query comes from perturbation states or developmental contexts that are only weakly represented in the training atlas?
- How much of the reported advantage over scGPT and scFoundation comes from the retrieval objective itself versus differences in reference construction and evaluation setup?
- As more papers are ingested into this collection, how should retrieval-first foundation models be compared against generative or perturbation-focused models for practical single-cell analysis workflows?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T10:53:22+0900
- Command: `.venv-opendataloader/bin/opendataloader-pdf raw/sources/heimberg_2025_a_cell_atlas_foundation_model.pdf -o /tmp/odl-check-heimberg -f markdown --image-output off -q`
- Manifest: [raw/derived/opendataloader/heimberg_2025_a_cell_atlas_foundation_model/opendataloader-run.json](../../raw/derived/opendataloader/heimberg_2025_a_cell_atlas_foundation_model/opendataloader-run.json)
- Output: [raw/derived/opendataloader/heimberg_2025_a_cell_atlas_foundation_model/heimberg_2025_a_cell_atlas_foundation_model.md](../../raw/derived/opendataloader/heimberg_2025_a_cell_atlas_foundation_model/heimberg_2025_a_cell_atlas_foundation_model.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
