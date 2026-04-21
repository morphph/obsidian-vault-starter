---
type: concept
created: 2026-04-19
last-updated: 2026-04-21
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-04-21-gbrain-gstack-github-deep-scan.md
  - raw/2026-04-21-anthropic-agent-skills-docs.md
tags: [wiki, principle, agentic, governance, eval]
---

# check-resolvable

## Summary
A meta-skill invented by [[garry-tan|Garry Tan]] that walks the whole resolver chain — `AGENTS.md → skill file → code` — and flags any skill, codepath, or capability that has **no reachable path from the resolver**. First run on his production system (40+ skills) found **6 unreachable skills (~15% dark capability)**. Runs weekly like a linter for the [[resolvers|resolver]]. **Confirmed as real TypeScript code (`src/core/check-resolvable.ts`) in [[gbrain]]**, not just a concept — performs reachability + MECE overlap + DRY checks, emits structured fix objects.

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

### The real implementation (2026-04-21 GitHub Deep Scan)
GBrain ships `src/core/check-resolvable.ts` in production. Three checks:

1. **Reachability** — every skill in `manifest.json` must have an entry in `RESOLVER.md`, and every `RESOLVER.md` entry must resolve to an existing `SKILL.md`
2. **MECE overlap** — catches duplicate triggers across skills (false-positive source for [[trigger-evals]])
3. **DRY violations** — finds inlined cross-cutting rules that should be delegated

DRY is proximity-based: `DRY_PROXIMITY_LINES = 40`. `extractDelegationTargets()` parses `> **Convention:**`, `> **Filing rule:**`, and inline backticks as valid delegations.

### Sister tool: `gbrain doctor --fix` (auto-remediation)
`src/core/dry-fix.ts` rewrites inlined rules to `> **Convention:** see [path](path).` callouts via three shape-aware expanders (bullet / blockquote / paragraph). **Five guards:**
- working-tree-dirty → refuse (don't mix auto-fix with uncommitted work)
- no-git-backup → refuse
- inside-code-fence → skip (don't edit docs inside examples)
- already-delegated (40-line proximity) → skip
- ambiguous-multi-match / block-is-callout → skip

`execFileSync` with array args (no shell — no injection surface). EOF newline preserved.

**Lesson:** auto-fixing markdown has five different ways to destroy user work. Every one of them needs a guard.

### Anthropic's built-in debugging playbook
The [[agent-skills-standard|Claude Code Skills docs]] documents the user-facing equivalent:
> **Skill not triggering:**
> 1. Check the description includes keywords users would naturally say
> 2. Verify the skill appears in `What skills are available?`
> 3. Try rephrasing your request to match the description more closely
> 4. Invoke it directly with `/skill-name` if user-invocable

This is the manual version of check-resolvable — walk the chain by hand. check-resolvable is what you build when step 1 isn't enough.

### Weekly cadence = linter for agent governance
- Runs on a schedule (like a test suite in CI)
- Catches drift between what was built and what's reachable
- Pairs with [[trigger-evals]]: trigger-evals catch **wrong routing**, check-resolvable catches **no routing at all**
- Together they give you reachability + correctness guarantees over a resolver-routed system

### Why the pattern generalizes
Any system with a plugin registry + auto-discovered plugins drifts over time. The registry is maintained by humans (or sub-agents at 3 AM); the plugins are created by any path. Without periodic reachability audits, ~15% of capability going dark looks like the expected failure rate at Garry's scale.

## Connections
- Related: [[resolvers]], [[trigger-evals]], [[context-rot]], [[agent-skills-standard]], [[garry-tan]], [[thin-harness-fat-skills]], [[openclaw]], [[gbrain]], [[documentation-layers]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
| 2026-04-21 | raw/2026-04-21-gbrain-gstack-github-deep-scan.md | Confirmed as real TS code (`src/core/check-resolvable.ts`); three checks (reachability + MECE + DRY); DRY_PROXIMITY_LINES=40; `gbrain doctor --fix` auto-remediation with five guards |
| 2026-04-21 | raw/2026-04-21-anthropic-agent-skills-docs.md | Added Anthropic's manual debugging playbook (the user-facing equivalent) |
