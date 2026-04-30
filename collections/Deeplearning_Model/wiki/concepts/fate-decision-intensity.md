# Fate Decision Intensity

## Definition

- Fate decision intensity is a score intended to quantify how strongly a cell state shapes downstream lineage choice before overt commitment becomes obvious in marker expression.
- In this collection, it is distinct from later lineage contribution or from simple pseudotime ordering: it is meant to localize early commitment pressure rather than only eventual outcome.

## In This Collection

- [scRL](../entities/scRL.md) is the main source for this concept, deriving decision intensity from the critic's learned state values under an early-biased reward scheme.
- [Cell2fate](../entities/Cell2fate.md) addresses a neighboring problem through RNA-velocity modules and posterior uncertainty, but with a different model family and a different notion of developmental evidence.
- Compared with [Clinical Reinforcement-Learning Translation](clinical-reinforcement-learning-translation.md), this is not a treatment-policy problem but a cell-state scoring problem: RL is used here to localize developmental commitment pressure rather than to recommend actions in patient care.

## Claimed Benefits

- Highlights branch points and pre-expression commitment states that classic pseudotime tools may smooth over.
- Separates early lineage choice from later lineage accumulation or contribution.
- Can be compared with gene-level signals to prioritize candidate regulators of commitment.

## Caveats

- The score depends on the trajectory representation, root-state definition, and reward design rather than on direct experimental observation alone.
- Decision intensity is therefore model mediated and can inherit artifacts from pseudotime construction or grid discretization.

## Sources

- [scRL: Utilizing Reinforcement Learning to Evaluate Fate Decisions in Single-Cell Data](../sources/fu_2025_scrl_utilizing_reinforcement_learning_to.md)
- [Cell2fate infers RNA velocity modules to improve cell fate prediction](../sources/aivazidis_2025_cell2fate_infers_rna_velocity_modules.md)
