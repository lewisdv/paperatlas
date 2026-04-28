---
title: Multi-platform discovery of haplotype-resolved structural variation in human genomes
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/chaisson_2019_multi-platform_discovery_of_haplotype-resolved_structural.pdf
deep_ingested: 2026-04-07
---

# Multi-platform discovery of haplotype-resolved structural variation in human genomes

## Source

- PDF: [raw/sources/chaisson_2019_multi-platform_discovery_of_haplotype-resolved_structural.pdf](../../raw/sources/chaisson_2019_multi-platform_discovery_of_haplotype-resolved_structural.pdf)
- Status: deep ingested on 2026-04-07
- Scope: foundational benchmark paper for multi-platform structural variant discovery in human genomes

## Study design

- Samples: 3 human trios analyzed in a haplotype-resolved way
- Platform: integrated long-read sequencing, short-read sequencing, Strand-seq, optical mapping, and multiple discovery algorithms
- Aim: define a high-sensitivity reference set for indels, SVs, and inversions, and quantify what standard short-read studies miss

## Summary

- This paper establishes the benchmark logic for much of the later Long Read WGS literature in this corpus: structural variation is systematically undercounted when sequencing and calling are dominated by short reads.
- By combining multiple orthogonal technologies, the authors report roughly 818,054 indels and 27,622 SVs per genome, plus about 156 inversions per genome.
- The main practical message is not that every future study should use the full multi-platform stack, but that long-read-aware workflows are necessary if the goal is comprehensive SV discovery.

## Key findings

- The integrated callset produces a threefold to sevenfold increase in SV discovery relative to standard high-throughput sequencing studies, including 1000 Genomes Project-era short-read workflows.
- The authors estimate that routine short-read calling misses most insertions, especially tandem-repeat and retrotransposon insertions in the 50 bp to 2 kb range.
- Inversion discovery improves dramatically when orthogonal technologies are combined; many events land near regions implicated in recurrent microdeletion and microduplication syndromes.
- Downsampling analysis suggests that coverage reduction matters less than poor caller choice and default-parameter use, which is a useful operational lesson for real-world pipelines.

## Strengths

- Exceptionally strong benchmark framing through orthogonal technologies rather than one platform or one caller.
- Haplotype-aware design makes the paper more useful than a simple aggregate SV catalog.
- The paper explicitly discusses cost-versus-sensitivity tradeoffs instead of only maximizing discovery in an unrealistic setup.

## Limitations and caveats

- The design is not operationally realistic for routine clinical or population-scale deployment.
- Only three trios were profiled, so the paper is a benchmark study rather than a population atlas.
- Some of its practical recommendations are historically important but should now be reinterpreted in light of newer HiFi-centered workflows.

## Relevance to this corpus

- This is the conceptual anchor for the corpus.
- Later studies in this collection largely validate the same thesis in more applied settings: long-read WGS is most valuable where insertions, repeats, inversions, dead zones, and complex rearrangements matter.

## Related concepts

- [Structural variation](../concepts/structural-variation.md)
- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)
- [Complex rearrangements and hard regions](../concepts/complex-rearrangements-and-hard-regions.md)

## Open questions

- How close can modern single-platform HiFi workflows get to this benchmark without the full multi-platform stack?
- Which inversion classes still require orthogonal technologies beyond routine long-read WGS?
