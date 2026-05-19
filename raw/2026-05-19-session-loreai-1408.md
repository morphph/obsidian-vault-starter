# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted a Chinese comparison article (`claude-code-vs-codex`) for the LoreAI blog.

**Key Exchanges:**
- Generated a full-length comparison piece covering architecture, workflow, pricing, and use-case recommendations for Claude Code vs OpenAI Codex

**Decisions Made:**
- Framed the core distinction as **local terminal Agent (Claude Code) vs cloud sandbox Agent (Codex)** — interactive vs async
- Positioned neither tool as outright winner; recommended complementary use (Claude Code for interactive/deep-context work, Codex for batch/parallel tasks)
- Used internal cross-links to existing LoreAI content: codex-complete-guide, claude-code-extension-stack, claude-code-agent-teams, etc.

**Lessons Learned:**
- Codex's sandbox isolation (no network by default) is a genuine security advantage worth highlighting
- Pricing comparison is nuanced: Codex bundled in ChatGPT Pro ($200/mo), Claude Code has API pay-per-token + Max tiers ($100-200/mo) — neither is universally cheaper
- Claude Code's four-layer extension stack (Skills/Hooks/Agents/MCP) is a major differentiator for customizability; Codex has no equivalent programmable extension mechanism yet

**Action Items:**
- Article needs to be saved to `drafts/` and indexed if not already done
- Verify all internal cross-links resolve to existing published pages
- Monitor for Codex API pricing changes (currently subscription-only, may shift)