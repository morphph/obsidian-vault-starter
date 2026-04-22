# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/processing a detailed comparison article between Claude Code and OpenAI Codex, likely for ingestion or drafting purposes.

**Key Exchanges:**
- The session appears to have involved reading/processing a long-form article: "Claude Code vs OpenAI Codex" — a comprehensive comparison covering execution model, context system, security, pricing, and enterprise adoption.

**Decisions Made:**
- No explicit decisions recorded — session appears to be content review only.

**Lessons Learned:**
- Key comparison frame: Claude Code = real-time pair programmer (local, terminal-centric, full env access); Codex = async task runner (cloud sandbox, no network by default, PR-review workflow)
- Claude Code advantages: CLAUDE.md/SKILL.md system, agent teams (parallel sub-agents), hooks/MCP extensibility, tight feedback loops
- Codex advantages: stronger sandboxing (no network by default), async delegation, ChatGPT Enterprise integration, VS Code-native
- Security models differ fundamentally: Codex isolated by default; Claude Code relies on user approval workflow
- Pricing: Codex bundled in ChatGPT Team ($30/user/mo); Claude Code on Max plan ($100–200/mo) with per-token billing

**Action Items:**
- Consider ingesting the Claude Code vs Codex comparison article as a raw source → wiki page (e.g., `claude-code-vs-codex.md`) covering tool comparison, tradeoffs, and use-case guidance