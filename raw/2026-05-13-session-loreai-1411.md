# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a blog article comparing Claude Code's CLAUDE.md vs Memory persistence systems — their architecture, use cases, failure modes, and team dynamics.

**Key Exchanges:**
- Article provides a comprehensive framework for deciding what goes in CLAUDE.md vs Memory
- CLAUDE.md = deterministic, always-loaded, version-controlled, team-shared project config
- Memory = selective retrieval, personal, situational, ephemeral context
- CLAUDE.md hierarchy: `~/.claude/CLAUDE.md` (global) → repo root `CLAUDE.md` → directory-level — all merged and loaded every session

**Decisions Made:**
- **CLAUDE.md for load-bearing rules**: Security constraints, build gates, quality standards, coding conventions — anything that must never be skipped
- **Memory for personalization**: Role/expertise, behavioral feedback, ephemeral project state (deadlines, incidents), external references
- **Gray zone rule**: "Does every developer need to follow this?" → Yes = CLAUDE.md, No = Memory
- **Promotion pattern**: If you've told Claude something 3+ times across sessions and it keeps being relevant, promote it from Memory to CLAUDE.md
- **SKILL.md for overflow**: Detailed task-specific instructions that would bloat CLAUDE.md belong in on-demand SKILL.md files

**Lessons Learned:**
- CLAUDE.md consumes context window regardless of relevance — keep it concise, 1000+ lines is a scaling problem
- Memory fails stochastically (right info, inconsistently applied) vs CLAUDE.md fails predictably (wrong info, consistently applied) — different debugging strategies needed
- Memory has a freshness/staleness problem with no built-in pruning mechanism — requires quarterly manual review
- CLAUDE.md survives context compression (system prompt preserved); Memory loaded mid-conversation may get summarized away
- Most common mistake: putting team conventions in Memory instead of CLAUDE.md
- Second most common: cluttering CLAUDE.md with personal preferences

**Action Items:**
- Consider ingesting this as a wiki page (e.g., `wiki/claude-code-persistence.md`) covering CLAUDE.md vs Memory architecture
- Cross-reference with existing Claude Code wiki content if any
- This article references several related posts that could be future ingest targets: Claude Code's seven programmable layers, extension stack guide, memory system explainer, 9 principles for writing skills