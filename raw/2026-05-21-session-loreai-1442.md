# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Codex custom agents vs Claude Code subagents for multi-agent workflows.

**Key Exchanges:**
- Detailed architectural comparison: Codex agents = pre-built profiles selected from a menu, cloud-sandboxed, async PR output; Claude Code subagents = dynamically composed at spawn time via prompts/skills/types, local environment, real-time coordination
- Codex uses `codex.md` (repo-level, applies to all agents) + dashboard profiles (per-agent); Claude Code uses `CLAUDE.md` + `SKILL.md` files + `subagent_type` parameter + per-spawn prompts

**Decisions Made:**
- Article positioning: not either/or — many teams use both platforms for different workflow segments
- Practical parallel subagent ceiling for Claude Code: 3-5 per spawn for complex tasks
- Codex inter-agent communication: none — must orchestrate dependencies manually via sequential task submission

**Lessons Learned:**
- Codex's `codex.md` cannot define per-agent instructions at repo level — must use dashboard for that
- SKILL.md is Claude Code-only; translating to Codex requires reformatting into `codex.md` + dashboard instructions
- Key differentiator is the **coordination layer**: Claude Code's parent agent synthesizes across subagent results; Codex has no equivalent
- Codex async model = developer parallelizes their own time; Claude Code sync model = developer present but gets immediate iteration
- Security tradeoff: Codex container isolation stronger for enterprise; Claude Code shared environment more practical for local dev

**Action Items:**
- Article references several internal links (`/blog/9-principles-writing-claude-code-skills-that-actually-work`, `/blog/claude-code-agent-teams`, `/blog/claude-code-subagents-examples`, `/blog/claude-code-hooks-a-complete-guide`, `/blog/claude-code-complete-guide`, `/glossary/agentic-coding`) — ensure these exist or are queued for creation
- Consider ingesting this article into wiki as a page on multi-agent architecture patterns (covers Codex, Claude Code, subagent coordination, SKILL.md vs codex.md)