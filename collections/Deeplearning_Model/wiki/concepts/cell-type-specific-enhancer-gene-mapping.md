# Cell-Type-Specific Enhancer-Gene Mapping

## Definition

- This task links accessible noncoding regions to target-gene expression within a particular cell type or state.
- It aims to interpret regulatory mechanisms and noncoding disease variants more specifically than bulk-tissue maps.

## Approaches In This Collection

- [scMultiMap](../entities/scMultiMap.md) uses paired RNA/ATAC counts, explicit depth/subject adjustment, and analytic association tests.
- [GLUE](../entities/GLUE.md) combines an external peak-gene guidance graph with unpaired multi-omics observations and derives embedding-similarity regulatory scores.
- [scooby](../entities/scooby.md) predicts profile changes from edited DNA sequence, allowing in silico motif or variant perturbation in specific cell embeddings.

## Evidence Boundaries

- Accessibility is a proxy for regulatory activity, not proof that a peak is an enhancer.
- Association and embedding similarity do not establish causal direction.
- Sequence perturbation predictions depend on model calibration and remain in silico.
- Orthogonal chromatin-contact, histone-mark, eQTL, and CRISPR evidence strengthen a link but answer different questions.

## Sources

- [scMultiMap](../sources/su_2025_scmultimap_enhancer_target_gene_mapping.md)
- [GLUE](../sources/cao_2022_glue_multi-omics_integration_regulatory_inference.md)
- [scooby](../sources/hingerl_2024_scooby_multimodal_genomic_profiles.md)
