# HNOCA

## Type

- Named atlas / resource

## Definition

- HNOCA is the Human Neural Organoid Cell Atlas, an integrated single-cell transcriptomic atlas of human neural organoids assembled across many protocols and studies.
- In this collection, it functions as a queryable reference resource for annotation, protocol evaluation, and disease-model comparison.

## Core Construction

- Integrates `36` datasets across `26` organoid protocols into a shared atlas of about `1.77` million cells.
- Uses RSS projection, `snapseed`-based preliminary hierarchical annotation, and `scPoli` label-aware integration.
- Maps organoid cells to primary human brain references and supports projection of new datasets into the atlas.

## Reported Uses

- Annotating neural organoid cell types and regions.
- Benchmarking protocol coverage and transcriptomic fidelity against primary human brain references.
- Evaluating morphogen screens and disease-model organoids against a shared control cohort.
- Highlighting under-represented primary neural states in current organoid protocols.

## Caveats

- HNOCA is a reference atlas and benchmarking substrate, not a general-purpose deep model.
- Its conclusions inherit limitations from the underlying public datasets, protocols, and reference mappings.
- Transcriptomic fidelity does not fully resolve functional fidelity.
- It also does not establish clonal division timing, progenitor birth-order logic, or within-clone fate diversity; those require lineage-resolved evidence such as the mouse cortical-organoid MADM study summarized in [Clonal Lineage Fidelity](../concepts/clonal-lineage-fidelity.md).

## Related

- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Clonal Lineage Fidelity](../concepts/clonal-lineage-fidelity.md)
- [Temporal uncoupling of radial glia lineage progression in cortical organoids](../sources/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.md)
- [Source: An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
