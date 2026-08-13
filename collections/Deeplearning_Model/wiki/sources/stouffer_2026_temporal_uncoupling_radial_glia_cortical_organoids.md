---
title: Temporal uncoupling of radial glia lineage progression in cortical organoids
kind: paper
status: ingested
added: 2026-08-13T10:50:33+09:00
raw_source: raw/sources/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.pdf
---

# Temporal uncoupling of radial glia lineage progression in cortical organoids

## Source

- File: [raw/sources/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.pdf](../../raw/sources/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.pdf)
- Added: 2026-08-13T10:50:33+09:00
- Authors: Melissa Stouffer, Osvaldo A. Miranda, Florian M. Pauler, Fabrizia Pipicelli, Carmen Streicher, Giselle Cheung, and Simon Hippenmeyer
- Venue/status: *Nature*, accepted 15 July 2026; open-access article
- DOI: [10.1038/s41586-026-10916-7](https://doi.org/10.1038/s41586-026-10916-7)
- Data: GEO `GSE327470`; analysis code and figure scripts: [Zenodo 10.5281/zenodo.21032850](https://doi.org/10.5281/zenodo.21032850)
- SHA-256: `348e8b26957b7ab4baafddd21bb66365468685a54b199c00cc93bb52a4b114b3`

## Summary

- This is a mouse embryonic-stem-cell cortical-organoid study that combines single-cell RNA-seq with Mosaic Analysis with Double Markers (MADM) lineage tracing. It asks whether a self-organizing organoid reproduces the quantitatively timed radial glial progenitor (RGP) lineage program measured in mouse cortex in vivo.
- The organoids reproduce major Emx1-lineage cell types, matched developmental abundance trends, and a unitary transcriptional RGP-to-neuron trajectory. Yet clonal observations differ: proliferative, asymmetric neurogenic, and organoid-specific small neurogenic clone architectures coexist at the same time points, and RGP clones are much more often restricted to deep- or upper-layer projection-neuron identity.
- The key result is an evidence-boundary result for organoid evaluation: matching scRNA-seq states or one inferred trajectory does not ensure faithful clonal lineage progression, temporal division control, or within-clone neuronal diversity.

## Experimental and Analytical Design

- The authors derive mESCs carrying Emx1-lineage reporters and generate cortical organoids. 10X FLEX scRNA-seq samples at differentiation days D8, D13, D20, and D25 are compared with mouse cortex at E10, E13, E16, and P1; after quality control, individual samples retain 1,302–9,220 organoid cells and 3,422–9,314 embryo cells.
- For clonal analysis, an inducible `MADM-11GT/TG;Emx1-creER` system uses 4-hydroxytamoxifen induction from D8 through D15 and analyzes clones at D20 (with a D15 check). Different fluorescent sister lineages permit in situ reconstruction of proliferative, asymmetric neurogenic, and small neurogenic clone architectures.
- `MADM-CloneSeq` joins clone assignment, spatial information, and Smart-seq3 transcriptomes. The study sequences 287 cells from 68 clones induced at D13 in 45 organoids; after quality and annotation filtering, 195 neuronal cells from 21 asymmetric and 34 small neurogenic clones support clone-level deep/upper-layer and pseudotime analyses.
- Organoid-to-embryo single-cell comparison uses CSS integration, reference annotation/nearest-neighbor projection, and marker analysis. Slingshot is used for the organoid RGP-to-neuron trajectory; these transcriptomic analyses complement rather than replace direct lineage tracing.

## Reported Findings

- At population level, organoid and embryo Emx1-lineage cell types, marker profiles, and broad developmental abundance curves are reported as similar. D8, D13, D20, and D25 are matched to E10, E13, E16, and P1, respectively, by transcriptomic signature and cell-type abundance trends.
- In contrast to the sequential in vivo program, all three observed clone architectures occur concurrently at each organoid induction point. Proliferative clone output declines over time, but not with the sharp, stage-specific switch described in vivo; organoid-specific small neurogenic clones persist even after a D15 analysis designed to reduce a simple cell-death explanation.
- RGP clone output is more lineage-restricted in organoids: 31/87 (35.6%) D8-induced and 25/78 (32.1%) D13-induced clones produce only CTIP2-positive deep-layer or only SATB2-positive upper-layer neurons, versus 11/386 (2.85%) in the cited in vivo comparison. The paper interprets this as reduced within-clone projection-neuron diversity.
- MADM-CloneSeq corroborates that both asymmetric and small neurogenic clones can be deep-layer-, upper-layer-, or translaminar. Lineage-restricted versus translaminar small clones do not differ significantly in the reported pseudotime comparison, arguing against simple developmental delay as the explanation.
- Transcriptomic analysis finds no separate organoid-specific RGP cluster and reports a single RGP-via-intermediate-progenitor-to-neuron trajectory across tested dimensionality/clustering settings. Nonetheless, hundreds of RGP differential-expression changes versus embryo are reported, with enrichment in regionalization, metabolism, development, and signaling terms.
- Organoids retain a later neurogenic-to-gliogenic transition: glia are scarce at D20 but occur in about 46% of clones at D25. Thus, the source does not claim wholesale organoid failure; it identifies a specific loss or alteration of temporal control and clonal fate diversity within otherwise broadly matched development.

## Interpretation Boundaries and Limitations

- The primary system is a self-organizing **mouse** mESC cortical organoid and its mouse in vivo reference. Its timing, lineage rules, and niche interpretation should not be directly generalized to human cortical organoids, human fetal cortex, or disease models.
- MADM measures marked clone architectures in this experimental setting, but clone classes are interpreted as progenitor division modes. Sparse sporadic cell death, undetected minor diverging sublineages, and limitations of the chosen marker/clone reconstruction scheme are not entirely excluded.
- The paper infers missing non-cell-autonomous niche influence from the contrast with in vivo tissue; it does not isolate a single absent cue or demonstrate that any one proposed factor restores the temporal program.
- A unitary scRNA-seq trajectory is an inferred state-space summary, not direct proof of clonal lineage equivalence. Conversely, the study's 195 high-quality MADM-CloneSeq neurons cover selected clone types and time points, not every lineage state or late maturation stage.
- The results sharpen fidelity evaluation rather than invalidate transcriptomic benchmarking: population-level identity, developmental abundance, and clonal lineage behavior are complementary axes that require distinct evidence.

## Related Pages

- [Clonal Lineage Fidelity](../concepts/clonal-lineage-fidelity.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [HNOCA](../entities/HNOCA.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [An integrated transcriptomic cell atlas of human neural organoids](he_2024_an_integrated_transcriptomic_cell_atlas.md)

## Open Questions

- Which niche features or multicellular interactions are sufficient to restore the timed in vivo RGP division sequence and translaminar clone output?
- Which lineage-tracing-compatible assays can add clonal output, birth order, or fate linkage to routine organoid reference-atlas benchmarks?
- Do comparable transcriptome-clone mismatches occur in human cortical organoids and in disease-relevant human genetic backgrounds?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF under OpenJDK 21.0.12
- Generated: 2026-08-13T10:50:33+0900
- Manifest: [raw/derived/opendataloader/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids/opendataloader-run.json](../../raw/derived/opendataloader/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids/opendataloader-run.json)
- Output: [raw/derived/opendataloader/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.md](../../raw/derived/opendataloader/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids/stouffer_2026_temporal_uncoupling_radial_glia_cortical_organoids.md)
- Layout text: [raw/derived/pdftext/Stouffer_2026_Radial_Glia_Cortical_Organoids/Stouffer_2026_Radial_Glia_Cortical_Organoids.txt](../../raw/derived/pdftext/Stouffer_2026_Radial_Glia_Cortical_Organoids/Stouffer_2026_Radial_Glia_Cortical_Organoids.txt)

These helper artifacts support navigation and extraction. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
