# HiFi vs ONT

## Current corpus readout

- HiFi currently looks strongest for general-purpose variant-calling accuracy in this corpus.
- ONT looks strongest where native-DNA properties matter, especially methylation-aware workflows and flexible large-scale deployment.

## Evidence in this corpus

- [Mahmoud 2024](../sources/2024_mahmoud_utility-long-read-sequencing-all-of-us.md) argues most clearly that HiFi gives the best overall small- and large-variant accuracy in its pilot comparisons.
- [Hard 2023](../sources/2023_hard_long-read-whole-genome-analysis-human-single-cells.md) uses PacBio HiFi for single-cell long-read work where per-read accuracy is critical.
- [Showpnil 2024](../sources/2024_showpnil_long-read-genome-sequencing-complex-rearrangements-rare-syndromes.md) uses HiFi for breakpoint-level rare disease resolution.
- [Otsuki 2022](../sources/2022_otsuki_trio-structural-variation-panel-activated-t-lymphocytes.md), [Sinha 2025](../sources/2025_sinha_long-read-sequencing-rare-diseases.md), and [Schloissnig 2025](../sources/2025_schloissnig_structural-variation-1019-diverse-humans-long-read-sequencing.md) show strong ONT use in population and clinical workflows.

## Practical interpretation

- If the main target is maximal variant accuracy across small and large variants, HiFi currently has the cleaner case in this corpus.
- If the workflow needs native methylation, flexible deployment, or large-scale long-read acquisition, ONT has strong representation here.

## Open questions

- How quickly does ONT duplex or later chemistry narrow the current HiFi accuracy edge?
- Which clinical use cases genuinely need HiFi, and which are already well served by ONT plus strong downstream filtering?
