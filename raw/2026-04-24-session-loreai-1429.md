# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article content comparing Codex CLI vs Claude Code for AI-assisted software engineering workflows

**Key Exchanges:**
- Detailed breakdown of Codex CLI vs Claude Code across 7 dimensions: execution model, context/config, extensibility, safety, pricing, workflow integration, and when to choose each

**Decisions Made:**
- Neither tool is universally "better" — choice depends on workflow philosophy: async delegation → Codex CLI; interactive pair-programming → Claude Code
- Many teams use both: Codex CLI for task backlog, Claude Code for current complex focus

**Lessons Learned:**
- Codex CLI: sandbox-first (network-isolated container), async fire-and-forget, bundled with ChatGPT Pro ($200/mo), no persistent memory across tasks, `CODEX.md`/`AGENTS.md` for project instructions
- Claude Code: local execution, permission-prompt safety model, per-token API billing, layered context system (CLAUDE.md + skills + auto-memory + MCP), hooks/sub-agents for extensibility
- Claude Code's persistent context compounds in value over time; Codex CLI is stateless per task
- Codex CLI safer by design for enterprises (hardware-level sandbox); Claude Code more powerful for local-env-dependent workflows
- Pricing: Codex bundled = better for light use; Claude Code per-token = better for heavy use with model flexibility

**Action Items:**
- Consider ingesting this as a wiki page on `codex-cli-vs-claude-code.md` for the AI builder knowledge base