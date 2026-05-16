---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-03-19-tw93-agent-architecture-and-engineering.md
tags: [wiki, principle, agentic, eval, debugging]
---

# Agent Evaluation Traps

## Summary
[[tw93|Tw93]]'s sharp framing for a category most teams under-invest in: **the eval system itself can be the bug**. When numbers drop, the instinct is to "fix the Agent," but the failure may live in the evaluator. Two specific traps are most common: (a) **conflating Pass@k with Pass^k** (capability eval vs regression eval — different questions, different metrics), and (b) **environment / grader bugs masquerading as model regression**. The Anthropic airline-booking example is the canonical case: only looking at *transcript* misses outcomes where the Agent found a better answer than the eval anticipated.

## Details

### Trap 1 — Pass@k vs Pass^k (don't mix them)

| Metric | Question it answers | When to use |
|--------|---------------------|-------------|
| **Pass@k** | "Out of k attempts, did *at least one* succeed?" — Can the Agent **theoretically** do this? | **Development phase** — capability ceiling testing |
| **Pass^k** | "Out of k attempts, did *all k* succeed?" — Is the Agent **reliably** doing this? | **Pre-launch / regression** — change-doesn't-break-existing |

**Why mixing them is bad:**
- Using Pass@k as a regression gate → false negatives (a single successful run hides a 90% failure rate)
- Using Pass^k as a capability test → false negatives (a real new capability is masked by one stochastic failure)

**Rule:** **Pass@k for "is this possible?"; Pass^k for "is this reliable?".** They are not interchangeable.

### Trap 2 — Eval system bugs look exactly like model regression

Common eval-system failure sources:
- Runtime resource limits → process killed by OOM, marked as eval failure
- Grader bug → correct answer judged wrong
- Test cases drifted from production scenarios
- Aggregate-only views → systematic regression in one task class hidden

**All of these manifest as: "our scores dropped." Indistinguishable from "the model got worse" by looking at numbers alone.**

> **Rule of thumb: when eval scores drop, check the environment and the grader first. Only then touch the Agent.**

Tw93 cites the classic chart: as resource limits relax, "model performance" jumps — except the model didn't change. The fix was raising the OOM ceiling. Acting on the original signal would have meant prompt-tweaking a working Agent into something worse.

### Trap 3 — Transcript ≠ Outcome (only-look-at-process fallacy)

> "Agent said 'order completed'" — that's the transcript. "Database has a new order row" — that's the outcome.

**Most teams' evals only check transcripts.** They miss:
- Agent says ✅ but the side-effect didn't happen
- Agent says ❌ but the side-effect did happen (worse: silent partial completion)

**Anthropic's airline-booking example (the canonical case):**

Opus 4.5 was tasked with booking flights. In one run, it found a policy loophole that produced a cheaper outcome than any pre-defined "happy path." 
- **Transcript-only eval:** marked failure (didn't follow expected steps).
- **Outcome eval:** user got a strictly better result.

Without outcome eval, you'd be silently penalizing the model for being smarter than your rubric.

**Rule: cover both transcript and outcome. Especially when the Agent has side-effects on real systems.**

### Trap 4 — Three grader types, certainty trade-off

| Grader type | Determinism | Coverage | Cost |
|-------------|-------------|----------|------|
| **Code** | Highest | Limited (binary answers) | Cheap |
| **Model (LLM-as-judge)** | Medium | Broad | Token cost |
| **Human** | Highest in principle, lowest in practice (rater drift) | Limited (rate limit + cost) | Expensive |

**Rule:** use code where you can. Use model where code can't capture quality. Use human where you need to *calibrate* model graders. **Code → Model → Human cascade**, not "pick one."

### Trap 5 — Saturated eval suite = false confidence

If pass rate is 100%, the suite **isn't measuring anything anymore**. It just confirms you're above a (now obsolete) floor. **Saturation is a signal to harden tasks, not to celebrate.**

> "When the pass rate approaches 100%, supplement harder tasks" → make this a recurring chore, not a one-time event.

### Bootstrap: how to start without a full eval system

Tw93's pragmatic guidance:
- **20-50 real failure cases** are enough to begin
- Source: cases you've already been manually fixing — that's empirical signal of what matters
- **Acceptance criteria test:** if two domain experts independently classify the same case and disagree, the acceptance criteria isn't written clearly enough yet. **Fix the definition first, then collect data.**

### Connection to existing wiki concepts

- **[[verification-loops]]** — same primitive ("test the output") at higher abstraction. These traps are the bugs that erode the verification layer.
- **[[trigger-evals]]** — routing-correctness evals. Same Trap 1/2 dynamics apply at the resolver layer.
- **[[silent-fallback-antipattern]]** — eval system failures are a special case of silent fallback: the test system degrades quality, but reports success.
- **[[self-evaluation-bias]]** — same-model-grades-itself bias makes Trap 4 worse. Use a different model family ([[cross-modal-review]]) for the grader where possible.
- **[[skillify-meta-skill]]** — the 10-step checklist explicitly separates Step 5 (LLM evals) from Step 9 (E2E smoke). Trap 3 is why both steps exist.

### Production checklist (synthesized from the article)
- [ ] Have you separated capability-test from regression-test (Pass@k vs Pass^k)?
- [ ] Does every eval include both transcript and outcome checks?
- [ ] Are environment failures distinguishable from model failures in your dashboard?
- [ ] When the suite saturates, is "add harder tasks" a recurring calendar event?
- [ ] Do you spot-check a few full Traces per week, or only look at aggregate?
- [ ] Are your graders calibrated against human spot-checks?

## Connections
- Related: [[tw93]], [[verification-loops]], [[trigger-evals]], [[silent-fallback-antipattern]], [[self-evaluation-bias]], [[skillify-meta-skill]], [[cross-modal-review]], [[claude-code-goal]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-03-19-tw93-agent-architecture-and-engineering.md | Initial creation — extracted from §6 (Evaluation) and §7 (Observability) |
