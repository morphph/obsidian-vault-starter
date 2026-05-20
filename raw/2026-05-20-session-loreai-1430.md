# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Codex CLI vs Claude Code for developers.

**Key Exchanges:**
- Detailed breakdown of execution models: Codex CLI = cloud sandbox (async, isolated), Claude Code = local terminal (interactive, full env access)
- Customization depth comparison: AGENTS.md (flat) vs CLAUDE.md + Skills + Hooks + MCP (layered programmable stack)
- Model families: Codex CLI uses codex-1 (o3-based) + GPT-4.1; Claude Code uses Opus 4 + Sonnet + Haiku

**Decisions Made:**
- Article frames it as "neither is universally better" — choice depends on workflow pattern
- Hybrid recommendation: Codex CLI for well-scoped async tasks (tests, lint, docs), Claude Code for interactive context-heavy work (debugging, architecture, refactoring)
- Pricing positioned as: subscriptions for steady usage, API billing for bursty usage

**Lessons Learned:**
- Codex CLI's strength is parallelism — 5 independent tasks simultaneously with no local resource contention
- Claude Code's differentiator is the programmable extension stack (CLAUDE.md → Skills → Hooks → MCP), not just the model
- Security tradeoff is clear: sandbox isolation (Codex) vs permission-based guardrails (Claude Code) — neither is strictly better, depends on compliance needs
- For large monorepos: Claude Code avoids container setup overhead; Codex CLI wins on parallel independent tasks across repo sections
- Interactive model produces better results on complex/ambiguous tasks because of real-time course correction; async model is fine for well-scoped work

**Action Items:**
- Article references internal links (`/blog/effective-harnesses-for-long-running-agents`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/faq/is-codex-cli-safe-to-use`, `/subscribe`) — verify these exist or create them
- Consider ingesting this as a wiki source if not already done — it contains durable knowledge about both tools' architecture and positioning