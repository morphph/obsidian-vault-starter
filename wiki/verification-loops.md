---
type: concept
created: 2026-04-07
last-updated: 2026-04-15
sources:
  - raw/2026-04-07-anatomy-of-agent-harness.md
  - raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
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
- **In [[ralph-wiggum|Ralph]] loops**: Feedback loops are the primary quality mechanism. Best setup blocks commits unless all checks pass — agent can't declare victory with red tests. Recommended stack: TypeScript types, unit tests, Playwright MCP, ESLint, pre-commit hooks. "Every tip in this article works for human developers too. Feedback loops, small steps, explicit scope — these aren't AI-specific techniques. They're just good engineering. Ralph makes them non-negotiable." ([[matt-pocock]])
- **Preflight gate pattern** (from [[blog2video]] incident): Before pipeline steps with critical dependencies, check availability explicitly. For Twitter/X URLs: ToolSearch must confirm `browser_navigate` is available. If not → hard stop. Prevents [[silent-fallback-antipattern]] where pipeline completes "successfully" with degraded quality. Reusable for any step depending on a specific MCP server or external service.

## Connections
- Related: [[harness-design]], [[self-evaluation-bias]], [[multi-agent-architecture]], [[permission-system]], [[silent-fallback-antipattern]], [[blog2video]], [[ralph-wiggum]], [[software-entropy]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-anatomy-of-agent-harness.md | Initial creation |
| 2026-04-09 | raw/2026-04-08-session-unknown-1421.md | Added preflight gate pattern from blog2video incident |
| 2026-04-15 | raw/2026-04-15-tips-ai-coding-ralph-wiggum.md | Added Ralph feedback loop stack and "non-negotiable" framing |
