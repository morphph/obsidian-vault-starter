# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/draft comparing Claude Code vs OpenAI Codex as AI coding tools — architecture, workflows, pricing, and use cases.

**Key Exchanges:**
- Claude Code = interactive, local-first, terminal-based AI pair-programmer; Codex = async, cloud-sandboxed task engine
- Claude Code runs with local permissions (soft trust boundary via approval prompts); Codex runs in isolated containers (hard sandbox, no local access)
- Claude Code customization stack: CLAUDE.md → SKILL.md → Hooks → MCP servers; Codex only has AGENTS.md (no hooks, skills, or MCP equivalent)

**Decisions Made:**
- Framing: tools are complementary, not interchangeable — different philosophies (interactive vs async, local vs cloud)
- Decision rule for security: regulated/enterprise environments favor Codex's hard isolation; full-environment access favors Claude Code
- Decision rule for workflow: need mid-task steering → Claude Code; well-scoped independent batch tasks → Codex
- Pricing comparison anchored at $20/mo entry for both; Claude Code API scales unlimited, Codex capped by subscription tier

**Lessons Learned:**
- Codex's async model breaks down when tasks need clarification, iterative exploration, or context beyond the repo
- Claude Code's agent teams bring parallelism to the interactive model without losing the feedback loop
- For monorepos, local filesystem access + agent teams > repo snapshots in sandboxes
- Codex available free for qualified open-source maintainers and students (access expansion programs)

**Action Items:**
- Article references several internal links (`/blog/claude-code-hooks-mastery`, `/blog/claude-code-agent-teams`, `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/blog/codex-vscode`, `/compare/claude-code-vs-cursor`) — verify these exist or queue for creation
- Could be ingested into wiki as a source covering: Claude Code capabilities, Codex capabilities, AI coding tool landscape, pricing models