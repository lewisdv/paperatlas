---
title: "Human cerebral organoids recapitulate gene expression programs of fetal neocortex development."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1073/pnas.1520760112
pmid: 26644564
authors: Camp JG et al.
journal: Proceedings of the National Academy of Sciences of the United States of America (2015)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Human cerebral organoids recapitulate gene expression programs of fetal neocortex development.

## Source

- Authors: Camp JG (co-first), Badsha F (co-first), Florio M, Kanton S, Gerber T, Wilsch-Bräuninger M, Lewitus E, Sykes A, Hevers W, Lancaster M, Knoblich JA, Lachmann R, Pääbo S (corresponding), Huttner WB (corresponding), Treutlein B (corresponding; Max Planck Institutes, Leipzig/Dresden).
- Journal: Proceedings of the National Academy of Sciences USA (2015), Vol 112(51):15672-15677.
- DOI: [10.1073/pnas.1520760112](https://doi.org/10.1073/pnas.1520760112)
- PMID: [26644564](https://pubmed.ncbi.nlm.nih.gov/26644564/)
- Data: GEO GSE75140 (single-cell RNA-seq).
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Cerebral organoids-3D cultures of human cerebral tissue derived from pluripotent stem cells-have emerged as models of human cortical development. However, the extent to which in vitro organoid systems recapitulate neural progenitor cell proliferation and neuronal differentiation programs observed in vivo remains unclear. Here we use single-cell RNA sequencing (scRNA-seq) to dissect and compare cell composition and progenitor-to-neuron lineage relationships in human cerebral organoids and fetal neocortex. Covariation network analysis using the fetal neocortex data reveals known and previously unidentified interactions among genes central to neural progenitor proliferation and neuronal differentiation. In the organoid, we detect diverse progenitors and differentiated cell types of neuronal and mesenchymal lineages and identify cells that derived from regions resembling the fetal neocortex. We find that these organoid cortical cells use gene expression programs remarkably similar to those of the fetal tissue to organize into cerebral cortex-like regions. Our comparison of in vivo and in vitro cortical single-cell transcriptomes illuminates the genetic features underlying human cortical development that can be studied in organoid cultures.

## Key findings

This is the manuscript's **fidelity/concordance anchor**: the first **single-cell** comparison of Lancaster-protocol cerebral organoids against primary human fetal neocortex, establishing that organoid cortex-like cells use **~80%+ concordant gene-expression programs** along the apical-progenitor → basal-progenitor → neuron (AP→BP→N) lineage - while flagging two specific deficits (under-produced basal progenitors; a tissue-culture stress signature).

### Datasets (scale and stage)
- **Fetal reference:** 226 single-cell transcriptomes from **two human neocortex specimens at 12-13 weeks post-conception (wpc)** (mid-neurogenesis).
- **Organoids:** **333 cells** from five whole organoids (days **33, 35, 37, 41, 65**, iPSC-derived) + **175 cells** from four microdissected single-ventricle cortical regions (day 53 r1/r2 ESC-derived; day 58 r3/r4 iPSC-derived). Total organoid cells ≈ **508**.
- Platform: Fluidigm **C1** capture, SMARTer Ultra Low RNA Kit, Nextera XT; 100-bp paired-end on HiSeq 2500 to **2-5 M reads/cell**.

### Fetal lineage reconstruction (the reference framework)
- PCA + hierarchical clustering of fetal cells → **7 clusters**: **AP1** (16 cells, S/G2/M, MKI67+), **AP2** (24 cells, G1) - both PAX6/GLI3/SOX2/HES1/VIM/PROM1+ and VZ-correlated; **BP1** (11 cells, iSVZ; INSM1/EOMES/HES6/NEUROD4+, VIM/SOX2-low; AP→BP transition); **BP2** (10 cells, EOMES + NEUROD6, cell-cycle-low; committed BPs); and three neuron clusters **N1** (39 cells, newborn/migrating, iSVZ-oSVZ), **N2** (53 cells, transitional), **N3** (67 cells, mature, CP-correlated).
- Cells were anchored to **bulk laser-microdissected zones** (VZ/iSVZ/oSVZ/CP; Fietz 2012) and **FACS-purified aRG/bRG/neurons** (Florio 2015). Zonal maximum-correlation tally: CP 100, oSVZ 62, iSVZ 24, VZ 39 cells.
- **Monocle** pseudotime recovered a continuous **AP(VZ) → BP(iSVZ/oSVZ) → neuron(CP)** trajectory; a TF correlation network (edges at correlation >0.3) split into two densely connected subnetworks (NPC proliferation: HES1/SOX9/PAX6/SOX2; neuronal differentiation: TBR1/MYT1L/BCL11A/B/NEUROD6) bridged by AP→BP-transition TFs (ASCL1, EOMES, NEUROD4, HES6, INSM1).
- Excluded 1 endothelial cell (PECAM1+) and 5 ventral-telencephalic interneurons (GAD1, DLX1/2/5/6, ERBB4) before lineage analysis.

### Organoid cell composition (t-SNE)
- 508 combined organoid cells → **11 t-SNE clusters**: dorsal-forebrain/cortex NPCs (c1-c3) + cortical neurons (c4), all **FOXG1+/OTX2-low** (also NFIA/NFIB; neurons NEUROD6+); ventral-telencephalic/hippocampal & immature-dorsal NPCs (c5-c6, OTX2+) + ventral/interneuron-like neurons (c7); **cortical-hem** signaling cells (c8-c9, R-spondins + WNT2B); **mesenchymal** ECM-expressing cells surrounding cortical regions (c10-c11).
- **Regional heterogeneity within single organoids:** 3 of 4 microdissected cortical regions were **FOXG1+/OTX2-/NFIA/NFIB/NEUROD6+** (true dorsal cortex); the 4th was **FOXG1-/OTX2+** (ventral forebrain) - i.e. individual organoids contain cortical regions of **divergent forebrain identity**, discriminable by NPC/neuron signatures.

### Organoid-vs-fetal concordance (the headline result)
- Organoid cortex-like cells (clusters 1-4; **157 cells**) reconstruct the **same AP→BP→N lineage** by Monocle, with PAX6/EOMES/MYT1L showing restricted lineage expression and matching GO enrichments (cell cycle, mitosis, neuron projection/differentiation, forebrain development, synapse formation, migration).
- **Combined PCA + a cell-lineage network intermix organoid and fetal cells** within the two main NPC and neuron subclusters: "the major proportion of the variation in these data is **not between in vitro and in vivo** tissues but among cell states during neurogenesis."
- **Pathway-level concordance** (fraction of genes with similar fetal vs organoid cell-type-specific expression): ECM production/sensing **16/18 = 89%**; transcription regulation **10/11 = 90%**; RG delamination **12/15 = 80%**; Notch/Delta signaling **7/10 = 70%**; neurite outgrowth **24/25 = 96%**.
- **Disease/evolution gene concordance:** projecting four curated gene sets - modern-human fixed amino-acid changes (modHuman; Prüfer 2014), OMIM neurogenesis-disorder genes, human-deleted conserved elements (hCondel; McLean 2011), and human-accelerated DHS regions (haDHS; Gittelman 2015) - onto the fetal AP→BP→N regulome, **average 82.5%** of these genes were positively correlated between fetal and organoid cell types → human-specific/disease-relevant corticogenesis features are "**faithfully modeled**" in organoids.

### Where organoids diverge (the limits)
- **Basal-progenitor deficit:** BPs were **6% of organoid NPCs vs 34% in fetal tissue** (organoid cortical cells classified as 57 AP1, 57 AP2, **1 BP1, 6 BP2**, 4 N1, 16 N2, 16 N3) - attributed to an **underdeveloped SVZ** and/or earlier developmental stage. (Note: bRG/oRG-like cells observed but rarer than in vivo.)
- **Tissue-culture stress / media signature:** the only systematic DEGs (>3-fold + 97th-percentile ROC discrimination) up in organoids were a "response to organic substance" GO set - **immediate-early genes FOS, EGR1** (Notch targets reported in human but not mouse RG), plus CSNK2B/HMGCS1/BCHE/HERPUD1/CLIC1/ADIPOR2; **TUBB** was the single most differential gene (up in both organoid APs and neurons). Down in organoid neurons: **RBP1** (vitamin-A transporter - likely a response to vitamin A in media), **PRDM8, NFIX**. Authors interpret these as **culture-environment responses, not fundamental differentiation differences**: <5% of fetal-vs-organoid DEGs reach the classification power seen between APs and neurons.
- **bRG/oRG timing note** (added in review, citing Pollen 2015 GW16-18): the bRG signature genes are expressed at **12-13 wpc in cells Camp classifies as VZ-correlated APs**, consistent with the **bRG state emerging from the VZ after GW13.5** - so this dataset's early stage partly explains the scarcity of a distinct bRG compartment.

## Methods

- **Organoids:** Lancaster/Knoblich cerebral-organoid protocol (Lancaster 2013/2014), with mTeSR1 used during embryoid-body formation; ESC and iPSC lines (mTeSR1 culture). Sampled across days 33-65 (whole) and days 53/58 (microdissected ventricle regions). Immunostaining for MKI67/DCX/PAX6/TBR2(EOMES)/p-vimentin to confirm VZ-like germinal zones and abventricular neurogenesis.
- **Fetal tissue:** human neocortex **12-13 wpc** (elective termination, ethics-approved, maternal consent); processed per Florio 2015.
- **scRNA-seq:** Accutase + DNase dissociation; sequential 40/30/20-µm strainers; 90-95% viability (Trypan blue); **Fluidigm C1** single-cell capture/lysis/cDNA (SMARTer Ultra Low); Nextera XT libraries; HiSeq 2500, 100-bp PE, 2-5 M reads/cell. Bowtie2/TopHat/Cufflinks; PCA on variable genes (variance >0.5, >2 cells); cell typing by **maximum correlation to bulk zonal (Fietz 2012) and FACS-purified (Florio 2015) references**.
- **Analysis:** hierarchical clustering; **t-SNE** (organoid clusters); **Monocle** pseudotime lineage reconstruction (independent-component space, minimal spanning tree); intercellular adjacency/correlation networks; **TF covariation networks** (edges at correlation >0.3, via AnimalTFDB); DAVID GO; differential expression by fold-difference + **median ROC test** (Macosko 2015) with >3-fold / 97th-percentile thresholds.
- **Comparative gene sets:** modHuman fixed substitutions (Neanderthal genome), OMIM neurogenesis disorders, hCondel human-lost conserved elements, haDHS human-accelerated brain-accessible chromatin.

## Relevance to the brain-organoid ASD review

- **This is the foundational organoid-vs-fetal *fidelity / concordance* citation** the review leans on to justify reading autism biology out of organoids at all: at single-cell resolution, organoid cortical cells deploy **~80-96% concordant** programs (ECM, delamination, Notch, neurite outgrowth, TF regulome) and **intermix with fetal cells** in lineage space - the variation is developmental-state, not in-vitro-vs-in-vivo. This is the evidentiary basis for "organoids recapitulate fetal corticogenesis."
- **Defines the concordance *window*:** the benchmark is **12-13 wpc fetal cortex vs day-33-65 organoids** (mid-neurogenesis, AP→BP→neuron). It tells the review *which developmental stage* organoid fidelity is established for, and pairs naturally with the Mariani telencephalic-organoid window (≈9-16 wpc by BrainSpan) - i.e. **organoid disease models like Mariani's FOXG1/ASD work operate inside a transcriptomically validated fetal window**. (Camp in fact cites Mariani 2015 as the bulk-transcriptome precedent it improves on with single-cell resolution.)
- **Names the fidelity *caveats* the review must hedge with:** (i) organoids **under-produce basal progenitors** (6% vs 34%) - directly relevant since BPs/oRG are the expansion-driving, ASD-overgrowth-relevant compartment (ties to the Pollen 2015 oRG-identity strand and macrocephaly ASD subtypes); (ii) a reproducible **tissue-culture stress / immediate-early-gene (FOS/EGR1) + media (RBP1/vitamin A) signature** - the same artifact class later formalized by Bhaduri 2020 and benchmarked by Cheroni 2022/Velasco 2019.
- Supplies the **human-specific-evolution fidelity** point (modHuman/hCondel/haDHS genes ~82.5% concordant), supporting the review's claim that organoids can model **human-specific** cortical features - the conceptual bridge to the oRG/NOTCH2NL/ARHGAP11B expansion literature.

## Open questions / limitations

- **Modest scale and single early stage:** ~226 fetal (12-13 wpc only) + ~508 organoid cells on 2014-era low-throughput C1 scRNA-seq; authors explicitly call for "higher throughput studies over an expanded time course." Rare cell types (notably bRG/oRG) and later corticogenesis (upper-layer neurons, gliogenesis, circuit assembly) are under-sampled or absent.
- **Basal-progenitor under-representation is unexplained mechanistically** (developmental-timing vs intrinsically underdeveloped SVZ vs dissociation bias unresolved); whether the BP deficit alters downstream neuron production/identity is untested here.
- **Concordance is correlational** (maximum-correlation cell typing + pairwise gene-expression correlation), not lineage tracing; organoid cells are *assigned* to fetal types, so true equivalence vs transcriptional mimicry is not formally separable.
- **Culture-artifact interpretation is inferential:** FOS/EGR1/RBP1 differences are *argued* to be media/stress responses with low functional impact (<5% reach AP-vs-N discrimination power), but their consequences for corticogenesis "will be required" to test - left open.
- **Generalizability across protocols/lines is untested:** uses the unguided Lancaster protocol on a small number of ESC/iPSC lines; whether the ~80% concordance holds for guided/patterned protocols or other lines is not addressed (later answered by Velasco 2019, Cheroni 2022, Kanton 2019).
- **No disease modeling here** - this is a normal-development fidelity benchmark; applicability to ASD/disease organoids is inferred, not demonstrated.

## Related

- [Mariani 2015 — FOXG1-dependent dysregulation of GABA/glutamate neuron differentiation in ASD](mariani_2015_foxg1_dependent_dysregulation_gaba_glutamate_neuron_differentiation.md) — cited here as the bulk-transcriptome precedent; the ASD disease model whose ≈9-16 wpc window this single-cell fidelity benchmark validates.
- [Pollen 2015 — Molecular identity of human outer radial glia during cortical development](pollen_2015_molecular_identity_human_outer_radial_glia_during.md) — the contemporaneous oRG/bRG marker paper Camp cites; the BP/oRG compartment Camp finds under-produced in organoids.
- [Lancaster 2013 — Cerebral organoids model human brain development and microcephaly](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) — the organoid protocol benchmarked here.
- [Kanton 2019 — Organoid single-cell genomic atlas uncovers human-specific features of brain development](kanton_2019_organoid_single-cell_genomic_atlas.md) — successor single-cell organoid-vs-primate atlas from the same Treutlein/Pääbo group; scales up this comparison.
- [Velasco 2019 — Individual brain organoids reproducibly form cell diversity of the human cerebral cortex](velasco_2019_individual_brain_organoids_reproducibly.md) — reproducibility/fidelity benchmark complementing this concordance result.
- [Cheroni 2022 — Benchmarking brain organoid recapitulation of fetal corticogenesis](cheroni_2022_benchmarking_brain_organoid_recapitulation_fetal_corticogenesis.md) — multi-protocol WGCNA benchmark vs BrainSpan; extends the fidelity-window question across protocols/time.
- [Bhaduri 2020 — Cell stress in cortical organoids impairs molecular subtype specification](bhaduri_2020_cell_stress_in_cortical.md) — formalizes the tissue-culture/metabolic-stress signature Camp first flags (FOS/EGR1, media responses).
- [Hansen 2010 — Neurogenic radial glia in the outer subventricular zone of human neocortex](hansen_2010_neurogenic_radial_glia_outer_subventricular_zone_human.md) — defines the oSVZ/bRG compartment whose organoid scarcity Camp quantifies.
- Concept: [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- Entity: [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)
