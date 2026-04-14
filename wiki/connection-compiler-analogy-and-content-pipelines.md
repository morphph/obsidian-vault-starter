---
type: concept
created: 2026-04-09
last-updated: 2026-04-09
sources:
  - raw/2026-04-08-session-unknown-0953.md
  - raw/2026-04-08-session-unknown-1421.md
  - raw/2026-04-08-session-unknown-1644.md
tags: [wiki, connection, insight]
---

# Connection: Compiler Analogy × Content Pipelines

## The Connection

The [[compiler-analogy]] was articulated for knowledge management: raw logs = source code, LLM = compiler, wiki = executable. But vfan's own projects reveal the same pattern applies to **any LLM-powered pipeline**, not just knowledge systems.

## Key Insight

Three pipelines in this ecosystem all follow the compiler pattern — and share its failure modes:

| | Source Code | Compiler | Executable | Test Suite |
|--|------------|----------|-----------|------------|
| **Wiki** | `raw/` articles | `/ingest` (LLM) | `wiki/` pages | `/lint` |
| **[[blog2video]]** | Article/tweet | Memo→Narration→Slides (LLM) | `.mp4` video | Human review at narration.md |
| **[[loreai]]** | Keywords + sources | Extraction pipeline (LLM) | Published pages | SEO audit |

The structural parallel runs deep:
- **Immutable sources:** Wiki's `raw/` is never modified; blog2video's source article is fetched once; LoreAI's keyword lists are input-only
- **Multi-pass compilation:** Wiki does entity extraction + concept synthesis + connection discovery. Blog2video does memo → narration → episode splitting → slide planning. Same principle: each pass refines.
- **Deterministic final stage:** Wiki's index update is deterministic. Blog2video's HTML→screenshot→video render is deterministic. LoreAI's page publishing is deterministic. The LLM is only in the middle.

## The Failure Modes Transfer Too

[[silent-fallback-antipattern]] in blog2video is structurally identical to **compiling with corrupted source code:**
- Blog2video: Playwright unavailable → vision transcription of images → pipeline "compiled" but with garbage input → video rendered but shallow
- Wiki equivalent: if `/ingest` fetched a truncated article → entities extracted from partial content → wiki pages created but incomplete
- LoreAI equivalent: LLM-generated content with truncated titles → pages published with bad metadata → SEO damage

The fix is also identical: **validate inputs before compilation**. Blog2video's pre-flight gate = wiki's source verification = LoreAI's slug validation filter. In compiler terms: type-check before compile.

## Where Else This Applies

Any pipeline with the shape `fetch → LLM transform → deterministic render` is a compiler:
- Newsletter generation (sources → LLM curation → formatted email)
- Slide deck generation (outline → LLM expansion → presentation)
- Report generation (data → LLM analysis → PDF)

For each: identify the "source code" (immutable), the "compiler" (LLM passes), the "executable" (output), and the "test suite" (validation). Then ask: what happens if the source is corrupted? If the answer is "it silently degrades," add a pre-flight gate.

## Related Concepts
- [[compiler-analogy]] — The original framework (knowledge systems)
- [[blog2video]] — Video pipeline as compiler
- [[loreai]] — Content platform as compiler
- [[silent-fallback-antipattern]] — The shared failure mode
- [[verification-loops]] — The shared solution (validate before compile)

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-09 | raw/2026-04-08-session-unknown-0953.md, raw/2026-04-08-session-unknown-1421.md, raw/2026-04-08-session-unknown-1644.md | Initial creation — three pipelines as compilers, shared failure modes |
