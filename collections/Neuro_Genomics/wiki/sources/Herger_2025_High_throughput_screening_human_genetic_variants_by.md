---
title: "High-throughput screening of human genetic variants by pooled prime editing."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.xgen.2025.100814
pmid: 40120586
authors: Herger M et al.
journal: Cell genomics (2025)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# High-throughput screening of human genetic variants by pooled prime editing.

## Source

- Authors: Herger M, Kajba CM, Buckley M, Cunha A, Strom M, Findlay GM
- Journal: Cell Genomics 5, 100814 (April 9, 2025); Open Access (CC-BY)
- DOI: [10.1016/j.xgen.2025.100814](https://doi.org/10.1016/j.xgen.2025.100814)
- PMID: [40120586](https://pubmed.ncbi.nlm.nih.gov/40120586/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- The Genome Function Laboratory, The Francis Crick Institute (lead contact: Gregory M. Findlay — also senior author on the foundational BRCA1 saturation genome editing / SGE work). Herger & Kajba contributed equally.

## Abstract

Multiplexed assays of variant effect (MAVEs) enable scalable functional assessment of human genetic variants. However, established MAVEs are limited by exogenous expression of variants or constraints of genome editing. Here, we introduce a pooled prime editing (PE) platform to scalably assay variants in their endogenous context. We first improve efficiency of PE in HAP1 cells, defining optimal prime editing guide RNA (pegRNA) designs and establishing enrichment of edited cells via co-selection. We next demonstrate negative selection screening by testing over 7,500 pegRNAs targeting SMARCB1 and observing depletion of efficiently installed loss-of-function (LoF) variants. We then screen for LoF variants in MLH1 via 6-thioguanine selection, testing 65.3% of all possible SNVs in a 200-bp region including exon 10 and 362 non-coding variants from ClinVar spanning a 60-kb region. The platform's overall accuracy for discriminating pathogenic variants indicates that it will be highly valuable for identifying new variants underlying diverse human phenotypes across large genomic regions.

## Key findings

A **pooled, lentiviral prime-editing (PE) platform** that installs and assays human variants **in their endogenous genomic context** in near-haploid HAP1 cells, scoring variants from **pegRNA frequency changes over time** (like a CRISPR dropout/enrichment screen) rather than requiring direct sequencing of each edited locus. Key innovation: each pegRNA is co-delivered with a **surrogate target (ST)** that records that pegRNA's editing efficiency, so inactive pegRNAs can be filtered out — the main determinant of data quality.

- **Scale**: thousands of pegRNAs per experiment. SMARCB1 essentiality library = **10,954 pegRNAs** (1,194 SNVs, 55 nonsense MNVs, 55 codon deletions; up to 9 pegRNAs/variant; abstract cites ">7,500 pegRNAs"). MLH1 exon 10 = 2,696 pegRNAs / 598 variants (96% of possible SNVs in a 200-bp window). MLH1 non-coding = **3,748 pegRNAs covering 874 ClinVar variants across ~60 kb** (771 SNVs, 69 dels, 25 insertions, 9 MNVs). Up to 9–12 pegRNA designs per variant, diverse spacers/3′ extensions, designed with **PEGG**.
- **PE-efficiency optimizations** (vs original setup):
  - Stable monoclonal **HAP1:PEmax** line (lentiviral); second line co-expresses **dominant-negative MLH1 (MLH1dn)** to suppress mismatch repair and boost PE. epegRNAs capped with **tevopreQ1** motif.
  - **Stabilized pegRNA scaffolds**: F+E scaffold gave **2.4× higher median editing** than the original scaffold (87% of pegRNAs equal/better); F+E v1 (G-C variant) similar (median 2.1% correct ST editing). Original scaffold median was only **0.6%**.
  - **PAM-disruptive synonymous edits** install **2.1× (SNV) / 1.6× (MNV)** more efficiently. **SNVs install ~61% more efficiently than MNVs** overall → screened SNVs as single substitutions.
  - **Edits accumulate over time** under constitutive PE expression: median ST editing rose from **4.1% (day 4) → 34% (day 34)** without selection.
  - **Co-selection** via ouabain resistance (PE installs ATP1A1-T804N in a HAP1-essential gene): raises median ST editing to **45% by day 34**; ATP1A1 editing went 10.4% → 34.6% (no ouabain, +7 d) → 84.4% correct alleles after ouabain. Benefit consistent but modest.
- **Editing is highly variable / bimodal across pegRNAs** — e.g., with co-selection by day 34, 33.0% of pegRNAs >75% ST editing while 30.6% <10%. This variability is why ST-based filtering is essential.
- **ST is a usable proxy for endogenous editing**: ST vs endogenous-target (ET) variant-frequency correlation r = 0.53 (all variants), 0.69 (MNVs/dels). In ouabain day-10 sample, 79% of intended variants detected above background in ET sequencing.
- **Negative selection (SMARCB1, essential gene)**: LoF variants deplete. Separation of nonsense vs synonymous pegRNAs requires stringent ST filtering — no separation at ≤10% threshold; at **75% ST-editing threshold**, mean nonsense pegRNA score = −3.70. Among 164 variants scored at this filter, **12 significantly depleted (FDR 0.05)**: 3 nonsense, 2 canonical-splice, plus LoF missense clustered in a conserved CTD α-helix, and intronic VUS **c.1119+12C>G** (SpliceAI 0.96; validated to create a novel splice junction with 11-bp intron retention).
- **Positive selection (MLH1, via 6-thioguanine)**: MMR-LoF → 6TG resistance. Across 4 conditions (±MLH1dn, ±ouabain), AUC for distinguishing putative-LoF (nonsense/canonical-splice) from putative-neutral (synonymous) reached **1.00 in 3 of 4 screens** at stringent ST thresholds (e.g., AUC=1.00 at 22% ST threshold in HAP1:PEmax+ouabain, retaining ~20% of pegRNAs). Final scores for **401/598 exon-10 variants** (≥2 conditions). Correlation to CADD r=0.50 (→0.64 at >36% ST editing); ET-enrichment correlation 0.69 (→0.77 at >36% ST). 57% of P/LP variants scored >2.0; **no B/LB variant scored >2.0**. 7.5% of exon-10 VUS scored LoF.
- **Non-coding screen (MLH1, ~60 kb)**: scored 362/874 variants. ClinVar-pathogenic median function score **4.87 (SD 2.90)** vs benign **0.22 (1.45)**; **AUC 0.89** (pathogenic vs benign); called 54% of pathogenic and only 2.4% of benign as LoF (q<0.01). LoF found at canonical splice sites, splice region (3–8 bp), deep intronic, 5′-UTR, and upstream of TSS. Examples validated: deep-intronic **c.1732−264A>T** (likely-pathogenic, function score 4.96), upstream-of-exon-11 VUS **c.885−3C>G** (SpliceAI 0.73; scores like known pathogenics; remains VUS — functional data potentially clinically useful), start-loss **c.7_1del**. Splice-region **c.884+3A>G** confirmed LoF (since reclassified likely-pathogenic in ClinVar).
- **Validation rigor**: hits re-tested in minipools and individually, in newly-built **HAP1:PE7+MLH1-KO** and **K562:PE7** lines; minipool↔large-screen function-score correlation Pearson r=0.91; individual↔minipool r up to 0.97–0.99. Both retested 3′-UTR variants in SMARCB1 were **false positives**; a near-TSS variant (c.−219G>T) flagged as a likely false positive (possible CRISPRi artifact). Confirms both false positives and false negatives occur.

## Methods

- **Cells**: near-haploid **HAP1** (recessive variant effects assayable in one allele). Engineered lines: HAP1:PEmax-2A-BSD; HAP1:PEmax-2A-MLH1dn-2A-BSD; later HAP1:PE7+MLH1-KO; validation also in K562:PE7. PE components expressed from minimal EF-1α promoter, blasticidin-selected.
- **Vector**: dual-pegRNA lentiviral construct encoding (1) the **library pegRNA** for the assayed variant + its matched **55-nt surrogate target (ST)** + 16-nt pegRNA barcode, and (2) the **co-selection pegRNA** (ATP1A1-T804N → ouabain resistance). Stabilized **F+E scaffold**; tevopreQ1 3′ cap. Oligos capped at 243 nt (Twist).
- **Workflow**: lentiviral delivery (MOI <0.5) → puromycin selection → optional ouabain co-selection → prolonged culture for edit accumulation → functional selection (essentiality dropout for SMARCB1; 6TG for MLH1) → deep-sequence **pegRNA-ST cassettes** (and endogenous loci for validation) at multiple timepoints (days 4–34).
- **Scoring**: pegRNA score = log2(late-timepoint freq / early-timepoint freq); **function score = mean of pegRNA scores for the same variant, restricted to pegRNAs above an ST-editing threshold**. AUC analysis sweeps ST thresholds (synonymous = putative-neutral; nonsense + canonical-splice = putative-LoF). LoF called via empirical null from synonymous variants (FDR 0.01–0.05). Incorrect/recombined pegRNA-ST cassettes discarded.
- **pegRNA features predictive of editing** (consistent across libraries): RT-template homology length (strongest, R≈0.43), PBS length, PBS GC content; total RTT length and nick-to-edit distance negatively correlated; modest correlation with CRISPick and (retrospective) **PRIDICT** scores.
- **Software / data**: design with **PEGG**; edit quantification with **CRISPResso2**; analysis with **DiMSum** + custom scripts (github.com/FrancisCrickInstitute/PooledPEScreen, Zenodo 10.5281/zenodo.14843845). Raw NGS at **ENA: PRJEB85691**. Plasmids on Addgene (234070–234073).

## Relevance to the brain-organoid ASD review

This is the **pooled prime-editing variant-installation method the manuscript cites as the scalable way to install variants in their endogenous context** — i.e., it underpins the **Build** stage of a DBTL loop for an organoid-based ASD-variant program, complementing the **Test** stage covered by reporter/DMS approaches such as [Hemker 2025](Hemker_2025_Saturation_mapping_MUTYH_variant_effects_DNA_repair.md).

Why it matters for the review's argument:
- **Endogenous-context editing** preserves native expression and, crucially, lets a single platform detect **coding, splicing, and non-coding regulatory effects** — the non-coding MLH1 screen across ~60 kb is a direct demonstration. ASD risk is substantially non-coding/regulatory, so an organoid program needs exactly this capability, which exogenous-cDNA reporters (Hemker) cannot provide.
- **"Install virtually any short variant anywhere in the genome"** via pegRNA: unlike base editing (limited substitution types, bystander edits) or SGE/HDR (low HDR rates, one ~100–200 bp region per experiment, many separate libraries needed), PE is not confined to a single locus per experiment — enabling multi-gene / large-region ASD-variant libraries.
- **Pooled, lentiviral, time-course readout** is compatible with the kind of selection or phenotypic enrichment one would design in organoids; the **surrogate-target QC** concept (filter on actual editing efficiency) is a generalizable design principle for any pooled editing screen, including in 3D/organoid contexts where editing efficiency is heterogeneous.
- Establishes a **path to screening >2,000 HAP1-essential genes by negative selection** and to prioritizing clinically-observed variants for deeper study — the scalable front-end the review would feed into organoid phenotyping.

**Important contrast for the review**: this is a 2D haploid-cell, proof-of-concept platform with notable false-negative rates, *not* an organoid assay. The review's contribution is presumably to port this endogenous-editing + functional-selection logic into brain organoids with neurodevelopment-relevant phenotypes (where HAP1 growth/drug selections do not apply). The two ingested method papers thus map onto Build (Herger, endogenous PE installation) and Test (Hemker, direct functional reporter readout) of the variant-effect-mapping toolkit the review builds on.

## Open questions / limitations

- **Only a limited fraction of pegRNAs edit robustly** (bimodal efficiency), so many designed variants go unscored; signal-from-noise depends heavily on ST-based filtering, which trades **coverage for accuracy** (stringent thresholds drop most pegRNAs).
- **Higher false-negative rates** than mature MAVEs (e.g., SGE), and **false positives occur** (3′-UTR SMARCB1 variants; near-TSS c.−219G>T possibly via CRISPRi-like artifact) → rigorous orthogonal validation (ET sequencing, independent pegRNAs, multiple cell lines) is required before clinical use.
- **MLH1dn expression can perturb the effect of some MLH1 variants** (e.g., c.866A>G, c.871T>A enriched only with MLH1dn) — a confounder specific to assaying MMR-pathway genes; for non-MMR genes MLH1dn/MLH1-KO should boost editing without confounding.
- Many variants had **mildly positive scores that failed FDR (q<0.01)** — unresolved whether these are true hypomorphs or just low-editing artifacts; score precision could improve by weighting pegRNA selection strength + ST editing and testing multiple highly-active pegRNAs per variant.
- Libraries here are **modestly sized proof-of-concept**; genome-wide scale is anticipated but not yet shown by these authors. Demonstrated phenotypes rely on **HAP1 essentiality and 6TG (drug) selection** — additional functional assays are needed to reach more genomic regions (and, by extension, neurodevelopmental phenotypes).
- Clinical use will require **rigorous benchmarking/calibration** (ClinVar, OddsPath-style) not yet performed at scale here.
