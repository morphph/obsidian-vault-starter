# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex subagents vs Claude Code agent teams for multi-agent workflows.

**Key Exchanges:**
- Comprehensive feature comparison produced: parallelism models, security/isolation, pricing, and practical workflows for both tools
- Codex = fire-and-forget, independent tasks, cloud-sandboxed, GitHub-native PR workflow
- Claude Code = orchestrated, dependent tasks, local execution, typed sub-agents (Explore, Plan, general-purpose)

**Decisions Made:**
- Verdict framing: not "X is better" but "different points on the autonomy-control spectrum" — Codex for async batch parallelism, Claude Code for interactive orchestrated sessions
- Recommended hybrid pattern: Claude Code for daytime interactive dev, Codex for overnight batch processing
- Article includes internal cross-links to `/blog/claude-code-subagents-examples`, `/blog/codex-complete-guide`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`

**Lessons Learned:**
- Codex parallelism is task-level (isolated containers, no shared state); Claude Code parallelism is agent-level within a session (shared filesystem, orchestrator coordinates)
- Codex's security advantage: sandboxed by default, no network access unless configured. Claude Code requires explicit permission management via `settings.json` and hooks
- Context window is the practical bound on Claude Code parallel agents; Codex has no such constraint since each task is isolated
- Codex bundles compute in subscription; Claude Code charges tokens only (local compute is free) — cost profiles differ significantly for compute-heavy tasks

**Action Items:**
- Article references several sibling posts (`codex-complete-guide`, `claude-code-subagents-examples`, `codex-vscode`, etc.) — ensure those exist or are queued for drafting
- Pricing section notes mid-2026 rates change frequently — flag for periodic refresh
- Consider ingesting this article into wiki as a knowledge page on multi-agent tooling comparison