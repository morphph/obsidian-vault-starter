# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Codex subagents vs Claude Code subagents for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Codex uses cloud sandbox (frozen repo snapshots, container isolation) vs Claude Code uses local terminal (shared working directory, optional worktree isolation)
- Custom agent config: Codex uses natural language prompts (external to codebase, no versioning) vs Claude Code uses file-based system (CLAUDE.md, SKILL.md, hooks — version-controlled)
- Orchestration: Codex follows map-reduce pattern; Claude Code supports both parallel-independent and sequential-dependent within one session

**Decisions Made:**
- Article positions both tools as complementary, not competing: Codex for batch/async/large-scale parallel; Claude Code for interactive/multi-step/team-standardized
- Practical workflow example uses "update all deprecated API calls" as concrete comparison scenario
- Cost framing: Codex charges compute + tokens per sandbox; Claude Code only charges API tokens (local execution)

**Lessons Learned:**
- Codex parallel limit is architectural (independent sandboxes, no cross-agent communication); Claude Code parallel limit is practical (3-5 agents effective, parent synthesis is the bottleneck)
- "Prompt drift" is a real team problem — different members using slightly different Codex prompts get inconsistent results; SKILL.md solves this
- Codex optimizes for **developer time** (walk away); Claude Code optimizes for **total time + control** (stay engaged, finish faster)
- Worktree isolation in Claude Code gives sandbox-like benefits without leaving local environment

**Action Items:**
- Article references several internal links that need to exist: `/blog/claude-code-subagents-examples`, `/blog/claude-code-seven-programmable-layers`, `/blog/claude-code-agent-teams`, `/blog/agent-harnesses-2026`, `/glossary/agentic-coding` — verify these are published or queued
- Consider ingesting this into wiki as a page on subagent architecture patterns (covers both Codex and Claude Code ecosystems)