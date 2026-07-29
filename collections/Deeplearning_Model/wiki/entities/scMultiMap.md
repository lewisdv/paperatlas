# scMultiMap

## Type

- Statistical enhancer-gene association method

## Definition

- scMultiMap tests cell-type-specific peak-gene associations from paired scRNA-seq and scATAC-seq counts.
- It separates latent biological covariance from sequencing-depth and subject-level confounding.

## Core Method

- Joint nonparametric latent abundance model with Poisson measurement distributions.
- Subject-specific means and explicit RNA/ATAC depth adjustment.
- Iteratively reweighted moment estimators for means, variances, and covariance.
- Analytically derived p-values rather than bootstrap or random-background inference.

## Reported Uses

- Reproducible enhancer-gene mapping in blood and brain cell types.
- TF-peak-gene trio construction.
- Differential regulatory association in Alzheimer disease.
- Linking microglial GWAS variants to candidate target genes.

## Caveats

- Requires paired modalities in the same cells.
- Accessibility alone does not prove enhancer activity.
- Sparse cell-type subsets limit power, and pairwise association is not causality.

## Related

- [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md)
- [GLUE](GLUE.md)
- [scooby](scooby.md)
- [Source: scMultiMap](../sources/su_2025_scmultimap_enhancer_target_gene_mapping.md)
