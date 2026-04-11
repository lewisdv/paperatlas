---
title: Long Read WGS Starter Corpus
status: active
created: 2026-04-07T09:48:00+09:00
---

# Long Read WGS Starter Corpus

## Scope

This corpus contains 10 deeply ingested papers on long-read whole-genome sequencing across human structural variation, clinical diagnostics, large-cohort benchmarking, rare disease resolution, and population-scale studies.

## Coverage Map

### Foundational SV and benchmarking

- [Multi-platform discovery of haplotype-resolved structural variation in human genomes](../sources/2019_chaisson_multi-platform-haplotype-resolved-structural-variation-human-genomes.md)
- [Approaches to long-read sequencing in a clinical setting to improve diagnostic rate](../sources/2022_sanford-kobayashi_clinical-long-read-diagnostic-rate.md)
- [Utility of long-read sequencing for All of Us](../sources/2024_mahmoud_utility-long-read-sequencing-all-of-us.md)
- [Comparative evaluation of SNVs, indels, and structural variations detected with short- and long-read sequencing data](../sources/2024_kosugi_comparative-evaluation-short-vs-long-read-variants.md)

### Population-scale SV resources

- [Construction of a trio-based structural variation panel utilizing activated T lymphocytes and long-read sequencing technology](../sources/2022_otsuki_trio-structural-variation-panel-activated-t-lymphocytes.md)
- [Long-read sequencing of 945 Han individuals identifies structural variants associated with phenotypic diversity and disease susceptibility](../sources/2025_gong_long-read-sequencing-945-han-individuals.md)
- [Structural variation in 1,019 diverse humans based on long-read sequencing](../sources/2025_schloissnig_structural-variation-1019-diverse-humans-long-read-sequencing.md)

### Clinical and rare disease resolution

- [Long-read genome sequencing resolves complex genomic rearrangements in rare genetic syndromes](../sources/2024_showpnil_long-read-genome-sequencing-complex-rearrangements-rare-syndromes.md)
- [Long read sequencing enhances pathogenic and novel variation discovery in patients with rare diseases](../sources/2025_sinha_long-read-sequencing-rare-diseases.md)

### Frontier application

- [Long-read whole-genome analysis of human single cells](../sources/2023_hard_long-read-whole-genome-analysis-human-single-cells.md)

## Reading Order

1. Chaisson 2019
2. Sanford Kobayashi 2022
3. Mahmoud 2024
4. Kosugi 2024
5. Showpnil 2024
6. Sinha 2025
7. Otsuki 2022
8. Gong 2025
9. Schloissnig 2025
10. Hard 2023

This order still works well for reading because it builds core concepts first, then clinical utility, then larger cohort studies, and finally the more specialized single-cell application.

## Cross-paper Claims

- Long-read WGS has its strongest and most stable advantage in structural variation, especially insertions, repeat-associated events, and rearrangement interpretation.
- The clinical case for long reads is strongest in rare disease when dead zones, hard genes, phasing, methylation, or complex SVs are plausible mechanisms.
- Population-scale long-read SV resources are now useful for filtering patient genomes, not only for discovery papers.
- HiFi currently has the strongest overall accuracy signal in this corpus, while ONT has strong representation for methylation-aware and scalable workflows.
- Short-read WGS remains competitive for many SNVs and some deletions outside repetitive regions, so long-read universal first-line use is still an open decision rather than a settled conclusion.

## Main Tensions

- targeted long-read escalation versus one unified long-read clinical workflow
- benchmark-style maximal sensitivity versus scalable intermediate-coverage cohorts
- HiFi accuracy advantages versus ONT workflow flexibility and native methylation support

## Concept Entry Points

- [Structural variation](../concepts/structural-variation.md)
- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)
- [HiFi vs ONT](../concepts/hifi-vs-ont.md)
- [Rare disease diagnostics](../concepts/rare-disease-diagnostics.md)
- [Population-scale SV atlases](../concepts/population-scale-sv-atlases.md)
- [Complex rearrangements and hard regions](../concepts/complex-rearrangements-and-hard-regions.md)

## Questions To Drive Next Work

- Which variant classes benefit most from long-read WGS over short-read WGS?
- Where do HiFi and ONT differ in accuracy, coverage, and clinical utility?
- What evidence already exists for diagnostic uplift in rare disease cohorts?
- How much incremental value comes from long-read data in medically relevant or hard-to-map regions?
- What population-scale SV resources now exist, and how transferable are they across ancestries?
