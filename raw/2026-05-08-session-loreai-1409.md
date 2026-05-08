# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article: Claude Code vs OpenAI Codex for the blog/wiki system.

**Key Exchanges:**
- Generated a full-length comparison article (`claude-code-vs-codex`) covering architecture, workflow, pricing, and use-case recommendations

**Decisions Made:**
- Framed the core distinction as **"pair programming (Claude Code) vs task delegation (Codex)"** — local sync Agent vs cloud async Agent. This is the central mental model for the piece.
- Positioned them as **different paradigms, not direct competitors** — many devs use both
- Chose to highlight Claude Code's 7-layer programmable architecture (CLAUDE.md → SKILL.md → Hooks → MCP) as its key differentiator vs Codex's simplicity/parallelism

**Lessons Learned:**
- Codex's sandboxed no-network default is both a security strength and a practical limitation (can't access local DBs, authenticated APIs)
- Codex's pricing is bundled into ChatGPT Pro ($200/mo) — zero marginal cost for existing subscribers vs Claude Code's token-based billing
- codex-1 is an RL-optimized o3 variant trained specifically to "write then test" — different training philosophy from Claude models

**Action Items:**
- Article needs to be saved to `drafts/` and cross-linked with existing wiki pages (`claude-code`, `codex`, `agentic-coding`)
- Related compare page `claude-code-vs-cursor` is referenced but should verify it exists
- Frontmatter references several blog slugs (`codex-complete-guide`, `codex-vscode`, `codex-for-students`, `codex-for-open-source`) — verify all are live before publishing