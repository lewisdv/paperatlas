# Long-read vs Short-read WGS

## Current position in this corpus

Long-read WGS is not uniformly better for every task, but it is consistently better where read length, phasing, or native-molecule information matters.

## Where long reads clearly help

- insertions larger than roughly 10 bp
- structural variants in repetitive regions
- hard medically relevant genes and sequencing dead zones
- breakpoint-level interpretation of complex rearrangements
- phasing of compound events
- native methylation-aware diagnostics

## Where short reads remain competitive

- many SNVs outside repetitive regions
- many deletions in nonrepetitive regions
- cost-efficient high-throughput cohort sequencing
- mature tooling and established clinical workflows

## Supporting sources

- [Chaisson 2019](../sources/2019_chaisson_multi-platform-haplotype-resolved-structural-variation-human-genomes.md)
- [Kosugi 2024](../sources/2024_kosugi_comparative-evaluation-short-vs-long-read-variants.md)
- [Mahmoud 2024](../sources/2024_mahmoud_utility-long-read-sequencing-all-of-us.md)
- [Kobayashi 2022](../sources/2022_sanford-kobayashi_clinical-long-read-diagnostic-rate.md)
- [Sinha 2025](../sources/2025_sinha_long-read-sequencing-rare-diseases.md)

## Main tension

- One view in the corpus favors targeted deployment where long reads have the highest incremental value.
- Another view favors a unified long-read clinical platform that replaces multiple follow-up assays.

## Open questions

- At what cost and coverage point does long-read WGS become the default rather than the escalation path?
- How much of the remaining short-read advantage is technical, and how much is simply ecosystem maturity?
