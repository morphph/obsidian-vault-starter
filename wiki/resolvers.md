---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
tags: [wiki, principle, context-management, agentic, governance]
---

# Resolvers

## Summary
[[garry-tan|Garry Tan]]'s name for a routing table over context: "when task type X appears, load document Y first." Skills tell the model **how**. Resolvers tell it **what to load and when**. Solves the CLAUDE.md bloat problem. Garry's follow-up article (2026-04-15) reframes resolvers as the **governance layer of an agent system** — the org chart, the filing clerk, and the linter — and introduces the companion patterns: [[trigger-evals]], [[check-resolvable]], [[context-rot]], and the idea of a **self-healing resolver** that learns from its own traffic.

## Details

### The one-sentence definition
> A resolver is a routing table for context. When task type X appears, load document Y first.

Invisible when it works. Catastrophic when it doesn't.

### Garry's CLAUDE.md confession (the anti-pattern)
- Original CLAUDE.md: **20,000 lines** of every quirk, pattern, lesson he'd encountered with Claude Code
- Symptom: model attention degraded; responses got slower and less precise; Claude Code itself told him to cut it back ("when the AI is telling *you* to stop talking, you've gone too far")
- Fix: ~200 lines. A numbered decision tree. Pointers to documents.
- Walk the tree: Is it a person? → `/people/`. A company? → `/companies/`. Policy analysis? → `/civic/`.
- **20,000 lines of knowledge stays accessible on demand, without polluting the context window.**
- Result: faster responses, more accurate filing, fewer hallucinations. *Not because the model got smarter. Because Garry stopped blinding it with noise.*

### Resolvers are fractal
Resolvers compose. They exist at every layer of the system, not just the top:

| Layer | Document | What it maps |
|-------|----------|--------------|
| **Skill resolver** | `AGENTS.md` | Task types → skill files |
| **Filing resolver** | `RESOLVER.md` | Content types → directories |
| **Context resolver** | Inside each skill | Sub-routing within a skill (email triage vs. scheduling vs. signature tracking) |

[[claude-code]] has this pattern already: every skill has a `description` field and the model matches user intent to descriptions automatically. You never have to remember that `/ship` exists. **The description *is* the resolver.** It's resolvers all the way down.

### The misfiling that revealed everything (the Manidis story)
Garry asked his agent to ingest Will Manidis's essay "No New Deal for OpenAI" — a policy analysis of OpenAI's industrial policy brief.
- Agent filed it in `sources/`. **Wrong** — `sources/` is for raw dumps (CSVs, API exports). This was policy analysis, belongs in `civic/`.
- Root cause: idea-ingest skill had hardcoded `brain/sources/` as default. It didn't consult the resolver.
- **Audit: 13 brain-writing skills, only 3 referenced the resolver. The other 10 had their own hardcoded filing logic.**
- Fix was not fixing 10 skills individually (whack-a-mole). Fix was:
  1. `_brain-filing-rules.md` — shared filing rules doc cataloging common misfilings
  2. Two-line mandate at the top of every brain-writing skill: *Before creating any new brain page, read `brain/RESOLVER.md` and `skills/_brain-filing-rules.md`. File by primary subject, not by source format or skill name.*
- Result: **zero misfilings since**.

### The invisible skill problem
A skill that exists but has no trigger in the resolver is **worse than a missing skill** — it creates the illusion of capability. Garry's example: the executive-assistant skill had a signature tracker (worked perfectly), but the resolver had no trigger for "check my signatures" or "what do I need to sign." Like having a surgeon on staff but not in the hospital directory.

Remedy: [[check-resolvable]] — weekly reachability audit. First run on Garry's 40+ skills: **6 unreachable (15% dark capability)**. Fixed in an hour by adding triggers to `AGENTS.md`.

### Context rot: resolvers decay
See [[context-rot]]. Day 1 the resolver is perfect; Day 90 it's a historical document. New skills get built by sub-agents, user phrasings drift from descriptions, capabilities go dark. The system still works — but only because the builder knows which skill to call. That's a person with a filing cabinet, not a system.

### The governance stack over a resolver
| Layer | Purpose | Cost |
|-------|---------|------|
| [[resolvers|Resolver]] (doc) | The routing table | 200 lines of markdown |
| [[trigger-evals]] | Does the right skill fire for real inputs? | 50-test eval suite |
| [[check-resolvable]] | Is every skill *reachable* at all? | Weekly cron |
| Self-healing RLM (forward-looking) | Table rewrites itself from observed traffic | Not yet fully built |

### The self-healing resolver (forward-looking)
A YC CTO asked Garry in office hours: *"Could an RLM be used to solve context rot particularly around resolvers?"*

The idea: observe every task dispatch (which skill fired / didn't / matched wrong), and nightly rewrite the resolver from the traffic evidence. Eight hundred dispatches over a month → the system sees "is my flight on time" never triggers flight-tracker but "check my flight" does; it rewrites the trigger description. **Not a human maintaining a table. The table maintaining itself.**

[[claude-code]]'s [[dreaming|AutoDream]] memory-consolidation system is a primitive version — it reviews accumulated context and compresses it. Apply the principle to the resolver specifically and you get a routing table that improves with use. **"A resolver that learns from its own traffic. That's the endgame for agent governance."**

### Resolvers as management (the reframe)
The final move in Garry's article: the technical framing (routing tables, context loading) is **too small**. What he actually built is closer to management:

| Primitive | Management analogue |
|-----------|---------------------|
| Skills | Employees (specialists, generalists, cron-only) |
| Resolver | Org chart + escalation logic |
| Filing rules | Internal process (where information lives) |
| [[check-resolvable]] | Audit & compliance (can the org do what it claims?) |
| [[trigger-evals]] | Performance reviews (does the right part respond?) |

> The problem isn't that models aren't smart enough. The problem is that we've been building organizations with no management layer. Just a pile of talented employees and a vague hope they'll coordinate. Resolvers are that missing layer.

### Why resolvers beat shoving everything into context
- Attention is the scarce resource ([[context-noise-governance]])
- 200 lines of pointers + on-demand loads beats 20,000 lines always-loaded
- Aligns with [[context-management]]: the harness manages what enters the window, not just what fits

### Direct application to this vault
This wiki already implements the resolver pattern in three ways:
1. **`.claude/rules/{name}.md` with `paths:` glob** (per `CLAUDE.md` [[documentation-layers]]) — rules auto-load only when relevant files are edited. Examples: `wiki-page-format.md` (`paths: wiki/**`), `log-format.md` (`paths: wiki/log.md`).
2. **Skill descriptions on slash commands** — the `/ingest`, `/draft`, `/query`, `/lint`, `/visualize`, `/ingest-anthropic-daily` descriptions in `.claude/commands/` are the resolver entries.
3. **`wiki/index.md`** — a cheap catalog the model loads first, then fetches only what it needs. [[index-over-rag]] at the retrieval layer.

**Gaps worth closing (inspired by Garry's 2026-04-15 piece):**
- We have no equivalent of [[check-resolvable]] — no test that every skill is reachable from CLAUDE.md
- We have no [[trigger-evals]] — no test that `/ingest` fires on "save this article" etc.
- The [[context-rot]] risk applies here too: if a slash command is added without updating CLAUDE.md's Commands table, it's effectively dark.

## Connections
- Related: [[trigger-evals]], [[check-resolvable]], [[context-rot]], [[thin-harness-fat-skills]], [[garry-tan]], [[skill-as-method-call]], [[gbrain]], [[gstack]], [[index-over-rag]], [[context-management]], [[context-noise-governance]], [[documentation-layers]], [[dreaming]], [[claude-code]], [[openclaw]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation |
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Major expansion: fractal resolvers, Manidis misfiling story, invisible-skill problem, context rot, governance stack (trigger evals + check-resolvable), self-healing RLM idea, management reframe |
