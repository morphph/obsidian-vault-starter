# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Claude Code subagents vs OpenAI Codex multi-agent workflows.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code uses built-in subagents (Explore, Plan, code-reviewer, general-purpose) spawned via `Agent` tool within a single session; Codex uses isolated cloud sandbox tasks requiring external orchestration via the Agents SDK
- Custom agent configuration: Claude Code uses `.claude/agents/*.md` markdown files (version-controlled, PR-reviewable); Codex uses Python `Agent` classes with the Agents SDK
- Isolation models: Codex = cloud container sandboxes (strongest isolation, no local access); Claude Code = git worktree isolation (flexible, local environment access)

**Decisions Made:**
- Article verdict: Claude Code is the more practical option for most engineering teams due to built-in coordination and zero-config agent specialization; Codex wins on isolation/security for regulated environments
- Positioning angle: "ready-to-use system" (Claude Code) vs "build-your-own orchestration" (Codex)

**Lessons Learned:**
- Claude Code subagents can share intermediate state within a session; Codex tasks are fire-and-forget with no inter-task communication
- Claude Code custom agents as markdown lowers adoption barrier — non-engineers can read/modify agent definitions
- Key tradeoff: markdown agents sacrifice Turing-complete routing flexibility for dramatically less setup
- `run_in_background` flag enables parallel subagent execution in Claude Code
- Codex's Agents SDK and Codex product are distinct — SDK handles coordination, Codex handles code generation

**Action Items:**
- Article references companion posts: "agent teams guide," "subagent examples," "complete Claude Code guide," "Codex guide" — ensure these are ingested/linked in wiki
- Article is ready for drafts/ — covers Claude Code subagents, Codex multi-agent, Agents SDK as wiki-worthy topics