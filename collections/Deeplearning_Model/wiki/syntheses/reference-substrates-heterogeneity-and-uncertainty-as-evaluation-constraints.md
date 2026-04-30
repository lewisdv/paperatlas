# Reference Substrates, Heterogeneity, and Uncertainty as Evaluation Constraints in Deeplearning_Model

## Claim

- This collection no longer supports reading model quality only through task scores such as annotation accuracy, perturbation correlation, or retrieval rank.
- A second layer has become explicit: reference substrates define what the target biology is, heterogeneity anchors define what should not be averaged away, and uncertainty mechanisms define what a method should do when support is weak.
- Together, these papers act as evaluation constraints on the rest of the collection rather than as side materials around the "main" model papers.

## 1. Reference Substrates Define The Target Space

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) and [HNOCA](../entities/HNOCA.md) define a queryable organoid-to-primary reference space.
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md) defines a richer developmental substrate where transcriptomic, epigenetic, and spatial structure all matter.
- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md) adds a trajectory-rich primary reference where anatomical region is part of the target rather than metadata on the side.
- The key point is that these sources do not mainly ask `how well does the model predict?`
- They ask `what biological space is the model supposed to match, cover, or preserve in the first place?`

## 2. Heterogeneity Anchors Define What Should Not Be Smoothed Away

- [Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders](../sources/xia_2024_transcriptomic_sex_differences_in_postmortem.md) acts as a heterogeneity anchor through [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md).
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md) adds another axis: a model can fail by flattening regionally distinct maturation paths into one generic developmental story.
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md) add a third constraint: a model can look acceptable at expression level while still collapsing regulatory or spatial structure that only appears when multiple modalities are considered together.
- The collection therefore treats heterogeneity not as nuisance variation, but as part of the biological signal a strong model should preserve or explain.

## 3. Uncertainty Mechanisms Define What To Do When Support Is Weak

- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md) shows one action: return a broader label instead of forcing a fragile leaf prediction.
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md), through [SCimilarity](../entities/SCimilarity.md), shows another: keep the retrieved state but downgrade confidence when atlas support is weak.
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md) shows a system-level variant: diagnose whether the target reference space is missing, immature, or stress-shifted rather than only whether one cell is hard to label.
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md), through [Cell2fate](../entities/Cell2fate.md), add posterior dynamical uncertainty as quality control on whether temporal claims should be trusted.
- [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md), through [GPerturb](../entities/GPerturb.md) and partly [GEARS](../entities/GEARS.md), adds the perturbation side: high average predictive agreement does not guarantee trustworthy effect direction or magnitude.
- The collection therefore treats uncertainty as action-specific, not as one generic confidence number.

## 4. What This Changes For The Predictive Models

- Retrieval-first systems such as [SCimilarity](../entities/SCimilarity.md) should not be judged only by neighbor quality; they should also be judged by whether they know when the reference atlas is weak.
- Generative or transfer-oriented systems such as [scGPT](../entities/scGPT.md), [scFoundation](../entities/scFoundation.md), [C2S-Scale](../entities/C2S-Scale.md), [Squidiff](../entities/Squidiff.md), [CellOT](../entities/CellOT.md), and [GEARS](../entities/GEARS.md) should not be judged only by prediction metrics; they should also be read against heterogeneity preservation, reference-space adequacy, and the credibility of their uncertainty signals.
- Sequence-focused work such as [Orthrus](../entities/Orthrus.md) is less directly tied to atlas coverage, but it still inherits the broader lesson that transfer performance and trustworthy interpretation are not the same question.
- In other words, the non-model papers in this collection are not peripheral. They redefine what successful modeling is supposed to mean.

## 5. A More Useful Reading Order For This Collection

- First read the predictive model family for the task of interest.
- Then ask which reference substrate or atlas defines the target space for that task.
- Then ask which heterogeneity axes the model might accidentally erase.
- Then ask what kind of uncertainty the method reports, and what action that uncertainty actually triggers.
- This sequence is more faithful to the current collection than a flat leaderboard approach.

## Practical Consequence

- A model can look strong on average and still be biologically weak if it ignores subgroup burden, misses region-specific developmental structure, or acts confidently outside reference coverage.
- A resource paper can look non-predictive yet still be central because it defines the biological scaffold or evaluation space that makes later prediction claims meaningful.
- The collection is therefore best read as a layered system:
- predictive models
- reference substrates
- heterogeneity constraints
- uncertainty policies

## Bottom Line

- The most important evaluation question in this collection is no longer only `which model scores highest?`
- It is also `what biology is the model being asked to match, what variation must it preserve, and what does it do when support is weak?`
- That shift is the clearest sign that `Deeplearning_Model` has moved from source accumulation into a more mature synthesis phase.

## Sources Used

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md)
- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md)
- [Transcriptomic sex differences in postmortem brain samples from patients with psychiatric disorders](../sources/xia_2024_transcriptomic_sex_differences_in_postmortem.md)
- [Uncertainty-aware single-cell annotation with a hierarchical reject option](../sources/theunissen_2024_uncertainty-aware_single-cell_annotation_with_a.md)
- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)
- [GPerturb: Gaussian process modelling of single-cell perturbation data](../sources/xing_2025_gperturb_gaussian_process_modelling_of.md)
- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
- [Cell-State Similarity Search](../concepts/cell-state-similarity-search.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Sex-Stratified Transcriptomic Burden](../concepts/sex-stratified-transcriptomic-burden.md)
- [Hierarchical Partial Rejection](../concepts/hierarchical-partial-rejection.md)
- [RNA Velocity Modules](../concepts/rna-velocity-modules.md)
- [Gene-Level Perturbation Uncertainty](../concepts/gene-level-perturbation-uncertainty.md)
