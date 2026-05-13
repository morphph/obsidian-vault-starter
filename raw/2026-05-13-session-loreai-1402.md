# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex

**Key Exchanges:**
- Comprehensive architectural comparison: Claude Code = local terminal agent (interactive, real-time); Codex = cloud sandbox agent (async, batch tasks)
- Codex is async-only — no back-and-forth during execution; you review PRs after completion
- Claude Code has 7 programmable layers (CLAUDE.md, skills, hooks, MCP); Codex has minimal customization (setup scripts + repo instructions only)

**Decisions Made:**
- **Verdict positioning:** Claude Code is better for most active developers; Codex is better for async task delegation and security-constrained environments
- **"Use both" framing:** Not mutually exclusive — Claude Code for interactive sessions, Codex for batch work (tests, lint fixes, well-specified tickets)
- **Workflow recommendation:** Claude Code for ambiguous/exploratory tasks requiring mid-task judgment; Codex for well-defined tasks with clear descriptions upfront

**Lessons Learned:**
- Codex's network-disabled sandbox = stronger default security model, easier compliance approval; Claude Code's local access = necessity for teams needing internal service interaction
- Codex pricing: bundled with ChatGPT Pro ($200/mo); Claude Code: per-token usage-based — variable cost
- Cost of using both tools: **context fragmentation** — Claude Code builds session context via CLAUDE.md; Codex tasks are stateless
- Codex sandbox limitation: complex build dependencies or environment-specific configs may not work in containerized environment
- Neither tool creates vendor lock-in at code level — both produce standard code + git commits
- Claude Code's CLAUDE.md and skill files are the main non-transferable investment

**Action Items:**
- Consider creating wiki pages for: `codex.md` (OpenAI Codex product profile), `claude-code-vs-codex.md` (comparison summary)
- Cross-link with existing wiki pages on [[Claude Code]], [[agentic coding]] if they exist
- Article references several other blog posts (`/blog/claude-code-seven-programmable-layers`, `/blog/claude-code-hooks-*`, `/blog/codex-vscode`, etc.) — ensure those are tracked if published