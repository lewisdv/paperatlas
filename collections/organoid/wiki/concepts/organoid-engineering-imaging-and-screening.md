# Organoid engineering, imaging, and screening

## Current position in this corpus

The newest protocols in this collection do not stop at making organoids. They increasingly add gene editing, pooled perturbation, viral delivery, advanced imaging, or whole-mount preparation to turn organoids into higher-leverage experimental systems.

## Strong supporting sources

- [Hendriks 2020](../sources/hendriks_2020_establishment_of_human_fetal_hepatocyte.md)
- [Dekkers 2021](../sources/dekkers_2021_long-term_culture_genetic_manipulation_and.md)
- [Broutier 2016](../sources/broutier_2016_culture_and_establishment_of_self-renewing.md)
- [Dekkers 2019](../sources/dekkers_2019_high-resolution_3d_imaging_of_fixed.md)
- [Bakker 2022](../sources/bakker_2022_preparing_ductal_epithelial_organoids_for.md)
- [Fitzgerald 2024](../sources/fitzgerald_2024_generation_of_semi-guided_cortical_organoids.md)
- [Dardano 2025](../sources/dardano_2025_production_of_human_blood-generating_heart-forming.md)
- [Meng 2025](../sources/meng_2025_crispr_screens_in_human_neural.md)
- [Chen 2023](../sources/chen_2023_protocol_for_generating_reproducible_miniaturized.md)
- [Protocol to create isogenic disease models from adult stem cell-derived organoids using next-generation CRISPR tools](../sources/m_2024_protocol-to-create-isogenic-disease-models-from-adult-stem-cell-derived-organoids-using-ne.md)
- [Protocol for transducing human primary epithelial prostate cells and patient-derived organoids with high efficiency](../sources/c_2024_protocol-for-transducing-human-primary-epithelial-prostate-cells-and-patient-derived-organ.md)
- [Protocol for the establishment and characterization of South African patient-derived intestinal organoids](../sources/n_2025_protocol-for-the-establishment-and-characterization-of-south-african-patient-derived-intes.md)
- [Protocol for generation and utilization of patient-derived organoids from multimodal specimen](../sources/s_2025_protocol-for-generation-and-utilization-of-patient-derived-organoids-from-multimodal-speci.md)
- [Protocol for generating and analyzing organ-on-chip using human and mouse intestinal organoids](../sources/iv_2024_protocol-for-generating-and-analyzing-organ-on-chip-using-human-and-mouse-intestinal-organ.md)
- [Protocol for the derivation and culture of murine trophoblast organoids for CRISPR-Cas9 screening](../sources/q_2024_protocol-for-the-derivation-and-culture-of-murine-trophoblast-organoids-for-crispr-cas9-sc.md)
- [Protocol for differentiating human pluripotent stem cells into midbrain organoids for targeted microinjection of viruses](../sources/m_2025_protocol-for-differentiating-human-pluripotent-stem-cells-into-midbrain-organoids-for-targ.md)
- [Blood-brain-barrier organoids for investigating the permeability of CNS therapeutics](../sources/bergmann_2018_bloodbrain-barrier_organoids_for_investigating_the.md)
- [Automated detection and growth tracking of 3D bio-printed organoid clusters using optical coherence tomography with deep convolutional neural networks](../sources/d_2023_automated-detection-and-growth-tracking-of-3d-bio-printed-organoid-clusters-using-optical.md)
- [Segmentation and Multi-Timepoint Tracking of 3D Cancer Organoids from Optical Coherence Tomography Images Using Deep Neural Networks](../sources/f_2024_segmentation-and-multi-timepoint-tracking-of-3d-cancer-organoids-from-optical-coherence-to.md)
- [A Convexity-Preserving Level-Set Method for the Segmentation of Tumor Organoids](../sources/x_2024_a-convexity-preserving-level-set-method-for-the-segmentation-of-tumor-organoids.md)
- [Shape Factor Analysis as a Quantitative Framework for Assessing Spheroid and Organoid Morphology and Invasiveness](../sources/shape_2026_shape-factor-analysis-as-a-quantitative-framework-for-assessing-spheroid-and-organoid-morp.md)

## Working synthesis

- Engineering layers make organoids much more useful for mechanism, screening, and lineage interrogation.
- The newer refill sources widen this from pooled perturbation and imaging prep to whole-mount clearing, MSI-ready sample handling, isogenic CRISPR editing, high-efficiency transduction, organ-on-chip deployment, trophoblast screening, specimen-normalized PDO setup, and targeted viral microinjection.
- The newest batch widens the engineering layer further into readout design itself: BBB permeability organoids, bioprinted tumor-cluster OCT tracking, 13-day breast-cancer OCT longitudinal tracking, convexity-preserving PDAC segmentation, and cross-system shape-factor phenotyping.
- They also show that adult or patient-derived and region-specific organoids increasingly act as substrates for engineering rather than endpoints in themselves.
- Together these papers show that organoid engineering is not only about perturbing the culture. It also includes building the image-analysis, permeability, and morphology-quantification stack that makes screening outputs comparable across batches and models.
- Deep networks dominate some tracking tasks, but classical geometry-aware segmentation and simple shape metrics still remain useful when data are small, labels are scarce, or high-throughput bright-field readouts matter more than end-to-end automation.
- The practical bottleneck often shifts from differentiation itself to delivery, imaging quality, screen design, or readout normalization.

## Main tension

- organoid generation as an endpoint versus organoid generation as a platform for perturbation
- experimental leverage versus technical overhead

## Open questions

- Which engineering layer adds the most insight for the least extra protocol burden?
- How should screening or imaging workflows be standardized across organoid lines and batches?
