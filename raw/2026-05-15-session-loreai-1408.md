# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a comparison article — "Claude Code vs Codex: Which AI Coding Agent Should You Use?" for LoreAI blog.

**Key Exchanges:**
- Produced a full-length comparison article covering architecture, features, pricing, and workflow fit for Claude Code (Anthropic) vs OpenAI Codex

**Decisions Made:**
- **Core framing:** Local agent (Claude Code) vs cloud sandbox (Codex) as the primary architectural axis — all other tradeoffs flow from this
- **Not a "winner" piece:** Verdict positions both as complementary — Claude Code for interactive/iterative work, Codex for async/batch tasks
- **Slug and metadata:** `claude-code-vs-codex`, category `tools`, cross-linked to existing guides (`claude-code-complete-guide`, `codex-complete-guide`, etc.)

**Lessons Learned:**
- Claude Code's advantage centers on full local environment access (auth CLIs, local services, custom build tools) and real-time steering; Codex's advantage is parallel cloud execution and fire-and-forget workflow
- Codex network isolation (no outbound calls from sandbox) is a significant constraint for projects with external dependencies
- Pricing models are fundamentally different: Claude Code = usage-based tokens; Codex = bundled in ChatGPT subscription tiers
- Both tools coexist in the same repo — `CLAUDE.md` and `AGENTS.md` are mutually ignored

**Action Items:**
- Article is drafted but needs commit + push per git workflow rules
- Related pages referenced (`codex-complete-guide`, `codex-vscode`, `codex-for-students`, `codex-for-open-source`) — verify these exist or are planned
- Consider ingesting this comparison's key claims into wiki pages for `claude-code` and `codex` topics