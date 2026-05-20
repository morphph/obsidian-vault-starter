# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/wiki article comparing Codex CLI vs Claude Code as agentic coding tools.

**Key Exchanges:**
- Comprehensive feature comparison between Codex CLI and Claude Code covering execution model, context systems, pricing, DX, and extensibility
- Core architectural distinction identified: Codex runs in isolated cloud sandboxes (network-off default); Claude Code runs locally with full shell access

**Decisions Made:**
- Verdict: Claude Code is the stronger choice for most professional developers on active codebases, due to local execution, test running, and programmable extension stack
- Framing: tools aren't mutually exclusive — Codex for async batch/triage, Claude Code for interactive development
- Decision rules articulated per section (safety → Codex; deep codebase interaction → Claude Code)

**Lessons Learned:**
- Codex CLI's sandbox-first approach trades capability for safety; Claude Code's local-first trades safety for capability — neither is universally better
- Claude Code's 7-layer programmable stack (CLAUDE.md, SKILL.md, hooks, MCP, agent teams, memory) is its key differentiator for team adoption
- Pricing models are structurally different: Codex bundles into ChatGPT Pro flat rate ($200/mo); Claude Code is usage-based API or Max subscription — the right choice depends on usage intensity
- Codex CLI is open source (Apache 2.0); Claude Code is closed source — matters for regulated industries
- Codex's async "fire and review" model suits supervising multiple parallel tasks; Claude Code's real-time model suits pair-programming style workflows

**Action Items:**
- Article references multiple internal blog links (`/blog/claude-code-*`, `/blog/codex-*`) — verify these exist and are live
- Pricing figures may need updating (marked as "moving target" in the text)
- Consider ingesting this into wiki as a page (e.g., `wiki/codex-cli-vs-claude-code.md`) and cross-linking to existing [[anthropic]], [[claude-code]] pages