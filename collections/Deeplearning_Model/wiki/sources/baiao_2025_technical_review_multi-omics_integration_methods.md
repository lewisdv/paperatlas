---
title: A technical review of multi-omics data integration methods: from classical statistical to deep generative approaches
kind: paper
status: ingested
added: 2026-07-30T11:20:01+09:00
raw_source: raw/sources/baiao_2025_technical_review_multi-omics_integration_methods.pdf
---

# A technical review of multi-omics data integration methods: from classical statistical to deep generative approaches

## Source

- File: [raw/sources/baiao_2025_technical_review_multi-omics_integration_methods.pdf](../../raw/sources/baiao_2025_technical_review_multi-omics_integration_methods.pdf)
- Added: 2026-07-30T11:20:01+09:00
- Authors: Ana R. Baião, Zhaoxiang Cai, Rebecca C. Poulos, Phillip J. Robinson, Roger R. Reddel, Qing Zhong, Susana Vinga, and Emanuel Gonçalves
- Venue: *Briefings in Bioinformatics* 26(4), bbaf355 (2025)
- DOI: [10.1093/bib/bbaf355](https://doi.org/10.1093/bib/bbaf355)
- Type: Technical review
- License stated in source: CC BY 4.0

## Summary

- This review organizes multi-omics integration along two separate axes: the experimental correspondence available across datasets and the algorithmic family used to integrate them.
- Its experimental regimes are `vertical` integration of several modalities in matched samples, `horizontal` integration of one modality across sample groups or batches, `diagonal` integration of distinct modalities in unpaired groups, and `mosaic` integration through partially overlapping modality blocks.
- Its method families span correlation or covariance methods, matrix factorization, probabilistic or Bayesian models, kernels, networks, non-generative neural networks, and deep generative models.
- The technical center of the review is variational autoencoder design: likelihood and ELBO choices, multimodal posterior fusion, alignment regularizers, missing-modality handling, and the tradeoff between shared and modality-specific structure.
- Foundation models and non-omic data such as images, clinical records, phenotypes, and wearables are treated as promising extensions rather than as established replacements for task-specific integration methods.

## Integration Geometry

- `Vertical`: different omics are observed in the same samples. Matched samples support direct correlation, covariance, or joint-latent learning.
- `Horizontal`: the same omics layer is measured across different groups, platforms, or batches. The central problem is often batch correction rather than cross-modality translation.
- `Diagonal`: different modalities come from different sample groups. Methods must replace missing pairing with prior graphs, feature relations, adversarial alignment, or inferred correspondences.
- `Mosaic`: datasets have incomplete but overlapping modality combinations. Overlap acts as a bridge for alignment and missing-modality imputation.
- These regimes describe the data available to a method, not the architecture itself. A matrix factorization model and a VAE can therefore target the same regime with different assumptions.

## Method Families And Tradeoffs

- Correlation or covariance methods such as CCA and PLS are comparatively interpretable and support co-regulated module discovery, but linearity and matched-sample assumptions can be restrictive.
- Matrix factorization methods such as JIVE, NMF, LIGER, and UINMF provide efficient shared and modality-specific factors. Their linear structure aids inspection, but standard formulations do not explicitly model uncertainty.
- Probabilistic approaches such as iCluster and MOFA place distributions over latent variables and can represent uncertainty or missing values, at the cost of model assumptions, tuning, and computation.
- Multiple-kernel and network methods shift heterogeneous features into sample-similarity spaces. Their performance and interpretation depend strongly on kernels, distance metrics, and graph construction.
- Deep models can learn nonlinear relationships and flexible task-specific representations. The review emphasizes their larger data and compute requirements and their weaker default interpretability.
- The paper does not nominate one universally best family. It argues that data geometry, sample size, missingness, desired output, uncertainty requirements, and interpretability should determine method choice.

## VAE Technical Map

- A standard VAE optimizes an evidence lower bound consisting of a reconstruction term and a KL-divergence regularizer between the variational posterior and prior.
- The observation likelihood must match the assay. The review highlights negative-binomial likelihoods for sparse single-cell counts rather than treating mean-squared error as universally appropriate.
- Multimodal VAEs typically assign each modality its own encoder and decoder, then construct a joint latent representation by concatenation, a mixture of experts, a product of experts, or mixtures of products of experts.
- A shared latent space aids clustering, visualization, batch correction, denoising, and imputation, but can attenuate modality-specific signals. Cross-learning or explicitly separated latent factors try to preserve them.
- Maximum mean discrepancy can replace or supplement KL-based regularization and can align modality or condition distributions.
- Supervised auxiliary losses make the latent variables useful for outcomes such as cancer classification, survival, or drug response rather than reconstruction alone.
- Adversarial discriminators align modalities or batches by penalizing latent representations that reveal their origin; [GLUE](../entities/GLUE.md) is the collection's main graph-guided example.
- Cycle-consistency checks whether a representation translated through another modality returns to its original latent state.
- Contrastive objectives pull known positive cross-modal pairs together and separate negative pairs.
- Disentanglement objectives separate shared biology, condition-specific biology, and technical variation; [MIDAS](../entities/MIDAS.md) is the collection's main information-bottleneck example.
- For missing modalities, product-of-experts models can omit an unavailable posterior, masked training can teach feature recovery, and decoders can generate the absent block. [MultiVI](../entities/MultiVI.md) and MIDAS instantiate different versions of these ideas.

## Evidence And Scope

- Table 1 supplies a qualitative comparison of six broad method categories by strengths, limitations, and typical applications.
- Table 2 inventories deep generative methods, their omics demonstrations, integration setting, method design, and intended applications.
- The review connects classical methods to recent single-cell systems including [MultiVI](../entities/MultiVI.md), [GLUE](../entities/GLUE.md), [MIDAS](../entities/MIDAS.md), Cobolt, [scMVP](../entities/scMVP.md), [totalVI](../entities/totalVI.md), [StabMap](../entities/StabMap.md), Multigrate, [scVAEIT](../entities/scVAEIT.md), and related VAE or adversarial models.
- The authors describe this as the first systematic review centered specifically on VAE architectures, loss functions, and regularization for multi-omics integration. This is an author claim, not independently tested in the paper.
- The evidence is a technical synthesis of prior publications rather than a new benchmark, dataset, or experimental validation study.

## Interpretation

- `Integration regime` and `algorithm family` should not be collapsed into one taxonomy: one states which correspondences exist, while the other states how the method exploits or reconstructs them.
- Deep generative flexibility comes from composable losses and likelihoods, but each added term introduces another weighting, optimization, or identifiability choice.
- A good joint embedding is not automatically good imputation, regulatory inference, or outcome prediction. Those outputs need task-specific evaluation.
- Classical models remain credible baselines when interpretability, small sample size, or computational efficiency matters.
- The review explicitly distinguishes multi-omics integration from broader multimodal learning that incorporates imaging, phenotypes, electronic health records, or wearable signals.

## Limitations

- No harmonized quantitative benchmark is performed across the reviewed categories, so the paper cannot rank methods under a shared dataset, preprocessing pipeline, or metric set.
- The method inventory is broad, but its deep-generative discussion is concentrated on scRNA-seq and scATAC-seq because those assays dominate available paired and mosaic benchmarks.
- Qualitative family-level strengths and weaknesses do not guarantee the behavior of every implementation.
- The review notes that VAEs can prioritize reconstruction over informative latent variables, become unstable with limited data, demand GPU and memory resources, and lose modality-specific information in a shared space.
- Foundation models are presented as promising, while concerns about their advantage over strong task-specific methods remain unresolved.

## Related Pages

- [Multi-Omics Integration Method Taxonomy](../concepts/multi-omics-integration-method-taxonomy.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [Cross-modality Generation](../concepts/cross-modality-generation.md)
- [Multimodal Foundation Models](../concepts/multimodal-foundation-models.md)
- [MIDAS](../entities/MIDAS.md)
- [GLUE](../entities/GLUE.md)
- [MultiVI](../entities/MultiVI.md)

## Open Questions

- Which benchmarks can compare interpretability, biological conservation, batch removal, missing-modality reconstruction, and compute without hiding their incompatible objectives inside one aggregate score?
- When does a shared latent representation erase scientifically important modality-specific variation?
- How much paired or overlapping data is required before mosaic imputation becomes reliable enough for downstream biological claims?
- Which VAE regularizers remain stable when sample size is small relative to feature dimension and modality count?
- For which multi-omics tasks do foundation models outperform well-tuned classical or task-specific generative methods after controlling for compute and training data?

## Parsed Artifacts

- Parser: OpenDataLoader PDF with reading-order inference disabled after the default list processor aborted.
- Markdown: [raw/derived/opendataloader/baiao_2025_technical_review_multi-omics_integration_methods/baiao_2025_technical_review_multi-omics_integration_methods.md](../../raw/derived/opendataloader/baiao_2025_technical_review_multi-omics_integration_methods/baiao_2025_technical_review_multi-omics_integration_methods.md)
- Manifest: [raw/derived/opendataloader/baiao_2025_technical_review_multi-omics_integration_methods/opendataloader-run.json](../../raw/derived/opendataloader/baiao_2025_technical_review_multi-omics_integration_methods/opendataloader-run.json)
- Poppler layout text: [raw/derived/pdftext/Baiao_2025_Multiomics_Review/Baiao_2025_Multiomics_Review.txt](../../raw/derived/pdftext/Baiao_2025_Multiomics_Review/Baiao_2025_Multiomics_Review.txt)
- These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
