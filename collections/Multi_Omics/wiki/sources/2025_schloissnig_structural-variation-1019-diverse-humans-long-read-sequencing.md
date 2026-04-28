---
title: Structural variation in 1,019 diverse humans based on long-read sequencing
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/schloissnig_2025_structural_variation_in_1019_diverse.pdf
deep_ingested: 2026-04-07
---

# Structural variation in 1,019 diverse humans based on long-read sequencing

## Source

- PDF: [raw/sources/schloissnig_2025_structural_variation_in_1019_diverse.pdf](../../raw/sources/schloissnig_2025_structural_variation_in_1019_diverse.pdf)
- Status: deep ingested on 2026-04-07
- Scope: globally diverse long-read population resource for SVs and VNTRs, built at intermediate coverage

## Study design

- Samples: 1,019 individuals from 26 populations linked to the 1000 Genomes Project
- Platform: intermediate-coverage long-read sequencing with integrated linear- and graph-genome analyses
- Aim: generate a diverse population SV resource and test whether it improves downstream variant prioritization

## Summary

- This paper is the most globally representative population resource in the corpus.
- It shows that intermediate-coverage long-read sequencing can still produce a highly useful SV atlas when paired with strong graph-aware analysis.
- The clinical hook is important: using the resource reduces rare disease candidate SV lists substantially while retaining most known causal events.

## Key findings

- The study reports over 100,000 sequence-resolved biallelic SVs and 300,000 multiallelic VNTRs.
- Many insertions, especially mobile element insertions, were not represented in prior large resources such as gnomAD.
- When used for rare disease filtering, the resource cut candidate SV lists by roughly 55% while filtering out only 2 of 35 previously validated causal SVs in the authors' evaluation.
- The paper also highlights graph-based analysis as a major enabler for population-scale long-read interpretation.

## Strengths

- Strong population diversity relative to many earlier long-read atlas papers.
- Connects resource building to practical patient-genome filtering.
- Clear discussion of where long-read graph-based approaches already work and where they still struggle.

## Limitations and caveats

- Extremely rare SVs, large inversions, centromeres, high-identity segmental duplications, and multiallelic VNTRs remain difficult.
- Intermediate coverage is a practical compromise, not a complete replacement for deeper multi-platform assemblies.
- The study is strongest on SVs and related repetitive variation, not on full-spectrum clinical WGS.

## Relevance to this corpus

- This is the strongest paper in the corpus for the idea that long-read population resources can directly improve patient-level filtering.
- It complements Otsuki and Gong by adding much broader ancestry coverage.

## Related concepts

- [Population-scale SV atlases](../concepts/population-scale-sv-atlases.md)
- [Structural variation](../concepts/structural-variation.md)
- [Complex rearrangements and hard regions](../concepts/complex-rearrangements-and-hard-regions.md)

## Open questions

- How much better do candidate-filtering resources become when intermediate-coverage long reads are paired with deeper assemblies in representative subsets?
- What is the best way to combine graph-based population resources with clinical interpretation pipelines?
