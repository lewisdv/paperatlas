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

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-12T12:42:38+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/kanton_2019_organoid_single-cell_genomic_atlas.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas -f json,markdown`
- Manifest: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/opendataloader-run.json](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/opendataloader-run.json)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas.json](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas.json)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas.md](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas.md)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile1.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile1.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile10.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile10.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile11.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile11.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile12.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile12.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile13.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile13.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile14.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile14.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile15.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile15.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile16.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile16.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile17.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile17.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile18.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile18.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile19.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile19.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile2.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile2.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile20.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile20.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile21.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile21.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile22.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile22.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile23.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile23.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile24.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile24.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile25.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile25.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile26.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile26.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile27.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile27.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile28.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile28.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile29.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile29.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile3.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile3.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile30.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile30.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile31.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile31.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile32.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile32.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile33.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile33.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile34.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile34.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile35.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile35.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile36.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile36.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile37.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile37.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile38.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile38.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile39.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile39.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile4.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile4.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile40.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile40.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile41.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile41.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile42.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile42.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile43.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile43.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile44.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile44.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile45.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile45.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile46.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile46.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile47.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile47.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile48.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile48.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile49.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile49.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile5.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile5.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile50.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile50.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile51.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile51.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile52.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile52.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile53.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile53.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile54.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile54.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile55.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile55.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile56.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile56.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile57.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile57.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile58.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile58.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile59.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile59.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile6.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile6.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile60.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile60.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile61.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile61.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile62.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile62.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile63.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile63.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile64.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile64.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile65.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile65.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile66.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile66.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile67.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile67.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile68.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile68.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile69.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile69.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile7.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile7.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile70.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile70.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile71.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile71.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile72.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile72.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile73.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile73.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile74.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile74.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile75.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile75.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile76.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile76.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile77.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile77.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile78.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile78.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile79.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile79.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile8.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile8.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile80.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile80.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile81.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile81.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile82.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile82.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile83.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile83.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile84.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile84.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile85.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile85.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile86.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile86.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile87.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile87.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile88.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile88.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile89.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile89.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile9.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile9.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile90.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile90.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile91.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile91.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile92.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile92.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile93.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile93.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile94.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile94.png)
- Output: [raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile95.png](../../raw/derived/opendataloader/kanton_2019_organoid_single-cell_genomic_atlas/kanton_2019_organoid_single-cell_genomic_atlas_images/imageFile95.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
