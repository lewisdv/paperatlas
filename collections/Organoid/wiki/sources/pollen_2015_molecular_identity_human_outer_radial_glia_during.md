---
title: "Molecular identity of human outer radial glia during cortical development."
kind: paper
status: ingested
added: 2026-06-09
doi: 10.1016/j.cell.2015.09.004
pmid: 26406371
authors: Pollen AA et al.
journal: Cell (2015)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/pollen_2015_molecular_identity_human_outer_radial_glia_during.pdf
pdf_status: downloaded
deep_ingested: 2026-06-09
---

# Molecular identity of human outer radial glia during cortical development.

## Source

- Authors: Pollen AA (co-first/corresponding), Nowakowski TJ (co-first), Chen J, Retallack H, Sandoval-Espinosa C, Nicholas CR, Shuga J, Liu SJ, Oldham MC, Diaz A, Lim DA, Leyrat AA, West JA, Kriegstein AR (corresponding; UCSF / Eli & Edythe Broad Center).
- Journal: Cell (2015), Vol 163:55-67.
- DOI: [10.1016/j.cell.2015.09.004](https://doi.org/10.1016/j.cell.2015.09.004)
- PMID: [26406371](https://pubmed.ncbi.nlm.nih.gov/26406371/)
- Data: dbGaP phs000989.v1.p1 (single-cell RNA-seq).
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

Radial glia, the neural stem cells of the neocortex, are located in two niches: the ventricular zone and outer subventricular zone. Although outer subventricular zone radial glia may generate the majority of human cortical neurons, their molecular features remain elusive. By analyzing gene expression across single cells, we find that outer radial glia preferentially express genes related to extracellular matrix formation, migration, and stemness, including TNC, PTPRZ1, FAM107A, HOPX, and LIFR. Using dynamic imaging, immunostaining, and clonal analysis, we relate these molecular features to distinctive behaviors of outer radial glia, demonstrate the necessity of STAT3 signaling for their cell cycle progression, and establish their extensive proliferative potential. These results suggest that outer radial glia directly support the subventricular niche through local production of growth factors, potentiation of growth factor signals by extracellular matrix proteins, and activation of self-renewal pathways, thereby enabling the developmental and evolutionary expansion of the human neocortex.

## Key findings

Defines the **molecular identity of human outer/basal radial glia (oRG / bRG)** by single-cell RNA-seq, yielding the now-canonical oRG marker set (**HOPX, TNC, PTPRZ1, FAM107A, MOXD1, LIFR, ITGB5**) and separating a true oRG transcriptional state from intermediate-progenitor (IPC) signatures.

### Single-cell dissection of the human germinal zone
- scRNA-seq of single cells captured **without enrichment** from microdissected **VZ and SVZ** of human cortex at **GW16-18**; **393 cells** (≥1,000 genes detected) from 3 individuals; Fluidigm C1 + SMARTer + Nextera XT.
- PCA + expectation-maximization clustering recovered the cortical excitatory lineage and ventral-telencephalic interneurons. Four clusters = **radial glia** (SLC1A3, PAX6, SOX2, PDGFD, GLI3); four = **intermediate progenitors** (EOMES/TBR2, ELAVL4, NEUROG1, NEUROD1/4, **PPP1R17**, PENK) with *loss* of VIM/HES1.
- **Reinterpretation of prior claims:** the "proneural" gene program recently attributed to oRG heterogeneity (Johnson et al. 2015) is here shown to be **the IPC signature**, not oRG. PPP1R17 marks IPCs of diverse multipolar morphology that lack the classical radial-glia signature -> a clean RG-vs-IPC boundary.

### Sources of variation among radial glia, and the oRG vs vRG split
- Among **107 classically-defined radial glia**, the dominant transcriptional axes (PC1/PC2/PC4) = **cell cycle** (G1 / G1-S / G2-M; novel G1 marker **CRYAB**, validated as ventricle-displaced, pHH3-/BrdU-low).
- **PC3 = anatomical niche (VZ vs OSVZ)**, significantly separating two states (OSVZ n=39 vs VZ n=68, p<1e-4): one almost purely VZ = **vRG**, the other from both VZ+SVZ = **oRG**.

### oRG marker set (the headline result) and validation
- Specificity scoring (correlation to an idealized cell-type marker across all 393 cells) -> **67 candidate oRG genes, 33 vRG genes, 31 pan-RG genes.**
- **oRG markers: HOPX (most specific), TNC, PTPRZ1, FAM107A, MOXD1** (+ ITGB5, SDC3, HS6ST1, PTN, LIFR, IL6ST). **vRG markers: CRYAB, PDGFD, TAGLN2, FBXO32, PALLD.** **Pan-RG: VIM, HES1, ATP1A2.**
- Validated by **in situ hybridization (GW17-19):** oRG markers strongest in **OSVZ**, vRG markers strongest in **VZ**; matched microdissected-tissue zonal expression (Allen prenatal atlas).
- ISH + immunostaining: cells expressing TNC/PTPRZ1/HOPX are **SOX2+, EOMES-, SATB2-** (radial glia, not IPCs/neurons) and bear **basal fibers** (oRG morphology). Time-lapse of GFP+ organotypic slices: cells undergoing **mitotic somal translocation (MST)** generate **SOX2/HOPX double-positive** daughters -> molecular identity tied to the defining oRG behavior.

### Mechanism: ECM + LIFR/STAT3 self-renewal in the OSVZ niche
- oRG cells (which **lack apical/CSF contact**) are enriched for **ECM / growth-factor-potentiating** genes - **TNC, PTPRZ1, SDC3, HS6ST1, ITGB5**, with ligand **PTN** the most up-regulated gene - i.e. oRG may **build their own trophic niche** locally.
- These oRG cell-surface genes (TNC, PTPRZ1, LGALS3BP) are also over-expressed in **glioblastoma**; oRG markers correlate with the GBM **stemness signature** more than vRG markers - a development/cancer parallel (EMT-like delamination, invasive migration).
- **LIFR/STAT3 self-renewal pathway is oRG-specific:** LIFR + co-receptor IL6ST(GP130) expressed in oRG; **p-Y705-STAT3 localized to oRG nuclei**; pharmacological STAT3-phosphorylation block **reduced oRG BrdU incorporation** (slice cultures); constitutively-active Stat3 in mouse cortex increased Sox2+ (not Eomes+) cells. oRG also express **NOG** (BMP inhibitor) - possibly restraining gliogenesis.

### Extensive neurogenic capacity (clonal analysis)
- Single FACS-sorted, retro-GFP-labeled cells imaged 1 wk: MST-first cells (oRG) gave **larger clones** than stationary-division IPCs. Three oRG clones followed 6 more weeks generated **hundreds (up to ~1,000) of daughter cells** - deep- and upper-layer neurons plus glia - vs mouse RG that typically make 10-100. Establishes oRG as **highly proliferative, multipotent human neural stem cells**.

### Developmental origin and primate conservation
- oRG marker transcripts appear in the **VZ early (~GW13.5)**, then become **OSVZ-restricted** by GW14.5 (FAM107A persists longest in VZ) - the **oRG transcriptional state emerges from the VZ** coincident with OSVZ elaboration. (Camp 2015 independently reports the same "bRG signature emerges from VZ after GW13.5.")
- **Conserved in macaque** (mirrors the human VZ->OSVZ trajectory). In **mouse**, oRG are rare/no distinct OSVZ; many human oRG genes (MOXD1, FAM107A, FBN2, BMP7, HS6ST2, LGALS3, TKTL1) are **not** expressed in mouse RG, though TNC/PTPRZ1/HOPX label scattered putative oRG in lateral/ventral pallium -> oRG signature is largely a **primate/human feature** of cortical expansion.

## Methods

- **Tissue:** microdissected VZ and SVZ from human fetal cortex (GW13.5-20 across experiments; scRNA-seq at GW16-18), Papain dissociation; macaque + mouse cortex for conservation.
- **scRNA-seq:** Fluidigm **C1** capture, SMARTer Ultra Low RNA Kit, Nextera XT; Tophat2 alignment, featureCounts, CPM normalization; QC drop <1,000 genes >1 CPM; **PCA + Expectation-Maximization clustering**; gene-specificity by Pearson correlation to idealized markers, confirmed by DESeq2.
- **In silico cross-reference:** Allen Institute Prenatal LMD microarray atlas (Miller 2014), NIH Blueprint NHP atlas, human/mouse coexpression networks (Lui 2014), single-cell GBM data (Patel 2014).
- **Tissue validation:** in situ hybridization + immunohistochemistry (HOPX, TNC, PTPRZ1, FAM107A, MOXD1, ITGB5, CRYAB, PDGFD; identity markers SOX2/EOMES/SATB2; pHH3, BrdU); confocal.
- **Behavior:** time-lapse imaging of GFP-adenovirus organotypic slices (GW15-19.5); post-hoc staining for HOPX/SOX2/GFP.
- **STAT3 function:** 48 h STAT3-phosphorylation-inhibitor treatment of fetal cortical slices + BrdU; in utero electroporation (E13.5) of constitutively-active Stat3 in mouse.
- **Clonal analysis:** FACS single cells -> pNIT-GFP retrovirus -> 1 cell/well on feeders; time-lapse classification (MST=oRG vs stationary=IPC); 7-day clone sizing; 6-week culture for lineage output.

## Relevance to the brain-organoid ASD review

- **This is the human-oRG molecular-identity anchor** the review uses for the "human-specific cell types" strand. oRG/bRG are the **human/primate-enriched basal progenitors** thought to drive neocortical expansion; their existence and markers are the yardstick for judging whether an organoid actually makes human-relevant progenitors.
- **Supplies the marker panel** (HOPX, TNC, PTPRZ1, FAM107A, MOXD1, ITGB5) used throughout the organoid literature to call oRG-like cells - and the **specificity caveats the manuscript discusses**: (i) the IPC "proneural" program is **not** oRG (a frequent mis-assignment the review flags); (ii) markers are **co-opted by glioblastoma stemness**, so positivity is not exclusively developmental; (iii) the oRG state **first appears in the VZ before becoming OSVZ-restricted**, so a marker+ cell's *location/morphology* (basal fiber, SOX2+/EOMES-) matters, not the transcript alone; (iv) several markers are **poorly conserved in mouse**, so rodent validation is unreliable.
- Defines the **mechanistic axes** (ECM/TNC-PTPRZ1, LIFR/STAT3 self-renewal, NOG) and the **defining behavior** (MST) that organoid-fidelity papers test for - directly relevant to whether brain organoids recapitulate the OSVZ niche.
- Pairs with the organoid-fidelity and human-evolution citations (Hansen 2010, Camp 2015, Andrews 2020, Benito-Kwiecinski 2021, Pollen 2019): Pollen 2015 provides the **ground-truth oRG signature**; the others ask whether organoids reproduce it. For the ASD review specifically, it grounds claims that organoids capture (or miss) the **proliferative basal-progenitor compartment** whose dysregulation underlies macrocephaly/overgrowth ASD subtypes.

## Open questions / limitations

- **Cell-type identity is inferred** from transcriptional clustering + correlation to bulk/atlas data and post-hoc staining; oRG vs vRG assignment rests on PC3 and marker specificity, not lineage tracing of the sequenced cells.
- **Modest scale/depth** (393 cells, GW16-18, 3 donors; 2014-era low-coverage C1 scRNA-seq); rare states and full oRG heterogeneity (Betizeau et al.'s morphological diversity) are under-sampled.
- **Marker non-exclusivity:** oRG genes overlap astrocyte (TNC, ITGB5, DIO2) and glioblastoma-stemness programs; HOPX et al. are enriched but not perfectly specific, and the VZ-origin phase means transient VZ expression.
- **STAT3 functional test** is pharmacological (slice) + mouse electroporation, not a clean human-oRG genetic loss; necessity for cell-cycle progression is correlational/inhibitor-based.
- **Mouse conservation is partial and ambiguous** - some markers label scattered mouse cells, complicating cross-species claims; what fraction of the human oRG program is truly human-specific is unresolved.
- **No organoid/iPSC data here** - applicability of the in vivo signature to pluripotent-stem-cell-derived oRG (the review's actual use case) must be imported from other studies.

## Related

- [Hansen 2010 — Neurogenic radial glia in the outer subventricular zone of human neocortex](hansen_2010_neurogenic_radial_glia_outer_subventricular_zone_human.md) — same lab; defines oRG/OSVZ by MST/self-renewal (the behavioral basis this paper gives a molecular identity).
- [Andrews 2020 — mTOR signaling regulates morphology and migration of outer radial glia](andrews_2020_mtor_signaling_regulates_morphology_migration_outer_radial.md) — mechanistic follow-up on oRG morphology/migration (CDC42), uses this marker set.
- [Camp 2015 — Human cerebral organoids recapitulate gene expression programs of fetal neocortex](camp_2015_human_cerebral_organoids_recapitulate_gene_expression_programs.md) — independently reports the bRG/oRG signature emerging from VZ after GW13.5; cites this paper.
- [Benito-Kwiecinski 2021 — An early cell-shape transition drives evolutionary expansion of the human forebrain](benitokwiecinski_2021_early_cell_shape_transition_drives_evolutionary_expansion.md) — human-vs-ape progenitor expansion, oRG-relevant.
- [Pollen 2019 — Establishing cerebral organoids as models of human-specific brain evolution](pollen_2019_establishing_cerebral_organoids_as_models_human_specific.md) — same first author; tests oRG/human-specific features in organoids.
- [Lancaster 2013 — Cerebral organoids model human brain development and microcephaly](lancaster_2013_cerebral_organoids_model_human_brain_development_microcephaly.md) — organoids that generate oRG/OSVZ-like progenitors.
- [Fleck 2023 — Inferring and perturbing cell-fate regulomes in human brain organoids](fleck_2023_inferring_perturbing_cell_fate_regulomes_human_brain.md) — GRN/perturbation framework for the progenitor fates this paper characterizes (GLI3, dorsal vs ventral).
- Concept: [Brain organoid fidelity, reproducibility, and atlas benchmarks](../concepts/brain-organoid-fidelity-reproducibility-and-atlases.md)
- Entity: [Single-cell atlas benchmarking](../entities/single-cell-atlas-benchmarking.md)
