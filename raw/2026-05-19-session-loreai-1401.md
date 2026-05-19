# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a Claude Code vs OpenAI Codex comparison article for LoreAI blog publication.

**Key Exchanges:**
- Article positions Claude Code as **interactive pair programmer** (real-time, terminal-native, deep customization) vs Codex as **async task runner** (dispatch-and-review, PR-oriented, sandbox-isolated)
- Detailed breakdown of customization stacks: Claude Code's layered system (CLAUDE.md → skills → hooks → MCP) vs Codex's simpler repo-level setup instructions

**Decisions Made:**
- **Framing:** Not direct competitors — different workflow optimizations. Verdict recommends using both together for different task types.
- **Audience angle:** Written for developers choosing between tools, with clear "when to choose" decision framework
- **Pricing framing:** Usage-based (Claude Code) vs bundled subscription (Codex). Light users → Codex cheaper via existing ChatGPT sub; heavy users → Claude Code offers model-tier flexibility.

**Lessons Learned:**
- Codex strengths: parallel task dispatch, clean sandbox per task (no session drift), accessible to non-developers via web UI, free with ChatGPT Plus (rate-limited)
- Claude Code strengths: mid-task steering, persistent project knowledge via CLAUDE.md/skills/hooks, local tool/DB/service access, agent harness architecture for custom automation
- Code quality depends more on underlying model + project context than the tool wrapper itself
- Codex's GitHub integration naturally produces PRs → fits code review workflows; Claude Code's sub-agent teams enable parallel work within a single interactive session

**Action Items:**
- Article references several internal links (`/blog/agent-harnesses-2026`, `/blog/claude-code-hooks-a-complete-guide...`, `/blog/5-claude-code-skills...`, `/compare/claude-code-vs-cursor`) — ensure these destination pages exist
- Article dated contextually to 2026 — may need freshness check on Codex pricing tiers and feature set before publishing
- Consider ingesting this as a raw source → wiki pages on `codex.md`, `claude-code-vs-codex.md`, and updating `claude-code.md` with competitive positioning details