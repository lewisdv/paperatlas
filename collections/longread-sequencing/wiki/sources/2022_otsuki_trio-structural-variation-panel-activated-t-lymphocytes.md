---
title: Construction of a trio-based structural variation panel utilizing activated T lymphocytes and long-read sequencing technology
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/otsuki_2022_construction_of_a_trio-based_structural.pdf
deep_ingested: 2026-04-07
---

# Construction of a trio-based structural variation panel utilizing activated T lymphocytes and long-read sequencing technology

## Source

- PDF: [raw/sources/otsuki_2022_construction_of_a_trio-based_structural.pdf](../../raw/sources/otsuki_2022_construction_of_a_trio-based_structural.pdf)
- Status: deep ingested on 2026-04-07
- Scope: Japanese population-scale SV panel built from trio-aware nanopore sequencing and activated T-cell DNA

## Study design

- Samples: 333 individuals forming 111 trios
- Platform: Oxford Nanopore long-read sequencing with mean depth around 22.2x and N50 around 25.8 kb
- Aim: show that activated T lymphocytes can support scalable high-molecular-weight DNA prep and produce a validated population SV reference panel

## Summary

- The paper is as much about sample logistics as it is about variant discovery.
- It argues that long-read population studies need a reliable source of high-quality DNA and proposes activated T lymphocytes as a practical biobank resource.
- Using this setup, the study identifies 74,201 SVs and shows that more than 95% are concordant with Mendelian inheritance, producing a Japanese SV frequency panel.

## Key findings

- The study builds a population SV panel with trio-based inheritance checks rather than relying only on caller-internal quality scores.
- Mean per-person discovery includes large numbers of deletions and insertions, supporting the claim that long-read WGS reveals substantially more SVs than short-read WGS.
- Clinically relevant examples are highlighted for loci including hemoglobin genes, skin barrier genes, CYP2A6, and ATXN3.
- The resulting panel is released through jMorp as JSV1, making it a usable downstream filtering resource rather than a closed paper-only dataset.

## Strengths

- Trio design provides unusually strong quality control for a population SV panel.
- The paper addresses a real bottleneck in long-read population studies: DNA input quality at biobank scale.
- It shows how long-read resources can become practical reference infrastructure, not just one-off discovery studies.

## Limitations and caveats

- The panel is ancestry-specific, so transferability outside Japanese cohorts is incomplete.
- The study centers on SV discovery and allele frequencies, not full-spectrum clinical interpretation across all variant classes.
- Activated T-cell workflows are operationally useful but may not be equally available across all biobanks.

## Relevance to this corpus

- This paper links long-read SV discovery to reference-panel building, which is crucial for rare disease filtering and population genetics.
- It pairs naturally with the Han Chinese and 1,019-diverse-human studies as part of the corpus's population-atlas theme.

## Related concepts

- [Structural variation](../concepts/structural-variation.md)
- [Population-scale SV atlases](../concepts/population-scale-sv-atlases.md)
- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)

## Open questions

- How much depth is really required to build clinically useful SV frequency panels in new cohorts?
- Can the activated T-cell DNA strategy be generalized across biobanks without introducing systematic biases?
