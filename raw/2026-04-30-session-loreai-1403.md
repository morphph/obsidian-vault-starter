# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Claude Code vs Codex (OpenAI) for the LoreAI blog.

**Key Exchanges:**
- Detailed feature-by-feature comparison covering: architecture (local vs cloud sandbox), workflow model (interactive vs async), multi-agent/parallel execution, IDE integration, safety models, pricing, and language support
- Decision frameworks provided for when to choose each tool

**Decisions Made:**
- **Positioning framework:** Claude Code = interactive pair programmer; Codex = async task delegator (junior dev you assign tickets to)
- **Key architectural distinction:** Claude Code runs locally in your environment; Codex runs in cloud sandbox (internet-isolated, disposable)
- **Recommendation matrix:** Solo devs/small teams → Claude Code; Engineering managers/team leads delegating scoped tasks → Codex; Budget allows both → use both for different task types
- **Ambiguity as selection criterion:** High ambiguity tasks → Claude Code's interactive loop; Low ambiguity tasks → Codex's async delegation

**Lessons Learned:**
- Codex sandbox cannot access private package registries, local databases, or external services — limits it to self-contained repos
- Claude Code's `CLAUDE.md` + skills system creates compounding returns over time; Codex treats each task as independent (no persistent project context)
- OpenAI introduced `AGENTS.md` as their equivalent to `CLAUDE.md`, but less structured
- Codex included in ChatGPT Pro subscription (effectively free if already paying); Claude Code is usage-based API or Claude Max flat rate
- Both tools can be used on the same project without conflict (Claude Code = local, Codex = GitHub PRs)

**Action Items:**
- Article references several internal links that need to exist: `/blog/agent-harnesses-2026`, `/compare/claude-code-vs-cursor`, `/blog/claude-code-complete-guide`, `/blog/codex-complete-guide`, `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/blog/codex-vscode`, `/blog/claude-code-remote-control-mobile`
- Wiki pages worth creating/updating: `codex.md` (OpenAI's coding agent), `claude-code-vs-codex.md` (comparison summary), update `claude-code.md` with agent teams and multi-model flexibility details