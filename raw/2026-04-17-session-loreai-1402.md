# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a blog article comparing Claude Code vs OpenAI Codex for potential wiki ingestion

**Key Exchanges:**
- No interactive Q&A — context is a standalone comparison article, not a live session

**Decisions Made:**
- N/A (no decisions made in session)

**Lessons Learned:**
- **Claude Code vs Codex — core distinction**: Claude Code = interactive pair-programmer (local execution, real-time control); Codex = async task worker (cloud sandbox, parallel queue)
- **Context systems differ**: Claude Code uses layered `CLAUDE.md` + `SKILL.md` + hooks + MCP; Codex uses a single `AGENTS.md` with no hook system or skill templates
- **Security split**: Claude Code keeps code local (only prompts/file contents sent to API); Codex clones repo into OpenAI cloud sandbox — disqualifying for some regulated environments
- **Pricing model**: Claude Code = per-token API or Pro/Max subscription; Codex = bundled with ChatGPT Pro ($200/mo), Team ($30/user/mo), or Enterprise — no standalone access
- **Workflow fit**: Claude Code better for ambiguous/exploratory tasks; Codex better for batch well-specified tasks (test gen, bug fixes, API migrations)
- **Complementary, not competing**: Best teams use both — Claude Code for architecture/debugging, Codex for parallel task queue

**Action Items:**
- This article is strong raw material for a `claude-code-vs-codex.md` wiki page — consider running `/ingest` on the source