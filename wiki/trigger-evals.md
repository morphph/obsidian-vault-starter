---
type: concept
created: 2026-04-19
last-updated: 2026-04-21
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
  - raw/2026-04-21-anthropic-agent-skills-docs.md
tags: [wiki, principle, agentic, eval, governance]
---

# Trigger Evals

## Summary
[[garry-tan|Garry Tan]]'s pattern for testing a [[resolvers|resolver]]: a test suite of ~50 sample inputs with expected skill outputs. Not evaluating the skill's output; evaluating whether **the right skill fires for the right input**. Two failure modes — false negative (skill exists but doesn't fire) and false positive (wrong skill fires because triggers overlap). Both fixable by editing the trigger description in markdown. **In production ([[gbrain]]), this is implemented as `skills/testing/SKILL.md` — a three-way integrity check across `manifest.json` ↔ `RESOLVER.md` ↔ each `SKILL.md`, plus a MECE-violation check for overlapping triggers.**

## Details

### The test suite format (Garry's examples)
```
Input: "check my signatures"
Expected: executive-assistant (signature section)

Input: "who is Pedro Franceschi"
Expected: brain-ops → gbrain search

Input: "save this article to brain"
Expected: idea-ingest + RESOLVER.md
```

### Two failure modes
| Mode | Cause | Fix |
|------|-------|-----|
| **False negative** | Trigger description doesn't match how users phrase things | Rewrite the trigger description |
| **False positive** | Two skills have overlapping triggers | Disambiguate descriptions; add priority |

### Garry's rule
> Make sure the resolver is tested and also there are proper eval LLM tests for all the prompts and skills that use the resolver.
>
> If you can't prove the right skill fires for the right input, you don't have a system. You have a collection of skills and a prayer.

### Why this matters for agent architecture
In a [[thin-harness-fat-skills]] system, routing is done by **natural-language matching of user intent to skill `description` fields** (this is the resolver — see [[resolvers]]). Without tests, the resolver silently drifts ([[context-rot]]) and the only person who knows which skill handles which request is the builder who wrote it. That's a person with a filing cabinet, not a system.

### Where this sits in the resolver governance stack
| Layer | Purpose |
|-------|---------|
| [[resolvers]] (doc) | Routing table |
| **Trigger evals** | Does the right skill fire? |
| [[check-resolvable]] | Is every skill *reachable* at all? |
| Self-healing RLM loop (future) | Rewrites the resolver from observed traffic |

### Concrete parallel: Claude Code's skill descriptions
[[claude-code]]'s skill `description` field is the canonical resolver. Every description is a trigger. Trigger evals are how you'd verify that `/ship`, `/lint`, `/ingest` fire on the right intents without the user having to remember exact command names.

### The production shape: three-way integrity check
From [[gbrain]]'s `skills/testing/SKILL.md` (2026-04-21 deep scan):

> **Contract. This skill guarantees:**
> - Every skill directory has a SKILL.md file
> - Every SKILL.md has valid YAML frontmatter (name, description)
> - Every SKILL.md has required sections (Contract, Anti-Patterns, Output Format)
> - `manifest.json` lists every skill directory
> - `RESOLVER.md` references every skill in the manifest
> - **No MECE violations (duplicate triggers across skills)**
>
> Automated: `bun test test/skills-conformance.test.ts test/resolver.test.ts`

**Key insight:** trigger-evals in production is not "50 sample inputs" — it's a **three-layer integrity check**:

1. `manifest.json` must list every `SKILL.md` in the tree
2. `RESOLVER.md` must have a trigger row for every entry in `manifest.json`
3. Every `SKILL.md` must have the required sections + valid frontmatter

Plus a **MECE check**: no two skills can have overlapping triggers.

This is cheaper than 50 LLM-based eval runs and catches most of the same failures. **Start with integrity checks; add LLM evals only where integrity is passing but routing still drifts.**

### Anthropic's user-facing debugging playbook
From the [[agent-skills-standard|Claude Code Skills docs]]:

**Skill triggers too often (false positive):**
> 1. Make the description more specific
> 2. Add `disable-model-invocation: true` if you only want manual invocation

**Skill doesn't trigger (false negative):**
> 1. Check the description includes keywords users would naturally say
> 2. Verify the skill appears in `What skills are available?`
> 3. Try rephrasing your request to match the description more closely

This is the manual version; trigger-evals automate it.

## Connections
- Related: [[resolvers]], [[check-resolvable]], [[context-rot]], [[agent-skills-standard]], [[gbrain]], [[garry-tan]], [[thin-harness-fat-skills]], [[verification-loops]], [[llm-judgment-vs-scripts]], [[openclaw]], [[claude-code]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Reframed as "three-layer integrity check" based on GBrain's `skills/testing/SKILL.md`; added MECE check |
| 2026-04-21 | raw/2026-04-21-anthropic-agent-skills-docs.md | Added Anthropic's user-facing false-positive / false-negative debugging playbook |
