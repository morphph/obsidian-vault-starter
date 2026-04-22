# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing curated AI news digest items (scored list of ~25 sources) for the 2026-04-22 newsletter cycle.

---

**Key Exchanges:**
- No interactive Q&A — this was a batch review/curation pass over scored items from multiple sources (Twitter, HN, RSS feeds).

---

**Decisions Made:**
- Top items flagged for coverage across categories: LAUNCH (GPT-Image-2), INSIGHT (Meta keystroke capture, Claude Code Pro tier change, Kimi K2.6), TECHNIQUE (LLM randomness trick, prompt caching), TOOL (CrabTrap, GoModel), BUILD (Agent-Simulator MCP, Kimi Code terminal), RESEARCH (economist replication study, MegaStyle)

---

**Lessons Learned:**
- **GPT-Image-2** (score 97) is the week's top story — thinking-capable image model, swept all Arena leaderboards on day 1; Emollick notes a *quality threshold* where AI-generated slides/papers become practically usable
- **Workplace surveillance for AI training** is an emerging pattern: Meta keystroke/mouse capture follows Atlassian's quiet data collection — worth tracking as a recurring topic
- **Claude Code exits Pro tier** — pricing signal that Anthropic is treating coding agents as a standalone premium SKU, not a subscriber benefit
- **Claude Code/Codex replication study**: produced more consistent results than 146 human economist teams — strong evidence for AI as credible research tool
- **CrabTrap** (Brex): LLM-as-judge HTTP proxy for agent safety — practical production pattern worth tracking
- **`/btw` or `CMD+;`** in Claude Code desktop = side-question shortcut without breaking main workflow

---

**Action Items:**
- Ingest high-score items (≥87) into wiki pages: GPT-Image-2, Kimi K2.6, Deep Research API MCP, Meta surveillance pattern, Claude Code pricing change
- Consider a wiki page on **agent safety patterns** (CrabTrap, LLM-judge proxies)
- Log this digest run in `wiki/log.md`