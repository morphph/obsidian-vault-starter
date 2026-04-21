# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article between Codex CLI and Claude Code for potential wiki ingestion.

**Key Exchanges:**
- No Q&A — this was a passive content review session. The content is a long-form comparison article titled something like "Codex CLI vs Claude Code" covering architecture, model quality, DX, open source stance, pricing, and decision criteria.

**Decisions Made:**
- (None recorded — session was content review only)

**Lessons Learned:**
- **Codex CLI key facts**: Apache 2.0 open source, uses OpenAI models (o4-mini default, o3 available), network-disabled sandbox by design, no persistent memory, sequential single-agent execution, reads `AGENTS.md` / `CODEX.md`, lightweight/no-config
- **Claude Code key facts**: Proprietary, uses Anthropic Claude models (Sonnet/Opus/Haiku), network access by default, persistent memory via CLAUDE.md + auto-memory, parallel agent teams, hooks for deterministic automation, MCP server integrations, SKILL.md for reusable task instructions, multi-surface (terminal, VS Code, JetBrains, desktop, web, mobile)
- **Decision framework**: Codex CLI wins on sandbox security + open-source compliance; Claude Code wins on multi-file/multi-session workflows, extensibility, and ecosystem integration
- **Pricing**: Both usage-based; Codex CLI via OpenAI API credits (o4-mini rates); Claude Code via Anthropic API or Pro ($20/mo) / Max ($100–200/mo) subscriptions

**Action Items:**
- Consider ingesting this article as a raw source: good candidate for a `wiki/codex-cli-vs-claude-code.md` comparison page
- Source appears to be from LoreAI blog (`/blog/` URLs referenced) — check if it belongs in `raw/` before wiki synthesis