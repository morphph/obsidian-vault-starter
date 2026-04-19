---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
tags: [wiki, principle, agentic, governance, eval]
---

# check-resolvable

## Summary
A meta-skill invented by [[garry-tan|Garry Tan]] that walks the whole resolver chain — `AGENTS.md → skill file → code` — and flags any skill, codepath, or capability that has **no reachable path from the resolver**. First run on his production system (40+ skills) found **6 unreachable skills (~15% dark capability)**. Runs weekly like a linter for the [[resolvers|resolver]].

## Details

### The problem it solves: the invisible skill
A skill that exists but isn't registered in the resolver is **worse than a missing skill**. A missing skill is honest — the system says "I can't do that" and you know to build it. An unreachable skill creates the **illusion of capability**: you think the system handles signatures, flights, citations — it doesn't, and you don't find out until the moment it matters.

Garry's concrete examples from his OpenClaw:
- Signature tracker inside executive-assistant skill — worked perfectly, but "check my signatures" didn't fire it
- Flight tracker — no trigger for "is my flight delayed?"
- Content-ideas generator — cron-only, no manual trigger
- Citation fixer — existed on disk, not listed in resolver at all

### The instruction Garry gave his agent
> Check if there is a direct line between the agents.md resolver all the way to this running. And then remember this as a 'check-resolvable' skill. The skill should actually check if this skill or codepath is either directly called out in the resolver or callable via something in the resolver. And if it isn't, figure out what resolvable skill should call it.

### How it works (inferred from Garry's description)
1. Walk every skill file in the skills directory
2. For each, check whether a trigger in `AGENTS.md` (the skill resolver) can reach it
3. Also check codepaths — e.g., cron-only skills that have no manual entry point
4. For each unreachable skill, suggest which existing resolvable skill should call it
5. Report as a list of dead links

### Why it's cheap: fixable by editing markdown
No code changes. The resolver is a document. For each dark capability, you add one trigger row. Garry fixed 6 in an hour.

### Weekly cadence = linter for agent governance
- Runs on a schedule (like a test suite in CI)
- Catches drift between what was built and what's reachable
- Pairs with [[trigger-evals]]: trigger-evals catch **wrong routing**, check-resolvable catches **no routing at all**
- Together they give you reachability + correctness guarantees over a resolver-routed system

### Why the pattern generalizes
Any system with a plugin registry + auto-discovered plugins drifts over time. The registry is maintained by humans (or sub-agents at 3 AM); the plugins are created by any path. Without periodic reachability audits, ~15% of capability going dark looks like the expected failure rate at Garry's scale.

## Connections
- Related: [[resolvers]], [[trigger-evals]], [[context-rot]], [[garry-tan]], [[thin-harness-fat-skills]], [[openclaw]], [[gbrain]], [[documentation-layers]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
