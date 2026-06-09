---
title: "Saturation genome editing-based clinical classification of BRCA2 variants."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/s41586-024-08349-1
pmid: 39779848
authors: Sahu S et al.
journal: Nature (2025)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Neuro_Genomics/raw/sources/Sahu_2025_Saturation_genome_editing_based_clinical_classification_BRCA2.pdf
pdf_status: downloaded
---

# Saturation genome editing-based clinical classification of BRCA2 variants.

## Source

- Authors: Sahu S, Galloux M, Southon E, Caylor D, Sullivan T, Arnaudi M, Zanti M, Geh J et al. (corresponding: Shyam K. Sharan, NCI)
- Journal: Nature (2025); Vol 638, 13 February 2025, pp. 538–544
- DOI: [10.1038/s41586-024-08349-1](https://doi.org/10.1038/s41586-024-08349-1)
- PMID: [39779848](https://pubmed.ncbi.nlm.nih.gov/39779848/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Sequencing-based genetic tests have uncovered a vast array of BRCA2 sequence variants1. Owing to limited clinical, familial and epidemiological data, thousands of variants are considered to be variants of uncertain significance2-4 (VUS). Here we have utilized CRISPR-Cas9-based saturation genome editing in a humanized mouse embryonic stem cell line to determine the functional effect of VUS. We have categorized nearly all possible single nucleotide variants (SNVs) in the region that encodes the carboxylate-terminal DNA-binding domain of BRCA2. We have generated function scores for 6,551 SNVs, covering 96.4% of possible SNVs in exons 15-26 spanning BRCA2 residues 2479-3216. These variants include 1,282 SNVs that are categorized as missense VUS in the clinical variant database ClinVar, with 77.2% of these classified as benign and 20.4% classified as pathogenic using our functional score. Our assay provides evidence that 3,384 of the SNVs in the region are benign and 776 are pathogenic. Our classification aligns closely with pathogenicity data from ClinVar, orthogonal functional assays and computational meta predictors. We have integrated our embryonic stem cell-based BRCA2-saturation genome editing dataset with other available evidence and utilized the American College of Medical Genetics and Genomics/Association for Molecular Pathology guidelines for clinical classification of all possible SNVs. This classification is available as a sequence-function map and serves as a valuable resource for interpreting unidentified variants in the population and for physicians and genetic counsellors to assess BRCA2 VUS in patients.

## Key findings

- **Scope / coverage.** Function scores for **6,551 SNVs = 96.4% of the 6,796 possible SNVs** in BRCA2 exons 15–26, encoding the **C-terminal DNA-binding (CTDB) domain, residues 2479–3216** (helical + tower + OB1–3 folds). Only 3.6% of SNVs not recovered. Region chosen because pathogenic missense variants concentrate here.
- **Problem being attacked.** ClinVar held **13,201 BRCA2 SNVs, 59% still VUS** (30 Oct 2023). BRCA2 is a 3,418-aa protein; loss of function is lethal in mouse ES cells, so **cellular fitness is a clean loss-of-function readout**.
- **Function-score separation.** Bimodal distribution. Nonsense SNVs median score **−1.84 (n=327)**; synonymous SNVs median **above −0.03 (n=1,321)**. Likelihood-ratio categorization correctly called **89.1% of synonymous SNVs benign (1,177)** and **93.3% of nonsense SNVs pathogenic (305)**.
- **VUS resolution (functional layer).** Of **1,069 missense VUS** scored: **835 (78.1%) benign, 179 (16.7%) pathogenic**. Of 213 conflicting-interpretation missense SNVs: 156 (73.2%) benign, 47 (22.1%) pathogenic, 65 uncertain. Abstract-level totals across the region: **3,384 SNVs benign, 776 pathogenic**; of 1,282 missense ClinVar VUS, 77.2% benign / 20.4% pathogenic.
- **Accuracy vs ClinVar.** Pathogenic prediction **sensitivity 0.89 / specificity 0.93**; benign prediction sensitivity 0.93 / specificity 0.91. **ROC AUC = 0.96** for both (P/LP-vs-B/LB and nonsense-vs-synonymous). Outperformed computational predictors (their AUCs 0.6–0.93). Expert-curated check: 35/42 ClinVar P/LP called pathogenic; 41/46 ClinVar B/LB called benign.
- **7-tier functional categorization of 6,551 SNVs:** benign strong 4,724 (72.1%), benign moderate 115 (1.7%), benign supporting 31 (0.47%), pathogenic strong 1,206 (18.4%), pathogenic moderate 80 (1.2%), pathogenic supporting 42 (0.7%), uncertain 353 (5.4%).
- **Drug-response axis.** Function scores from cellular fitness (DMSO) correlate tightly with cisplatin (ρ=0.82) and olaparib (PARP-inhibitor) (ρ=0.84) dropout (cisplatin vs olaparib ρ=0.85). Integrating fitness + drug response, **6,209 SNVs (94.7%) concordant**; the **353 discordant (5.4%) flagged "uncertain"** and may be **hypomorphic** (survive but drug-sensitive; e.g. Tyr3035Ser, c.9104A>C).
- **Structural mechanism.** MAVISp (FoldX/Rosetta stability + SEM1/DSS1 interaction) concordant with SGE and AlphaMissense: **92 non-functional variants** explained by destabilization, **38** by disrupted BRCA2–SEM1 interaction. Helical-domain residues 2619–2630 and OB1 residues 2720–2726 intolerant; OB2/tower domain tolerant (no reported pathogenic variants).
- **Cancer-risk calibration (BRIDGES consortium).** 59,538 cases / 53,165 controls. Burden test: SGE-pathogenic missense **OR 2.56 (95% CI 1.94–3.38)** — moderate risk (OR<4), attenuated vs nonsense/protein-truncating **OR 6.65 (3.42–12.96)**; benign tier OR 0.89 (0.80–0.99, not elevated). Consistent with reduced-penetrance missense risk (e.g. Trp2626Cys OR ≈2.2).
- **Final ACMG/AMP clinical classification (integrated).** Of all SNVs: **437 pathogenic, 565 likely pathogenic, 732 VUS, 4,478 likely benign, 339 benign**. **1,190 of 1,358 SNVs (≈85–88%) previously VUS or conflicting were resolved**; only 732 (~11%) remain VUS. Delivered as an interactive **sequence-function map** at https://appshare.cancer.gov/BRCA2_SGE/.

## Methods

- **Platform:** CRISPR–Cas9 **saturation genome editing (SGE)** via homology-directed repair in a **humanized mouse ES cell line** carrying a single copy of human *BRCA2* on a *Brca2^−/−* background (*Brca2^−/−; Tg[BRCA2]*). Single copy ⇒ one variant per cell ⇒ effects on regulation, splicing and protein all captured.
- **Library:** 48 oligonucleotide pools (87–339 ssODNs each, **180-mer ssODN donors**) tiling 12 exons + 3–7 bp flanking intron. Each ssODN carries a **synonymous PAM-blocking variant** (HDR marker preventing re-cutting) plus degenerate positions giving **all three non-WT nucleotides** across a 30–80 bp saturation window.
- **Selection / readout:** transfect day 0; amplicon NGS at **day 3 (baseline) and day 14**, with arms ± **cisplatin** and ± **olaparib (PARP inhibitor)**. **Function score = log2(day-14 / day-3 frequency)** = relative dropout; positional editing biases corrected; scores normalized across pools/exons so median synonymous and median nonsense match global medians. Two independent replicates (strong day-3 read-count correlation justifies using initial frequency).
- **Statistics / calibration:** two-component **Gaussian mixture model** → probability of impact on function (PIF); missense prior 0.1; ACMG/AMP threshold tuned to odds of pathogenicity **18.7:1**. PIF → likelihood ratios → ACMG strong/moderate/supporting evidence tiers (calibrated against BRCA2 multifactorial human evidence: segregation, family history, case–control).
- **Clinical integration:** ClinGen ENIGMA BRCA1/BRCA2 VCEP point system. PVS1 (+8) for nonsense and ±1–2 nt from canonical splice sites; SGE entered as **PS3/BS3** (±4/±2/±1 for strong/moderate/supporting). Combined with in silico + case–control evidence → P (≥10), LP (6–9), VUS (−1 to 5; sub-binned VUS-high/mid/low), LB (−2 to −6), B (≤−7).
- **Editing efficiency (caveat context):** indel rates 2.7–48.7% of reads; HDR rates 0.3–20.7% across exons.

## Orthogonal validation

- HDR-based homologous-recombination classification of **440 germline missense variants** — strong concordance (tower-domain variants functional in both).
- **167** BAC-recombineering variants in the same ES line — **90.4% match**.
- **190** prime-editing SNVs — **171 (90%) concordant**.
- **144** MANO-B PARP-inhibitor/carboplatin variants — strong concordance.
- HAP1 cell-viability MAVE and VarSome ACMG (v12.1.1, >70 databases) — concordant.

## Relevance to the brain-organoid ASD review

- **Canonical SGE template the review extends to organoids.** This is the methodological exemplar: take a clinically important gene, generate **near-complete base-resolution variant-effect maps** in a relevant cellular model, calibrate to ACMG/AMP, and collapse the VUS backlog. The review proposes the same loop for ASD risk genes but in **brain-organoid** cellular contexts rather than ES-cell fitness.
- **Demonstrates the "proactive" interpretation paradigm** central to the review's thesis — assay *every possible* variant *before* it is seen in a patient, so a future VUS is already classified. Concrete payoff shown here: ~85–88% of standing VUS/conflicting BRCA2 variants resolved; ~11% residual.
- **Multi-readout design as a model for organoid endophenotypes.** Combining a generic fitness readout with a pathway-specific stressor (DNA-damaging drugs) both sharpens classification and surfaces **hypomorphs** — directly analogous to pairing organoid growth/survival with neurodevelopmental readouts (progenitor proliferation, morphology, activity) to capture partial-loss ASD alleles.
- **Sets the calibration / evidence-integration bar** (GMM → odds of pathogenicity 18.7:1 → ACMG PS3/BS3) that any organoid-based variant-effect map must meet to be clinically actionable.
- Methodological sibling to [Findlay 2018 BRCA1 SGE](Findlay_2018_Accurate_classification_BRCA1_variants_saturation_genome_editing.md) (whose calibration this paper reuses) and to the domain-scale approach of [Beltran 2025](Beltran_2025_Site_saturation_mutagenesis_500_human_protein_domains.md); contrasts with the locus-level dosage genetics of [Brunetti-Pierri 2008](BrunettiPierri_2008_Recurrent_reciprocal_1q21_1_deletions_duplications_associated.md).

## Open questions / limitations

- **Only two replicates** — authors explicitly caution on clinical use; discordant variants may reflect technical variation. More replicates / orthogonal assays needed.
- **Single domain (CTDB only).** Exons 15–26 / residues 2479–3216; the rest of BRCA2 (PALB2-binding N-terminus, 8 BRC repeats, CRB) is not mapped. **Residues 3012–3026 (exon 23) excluded** for lack of efficient sgRNAs.
- **Off-target / reproducible-artifact risk** inherent to CRISPR SGE; mitigated only by cross-assay comparison.
- **Hypomorph ambiguity.** 353 "uncertain" (5.4%) genuinely intermediate; clinical meaning of potential hypomorphs (e.g. Tyr3035Ser) and their value as treatment markers unresolved.
- **Model-system caveats:** mouse ES-cell fitness as a proxy for human breast/ovarian cancer risk; missense ORs (~2.5) come with wide CIs — per-variant risk needs larger case–control data.
- **Splicing nuance:** a few synonymous variants act non-functional (e.g. Pro3039 c.9117G>A, exon-23 skipping) and some nonsense alleles remain functional (readthrough / alt-splicing), so DNA-level prediction alone is insufficient.

## Related pages

- [Findlay 2018 — Accurate classification of BRCA1 variants with saturation genome editing](Findlay_2018_Accurate_classification_BRCA1_variants_saturation_genome_editing.md)
- [Beltran 2025 — Site-saturation mutagenesis of 500 human protein domains](Beltran_2025_Site_saturation_mutagenesis_500_human_protein_domains.md)
- [Brnich 2019 — Recommendations for application of the functional evidence PS3/BS3 criterion](Brnich_2019_Recommendations_application_functional_evidence_PS3_BS3_criterion.md)
- [Cheng 2023 — Accurate proteome-wide missense variant effect prediction with AlphaMissense](Cheng_2023_Accurate_proteome_wide_missense_variant_effect_prediction.md)
- [Brunetti-Pierri 2008 — Recurrent reciprocal 1q21.1 deletions and duplications](BrunettiPierri_2008_Recurrent_reciprocal_1q21_1_deletions_duplications_associated.md)
