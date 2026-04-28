---
title: Mathematical Modeling of Non-Small-Cell Lung Cancer Biology through the Experimental Data on Cell Composition and Growth of Patient-Derived Organoids
kind: paper
status: ingested
added: 2026-04-21T14:25:57+09:00
raw_source: raw/sources/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10672646/
published_date: 2023-11-01
organ: lung
protocol_focus: mathematical Modeling of Non-Small-Cell Lung Cancer Biology through the Experimental Data on Cell Composition and Growth of Patient-Derived Organoids
deep_ingested: 2026-04-22
---

# Mathematical Modeling of Non-Small-Cell Lung Cancer Biology through the Experimental Data on Cell Composition and Growth of Patient-Derived Organoids

## Source

- PDF: [raw/sources/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.pdf](../../raw/sources/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC10672646/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10672646/)
- Status: deep ingested 2026-04-22
- Organ focus: patient-derived NSCLC organoids used as a quantitative substrate for tumor-composition modeling
- Protocol focus: couple lung tumor organoid culture with serial flow-cytometric cell-composition measurements so an ODE-based model can predict how key tumor and stromal populations shift over time

## Study design

- Starting material: surgical NSCLC tissue from 16 patients undergoing thoracotomic lobectomy
- Protocol stages:
  - digest minced tumor tissue with collagenase I, filter through a 70 um strainer, and resuspend the recovered cells in a lung organoid medium containing bFGF, EGF, N2, NeuroMax, N-acetyl cysteine, nicotinamide, Y27632, and HEPES
  - generate free-floating tumor organoids in agarose-coated 96-well plates by dispensing 25 uL collagen-based gel domes containing 50,000 cells per well and imaging them daily over a 14-day culture period
  - dissociate harvested organoids and quantify four major cell compartments by flow cytometry using PD-L1, CD206, CD8, and alpha-SMA as markers for cancer cells, tumor-associated macrophages, cytotoxic lymphocytes, and fibroblast-like stromal cells
  - fit an ordinary-differential-equation model and software application to the serial composition data, focusing on prediction across days 7, 14, and 21
- Key validation: the model captured time-dependent shifts in the four dominant subpopulations and could reproduce divergent patient-specific patterns, such as rising CD8 fractions accompanying falling PD-L1-positive cells in some organoids while the opposite balance stabilized in others
- Distinct protocol emphasis: this paper uses organoids as a measurement scaffold for quantitative systems modeling, not only as a 3D culture endpoint

## Summary

- The important move here is to treat PDOs as data-generating objects whose internal cell composition can parameterize a predictive model.
- This shifts the paper out of the usual derivation-or-drug-screen mold and into a quantitative readout-design space.
- Within this corpus, it sits between patient-derived cancer organoid culture and engineering-oriented analysis workflows.

## Key findings

- Patient-derived lung tumor organoids can preserve enough multicompartment structure to support composition-aware modeling rather than only gross growth readouts.
- The four-cell-state framing makes explicit that organoid behavior reflects competition and coexistence among tumor, immune-like, macrophage-like, and fibroblast-like compartments.
- The software layer is useful precisely because the authors acknowledge marker ambiguity and time-window limits, making the model a structured approximation rather than a definitive digital twin.

## Distinctive contribution in this corpus

- One of the clearest papers in the collection for showing how patient-derived tumor organoids can be turned into quantitative modeling substrates.
- Gives the engineering-or-screening branch a computational and flow-cytometric readout layer rather than an imaging-only one.
- Extends the adult-platform branch by showing that translational value can come from predicting changing cell composition, not just from preserving morphology or enabling drug response assays.

## Limitations and caveats

- The cohort is modest and the model is calibrated only across a limited time window, so longer-term predictions remain uncertain.
- Marker specificity is imperfect: PD-L1 and alpha-SMA are not uniquely confined to one compartment, which weakens a literal reading of the inferred subpopulation sizes.
- The in vitro system cannot recruit fresh cells from outside the plated organoid, so some ecological dynamics of the parental tumor are structurally absent.

## Relevance to corpus

- Strengthens both the adult-platform and engineering layers with a lung-cancer paper organized around serial composition measurement and prediction.
- Useful when a project needs more than endpoint viability and wants a principled way to think about internal tumor-organoid ecology over time.
- Pairs well with host-context restoration papers elsewhere in the corpus by clarifying what can already be extracted quantitatively before xenografting.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid engineering, imaging, and screening](../concepts/organoid-engineering-imaging-and-screening.md)

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)

## Related sources

- [Establishment of patient-derived cancer organoids for drug-screening applications](driehuis_2020_establishment_of_patient-derived_cancer_organoids.md) - the broader tumor-PDO foundation that this paper extends in a more quantitative direction.
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md) - another paper asking what key biological layers are retained or lost in PDO culture, but through kinome profiling rather than ODE modeling.
- [Reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy](w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md) - a tumor-organoid comparator where quantitative compartment control is achieved through immune reconstruction rather than through mathematical inference alone.

## Open questions

- Which added measurements, such as single-cell omics or better multiplexed markers, would most improve the model's biological fidelity?
- How far can patient-specific composition prediction be pushed before host-context effects make in vitro forecasts misleading?
- Which clinical decisions, relapse risk, immunotherapy timing, or drug sequencing, could realistically benefit from this kind of PDO-based ecological model?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:50:14+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data -f json,markdown`
- Manifest: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/opendataloader-run.json](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/opendataloader-run.json)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.json](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.json)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.md](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data.md)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile1.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile1.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile2.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile2.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile3.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile3.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile4.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile4.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile5.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile5.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile6.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile6.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile7.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile7.png)
- Output: [raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile8.png](../../raw/derived/opendataloader/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data/r_2023_mathematical-modeling-of-non-small-cell-lung-cancer-biology-through-the-experimental-data_images/imageFile8.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
