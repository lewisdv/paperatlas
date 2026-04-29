---
title: Orthrus: toward evolutionary and functional RNA foundation models
kind: paper
status: ingested
added: 2026-04-29T22:21:17+09:00
raw_source: raw/sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.pdf
---

# Orthrus: toward evolutionary and functional RNA foundation models

## Source

- File: [raw/sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.pdf](../../raw/sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.pdf)
- Added: 2026-04-29T22:21:17+09:00
- Venue/status: Nature Methods article; accepted 13 March 2026, with the extracted PDF still showing an unresolved published-online placeholder
- Authors: Philip Fradkin, Ruian "Ian" Shi, Taykhoom Dalal, Keren Isaev, Brendan J. Frey, Leo J. Lee, Quaid Morris, and Bo Wang
- DOI: `10.1038/s41592-026-03064-3`

## Summary

This paper introduces Orthrus, a mature RNA foundation model that replaces generic masked-token-style genomic pretraining with biologically motivated contrastive pretraining over splice isoforms and orthologous transcripts. Orthrus uses a Mamba encoder and learns RNA representations that group transcripts by evolutionary and functional similarity, then transfers those embeddings to mRNA property prediction tasks with strong data efficiency. In this collection, the paper matters because it extends the foundation-model thread beyond single-cell transcriptomes into mature RNA sequence modeling and argues that biological augmentations can outperform scale-only strategies.

## Methods

- Orthrus is pretrained with contrastive learning rather than pure reconstruction, using positive transcript pairs derived from alternative splicing and orthology.
- The splice augmentation set is built from GENCODE and RefSeq annotations across ten metazoan organisms, and the orthology augmentation set uses TOGA alignments spanning more than `400` mammalian species.
- A Mamba encoder maps transcripts to embeddings, and a decoupled contrastive loss maximizes similarity for positive pairs while pushing apart unrelated transcripts.
- The paper evaluates linear probing and fine-tuning on mature RNA property tasks including mRNA half-life, localization, translational efficiency, protein localization, and isoform function-related settings.
- Three Orthrus variants are described, including a `10.1` million parameter model and a joint contrastive-plus-MLM variant, enabling comparison between biologically motivated contrastive pretraining and more standard self-supervised objectives.

## Key Claims

- Biologically informed contrastive pretraining yields more useful RNA representations than generic reconstruction objectives borrowed from NLP.
- Mature RNA foundation models can be highly parameter-efficient when pretraining focuses on function-preserving biological variation rather than generic token recovery.
- Orthrus representations transfer well in low-data regimes, reducing the amount of labeled data needed for downstream RNA property prediction.
- Isoform-level embeddings can capture divergent transcript function within the same gene, which is a long-standing challenge for RNA annotation.

## Evidence

- The source reports pretraining over `32` million unique transcripts and more than `887` million unique positive pairs constructed from splicing and orthology augmentations.
- Orthrus is described as outperforming most other self-supervised foundation models on mature mRNA property prediction tasks, with a linear probe even exceeding supervised baselines on the reported tasks.
- The paper highlights a low-data result where Orthrus needs as few as `30` labeled examples to fine-tune an mRNA half-life predictor.
- The model uses only `10.1` million parameters in its main form yet is reported to achieve state-of-the-art performance with orders-of-magnitude fewer parameters than many larger genomic foundation models.
- The authors also show that Orthrus embeddings can group RNA isoforms by common function and distinguish divergent isoform biology within a gene.

## Limitations

- The extracted PDF still shows an unresolved published-online placeholder, so the final online-publication date is not recoverable from the current collection source.
- The work is centered on mature RNA sequence properties, not on multimodal cellular state modeling or perturbation-response simulation.
- Its biological contrastive pairs rely on assumptions that splice isoforms and orthologs are usually more functionally similar than random transcripts, which may not hold uniformly for every transcript family.
- The paper positions Orthrus against other genomic foundation models, but the collection does not currently contain all those baselines as full source pages for direct within-collection comparison.

## Related Pages

- [Orthrus](../entities/Orthrus.md)
- [Evolutionary Contrastive RNA Pretraining](../concepts/evolutionary-contrastive-rna-pretraining.md)
- [Super Transformer Architecture](../concepts/super-transformer-architecture.md)

## Open Questions

- How far can biologically motivated contrastive pretraining go before multimodal or perturbation-aware objectives become necessary for downstream transfer?
- Should this collection treat Orthrus as a sequence-foundation-model branch parallel to single-cell foundation models, or as part of the same broader design space?
- If more RNA-centric sources arrive, does this collection need a dedicated synthesis separating cell-state models from transcript-property models?

<!-- opendataloader:begin -->
## Parsed Artifacts

- Parser: OpenDataLoader PDF
- Generated: 2026-04-29T22:20:30+0900
- Command: `/bin/zsh -lc 'export JAVA_HOME=/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home; export PATH=/usr/local/opt/openjdk@21/bin:$PATH; /Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/.venv-opendataloader/bin/opendataloader-pdf "/Users/davin/Library/CloudStorage/Dropbox/LLM_wiki/collections/Deeplearning_Model/raw/sources/Philip_2026_Orthrus_toward_ evolutionary_and_functional.pdf" -o /tmp/odl-check-orthrus -f markdown --use-struct-tree --image-output off -q'`
- Manifest: [raw/derived/opendataloader/Philip_2026_Orthrus_toward_ evolutionary_and_functional/opendataloader-run.json](../../raw/derived/opendataloader/Philip_2026_Orthrus_toward_ evolutionary_and_functional/opendataloader-run.json)
- Output: [raw/derived/opendataloader/Philip_2026_Orthrus_toward_ evolutionary_and_functional/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md](../../raw/derived/opendataloader/Philip_2026_Orthrus_toward_ evolutionary_and_functional/Philip_2026_Orthrus_toward_ evolutionary_and_functional.md)

These parsed files are helper artifacts. Treat the original raw PDF as the source of truth.
<!-- opendataloader:end -->
