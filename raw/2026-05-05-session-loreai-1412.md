# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting a Chinese-language compare article (claude-code-vs-codex) for LoreAI blog.

**Key Exchanges:**
- Produced a full compare article contrasting Claude Code (local terminal agent) vs OpenAI Codex (cloud sandbox agent)

**Decisions Made:**
- Framing angle: "两条技术路线之争" (two competing technical philosophies) rather than feature-list comparison — local-first vs cloud-first as the root divergence from which all other differences derive
- Standout positioning: action-oriented decision rules after each section instead of wishy-washy "both are good"
- Included dual-use recommendation (teams use both for different task types) as the realistic conclusion

**Lessons Learned:**
- Claude Code's differentiator: four-layer extension stack (CLAUDE.md → SKILL.md → Hooks → MCP) gives deep customization that Codex lacks
- Codex's differentiator: true parallel cloud execution (multiple sandboxes simultaneously) that Claude Code can only approximate via Agent Teams subprocesses
- Neither fully replaces the other — complementary tools for sync-interactive vs async-batch workflows
- Pricing comparison is non-trivial: Claude Code = API token-based or Pro/Max sub; Codex = bundled in ChatGPT Pro ($200/mo) / Team

**Action Items:**
- Article needs to be saved to `drafts/` directory and committed
- Internal links reference several related pages (`codex-complete-guide`, `claude-code-extension-stack-skills-hooks-agents-mcp`, `claude-code-agent-teams`, `codex-vscode`, `codex-for-open-source`) — verify these exist or queue them for creation