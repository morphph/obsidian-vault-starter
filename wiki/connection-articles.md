---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, system-design, pattern]
---

# Connection Articles

## Summary
Pattern where cross-cutting insights linking 2+ concepts are promoted from metadata (a "Related:" section) to first-class standalone articles. The connection itself has unique content — the insight, the evidence, the non-obvious relationship — that doesn't belong to either concept alone.

## Details
- Implemented in [[claude-memory-compiler]] as `knowledge/connections/` directory
- Each connection article has: title, which concepts it connects, the key insight, evidence from source material, bidirectional links
- Example: "Context Anxiety and Self-Evaluation Bias are two symptoms of the same root cause — LLM self-awareness distortion in long tasks." This insight belongs to neither page individually.
- Contrast with current wiki approach: connections listed as bullet points in `## Connections` section. Works for simple "related to" links, but loses the insight.
- Connection articles compound: they become queryable via index, visible in Obsidian graph view as bridge nodes, and discoverable by future ingests
- The old /connect command (now archived) generated similar outputs but filed them in agent-output/ (ephemeral). Connection articles are permanent wiki knowledge.

## Connections
- Related: [[claude-memory-compiler]], [[compiler-analogy]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-repo-claude-memory-compiler.md | Initial creation |
