# Session Capture: loreai

**Date:** 2026-05-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Curating the daily AI newsletter digest for May 16, 2026 — structured JSON output with 22 items across 6 sections plus quick links.

**Key Exchanges:**
- Generated a full newsletter JSON with headline hook, pick of the day, model literacy explainer, and categorized items (LAUNCH, TOOL, TECHNIQUE, RESEARCH, INSIGHT, BUILD, QUICK_LINKS)

**Decisions Made:**
- **Pick of the Day:** Item 38260 — the 10x token efficiency gap between code-first and MCP-based agents (SDK: 1 step/15k tokens vs MCP: 4 steps/158k tokens on Monday.com's GraphQL API). Thesis: tool-calling abstraction is architecturally wasteful.
- **Model Literacy concept:** Mixture of Experts (MoE), pegged to the 30B-A3B Olympiad model
- **Hero items chosen:** OpenAI+Zed integration, 30B-A3B MoE model, Anthropic $200M Gates commitment, OpenAI unified-app merger under Brockman

**Lessons Learned:**
- MoE active-vs-total parameter distinction matters for deployment cost estimates (3B active out of 30B total → consumer GPU viable)
- LeCun framework: LLMs dominate when language IS the reasoning substrate (math, code), not when it merely describes the domain

**Action Items:**
- Track upcoming frontier releases: GPT 5.6 and Gemini 3.2 both expected next week
- Track Grok V9 (1.5T params, no Cursor fine-tuning yet) — coding benchmark results pending
- Monitor MCP efficiency debate — the 10x token gap is the most concrete data point yet
- Note: Claude Code v2.1.143 shipped plugin dependency enforcement and worktree isolation
- Mitchell Hashimoto coined "AI Psychosis" for companies making irrational AI-hype-driven decisions — concept worth tracking