# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a blog post comparing Claude Code vs OpenAI Codex as AI coding agents.

**Key Exchanges:**
- Detailed comparison across security models (Claude Code's permission-based approval vs Codex's network-isolated sandbox), pricing tiers, and workflow paradigms (interactive/synchronous vs async/PR-based)

**Decisions Made:**
- **Positioning framework:** Claude Code = interactive, deep-control tool for senior devs; Codex = async task dispatcher for well-specified work
- **Pricing angle:** Claude Pro ($20/mo) positioned as better value for moderate individual use vs ChatGPT Pro ($200/mo), but acknowledged ChatGPT Team ($25-30/seat) can beat API usage-based billing for teams
- **Verdict structure:** Not a single winner — segmented by persona (senior devs → Claude Code, throughput-focused teams → Codex) with hybrid "use both" recommendation
- **Cross-links:** Ties to existing blog content (Claude Code complete guide, Codex complete guide, hooks guide, skills guide, Claude Code vs Cursor comparison)

**Lessons Learned:**
- Claude Code's CLAUDE.md / skills / hooks configuration is a compounding investment — worth calling out as a differentiator
- Codex's sandbox limitation (no network = can't test API integrations) is a practical gotcha worth flagging
- Context duplication is the main friction point when using both tools — project standards don't transfer between them

**Action Items:**
- Ensure linked pages exist: `/blog/codex-complete-guide`, `/compare/claude-code-vs-cursor`, `/blog/claude-code-agent-teams`
- Article references pricing as of drafting date — will need periodic updates as both products evolve rapidly
- Consider ingesting this as a raw source once published, to update wiki pages on [[Claude Code]] and potentially create a [[Codex]] wiki page