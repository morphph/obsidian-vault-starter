# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on Codex Custom Agents vs Claude Code Subagents for the LoreAI blog.

**Key Exchanges:**
- Detailed use-case comparison across three scenarios: large codebase refactoring, PR review pipelines, and test generation
- Codex = async, isolated, batch-style; Claude Code = real-time, coordinated, multi-agent orchestration

**Decisions Made:**
- **Codex wins** for: high-volume independent tasks, strong isolation needs, standardized team workflows, async batch work
- **Claude Code wins** for: interdependent changes, real-time multi-agent coordination, deep codebase exploration, iterative workflows, complex orchestration (conditional branching, parallel-then-merge)
- **Verdict is "use both"**: Codex for volume (PR reviews, test gen, bug triage); Claude Code for depth (architecture refactoring, security audits, multi-system migrations)

**Lessons Learned:**
- Codex tasks are stateless — each runs in a fresh container, no memory between tasks. Config persists via repo-level `codex-setup.sh`
- Claude Code sub-agents have no hard concurrency limit but practical ceiling is 2-4 parallel agents due to token cost
- Claude Code's `codex:codex-rescue` sub-agent type enables hybrid workflows — Claude orchestration + Codex execution
- Pricing model difference matters: Codex flat-rate favors high-volume small tasks; Claude Code per-token favors fewer complex sessions
- As of mid-2026, Codex cannot spawn sub-agents within a single task — no intra-task orchestration

**Action Items:**
- Article references several internal links (`/blog/claude-code-review-agents`, `/blog/claude-code-agent-teams`, etc.) — ensure these exist or are queued for creation
- Pricing section flagged as volatile — needs periodic review against official pricing pages