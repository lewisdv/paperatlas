---
title: Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression
kind: paper
status: ingested
added: 2026-04-21T14:25:54+09:00
raw_source: raw/sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13060066/
published_date: 2026-04-03
organ: breast
protocol_focus: patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression
deep_ingested: 2026-04-22
---

# Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression

## Source

- PDF: [raw/sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.pdf](../../raw/sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC13060066/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13060066/)
- Status: deep ingested 2026-04-22
- Organ focus: breast cancer patient-derived organoids used as a front-end screen and then escalated into PDO-xenograft metastasis assays
- Protocol focus: screen a breast PDO biobank for MALAT1 antisense-oligonucleotide knockdown, then carry responsive TNBC models into in vivo splicing, stromal-remodeling, and metastasis readouts

## Study design

- Starting material: a biobank of 28 human breast tumor PDO models, followed by three selected TNBC PDO-xenograft lines for in vivo work
- Protocol stages:
  - expose breast tumor PDOs to human-specific 16-mer 3-10-3 gapmer MALAT1 ASOs at 3 uM, replenish ASO-containing medium on day 3, and harvest on day 6 to measure knockdown efficiency
  - use the in vitro screen to identify models with strong MALAT1 depletion and carry a subset of TNBC lines into PDO-xenograft experiments in the mammary fat pad
  - deliver MALAT1-targeting or scrambled ASOs systemically in vivo at 50 mg/kg twice weekly, then profile primary tumors, lung metastases, and stromal responses at endpoint
  - compare transcript abundance, differential expression, and alternative splicing changes across independent PDO-X models, with particular attention to intron-retention events and tumor-microenvironment signatures
- Key validation: 15 of 28 PDO models exceeded 70% MALAT1 knockdown, the three PDO-X models showed robust MALAT1 depletion in vivo, splicing changes appeared across all major event classes with strong intron-retention enrichment, and MALAT1 targeting reduced macrophage-associated stromal programs plus lung metastatic burden in the NH85TSc model
- Distinct protocol emphasis: this paper treats organoids as a translational funnel, beginning with a medium-throughput perturbation screen and ending in host-context metastasis and stroma readouts

## Summary

- The main value here is not simply that breast PDOs can be xenografted, but that organoids are used to choose which perturbation is worth escalating into animals.
- MALAT1 is tested as a regulator of transcription, alternative splicing, stromal crosstalk, and metastatic burden rather than as a one-dimensional growth gene.
- Within this corpus, the paper belongs to the patient-derived cancer and host-validation branch where in vivo readouts are needed to see effects absent from organoid growth alone.

## Key findings

- Knockdown accessibility varied sharply across the 28-model biobank, showing that delivery or targetability is itself a biologically meaningful filter rather than an implementation detail.
- Across three TNBC PDO-X models, MALAT1 depletion reproducibly rewired alternative splicing, with intron retention emerging as the clearest shared event class.
- The strongest cross-model in vivo effects were not limited to tumor-intrinsic transcript changes: mouse stromal signatures, especially macrophage-associated programs, also dropped after tumor-specific MALAT1 knockdown.
- At least one PDO-X line showed reduced lung metastatic burden even when gross primary-tumor shrinkage was not the dominant phenotype, which is exactly why the host step matters here.

## Distinctive contribution in this corpus

- One of the clearest examples in the collection where PDOs act as a front-end triage system for deciding which perturbation deserves animal escalation.
- Gives the adult-platform branch a breast-cancer paper where metastasis and tumor-stroma effects, not just culture growth, become the decisive readouts.
- Extends the host-validation logic from structural engraftment papers into transcriptomic and splicing-centered pharmacology.

## Limitations and caveats

- The most detailed in vivo work is concentrated in three TNBC PDO-X models, so the mechanistic generality beyond that subset remains uncertain.
- Knockdown efficiency is heterogeneous across the PDO bank, which means part of the observed biology may reflect ASO accessibility or uptake as much as MALAT1 dependence.
- Tumor-volume effects are not uniformly dramatic, so this platform is stronger for metastasis, splicing, and stromal-response questions than for claiming simple cytotoxic efficacy.

## Relevance to corpus

- Strengthens both the adult-platform and functional-assay concept paths with a breast PDO workflow that explicitly escalates from in vitro screening to metastatic validation.
- Useful when a project needs a template for deciding whether a tumor-organoid perturbation has enough signal to justify PDO-X work.
- Helps anchor questions about how much of a cancer phenotype is tumor intrinsic versus only visible once stromal and metastatic contexts re-enter the system.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related sources

- [Long-term culture, genetic manipulation and xenotransplantation of human normal and breast cancer organoids](dekkers_2021_long-term_culture_genetic_manipulation_and.md) - an earlier breast organoid bridge paper connecting stable ex vivo culture, genetic manipulation, and xenotransplantation.
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md) - another host-escalation paper where in vivo context restores biology that isolated PDO culture misses.
- [Integrated Molecular and Functional Characterization of Cervical Small-Cell Neuroendocrine Carcinoma Using a 3D Organoid Model](h_2026_integrated-molecular-and-functional-characterization-of-cervical-small-cell-neuroendocrine.md) - a rare-cancer tri-model comparator where matched genomics, xenografting, and drug response are evaluated together.

## Open questions

- Which molecular features best predict whether a PDO model will support strong ASO-mediated MALAT1 knockdown before any in vivo work begins?
- How generalizable are the metastasis and stromal-remodeling effects beyond TNBC and beyond the three PDO-X lines tested here?
- When MALAT1 depletion changes splicing strongly but tumor size only modestly, which downstream endpoint should be treated as the decisive translational readout?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:50:09+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b -f json,markdown`
- Manifest: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/opendataloader-run.json](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/opendataloader-run.json)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.json](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.json)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile1.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile1.png)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile2.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile2.png)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile3.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile3.png)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile4.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile4.png)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile5.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile5.png)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile6.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile6.png)
- Output: [raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile7.png](../../raw/derived/opendataloader/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b_images/imageFile7.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
