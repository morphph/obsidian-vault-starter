# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a detailed article comparing Claude Memory vs CLAUDE.md — the two persistence mechanisms in Claude Code.

**Key Exchanges:**
- Comprehensive decision framework for what goes in CLAUDE.md vs Claude Memory vs neither
- Performance impact analysis: CLAUDE.md fully loaded every turn; Memory index loaded but files read on-demand

**Decisions Made:**
- CLAUDE.md should stay under ~200 lines for optimal context window performance (500-line file ≈ 2,000–3,000 tokens consumed every turn)
- Memory MEMORY.md index truncates at ~200 lines; keep entries under 150 chars each
- Personal preferences belong in Memory even on solo projects (avoids polluting shared config if repo is ever cloned)
- Recurring memory patterns across team members should be promoted to CLAUDE.md rules

**Lessons Learned:**
- CLAUDE.md = project constitution (shared, durable, version-controlled, available in CI). Memory = personal relationship (local, fragile, auto-learning, project-scoped)
- Memory cannot override CLAUDE.md — CLAUDE.md is authoritative when they conflict
- Memory does NOT work in CI/CD (lives in `~/.claude/projects/`, not in repo)
- CLAUDE.md supports directory-level scoping (monorepo packages); Memory is flat per-project
- Overloading CLAUDE.md with knowledge-base content degrades performance — move detailed docs to `skills/*/SKILL.md` or other on-demand files
- Common antipattern: treating CLAUDE.md as a knowledge base instead of a rule set

**Action Items:**
- Consider auditing current `CLAUDE.md` against the 200-line guideline
- Could create a wiki page: `claude-code-persistence-layers.md` covering this CLAUDE.md vs Memory framework
- Relevant to existing wiki topics: [[Claude Code]] tooling, builder workflow optimization