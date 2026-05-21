# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a detailed comparison article — Codex custom agents vs Claude Code subagents — covering configuration, execution models, pricing, and use-case recommendations.

**Key Exchanges:**
- Comprehensive feature-by-feature breakdown produced: configuration model, execution model, built-in specializations, pricing, and decision framework
- Article structured with clear "bottom line" verdicts per section plus an FAQ

**Decisions Made:**
- Positioned the comparison as non-binary ("many teams will benefit from using both") — Codex for batch/offline, Claude Code for interactive/context-rich work
- Codex strengths: cloud parallelism, bundled pricing on ChatGPT plans, centralized agent management
- Claude Code strengths: built-in agent types (Explore, Plan, pipeline-reviewer), file-based customization via CLAUDE.md/skills, live local environment access, worktree isolation, real-time steering via SendMessage
- Pricing breakpoint identified: 1-3 devs → Claude Code pay-per-token cheaper; 5+ devs on ChatGPT Team/Enterprise → Codex bundled free

**Lessons Learned:**
- Codex context staleness is a real tradeoff — works on repo snapshot at submission time, no mid-task updates
- Codex container spin-up latency: 30-90 seconds; Claude Code agents start immediately
- Claude Code worktree isolation bridges the gap between interactivity and safety (isolated copy but local environment access)
- Codex custom agents require dashboard config changes for behavior modification (rigid); Claude Code agents customizable per-invocation via prompt (flexible)
- Claude Code disk usage scales with parallel agent count due to worktree copies

**Action Items:**
- Article appears draft-complete — needs to be saved to `drafts/` if not already
- Internal links reference several related articles (claude-code-memory, claude-code-extension-stack, anatomy-of-git-worktree-add, codex-vscode, claude-code-agent-teams) — verify these exist or are planned
- Consider ingesting this content into wiki pages: one for Codex, one for Claude Code subagents, with cross-references