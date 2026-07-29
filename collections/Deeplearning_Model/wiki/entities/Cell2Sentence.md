# Cell2Sentence

## Type

- Framework / representation and fine-tuning method

## Definition

- Cell2Sentence (`C2S`) converts a normalized single-cell transcriptome into a sequence of gene names ordered by decreasing expression.
- Ordinary causal language models can then be fine-tuned on those `cell sentences` together with metadata prompts and biological prose.
- The original 2024 paper demonstrates the framework with GPT-2 and Pythia. It is the predecessor of the later [C2S-Scale](C2S-Scale.md) model family.

## Core Method

- Rank genes within each cell and serialize the ranked gene names as text tokens.
- Mix the sequence with natural-language conditions or labels for generation and prediction tasks.
- Use a dataset-specific log-rank regression to approximately reconstruct expression values from a generated sequence.
- Fine-tune pretrained language models for cell generation, multipart label prediction, and abstract-like text generation.

## Reported Uses

- Conditional and unconditional cell generation.
- Cell-type and combinatorial metadata prediction in natural language.
- Held-out cytokine-condition generation.
- Generating biological prose from a cell sentence.

## Caveats

- Exact expression is discarded and only approximately reconstructed.
- GPT-2 experiments truncate cells to the top `100` genes.
- Generated gene sequences require invalid-token and duplicate handling.
- Abstract-like outputs can sound biologically plausible without being factually reliable.
- The original paper is a proof of concept and has no wet-lab validation.

## Related

- [Cell Sentences](../concepts/cell-sentences.md)
- [C2S-Scale](C2S-Scale.md)
- [Source: Cell2Sentence: Teaching Large Language Models the Language of Biology](../sources/levine_2024_cell2sentence_teaching_llms_biology.md)
