# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison draft article: "Claude Code vs Codex：终端 Agent 与云端 Agent 的路线之争"

**Key Exchanges:**
- Article created as a `/draft` output comparing Claude Code and OpenAI Codex across architecture, workflow, pricing, and use cases
- Core framing: local-first (Claude Code) vs cloud-first (Codex) — two distinct design philosophies, not a "which is better" question

**Decisions Made:**
- Article slug: `claude-code-vs-codex`, category: `tools`, lang: `zh`
- Related compare: `claude-code-vs-cursor`; related topics: `claude-code`, `codex`
- Linked to existing blog posts: `codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-enterprise-engineering-ramp-shopify-spotify`

**Lessons Learned:**
- Claude Code = real-time pair programming, full local access, deep programmability (CLAUDE.md + Skills + Hooks + MCP)
- Codex = async task dispatch, cloud sandbox, parallel execution, safer isolation but limited extensibility
- The two tools are complementary: use Claude Code for complex/contextual tasks, Codex for batch/parallel small tasks

**Action Items:**
- Draft file should be saved to `drafts/` — verify it was written there
- May want to check/update `wiki/index.md` if a new wiki page on Codex comparison was created
- Consider ingesting Codex-related sources into `raw/` if not already present, to ensure wiki claims are source-backed