---
title: "Assembly of functionally integrated human forebrain spheroids."
kind: paper
status: ingested
added: 2026-06-09
deep_ingested: 2026-06-09
doi: 10.1038/nature22330
pmid: 28445465
authors: Birey F et al.
journal: Nature (2017)
source_ref: manuscript_brain_organoid_v6
raw_source: collections/Organoid/raw/sources/birey_2017_assembly_functionally_integrated_human_forebrain_spheroids.pdf
pdf_status: downloaded
---

# Assembly of functionally integrated human forebrain spheroids.

## Source

- Authors: Birey F, Andersen J, Makinson CD, Islam S, Wei W, Huber N, Fan HC, Metzler KRC et al. (senior author Sergiu P. Pașca, Stanford)
- Journal: Nature (2017), vol. 545, pp. 54-59
- DOI: [10.1038/nature22330](https://doi.org/10.1038/nature22330)
- PMID: [28445465](https://pubmed.ncbi.nlm.nih.gov/28445465/)
- Added via: manuscript_brain_organoid_v6 reference ingest

## Abstract

The development of the nervous system involves a coordinated succession of events including the migration of GABAergic (γ-aminobutyric-acid-releasing) neurons from ventral to dorsal forebrain and their integration into cortical circuits. However, these interregional interactions have not yet been modelled with human cells. Here we generate three-dimensional spheroids from human pluripotent stem cells that resemble either the dorsal or ventral forebrain and contain cortical glutamatergic or GABAergic neurons. These subdomain-specific forebrain spheroids can be assembled in vitro to recapitulate the saltatory migration of interneurons observed in the fetal forebrain. Using this system, we find that in Timothy syndrome-a neurodevelopmental disorder that is caused by mutations in the CaV1.2 calcium channel-interneurons display abnormal migratory saltations. We also show that after migration, interneurons functionally integrate with glutamatergic neurons to form a microphysiological system. We anticipate that this approach will be useful for studying neural development and disease, and for deriving spheroids that resemble other brain regions to assemble circuits in vitro.

## Key findings

- **First human forebrain assembloid.** Two separately patterned hPS-cell spheroids — dorsal forebrain / pallium (human cortical spheroids, **hCS**, glutamatergic) and ventral forebrain / subpallium (human subpallium spheroids, **hSS**, GABAergic) — are physically fused ("assembled") in vitro to model inter-regional interactions that prior single-region 3D cultures and whole-brain organoids could not capture. This is the foundational dorsal-ventral fusion paradigm later branded "assembloids."
- **hSS are bona fide ventral forebrain / GABAergic tissue.** Day-25 hSS strongly induce NKX2-1 with high FOXG1 and downregulated pallial EMX1 (subpallial identity). By day 60 they express GABA and GAD67; GABAergic subtypes appear over time — somatostatin (SST), calretinin (CR), calbindin (CB) early, and parvalbumin (PV) after ~200 days. Single-cell profiling (day 105; n = 11,838 cells, BD Resolve barcoding) separates hCS vs hSS: hCS contain VGLUT1+/TBR1/FEZF2/CTIP2 cortical glutamatergic neurons, TBR2+ intermediate progenitors, and PAX6/LHX2 dorsal (incl. HOPX+ outer radial glia-like) progenitors; hSS contain DLX1/GAD1/VGAT/SST GABAergic cells, ventral progenitors, and a small OLIG2/SOX10 oligodendrocyte-progenitor group. No mesodermal/endodermal cells.
- **hSS are functionally GABAergic before fusion.** Synaptogenesis shown by array tomography (SYN1 + VGAT puncta); ~75% of neurons fire action potentials on depolarization; ~60% show spontaneous IPSCs that reverse near the chloride potential and are abolished by the GABA_A antagonist gabazine (10 µM).
- **Saltatory interneuron migration is recapitulated and is directional.** Using a Dlxi1/2b::eGFP reporter (labels MGE-derived cortical interneurons; ~65% of GFP+ hSS cells are GAD67+), live imaging of fused hSS–hCS shows progressive, **unidirectional** movement of interneurons from hSS into hCS (no reverse hCS→hSS or hSS→hSS movement). Migration is **saltatory** — leading-process extension, then a transient soma swelling with nuclear translocation (nucleokinesis), then pause. By 30-50 days after fusion ~60% of migrated cells sit within the outer 100 µm of the hCS. The leading-process-to-soma ratio of human interneurons is ~2× that of mouse.
- **Migration matches human fetal tissue.** Dlxi1/2b::eGFP+ cells in human fetal forebrain (GW18, GW20) co-express GABA and NKX2-1 and show the same morphology and saltatory pattern, validating biological fidelity of the in-dish phenotype.
- **Migration is pharmacologically tractable.** A CXCR4 antagonist (AMD3100) reduces saltation frequency, length, speed, and path directness — consistent with the known CXCR4/CXCL12 control of cortical interneuron migration.
- **Disease modeling — Timothy syndrome (TS).** hSS/hCS were derived from 3 TS patients carrying the recurrent CACNA1C/CaV1.2 p.G406R gain-of-function mutation vs controls. TS neurons show increased residual calcium after depolarization. TS interneurons migrate with **increased saltation frequency but reduced saltation length and reduced speed-when-mobile → net less-efficient migration**. The defect is **cell-autonomous** (TS hSS interneurons migrating into control hCS keep the phenotype) and was reproduced by electroporating TS-CaV1.2 cDNA into mouse E14 ganglionic eminence (more frequent, shorter saltations).
- **TS migration defect is rescuable.** L-type calcium channel (LTCC) blocker nimodipine and the CaV1.2-inactivating CDK inhibitor roscovitine rescue TS saltation length/speed (nimodipine reduces saltation length in controls but rescues it in TS) — implicating LTCC activity directly.
- **Post-migration functional integration into a microcircuit.** After migrating into hCS, interneurons increase dendritic branching complexity, upregulate migration/activity genes (ERBB4, NXPH1, NNAT, SOX11; FOS, GRIP2, IGF1; disease genes RASD1, TCF4), and roughly **double** their max action-potential rate vs non-migrated cells. GABAergic synapses form on the cortical side (gephyrin/GPHN appears only in fused hCS; synaptograms show Dlxi1/2b eGFP co-localized with SYN1/VGAT apposed to GPHN). Migrated interneurons display both EPSCs and IPSCs and shift to receiving mainly EPSCs (synaptic input ~3×). Reciprocally, hCS glutamatergic neurons — EPSC-only before fusion — begin receiving IPSCs after interneuron arrival. Electrical stimulation of the hCS side evokes fast EPSCs then presumed multisynaptic, gabazine-sensitive IPSCs in migrated interneurons, demonstrating a connected human microcircuit.

## Methods / Protocol

- **Patterning (double-SMAD start, then opposing morphogens).** Intact hPS-cell colonies are lifted (dispase) into ultralow-attachment plates and neuralized by dual SMAD inhibition (dorsomorphin + SB-431542) plus ROCK inhibitor Y-27632, days 0-5/6; then moved to neural medium with EGF + FGF2 to ~day 24.
  - **hCS (dorsal/pallial):** default cortical protocol (per Pașca et al. 2015, Nat. Methods) — no ventralizing molecules.
  - **hSS (ventral/subpallial):** add the WNT-production inhibitor **IWP-2** (day 4-24) and the SHH-pathway agonist **SAG** (day 12-24) to drive subpallial NKX2-1 identity. Variant conditions add allopregnanolone (day 15-24) ± a brief retinoic-acid pulse (day 12-15) to raise spontaneous calcium activity without changing GABAergic fate (these "hSS-ISA/hSS-ISRA" conditions were used downstream). BDNF + NT3 days 25-42; unsupplemented neural medium thereafter.
- **Viral labelling before fusion.** Spheroids are infected overnight in microcentrifuge tubes. Interneurons are tracked with **lenti-Dlxi1/2b::eGFP** (Dlx1/2 enhancer; J. L. Rubenstein); cortical neurons/synapses with **AAV-hSYN1::mCherry**.
- **Assembly / fusion.** Around day 60-90 of differentiation (virally labelled 8-10 days prior), one hCS and one hSS are placed adjacent in a 1.5-ml Eppendorf tube for **3 days** in an incubator — >95% fuse — then gently transferred (cut P1000 tip) to 24-well ultralow-attachment plates with gentle medium changes every 2-3 days. hCS used were ~day-60 ("mid-gestation pallium" stage).
- **Migration readout (live imaging).** Intact fused hSS–hCS imaged 8-12 h (and up to 12 h baseline + 12 h post-drug for pharmacology) on a confocal with motorized stage (Leica SP8), 37 °C / 5% CO2, 50-150 µm depth, 15-20 min/frame; saltation frequency, saltation length, speed-when-mobile, and path directness quantified. Plating hSS on coverslips abolishes efficient migration (3D context required). Whole-mount **iDISCO** clearing visualizes deep migration into hCS.
- **Electrophysiology.** Whole-cell patch clamp (current- and voltage-clamp) on acute hSS or hSS–hCS slices; spontaneous and evoked EPSC/IPSC recordings; gabazine to confirm GABA_A-mediated IPSCs; array tomography for pre/post-synaptic protein localization.
- **Calcium imaging.** Fura-2 ratiometric imaging (depolarization-evoked residual Ca2+ in TS vs control) and GCaMP-style spontaneous spike recording (ΔF/F0 with ΔF > 1.2 scored as a spike).
- **Single-cell transcriptomics.** BD Resolve stochastic barcoding for bulk hCS/hSS characterization (day 105); FACS-sorted Dlxi1/2b::eGFP+ cells + Smart-seq2 for migrated-vs-resident interneuron states (4 weeks after assembly, ~day 121).
- **Cross-validation.** Mouse E14 ganglionic-eminence slice electroporation of WT vs TS CaV1.2; live imaging of Dlxi1/2b::eGFP in human fetal GW18/GW20 forebrain slices.
- A step-by-step protocol is deposited at Protocol Exchange (referenced in Methods).

## Relevance to the brain-organoid ASD review

- **Foundational assembloid platform.** This is the origin paper for dorsal-ventral forebrain **fusion (hSS + hCS → assembloid)**, the core platform the review cites for modeling inter-regional interactions and interneuron migration that single-region organoids cannot address. Cite as the entry point of the platform progression (manuscript **Fig. 1** platform-progression panel) — predecessor to later, assay-ready assembloid work (e.g., Sloan 2018, Miura 2022) and neuromodulatory/disease extensions.
- **Direct basis for Timothy-syndrome CACNA1C migration phenotype.** Establishes the CACNA1C p.G406R interneuron migration defect (more frequent but shorter, less-efficient saltations; cell-autonomous; LTCC-blocker-rescuable). This is the canonical example for the review's argument that programmable/patient-derived assembloids surface ASD-relevant, channelopathy-driven circuit-assembly phenotypes — and motivates "proactive" genotype-to-phenotype modeling.
- **Interneuron migration as a measurable disease readout.** Provides the quantitative migration metrics (saltation frequency/length, speed-when-mobile, path directness) and the excitation/inhibition (E/I) integration assays that the review can invoke when arguing assembloids yield mechanistic, druggable phenotypes relevant to the E/I-imbalance model of autism.
- **Demonstrates inter-regional functional circuit formation**, supporting review claims that fused regional organoids build connected human microcircuits (EPSC/IPSC integration, evoked multisynaptic responses) — not just cell mixing.

## Open questions / limitations

- **Maturation/fidelity ceiling.** Phenotypes are read out over weeks-to-months but still correspond to fetal/mid-gestation stages (PV interneurons appear only after ~200 days); the system models developmental migration, not mature cortical circuitry.
- **Subtype completeness.** hSS interneurons are biased toward MGE/Dlx-lineage (SST/CR/CB; PV late); CGE-derived and other interneuron classes are under-represented, and the Dlxi1/2b reporter, while largely cortical-interneuron-specific, is not a perfect lineage marker.
- **Reproducibility of fusion.** Outcomes depend on compartment age-matching (~day 60-90) and fusion timing; >95% fuse but projection/migration quantification variability across lines and labs is not deeply benchmarked here.
- **Reduced-complexity model.** Lacks vasculature, microglia, full layered cytoarchitecture, and long-range thalamic/other inputs; whether migrated interneurons reach physiological density, laminar positioning, and circuit balance is unresolved.
- **Generality of the disease readout.** TS findings rest on a single recurrent gain-of-function mutation in a small patient cohort; extension to other ASD risk genes and to loss-of-function or polygenic backgrounds remains to be shown.

## Related

- [Assembloids and regional fusion](../entities/assembloids-and-regional-fusion.md)
- [Brain organoid patterning and assembloids](../concepts/brain-organoid-patterning-and-assembloids.md)
- [Calcium imaging readouts](../entities/calcium-imaging-readouts.md)
