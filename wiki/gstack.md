---
type: entity
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
tags: [wiki, product, open-source, skills, agentic]
---

# GStack

## Summary
[[garry-tan|Garry Tan]]'s open-source **coding/skills layer** for Claude Code — the "fat skills in markdown" layer from [[thin-harness-fat-skills]]. **72,000+ stars on GitHub** (as of 2026-04-15). Calls the knowledge in [[gbrain]]; plugs into [[openclaw|OpenClaw]] or Hermes Agent as the harness. Repo: github.com/garrytan/gstack.

## Details

### What it is
- Library of reusable fat skills written as markdown files
- Each skill is a procedure with parameters (TARGET / QUESTION / DATASET) — see [[skill-as-method-call]]
- Designed to call [[gbrain|GBrain]]'s knowledge layer (`gbrain search` is referenced in Garry's trigger eval examples)
- Runs under any thin harness that executes markdown skills: [[claude-code]], [[openclaw]], Hermes Agent

### Why "fat" matters
Garry's architectural claim: in the 2026 stack, **90% of value lives in skills**, not in harnesses or models. [[thin-harness-fat-skills]]. A skill is not a prompt; it's a codified procedure that:
- Gets re-used across 100s of invocations
- Automatically improves with every model release (model is the runtime; skill is the program)
- Can be moved between harnesses without rewriting — it's just markdown

### Traction signal
72K+ GitHub stars is in the same league as large AI-tooling repos. Suggests that the fat-skills pattern has found product-market fit among AI builders.

### Garry's three-project stack
| Layer | Project | What it owns |
|-------|---------|--------------|
| Harness | [[openclaw|OpenClaw]] / Hermes Agent | Event loop, sessions, crons |
| **Skills** | **GStack** | **Reusable markdown procedures** |
| Knowledge | [[gbrain|GBrain]] | Filing rules, resolver, compiled memory |

### Relationship to Claude Code
Claude Code's native "skills" concept (skill descriptions as [[resolvers|resolver]] entries) is the same primitive. GStack is a curated library of skills that plug into that primitive — fat skills that have been hardened across many production runs.

### For this vault
The `.claude/commands/` slash commands in this repo are already fat-ish skills. GStack represents a mature library worth surveying for patterns (the [[garry-tan|Garry Tan]] skill-writing conventions — registration in `AGENTS.md`, trigger descriptions, `RESOLVER.md` mandate header).

## Connections
- Related: [[garry-tan]], [[gbrain]], [[openclaw]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[resolvers]], [[claude-code]], [[harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
