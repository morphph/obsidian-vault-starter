# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex vs Claude Code subagent/custom agent architectures for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Codex uses container-per-task isolation (async, independent), Claude Code uses typed subagents within a single interactive session (real-time orchestration)
- Codex parallelism = task-level (independent containers); Claude Code parallelism = subagent-level (concurrent processes on local machine, orchestrator sees all results)
- Claude Code has explicit agent types (Explore, Plan, general-purpose, code-reviewer) with per-agent tool access/permissions; Codex has one agent type with different text instructions

**Decisions Made:**
- Framing: "async independence vs interactive orchestration" as the core tradeoff
- Verdict: not either/or — use Codex for overnight batch queues (independent bugs, tests, docs), use Claude Code for complex coordinated sessions (explore → plan → execute)
- Codex better for: strong isolation, GitHub-native teams, batch processing, simple customization
- Claude Code better for: multi-agent orchestration, deep codebase understanding, custom agent specialization, local env integration, programmable automation

**Lessons Learned:**
- Claude Code subagents share local environment — `worktree` isolation is opt-in, not default; still doesn't restrict shell access
- Codex customization is three layers: task-level instructions, repo-level config, system-level prompts — coarse-grained but straightforward
- Claude Code customization is four layers: built-in agent types, SKILL.md files, per-spawn agent config, CLAUDE.md project files — enables genuinely specialized agents
- Claude Code's "seven programmable layers" (hooks, MCP, skills, agents, etc.) provide extension points Codex doesn't expose
- Key limitation of Codex: no intra-task coordination; dependent tasks must be serialized or managed externally

**Action Items:**
- Article references several internal blog links (claude-code-agent-teams, codex-vscode, etc.) — ensure corresponding wiki pages exist
- Consider creating/updating wiki pages: `codex.md` (OpenAI Codex), `claude-code-subagents.md`, `agent-orchestration-patterns.md`