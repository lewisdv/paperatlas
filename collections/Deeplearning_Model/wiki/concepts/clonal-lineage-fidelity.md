# Clonal Lineage Fidelity

## Definition

- Clonal lineage fidelity asks whether an in vitro or generated developmental system preserves the division sequence, output size, birth-order logic, and within-clone cell-type diversity of a primary lineage.
- It is distinct from transcriptomic fidelity: cells can map well to reference states and lie on a plausible inferred trajectory while their clonally related progeny follow a different temporal or fate-output program.

## In This Collection

- [Stouffer et al. 2026](../sources/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.md) provides the direct example. Mouse cortical organoids match major Emx1-lineage transcriptional states and a unitary RGP-to-neuron trajectory, yet MADM lineage tracing shows concurrent clone architectures and much more frequent deep- or upper-layer-restricted clones than in the in vivo comparator.
- [HNOCA](../entities/HNOCA.md) supplies a complementary population-level atlas framework: it measures reference coverage, annotation, timing, and transcriptomic divergence across human neural organoids, but does not by itself test clonal output or birth order.
- This concept therefore extends [Transcriptomic Fidelity Benchmarking](transcriptomic-fidelity-benchmarking.md) rather than replacing it. A strong organoid evaluation may need both transcriptomic reference matching and lineage-resolved validation appropriate to the biological question.

## What It Can Test

- Temporal ordering and coexistence of progenitor division modes.
- Clone size, sister-lineage balance, and persistence of progenitor potential.
- Whether one progenitor yields the expected range and temporal order of descendant cell identities.
- Alignment or mismatch between clone architecture, spatial position, transcriptomic identity, and pseudotime.

## Caveats

- Direct clonal assays are system-, species-, reporter-, and time-window-specific; they do not automatically establish a universal lineage rule.
- Clone architecture can be affected by labeling efficiency, reconstruction, sparse cell loss, marker choice, and incomplete capture of long-term descendants.
- Neither clonal lineage fidelity nor transcriptomic fidelity proves complete functional, circuit, or disease-model fidelity. They measure different biological constraints.

## Sources

- [Temporal uncoupling of radial glia lineage progression in cortical organoids](../sources/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.md)
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
