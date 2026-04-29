---
title: Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus
kind: paper
status: ingested
added: 2026-04-29T22:28:12+09:00
raw_source: raw/sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.pdf
---

# Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus

## Source

- File: [raw/sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.pdf](../../raw/sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.pdf)
- Added: 2026-04-29T22:28:12+09:00
- Venue/status: Science Advances research article; 2023
- Authors: Brian R. Herb, Hannah J. Glover, Aparna Bhaduri, Carlo Colantuoni, Tracy L. Bale, Kimberly Siletti, Rebecca Hodge, Ed Lein, Arnold R. Kriegstein, Claudia A. Doege, and Seth A. Ament

## Summary

This paper builds a large single-cell and single-nucleus transcriptomic atlas of the prenatal and adult human hypothalamus to trace developmental trajectories into mature neuronal diversity. It integrates prenatal and adult data to identify robust hypothalamic neuronal subtypes, infer region-specific developmental programs, and compare lineage drivers across human forebrain regions and across species. In this collection, the paper matters because it strengthens the `region-specific developmental trajectory` and `reference atlas` threads that later modeling systems may use for trajectory benchmarking or developmental-state mapping.

## Methods

- The study profiles prenatal human hypothalamus with scRNA-seq across gestational weeks `6` to `25` and adult hypothalamus with snRNA-seq from three neurotypical donors.
- It integrates `241,096` cells in total, including `126,840` newly generated cells, with previously published prenatal hypothalamus data to build a development-to-adulthood atlas.
- Monocle3 pseudotime trajectories are used to trace lineages from progenitor populations into mature neuronal nuclei.
- Adult neuronal diversity is resolved by iterative hierarchical clustering across `15` resolutions, with stability analysis selecting `108` robust transcriptionally distinct neuronal subtypes.
- Comparative analyses align human hypothalamic trajectories with mouse hypothalamus data and with excitatory and inhibitory lineages in cortex and ganglionic eminence.

## Key Claims

- Region-specific developmental trajectories are a major determinant of mature hypothalamic neuronal diversity.
- The adult human hypothalamus contains a much richer subtype structure than coarse cell-class labels capture, including more than a hundred robust transcriptional neuronal subtypes.
- Many hypothalamic neuronal programs are conserved with mouse, but species-enriched gene expression and regulatory differences remain important.
- Shared excitatory or inhibitory forebrain programs are refined by region-specific regulators early in development.

## Evidence

- The atlas integrates `241,096` cells, including `40,927` prenatal cells generated in this study, `114,256` additional prenatal cells from Zhou et al., and `85,913` adult nuclei.
- The adult hypothalamus clustering resolves `108` robust transcriptionally distinct neuronal subtypes spanning `10` hypothalamic nuclei, plus zona incerta populations.
- Pseudotime analyses organize prenatal-to-adult trajectories and identify genes associated with the formation of specific nuclei.
- Cross-species comparison finds putative mouse homologs for `105` of the `108` human neuron clusters, supporting broad conservation with targeted differences.
- The paper also compares hypothalamic lineages with cortical excitatory and ganglionic-eminence inhibitory lineages to show both shared and distinct maturation drivers across the human forebrain.

## Limitations

- The study lacks third-trimester and postnatal developmental samples, leaving later maturation unresolved.
- Adult samples are all male, so sex differences cannot be assessed from this source.
- Spatial placement of inferred nuclei and trajectories remains partly bioinformatic and would benefit from additional spatial transcriptomic validation.
- In this collection, the paper functions primarily as a developmental reference atlas rather than as a reusable deep model.

## Related Pages

- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)

## Open Questions

- Which developmental trajectory features here could serve as the strongest benchmark for future generative or trajectory-aware models in this collection?
- How much of the region-specific regulatory divergence would remain if later gestational and postnatal samples were added?
- If more primary developmental atlases enter the collection, should hypothalamus, organoid, and skeletal references be synthesized into a broader `developmental substrate` view?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:26:44+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.pdf -o /tmp/odl-check-hypothalamus -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/herb_2023_single-cell_genomics_reveals_region-specific_developmental/opendataloader-run.json](../../raw/derived/opendataloader/herb_2023_single-cell_genomics_reveals_region-specific_developmental/opendataloader-run.json)
- Output: [raw/derived/opendataloader/herb_2023_single-cell_genomics_reveals_region-specific_developmental/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md](../../raw/derived/opendataloader/herb_2023_single-cell_genomics_reveals_region-specific_developmental/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
