# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Codex vs Claude Code multi-agent architectures for the blog/wiki.

**Key Exchanges:**
- Detailed architectural comparison: Codex uses independent sandboxed containers per task (no inter-task communication); Claude Code uses parent-child orchestration with typed subagents (Explore, Plan, general-purpose) that share context through the parent
- Claude Code's customization stack: toolset restrictions, model selection per agent, SKILL.md system, git worktree isolation for parallel editing
- Codex's customization is prompt-level only — no enforcement mechanism for tool/behavior constraints

**Decisions Made:**
- Article verdict: Claude Code is more capable for coordinated multi-agent work; Codex wins for "embarrassingly parallel" batch tasks — recommend teams use both
- Four workflow patterns identified with clear winner for each: Batch Refactoring (Codex), Feature Implementation with Discovery (Claude Code), Code Review Automation (tie), Multi-Agent Research+Implementation (Claude Code decisively)

**Lessons Learned:**
- Codex sandbox = safer for unsupervised/fire-and-forget; Claude Code local execution = more powerful but needs supervision or configured permission boundaries
- Codex tasks cannot share context without human-in-the-loop bridging between sequential runs — fundamental architectural limitation for multi-step workflows
- Claude Code worktree isolation makes parallel file-editing subagents feasible but more complex to orchestrate than Codex's native cloud parallelism
- Cost model difference: Codex flat subscription vs Claude Code per-token — heavy multi-agent usage favors comparing projected tokens against flat rate

**Action Items:**
- Article references several internal links (`/blog/claude-code-agent-teams`, `/blog/codex-complete-guide`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — verify these exist or are planned before publishing
- Consider ingesting this into wiki as a page on multi-agent architecture patterns (covers both platforms comprehensively)