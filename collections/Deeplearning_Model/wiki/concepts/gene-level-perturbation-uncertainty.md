# Gene-Level Perturbation Uncertainty

## Definition

- Gene-level perturbation uncertainty is uncertainty about whether a perturbation truly affects a given gene, in what direction, and with what magnitude.
- In this collection, the concept matters because perturbation models can agree on average predictive correlation while still disagreeing on effect scale, effect direction, or whether an effect is supported strongly enough to trust biologically.

## In This Collection

- [GPerturb](../entities/GPerturb.md) is the clearest direct example: it uses hierarchical Bayesian Gaussian-process modeling and sparsity switches to expose uncertainty over perturbation-effect presence and strength.
- The paper also shows that inferred effects can change materially depending on whether Gaussian or zero-inflated Poisson observation models are used, making uncertainty partly a model-choice issue rather than only a data-noise issue.
- [GEARS](../entities/GEARS.md) is a neighboring case: it outputs a Bayesian uncertainty estimate when graph support for a perturbation is weak, even though its main emphasis is combinatorial extrapolation rather than a fully probabilistic gene-effect decomposition.
- Compared with [Hierarchical Partial Rejection](hierarchical-partial-rejection.md), the question here is not which fallback label to return, but whether a predicted perturbation effect is reliable enough to interpret.
- Compared with [RNA Velocity Modules](rna-velocity-modules.md), the uncertainty target is intervention effect estimation rather than whether inferred temporal dynamics are meaningful.
- Compared with [Transcriptomic Fidelity Benchmarking](transcriptomic-fidelity-benchmarking.md), this is a gene-and-perturbation-level uncertainty mode rather than a system-level reference-coverage diagnosis.

## Claimed Benefits

- Flags fragile perturbation conclusions before they are overinterpreted as biology.
- Helps separate high average prediction correlation from actually trustworthy effect direction and magnitude.
- Supports interpretable analyses of dosage-sensitive and non-monotonic response patterns.

## Caveats

- Uncertainty estimates depend strongly on modeling assumptions, preprocessing choices, and observation model choice.
- Strong uncertainty reporting does not by itself solve broader out-of-distribution generalization.
- Different perturbation models may expose uncertainty in incompatible ways, making direct method comparison difficult.

## Sources

- [GPerturb: Gaussian process modelling of single-cell perturbation data](../sources/xing_2025_gperturb_gaussian_process_modelling_of.md)
- [Predicting transcriptional outcomes of novel multigene perturbations with GEARS](../sources/roohani_2024_predicting_transcriptional_outcomes_of_novel.md)
