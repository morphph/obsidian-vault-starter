---
type: entity
created: 2026-04-17
last-updated: 2026-04-17
sources:
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
  - raw/2026-04-16-claude-docs-opus-4-7-whats-new.md
tags: [wiki, product, llm, model]
---

# Claude Opus 4.7

## Summary
[[Anthropic]]'s flagship model released 2026-04-16. Positioned as "the Opus 4.6 you can delegate to without watching" — substantial gains in agentic coding reliability, literal instruction following, self-verification, and high-resolution vision. First Claude model with high-res image support (3.75MP). Pricing unchanged from 4.6.

## Details
- **Model ID:** `claude-opus-4-7`
- **Pricing:** $5 / $25 per M input/output tokens (unchanged from 4.6). Prompt caching up to 90% off, batch 50% off.
- **Context/output:** 1M context, 128k max output tokens (same as 4.6)
- **Availability:** Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry
- **Core improvements over 4.6:**
  - **Agentic coding reliability** — users report confidently delegating long-running tasks without supervision; model self-verifies before reporting
  - **Literal instruction following** — interprets prompts more literally; existing 4.6 prompts may need re-tuning
  - **High-res vision (first for Claude)** — 2576px long edge / 3.75MP, up from 1568px / 1.15MP. XBOW reports 98.5% vs 54.6% on visual-acuity benchmark
  - **Better file-system memory** — improved at maintaining notes/scratchpads across turns
- **New control primitives:**
  - [[xhigh-effort-level]] — new effort tier between `high` and `max`, recommended for agentic coding
  - [[task-budgets]] — token budget hint for the full agentic loop (beta; header `task-budgets-2026-03-13`; minimum 20k)
  - [[adaptive-thinking]] — now the only thinking-on mode; **off by default** on 4.7
- **Breaking API changes (Messages API only; Managed Agents unaffected):**
  - Extended thinking budgets removed — `thinking: {type: "enabled", budget_tokens: N}` returns 400
  - Sampling parameters removed — `temperature`, `top_p`, `top_k` at non-default values return 400
  - Thinking content omitted from response by default — set `display: "summarized"` to opt in
  - 1M context available at standard API pricing — no long-context premium
- **Behavior changes (non-breaking but may require prompt updates):**
  - More literal instruction following (especially at lower effort); won't silently generalize
  - Response length calibrates to task complexity (no fixed verbosity)
  - Fewer tool calls by default — uses reasoning more; raise effort to get more tool use
  - More direct, opinionated tone; less validation-forward; fewer emoji than 4.6
  - More regular progress updates during long agentic traces — remove scaffolding that forced interim messages
  - Fewer subagents spawned by default — steerable via prompting
  - Real-time cybersecurity safeguards active on prohibited/high-risk requests
- **Benchmark quotes from early testers:**
  - Cursor CEO: 70% vs 58% (4.6) on their internal benchmark
  - Notion AI Lead: +14% over 4.6 with fewer tokens and 1/3 the tool errors
  - Rakuten: resolves 3x more production tasks than 4.6
- **Safety posture (Project Glasswing):** cyber offensive capabilities deliberately reduced relative to the unreleased Mythos Preview. Automated safeguards block high-risk cyber requests. Legitimate security researchers can apply to the Cyber Verification Program.
- **Alignment:** similar profile to 4.6; improved honesty and prompt-injection resistance; modest regression on controlled-substance harm-reduction guidance.
- **Migration gotcha:** updated tokenizer inflates token counts 1.0–1.35× depending on content type; higher effort levels also generate more thinking tokens.
- **Claude Code updates tied to 4.7:**
  - `/ultrareview` — dedicated code-review session (Pro/Max get 3 free/month)
  - Extended auto mode for Max subscribers

## Connections
- Related: [[Anthropic]], [[claude-model-family]], [[claude-code]], [[xhigh-effort-level]], [[task-budgets]], [[adaptive-thinking]], [[verification-loops]], [[context-anxiety]], [[assumptions-expire]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Initial creation from official announcement |
| 2026-04-17 | raw/2026-04-16-claude-docs-opus-4-7-whats-new.md | Added breaking API changes, behavior changes, adaptive thinking |
