---
title: A multi-omic atlas of human embryonic skeletal development
kind: paper
status: ingested
added: 2026-04-29T22:28:12+09:00
raw_source: raw/sources/to_2024_a_multi-omic_atlas_of_human.pdf
---

# A multi-omic atlas of human embryonic skeletal development

## Source

- File: [raw/sources/to_2024_a_multi-omic_atlas_of_human.pdf](../../raw/sources/to_2024_a_multi-omic_atlas_of_human.pdf)
- Added: 2026-04-29T22:28:12+09:00
- Venue/status: Nature article; published online 20 November 2024
- Authors: Ken To, Lijiang Fei, J. Patrick Pett, Kenny Roberts, Raphael Blain, Krzysztof Polanski, Tong Li, Nadav Yayon, Peng He, Chuan Xu, and many co-authors including Sarah A. Teichmann
- DOI: `10.1038/s41586-024-08189-z`

## Summary

This paper builds a multi-omic atlas of human embryonic skeletal development by combining paired transcriptional and epigenetic profiling with spatial transcriptomics across embryonic joint and cranium development. The atlas is used to reconstruct region-specific osteogenic and chondrogenic trajectories, infer regulatory programs, localize progenitor niches, connect cell states to polygenic skeletal traits, and simulate monogenic disease perturbations. In this collection, the paper matters because it adds a developmental multi-omics reference resource that behaves like a substrate for lineage modeling and in silico perturbation, even though it is not itself a general-purpose foundation model.

## Methods

- The study profiles about `336,000` nucleus droplets with paired transcriptional and epigenetic measurements across human embryonic limb and cranial skeletal tissues between `5` and `11` post-conception weeks.
- Spatial transcriptomic measurements are added through in situ sequencing and related spatial assays to place inferred clusters back into anatomical context.
- Combined modeling of transcriptional and epigenetic data is used to reconstruct regionally distinct limb and cranial osteoprogenitor trajectories and the regulatory networks governing intramembranous and endochondral ossification.
- The paper introduces `ISS-Patcher` to impute cell labels onto high-resolution in situ sequencing data and `SNP2Cell` to connect cell-type-specific regulatory networks to polygenic traits such as osteoarthritis.
- The inferred osteolineage trajectories are also used for in silico perturbation of genes implicated in monogenic craniosynostosis.

## Key Claims

- Human embryonic skeletal development contains region-specific osteogenic and chondrogenic trajectories that are better resolved when transcriptional, epigenetic, and spatial information are modeled jointly.
- Multi-omic developmental atlases can uncover regulatory programs and spatial zonation mechanisms that would be difficult to recover from transcriptomics alone.
- The atlas supports disease-oriented inference by linking lineage-specific regulatory states to both polygenic skeletal traits and monogenic developmental perturbations.
- Some chondrocyte origins may be non-canonical, including a predicted contribution from Schwann-cell-related lineages.

## Evidence

- The paper explicitly profiles approximately `336,000` nucleus droplets and spans embryonic development from `5` to `11` post-conception weeks.
- The atlas combines paired multiome data with spatial localization, including a `155`-plex in situ sequencing setup used for regional mapping.
- It reports distinct cranial and limb osteoprogenitor trajectories and regulatory differences between intramembranous and endochondral ossification programs.
- Spatial mapping with `ISS-Patcher` is presented as evidence for progenitor zonation during bone and joint formation.
- `SNP2Cell` and the in silico craniosynostosis perturbation analyses are used to demonstrate that the atlas can support disease-mechanism inference rather than only descriptive annotation.

## Limitations

- This is a developmental atlas and tool paper, not a broad foundation model intended for downstream reuse across many unrelated tasks.
- The developmental window is limited to early embryonic skeletal formation and may not capture later maturation or postnatal remodeling.
- Some lineage and perturbation conclusions, such as non-canonical cellular origins, are model-based predictions rather than direct causal proof.
- In this collection, the paper is most useful as a reference substrate and benchmarking resource, not as a directly comparable model to single-cell FMs.

## Related Pages

- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [HNOCA](../entities/HNOCA.md)

## Open Questions

- How much of the regulatory insight here depends on paired epigenomic measurements versus large enough transcriptomic atlases with good references?
- Could atlas-derived in silico perturbation become a standard pretraining or evaluation target for future developmental models in this collection?
- If more developmental atlas papers are ingested, does the collection need a synthesis separating `reference substrate` papers from `predictive model` papers?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:26:47+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/to_2024_a_multi-omic_atlas_of_human.pdf -o /tmp/odl-check-skeletal -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/to_2024_a_multi-omic_atlas_of_human/opendataloader-run.json](../../raw/derived/opendataloader/to_2024_a_multi-omic_atlas_of_human/opendataloader-run.json)
- Output: [raw/derived/opendataloader/to_2024_a_multi-omic_atlas_of_human/to_2024_a_multi-omic_atlas_of_human.md](../../raw/derived/opendataloader/to_2024_a_multi-omic_atlas_of_human/to_2024_a_multi-omic_atlas_of_human.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
