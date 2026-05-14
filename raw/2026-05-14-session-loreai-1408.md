# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article comparing Claude Code vs OpenAI Codex — decision frameworks for choosing between them.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code = local-first, synchronous, full shell access; Codex = cloud-based, async, sandboxed containers with no network
- Context systems differ fundamentally: Claude Code has layered CLAUDE.md → Skills → Memory → Hooks that compound over time; Codex starts fresh each task from repo clone + optional `agents.md`
- Security tradeoff clearly articulated: Claude Code = more capable but runs with user's full permissions; Codex = safer but can't reach local services/APIs

**Decisions Made:**
- Three decision rules established:
  1. **Local context needed?** → Claude Code. **Self-contained task?** → Codex
  2. **Long-lived project with accumulated context?** → Claude Code. **Many repos / one-off tasks?** → Codex
  3. **Need real-time steering?** → Claude Code. **Can fully specify upfront?** → Codex
- Verdict: "Most productive setup for many teams will be both" — Claude Code for hard problems needing human-in-loop, Codex for well-defined background tasks

**Lessons Learned:**
- Codex pricing bundled with ChatGPT Pro ($200/mo); Claude Code is usage-based per-token — volume determines which is cheaper
- Codex offers free access for open-source maintainers and $100 credits for students — relevant for community positioning
- As both tools evolve (Claude Code → more autonomous; Codex → richer environments), the gap narrows, but the local-vs-cloud architectural bet persists
- For large codebases/monorepos, Claude Code's agent teams + layered context outperform Codex's full-repo-per-task approach

**Action Items:**
- Article references related posts that should be cross-linked in wiki: Claude Code hooks, Skills principles, agent teams, voice mode, remote control, long-running agents, Claude Code vs Cursor comparison