---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-10-khairallah-how-to-master-context-engineering.md
tags: [wiki, principle, context-engineering, personal-ai, agentic]
---

# Four-Files Context Architecture

## Summary
[[eng-khairallah|Khairallah]]'s minimalist context-engineering primitive: **maintain four persistent files** — **Identity / Audience / Standards / Project** — and load them at the start of every AI session. Solves the "re-explaining yourself every conversation" productivity leak with the smallest possible architecture. **One-tier-down version of [[gbrain]] / [[filing-cabinet-vs-nervous-system|nervous-system]] approach**: if you can't build a knowledge graph today, build these four files this week.

## Details

### The four files (each under ~2,000 words)

| File | Content | Update cadence |
|------|---------|----------------|
| **Identity** | Who you are. What you do. Expertise. Background. Communication style. | Rarely (career change) |
| **Audience** | Who you create for. Demographics, psychographics, knowledge level, pain points, goals, language they use. | Occasionally (new segment) |
| **Standards** | What good looks like. Quality criteria, formatting preferences, tone guidelines, anti-patterns. Examples of excellent and terrible work. | Periodically (after major learnings) |
| **Project** | What you're working on **right now**. Current goals, active projects, recent decisions, open questions, deadlines. | **Weekly to monthly** — the dynamic layer |

### Why exactly these four
- **Identity + Audience** = the *role-mapping*. Who's writing for whom.
- **Standards** = the *quality bar*. What the output should look like.
- **Project** = the *current context*. What's actually happening this week.

Together they cover Khairallah's framing: *"the model already knows everything it needs to know"* — without exhaustively pre-loading every detail of your work.

### Where they fit in the [[context-management|three-layer context model]]

| Context layer | What sits there |
|---------------|------------------|
| Layer 1 — Immediate (your prompt) | Today's request |
| Layer 2 — Session (within one chat) | Uploaded files, system instructions, in-conversation references |
| **Layer 3 — Persistent (cross-session)** | **The Four Files (+ memory documents, knowledge base, etc.)** |

**Most people only use Layer 1.** The four-files architecture is the smallest possible Layer 3 implementation that produces measurable quality improvement.

### The "context loading rules" extension

After you have the four files, **don't load all four for every task**. Define per-work-type loading rules:

| Work type | Files to load |
|-----------|---------------|
| **Writing** | Identity + Audience + Standards + format-specific examples |
| **Analysis** | Identity + Project + raw data + previous analysis |
| **Research** | Project + research methodology + existing related research |
| **Strategy** | All four + competitive landscape + industry data |

> "A surgeon doesn't review every medical textbook before every operation. They review the specific patient file, procedure notes, imaging results. They load **relevant** context, not all context."

This is the [[resolvers|resolver]] pattern applied to context loading: same primitive (route by task type to right inputs), simpler implementation (no `RESOLVER.md` needed — just a doc that maps work types to files).

### How this fits in the wiki's existing stack

| Tier | Pattern | Source |
|------|---------|--------|
| **Personal mini** | **Four-Files (this page)** | Khairallah |
| **Personal full** | [[gbrain|GBrain]] with RESOLVER.md + skills + crons | Garry Tan |
| **Enterprise** | [[system-of-intelligence]] | a16z (Steph Zhang) |

All three are **the same primitive at different scales**: persistent context + dynamic loading + agentic execution. **Four-Files is the version anyone can build this weekend.**

### Why "weekly Project update" is the load-bearing habit

Identity / Audience / Standards barely change. **The Project file is what makes the system stay alive.** Without weekly updates:
- The model lags reality
- "Current goals" become stale → its prioritization breaks
- The architecture decays into static-file storage

**Treat the Project file like a brief you'd write for an incoming consultant** — update it weekly, prune what's done, add what's new.

### Where it falls short of [[gbrain]]
- **No automatic entity propagation** — when you mention a new person/company, the system doesn't update their file
- **Manual loading per session** — no `RESOLVER.md` doing the routing
- **No verification / audit** — no [[check-resolvable]] equivalent
- **No multi-source ingest** — calendar, email, meetings don't write back

But it has one decisive advantage: **anyone can implement it in a weekend with text files.** That's why it's the right starting point for mass-market builders.

### Practical implementation for this vault
Our existing wiki already has the bones of Identity (CLAUDE.md), Standards (`.claude/rules/`), and Project (the `wiki/log.md` recent ingests). What's missing:
- An explicit **Audience file** — who is the output for? (vfan's mixed audience: himself + Chinese AI builders + general LLM-curious)
- A **per-work-type loading rules** doc — when working on /draft, load files X+Y+Z; on /ingest, load A+B+C

Adding a one-page `wiki/_audience.md` + an `.claude/loading-rules.md` would close most of the gap.

## Connections
- Related: [[eng-khairallah]], [[context-management]], [[context-noise-governance]], [[gbrain]], [[resolvers]], [[filing-cabinet-vs-nervous-system]], [[system-of-intelligence]], [[skillify-meta-skill]], [[documentation-layers]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-10-khairallah-how-to-master-context-engineering.md | Initial creation — Khairallah's mass-market simplification of context engineering |
