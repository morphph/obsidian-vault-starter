# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a comparison article on Codex CLI vs Claude Code for potential wiki ingestion.

**Key Exchanges:**
- Source document is a detailed comparison of Codex CLI (OpenAI) vs Claude Code (Anthropic) across dimensions: execution model, autonomy/workflow, extensibility, model capabilities, pricing, and IDE integration.

**Decisions Made:**
- No decisions recorded — this appears to be a read/review session with no tool calls or edits made.

**Lessons Learned:**
- Codex CLI: cloud sandbox, async/fire-and-forget, o3-based codex-1 model, requires ChatGPT Pro ($200/mo), limited customization, strong isolation
- Claude Code: local execution, interactive/real-time, Claude Sonnet/Opus models, pay-per-token or Max plan ($100/$200/mo), deep customization (CLAUDE.md, skills, hooks, MCP, sub-agents)
- Key differentiator: Codex = batch + isolation; Claude Code = interactive + local env + programmable guardrails
- Claude Code sub-agents share context and coordinate; Codex containers are fully independent
- Both support VS Code; Claude Code also has JetBrains, desktop app, web app
- Codex CLI suitable for: batch tasks, security-isolated teams, ChatGPT Pro subscribers, simple project setups
- Claude Code suitable for: complex local environments, interactive iteration, MCP integrations, variable usage patterns

**Action Items:**
- Consider ingesting this article as a raw source → wiki page on `codex-cli-vs-claude-code.md` or updating existing `claude-code.md` with Codex comparison notes