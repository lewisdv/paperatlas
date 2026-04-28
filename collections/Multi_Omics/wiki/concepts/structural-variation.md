# Structural Variation

## Working definition

Structural variants in this corpus are genomic alterations typically 50 bp or larger, including deletions, insertions, duplications, inversions, translocations, mobile element insertions, and repeat-mediated events.

## What this corpus says

- Structural variation is the clearest and most consistent advantage zone for long-read WGS.
- Long reads especially improve discovery of insertions, inversions, repeat-associated events, and rearrangements that short reads undercount or mischaracterize.
- Population-scale long-read SV resources are becoming useful not only for discovery but also for patient-level filtering.
- The clinically important shift is not just more calls, but more sequence-resolved and structurally interpretable calls.

## Supporting sources

- [Chaisson 2019](../sources/2019_chaisson_multi-platform-haplotype-resolved-structural-variation-human-genomes.md)
- [Kosugi 2024](../sources/2024_kosugi_comparative-evaluation-short-vs-long-read-variants.md)
- [Otsuki 2022](../sources/2022_otsuki_trio-structural-variation-panel-activated-t-lymphocytes.md)
- [Gong 2025](../sources/2025_gong_long-read-sequencing-945-han-individuals.md)
- [Schloissnig 2025](../sources/2025_schloissnig_structural-variation-1019-diverse-humans-long-read-sequencing.md)
- [Showpnil 2024](../sources/2024_showpnil_long-read-genome-sequencing-complex-rearrangements-rare-syndromes.md)

## Current takeaways

- Insertions are disproportionately missed by short-read workflows.
- Inversions and large complex events still often benefit from orthogonal or graph-aware approaches even within the long-read era.
- SV reference panels and atlases are becoming a realistic extension of long-read cohort studies.

## Open questions

- Which SV classes now require full multi-platform support, and which are well covered by modern single-platform long-read workflows?
- How should SV resources be integrated into routine clinical prioritization pipelines?
