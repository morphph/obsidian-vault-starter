---
type: entity
created: 2026-04-19
last-updated: 2026-04-21
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
tags: [wiki, product, open-source, knowledge-base, agentic]
---

# GBrain

## Summary
[[garry-tan|Garry Tan]]'s open-source **knowledge-base scaffold** for a personal agent (github.com/garrytan/gbrain, **9,718 stars** as of 2026-04-21, TypeScript, PGLite/Postgres+pgvector hybrid RAG). Ships with the [[resolvers|resolver]] pattern built in: `gbrain init` creates `RESOLVER.md`, a filing decision tree, and disambiguation rules so the agent starts filing correctly from day one. Includes [[check-resolvable]] as **real TypeScript code** (`src/core/check-resolvable.ts`). Paired with [[gstack]] (the coding/skills layer) and runs inside [[openclaw|OpenClaw]] or Hermes Agent (the thin harness). Production scale: **17,888 pages, 4,383 people, 723 companies, 21 crons, built in 12 days.**

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
Runs in production on his personal agent. Processes **200 inputs/day**. Has **25,000 files** (17,888 pages in brain + other artifacts). Compounds.

### What the repo actually contains (2026-04-21 Deep Scan)

**Core architecture:**
- `src/core/operations.ts` — Contract-first: 41 shared operations. CLI + MCP server generated from this single source.
- `src/core/engine-factory.ts` — Pluggable: PGLite (embedded Postgres via WASM, zero-config default) OR Postgres + pgvector (Supabase).
- `src/core/check-resolvable.ts` — **The check-resolvable meta-skill as real code.** Reachability + MECE overlap + DRY checks. `DRY_PROXIMITY_LINES = 40`. `extractDelegationTargets()` parses `> **Convention:**`, `> **Filing rule:**`, inline backticks.
- `src/core/dry-fix.ts` — `gbrain doctor --fix` engine. Rewrites inlined rules → `> **Convention:** see [path](path).` callouts. Five guards (working-tree-dirty, no-git-backup, inside-code-fence, already-delegated, ambiguous).
- `src/core/minions/` — Postgres-native job queue. Deterministic work routing (see below).

**Resolver artifacts:**
- `skills/RESOLVER.md` — the trigger → skill table (pure markdown)
- `skills/_brain-filing-rules.md` — **Manidis fix in production form**: a table of `Wrong | Right | Why` misfiling patterns + Iron Law of Back-Linking + Citation Requirements
- `skills/_output-rules.md` — deterministic output standards
- `skills/manifest.json` — machine-readable skill registry `{name, path, description}`
- `skills/conventions/{quality,brain-first,model-routing,test-before-bulk,cross-modal,subagent-routing}.md` — cross-cutting rules every skill imports

**26 skills organized by RESOLVER.md:**
- **Always-on:** signal-detector (every message), brain-ops (every read/write)
- **Content ingestion:** ingest (router), idea-ingest (links/tweets), media-ingest (video/audio/PDF), meeting-ingestion
- **Brain ops:** enrich, query, maintain, citation-fixer, repo-architecture, publish, data-research
- **Operational:** daily-task-manager, daily-task-prep, cron-scheduler, reports, cross-modal-review, webhook-transforms, testing, skill-creator, minion-orchestrator
- **Identity & setup:** soul-audit (6-phase interview → SOUL.md/USER.md/ACCESS_POLICY.md/HEARTBEAT.md), setup, migrate, briefing

### Minions — latent vs deterministic at runtime
GBrain's built-in job queue embodies [[latent-vs-deterministic]]. The auto-routing rule (`minion_mode: pain_triggered`):
- **Deterministic** (same input → same steps → same output) → Minions (Postgres-native, **$0 tokens**, millisecond runtime)
- **Judgment** (requires assessment or decision) → Sub-agents (LLM, tokens, seconds)

Production benchmark (pulling a month of social posts):
| | Minions | sessions_spawn (sub-agent) |
|---|---|---|
| Wall time | **753ms** | >10,000ms (gateway timeout) |
| Token cost | **$0.00** | ~$0.03/run |
| Success rate | 100% | 0% |

### BrainBench v1 — measured win over vector search / grep
- Recall@5: 83% → **95%** (+12 pt)
- Precision@5: 39% → **45%**
- Graph-only F1: **86.6%** vs grep's 57.8% (+28.8 pt)
- Corpus: 240-page Opus-generated rich-prose

Why: **self-wiring knowledge graph**. Every page write extracts entity references and creates typed links (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with **zero LLM calls**. Hybrid search: vector + keyword + RRF + multi-query expansion + dedup.

### SKILL.md contract (stricter than Anthropic baseline)
GBrain's SKILL.md frontmatter:
```yaml
---
name: xxx
version: 1.0.0
description: |
  ...
triggers:          # explicit array (vs Anthropic's free-text description)
  - "phrase 1"
  - "phrase 2"
tools:
  - op1
mutating: true
---

## Contract (what this skill guarantees)
## Phases (numbered steps)
## Output Format
## Anti-Patterns (what to never do)
```

`skills/testing/SKILL.md` enforces this structure — three-way integrity between `manifest.json`, `RESOLVER.md`, and every `SKILL.md`. See [[trigger-evals]].

### Connection to [[agent-skills-standard]]
GBrain implements the Agent Skills standard + adds:
- Explicit `triggers: []` array (canonical phrases)
- `RESOLVER.md` as a deterministic routing table layered on top of description-matching
- `manifest.json` registry
- Mandatory skill-body structure (Contract/Phases/Output Format/Anti-Patterns)
- Built-in audit tools (check-resolvable, doctor --fix)

The Anthropic standard is minimal; GBrain is opinionated. Both are valid.

### Relationship to this wiki
This vault is philosophically the same thing at a smaller scale: immutable `raw/`, LLM-compiled `wiki/`, flat structure with [[index-over-rag]]. GBrain is a more opinionated scaffold — it enforces the resolver pattern and ships [[check-resolvable]]. Potential inspiration for hardening this vault's ingest skills ([[resolvers]], [[context-rot]]).

## Connections
- Related: [[garry-tan]], [[gstack]], [[openclaw]], [[resolvers]], [[check-resolvable]], [[trigger-evals]], [[context-rot]], [[agent-skills-standard]], [[thin-harness-fat-skills]], [[latent-vs-deterministic]], [[index-over-rag]], [[two-pipeline-architecture]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Major expansion from GitHub Deep Scan: 9,718 stars; 17,888 pages/4,383 people/723 companies production scale; 26 skills; real TS code for check-resolvable & dry-fix; Minions job queue; BrainBench numbers; stricter SKILL.md contract; pluggable PGLite/Postgres engine |
