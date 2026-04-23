---
title: Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids
kind: paper
status: ingested
added: 2026-04-21T14:30:21+09:00
raw_source: raw/sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.pdf
article_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13083117/
published_date: 2026-04-20
organ: organoid-system
protocol_focus: histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids
deep_ingested: 2026-04-22
---

# Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids

## Source

- PDF: [raw/sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.pdf](../../raw/sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.pdf)
- Article: [https://pmc.ncbi.nlm.nih.gov/articles/PMC13083117/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13083117/)
- Status: deep ingested 2026-04-22
- Organ focus: metastatic patient-derived tumor organoids compared with their matched biopsy and liver-metastatic PDO-xenograft states
- Protocol focus: ask which signaling programs are preserved in metastatic PDO culture and which ones reappear only after in vivo engraftment

## Study design

- Starting material: 18G core-needle biopsies from metastatic lesions of five cancer patients, used to derive matched patient biopsy, PDO, and PDO-xenograft samples
- Protocol stages:
  - mince metastatic biopsy tissue and establish PDO cultures in BME, then maintain successful lines for up to 6 months with low-passage use at passage 10 or below
  - expand PDOs for roughly 1-4 months before profiling, then dissociate them to single cells for xenograft work
  - inject 5 x 10^5 PDO cells in 10 uL PBS into the splenic parenchyma of NSG mice to seed liver metastatic PDOX lesions
  - compare the original biopsy state KP1, cultured organoid state KP2, and xenograft state KP3 using blinded histology plus PamGene protein-tyrosine-kinase activity profiling
- Key validation: KP3 tumors recapitulated the histological appearance of the original metastatic lesions, most kinase activity remained conserved across the three states, and a recurrent SRC-family kinase signal was specifically depressed in KP2 but partially restored in KP3
- Distinct protocol emphasis: this is less a derivation paper than a model-calibration paper about what PDO culture keeps, what it loses, and what host re-engraftment can recover

## Summary

- The paper is useful because it names a specific failure mode of metastatic PDO culture instead of simply saying that "microenvironment is missing."
- The central claim is that most tumor-intrinsic signaling survives PDO culture, but SRC-family and other context-sensitive kinase activity can disappear in vitro and re-emerge in vivo.
- Within this corpus, it belongs to the host-validation branch of patient-derived cancer work where xenografting is used to restore interpretability, not just to prove tumorigenicity.

## Key findings

- Metastatic core-needle biopsies can support durable PDO culture, which matters because metastatic sampling is often smaller and clinically messier than resection-based tumor collection.
- Histological identity remained surprisingly stable even after the organoids were sent through a mouse liver metastasis stage, supporting PDOX as a credible structural validation layer.
- The main loss in isolated culture was not global signaling collapse but a narrower microenvironment-sensitive kinase module, especially SRC-family activity.
- That distinction matters for translational screening because a drug aimed at a context-restored pathway could look inactive in KP2 even if it remains relevant in the patient or KP3 state.

## Distinctive contribution in this corpus

- One of the clearest papers in the collection for explaining why xenograft escalation sometimes adds mechanistic value rather than merely checking whether tumors grow.
- Gives the adult-platform branch a metastatic-cancer comparator where the missing layer is quantified as a kinome signature, not just described qualitatively.
- Helps connect patient-derived cancer organoids to host-context validation without requiring a full immunotherapy or orthotopic tumor-model framing.

## Limitations and caveats

- The cohort is small and heterogeneous across metastatic cancer types, so the exact signaling changes may not generalize evenly across tumors.
- The kinome assay is focused on protein-tyrosine-kinase activity and does not fully capture the broader signaling landscape, stromal composition, or immune context.
- KP3 restoration occurs in a mouse liver-metastasis setting, which is informative but not necessarily identical to each patient's native metastatic niche.

## Relevance to corpus

- Strengthens both the adult-platform and functional-assay concept pages with a concrete example of when host escalation repairs a missing signaling layer.
- Useful whenever a tumor-organoid result looks biologically plausible but may be falsely negative because the relevant pathway is microenvironment dependent.
- Pairs especially well with PDO-X and organoid-initiated mouse-model papers that need a sharper rationale for when in vivo work is worth the cost.

## Related concepts

- [Adult stem cell and patient-derived organoid platforms](../concepts/adult-stem-cell-and-patient-derived-organoid-platforms.md)
- [Organoid functional assays, transplantation, and coculture](../concepts/organoid-functional-assays-transplantation-and-coculture.md)

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Patient-derived organoid xenografts (PDO-X)](../entities/patient-derived-organoid-xenograft-pdo-x.md)

## Related sources

- [Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression](patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md) - another PDO-X paper where in vivo escalation reveals biology that simple growth assays would miss.
- [Integrated Molecular and Functional Characterization of Cervical Small-Cell Neuroendocrine Carcinoma Using a 3D Organoid Model](h_2026_integrated-molecular-and-functional-characterization-of-cervical-small-cell-neuroendocrine.md) - a rare-cancer tri-model comparator with stronger genomics and histopathology coupling.
- [Protocol to generate genetically engineered organoid-initiated mouse models of esophageal cancer.](j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.md) - a different host-escalation strategy where the purpose is orthotopic tumor initiation rather than restoration of missing microenvironmental signaling.

## Open questions

- Which stromal, ECM, or vascular cues are most responsible for the SRC-family signal that disappears in KP2 and partially returns in KP3?
- Can defined coculture or engineered-matrix systems rescue this kinase program in vitro well enough to avoid some xenograft work?
- How often should negative PDO drug results be re-tested in PDOX or more complex coculture systems before being treated as true negatives?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-21T14:49:43+09:00
- Command: `/Users/davin/paper_collect/.venv-opendataloader/bin/opendataloader-pdf /Users/davin/paper_collect/collections/organoid/raw/sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.pdf -o /Users/davin/paper_collect/collections/organoid/raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv -f json,markdown`
- Manifest: [raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/opendataloader-run.json](../../raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/opendataloader-run.json)
- Output: [raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.json](../../raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.json)
- Output: [raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md](../../raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)
- Output: [raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv_images/imageFile1.png](../../raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv_images/imageFile1.png)
- Output: [raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv_images/imageFile2.png](../../raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv_images/imageFile2.png)
- Output: [raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv_images/imageFile3.png](../../raw/derived/opendataloader/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv_images/imageFile3.png)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
