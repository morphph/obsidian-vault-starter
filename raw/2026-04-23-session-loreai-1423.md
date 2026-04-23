# Session Capture: loreai

**Date:** 2026-04-23
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a detailed comparison article between Codex CLI and Claude Code, likely for potential wiki ingest.

**Key Exchanges:**
- No actual conversation — the context is an article body comparing Codex CLI vs Claude Code across: sandbox model, context/config system, multi-agent orchestration, model capabilities, git integration, pricing, and IDE support.

**Decisions Made:**
- N/A (no active session decisions)

**Lessons Learned:**
- Codex CLI: network-disabled sandbox (hard security boundary), open-source (Apache 2.0), single-agent, flat `codex.md` config, pure API billing (o4-mini default), minimal git (diff only)
- Claude Code: approval-based model (no network block), hierarchical CLAUDE.md + SKILL.md + hooks + MCP, multi-agent orchestration, full git automation (commit/push/PR), subscription tiers ($20/$100/$200/mo) plus API
- Key differentiator: Codex CLI = security + simplicity; Claude Code = extensibility + orchestration
- Both can coexist: Codex for sandboxed quick tasks, Claude Code for complex multi-step workflows

**Action Items:**
- This article is a strong candidate for `/ingest` into the wiki — maps directly to domain focus ("Builder tools and workflows") and could anchor a `codex-cli-vs-claude-code.md` wiki page cross-linked with existing [[Claude Code]] content.