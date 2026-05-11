# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/content piece comparing Claude Code vs OpenAI Codex as coding agent tools.

**Key Exchanges:**
- Detailed feature comparison between Claude Code (interactive, local, extensible) and Codex (async, sandboxed, batch-oriented)

**Decisions Made:**
- Claude Code = better for individual developers who want real-time pair programming, complex debugging, full-stack tasks requiring env access
- Codex = better for batch task delegation, team-scale distribution, self-contained repo work, GitHub-native workflows
- Tools are not mutually exclusive — recommended combo: Claude Code for daily dev work, Codex for overnight batch processing of well-defined tasks

**Lessons Learned:**
- Codex runs in isolated cloud sandboxes with NO internet access during execution — cannot install packages mid-task, call external APIs, or access local services
- Codex is fire-and-forget (no mid-task steering); wrong approaches only discovered at review time
- Claude Code's hidden cost: developer presence during execution. Codex's advantage: async frees developer time
- Codex uses `AGENTS.md` (equivalent to Claude Code's `CLAUDE.md`) but simpler — no MCP, no hooks
- Privacy: Claude Code keeps code local; Codex uploads repo to cloud containers
- Both can work on same repo — just pull Codex PRs before starting Claude Code sessions

**Action Items:**
- This content should be ingested into wiki as a knowledge page covering the Claude Code vs Codex landscape (competitive positioning, pricing tiers, use-case matrix)
- Pricing data worth tracking: Claude Max $100-200/mo, ChatGPT Pro $200/mo (includes Codex), ChatGPT Plus $20/mo (limited Codex)
- Codex offers free tier for open-source maintainers and $100 student credits