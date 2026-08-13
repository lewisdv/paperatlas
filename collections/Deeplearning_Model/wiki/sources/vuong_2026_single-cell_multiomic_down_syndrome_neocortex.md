---
title: A single-cell multiomic analysis identifies molecular and gene-regulatory mechanisms dysregulated in developing Down syndrome neocortex
kind: paper
status: ingested
added: 2026-08-13T10:40:00+09:00
raw_source: raw/sources/vuong_2026_single-cell_multiomic_down_syndrome_neocortex.pdf
---

# A single-cell multiomic analysis identifies molecular and gene-regulatory mechanisms dysregulated in developing Down syndrome neocortex

## Source

- File: [raw/sources/vuong_2026_single-cell_multiomic_down_syndrome_neocortex.pdf](../../raw/sources/vuong_2026_single-cell_multiomic_down_syndrome_neocortex.pdf)
- Added: 2026-08-13T10:40:00+09:00
- Authors: Celine K. Vuong, Alexis Weber, Patrick Seong, Nana Matoba, Yu-Jen Chen, Jordan Peyer, Shahab Younesi, and co-authors; Luis de la Torre-Ubieta (senior author)
- Venue/status: *Science* 392 (6796), `eaea1259` (23 April 2026)
- DOI: [10.1126/science.aea1259](https://doi.org/10.1126/science.aea1259)
- SHA-256: `91ccc14d4c621a4fa428783589f70d862fa2c92b2443036eac43c821f468713f`

## Summary

- This is a disease-comparative, paired single-nucleus RNA-and-chromatin-accessibility study of human mid-gestation neocortex in trisomy 21 (Ts21, Down syndrome) and control donors. It is a biological reference and regulatory-inference application, not a new multimodal-integration algorithm or a foundation model.
- Across 26 donors at gestational weeks 13–23, the authors retain 113,801 high-quality nuclei and report reduced neural progenitors and corticothalamic neurons, increased intratelencephalic neurons, and an accelerated excitatory-neuron specification trajectory in Ts21.
- Joint RNA–ATAC analysis and gene-regulatory-network inference identify broad Ts21-associated expression, accessibility, and regulatory-program changes. The authors nominate the chromosome-21 transcription factor [BACH1](../entities/BACH1.md) as a candidate pro-intratelencephalic regulator, including an inferred eRegulon containing `CUX2` and `BHLHE22`.

## Data and Analysis Setup

- The source profiles frozen human neocortex by single-nucleus multiome sequencing, measuring gene expression and chromatin accessibility in the same nucleus. It retains 113,801 nuclei from a cohort of 26 control and Ts21 donors spanning gestational weeks 13–23.
- RNA and ATAC modalities are jointly represented with weighted nearest-neighbor (WNN) integration for cell annotation and trajectory analyses. Differential composition, differential gene expression/accessibility, and pseudotime tests account for donor and relevant covariates as described in the Methods.
- The study uses `hdWGCNA` for cell-type-specific coexpression modules; NeuronChat and CellChat for expression-based cell-cell communication inference; and SCENIC+ on WNN-cell-type metacells to build enhancer-driven regulons (TF, motif-enriched regions, and target genes).
- An orthogonal primary human neural progenitor-cell (phNPC) system from control and Ts21 donors is differentiated for four weeks and profiled with the same multiome assay (45,282 nuclei) to test whether selected in vivo patterns recur in vitro.

## Reported Findings

- Ts21 is associated with fewer neural progenitors and corticothalamic/deep-layer neurons and more intratelencephalic/upper-layer neurons. Within the excitatory lineage, the pseudotime distribution and branch composition support the authors' interpretation of earlier neuronal differentiation and a shift toward intratelencephalic specification.
- The paper reports widespread, cell-type-specific differential gene expression and chromatin accessibility. The affected programs include progenitor maintenance, oxidative metabolism, extracellular-matrix and cytoskeletal regulation, neuronal maturation, and specification programs; these are reported associations, not a single demonstrated causal cascade.
- SCENIC+ yields enhancer-driven eRegulons from paired modalities. In excitatory newborn neurons, the HSA21-encoded `BACH1` eRegulon is reported as up-regulated, its inferred targets include pro-intratelencephalic TFs `CUX2` and `BHLHE22`, and its peak expression precedes `CUX2` in pseudotime. Recurrent patterns in phNPCs provide an orthogonal replication of this computational regulatory nomination.
- The phNPC experiment also reproduces the direction of several tissue-level findings: fewer progenitors, more neurons including upper-layer intratelencephalic cells, altered pseudotime distribution, widespread expression change, and increased oxidative-phosphorylation-associated programs.
- Communication analysis reports altered neurovascular and microglial signaling, including patterns consistent with a proangiogenic environment and prenatal microglial activation. These are ligand-receptor/expression-based network inferences rather than direct measurements of cell-cell signaling activity.
- The authors overlap differential regulons and accessible regions with neurodevelopmental-disorder gene and GWAS annotations. Such enrichment connects the altered programs to broader genetic-risk signals, but does not identify causal variants or establish that a particular regulon mediates a disorder.

## Interpretation Boundaries and Limitations

- The tissue comparison is cross-sectional. Pseudotime, differential composition, and inferred developmental acceleration are useful evidence of altered state distributions, but do not directly observe lineage histories or establish a causal developmental clock.
- Paired RNA–ATAC, TF motifs, and SCENIC+ eRegulons strengthen regulatory hypotheses but do not prove TF-to-peak-to-gene causality. In particular, the BACH1-to-`CUX2`/`BHLHE22` relationship is a nominated regulatory mechanism, not a direct perturbation result in this paper.
- phNPC recurrence supports part of the tissue signal in vitro, but a four-week progenitor culture cannot reproduce the full fetal neocortical tissue environment, spatial organization, or long-term maturation.
- The cohort covers mid-gestation only (GW13–23). Results should not be generalized to earlier development, late fetal development, postnatal cortex, all cortical regions, or therapeutic response without additional evidence.
- Cell-cell communication and genetic-enrichment results are computational/statistical associations whose evidential status differs from the IHC and cell-culture validations.

## Related Pages

- [BACH1](../entities/BACH1.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [Cell-Type-Specific Enhancer-Gene Mapping](../concepts/cell-type-specific-enhancer-gene-mapping.md)
- [Single-Cell Multimodal Integration Regimes](../concepts/single-cell-multimodal-integration-regimes.md)
- [A multi-omic atlas of human embryonic skeletal development](to_2024_a_multi-omic_atlas_of_human.md)
- [scMultiMap](../entities/scMultiMap.md)

## Open Questions

- Which altered regulatory programs remain after explicitly separating accelerated developmental state from direct trisomy-associated effects within each lineage?
- Can BACH1, its candidate cis-regulatory elements, and the proposed `CUX2`/`BHLHE22` relationships be validated with lineage-appropriate perturbations in human tissue models?
- How reproducibly do the reported cell-composition and interaction-network changes extend across cortical areas and later developmental windows?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: Poppler `pdftotext -layout` fallback; OpenDataLoader PDF under OpenJDK 21.0.12 failed before producing an output because of an internal page-content sort-comparator error.
- Generated: 2026-08-13T10:40:00+0900
- Extraction manifest: [raw/derived/opendataloader/vuong_2026_single-cell_multiomic_down_syndrome_neocortex/opendataloader-run.json](../../raw/derived/opendataloader/vuong_2026_single-cell_multiomic_down_syndrome_neocortex/opendataloader-run.json)
- Layout text: [raw/derived/pdftext/Vuong_2026_Down_Syndrome_Neocortex/Vuong_2026_Down_Syndrome_Neocortex.txt](../../raw/derived/pdftext/Vuong_2026_Down_Syndrome_Neocortex/Vuong_2026_Down_Syndrome_Neocortex.txt)

The fallback layout extraction and visual rendering support navigation and review. The immutable raw PDF remains the source of truth.
<!-- opendataloader:end -->
