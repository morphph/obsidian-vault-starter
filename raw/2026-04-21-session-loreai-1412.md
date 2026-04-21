# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison draft article: "Claude Code vs Codex：两大 AI 编程 Agent 深度对比"

**Key Exchanges:**
- Draft produced a full `/zh/compare/claude-code-vs-codex` article comparing Claude Code (local terminal agent) vs OpenAI Codex (cloud async agent)
- Core framing: these solve *different* problems, not competing directly — Claude Code = real-time interactive dev, Codex = batch parallel task dispatch

**Decisions Made:**
- Article structure: TL;DR → overview each → feature table → architecture philosophy → workflow UX → customizability → OSS ecosystem → when to choose each → FAQ
- Positioned the two tools as complementary, not substitutes — recommended mixed-use workflow
- Linked to existing internal articles: `codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-agent-teams`, `codex-vscode`, `codex-for-open-source`, `claude-code-vs-cursor`

**Lessons Learned:**
- Key architectural distinction worth encoding in wiki: Claude Code = "default open + permission controls", Codex = "default isolated sandbox" — two different security models
- Codex's parallel container architecture is its primary differentiator; Claude Code's 7-layer programmable stack (CLAUDE.md → SKILL.md → Hooks → MCP) is its primary differentiator
- Codex for Open Source (free quota for OSS projects) is a notable ecosystem strategy worth tracking separately

**Action Items:**
- Confirm draft was saved to `drafts/` directory
- Verify all internal `[[wikilinks]]` and `/zh/blog/` paths resolve correctly
- Consider creating/updating `wiki/codex.md` if it doesn't already capture the cloud-sandbox-async architecture model