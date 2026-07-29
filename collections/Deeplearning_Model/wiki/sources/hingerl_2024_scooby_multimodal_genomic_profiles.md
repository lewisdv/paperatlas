---
title: scooby: Modeling multi-modal genomic profiles from DNA sequence at single-cell resolution
kind: paper
status: ingested
added: 2026-07-29T17:52:24+09:00
raw_source: raw/sources/hingerl_2024_scooby_multimodal_genomic_profiles.pdf
---

# scooby: Modeling multi-modal genomic profiles from DNA sequence at single-cell resolution

## Source

- File: [raw/sources/hingerl_2024_scooby_multimodal_genomic_profiles.pdf](../../raw/sources/hingerl_2024_scooby_multimodal_genomic_profiles.pdf)
- Added: 2026-07-29T17:52:24+09:00
- Venue/status: bioRxiv preprint, version posted 22 September 2024
- Authors: Johannes C. Hingerl, Laura D. Martens, Alexander Karollus, Trevor Manz, Jason D. Buenrostro, Fabian J. Theis, and Julien Gagneur
- DOI: `10.1101/2024.09.19.613754`
- SHA-256: `58fdc008ba42361ddf2d1889e03de59c867932ddd531b61cd3a66d92c51cfdef`

## Summary

scooby is a sequence-to-function model that predicts scRNA-seq coverage and scATAC-seq insertion profiles from DNA sequence at single-cell resolution. It adapts the bulk multi-omics model Borzoi using LoRA and adds a lightweight decoder whose weights are conditioned on each cell's Poisson-MultiVI embedding. This avoids a separate output track per cell and enables predictions for cells not seen during training. The paper studies held-out genomic regions and cell states, in silico transcription-factor motif deletion, and cell-type-specific decomposition of bulk eQTL effects.

## Methods

- Borzoi supplies sequence embeddings from approximately `0.5 Mb` genomic context at `32 bp` resolution.
- LoRA adapts convolutional and Transformer layers to 3-prime single-cell RNA coverage and ATAC insertions while leaving pretrained weights frozen.
- A small MLP converts a cell-state embedding into parameters for a position-wise convolutional decoder.
- RNA and ATAC profiles are trained jointly on `63,683` bone-marrow multiome cells with chromosome-based train/validation/test splits.
- In silico motif replacement measures cell-specific changes in predicted gene expression; reference-versus-alternate sequences estimate variant effects.

## Key Claims

- A pretrained bulk sequence model can be adapted to predict multimodal genomic profiles for arbitrary cells represented in a continuous embedding space.
- Conditioning on cell state permits generalization to related unseen cell populations rather than only memorizing fixed output tracks.
- Model interpretation can connect cell-type-specific expression, accessibility, TF motifs, and genetic variant effects.

## Evidence

- Test-region profile predictions correlate with neighbor-averaged observations at mean Pearson `0.63` for RNA and `0.70` for ATAC; cell-type pseudobulk values reach `0.67` and `0.72`.
- Across genes, cell-type pseudobulk expression has mean Pearson `0.86`; after removing gene and cell-type means, the remaining cell-type-specific variation correlates at `0.54`.
- Against retrained seq2cells, mean correlation across genes improves from `0.77` to `0.87` and across cell types from `0.43` to `0.55`.
- A model trained without normoblasts predicts that unseen population at `0.78` versus `0.81` for the full model; HEMGN trajectory correlations are `0.937` and `0.939`.
- Whole-blood eQTL effect correlation is Spearman `0.495`; on the shared set, scooby reaches `0.517` versus `0.380` for seq2cells, with `91.7%` versus `83.9%` sign agreement among non-negligible predictions.

## Limitations

- The study is a preprint centered on one hematopoietic multiome dataset; cross-tissue generalization is not established.
- Training used eight A40 GPUs for two days and did not include extensive hyperparameter optimization.
- The 10X 3-prime RNA assay contains limited information about alternative transcription start sites and isoforms.
- Distal regulatory effects remain difficult: eQTL concordance falls with distance from the transcription start site.
- Motif deletions and cell-type-specific eQTL decompositions are in silico interpretations and need experimental validation.

## Related Pages

- [scooby](../entities/scooby.md)
- [Sequence-to-Single-Cell Profile Modeling](../concepts/sequence-to-single-cell-profile-modeling.md)
- [MultiVI](../entities/MultiVI.md)
- [scMultiMap](../entities/scMultiMap.md)

## Open Questions

- Does the cell-conditioned decoder extrapolate to tissues or states not represented in its embedding training data?
- How much performance comes from Borzoi pretraining, LoRA adaptation, and the multiomic cell embedding separately?
- Can richer full-length or long-read assays make the same architecture useful for isoform-specific prediction?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T18:04:58+0900
- Manifest: [raw/derived/opendataloader/hingerl_2024_scooby_multimodal_genomic_profiles/opendataloader-run.json](../../raw/derived/opendataloader/hingerl_2024_scooby_multimodal_genomic_profiles/opendataloader-run.json)
- Output: [raw/derived/opendataloader/hingerl_2024_scooby_multimodal_genomic_profiles/hingerl_2024_scooby_multimodal_genomic_profiles.md](../../raw/derived/opendataloader/hingerl_2024_scooby_multimodal_genomic_profiles/hingerl_2024_scooby_multimodal_genomic_profiles.md)
- Layout text: [raw/derived/pdftext/Hingerl_2024_scooby/Hingerl_2024_scooby.txt](../../raw/derived/pdftext/Hingerl_2024_scooby/Hingerl_2024_scooby.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
