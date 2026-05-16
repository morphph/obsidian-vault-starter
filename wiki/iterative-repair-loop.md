---
type: concept
created: 2026-05-16
last-updated: 2026-05-16
sources:
  - raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md
tags: [wiki, principle, agentic, loop, repair, openai]
---

# Iterative Repair Loop (Review → Repair → Validate)

## Summary
OpenAI Cookbook's three-phase closed-loop pattern (Shreekant Agrawal, 2026-05-11): **Review** (inspect, return structured findings, **no edits**) → **Repair** (focused edits to *copied* artifacts using findings + validation feedback) → **Validate** (execute end-to-end checks, report deltas as structured feedback). **The deeper principle is "separating judgment from proof through structured handoffs."** Each phase produces JSON conforming to a defined schema; validation grounds repairs in **observed behavior**, not inference from diffs. Sibling pattern to [[verification-loops]] and [[agent-improvement-flywheel]] — Iterative Repair is the *narrow per-task* version; Improvement Flywheel is the *broad per-system* version.

## Details

### The three phases (and why they're separated)

| Phase | What it does | What it does NOT do | Output |
|-------|--------------|---------------------|--------|
| **Review** | Inspect artifact, identify issues | **Never edits files** | Structured findings JSON |
| **Repair** | Apply focused edits to **copies** of artifacts | Doesn't decide which issues are real | Updated artifact path + change log |
| **Validate** | Execute end-to-end (e.g., run the notebook) | Doesn't repair | Pass/fail + remaining deltas |

**The separation is the load-bearing design choice:**
- If Review can edit, it confuses "what's wrong" with "what to do about it"
- If Repair can decide what's wrong, it skips investigation in favor of action (Tw93's "agent had the right tool and chose cleverness")
- If Validate is fused with Repair, the eval becomes biased toward the model's own output

### The structured-handoff principle
Each phase produces **strict JSON** following defined schemas. This:
- Forces explicit verdicts (no vague "pretty good")
- Allows mechanical handoff between phases (validation feedback gets *injected* into next repair iteration)
- Creates an **audit trail** — every change traceable to its triggering finding

### Validation as feedback (the key insight)
> "Validation executes notebooks end-to-end, capturing execution failures as structured feedback. This grounds subsequent repairs in **observed behavior** rather than inference from diffs alone."

The repair agent doesn't get to argue "but this *should* work." The notebook either runs or it doesn't. **The feedback signal is empirical, not editorial.**

### Production requirements (stop conditions)
- Validation passes (success)
- Max iterations reached (budget)
- Delta stabilization (we're going in circles)

Plus:
- Complete audit trails for each pass
- Human review checkpoints for unresolved cases

### Concrete example from the cookbook
**Use case:** Documentation reliability for OpenAI's own SDK notebooks. Some had outdated API patterns (`client.chat.completions.create` → `client.responses.create`).

Iteration progression:
- **Iter 1:** simple notebook passes; deeper cases generate focused deltas
- **Iter 2:** medium-complexity fixture clears after validation feedback
- **Iter 3:** most complex case resolves with evidence-driven repairs

### Broader applications (the pattern generalizes)
- **Documentation reliability** (this example)
- **Protocol optimization** (e.g., updating compliance procedures)
- **Regulatory remediation** (audit findings → fix → reverify)
- **Support article updates** (KB drift)
- **Code modernization** (API migrations, deprecation cleanup)

### Comparison to other loop patterns in this wiki

| Pattern | Granularity | Closed by |
|---------|-------------|-----------|
| **Iterative Repair Loop** (this) | Per-artifact iteration | End-to-end validation runs |
| [[verification-loops]] | Per-tool / per-step | Test results, type checks |
| [[quality-gate-loop]] | Per-output quality | Score-then-rewrite until threshold |
| [[claude-code-goal]] / [[agentic-loop-tracking-files]] | Per-task completion | Goal evaluator says "yes" |
| [[agent-improvement-flywheel]] | Per-agent-version | Optimization recommends harness changes |

**The iterative repair pattern is distinct from quality-gate-loop in that quality-gate operates on a single subjective output (does the draft sound right?), while iterative repair operates on **objectively checkable artifacts** (does the notebook actually run?).**

### Direct application to this vault
- **`/lint` could be expanded** to follow this pattern: Review (find issues) → Repair (auto-fix) → Validate (re-run checks). We already do something similar but not formally separated.
- **`/draft` revision** could use this pattern when the human reviewer requests changes: parse comments → apply edits to draft copy → re-validate against original requirements.
- **`/ingest` for already-ingested-but-changed sources** (eg: when an X article gets updated): Review what changed → Repair the wiki pages → Validate links / index.

## Connections
- Related: [[verification-loops]], [[quality-gate-loop]], [[agent-improvement-flywheel]], [[claude-code-goal]], [[agentic-loop-tracking-files]], [[skillify-meta-skill]], [[trigger-evals]], [[silent-fallback-antipattern]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-16 | raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md | Initial creation — OpenAI Cookbook's three-phase Review→Repair→Validate pattern |
