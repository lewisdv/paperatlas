---
title: Comparative evaluation of SNVs, indels, and structural variations detected with short- and long-read sequencing data
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/kosugi_2024_comparative_evaluation_of_snvs_indels.pdf
deep_ingested: 2026-04-07
---

# Comparative evaluation of SNVs, indels, and structural variations detected with short- and long-read sequencing data

## Source

- PDF: [raw/sources/kosugi_2024_comparative_evaluation_of_snvs_indels.pdf](../../raw/sources/kosugi_2024_comparative_evaluation_of_snvs_indels.pdf)
- Status: deep ingested on 2026-04-07
- Scope: method-centered comparison of short-read and long-read detection performance across SNVs, indels, and SVs

## Study design

- Samples: benchmarking framework using matched short-read and long-read data
- Platform: 6 SNV callers, 12 indel callers, and 13 SV callers assessed with a manual-visual-inspection correction layer
- Aim: compare variant-calling strengths and weaknesses by variant class and genomic context

## Summary

- This paper is important because it reduces vague claims like "long reads are better" into specific statements about where they are better.
- The strongest long-read advantage appears in insertions greater than 10 bp and in SV detection within repetitive regions, especially STR-rich sequence.
- Outside those contexts, short reads remain more competitive than some long-read advocacy papers imply, especially for SNVs and many deletions in nonrepetitive regions.

## Key findings

- Short-read workflows perform poorly for insertion-rich indel detection once insertion size grows beyond about 10 bp.
- SV recall for short-read callers drops sharply in repetitive regions, especially for small and intermediate-sized SVs.
- In nonrepetitive regions, short-read and long-read workflows can achieve more similar precision and recall for several variant classes.
- The paper argues that combining strong short-read callers can partially mitigate performance gaps when long-read data are unavailable.

## Strengths

- Careful evaluation framework that explicitly corrects for incompleteness in benchmark sets using manual inspection.
- Helpful decomposition by variant class and genomic context.
- Provides a needed "where exactly does long-read help?" lens for interpreting the rest of the corpus.

## Limitations and caveats

- Benchmark correction still depends on limited manual inspections, so estimates are improved rather than perfect.
- Alignment uncertainty in repetitive regions remains a source of residual error even for long reads.
- This is a benchmarking paper, not a clinical-outcome or population-resource paper.

## Relevance to this corpus

- This paper explains why the other papers keep converging on insertions, repeats, SVs, and complex regions as long-read strengths.
- It also keeps the corpus honest by showing that not every variant class justifies long reads equally.

## Related concepts

- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)
- [Structural variation](../concepts/structural-variation.md)
- [Complex rearrangements and hard regions](../concepts/complex-rearrangements-and-hard-regions.md)

## Open questions

- Which hybrid strategies recover most of the long-read advantage when only short-read data are available?
- How much will newer graph-aware short-read and long-read callers shift these boundaries?
