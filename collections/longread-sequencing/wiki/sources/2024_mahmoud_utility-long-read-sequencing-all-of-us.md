---
title: Utility of long-read sequencing for All of Us
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/mahmoud_2024_utility_of_long-read_sequencing_for.pdf
deep_ingested: 2026-04-07
---

# Utility of long-read sequencing for All of Us

## Source

- PDF: [raw/sources/mahmoud_2024_utility_of_long-read_sequencing_for.pdf](../../raw/sources/mahmoud_2024_utility_of_long-read_sequencing_for.pdf)
- Status: deep ingested on 2026-04-07
- Scope: pilot comparison of short-read and long-read sequencing strategies for a large national biobank context

## Study design

- Samples: HapMap samples and All of Us control samples spanning eight datasets
- Platform: comparison across short-read and long-read technologies, including PacBio HiFi and ONT, with scalable cloud pipelines
- Aim: determine which long-read approaches are most useful for medically relevant genes, small variants, and SVs in a large-cohort program

## Summary

- This paper asks a deployment question: if a program the size of All of Us considers long reads, what do they buy?
- The answer is that long reads materially improve coverage and variant recovery in medically relevant, technically challenging genes, and that HiFi gives the strongest overall variant-calling accuracy in this pilot.
- The paper also contributes operational infrastructure by releasing a cloud-based long-read analysis pipeline.

## Key findings

- HiFi produced the most accurate results in the study for both small and large variants.
- Long reads improved sequencing and variant calling in challenging medically relevant genes, including complex loci where short reads remain weaker.
- The authors show that machine-learning-based callers and merged calling strategies can improve long-read small-variant performance.
- The paper frames low-coverage long-read sequencing as a potential strategy for scaling sample counts, but treats that as a tradeoff rather than a solved recipe.

## Strengths

- Strong translational relevance to biobank-scale decision-making.
- Focuses on clinically important gene sets rather than only genome-wide aggregate metrics.
- Provides practical pipeline infrastructure instead of only benchmark figures.

## Limitations and caveats

- Pilot scale: the paper does not settle how long-read sequencing should be rolled out across a cohort of one million people.
- Technology conclusions are sensitive to rapidly changing chemistry and caller performance.
- The paper is richer on comparative performance than on end-to-end clinical outcome.

## Relevance to this corpus

- This paper sharpens the corpus-wide platform question.
- It supports broad value for long reads, but its strongest claims are in hard medically relevant regions rather than in every part of the genome equally.

## Related concepts

- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)
- [HiFi vs ONT](../concepts/hifi-vs-ont.md)
- [Complex rearrangements and hard regions](../concepts/complex-rearrangements-and-hard-regions.md)

## Open questions

- At what coverage and cost point do long reads become justified for national-scale screening programs?
- How durable is the HiFi-over-ONT advantage as ONT chemistry and duplex workflows improve?
