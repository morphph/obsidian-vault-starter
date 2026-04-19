---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, principle, context-management, agentic]
---

# Resolvers

## Summary
[[garry-tan|Garry Tan]]'s name for a routing table over context: "when task type X appears, load document Y first." Skills tell the model **how**. Resolvers tell it **what to load and when**. Solves the CLAUDE.md bloat problem and lets you keep tens of thousands of lines of knowledge accessible without polluting the context window.

## Details

### The pattern
A developer changes a prompt.
- Without a resolver: they ship it.
- With a resolver: the model reads `docs/EVALS.md` first, which says "run the eval suite, compare scores, if accuracy drops more than 2%, revert and investigate." The developer didn't know the eval suite existed. The resolver loaded the right context at the right moment.

### The canonical implementation: skill descriptions
[[claude-code]] has a built-in resolver. Every skill has a `description` field, and the model matches user intent to skill descriptions automatically. **You never have to remember that `/ship` exists. The description is the resolver.**

### Garry's confession (the CLAUDE.md anti-pattern)
- Original CLAUDE.md: 20,000 lines of every quirk, pattern, lesson he'd encountered.
- Symptom: model attention degraded. Claude Code itself told him to cut it back.
- Fix: ~200 lines, just *pointers to documents*. The resolver loads the right one when it matters.
- Result: 20,000 lines of knowledge stays accessible on demand, without polluting context.

### Direct application to this vault
This wiki already implements the resolver pattern in two ways:
1. **`.claude/rules/{name}.md` with `paths:` glob** (per `CLAUDE.md` Documentation Layers table) — rules auto-load only when relevant files are edited. Examples already in use: `wiki-page-format.md` (paths: `wiki/**`), `log-format.md` (paths: `wiki/log.md`).
2. **Skill descriptions on slash commands** — the `/ingest`, `/draft`, `/query`, `/lint`, `/visualize`, `/ingest-anthropic-daily` descriptions in `.claude/commands/` are the resolver entries the model matches against intent.
3. **`wiki/index.md`** itself — a one-line-summary catalog. The model loads it cheaply, then fetches only the linked pages it needs. [[index-over-rag]] is the same principle at the retrieval layer.

### Why resolvers beat shoving everything into context
- Attention is the scarce resource ([[context-noise-governance]]).
- 200 lines of pointers + on-demand loads beats 20,000 lines always-loaded.
- Aligns with [[context-management]]: the harness manages what enters the window, not just what fits.

## Connections
- Related: [[thin-harness-fat-skills]], [[garry-tan]], [[skill-as-method-call]], [[index-over-rag]], [[context-management]], [[context-noise-governance]], [[documentation-layers]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation |
