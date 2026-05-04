# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing Claude Code vs OpenAI Codex — positioning, pricing, use cases, and developer experience.

**Key Exchanges:**
- Claude Code = local, interactive, terminal-first agent with full environment access; Codex = cloud-based, async, sandboxed task runner
- Pricing: Claude Code is usage-based (API) or bundled with Pro ($20/mo); Codex is bundled with ChatGPT Pro ($200/mo) or Team ($25/user/mo)
- Codex supports `AGENTS.md` but lacks equivalents for SKILL.md, hooks, or MCP integrations

**Decisions Made:**
- Framing: "not competing to solve the same problem" — different workflow slots, not a feature horse race
- Recommendation axis: "Do I need to steer in real time, or fire and forget?" — this is the core decision heuristic
- "Use both" is the pragmatic answer for many teams: Claude Code for active sessions, Codex for background batch tasks

**Lessons Learned:**
- Codex cannot access local dev environment (no databases, services, env vars) — this is the hard architectural constraint that defines use cases
- Codex's student program ($100 free API credits) and open-source maintainer program (free Pro) are notable distribution plays
- Claude Code's cognitive cost is real: you're partially occupied during the session; Codex's cost is latency (minutes per task, slower iteration loop)
- Codex's sandbox isolation is genuinely valuable for junior developers and safety-critical contexts, not just a limitation

**Action Items:**
- Article references several internal links (`/blog/codex-for-students`, `/blog/codex-complete-guide`, `/compare/claude-code-vs-cursor`, etc.) — ensure these exist or are planned before publishing
- Pricing details will go stale quickly — flag for periodic review
- Consider ingesting this into wiki as a page on coding agent landscape / competitive positioning