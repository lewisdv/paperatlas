# Reference Substrates and Queryable Biological Spaces in Deeplearning_Model

## Claim

- The reference-oriented papers in this collection are not one homogeneous class.
- They define at least four different kinds of biological substrate:
- a queryable organoid-to-primary projection atlas
- a multi-omic developmental regulatory scaffold
- a primary developmental trajectory atlas
- a forward-looking perturbation atlas roadmap
- These substrates matter because they define different target spaces, coverage assumptions, and evaluation uses for the predictive models elsewhere in the collection.

## 1. Queryable Projection Substrate: HNOCA

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md) and [HNOCA](../entities/HNOCA.md) define the clearest queryable projection substrate.
- Its main strength is not a new predictive architecture, but a large control-and-reference space for mapping organoid cells onto primary developing human brain states.
- Through [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md), HNOCA lets the collection ask whether an organoid protocol covers the right states, misses expected states, or drifts through common in vitro stress programs.
- This makes HNOCA especially useful as a projection, benchmarking, and protocol-comparison substrate.

## 2. Multi-Omic Developmental Substrate: Embryonic Skeletal Atlas

- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md) defines a different kind of substrate.
- Through [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md), it combines transcriptomic, epigenetic, and spatial structure to reconstruct developmental programs and regulatory zonation.
- This substrate is richer than a transcript-only reference because it can support lineage reconstruction, regulatory-network inference, spatial localization, and disease-oriented reasoning inside one developmental scaffold.
- In the collection, this is the strongest example of a reference space where multimodal structure itself is part of the target biology.

## 3. Primary Developmental Trajectory Substrate: Human Hypothalamus Atlas

- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md) defines a third substrate type.
- Through [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md), its central contribution is not multimodal depth or query tooling, but a primary developmental map in which anatomical region and lineage path are inseparable from mature cell identity.
- This makes it a strong benchmark substrate for asking whether future models preserve region-aware maturation logic rather than only endpoint labels.
- Compared with HNOCA, this atlas is less about in vitro projection infrastructure and more about what the native developmental target space actually looks like.

## 4. Causal-Roadmap Substrate: Perturbation Cell Atlas

- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md) contributes a fourth kind of substrate.
- Through [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md), the paper reframes perturbation modeling as an atlas-building problem rather than only a downstream prediction task.
- This substrate is still partly aspirational, but it matters because it defines the causal and interventional space that perturbation models such as [GEARS](../entities/GEARS.md), [CellOT](../entities/CellOT.md), [Squidiff](../entities/Squidiff.md), and [Tahoe-x1](../entities/Tahoe-x1.md) might eventually plug into.
- In the collection, it is the clearest example of a substrate defined by desired intervention coverage rather than by already harmonized observational references.

## 5. Why These Substrates Are Not Interchangeable

- HNOCA is strongest as a queryable projection and fidelity-comparison system for organoids.
- The skeletal atlas is strongest as a multi-omic developmental and regulatory scaffold.
- The hypothalamus atlas is strongest as a primary region-and-trajectory benchmark.
- Perturbation Cell Atlas is strongest as a causal-roadmap substrate for future intervention modeling.
- Calling all of them simply `reference papers` hides the fact that they answer different evaluation questions.

## 6. What Each Substrate Lets The Rest Of The Collection Ask

- HNOCA asks whether a model or protocol lands in the right primary reference neighborhood and whether atlas coverage is strong enough to trust the mapping.
- The skeletal atlas asks whether a model preserves multimodal regulatory and spatial structure rather than only transcript-level resemblance.
- The hypothalamus atlas asks whether a model preserves region-specific developmental divergence instead of collapsing it into one generic maturation path.
- Perturbation Cell Atlas asks whether future perturbation models cover enough causal state space to be worth reading as atlas components rather than only narrow predictors.

## Practical Consequence

- Predictive models in this collection should not be judged against an abstract notion of `ground truth`.
- They should be read against the specific substrate they implicitly target.
- A model aligned to HNOCA-style projection may still be weak on skeletal multi-omic regulatory structure.
- A model that predicts perturbation endpoints well may still be far from the Perturbation Cell Atlas vision of broad causal coverage.
- A model that performs strongly on pooled metrics may still miss the region-specific structure visible in primary developmental atlases.

## Bottom Line

- The collection now contains multiple distinct biological spaces that can function as supervision, benchmarking, or future atlas targets.
- `Reference substrate` in this collection therefore means more than `background atlas`.
- It can mean queryable projection space, multimodal developmental scaffold, primary trajectory benchmark, or causal perturbation roadmap.
- Keeping those substrate types separate makes later model comparison much clearer.

## Sources Used

- [An integrated transcriptomic cell atlas of human neural organoids](../sources/he_2024_an_integrated_transcriptomic_cell_atlas.md)
- [A multi-omic atlas of human embryonic skeletal development](../sources/to_2024_a_multi-omic_atlas_of_human.md)
- [Single-cell genomics reveals region-specific developmental trajectories underlying neuronal diversity in the human hypothalamus](../sources/herb_2023_single-cell_genomics_reveals_region-specific_developmental.md)
- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md)
- [HNOCA](../entities/HNOCA.md)
- [Transcriptomic Fidelity Benchmarking](../concepts/transcriptomic-fidelity-benchmarking.md)
- [Multi-Omic Developmental Atlases](../concepts/multi-omic-developmental-atlases.md)
- [Region-Specific Developmental Trajectories](../concepts/region-specific-developmental-trajectories.md)
- [Perturbation Cell Atlas](../concepts/perturbation-cell-atlas.md)
