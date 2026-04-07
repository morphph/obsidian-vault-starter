---
type: concept
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-anatomy-of-agent-harness.md
tags: [wiki, architecture, agentic, quality]
---

# Verification Loops

## Summary
Quality assurance mechanisms in agent harnesses that improve output quality by 2-3x. Three approaches: rules-based feedback (tests, linters), visual feedback (screenshots), and LLM-as-judge using separate subagents.

## Details
- **Rules-based**: deterministic checks — tests pass/fail, linter errors, type checks
- **Visual feedback**: screenshot comparison, rendering validation (e.g., Playwright MCP testing UI)
- **LLM-as-judge**: separate subagent evaluates output using semantic criteria
- Two verification paradigms:
  - **Computational (deterministic)**: binary pass/fail, reproducible, fast
  - **Inferential (semantic)**: nuanced quality judgment, subjective, more expensive
- In GAN-inspired [[harness-design]], the evaluator agent IS the verification loop — iterates 5-15 rounds with the generator
- Risk: [[self-evaluation-bias]] — agents approve their own mediocre work. Fix by using a separate evaluator agent, not self-review.
- Three-level guardrail enforcement: input guardrails (first agent), output guardrails (final), tool guardrails (every invocation)

## Connections
- Related: [[harness-design]], [[self-evaluation-bias]], [[multi-agent-architecture]], [[permission-system]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Initial creation |
