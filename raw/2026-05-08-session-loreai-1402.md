# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Blog article comparing Claude Code vs OpenAI Codex as AI coding tools (competitive analysis / comparison post).

**Key Exchanges:**
- Claude Code = interactive, local-first, terminal-native; Codex = async, cloud-sandboxed, task-queue model
- Claude Code parallelism is within-task (sub-agents coordinating on one complex change); Codex parallelism is across-tasks (many independent containers)
- Codex average task completion: few minutes to 15+ minutes; Claude Code shows first results in seconds
- Codex sandbox has no network access, no local DB/services, no private registries unless explicitly configured

**Decisions Made:**
- Verdict positions Claude Code as the stronger tool for most professional developers (interactive work dominates engineering time), with Codex better for well-scoped batch/parallel tasks
- Framing: "complement rather than compete" — many teams use both
- Pricing comparison: Claude Code Max ($100/mo) > value per active coding hour than Codex via ChatGPT Pro ($200/mo)

**Lessons Learned:**
- CLAUDE.md + SKILL.md + hooks + MCP = compounding project-specific configuration advantage over Codex's flat instructions field
- Codex's fire-and-forget model is genuinely novel for "multiply throughput" use cases (e.g., add tracing to all API handlers)
- Security tradeoff: local execution (Claude Code) = code never leaves machine; cloud execution (Codex) = code transmitted to OpenAI infra — blocker for strict IP policies
- For team consistency, file-based config that versions with the repo (Claude Code) beats per-user/per-task instructions (Codex)

**Action Items:**
- Article references several internal blog posts that should exist: `/blog/codex-complete-guide`, `/blog/codex-vscode`, `/blog/codex-for-students`, `/blog/codex-for-open-source`, `/blog/claude-code-enterprise-engineering-ramp-shopify-spotify` — verify these are published or queued
- Pricing data (Claude Pro $20, Max $100-200, ChatGPT Plus $20, Pro $200) should be tracked in wiki as it changes frequently