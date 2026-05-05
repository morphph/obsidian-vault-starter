# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article on Codex custom agents vs Claude Code subagents for multi-agent coding workflows.

**Key Exchanges:**
- Detailed architectural comparison: Codex = ephemeral cloud sandboxes (cold start, isolated, async); Claude Code subagents = in-session (shared filesystem, real-time, orchestrated by parent)
- Three practical workflow comparisons: test generation, codebase refactoring, code review

**Decisions Made:**
- Decision framework crystallized: **synchronous vs asynchronous** is the primary decision boundary
  - Need results now → Claude Code subagents
  - Can dispatch and review later → Codex custom agents
- Coupled tasks → Claude Code (parent orchestrates dependencies); Independent tasks → Codex (embarrassingly parallel)
- Hybrid recommended: Claude Code for active dev sessions, Codex for batch/team automation

**Lessons Learned:**
- Codex agents cannot communicate during execution — coordination is human/CI layer only
- Claude Code worktree isolation (`isolation: "worktree"`) is the middle ground between full local access and Codex's cloud sandbox
- Claude Code's skills/CLAUDE.md system = version-controlled agent instructions that evolve with codebase (vs Codex's separate profile management)
- Codex's named profiles enforce team standardization without relying on individual prompt craft
- Claude Code practical parallelism is bounded by context window/token budget, not a hard agent count

**Action Items:**
- Article references several internal links (`/blog/codex-complete-guide`, `/blog/claude-code-subagents-examples`, `/blog/claude-code-agent-teams`, etc.) — ensure these exist or are planned
- Consider ingesting this as a wiki page covering multi-agent architecture patterns (would complement existing builder-tools knowledge)