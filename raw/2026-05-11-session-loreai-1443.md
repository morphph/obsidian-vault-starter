# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a comparison article: Claude Code Subagents vs Codex Custom Agents for the LoreAI blog.

**Key Exchanges:**
- Produced a full `/compare` article covering architecture, features, use cases, and verdict for Claude Code subagents (local, real-time, shared-context) vs Codex custom agents (cloud, async, sandboxed)

**Decisions Made:**
- Framed the comparison around **synchronous vs asynchronous workflow** as the primary decision axis, not "which is better"
- Verdict: Claude Code subagents for interactive coordinated work; Codex custom agents for batch-style delegated tasks
- Positioned hybrid usage (both tools together) as the forward-looking recommendation

**Lessons Learned:**
- Claude Code subagents' key advantage is **context inheritance** — child agents start with parent's understanding rather than re-discovering from scratch
- Codex's key advantage is **container-level isolation** — agents can't interfere with each other or local environment
- Token efficiency differs: shared context (Claude Code) saves tokens for context-heavy tasks; per-task pricing (Codex) is simpler for many small independent tasks

**Action Items:**
- Article references several internal links (`claude-code-agent-teams`, `claude-code-subagents-examples`, `codex-complete-guide`, `codex-vscode`, etc.) — ensure these exist or are queued for creation
- No commit/push was observed in context — article may still need to be saved and deployed