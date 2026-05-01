# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User was working on (or reviewing) a comparison article: Claude Code subagents vs OpenAI Codex subagents — likely a draft for LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison of cloud-sandbox (Codex) vs terminal-native (Claude Code) execution models
- Use-case analysis across four scenarios: refactoring, test generation, bug investigation, team task distribution

**Decisions Made:**
- **Verdict is "both, not either/or"**: Codex for batch delegation of independent tasks; Claude Code for interactive, context-rich multi-agent sessions
- **Category winners assigned**: Claude Code wins agent customization (typed agents, model overrides, isolation controls), Codex wins initial setup simplicity and team-scale features
- **Use-case edges**: Claude Code better for dependent workflows, deep debugging, live system access; Codex better for embarrassingly parallel tasks (test gen), team task queues, async review culture

**Lessons Learned:**
- Codex subagents cannot communicate during execution — full isolation means no real-time coordination
- Claude Code worktree isolation prevents file conflicts between sub-agents; without it, orchestrator must sequence work manually
- Codex cold-start overhead (env setup per task) is a real cost for interactive workflows
- Claude Code's power comes at steeper learning curve (typed agents, permission modes, isolation options)
- Pricing models differ fundamentally: Codex subscription-bundled vs Claude Code pay-per-token — volume profile determines which is cheaper

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/blog/claude-code-agent-teams`, `/blog/codex-vscode`, `/blog/claude-code-hooks-...`) — ensure these destination pages exist or are queued for creation
- Consider ingesting this as a wiki page (e.g., `wiki/codex-vs-claude-code-subagents.md`) once finalized
- FAQ section could seed standalone wiki entries on subagent isolation patterns and cost modeling