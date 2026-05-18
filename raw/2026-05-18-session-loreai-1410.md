# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/drafting a blog post comparing Claude Memory vs CLAUDE.md as persistence layers in Claude Code.

**Key Exchanges:**
- Full article covering architecture, use cases, and practical guidance for Claude Code's two persistence systems

**Decisions Made:**
- CLAUDE.md = shared project constitution (version-controlled, deterministic, team-aligned)
- Memory = personal learned context (local, auto-accumulated, individual optimization)
- They are complementary layers, not competing — CLAUDE.md is the foundation, Memory is personalization on top
- If forced to choose one: start with CLAUDE.md (prevents mistakes > prevents repetition)
- CLAUDE.md takes precedence over Memory when they conflict

**Lessons Learned:**
- Anti-pattern: putting personal preferences in CLAUDE.md or project rules in Memory
- Memory's maintenance risk is staleness — sprint goals, team assignments decay fast; periodically prune `.claude/projects/` files
- CLAUDE.md sits at project-level in Claude Code's seven programmable layers; Memory sits at user-level
- Useful feedback memories that reflect project-wide rules should be migrated into CLAUDE.md
- Memory files should NOT be checked into version control — they'd impose one person's style on the team
- CLAUDE.md supports hierarchical merging: global `~/.claude/CLAUDE.md` → project root → subdirectory, with more specific files winning

**Action Items:**
- This content is a draft article — should be ingested into `wiki/` as a Claude Code knowledge page (e.g., `wiki/claude-code-memory-vs-claude-md.md`)
- Cross-link with existing wiki pages on [[Claude Code]] and builder tools
- Article references several other blog posts (complete guide, seven programmable layers, enterprise engineering, extension stack) — those could be future ingest targets