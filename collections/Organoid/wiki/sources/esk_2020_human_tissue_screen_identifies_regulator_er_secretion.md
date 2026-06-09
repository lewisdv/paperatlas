---
title: "A human tissue screen identifies a regulator of ER secretion as a brain-size determinant."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1126/science.abb5390
pmid: 33122427
authors: Esk C et al.
journal: Science (New York, N.Y.) (2020)
source_ref: manuscript_brain_organoid_v6
pdf_status: downloaded
---

# A human tissue screen identifies a regulator of ER secretion as a brain-size determinant.

## Source

- Authors: Esk C, Lindenhofer D, Haendeler S, Wester RA, Pflug F, Schroeder B, Bagley JA, Elling U et al.
- Journal: Science (New York, N.Y.) (2020) — Science 370 (6519), 935–941; published online 29 Oct 2020.
- DOI: [10.1126/science.abb5390](https://doi.org/10.1126/science.abb5390)
- PMID: [33122427](https://pubmed.ncbi.nlm.nih.gov/33122427/)
- Lab: Jürgen A. Knoblich (IMBA, Vienna BioCenter). Co-first authors C. Esk and D. Lindenhofer.
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Loss-of-function (LOF) screens provide a powerful approach to identify regulators in biological processes. Pioneered in laboratory animals, LOF screens of human genes are currently restricted to two-dimensional cell cultures, which hinders the testing of gene functions requiring tissue context. Here, we present CRISPR-lineage tracing at cellular resolution in heterogeneous tissue (CRISPR-LICHT), which enables parallel LOF studies in human cerebral organoid tissue. We used CRISPR-LICHT to test 173 microcephaly candidate genes, revealing 25 to be involved in known and uncharacterized microcephaly-associated pathways. We characterized IER3IP1, which regulates the endoplasmic reticulum (ER) function and extracellular matrix protein secretion crucial for tissue integrity, the dysregulation of which results in microcephaly. Our human tissue screening technology identifies microcephaly genes and mechanisms involved in brain-size control.

## Key findings

- **CRISPR-LICHT enables the first pooled LOF screen in human 3D brain organoid tissue.** The method links each guide RNA (gRNA) to two nested DNA barcodes — a lineage barcode (LB) marking individual clones expressing a given gRNA, and a cell barcode (CB) tagging individual integrated templates within a lineage — so that gRNA effects can be scored as changes in *cells per lineage* rather than raw read counts. CB labeling uses a nonsense-mediated primer exclusion (NOPE) PCR strategy to count cells precisely without intermediate purification.
- **Motivating problem solved:** conventional pooled screens require homogeneous clonal growth, but DNA-barcode lineage tracing showed organoid lineages grow *unequally* (like tissue stem cells) whereas 2D cells grow equally; lineage-size variability increased reproducibly over organoid development. Dual barcoding separates this intrinsic growth noise from gRNA-induced cell loss. Dropping either CB or both LB+CB from the analysis **failed to score** nontargeting, cell-proliferation, and CDK5RAP2 controls, demonstrating both barcodes are required.
- **Screen scope and scale:** candidates drawn from the Developmental Brain Disorder Database (DBDB) plus a clinical test panel. The abstract states **173** microcephaly candidate genes; figure/text describe **172** genes categorized by level of evidence (LOE 1/2/3 = strong/moderate/weak). **4 gRNAs per candidate gene** plus nontargeting negative controls and cell-proliferation positive controls.
- **Validation rate:** 32 top-scoring LOE2/LOE3 genes (those with significant depletion of ≥2 gRNAs) were retested individually in independent flow-cytometry mixing assays; **78% of gRNAs validated**. **25 genes** were validated overall — described as nearly doubling the number of model-verified microcephaly genes. Most validated hits fall in centriole/centrosome biogenesis and DNA-damage-response pathways (the two canonical microcephaly pathways), but several lie outside them.
- **Hit categorization by timing:** category I = significant at day 17 AND day 28/42 (general proliferation control); category II = not significant at day 17 but significant at day 28 or 42 (more likely neurogenesis regulators). IER3IP1 was pursued as an underexamined category II hit.
- **Engineering/controls:** screen run in H9 hESCs carrying a lox-STOP-lox eCas9 (off-target-reduced eCas9-1.1) + dTomato reporter, de-repressed by 4-OHT–induced Cre delivered on the gRNA lentivirus. eCas9 induced at day 6. Proof-of-principle: a dTomato-targeting gRNA ablated reporter signal, and an RPL3 (proliferation gene) gRNA caused selective, induction-dependent cell loss (Fig. 1; *P* = 0.03 to *P* < 10⁻⁴, two-way ANOVA). 3 of 4 gRNAs against the positive-control microcephaly gene CDK5RAP2 showed significant depletion.

### IER3IP1 mechanism (deep characterization)

- **IER3IP1 KO organoids are microcephalic.** Three independent homozygous-LOF hESC lines all gave significantly smaller organoids than WT at day 42 (Fig. 4B; *n* = 65 WT, 70/62/60 for KO 1/2/3 across 8 differentiation experiments; *P* < 10⁻⁴, one-way ANOVA + Dunnett). Smaller SOX2⁺ neural rosettes indicate neural progenitor loss (*n* = 54 WT, 67/56/91 KO; *P* < 10⁻⁴).
- **Causality confirmed:** size defect rescued by re-expression of WT IER3IP1 but NOT by the patient mutant L78P, confirming the L78P patient mutation is causal.
- **ER dysfunction:** IER3IP1 localizes in cytosol close to but distinct from luminal ER/Golgi markers (yeast homolog Yos1p controls ER→Golgi exit of secreted proteins). RNA-seq over time: WT vs KO transcriptomes similar at the pluripotent stage but diverge in organoids; KO enriched for neural-differentiation pathways at day 28 at the expense of cell-division pathways. Day-42 up-regulated GO terms = ER stress / unfolded protein response (UPR), secretory pathway, Golgi vesicle transport; ERAD genes selectively up. EM showed significantly increased **ER width** (not length or area). UPR signature seen in hESCs and day-17 organoids fails to be down-regulated in KO at days 28/42.
- **ECM/secretion defect drives the phenotype:** mass spectrometry found many ECM proteins (collagens, laminin, fibronectin, etc.) depleted in KO organoids despite largely unchanged mRNA — a post-transcriptional/secretory defect. IHC confirmed reduced laminin, collagen IV, collagen I. Proliferative SOX2⁺KI67⁺ (and PAX6⁺) progenitors were abnormally localized outside ventricular-like rosettes (progenitor "shedding"); H&E showed disorganized rosettes. Model: IER3IP1 loss → reduced ECM deposition → loss of rosette/tissue integrity → premature neurogenesis → microcephaly.
- **Pharmacological rescue:** the integrated stress response inhibitor **ISRIB** (promotes eIF2B, restoring translation suppressed by UPR) significantly increased organoid and neural-rosette sizes in KO organoids (Fig. 5J; e.g. *P* = 0.002, *P* = 0.016, *P* = 0.02 for KO vs KO+ISRIB), partially rescuing the morphological defect.

## Methods

- **System:** dorsal-forebrain cerebral organoids from H9 hESCs (Lancaster-type protocol adapted to serum-free media); dorsal forebrain identity confirmed by expression analysis, IHC, and scRNA-seq. Neurogenesis barely detectable at day 17, extensive by days 28–42.
- **CRISPR machinery:** inducible eCas9-1.1 + dTomato behind lox-STOP-lox; Cre-ERT2 + gRNA delivered by lentivirus; activation by 4-hydroxytamoxifen at day 6.
- **Screen readout:** dual DNA barcoding (LB + CB with NOPE PCR), FACS for active-Cas9 (dTomato⁺/eCas9⁺) cells, next-gen sequencing; gRNA effects scored as cells-per-lineage fold change.
- **Validation/characterization:** independent flow-cytometry mixing assays; three homozygous IER3IP1-LOF hESC lines + WT/L78P rescue constructs; time-course RNA-seq, mass spectrometry (ProteomeXchange PXD019350), IHC, electron microscopy, H&E; ISRIB drug treatment.
- **Statistics:** two-way / one-way ANOVA (Sidak's / Dunnett's), unpaired two-tailed Student's *t* test; replicate counts given per panel above.
- **Data availability:** NGS under GEO GSE151384; MS under ProteomeXchange PXD019350.

## Relevance to the brain-organoid ASD review

This is the **in-organoid pooled-screen precedent** the review cites for its "in-organoid CRISPR tissue screen" theme. Key points for the manuscript "Programmable Brain Organoids for Proactive Autism Genetics":

- Demonstrates that **systematic, parallel loss-of-function genetics is feasible directly inside human brain tissue**, not just 2D culture — the conceptual foundation for proposing tissue-context CRISPR screens of ASD-risk genes in organoids.
- Provides the **technical template (CRISPR-LICHT)**: dual lineage+cell barcoding to overcome the unequal clonal growth and limited gRNA coverage that otherwise make organoid pooled screens infeasible. Any proposed ASD organoid screen must solve these same noise problems.
- Shows the readout can score **moderate, disease-relevant (not all-or-none) phenotypes** — relevant because many ASD-gene effects on neurodevelopment are expected to be subtle.
- Establishes a full **screen → validate → mechanism → drug-rescue** arc (173/172 candidates → 25 validated → IER3IP1 → ISRIB rescue), modeling the "proactive genetics" pipeline the review advocates: move from candidate gene lists to causally validated, human-tissue mechanisms and candidate interventions.
- Scope note: this screen targeted **microcephaly/brain-size genes**, not autism genes, and read out **cell loss/proliferation**. Extending the approach to ASD would require phenotypes beyond proliferation (e.g. maturation, connectivity, cell-type composition) — a gap the review's program would need to address.

## Open questions / limitations

- Readout is essentially a **proliferation/cell-loss (depletion) screen**; genes acting on differentiation, maturation, migration, or circuit function without changing cell number are poorly captured.
- **Coverage and clone number per organoid are limited**, constraining sensitivity for weak phenotypes and large libraries; the screen targeted ~172 curated candidates, not a genome-wide library.
- Minor internal inconsistency between the abstract ("173" genes) and the figures/text ("172" candidate genes categorized by LOE) — likely the inclusion/exclusion of a control; the validated-gene count (25) and "almost doubled" framing are consistent.
- IER3IP1 is a **ubiquitous ER housekeeping factor**; why its loss is brain-specific is explained only by a model (brain-critical secreted ECM cargo) and not exhaustively proven.
- ISRIB rescue is **partial**, and rescue significance varies across KO lines; therapeutic relevance is suggestive, not established.
- All work in H9-based lines / one organoid protocol; generality across genetic backgrounds and protocols is asserted ("can potentially be applied to other organoid systems") but not demonstrated here.

## Related

- [Lancaster 2013 cerebral organoids](../../wiki/sources/) — base organoid protocol adapted here (Nature 501, 373–379; cited ref 4).
- See collection [index](../index.md) for other in-organoid perturbation/screening methods (e.g. Fleck 2023 regulome inference/perturbation) and human-specific developmental-timing papers (Benito-Kwiecinski 2021, Schörnig 2021) ingested alongside this one.
