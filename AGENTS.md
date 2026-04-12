# Agent Schema For `paper_collect`

This repository is a persistent research wiki maintained by Codex.
It may contain multiple topic-specific collections under `collections/`.

## Mission

Turn a growing pile of raw sources into interlinked Markdown knowledge bases that compound over time.

## Repository Contract

- Work inside one collection at a time. A collection root is usually `collections/<collection>/`.
- Within a collection, `raw/` is immutable source material. Read from it, never edit it.
- Within a collection, generated helper artifacts may live under `raw/derived/`, but they never replace the original source of truth in `raw/sources/`.
- Within a collection, `wiki/` is LLM-owned working knowledge. Create, update, reorganize, and cross-link pages there.
- For collection-scoped questions, use only that collection's `wiki/` and `raw/` as the knowledge base unless the user explicitly asks for outside knowledge or web research.
- Do not fill gaps with model priors. If the collection does not support the answer, say that the information is not present in the knowledge base.
- `wiki/index.md` is the content catalog. Keep it current.
- `wiki/log.md` is append-only chronology. Record ingests, queries, and lint passes.
- `README.md` explains the human workflow.
- Do not mix unrelated topics across collections.
- Off-topic or casual questions should be answered in chat only unless the user explicitly asks to save them.

## Directory Rules

- `collections/<collection>/raw/sources/`: papers, articles, transcripts, notes, exports, datasets, or images
- `collections/<collection>/raw/assets/`: local images or attachments referenced by sources
- `collections/<collection>/raw/derived/`: parser outputs or other generated helper artifacts derived from raw sources
- `collections/<collection>/wiki/sources/`: one page per raw source
- `collections/<collection>/wiki/entities/`: people, organizations, tools, places, or named systems
- `collections/<collection>/wiki/concepts/`: themes, methods, debates, patterns, or claims
- `collections/<collection>/wiki/queries/`: saved question-driven analyses
- `collections/<collection>/wiki/syntheses/`: larger writeups, comparisons, briefs, or literature reviews

## Ingest Workflow

When asked to ingest a source inside a collection:

1. Read the relevant raw source from `raw/sources/`.
2. If layout extraction is difficult and helper artifacts exist in `raw/derived/`, use them as support context, but keep the original raw source as the final source of truth.
3. Create or update a matching page in `wiki/sources/`.
4. Extract important entities and concepts into their own pages when useful.
5. Update existing pages if the source strengthens, refines, or contradicts prior knowledge.
6. Add or refresh cross-links between related pages.
7. Update `wiki/overview.md` if the top-level picture changed.
8. Update `wiki/index.md`.
9. Append an entry to `wiki/log.md`.

## Query Workflow

When asked a question about a collection:

1. Read `wiki/index.md` first.
2. Open the most relevant wiki pages, not every raw source by default.
3. Answer only from the current collection knowledge base. Do not add unsupported outside facts from memory.
4. If the relevant wiki pages do not contain enough information, open the most relevant raw source files and, when helpful, any derived helper artifacts in `raw/derived/` for the same source. Use them to repair or enrich the wiki before answering.
5. If the answer still cannot be supported after checking the relevant wiki pages, raw sources, and any relevant helper artifacts, explicitly say the information is not available in the knowledge base.
6. Cite the wiki pages and raw sources used when practical.
7. Offer to save substantial answers to `wiki/queries/` or `wiki/syntheses/`.
8. Save the answer in `wiki/queries/` or `wiki/syntheses/` only when the user explicitly asks to save it or when the request clearly asks for a persistent writeup.
9. Update `wiki/log.md` only when wiki files were actually created or edited.

## Lint Workflow

When asked to lint the wiki:

- look for stale claims
- flag contradictions
- find broken or missing cross-links
- identify duplicate or near-duplicate pages
- suggest merges, redirects, or consolidations for overlapping wiki pages
- identify important concepts without dedicated pages
- identify orphan pages
- suggest missing sources or follow-up questions

## Writing Conventions

- Use Markdown only.
- Prefer short, dense sections over long narrative blocks.
- Use relative links inside `wiki/`.
- Make uncertainty explicit.
- Separate observations, claims, evidence, and open questions when possible.
- Preserve chronology in `wiki/log.md`.
- Never silently delete important claims; rewrite them with better sourcing or mark them as superseded.
