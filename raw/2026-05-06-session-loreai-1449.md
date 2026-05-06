# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Claude Code subagents vs Codex custom agents for multi-agent workflows.

**Key Exchanges:**
- Claude Code uses a **parent-child orchestration model** — one session spawns typed sub-agents (Explore, Plan, general-purpose, code-reviewer) that report back in real time; parent adapts strategy based on intermediate results
- Codex uses a **task-dispatch model** — independent agents run in isolated cloud containers asynchronously; no real-time coordination between them
- Claude Code customization is file-based (CLAUDE.md, SKILL.md) and version-controlled in repo; Codex customization lives in the platform with freeform agent configs + containerized environments

**Decisions Made:**
- **Orchestration verdict:** Claude Code wins for adaptive, coordinated tasks; Codex wins for batch/independent work
- **Customization verdict:** Codex more flexible for agent roles/environments; Claude Code more portable and version-controllable
- **Overall verdict:** Interactive orchestration (Claude Code) vs async dispatch (Codex) — complementary, not competing
- Recommended combo: Claude Code for daily interactive dev (debugging, refactoring); Codex for standardized batch ops (cross-repo test gen, doc sweeps)

**Lessons Learned:**
- Claude Code sub-agent types are predefined (4 types) — you can't create entirely new agent types with custom tool access
- Codex agents cannot dynamically adjust based on what other agents discover mid-run
- Codex agent configs lack built-in version control mechanism (don't live in repo)
- Practical parallel sub-agent sweet spot for Claude Code: 2-5 concurrent agents
- Each Codex task starts fresh — no incremental context across tasks

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/blog/codex-complete-guide`, etc.) — ensure those target pages exist in wiki or drafts before publishing
- Consider ingesting this article's key claims into wiki pages: one for Claude Code architecture, one for Codex architecture, one comparison page