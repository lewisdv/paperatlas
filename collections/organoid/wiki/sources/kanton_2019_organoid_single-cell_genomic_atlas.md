---
title: "Organoid single-cell genomic atlas uncovers human-specific features of brain development"
kind: paper
status: ingested
added: 2026-04-09T15:30:00+09:00
raw_source: raw/sources/kanton_2019_organoid_single-cell_genomic_atlas.pdf
article_url: https://www.nature.com/articles/s41586-019-1654-9
published_date: 2019-10-16
organ: brain
protocol_focus: longitudinal scRNA-seq + chromatin atlas of cerebral organoid development with cross-species comparison
deep_ingested: 2026-04-09
---

# Organoid single-cell genomic atlas uncovers human-specific features of brain development

## Source

- PDF: [raw/sources/kanton_2019_organoid_single-cell_genomic_atlas.pdf](../../raw/sources/kanton_2019_organoid_single-cell_genomic_atlas.pdf)
- Article: [Nature](https://www.nature.com/articles/s41586-019-1654-9)
- Labs: Barbara Treutlein, J. Gray Camp, Svante Pääbo (Max Planck Leipzig / ETH Zürich)
- Status: deep ingested 2026-04-09

## Study design

- Longitudinal scRNA-seq of cerebral organoids (10x Genomics) from human ESCs (H9) and iPSCs (409b2)
- Time points: pluripotency, 4 days, 10 days, 15 days, 1 month, 2 months, 4 months
- Total human cells: 43,498 + 49,153 neuronal lineage cells across lines
- Cross-species: chimpanzee organoids (36,884 cells) and macaque organoids
- Additional: single-nucleus RNA-seq of adult prefrontal cortex for persistence of developmental differences
- Chromatin accessibility: ATAC-seq throughout cortical development

## Key findings

- **Full developmental trajectory**: pluripotency → neuroectoderm → neuroepithelium → divergent neural fates (dorsal telencephalon, ventral telencephalon, diencephalon, midbrain, hindbrain, retina) → cortical excitatory/inhibitory neurons → astrocytes (by 4 months).
- **Brain-region composition varies across iPSC lines but regional gene expression patterns are highly conserved** — i.e., the identity of each lineage is reproducible even if the proportion is not.
- **Human neuronal development proceeds more slowly** than chimpanzee or macaque counterparts (human-specific temporal extension).
- Human-specific gene expression resolved to distinct progenitor-to-neuron cell states.
- Chromatin accessibility divergence between human and chimpanzee correlates with gene expression and genetic change.
- Some developmental differences persist into adult prefrontal cortex (via snRNA-seq).

## Distinctive contribution in this corpus

- **First longitudinal temporal cell atlas of cerebral organoid development with cross-species comparison.**
- Establishes temporal benchmarking baseline: "what cells should appear at which day in cerebral organoids."
- Provides the cross-species framework that cerebral organoid evolution work (including He 2024) builds on.
- The scRNA-seq data became a foundational input for He 2024's integrated atlas.

## Limitations and caveats

- Only unguided cerebral organoids (Lancaster 2014 protocol); does not generalize directly to guided protocols.
- Two human lines, limited line diversity.
- Chromatin accessibility was on pooled populations rather than single cells.

## Relevance to brain synchronization query

- **The only source in the current corpus with a full day-by-day temporal map of cerebral organoid cell state transitions.**
- Directly addresses the "maturation timeline" axis: when NPCs become neurons, when astrocytes emerge, when regional identity diverges.
- Provides quantitative comparison of human vs chimpanzee vs macaque tempo — first data on inter-species developmental pacing in vitro.

## Related concepts

- [Self-organization and directed patterning](../concepts/self-organization-and-directed-patterning.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Multi-lineage and tissue complexity](../concepts/multi-lineage-and-tissue-complexity.md)

## Related sources

- [Lancaster 2014](lancaster_2014_generation_of_cerebral_organoids_from.md) — protocol whose developmental trajectory this atlas maps.
- [He 2024](he_2024_an_integrated_transcriptomic_cell_atlas.md) — cross-protocol atlas that integrates Kanton's data.
- [Velasco 2019](velasco_2019_individual_brain_organoids_reproducibly.md) — reproducibility study for dorsally patterned alternative.

## Open questions

- How does Kanton's unguided developmental tempo compare to directed protocols (Velasco, Yoon)?
- What is the cost of delayed human neuronal development in a dish — does it matter for disease modeling?
- Can the cross-species framework be extended to non-great-ape primates (e.g., marmoset)?
