# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a detailed article comparing Claude Memory vs CLAUDE.md as context systems in Claude Code.

**Key Exchanges:**
- Article lays out two mental models: Memory = **accumulation model** (conversational, personal, self-maintaining); CLAUDE.md = **declaration model** (deliberate, team-visible, version-controlled)
- Memory captures context through natural interaction; CLAUDE.md requires intentional editing like infrastructure config

**Decisions Made:**
- **CLAUDE.md for team contracts:** build commands, quality gates, style guides, architecture boundaries, workflow rules — anything that must be consistent across developers
- **Memory for personal context:** role, preferences, behavioral corrections, accumulated project knowledge, external resource links
- **Precedence rule:** CLAUDE.md always overrides Memory if they conflict
- **Maintenance cadence:** CLAUDE.md needs quarterly review + updates in the same PR as related code changes; Memory self-corrects but needs occasional pruning

**Lessons Learned:**
- Stale CLAUDE.md is worse than no CLAUDE.md — Claude follows it faithfully even if outdated
- Memory has no staleness detection built-in for CLAUDE.md (unlike Memory entries which Claude verifies against current state)
- Memory serves as a **discovery mechanism** for patterns; once validated, promote team-relevant ones to CLAUDE.md as the **enforcement mechanism**
- MEMORY.md index truncates after 200 lines — keep entries concise
- Solo devs get most value from Memory with lowest effort; teams need CLAUDE.md as non-negotiable baseline

**Action Items:**
- Potential wiki pages: `claude-memory-vs-claude-md.md`, update `claude-code.md` or related pages with the two-model framework
- Source article references several related posts: claude-code-seven-programmable-layers, claude-code-extension-stack, claude-code-memory, 5-claude-code-skills — worth ingesting if not already in wiki