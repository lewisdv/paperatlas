# totalVI

## Type

- Probabilistic deep generative model for paired CITE-seq RNA and surface-protein counts

## Definition

- `totalVI` stands for Total Variational Inference.
- It represents RNA, protein, cell state, batch, RNA library size, and protein background in one end-to-end model.

## Core Architecture

- Logistic-normal joint latent cell-state representation.
- Negative-binomial RNA likelihood.
- Cell- and protein-specific negative-binomial foreground/background mixture for antibody counts.
- Variational posterior inference with batch-conditioned decoders.
- Missing-protein training that omits unobserved likelihood terms.

## Reported Uses

- RNA-protein normalization and joint embedding.
- Protein-background correction.
- Integration across datasets with different antibody panels.
- Missing-protein imputation.
- Denoised feature correlations and Bayesian differential-expression testing.

## Caveats

- Specialized to RNA and surface proteins.
- Missing-panel prediction depends on adequate latent batch mixing.
- Foreground/background separation is model-based rather than directly observed.
- Posterior DE evidence is not automatic frequentist FDR control under every misspecification.

## Related

- [Protein Background Modeling](../concepts/protein-background-modeling.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Post-Imputation Inference](../concepts/post-imputation-inference.md)
- [MultiVI](MultiVI.md)
- [scVAEIT](scVAEIT.md)
- [Source: Joint probabilistic modeling of single-cell multi-omic data with totalVI](../sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md)
