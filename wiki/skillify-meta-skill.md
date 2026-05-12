---
type: concept
created: 2026-05-11
last-updated: 2026-05-12
sources:
  - raw/2026-04-21-garry-tan-skillify-manifesto.md
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
tags: [wiki, principle, agentic, meta-skill, claude-code]
---

# Skillify (Meta-Skill)

## Summary
[[garry-tan|Garry Tan]]'s production-confirmed name for the **meta-skill that creates new skills**. In [[gbrain]], `/skillify` is a real command: you do a workflow manually once, then say "skillify this" — the system examines what happened, extracts the repeatable pattern, **runs the 10-step quality checklist** below, and registers the new skill in the [[resolvers|resolver]]. The operational implementation of Garry's "if I have to ask you for something twice, you failed" rule. Composes with [[check-resolvable]] (verifies reachability) and `cross-modal-eval` (multi-model quality check).

## Details

### The four-step compounding loop (Garry's "How to Start")

```
1. Do something interesting (NOT plan the skill architecture first)
2. Iterate with the agent until the output is good
3. /skillify → extracts pattern, writes SKILL.md, registers in RESOLVER.md
4. check_resolvable → verifies it's reachable from the routing table
```

> "That loop turns one-off work into compounding infrastructure."

### The 10-step Skillify Checklist (from the Skillify Manifesto, 2026-04-21)

This is what `gbrain doctor` actually enforces:

```
□ 1. SKILL.md            — the contract (name, triggers, rules)
□ 2. Deterministic code  — scripts/*.mjs (no LLM for what code can do)
□ 3. Unit tests          — vitest
□ 4. Integration tests   — live endpoints
□ 5. LLM evals           — quality + correctness
□ 6. Resolver trigger    — entry in AGENTS.md
□ 7. Resolver eval       — verify the trigger actually routes
□ 8. Check-resolvable + DRY audit
□ 9. E2E smoke test
□ 10. Brain filing rules
```

> "**A feature that doesn't pass all ten is not a skill. It's just code that happens to work today.**"

**Production numbers (Garry's own system as of 2026-04-21):**
- 179 unit tests across 5 suites, runs in <2 seconds
- 35 LLM evals run daily for `context-now` alone
- 50+ resolver eval cases for routing accuracy
- `gbrain doctor --fix` runs check-resolvable + DRY audit weekly

**Most honest eval-discovery heuristic:**
> "Search your conversation history for when you said 'fucking shit' or 'wtf.' **Those are the test cases you're missing.**"

### Canonical case studies (the two production failures that birthed the checklist)

**Case 1: `calendar-recall`** — Agent called live calendar API for an event 10 years old, ignored 3,146 local calendar files. Fix: skill mandates "live calendar API ONLY for events in the FUTURE or LAST 48 HOURS." Agent itself wrote `calendar-recall.mjs` (sub-millisecond grep, zero LLM calls). The script now constrains the latent space that built it.

**Case 2: `context-now`** — Agent did UTC→PT timezone math in head, off by 60 minutes. Existing `context-now.mjs` script (50ms, zero ambiguity) wasn't being run. Fix: skill mandates "NEVER do UTC→PT conversion in your head — always run context-now.mjs before any time-sensitive claim."

**Same shape both times:** [[latent-vs-deterministic|deterministic work done in latent space]]. The agent had the right tool and chose cleverness instead of discipline.

### The recursive insight (the loop that makes the architecture work)

> "**The latent space builds the deterministic tool, then the deterministic tool constrains the latent space.** The agent used judgment (latent) to write `calendar-recall.mjs`. Now the skill forces the agent to use that script instead of reasoning about calendar data. **The model's intelligence created the constraint that prevents the model from being stupid.**"

This is the deepest design pattern in the entire Garry Tan series: **LLM judgment is used to manufacture the constraints that subsequently prevent LLM judgment from being misapplied.** Self-bootstrapping discipline.

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

### Skillify has become a verb (daily workflow examples)

The checklist started as failure-response protocol, then became how Garry builds everything. Real examples from his article:

> "hot damn it worked. can you remember this as a webhook skill and skillify it, next time we need to do some webhooks? ... DRY it up too" — OAuth webhook integration, one hour of work made permanent

> "we should actually remember this as a skill whenever anything in openclaw needs a headless browser! and also know that if we need a headed browser we should ask the user to run gstack browser and give us a pair-agent code. skillify it!"

> "can we make a skill that says whenever you send me a link you have to curl it yourself to make sure the endpoint is open and the tunnel works? skillify it!"

> "Here is one regular skill I need you to write. It's the calendar check skill. Tomorrow I have a double booked 11am. Make a skill, make it deterministic to check these kinds of things."

**Pattern:** prototype in conversation → see it work → say "skillify" → 10-step checklist runs → permanent infrastructure. **One sentence, the whole pipeline.**

> "I don't write specs. I don't file tickets. I talk to my agent, we solve the problem together, and then the solution becomes a skill that the agent can use forever without me."

### Why Hermes Agent's `skill_manage` isn't enough on its own
Hermes Agent has `skill_manage` — the agent itself creates/patches/deletes skills based on what it learns. Smart design, but **no testing layer**:
- No unit tests on deterministic code
- No resolver evals to verify routing
- No check-resolvable to find dark skills
- No DRY audit to catch duplicates
- No daily health check

**Three failure modes that accumulate in any untested skill system:**
1. **Duplicate skills** — `deploy-k8s` on Monday, `kubernetes-deploy` on Thursday → ambiguous routing
2. **Silent API drift** — skill perfect when written, upstream API changes 6 weeks later → silently returns garbage
3. **Orphans** — auto-created skill with weak trigger → never matches, eats index tokens, rots

> "Hermes handles creation beautifully. GBrain handles verification. **You need both.**"

This is the agentic equivalent of "without tests, any codebase rots" — software engineering solved this in 2005. Agent skills are no different.

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
| 2026-05-12 | raw/2026-04-21-garry-tan-skillify-manifesto.md | Major expansion — added full 10-step Skillify Checklist (the operational deliverable); calendar-recall + context-now case studies; "latent builds deterministic that constrains latent" recursive insight; skillify-as-verb daily workflow examples; Hermes Agent comparison (creation vs verification) |
