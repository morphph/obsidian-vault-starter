# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex for agentic coding workflows.

**Key Exchanges:**
- Detailed feature comparison between Claude Code (interactive, terminal-native, local execution) and OpenAI Codex (async, cloud-sandboxed, task-based)
- Pricing breakdown: Claude Code available from $20/mo (Pro), Codex requires $200/mo (Pro) minimum — significant accessibility gap

**Decisions Made:**
- Framing: "two visions of agentic coding" — Claude Code = developer-in-the-loop collaborator; Codex = async task delegator
- Verdict: not either/or — complementary tools. Claude Code for complex/ambiguous work, Codex for well-defined batch tasks
- Decision rule articulated: "needs judgment → Claude Code; well-specified + parallelizable → Codex"

**Lessons Learned:**
- The harness (CLAUDE.md, sandbox, extension system) matters more than the underlying model — this is the key differentiator in 2026
- Claude Code rewards *investment* (project customization via CLAUDE.md/SKILL.md); Codex rewards *clarity* (precise task specs)
- Codex tradeoff: no mid-task steering means ambiguous tasks require multiple submit-review-revise cycles
- Claude Code tradeoff: requires active attention, fundamentally interactive even with remote control
- For large monorepos with complex local infra, Claude Code's local execution model has a clear advantage over Codex's cloud clone approach

**Action Items:**
- Article references companion pieces: Claude Code complete guide, Codex complete guide, agent harnesses 2026 analysis — ensure these exist or are planned
- Cross-links to `/blog/claude-code-agent-teams`, `/blog/claude-code-remote-control-mobile`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source` — verify all live