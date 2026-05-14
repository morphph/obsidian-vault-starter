# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on/reviewing a comparative article about Codex subagents vs Claude Code subagents for the LoreAI blog.

**Key Exchanges:**
- Detailed technical comparison of multi-agent architectures: Codex (task-level prompting, cloud containers, async batch model) vs Claude Code (typed agent specializations, local execution, interactive orchestration)
- Codex customization requires OpenAI Agent SDK (Python code); Claude Code uses built-in `subagent_type` primitives (Explore, Plan, codex-rescue, general-purpose) + prompt-based briefing
- Claude Code supports real-time coordination via `SendMessage`, foreground/background execution, and worktree isolation; Codex tasks are independent and cannot communicate mid-execution

**Decisions Made:**
- Article frames platforms as complementary, not competitive — "Many advanced teams use both"
- Claude Code's `codex:codex-rescue` subagent type is highlighted as the bridge between platforms
- Cost model distinction: Codex bundled into ChatGPT plans (predictable); Claude Code is per-token API billing (pay-for-use)

**Lessons Learned:**
- Codex parallelism is effectively unlimited (cloud) but tasks can't coordinate; Claude Code parallelism is limited (~3-5 agents locally) but supports multi-step orchestration patterns (research→implement→review)
- Codex container isolation means no access to local services, env vars, or uncommitted changes — important tradeoff for local-state-dependent codebases
- CLAUDE.md and SKILL.md propagate to all Claude Code subagents automatically; Codex requires per-task configuration
- The harness around the model often matters more than the model itself for agent effectiveness

**Action Items:**
- Article references several internal links that need to exist: `/blog/claude-code-subagents-examples`, `/blog/agent-harnesses-2026`, `/blog/codex-vscode`, `/blog/codex-for-open-source`, `/blog/codex-for-students`
- Consider ingesting this article into wiki as a page on multi-agent architecture patterns
- Potential wiki pages: `codex-subagents.md`, `claude-code-subagents.md`, `multi-agent-patterns.md`