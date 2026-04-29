# Gene Block Attention

## Definition

- Gene Block Attention is the paper's coarse-grained attention scheme for scRNA-seq modeling.
- Instead of treating each gene as an independent token, it groups semantically related genes into balanced non-overlapping blocks and attends over those blocks.

## Motivation

- The source argues that flat gene-token modeling ignores higher-order biological structure such as shared function or module-level relationships.
- Block-level attention is proposed as a way to preserve more biological context while reducing the burden of naive full-gene attention.

## Construction In SAVE

- Start from cleaned NCBI Gene summary text for each gene.
- Embed the summaries with `text-embedding-ada-002`.
- Use an iterative optimal transport procedure to assign genes into equal-sized semantic blocks.
- Reshape the input expression matrix into an `N x L x K` tensor and run Transformer-style attention over the block dimension.

## Claimed Benefits

- Captures higher-order dependencies among genes.
- Provides a biologically motivated tokenization for conditional generation.
- Supports the paper's reported gains on generation fidelity and robustness in more complex conditional settings.

## Caveats

- The quality of the blocks depends on available text annotations and can inherit historical literature bias.

## Sources

- [SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention](../sources/li_2026_save_a_generalizable_framework_for.md)
