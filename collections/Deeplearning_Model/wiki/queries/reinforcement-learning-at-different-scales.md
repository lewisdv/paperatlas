# How does reinforcement learning appear at different scales in this collection?

## Short Answer

- Reinforcement learning appears in this collection in two direct forms, and they operate at very different biological scales.
- [scRL](../entities/scRL.md) uses RL inside a cell-state manifold to score developmental commitment structure.
- [Reinforcement Learning and Its Clinical Applications Within Healthcare: A Systematic Review of Precision Medicine and Dynamic Treatment Regimes](../sources/frommeyer_2025_reinforcement_learning_and_its_clinical.md) treats RL as a patient-level decision-support framework for sequential care.
- The common language is `sequential decision making`, but the objects, rewards, risks, and evaluation constraints are very different.

## 1. RL As Cell-State Trajectory Scoring

- [scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](../sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md) is the clearest direct example of RL applied inside single-cell biology.
- The framework rasterizes a developmental manifold, defines early-biased and late-biased reward schemes, and uses actor-critic learning to estimate decision intensity and contribution intensity.
- In this setting, the `agent` is not choosing a treatment for a patient. It is effectively exploring a state graph of cell transitions and learning which regions look like early commitment points.
- The goal is scientific interpretation of developmental structure, especially branch points and regulators, rather than operational decision deployment.

## 2. RL As Patient-Level Dynamic Treatment Optimization

- [Reinforcement Learning and Its Clinical Applications Within Healthcare: A Systematic Review of Precision Medicine and Dynamic Treatment Regimes](../sources/frommeyer_2025_reinforcement_learning_and_its_clinical.md) shows the second direct scale.
- Here RL is framed around precision medicine, dosing, treatment timing, escalation, and multistage care planning in real clinical workflows.
- The core challenge is not recovering developmental structure but selecting adaptive actions over time for patients under uncertainty.
- Reward design, interpretability, reproducibility, data sufficiency, and workflow integration become central because the outputs are potentially actionable in care settings.

## What Is Shared Across Both Scales

- Both uses treat biology or medicine as sequential rather than static.
- Both rely on the idea that present state matters because it shapes downstream consequences.
- Both are sensitive to reward design: scRL explicitly uses different reward landscapes for early decision versus later contribution, while clinical RL faces the harder problem of defining rewards that align with patient and clinician goals across short and long time horizons.

## What Changes Across The Scales

- In scRL, the state space is a developmental manifold built from transcriptomic data.
- In clinical RL, the state space is a patient care trajectory shaped by diagnoses, monitoring, treatments, and outcomes.
- In scRL, the output is an interpretable score over cell states.
- In clinical RL, the intended output is an action or policy recommendation.
- In scRL, the main risks are representation artifacts, root-state sensitivity, and grid discretization.
- In clinical RL, the main risks are offline bias, poor reward alignment, weak transparency, limited reproducibility, and deployment friction.

## An Important Boundary In This Collection

- The collection also contains adjacent ideas such as [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md) and [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md), both of which discuss iterative experiment-model loops.
- But these are not direct RL applications in the same concrete sense as scRL or the clinical review literature.
- It is useful to keep that boundary clear so the RL label does not get diluted into every feedback-loop or active-learning idea.

## Current Collection Conclusion

- Right now, this collection does not support one unified story of RL across scales.
- It supports a narrower but useful claim: RL is being used both as an interpretive tool for cell-state dynamics and as a policy-learning framework for adaptive clinical care, and the two should not be evaluated with the same standards.
- The main bridge between them is conceptual rather than technical: both ask how to act or score well in a sequential state space, but they answer that question under very different biological and operational constraints.

## Pages Used

- [scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](../sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md)
- [Reinforcement Learning and Its Clinical Applications Within Healthcare: A Systematic Review of Precision Medicine and Dynamic Treatment Regimes](../sources/frommeyer_2025_reinforcement_learning_and_its_clinical.md)
- [Fate Decision Intensity](../concepts/fate-decision-intensity.md)
- [Clinical Reinforcement-Learning Translation](../concepts/clinical-reinforcement-learning-translation.md)
- [How to build the virtual cell with artificial intelligence: Priorities and opportunities](../sources/bunne_2024_how_to_build_the_virtual.md)
- [Toward a foundation model of causal cell and tissue biology with a Perturbation Cell and Tissue Atlas](../sources/rood_2024_toward_a_foundation_model_of.md)
