# Which heterogeneity axes do the reference papers in this collection make hard to ignore?

## Short Answer

- The reference papers in this collection argue that `biological realism` cannot be reduced to one average similarity or one pooled disease signal.
- They make at least four heterogeneity axes hard to ignore:
- sex-stratified disease burden
- anatomical region and lineage path
- developmental-stage coverage and primary-reference fidelity
- multimodal regulatory and spatial context

## 1. Sex-Stratified Disease Burden

- [Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders](../sources/xia_2024_transcriptomic_sex_differences_in_postmortem.md) is the clearest example.
- Through [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md), it argues that psychiatric dysregulation differs not only in which genes move, but in the magnitude and network organization of disease-associated burden between females and males.
- This means a model that only learns one pooled psychiatric transcriptomic pattern could miss an important supported heterogeneity axis already present in the collection.

## 2. Anatomical Region And Developmental Path

- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md) shows that mature neuronal diversity depends on [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md), not only on broad endpoint labels.
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md) extends the same logic to cranial versus limb development and to different ossification programs.
- Together these papers push the collection toward trajectory-aware and region-aware evaluation rather than one generic `developmental state` notion.

## 3. Coverage And Fidelity Relative To Primary References

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) adds a different heterogeneity warning through [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md).
- The question here is not only whether one cell gets the right label, but whether an entire in vitro system covers the right primary states, misses important states, or diverges through common stress programs.
- This makes reference coverage itself a heterogeneity problem: model outputs or organoid datasets can fail because the biological target space is incompletely represented, developmentally shifted, or systematically biased.

## 4. Multimodal Regulatory And Spatial Context

- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md), especially through [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md), make another point.
- Some heterogeneity is not visible in transcript counts alone; it emerges only when transcriptional, epigenetic, and spatial structure are modeled together.
- In this collection, that means a model can look adequate at the expression level while still collapsing region-specific regulatory programs or spatially localized progenitor structure.

## 5. What This Means For The Rest Of The Collection

- The collection supports the claim that reference papers are defining evaluation constraints for later models, even when they are not themselves deep models.
- They collectively suggest that strong model performance should not be read only as high average annotation accuracy, perturbation correlation, or retrieval quality.
- It should also be read against whether the model preserves subgroup burden, regional developmental divergence, reference coverage, and multimodal regulatory structure.

## What The Collection Does Not Yet Support

- The current knowledge base does not support claiming that any one model in this collection already handles all four axes well.
- It also does not support a single unified benchmark that jointly measures sex-stratified burden, region-specific development, atlas coverage, and multimodal regulatory fidelity.

## Bottom Line

- The reference papers in this collection make heterogeneity look multi-axis rather than incidental.
- They push against `one average model score` thinking by showing that fidelity can fail by sex, by region, by developmental timing, by missing reference coverage, or by loss of multimodal regulatory context.

## Pages Used

- [Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders](../sources/xia_2024_transcriptomic_sex_differences_in_postmortem.md)
- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md)
- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md)
- [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [HNOCA](../entities/HNOCA.md)
