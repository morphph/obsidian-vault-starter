# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature comparison between Claude Code (synchronous, local, interactive) and Codex (asynchronous, cloud-sandboxed, PR-based)
- Pricing breakdown: Claude Code = API billing or Max subscriptions; Codex = bundled with ChatGPT Pro ($200/mo), Team, Enterprise plans
- Codex launched free access for open-source maintainers and $100 credits for students

**Decisions Made:**
- Framing: "not competing for the same workflow — competing for the same developer's time"
- Verdict positioning: Claude Code wins on interactive dev; Codex wins on async task delegation; hybrid workflow recommended
- Claude Code's extensibility stack (CLAUDE.md → SKILL.md → Hooks → MCP) positioned as significantly deeper than Codex's AGENTS.md-only approach

**Lessons Learned:**
- Codex's key limitation: no mid-execution course correction — ambiguous tasks require full resubmit cycle
- Claude Code's key limitation: requires terminal comfort and local trust (weaker isolation vs Codex sandbox)
- Codex's killer feature is parallelization: assign 10 well-defined bugs simultaneously, review PRs in batch
- Claude Code's killer feature is tight feedback loop: catch wrong turns in seconds, not hours

**Action Items:**
- Article references several internal links (`/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/codex-complete-guide`, `/compare/claude-code-vs-cursor`, etc.) — verify all exist before publishing
- Article ends with `/subscribe` CTA — confirm this route works on loreai.dev
- Consider ingesting this into wiki as a competitive intelligence page (e.g., `wiki/claude-code-vs-codex.md`) once published