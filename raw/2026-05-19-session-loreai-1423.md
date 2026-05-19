# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article comparing Codex CLI vs Claude Code — architectural differences, workflows, pricing, and when to use each.

**Key Exchanges:**
- Codex CLI = async task queue: sandboxed containers, no network, stateless, produces diffs/PRs. Included in ChatGPT Pro ($200/mo).
- Claude Code = sync pair programmer: local execution, layered context (CLAUDE.md → skills → hooks → MCP), usage-based API billing.
- Context models differ fundamentally: Codex is stateless per-task (clone + setup script); Claude Code accumulates context across sessions via CLAUDE.md, skills, hooks, auto-memory.

**Decisions Made:**
- Not competitors but complementary tools for different workflows
- Solo devs / hands-on coding → start with Claude Code (interactive, extensible)
- Tech leads / delegation at scale → start with Codex CLI (async, sandboxed)
- Many teams use both: Claude Code for active dev, Codex CLI for batch tasks

**Lessons Learned:**
- Codex CLI breaks down for exploratory/debugging work — submit-wait-review cycle too slow for iterative discovery
- Claude Code's extensibility (skills, hooks, MCP) creates compounding returns over time; Codex's simplicity may limit customization as agentic coding matures
- Codex safer by default (isolation); Claude Code safer with investment (permissions + hooks)
- Large codebases: Claude Code more efficient (no per-task clone overhead); Codex avoids state pollution from long sessions
- Codex CLI latency = minutes per task but parallelizable; Claude Code latency = seconds but sequential attention required

**Action Items:**
- This content likely belongs in `wiki/` as a page (e.g., `codex-cli-vs-claude-code.md`) — covers a key builder-tools topic in the domain focus
- Pricing info tagged as mid-2026; will need periodic refresh