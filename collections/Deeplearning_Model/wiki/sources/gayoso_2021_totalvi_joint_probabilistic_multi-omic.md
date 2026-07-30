---
title: Joint probabilistic modeling of single-cell multi-omic data with totalVI
kind: paper
status: ingested
added: 2026-07-30T16:44:20+09:00
raw_source: raw/sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.pdf
---

# Joint probabilistic modeling of single-cell multi-omic data with totalVI

## Source

- File: [raw/sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.pdf](../../raw/sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.pdf)
- Added: 2026-07-30T16:44:20+09:00
- Authors: Adam Gayoso, Zoe Steier, Romain Lopez, Jeffrey Regier, Kristopher L. Nazor, Aaron Streets, and Nir Yosef
- Venue: *Nature Methods* 18, 272-282 (2021)
- DOI: [10.1038/s41592-020-01050-x](https://doi.org/10.1038/s41592-020-01050-x)
- Published online: 15 February 2021
- License stated in source: The Authors, under exclusive licence to Springer Nature America, Inc. 2021

## Summary

- `totalVI`, or Total Variational Inference, is an end-to-end probabilistic model for paired CITE-seq RNA and surface-protein counts.
- It learns a joint cell-state representation while modeling modality-specific technical effects, especially RNA library size, experimental batch, and ambient or nonspecific protein background.
- The same fitted model supports normalization, dimensionality reduction, integration across antibody panels, protein imputation, feature correlations, and Bayesian differential-expression analysis.
- Its defining contribution is not merely RNA-protein fusion; it builds the protein foreground/background distinction into the generative model.

## Probabilistic Model

- Each cell has a 20-dimensional logistic-normal latent cell-state variable in the reported experiments.
- RNA counts follow gene-specific negative-binomial likelihoods conditioned on cell state, RNA size factor, and batch.
- Each protein follows a negative-binomial mixture with cell- and protein-specific foreground and background components.
- The mixture weight estimates the probability that an observed antibody count came from protein background.
- An encoder approximates posterior distributions over cell state, RNA size factor, and protein background; a decoder maps cell state and batch to RNA and protein likelihood parameters.
- The evidence lower bound is optimized with mini-batches of 256 cells and early stopping.
- For unmatched antibody panels, missing protein inputs are set to zero for the encoder, likelihood terms are evaluated only for observed proteins, and prediction is transferred through the integrated latent space.

## Evidence

### Fit And Scale

- Evaluation spans human PBMC and MALT data and four mouse spleen/lymph-node CITE-seq datasets.
- The mouse experiments contain 32,648 cells measured with nested panels of 111 or 208 antibodies.
- Posterior predictive checks compare totalVI with factor analysis, scHPF, and RNA-only scVI; totalVI performs best on the reported observed-data variation metrics.
- On held-out data, totalVI improves protein mean absolute error and calibration relative to factor analysis, while RNA performance is similar to scVI.
- Approximately 33,000 cells with more than 4,100 RNA and protein features are processed in under one hour.

### Protein Background

- For 9 of 11 known marker proteins, both totalVI and a two-component Gaussian mixture achieve cell-type classification AUC above 0.97.
- For overlapping foreground/background cases such as CD20 and CD28, totalVI performs better because its decision varies by cell state instead of using one protein-wide threshold.
- Denoised protein values remove the estimated background component while retaining posterior uncertainty.
- The paper's correlation procedure samples from controlled model quantities rather than calculating correlations directly from one denoised matrix, reducing denoising-induced artifacts in its negative-control tests.

### Integration And Missing Proteins

- totalVI integrates datasets with matched 111-protein panels and with the union of 111- and 208-protein panels.
- It outperforms Seurat v3, Scanorama, and Harmony on the reported feature-retention and clustering metrics while remaining competitive on dataset-mixing metrics.
- In a held-out-protein experiment repeated over 30 resampled training sets, 80 proteins differ significantly in imputation error between totalVI and Seurat v3; totalVI has lower mean error for about 68% of them.
- The paper emphasizes that missing-protein prediction depends on adequate mixing between the source and target batches in the latent space.

### Differential Expression And Biological Structure

- totalVI estimates a posterior distribution over log fold change and uses Bayes factors rather than treating one denoised matrix as fully observed.
- It calls the fewest, often zero, isotype-control antibodies as differentially expressed and is more reproducible across biological replicates than the Welch and Wilcoxon baselines.
- In an ICOS-high regulatory-T-cell comparison, the two baseline tests call all curated putative negatives as upregulated, whereas totalVI excludes them; the baselines call 78 of 110 proteins significant.
- Archetypal analysis links latent dimensions to RNA-protein programs, including interferon-response variation and a transitional-to-mature B-cell axis.

## Interpretation

- totalVI demonstrates why multimodal modeling must distinguish `biological state` from `assay-specific technical variation`.
- Its cell- and protein-specific background mixture is more flexible than a single cutoff fitted independently to each antibody.
- Integration, background correction, imputation, and differential testing are coupled through one probability model rather than assembled as separate preprocessing steps.
- The posterior DE workflow is more principled than testing a plug-in denoised matrix, but its empirical controls do not establish universal frequentist FDR calibration.
- totalVI is a direct architectural ancestor of protein handling in [MultiVI](../entities/MultiVI.md).

## Limitations

- The model is specialized to paired RNA and surface-protein counts and does not directly model chromatin accessibility.
- It assumes both modalities arise from a common latent cell state and that the chosen negative-binomial mixture adequately represents antibody background.
- Missing-panel imputation requires overlapping biology and good batch mixing; the paper does not establish identifiability under strong cell-state or protocol shift.
- Most detailed biological demonstrations use immune tissues and author-generated spleen/lymph-node data.
- Isotype controls and curated positive or negative markers provide useful checks but are not complete ground truth for every protein.
- Bayesian DE evidence and posterior uncertainty should not be interpreted as automatic frequentist error control in every downstream setting.
- The supplied PDF includes extended data but not the separately hosted supplementary notes and tables.

## Related Pages

- [totalVI](../entities/totalVI.md)
- [Protein Background Modeling](../concepts/protein-background-modeling.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Post-Imputation Inference](../concepts/post-imputation-inference.md)
- [MultiVI](../entities/MultiVI.md)
- [scVAEIT](../entities/scVAEIT.md)

## Open Questions

- How stable is foreground/background decomposition under new antibody chemistries or tissues?
- How should batch-mixing diagnostics gate whether a missing protein is safe to impute?
- How do posterior Bayes factors relate to task-specific FDR guarantees under model misspecification?
- Can protein-background uncertainty be propagated into downstream causal or regulatory analyses?

## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Markdown: [raw/derived/opendataloader/gayoso_2021_totalvi_joint_probabilistic_multi-omic/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md](../../raw/derived/opendataloader/gayoso_2021_totalvi_joint_probabilistic_multi-omic/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md)
- Manifest: [raw/derived/opendataloader/gayoso_2021_totalvi_joint_probabilistic_multi-omic/opendataloader-run.json](../../raw/derived/opendataloader/gayoso_2021_totalvi_joint_probabilistic_multi-omic/opendataloader-run.json)
- Poppler layout text: [raw/derived/pdftext/Gayoso_2021_totalVI/Gayoso_2021_totalVI.txt](../../raw/derived/pdftext/Gayoso_2021_totalVI/Gayoso_2021_totalVI.txt)
- These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
