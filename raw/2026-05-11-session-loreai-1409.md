# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese comparison article (`claude-code-vs-codex`) for the LoreAI blog.

**Key Exchanges:**
- Produced a full-length comparison piece: Claude Code (local terminal agent) vs OpenAI Codex (cloud sandbox agent)
- Core framing: "real-time collaboration" vs "batch async dispatch" — all feature differences derive from this architectural split

**Decisions Made:**
- Positioned neither tool as outright winner; framed as complementary (Claude Code for interactive + context-heavy tasks, Codex for parallel batch jobs)
- Emphasized Claude Code's programmability advantage (4-layer extension stack: Skills, Hooks, Agents, MCP) as the key differentiator over Codex's simpler `AGENTS.md` config
- Cross-linked to existing site content: `codex-complete-guide`, `claude-code-extension-stack`, enterprise case studies, `claude-code-vs-cursor`

**Lessons Learned:**
- Codex's no-network sandbox constraint is the critical practical limitation — any test needing DB/external API won't run there
- Many teams end up using both tools together, not choosing one exclusively