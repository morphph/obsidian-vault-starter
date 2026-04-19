---
type: entity
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
tags: [wiki, product, open-source, knowledge-base, agentic]
---

# GBrain

## Summary
[[garry-tan|Garry Tan]]'s open-source **knowledge-base scaffold** for a personal agent. Ships with the [[resolvers|resolver]] pattern built in: `gbrain init` creates `RESOLVER.md`, a filing decision tree, and disambiguation rules so the agent starts filing correctly from day one. Includes [[check-resolvable]] as a built-in skill. Paired with [[gstack]] (the coding/skills layer) and runs inside [[openclaw|OpenClaw]] or Hermes Agent (the thin harness). **Repo: github.com/garrytan/gbrain.**

## Details

### What it is
- A git repo + scaffold you `init` into your own knowledge base directory
- Structured filing: `people/`, `companies/`, `civic/`, `sources/`, `originals/` (etc.)
- Encodes the **filing resolver** at the root: `RESOLVER.md`
- Encodes **common misfiling rules** at `skills/_brain-filing-rules.md`
- Includes the [[check-resolvable]] meta-skill out of the box
- **Everything is plain markdown in a git repo you own**. If any piece disappeared tomorrow, your knowledge survives as plain text files.

### Why it exists (the Manidis misfiling story)
Garry's agent misfiled Will Manidis's policy analysis "No New Deal for OpenAI" into `sources/` (raw data dumps) instead of `civic/` (policy analysis). Root cause: the idea-ingest skill had hardcoded `brain/sources/` as the default directory. Of 13 brain-writing skills, only 3 consulted the resolver; the other 10 had hardcoded paths. The fix — a single shared filing-rules doc + a mandate that every skill reads `RESOLVER.md` before creating any page — is the principle GBrain ships with.

### Architecture slot (in the Garry Tan stack)
| Layer | Project | Role |
|-------|---------|------|
| Harness | [[openclaw|OpenClaw]] / Hermes Agent | Thin CLI loop |
| Skills | [[gstack]] | Fat markdown skills, 72K+ stars |
| **Knowledge** | **GBrain** | **Resolver + filing rules + compiled memory** |

Your agent reads GBrain's compiled truth before answering. Your crons run rollup pipelines into GBrain while you sleep.

### What's built in from day 1
- `RESOLVER.md` — the filing decision tree
- `skills/_brain-filing-rules.md` — documented misfiling patterns (sources vs. originals, people vs. companies, civic vs. sources)
- [[check-resolvable]] — weekly reachability audit
- Two-line mandate template for any brain-writing skill: *Before creating any new brain page, read `brain/RESOLVER.md` and `skills/_brain-filing-rules.md`. File by primary subject, not by source format or skill name.*

### Garry's claim about scale
Runs in production on his personal agent. Processes **200 inputs/day**. Has **25,000 files**. Compounds.

### Relationship to this wiki
This vault is philosophically the same thing at a smaller scale: immutable `raw/`, LLM-compiled `wiki/`, flat structure with [[index-over-rag]]. GBrain is a more opinionated scaffold — it enforces the resolver pattern and ships [[check-resolvable]]. Potential inspiration for hardening this vault's ingest skills ([[resolvers]], [[context-rot]]).

## Connections
- Related: [[garry-tan]], [[gstack]], [[openclaw]], [[resolvers]], [[check-resolvable]], [[trigger-evals]], [[context-rot]], [[thin-harness-fat-skills]], [[index-over-rag]], [[two-pipeline-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
