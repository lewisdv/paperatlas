# Organoid functional assays, transplantation, and coculture

## Current position in this corpus

Several papers in this corpus are best understood as second-wave protocols: they assume an organoid already exists, then teach how to expose it to microbes, immune cells, injury models, or host tissue.

## Strong supporting sources

- [Cattaneo 2019](../sources/cattaneo_2019_tumor_organoid-t-cell_coculture_systems.md)
- [Puschhof 2021](../sources/puschhof_2021_intestinal_organoid_cocultures_with_microbes.md)
- [Co 2021](../sources/co_2021_controlling_the_polarity_of_human.md)
- [Watanabe 2022](../sources/watanabe_2022_transplantation_of_intestinal_organoids_into.md)
- [Kelley 2024](../sources/kelley_2024_host_circuit_engagement_of_human.md)
- [Olijnik 2024](../sources/olijnik_2024_generating_human_bone_marrow_organoids.md)
- [Protocol for the establishment and characterization of an endometrial-derived epithelial organoid and stromal cell co-culture system](../sources/ja_2024_protocol-for-the-establishment-and-characterization-of-an-endometrial-derived-epithelial-o.md)
- [Protocol for modeling injury-induced regeneration in retinal organoids and isolating hNRSCs for subretinal transplantation in rd10 mice](../sources/m_2025_protocol-for-modeling-injury-induced-regeneration-in-retinal-organoids-and-isolating-hnrsc.md)
- [Protocol for the coculture of murine vaginal epithelial organoids and T cells to induce resident memory CD8 T cell differentiation](../sources/jc_2025_protocol-for-the-coculture-of-murine-vaginal-epithelial-organoids-and-t-cells-to-induce-re.md)
- [Human liver-derived organoids recapitulate Oropouche virus infection and manifestation, enabling antiviral drug discovery](../sources/j_2026_human-liver-derived-organoids-recapitulate-oropouche-virus-infection-and-manifestation-ena.md)
- [Monocytes prevent apoptosis of iPSCs and promote differentiation of kidney organoids](../sources/e_2024_monocytes-prevent-apoptosis-of-ipscs-and-promote-differentiation-of-kidney-organoids.md)
- [Patient-derived and mouse endo-ectocervical organoid generation, genetic manipulation and applications to model infection](../sources/gurumurthy_2022_patient-derived_and_mouse_endo-ectocervical_organoid.md)
- [Protocol to enhance pre-sexual and sexual differentiation of Toxoplasma gondii using retinal cells and intestinal organoid-derived monolayers](../sources/s_2026_protocol-to-enhance-pre-sexual-and-sexual-differentiation-of-toxoplasma-gondii-using-retin.md)
- [Protocol for modeling the repair of intestinal damage by co-culturing mesenchymal stromal/stem cells and intestinal organoids](../sources/kp_2026_protocol-for-modeling-the-repair-of-intestinal-damage-by-co-culturing-mesenchymal-stromal.md)
- [Protocol to generate genetically engineered organoid-initiated mouse models of esophageal cancer](../sources/j_2025_protocol-to-generate-genetically-engineered-organoid-initiated-mouse-models-of-esophageal.md)
- [Blood-brain-barrier organoids for investigating the permeability of CNS therapeutics](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md)
- [A Dynamic Protocol to Explore NLRP3 Inflammasome Activation in Cerebral Organoids](../sources/d_2024_a-dynamic-protocol-to-explore-nlrp3-inflammasome-activation-in-cerebral-organoids.md)
- [Choroid plexus defects in Down syndrome brain organoids enhance neurotropism of SARS-CoV-2](../sources/m_2024_choroid-plexus-defects-in-down-syndrome-brain-organoids-enhance-neurotropism-of-sars-cov-2.md)
- [Integrated Molecular and Functional Characterization of Cervical Small-Cell Neuroendocrine Carcinoma Using a 3D Organoid Model](../sources/h_2026_integrated-molecular-and-functional-characterization-of-cervical-small-cell-neuroendocrine.md)
- [Patient-derived organoid xenografts reveal the multifaceted role of the lncRNA MALAT1 in breast cancer progression](../sources/patient-derived_2026_patient-derived-organoid-xenografts-reveal-the-multifaceted-role-of-the-lncrna-malat1-in-b.md)
- [Reconstruction of T cell infiltration in an osteosarcoma PDX-organoid interactive biobank for personalized immunotherapy](../sources/w_2026_reconstruction-of-t-cell-infiltration-in-an-osteosarcoma-pdx-organoid-interactive-biobank.md)
- [Histological fidelity and microenvironmental kinome signatures of metastatic patient-derived organoids](../sources/j_undated_histological-fidelity-and-microenvironmental-kinome-signatures-of-metastatic-patient-deriv.md)
- [Clinically used drug arsenic trioxide targets XIAP and overcomes apoptosis resistance in an organoid-based preclinical cancer model](../sources/l_2024_clinically-used-drug-arsenic-trioxide-targets-xiap-and-overcomes-apoptosis-resistance-in-a.md)
- [Th2 Cytokines Reshape the Transcriptome: Insights from a Canine Organoid Model of Atopic Dermatitis](../sources/b_2026_th2-cytokines-reshape-the-transcriptome-insights-from-a-canine-organoid-model-of-atopic-de.md)
- [Modeling Atrial Fibrillation in a Human Heart Macrophage Assembloid](../sources/modeling_undated_modeling-atrial-fibrillation-in-a-human-heart-macrophage-assembloid.md)

## Working synthesis

- This branch matters because many organoid projects fail or succeed at the assay-layer decision, not at baseline derivation.
- The collection now separates several distinct moves that used to blur together: access correction, partner reconstruction, injury or repair assays, barrier-specific platforms, and host-context validation.
- The practical rule is to add the **smallest sufficient layer**. If the missing piece is a defined partner, start with coculture or reconstruction. If the endpoint itself is repair, host circuitry, or host-restored signaling, escalate to transplantation or host context.
- The newer cohort broadens this beyond classic microbe or T-cell coculture into retinal repair plus transplantation, liver antiviral assays, cervical lineage-plus-infection platforms, cerebral inflammasome assays, choroid-plexus viral access systems, and cardiac immune-triggered arrhythmia models.
- Some assay layers intervene earlier than expected. Monocyte support in kidney organoids, for example, acts before the downstream readout by preserving competence during a vulnerable differentiation window.
- A useful rule for this page is therefore: **come here first when the baseline tissue already exists and the real problem is what interaction, injury, exposure, or validation layer should be added next**.
- The main tradeoff stays consistent across the branch: cleaner attribution and lower burden in vitro versus richer but noisier host-defined validation.

## Main tension

- baseline organoid robustness versus sophistication of the downstream assay layer
- controlled in vitro exposure versus more realistic but noisier in vivo validation

## Open questions

- What baseline maturity or polarity is required before a coculture or transplantation result is believable?
- Which assays genuinely add biological insight rather than just technical complexity?

## Related entities

- [Patient-derived organoids (PDO)](../entities/patient-derived-organoids-pdo.md)
- [Patient-derived organoid xenografts (PDO-X)](../entities/patient-derived-organoid-xenograft-pdo-x.md)
- [Host-context transplantation and repair validation](../entities/host-context-transplantation-and-repair-validation.md)
- [Host circuit engagement](../entities/host-circuit-engagement.md)
- [NLRP3 inflammasome](../entities/nlrp3-inflammasome.md)
- [Reproductive mucosal epithelial organoids](../entities/reproductive-mucosal-epithelial-organoids.md)

## Related queries

- [언제 coculture로 충분하고 언제 host validation이 필요한가](../queries/20260420_191749_coculture-vs-host-validation-for-interaction-questions.md)
- [donor-derived cancer work는 언제 compact ex vivo validation에서 멈추고 언제 immune reconstruction이나 PDO-X로 올라가야 하나](../queries/20260423_1600_compact-ex-vivo-vs-immune-reconstruction-vs-pdo-x.md)

## Related syntheses

- [Organoid assay escalation and validation playbook](../syntheses/20260423_organoid-assay-escalation-and-validation-playbook.md)
