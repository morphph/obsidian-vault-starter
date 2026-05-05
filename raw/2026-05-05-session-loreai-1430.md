# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working with a comparison article (likely for ingestion or drafting) on Codex CLI vs Claude Code — two AI coding agents with fundamentally different architectures.

**Key Exchanges:**
- Codex CLI = cloud-sandboxed, async delegation model; Claude Code = local-machine, interactive collaboration model
- This architectural difference cascades into every other tradeoff: context, safety, extensibility, pricing

**Decisions Made:**
- The comparison framework is **architectural, not capability-based** — both are powerful, but optimize for different workflows
- Codex for ticket-driven parallel task execution; Claude Code for deep, exploratory, environment-aware work
- They complement rather than compete — can be used on the same project for different task types

**Lessons Learned:**
- Codex CLI (2025) is **not** the original OpenAI Codex model (GPT-3 descendant that powered Copilot autocomplete) — completely different product sharing a name
- Codex's sandboxing = stronger security isolation by default, but cannot access local env/services/DBs
- Claude Code's persistent memory stack (CLAUDE.md → Skills → hooks → MCP) makes it behave more like a platform than a tool
- Pricing: Codex = fixed subscription (Pro $200/mo, Teams $30/user/mo); Claude Code = usage-based API billing (per-token, varies by model tier)
- Cost crossover: Claude Code cheaper at <20 tasks/mo; Codex Pro better value at 100+ tasks/mo
- Claude Code handles large monorepos better (no container clone overhead)
- Codex strengths: parallel task processing, open-source issue triage, security-sensitive environments
- Claude Code strengths: integration testing against live services, complex debugging, team convention enforcement

**Action Items:**
- Content is ready for wiki ingestion — covers AI coding tools landscape (Codex CLI, Claude Code positioning)
- Could create/update wiki pages: `codex-cli.md`, `claude-code.md`, or a comparison page
- Pricing data flagged as rapidly evolving — will need periodic refresh