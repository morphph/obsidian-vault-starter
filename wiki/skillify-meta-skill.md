---
type: concept
created: 2026-05-11
last-updated: 2026-05-11
sources:
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
tags: [wiki, principle, agentic, meta-skill, claude-code]
---

# Skillify (Meta-Skill)

## Summary
[[garry-tan|Garry Tan]]'s production-confirmed name for the **meta-skill that creates new skills**. In [[gbrain]], `/skillify` is a real command: you do a workflow manually once, then say "skillify this" — the system examines what happened, extracts the repeatable pattern, writes a tested skill file with triggers and edge cases, and **registers it in the [[resolvers|resolver]]**. The operational implementation of Garry's earlier "if I have to ask you for something twice, you failed" rule. Composes with [[check-resolvable]] (verifies the new skill is reachable) and `cross-modal-eval` (quality-checks output across multiple models).

## Details

### The four-step compounding loop (Garry's "How to Start")

```
1. Do something interesting (NOT plan the skill architecture first)
2. Iterate with the agent until the output is good
3. /skillify → extracts pattern, writes SKILL.md, registers in RESOLVER.md
4. check_resolvable → verifies it's reachable from the routing table
```

> "That loop turns one-off work into compounding infrastructure."

### What `/skillify` actually does (production behavior)

From Garry's article:
> "When I encounter a workflow I'm going to repeat, I say 'skillify this' and it examines what just happened, extracts the repeatable pattern, writes a tested skill file with triggers and edge cases, and registers it in the resolver."

Concrete outputs:
- A new `SKILL.md` file in the skills directory
- YAML frontmatter with `name`, `triggers: []`, `tools: []` (see [[agent-skills-standard]] dialect comparison)
- Body following GBrain's mandatory structure: Contract / Phases / Output Format / Anti-Patterns
- A new entry in `RESOLVER.md` mapping trigger phrases to the new skill
- An entry in `manifest.json` (machine-readable registry)

### Why this is the "meta" in "meta-meta-prompting"

The article's title invokes three levels:
- **Prompting** (level 0) — you write a prompt
- **Meta-prompting** (level 1) — the model writes prompts for itself (skills)
- **Meta-meta-prompting** (level 2) — **the model writes the skills that write the prompts**

`/skillify` lives at level 2. It is the recursive primitive that makes the system self-extending.

### The compounding mechanism

> "Skills compose. Book-mirror calls brain-ops for storage, enrich for context, cross-modal-eval for quality, and pdf-generation for output. Each skill is focused on one thing. **When I improve one skill, every workflow that uses it gets better automatically.**"

Skillify's value isn't just "create one more skill." It's that **every future workflow that uses this skill inherits the encoded operational knowledge**. Garry's claim:
> "Each skill encodes operational knowledge that would take a new human assistant months to learn."

### Counter-intuitive: do the work FIRST, skillify SECOND

The most actionable insight from this article is the explicit ordering:
> "Don't start by planning your skill architecture. Start by doing a thing... Do it with your agent, iterate until it's good, and then run Skillify."

This contradicts the engineering instinct ("design before build"). The reason:
- You can't know which abstraction is right until you've executed the workflow at least once
- A skill written before you've done the task captures the wrong pattern
- Skillify extracts the **observed** pattern, including the edge cases you discovered live

Pairs naturally with [[thariq]]'s warning against premature `/html` skill creation — same principle.

### Skillify + the "if I ask twice" rule
[[garry-tan|Garry]]'s [[openclaw|OpenClaw]] discipline rule: *"If I have to ask you for something twice, you failed."* `/skillify` is **the operational mechanism that enforces this rule** — it converts the second-ask trigger into a permanent capability. Without skillify, the rule is a wish. With skillify, it's a procedure.

### What skillify needs to work well

- A [[resolvers|resolver]] that accepts new entries cleanly (no manual editing required)
- A skill template / contract (so generated skills are uniform — see [[gbrain]]'s `Contract/Phases/Output Format/Anti-Patterns` structure)
- A [[check-resolvable]]-style validator (so the new skill is actually reachable)
- Optional: a `cross-modal-eval` for quality-checking the generated skill against real outputs

### How this fits this vault's workflow

This vault has no skillify equivalent. The closest workflow:
- Discover a repeated pattern in `raw/` ingestion
- Update `.claude/commands/ingest.md` by hand
- Add to CLAUDE.md's Commands table

A skillify-like primitive for this vault would:
- Watch when we (a) ingest a new source type or (b) build a one-off draft workflow
- Extract the pattern
- Generate a new `.claude/commands/{name}.md` with appropriate triggers
- Add to CLAUDE.md Commands table (or RESOLVER.md if we build one)

**This is candidate 9 for the implementation queue** — but it's a downstream optimization; we should build the filing rules ([[1️⃣]]) and a check-resolvable equivalent ([[3️⃣]]) first so the skillify output has something correct to register into.

## Connections
- Related: [[garry-tan]], [[gbrain]], [[gstack]], [[openclaw]], [[resolvers]], [[check-resolvable]], [[agent-skills-standard]], [[skill-as-method-call]], [[thin-harness-fat-skills]], [[plan-mode-as-tools]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-11 | raw/2026-05-09-garry-tan-meta-meta-prompting.md | Initial creation |
