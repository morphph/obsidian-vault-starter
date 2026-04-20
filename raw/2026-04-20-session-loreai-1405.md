# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a comparative article on Claude Code vs Codex (OpenAI) for potential wiki ingestion

**Key Exchanges:**
- Article covers Claude Code vs Codex across 7 dimensions: architecture, customization, multi-agent, workflow integration, pricing, ecosystem, and FAQs
- Source appears to be a LoreAI blog post (`/compare/claude-code-vs-codex` or similar)

**Decisions Made:**
- No decisions recorded — this was a passive content review, no tools were invoked

**Lessons Learned:**
- **Architecture split**: Claude Code = local + interactive + full shell access; Codex = cloud sandbox + async + PR-based output
- **Customization**: Claude Code has layered stack (CLAUDE.md + SKILL.md + hooks + MCP); Codex uses simpler AGENTS.md only
- **Multi-agent**: Claude Code spawns coordinated sub-agents in git worktrees; Codex parallelizes at task level (no cross-task coordination)
- **Pricing**: Claude Code = pay-per-token API; Codex = bundled with ChatGPT Pro ($200/mo) / Team ($30/user/mo)
- **Security**: Codex stronger isolation by default (sandboxed, no network); Claude Code more granular control via permissions + hooks
- **Model**: Claude Code = Claude only; Codex = codex-mini + GPT-4.1 dual-model
- **Verdict**: Tools are complementary — Claude Code for interactive/complex work, Codex for async delegation

**Action Items:**
- Consider ingesting this source into `raw/` and creating/updating a `wiki/claude-code-vs-codex.md` or updating existing `claude-code.md` with competitive positioning notes