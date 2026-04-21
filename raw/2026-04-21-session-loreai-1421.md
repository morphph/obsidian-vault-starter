# Session Capture: loreai

**Date:** 2026-04-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an article about Claude Code's two context systems — CLAUDE.md vs Claude Memory — for potential wiki ingestion.

**Key Exchanges:**
- Article explains the fundamental split: CLAUDE.md = shared team rules (deterministic, version-controlled); Claude Memory = personal adaptation layer (automatic, evolving, individual)
- Three-question decision framework: (1) Everyone or just me? (2) Derivable from code? (3) Still true in 3 months?
- FAQ clarifies CLAUDE.md always overrides Memory when they conflict — intentional hierarchy

**Decisions Made:**
- (Article recommendation) Start with CLAUDE.md for build commands + top 5 conventions; let Memory accumulate naturally through corrections
- Simple test: "Would my teammate need to know this?" → Yes = CLAUDE.md, No = Memory

**Lessons Learned:**
- CLAUDE.md should stay under 200 lines — entire file loads into context window every session
- Add `.claude/` to `.gitignore` — Memory files are private, CLAUDE.md travels with the repo
- Outdated CLAUDE.md is worse than none — actively misleads Claude (e.g., "use Webpack" after migrating to Vite)
- Four-layer hierarchy: project root CLAUDE.md → subdirectory CLAUDE.md → `~/.claude/CLAUDE.md` → project-scoped Memory
- Memory has natural decay — Claude treats old memories as potentially stale and cross-checks against current state

**Action Items:**
- Consider ingesting this as a raw source for a `claude-code-context-systems.md` wiki page covering the CLAUDE.md vs Memory architecture