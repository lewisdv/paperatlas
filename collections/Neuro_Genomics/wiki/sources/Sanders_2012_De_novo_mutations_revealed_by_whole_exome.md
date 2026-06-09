---
title: "De novo mutations revealed by whole-exome sequencing are strongly associated with autism"
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/nature10945
pmid: 22495306
authors: Sanders SJ et al.
journal: Nature (2012)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Sanders_2012_De_novo_mutations_revealed_by_whole_exome.pdf
pdf_status: downloaded
---

# De novo mutations revealed by whole-exome sequencing are strongly associated with autism

## Source

- Authors: Sanders SJ, Murtha MT, Gupta AR, Murdoch JD, Raubeson MJ, Willsey AJ, Ercan-Sencicek AG, DiLullo NM (… Roeder K, Geschwind DH, Devlin B, State MW)
- Journal: Nature (2012), vol. 485, 237–241
- DOI: [10.1038/nature10945](https://doi.org/10.1038/nature10945)
- PMID: [22495306](https://pubmed.ncbi.nlm.nih.gov/22495306/)
- Added via: manuscript_brain_organoid_v6 reference ingest (foundational gap-fill)

## Abstract

Multiple studies have confirmed the contribution of rare de novo copy number variations to the risk for autism spectrum disorders. But whereas de novo single nucleotide variants have been identified in affected individuals, their contribution to risk has yet to be clarified. Specifically, the frequency and distribution of these mutations have not been well characterized in matched unaffected controls, and such data are vital to the interpretation of de novo coding mutations observed in probands. Here we show, using whole-exome sequencing of 928 individuals, including 200 phenotypically discordant sibling pairs, that highly disruptive (nonsense and splice-site) de novo mutations in brain-expressed genes are associated with autism spectrum disorders and carry large effects. On the basis of mutation rates in unaffected individuals, we demonstrate that multiple independent de novo single nucleotide variants in the same gene among unrelated probands reliably identifies risk alleles, providing a clear path forward for gene discovery. Among a total of 279 identified de novo coding mutations, there is a single instance in probands, and none in siblings, in which two independent nonsense variants disrupt the same gene, SCN2A (sodium channel, voltage-gated, type II, α subunit), a result that is highly unlikely by chance.

## Key findings

- **Cohort:** whole-exome sequencing of 928 individuals from the **Simons Simplex Collection (SSC)** — 238 families selected, 225 passing QC (200 quartets = parents + proband + unaffected sibling, plus 25 trios). 96% of predicted de novo SNVs Sanger-validated.
- **De novo burden in probands vs sibling controls (the discordant-sib design):** non-synonymous de novo SNVs significantly higher in probands than siblings (125 vs 87; `P = 0.01`, two-tailed binomial; OR of non-synonymous:silent 1.93, 95% CI 1.11–3.36).
- **Highly disruptive (nonsense + splice-site) de novo in brain-expressed genes carry the largest effect:** burden 13 (probands) vs 3 (siblings), `P = 0.02`; OR of nonsense/splice:silent = **5.65** (95% CI 1.44–22.2, `P = 0.01`). This class is where the ASD signal concentrates.
- **Liability estimate:** assuming sibling de novo events confer no liability, **at least ~14% of affected SSC individuals** carry a de novo SNV risk event. Among probands (brain-expressed genes), an estimated **41%** of non-synonymous de novo SNVs and **77%** of nonsense/splice-site de novo SNVs point to bona fide ASD-risk loci.
- **Core statistical argument (the foundational result):** by modeling per-base mutation rates, gene size and GC content across 150,000 simulations under varying locus heterogeneity (100/333/667/1,000 risk genes), **observing ≥2 independent nonsense/splice-site de novo mutations in the same brain-expressed gene is highly unlikely by chance and reliably flags a risk gene** — `P = 0.008`, `Q (FDR) = 0.005`, robust to sample size and heterogeneity. For milder non-synonymous variants, ≥3 (often ≥4) recurrences are needed and the threshold is sensitive to assumptions.
- **SCN2A is the first gene to meet the bar:** of 279 de novo coding mutations, the only gene with two independent de novo nonsense variants in unrelated probands (none in siblings) was **SCN2A** (`P = 0.008`); neither carrier had a seizure history.
- **Two further genes after merging with a parallel SSC trio study:** combining with non-overlapping SSC families (414 probands total) added **KATNAL2** and **CHD8**, each with two highly disruptive de novo mutations — yielding significant association for three genes: **SCN2A, KATNAL2, CHD8.**
- **Negative results that shaped the field:** the distribution of multiple de novo events *within a single individual* matched Poisson and did not differ between cases and controls → **no support for a "two de novo hit" (within-individual) hypothesis.** De novo SNVs were not over-represented in prior synaptic / chrX / known-ASD / ID gene lists, and pathway/PPI enrichment did not survive multiple-testing correction (limited power).
- **Locus heterogeneity / target estimate:** point estimate of **~1,034 ASD-risk genes** (wide CIs; distribution of risk unknown), with a prediction that **~25–50 additional risk genes** would be found upon completing the 2,648-family SSC. Effect sizes for nonsense/splice de novo are in the range previously seen for large multigenic de novo CNVs.
- **Covariates:** de novo SNV rate rises with paternal age (`P = 0.008`), but adjusting for age did not change the significant results; no significant association with proband IQ or sex.

## Methods

- Family-based **whole-exome sequencing** (NimbleGen capture, Illumina), genotypes called at targeted bases; de novo calling restricted to bases with ≥20 reads in all family members (covering ~83% of targeted bases, ~73% of exons/splice sites in RefSeq hg18). Indels excluded from case-control comparisons due to detection-sensitivity uncertainty.
- **Phenotypically discordant sibling-pair (quartet) design** to obtain matched unaffected controls and quantify the de novo background rate — the key methodological advance vs prior proband-only studies.
- All predicted de novo SNVs validated by Sanger sequencing with readers blinded to affected status; silent / non-coding / novel-transmitted variants used to confirm no detection bias between probands and siblings.
- **Simulation framework** (per-base mutation rate × gene size × GC content; 150,000 iterations across locus-heterogeneity models) to derive the P/Q thresholds for recurrent de novo events — the statistical engine later generalized into TADA.
- Brain-expressed gene list from expression arrays across post-mortem brains; pathway and protein-protein-interaction analyses run but underpowered.

## Relevance to the brain-organoid ASD review

- **Foundational de novo / multiple-hit paper** that established, with matched controls, that highly disruptive de novo LoF variants in brain-expressed genes carry large ASD effect sizes — the conceptual seed for all later large exome studies (Iossifov 2014, De Rubeis 2014, Satterstrom 2020, Fu 2022).
- **Provides the original statistical logic** — "≥2 independent de novo LoF in the same gene reliably identifies a risk gene" (`P = 0.008`, `Q = 0.005`) — that matured into the TADA framework Fu 2022 uses to call the 185/72-gene lists.
- **SCN2A as the prototype gene-first target:** the first high-confidence ASD gene identified this way; canonical example of a high-penetrance, individually modelable gene for organoid functional studies, alongside CHD8.
- Quantifies the **heterogeneity scale (hundreds–~1,000 genes)** that a programmable, many-gene organoid platform is designed to address, and the early effect-size benchmarks against which functional assays can be calibrated.

## Open questions / limitations

- **Small cohort (200 quartets + 25 trios):** powered to find only the strongest recurrent genes; the ~1,034-gene estimate has very wide confidence intervals and the distribution of risk across genes is unknown.
- Effect-size estimates **mix true risk and neutral de novo events** in probands; per-gene/per-class effects were expected to refine with larger samples (and did).
- **Indels and CNVs** largely excluded from the SNV case-control analysis; de novo indel contribution under-characterized here.
- No significant **pathway/PPI convergence** detected — but explicitly attributed to limited power, not absence of convergence (later studies did find synaptic/chromatin convergence).
- Detection limited to bases with ≥20 reads in all family members; some exons/splice sites (~27% of exons) not assessable for de novo events.
