---
title: scMultiMap: Cell-type-specific mapping of enhancers and target genes from single-cell multimodal data
kind: paper
status: ingested
added: 2026-07-29T17:52:24+09:00
raw_source: raw/sources/su_2025_scmultimap_enhancer_target_gene_mapping.pdf
---

# scMultiMap: Cell-type-specific mapping of enhancers and target genes from single-cell multimodal data

## Source

- File: [raw/sources/su_2025_scmultimap_enhancer_target_gene_mapping.pdf](../../raw/sources/su_2025_scmultimap_enhancer_target_gene_mapping.pdf)
- Added: 2026-07-29T17:52:24+09:00
- Venue/status: Nature Communications 16, 3941 (2025)
- Authors: Chang Su, Dongsoo Lee, Peng Jin, and Jingfei Zhang
- DOI: `10.1038/s41467-025-59306-z`
- SHA-256: `458e955c1e139cd0c2548a3b45888e9554a9b84adc6f6a12005f53e75af94af7`

## Summary

scMultiMap is a statistical method for identifying cell-type-specific enhancer-gene associations from paired single-cell RNA and ATAC counts. Rather than integrating cells into a shared embedding, it estimates correlation between latent expression and accessibility while explicitly accounting for RNA/ATAC sequencing depth and subject-specific mean shifts. Moment-based estimation and an analytic null distribution replace costly bootstrap or sampling-based tests. The paper emphasizes valid type-I error, power, reproducibility, external chromatin-contact support, and application to Alzheimer disease genetics.

## Methods

- A joint latent-variable model treats observed gene and peak counts as Poisson measurements of underlying relative expression and accessibility.
- Covariance between the latent abundance variables defines the peak-gene association and is separated from correlated sequencing depths.
- Subject indicators model between-sample mean shifts to avoid pooling-induced spurious associations.
- Iteratively reweighted least squares estimates gene/peak means and variances; weighted moment regression estimates covariance.
- An asymptotic normal test provides analytic p-values without Monte Carlo sampling.

## Key Claims

- Proper count and confounder modeling controls false positives better than correlation-based or binarized-peak methods.
- Analytic moment-based inference makes genome-scale cell-type-specific peak-gene testing much faster.
- Associations from paired multimodal cells can connect noncoding GWAS variants to plausible target genes in disease-relevant cell types.

## Evidence

- In null PBMC data, empirical type-I error tracks the nominal `0.05`, while SCENT is sometimes conservative or inflated and Signac is inflated.
- On `729` cells and `31,132` candidate pairs, the paper reports computational cost below `1%` of the comparison methods.
- scMultiMap findings are more reproducible across replicate PBMC and brain datasets and more consistent with promoter-capture Hi-C, HiChIP, PLAC-seq, and cell-type eQTL evidence.
- In Alzheimer disease data, scMultiMap peaks show the highest reported microglial heritability enrichment among the compared methods.
- The application nominates context-specific links including `rs10792831-PICALM` and `rs4075111-INPP5D`, but these remain hypotheses rather than validated causal mechanisms.

## Limitations

- scMultiMap requires paired RNA and ATAC measurements in the same cells and cannot analyze fully unpaired data.
- Chromatin accessibility is necessary but not sufficient to define an enhancer; histone marks or perturbational validation are needed.
- The conditional Poisson measurement model may need a negative-binomial extension when sequencing introduces additional dispersion.
- Cell-type-specific subsets often contain only a few hundred cells, leaving low-to-moderate power despite the method's relative advantage.
- Pairwise association does not establish causality or uniquely identify a regulatory mechanism.

## Related Pages

- [scMultiMap](../entities/scMultiMap.md)
- [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md)
- [GLUE](../entities/GLUE.md)
- [scooby](../entities/scooby.md)

## Open Questions

- How many cells and donors are needed for stable disease-versus-control differential association?
- Can the framework incorporate histone marks without losing analytic inference and scalability?
- Which predicted disease-variant links survive CRISPR or other direct perturbational validation?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-07-29T18:04:58+0900
- Manifest: [raw/derived/opendataloader/su_2025_scmultimap_enhancer_target_gene_mapping/opendataloader-run.json](../../raw/derived/opendataloader/su_2025_scmultimap_enhancer_target_gene_mapping/opendataloader-run.json)
- Output: [raw/derived/opendataloader/su_2025_scmultimap_enhancer_target_gene_mapping/su_2025_scmultimap_enhancer_target_gene_mapping.md](../../raw/derived/opendataloader/su_2025_scmultimap_enhancer_target_gene_mapping/su_2025_scmultimap_enhancer_target_gene_mapping.md)
- Layout text: [raw/derived/pdftext/Su_2025_scMultiMap/Su_2025_scMultiMap.txt](../../raw/derived/pdftext/Su_2025_scMultiMap/Su_2025_scMultiMap.txt)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
