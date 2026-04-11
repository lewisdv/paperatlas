---
title: Long-read whole-genome analysis of human single cells
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/hard_2023_long-read_whole-genome_analysis_of_human.pdf
deep_ingested: 2026-04-07
---

# Long-read whole-genome analysis of human single cells

## Source

- PDF: [raw/sources/hard_2023_long-read_whole-genome_analysis_of_human.pdf](../../raw/sources/hard_2023_long-read_whole-genome_analysis_of_human.pdf)
- Status: deep ingested on 2026-04-07
- Scope: proof-of-concept extension of long-read WGS into human single-cell genomics

## Study design

- Samples: clonally expanded CD8+ T cells from a healthy donor
- Platform: droplet-based multiple displacement amplification followed by PacBio HiFi sequencing
- Aim: test whether long-read sequencing can recover SNVs, SVs, tandem repeats, and partial de novo assemblies from single human cells

## Summary

- This paper is a frontier-methods study rather than a diagnostic or population paper.
- It shows that single-cell long-read WGS can recover variant classes and genomic regions that short-read single-cell workflows miss, including repeat-rich and dark regions.
- The signal is real, but the workflow remains constrained by amplification bias, allelic dropout, and chimeric artifacts.

## Key findings

- PacBio sequencing reached up to about 40% genome coverage per single cell.
- The authors report 28 somatic SNVs, including mitochondrial heteroplasmy, and around 5,473 high-confidence SVs per cell.
- Compared with Illumina data from clonally related cells, the long-read workflow detected roughly sixteen times more high-confidence SVs.
- Single-cell de novo assemblies reached up to 598 Mb and recovered 1,762 complete gene models.

## Strengths

- Extends the long-read WGS argument beyond bulk genomes into a technically harder regime.
- Demonstrates clear utility in dark regions, tandem repeats, and partial assembly.
- Explicitly documents artifact sources instead of overclaiming.

## Limitations and caveats

- Single donor, single cell type, and partial genome recovery limit generalization.
- The current workflow is not reliable for inversions and duplications because amplification chimeras create false positives.
- The study depends on whole-genome amplification, which remains the key bottleneck.

## Relevance to this corpus

- This is the most exploratory paper in the corpus.
- It matters less for immediate clinical rare disease workflows and more as a signal of where long-read WGS can expand next once bulk-genome methods mature.

## Related concepts

- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)
- [Structural variation](../concepts/structural-variation.md)

## Open questions

- Can single-cell long-read WGS become robust enough for inversion, duplication, and complex rearrangement analysis without heavy amplification artifacts?
- How much of the current limitation is wet-lab versus bioinformatics?
