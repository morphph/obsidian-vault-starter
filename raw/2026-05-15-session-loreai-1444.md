# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a detailed comparison article: Codex (OpenAI) vs Claude Code subagent architectures for multi-agent workflows.

**Key Exchanges:**
- Detailed technical comparison of two multi-agent paradigms: Codex's cloud-sandbox task farming vs Claude Code's local coordinated agent teams
- Analysis of custom agent configuration stacks (Codex: system prompt + AGENTS.md + setup.sh vs Claude Code: CLAUDE.md + SKILL.md + Hooks + MCP + typed agents)

**Decisions Made:**
- **Decision framework distilled:** "Do your agents need to talk to each other?" → Yes = Claude Code, No = Codex
- **Hybrid model endorsed:** Claude Code as daily driver for interactive work, Codex as batch processor for independent tasks
- **Parallel pattern taxonomy:** "Task farming" (Codex) vs "Coordinated agent teams" (Claude Code) — each suits different decomposition styles

**Lessons Learned:**
- Codex cold-start overhead (clone → install → build context) is the key tradeoff for isolation; makes dependent task chains expensive
- Claude Code practical concurrency ceiling is ~3-7 sub-agents before local resource contention degrades performance
- Codex lacks structural agent-type differentiation — specialization is prompt-only, not tool-access-restricted
- Shared context in Claude Code sub-agents reduces redundant token usage vs Codex's per-task re-reading
- Worktree isolation in Claude Code mitigates filesystem conflict risk when running parallel agents

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/blog/codex-vscode`, `/blog/agent-harnesses-2026`, etc.) — ensure these exist or are created before publishing
- FAQ section covers common objections — good candidate for standalone wiki entries on `codex-vs-claude-code.md` and `multi-agent-patterns.md`
- The "2026 hybrid agent harness" trend is worth tracking as a wiki concept page