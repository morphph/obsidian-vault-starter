# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex vs Claude Code multi-agent architectures.

**Key Exchanges:**
- Detailed architectural comparison: Codex uses task-parallel isolation (independent sandboxed containers), Claude Code uses hierarchical subagents (parent-child with context passing)
- Codex: `AGENTS.md` flat config → every task sees same instructions. Claude Code: layered system (`CLAUDE.md` + `.claude/agents/` + skills + hooks)
- Codex tasks run in cloud sandboxes with network disabled by default; Claude Code runs locally with full filesystem/shell access

**Decisions Made:**
- Article verdict: Codex better for independent batch tasks (simpler, safer sandbox); Claude Code better for coordinated multi-step workflows needing context sharing
- Practical recommendation framed as "start with tool matching current workflow" rather than picking a winner
- Article includes internal cross-links to other LoreAI posts (extension stack, subagent examples, agent teams)

**Lessons Learned:**
- Codex's isolation is both strength (no interference, no cascading failures) and limitation (no inter-task communication)
- Claude Code's shared filesystem is both strength (context flow) and risk (concurrent agents can conflict — mitigated by worktree isolation)
- Codex pricing is subscription-bundled (ChatGPT Pro/Team/Enterprise); Claude Code is usage-based per-token across all subagents — costs scale with parallel subagent usage
- Key differentiator: Claude Code subagents can iterate (Explore → discover rename → inform next agent); Codex tasks are fire-and-forget with no feedback loops

**Action Items:**
- Article references several internal links (`/blog/claude-code-agent-teams`, `/blog/claude-code-subagents-examples`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/codex-for-students`) — ensure these exist or are planned
- Wiki pages to update/create: Codex multi-agent model, Claude Code subagent architecture, comparison of agent orchestration patterns