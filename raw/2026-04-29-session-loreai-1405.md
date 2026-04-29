# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/ingesting a comprehensive comparison article: Claude Code vs OpenAI Codex.

**Key Exchanges:**
- Detailed feature-by-feature comparison of Claude Code (Anthropic) and OpenAI Codex as agentic coding tools

**Decisions Made:**
- Article verdict: Claude Code recommended for most individual developers; Codex for teams parallelizing at scale
- Framing: two modes of agentic coding — **interactive** (Claude Code) vs **async task delegation** (Codex) — positioned as complementary, not competing

**Lessons Learned:**
- Codex sandbox has **no outbound network** during execution — limits it to self-contained repo tasks; Claude Code's local execution handles broader task types
- Codex sweet spot: well-defined tasks + strong test suites + batch submission; Claude Code sweet spot: exploratory work, complex environments, real-time iteration
- Pricing gap is significant: Claude Code Pro $20/mo vs Codex Pro $200/mo for full access
- Codex lacks equivalent of CLAUDE.md/SKILL.md persistent context system — context must be provided per-prompt
- Common hybrid pattern: Claude Code for active development, Codex for parallelizable batch work (bug fixes, test generation, boilerplate)
- Second hybrid pattern: Claude Code for iteration, then Codex for independent review of changes
- Both tools can operate on the same repo without conflict (local vs cloud execution)

**Action Items:**
- Wiki pages to create/update: [[codex]], [[agentic-coding]], [[claude-code]] with comparison data
- Cross-reference with existing wiki content on Claude Code pricing tiers (Pro $20, Max $100-200, API billing)
- Article references related posts: claude-code-vs-cursor, claude-code-complete-guide, codex-complete-guide, codex-for-open-source, codex-for-students — check if these need wiki entries