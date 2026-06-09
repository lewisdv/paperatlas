---
title: "Integrative functional genomic analyses implicate specific molecular pathways and circuits in autism."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1016/j.cell.2013.10.031
pmid: 24267887
authors: Parikshak NN et al.
journal: Cell (2013)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# Integrative functional genomic analyses implicate specific molecular pathways and circuits in autism.

## Source

- Authors: Parikshak NN, Luo R, Zhang A, Won H, Lowe JK, Chandran V, Horvath S, Geschwind DH
- Journal: Cell (2013)
- DOI: [10.1016/j.cell.2013.10.031](https://doi.org/10.1016/j.cell.2013.10.031)
- PMID: [24267887](https://pubmed.ncbi.nlm.nih.gov/24267887/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Genetic studies have identified dozens of autism spectrum disorder (ASD) susceptibility genes, raising two critical questions: (1) do these genetic loci converge on specific biological processes, and (2) where does the phenotypic specificity of ASD arise, given its genetic overlap with intellectual disability (ID)? To address this, we mapped ASD and ID risk genes onto coexpression networks representing developmental trajectories and transcriptional profiles representing fetal and adult cortical laminae. ASD genes tightly coalesce in modules that implicate distinct biological functions during human cortical development, including early transcriptional regulation and synaptic development. Bioinformatic analyses suggest that translational regulation by FMRP and transcriptional coregulation by common transcription factors connect these processes. At a circuit level, ASD genes are enriched in superficial cortical layers and glutamatergic projection neurons. Furthermore, we show that the patterns of ASD and ID risk genes are distinct, providing a biological framework for further investigating the pathophysiology of ASD.

## Key findings

- **17 developmental coexpression modules** built by signed WGCNA on BrainSpan RNA-seq of human neocortex (PCW 8 → 12 months postnatal); 10/17 were preserved in independent data + GO-enriched + PPI-enriched (12/17 PPI-enriched at p < 0.003), giving ~12 reproducible, biologically meaningful modules.
- **Two functional families of ASD-relevant modules.** ASD risk genes split between (a) **early-fetal transcriptional-regulation modules M2 and M3** (downregulated over time, enriched for DNA binding / chromatin remodeling, incl. many BAF-complex members) and (b) **later synaptic modules M13, M16, M17** (upregulated over development; M16 from PCW 10 with hubs SV2A/NRXN1; M17 after PCW 13 with hubs CAMK2B/CACNA1C; M13 after PCW 16 with hubs GRIN2A/GABRA1).
- **Curated + unbiased ASD gene sets converge on the synaptic modules.** SFARI ASD (155 genes) most over-represented in M16 (p = 0.0024; OR 2.9 [1.4–5.5]; FDR<0.05), with M13/M17 trends. The independent asdM12 set (ASD postmortem cortex dysregulated genes; Voineagu 2011) was strongly enriched in the same three: M13 (p = 3.0×10⁻¹⁵, OR 3.6), M16 (p = 3.5×10⁻¹⁵, OR 3.9), M17 (p = 1.0×10⁻⁷, OR 2.5). 42% of asdM12 and 25% of SFARI ASD fall in these three modules — despite only 15 genes overlapping between the two sets.
- **Rare de novo variants (RDNVs) hit the early-transcriptional modules instead.** Protein-disrupting RDNVs in probands enriched in M2 (p = 0.006, OR 3.2) and M3 (p = 0.0011, OR 3.6) in the discovery set (622 probands / 222 sibs); replicated in an independent set (Iossifov 2012). Combining 4 studies (965 probands / 564–565 sibs): of 598 protein-disrupting+missense RDNV genes expressed in cortex, **52 in M2 (p = 9.6×10⁻⁶, OR 2.0) and 61 in M3 (p = 8.5×10⁻⁷, OR 2.1)** — i.e., ~113/598 (19%) of RDNV-affected genes sit in just two early-fetal modules. Silent RDNVs and siblings' RDNVs showed no enrichment (key negative controls).
- **Mutation-class → module mapping.** Inherited/common-variant-weighted sets (SFARI, asdM12) → synaptic modules (M13/M16/M17); larger-effect noninherited RDNVs → early transcriptional-regulation modules (M2/M3). ASD GWA signal was stronger in M13/M16 than M2/M3 — consistent with distinct biological processes being hit by distinct mutational classes (severity gradient: early transcriptional disruption predicted more severe than later synaptic).
- **ASD ≠ ID at the network level.** A curated set of 401 ID genes (364 cortex-expressed) was **not enriched in any of the 12 modules** (even at relaxed uncorrected p > 0.05). After removing the ~37 ASD/ID overlap genes, "ASD only" stayed enriched while "ID only" did not — establishing developmental/anatomical specificity of ASD vs the broadly distributed ID genes.
- **FMRP links the two ASD module families translationally.** FMRP CLIP targets (Darnell 2011) enriched in M2, M16, M17 (M2 p = 1.6×10⁻¹³ OR 3.0; M16 p = 2.4×10⁻²⁹ OR 5.7; M17 p = 9.3×10⁻¹⁰ OR 2.4) — translational regulation by FMRP connects early-transcriptional and synaptic ASD modules.
- **Transcriptional coregulation links anticorrelated modules.** 17 TFs predicted to bridge an up- and a down-regulated module via binding-site enrichment; MEF2A/MEF2C (synaptic plasticity), SATB1 (interneuron development), ELF1, FOXO1 highlighted, linking M2 ↔ M17. ChIP support: 39% of MEF2A, 23% of MEF2C, 87% of ELF1 predicted sites.
- **Circuit-level: superficial layers + glutamatergic projection neurons.** In adult primate cortex, asdM12 enriched in L3 (Z > 2.7, FDR<0.01) and ASD lists trend toward superficial (L2–L4) enrichment; ID genes trend toward deeper/germinal layers — significantly distinct distributions. In fetal cortex, ASD sets enrich in postmitotic-neuron laminae; M2 peaks in cortical plate (CPi/CPo) while M3 peaks earlier in germinal zone (VZ/SZ). Multiple ASD modules enriched for upper-layer glutamatergic neuron markers.
- **Gene prioritization output.** Network membership narrowed 684 RDNV-affected genes to a **113-gene higher-confidence list** (M2/M3 membership + elevated haploinsufficiency), and a further filter (P[HI]>0.5, layer/cell-type preference) to **24 candidates** (e.g., TBR1, CHD3, SMARCC1/SMARCC2, TOP1). BAF complex statistically associated: 6/28 BAF genes carry RDNVs (p = 0.0015, OR 5.7 [1.9–14.5]).

## Methods

- **Developmental networks:** Signed WGCNA (Zhang & Horvath; R WGCNA package) on BrainSpan whole-genome RNA-seq, neocortex only, PCW 8 → 12 months; genes called expressed at normalized RPKM ≥ 1 in ≥1 region/time in 80% of samples. Modules characterized by eigengene trajectory, GO (GO-Elite; ≥10 genes, Z>2, FDR<0.05), and PPI enrichment (InWeb+BioGRID: 251,881 interactions among 18,384 proteins; degree-matched permutation).
- **Gene sets:** SFARI ASD (AutDB; syndromic + evidence levels 1–4); asdM12/asdM16 (Voineagu 2011 ASD-cortex dysregulated modules); "ID all" (401 genes from 4 reviews); RDNVs from 4 exome studies (Iossifov, Neale, O'Roak, Sanders), split into discovery and replication sets, with silent RDNVs and sibling RDNVs as controls. Haploinsufficiency probability P(HI) computed per gene. Enrichment by two-sided Fisher's exact test, FDR-controlled; lack-of-enrichment claims required uncorrected p > 0.05.
- **Regulatory analyses:** TF binding-site enrichment on top-200-kME genes per module vs 3 background sets (upstream 1 kb of all genes, CpG islands, chr20) using TRANSFAC; overlaid with ENCODE/ChEA ChIP data. FMRP targets from CLIP (Darnell 2011).
- **Laminar/cell-type analyses:** Human fetal laminar expression (BrainSpan LMD, PCW 15/16 and 21) and adult primate laminar expression (Bernard 2012); per-gene per-layer differential-expression t values; gene-set skew quantified with bootstrapped CIs, FDR cutoff Z = 2.7 (FDR = 0.01); cell-marker relationships via correlation to cell-marker PC; ASD-vs-ID layer distributions compared by permutation.
- **Resource:** interactive coexpression network browser released (top 500 connections per module).

## Relevance to the brain-organoid ASD review

- The **second anchor paper grounding the review's developmental-convergence argument**, and the broader, hypothesis-naïve complement to Willsey 2013. It shows ASD genetic risk — across curated candidates, postmortem-dysregulated genes, common variants, and rare de novo variants — coalesces into a small number of human cortical developmental modules, supporting the review's thesis that heterogeneous ASD genetics funnels into tractable shared programs.
- Supplies the review's **molecular-pathway taxonomy**: an *early-fetal transcriptional/chromatin-regulation* axis (M2/M3; BAF complex, CHD genes, TBR1, FEZF2, TOP1) hit by large-effect de novo mutations, and a *synaptic-development* axis (M13/M16/M17; NRXN1, SV2A, GRIN2A, CAMK2B, SHANK2) — exactly the "ASD molecular pathways" theme, with FMRP and shared TFs (MEF2A/C, SATB1) named as the cross-linking regulators.
- Grounds the **circuit/cell-type target for organoid modeling**: glutamatergic cortical projection neurons and (in this analysis) superficial L2–L4, plus a fetal CPi signal and weaker deep L5/6 — reconciled in-text with Willsey's L5/6 finding. Together they tell an organoid platform to generate cortical projection neurons across deep and upper layers in a midfetal-like window.
- Gives the review a defensible **ASD-vs-ID specificity claim** (ID genes lack the same developmental/laminar focus), and a ready-made **prioritized gene list** (113 → 24 candidates) for organoid perturbation screens — directly serving "proactive autism genetics" by nominating which genes and circuits to model and read out.

## Open questions / limitations

- **Convergence is statistical/transcriptomic, not mechanistic.** Module membership and TF/FMRP linkage are bioinformatic predictions; the paper provides a framework and candidate list for experimental validation, not proven disease mechanisms — the validation gap an organoid system can address.
- **Incomplete annotation:** many implicated genes lack complete PPI data, P(HI) scores, TF-binding information, or brain functional study; reliance is placed most on RNA-seq coexpression for this reason.
- **Scope restrictions:** only neocortex analyzed (cerebellum, amygdala, etc. excluded due to cell-type heterogeneity / sample size); only single-gene disruptions considered (multigene CNVs excluded to improve signal-to-noise); de-novo-biased mutation data (inherited rare/noncoding variants under-represented). Authors predict heritable variants will preferentially hit synaptic (M13/M16/M17) rather than early-transcriptional modules.
- **ASD/ID boundary is not absolute:** some severe-ID and X-linked-ID gene subsets do overlap M2/M3 RDNV genes, consistent with milder hits to the same proteins causing ASD vs severe ID; finer ID specificity may emerge with more sequencing.
- **Resolution limits:** bulk laminar/developmental expression; conclusions pass stringent multiple-comparison cutoffs but weaker (potentially real) enrichments may surface with higher-resolution developmental tiling and larger sequencing cohorts. Upper-layer neuronal identity is not finalized until after PCW 28, complicating fetal laminar attribution (adult laminae used for cell-marker analyses).
- **Layer discordance with Willsey** (L2/3 emphasis here vs L5/6 there) reflects different input genes, network/module construction, and expression data sets; the review should present the deep-vs-superficial question as unresolved but bracketing the same midfetal cortical-projection-neuron biology.
