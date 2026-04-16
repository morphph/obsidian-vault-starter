# Session Capture: loreai

**Date:** 2026-04-16
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison draft article: Claude Code vs OpenAI Codex

**Key Exchanges:**
- Article produced for `/zh/compare/claude-code-vs-codex` (slug: `claude-code-vs-codex`)
- Category: `compare`, lang: `zh`, relates to glossary entries `agentic-coding`, `agent-sdk`

**Decisions Made:**
- Core framing: local-first (Claude Code) vs cloud-first (Codex) — not a quality comparison but an architectural philosophy split
- Positioned Claude Code as "sync pair programmer" and Codex as "async contractor fleet"
- Combined strategy recommended: Claude Code for deep dev, Codex for routine batch tasks

**Lessons Learned:**
- The most meaningful differentiator is execution model (local shell vs cloud sandbox), not model quality — context quality matters more than tool choice
- CLAUDE.md / SKILL.md system (Claude Code) vs AGENTS.md (Codex) is the practical context-programming comparison worth tracking

**Action Items:**
- Draft file may need to be saved to `drafts/` if not already done — confirm path
- Cross-link pages: `codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-vs-cursor` should link back to this compare page once published
- Consider creating/updating wiki page for `codex.md` if not yet tracked in `wiki/index.md`