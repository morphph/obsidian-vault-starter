# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/drafting a comparison article on Codex vs Claude Code multi-agent (subagent) workflows.

**Key Exchanges:**
- Detailed pattern comparison across 3 workflow types: parallel independent tasks, research-then-implement, and large-scale refactoring
- Codex = cloud-isolated containers, fire-and-forget; Claude Code = in-session orchestration with parent coordination

**Decisions Made:**
- **Codex best for**: batch processing, strict isolation, async team workflows, CI/CD integration
- **Claude Code best for**: coordinated multi-step workflows, exploratory investigation, real-time oversight, custom agent libraries, local dev context
- **Core tradeoff framed as**: isolation vs. orchestration
- **Recommendation**: start with Claude Code for interactive dev needing coordination; start with Codex for automation pipelines with self-contained units; many teams use both

**Lessons Learned:**
- Codex tasks cannot communicate mid-execution — coordination only happens post-completion
- Claude Code sub-agents eliminate manual handoffs in sequential workflows (research → plan → implement)
- Neither tool is inherently cheaper — cost depends on prompt efficiency and workflow structure
- Claude Code has a higher learning curve (agent types, foreground/background, worktree isolation, prompt design) but compounds value via reusable skill files
- Codex debugging is simpler but isolated; Claude Code debugging is interactive but harder to trace after the fact

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/blog/agent-harnesses-2026`, `/blog/effective-harnesses-for-long-running-agents`) — verify these exist or queue them for creation
- Consider ingesting this as a wiki page (e.g., `wiki/codex-vs-claude-code-subagents.md`) if not already tracked