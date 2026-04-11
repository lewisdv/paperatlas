---
title: Long read sequencing enhances pathogenic and novel variation discovery in patients with rare diseases
kind: paper
status: ingested
added: 2026-04-07T09:46:12+09:00
raw_source: raw/sources/sinha_2025_long_read_sequencing_enhances_pathogenic.pdf
deep_ingested: 2026-04-07
---

# Long read sequencing enhances pathogenic and novel variation discovery in patients with rare diseases

## Source

- PDF: [raw/sources/sinha_2025_long_read_sequencing_enhances_pathogenic.pdf](../../raw/sources/sinha_2025_long_read_sequencing_enhances_pathogenic.pdf)
- Status: deep ingested on 2026-04-07
- Scope: clinical long-read WGS workflow that unifies small variants, structural variants, phasing, and methylation in rare disease diagnostics

## Study design

- Samples: positive-control set of 76 cases, independent methylation-validation set of 57, and 51 previously short-read-negative rare disease patients
- Platform: Oxford Nanopore whole-genome sequencing with an in-house funnel-down filtering and methylation-aware analysis pipeline
- Aim: test whether one long-read workflow can recover pathogenic genomic and epigenomic variation and improve diagnosis in unsolved rare disease cases

## Summary

- This paper argues most directly for long-read WGS as a unified clinical platform.
- The study reports detection of all known pathogenic SNV, SV, and methylation variants in its positive controls, then shows additional diagnoses in 10% of previously negative cases.
- It is especially important because it combines variant detection, phasing, copy number analysis, and methylation-aware interpretation in one workflow.

## Key findings

- The funnel-down workflow detected all pathogenic single-nucleotide, structural, and methylation variants in the positive-control cohorts used for validation.
- In the 51 previously negative patients, the approach produced additional diagnoses in 10% of cases.
- The paper includes examples where long reads clarify compound heterozygosity, identify pathogenic deletions, and use methylation at the SMA locus as a diagnostic signal.
- Large raw callsets were reduced aggressively by filtering, showing that the bottleneck is not only generation of calls but clinically meaningful prioritization.

## Strengths

- One of the strongest clinical workflow papers in the corpus.
- Native methylation and phasing are treated as first-class diagnostic features rather than side benefits.
- Uses orthogonal validation and concrete solved-case examples, not only benchmark metrics.

## Limitations and caveats

- The unsolved cohort is still moderate in size, so the 10% uplift should be treated as promising rather than universal.
- Manual review and phenotype-aware filtering remain essential.
- Some candidate events still require functional follow-up, so long-read WGS does not eliminate downstream interpretation work.

## Relevance to this corpus

- This paper is the strongest counterpoint to a narrowly targeted-use view of long-read WGS.
- Together with Kobayashi, it defines an important tension in the corpus: targeted deployment versus broader unified-platform deployment.

## Related concepts

- [Rare disease diagnostics](../concepts/rare-disease-diagnostics.md)
- [HiFi vs ONT](../concepts/hifi-vs-ont.md)
- [Long-read vs short-read WGS](../concepts/long-read-vs-short-read-wgs.md)

## Open questions

- Which parts of this workflow are robust enough for routine accredited clinical labs today?
- How much of the reported uplift comes from methylation, phasing, or SV detection separately?
