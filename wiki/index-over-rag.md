---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, harness-engineering, retrieval]
---

# Index Over RAG

## Summary
At personal knowledge base scale (50-500 articles), an LLM reading a structured index.md outperforms vector similarity (RAG) for retrieval. The LLM understands what you're really asking; cosine similarity just finds similar words. RAG becomes necessary at ~2,000+ articles when the index exceeds the context window.

## Details
- Karpathy's original insight, validated by [[claude-memory-compiler]] implementation
- The index.md approach: every article listed with one-line summary, organized by category. LLM reads index first, selects relevant pages, reads them in full.
- Why it works: LLM can reason about relevance ("this question is about auth patterns" → selects auth-related articles even if the question doesn't contain the word "auth"). Embeddings can't do this.
- Threshold: ~2,000+ articles / ~2M+ tokens → index too large for context → add hybrid RAG (keyword + semantic search)
- This wiki uses this pattern: `wiki/index.md` is the retrieval mechanism for `/query`
- Recommended tool at scale: qmd by Tobi Lutke (local markdown search, BM25 + vector, LLM re-ranking)

## Connections
- Related: [[compiler-analogy]], [[context-management]], [[claude-memory-compiler]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation |
