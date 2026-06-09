---
title: "Saturation mapping of MUTYH variant effects using DNA repair reporters."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1101/2025.03.01.640912
pmid: 40093110
authors: Hemker SL et al.
journal: bioRxiv : the preprint server for biology (2025)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Saturation mapping of MUTYH variant effects using DNA repair reporters.

## Source

- Authors: Hemker SL, Marsh A, Hernandez F, Glick E, Clark G, Bashir A, Jiang K, Kitzman JO
- Journal: bioRxiv : the preprint server for biology (2025)
- DOI: [10.1101/2025.03.01.640912](https://doi.org/10.1101/2025.03.01.640912)
- PMID: [40093110](https://pubmed.ncbi.nlm.nih.gov/40093110/)
- Added via: manuscript_brain_organoid_v6 reference ingest
- Preprint posted March 6, 2025; not peer-reviewed (CC-BY 4.0). Senior author: Jacob O. Kitzman (Univ. Michigan). Co-authors A. Marsh and F. Hernandez are Ambry Genetics employees (clinical database).

## Abstract

Variants of uncertain significance (VUS) limit the actionability of genetic testing. A prominent example is MUTYH, a base excision repair factor associated with polyposis and colorectal cancer, which has a pathogenic variant carrier rate approaching 1 in 50 individuals in some populations. To systematically interrogate variant function in MUTYH, we coupled deep mutational scanning with a DNA repair reporter containing its lesion substrate, 8OG:A. Our variant-to-function map covers >97% of all possible MUTYH point variants (n=10,941) and achieves 100% accuracy classifying the pathogenicity of known clinical variants (n=247). Leveraging a large clinical registry, we observe significant associations with colorectal polyps and cancer, with more severely impaired missense variants conferring greater risk. We recapitulate known functional differences between pathogenic founder alleles, and highlight sites of complete missense intolerance, including residues that intercalate DNA and coordinate essential Zn2+ or Fe-S clusters. This map provides a resource to resolve the 1,032 existing missense VUS and 90 variants with conflicting interpretations in MUTYH, and demonstrates a scalable strategy to interrogate other clinically relevant DNA repair factors.

## Key findings

A **deep mutational scan (DMS) of MUTYH** coupled to a **DNA-repair reporter** that directly reads out enzymatic function (8OG:A excision), rather than the cell-proliferation/drug-sensitivity readouts most saturation screens rely on. This makes growth-dispensable genes (~90% of the genome is dispensable for growth in culture) assayable.

- **Coverage / scale**: saturation mutagenesis of the 521-codon nuclear isoform cDNA. Map provides scores for **98% of possible single-codon variants**; abstract states **>97% of all possible point variants, n=10,941**. 99.0% of intended variants present at frequency ≥1/10,000 in the library. Function scores computed with **Rosace** (log2-scaled enrichment in repair-positive vs repair-negative sorts, with local false sign rate / lfsr akin to FDR).
- **Internal calibration is perfect at the extremes**: function scores **perfectly separated synonymous from nonsense variants** across codons 1–471 (n=725; precision-recall AUC = 1.0). Nonsense variants from codon 472 onward were uniformly tolerated (mean score −0.03) → disordered C-terminus is dispensable for 8OG:A repair in this assay.
- **Missense effects are continuous, not all-or-none.** Excluding unstructured termini (codons 1–51, 472–521): **25% of missense = loss-of-function (LOF), 59% = neutral (NEU), 16% = intermediate (INT)**. 9,776 missense variants classified total.
- **Clinical classification accuracy = 100%.** On a stringently filtered ClinVar truth set (n=247: 187 P/LP, 60 B/LB), function scores gave **prAUC = 1.0** and **100% concordance** (treating LOF+INT as pathogenic, NEU as benign). Less-stringent set allowing conflicting submissions (n=460): prAUC = 0.998. On clinical-lab missense-only set (n=87 benign/pathogenic, classifications independent of prior functional assays): agreed with 86/87 → **100% sensitivity, 98% specificity**.
- **ACMG evidence strength**: OddsPath for an abnormal call = 187 (PS3, strong evidence for pathogenicity); OddsPath for a neutral call = 0.0167 (= 1/59.9) (BS3, strong evidence for benignity). Lenient set reached PS3_very-strong (OddsPath 354).
- **Recapitulates founder-allele biology** (individual-variant validation, Fig. 2D): WT and benign polymorphism V8M restore repair; pathogenic **Y151C shows no activity** above KO background; **G368D reproducibly intermediate (~48% activity)** — consistent with G368D's lower mutation burden, later age of onset, and INT classification in the pooled map.
- **Orthogonal validation**: strong correlation (Fig. 3B) with E. coli fluctuation-assay mutation rates for **50 human MUTYH missense variants** (refs 21, 22). INT calls have low false-positive rate (no synonymous variants score INT) and recover known partially-active alleles (V218F, C304S, V206M, P129L).
- **Clinical risk (Ambry database, individual-level records)**: among individuals carrying a known pathogenic variant *in trans* with a missense VUS, MAP phenotype (CRC ≤50 y or polyp count ≥10, vs unaffected ≥60 y) was strongly enriched for **LOF VUS: hazard ratio 21.9 (95% CI 9.4–51.0), p = 7.7×10⁻¹³** (Cox PH), vs NEU baseline. **INT VUS: HR 3.6 (1.2–10.8), p = 0.02.** Functionally-abnormal missense VUS conferred risk comparable to Y151C/G368D compound heterozygosity. Cohort = 356 individuals biallelic for MUTYH variants (an order of magnitude more than UK Biobank).
- **VUS resolution resource**: map covers 99.4% of the 1,122 missense ClinVar VUS/conflicting SNVs; 26% are functionally abnormal (LOF 14%, INT 12%) → **295 clinical VUS reclassifiable toward likely-pathogenic**. Another ~696 LOF/INT missense SNVs not yet seen in clinical/population databases (sequencing has not saturated the pathogenic repertoire).
- **Equity / ancestry-agnostic**: 318 MUTYH missense SNVs ≥5-fold more common in non-European vs European ancestry groups; 84 functionally abnormal, mostly absent from ClinVar (23%) or VUS/conflicting (64%) despite being on average 220-fold more common in those ancestry groups.
- **Structure-function (AlphaFold3 model of MUTYH+8OG:A)**: LOF/INT enriched in buried residues (OR 35.7 and 6.6; Fisher P ≈ 10⁻¹⁸⁵). FoldX ΔΔG correlated modestly with score (Pearson r = −0.52) → destabilization explains many but not all defects. **7.9% of residues fully missense-intolerant**, 15.0% nearly so. Critical sites: [4Fe-4S] cluster cysteines (mean −0.90), catalytic D208/E106, allosteric network (N210, R213, R217), zinc-linchpin (H57 fully intolerant > C311/C314 > C304). A "ribbon" of constraint disfavors Asp/Glu substitutions near the DNA backbone (the founder G368D mechanism).

## Methods

- **Reporter**: GFP-off cassette where EGFP codon 35 carries a single **8OG:A mispair** that creates a stop codon on the transcribed strand; MUTYH excision of the mispaired adenine + downstream BER restores a Gln codon and GFP. Novel scalable reporter synthesis via enzymatic ssDNA production with site-specific 8OG incorporation by Hemo KlenTaq + 8oxo-dGTP; 8OG placement Sanger-verified (polymerase stalls, then ~2:1 A/C incorporation). mCherry co-transfected as transfection-efficiency control; repair % = (%GFP+)/(%mCherry+) normalized to WT.
- **Cell system**: HEK-293 with isogenic clonal **MUTYH knockout** (Cas9 targeting exon 4). KO reduces 8OG:A repair 76% vs parental. Mutant MUTYH cDNA libraries stably integrated at **low MOI (<0.1)** so each cell carries 0–1 variant; doxycycline-inducible (pCW57.1).
- **Library**: WT MUTYH cDNA (NM_001048174.1) split into 10 tiles; each codon replaced by NNN randomer; oPool oligos (IDT) cloned by Golden Gate (PaqCI) into tile plasmids, then into inducible lentiviral vector. 3 replicates/tile.
- **Selection & sequencing**: co-transfect mutant pools with 8OG-GFP reporter + mCherry; FACS-sort repair-positive (mCherry+GFP+) vs repair-negative (mCherry+GFP−); deep amplicon tile-sequencing of integrated cDNA from pre-sort + sorted pools (NovaSeqX / Singular G4). Reads merged (PEAR), aligned (bwa mem), counted via Snakemake (kitzmanlab/tileseq), scored by **Rosace**.
- **Classification cutoffs**: LOF = score ≤ −0.593 (97.5th pct of nonsense) & lfsr<0.05; NEU = score ≥ −0.237 (2.5th pct synonymous) or lfsr≥0.05; INT = between, lfsr<0.05. Low-abundance variants (<300 cpm, 3.5%) removed. Splice-disruptive exonic SNVs flagged by **SpliceAI** deltaMax ≥0.3.
- **Clinical validation**: ClinVar (downloaded 2024-12-08) stringent vs lenient truth sets; Ambry Genetics individual-level genotype + phenotype records; Cox PH regression (R survival/survminer). Evidence strength via ClinGen SVI OddsPath framework.
- **Structure/prediction**: AlphaFold3 model of 521-aa MUTYH + 8OG:A duplex + Zn²⁺ (aligned to mouse crystal 7ef8; ChimeraX, dssp, SASA); FoldX ΔΔG; GEMME, AlphaMissense, ESM1v for evolutionary/computational comparison.
- **Data**: scores in Supplementary Tables 1–2; raw + processed data at NCBI GEO **GSE290379**.

## Relevance to the brain-organoid ASD review

This is a **variant-effect-mapping (MAVE/DMS) method paper** — exactly the class of high-throughput functional-genomics technology the review extends to brain organoids for proactive autism genetics. In a Design–Build–Test–Learn (DBTL) framing it informs the **Test/measure** stage: it shows that a **direct molecular reporter of protein function** (here, DNA-repair activity) can yield saturation-scale, clinically-calibrated variant-to-function maps without relying on cell growth — important because most neurodevelopmental / ASD-relevant genes are *not* essential for proliferation in culture, so growth-based selection (as in many cancer-gene MAVEs) is inapplicable. The paper's explicit motivation that "~90% of genes are dispensable for growth in culture and remain inaccessible to [proliferation-based] approaches" is precisely the gap a custom organoid phenotypic readout would fill.

Key transferable elements for an organoid ASD-variant program:
- **Saturation single-codon mutagenesis** of a target cDNA, giving complete (not SNV-only) amino-acid coverage — the review's argument for exhaustive variant installation over sparse sampling.
- **Synonymous/nonsense internal controls** to calibrate score cutoffs and quantify false-positive rate (no synonymous in INT range) — a template for validating any organoid-based functional readout.
- **OddsPath/ACMG PS3/BS3 calibration** against ClinVar + an individual-level clinical registry — the standard the review would hold organoid-derived ASD-variant evidence to.
- **Resolving the VUS burden equitably across ancestries** — a stated goal for clinically-actionable ASD genes.

Caveat / contrast vs the review's likely Build stage: Hemker uses **exogenous cDNA over-expression in HEK-293 KO cells**, not endogenous-context editing. It therefore *cannot* capture regulatory/splicing effects — a limitation the companion ingest [Herger 2025](Herger_2025_High_throughput_screening_human_genetic_variants_by.md) (pooled prime editing in endogenous context) directly addresses. Together the two papers bracket the methodological spectrum (reporter-based DMS vs endogenous genome editing) the review draws on.

## Open questions / limitations

- **cDNA over-expression design cannot detect regulatory or splicing effects** (authors' stated primary limitation); they rely on SpliceAI to flag splice-disruptive SNVs rather than measuring them. Endogenous-locus saturation editing captures these but at sparser coverage.
- **Single-substrate, single-pathway readout**: the reporter measures only 8OG:A adenine excision in HEK-293; effects on other MUTYH functions, tissue-specific behavior, or protein-protein hand-offs (e.g., to APE1, the 9-1-1 complex) are inferred, not measured. Excess constraint at exposed residues D224, Q240, R246 *nominates* PPI sites but the interacting factor(s) are unconfirmed.
- **C-terminal truncations (≥472) score neutral**, but clinical evidence is equivocal (one Q473*/G368D compound-het CRC patient is a possible exception). Role of the C-terminus / PIP box in genome stability needs follow-up.
- **Intermediate (INT) variants (16%) are biologically real but clinically ambiguous** — likely hypomorphs sensitized to modifier effects (epistasis with OGG1, cis-regulatory variation in MUTYH or BER partners). Penetrance for these is not directly predictable from the map alone.
- A minority of ClinVar entries are **discordant** with the functional call (mostly somatic, criteria-lacking, or non-MAP incidental findings) — flagged for reclassification but not independently resolved here.
- Preprint, **not yet peer-reviewed**.
