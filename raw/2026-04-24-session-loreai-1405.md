# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User ingested or reviewed a detailed comparison article between Claude Code and OpenAI Codex as a potential raw source for the wiki.

**Key Exchanges:**
- Article covers: interaction model, project configuration, multi-agent execution, security/data handling, developer experience, pricing, and decision framework for choosing between the two tools.

**Decisions Made:**
- N/A (no interactive decisions visible — this appears to be a context flush from a reading/ingestion session)

**Lessons Learned:**
- Claude Code = interactive/exploratory (pair programming model); Codex = async/task delegation (ticket model)
- Claude Code keeps code local (API inference only); Codex runs code in ephemeral cloud containers with network disabled
- Claude Code config: `CLAUDE.md` + `SKILL.md` + memory + MCP; Codex config: `AGENTS.md` only — simpler but less extensible
- Claude Code agent teams coordinate via isolated git worktrees; Codex parallelism = independent cloud containers (no cross-task coordination)
- Pricing: Claude Code Pro $20/mo vs Codex requires ChatGPT Pro $200/mo — Claude Code significantly cheaper for light/moderate use
- Combined workflow pattern: use Claude Code for interactive exploration + architecture, then hand off well-defined tasks to Codex

**Action Items:**
- Consider ingesting this article as `raw/` source and creating a `wiki/claude-code-vs-codex.md` page covering the comparison framework, pricing tiers, and the combined workflow pattern