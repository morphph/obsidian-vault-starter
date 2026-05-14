---
type: concept
created: 2026-05-14
last-updated: 2026-05-14
sources:
  - raw/2026-04-07-anatomy-of-agent-harness.md
tags: [wiki, principle, agentic, multi-agent, contracts]
---

# Sprint Contracts

## Summary
A pattern from production [[multi-agent-architecture|multi-agent harnesses]] where the **evaluator and generator agents negotiate success criteria before implementation begins**, instead of the evaluator scoring an output the generator never knew it'd be judged on. Closes the "what good looks like" gap that turns 5-15 iteration cycles into 50. Documented in Anthropic's [[harness-design]] and reflected in production patterns like [[gstack]]'s `/plan-ceo-review` → `/plan-eng-review` chain.

## Details

### The problem
Without a shared contract, evaluator/generator iteration drifts:
- Generator produces work that satisfies one mental model of "done"
- Evaluator scores against a *different* mental model
- Iteration becomes a search for what the evaluator happens to reward, not what was needed
- 5-15 cycles becomes 30-50 because the target keeps moving

### The contract
Before generation starts, the evaluator and generator agree on:
- **Acceptance criteria** — specific testable conditions
- **Out-of-scope** — what *won't* be done
- **Open questions** — assumptions to flag rather than guess
- **Definition of "good enough"** — when iteration stops

This is the agentic version of "spec before code" — but with the added discipline that **both** parties acknowledge the spec.

### How [[gstack]] implements this
Garry Tan's planning chain (`/office-hours` → `/plan-ceo-review` → `/plan-eng-review` → `/plan-design-review`) is essentially a multi-pass sprint-contract negotiation:
1. CEO review establishes *what* the 10-star product looks like
2. Eng review locks architecture, edge cases, test matrix
3. Design review pins down 0-10 scoring criteria per dimension
4. Only then does implementation start

When [[verification-loops|verification]] runs against the implementation, it's checking against a contract everyone already agreed on. **The agents aren't trying to read each other's minds.**

### Connection to [[trigger-evals]]
Trigger evals are a kind of micro-contract for skill routing — *"this intent should fire this skill"* is a one-line contract verifiable in advance. Sprint contracts are the same idea scaled up to features/sprints.

### When NOT to use it
- One-shot tasks (no iteration → no drift to prevent)
- Pure exploration phases where the *goal* is to discover what good looks like
- Single-agent runs (no second party to contract with)

### Failure modes
- Contracts that are too vague to test ("be good") — defeats the purpose
- Contracts that lock in the wrong thing too early — better to ship a thin spike first
- Contract-as-bureaucracy — if it adds more time than it saves, the team is doing it wrong

## Connections
- Related: [[multi-agent-architecture]], [[harness-design]], [[verification-loops]], [[trigger-evals]], [[gstack]], [[skillify-meta-skill]], [[self-evaluation-bias]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-14 | raw/2026-04-07-anatomy-of-agent-harness.md | Initial creation — extracted from harness-design and multi-agent-architecture cross-references |
