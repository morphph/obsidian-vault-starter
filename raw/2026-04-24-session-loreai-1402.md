# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/drafting a comparison article between Claude Code and OpenAI Codex for publication (likely LoreAI blog).

**Key Exchanges:**
- The article covers: interaction model (pair programming vs async task assignment), context systems (CLAUDE.md vs AGENTS.md), parallel execution, IDE integration, safety/permissions, pricing, and model quality.

**Decisions Made:**
- Core framing: Claude Code = real-time pair programmer; Codex = async task executor in cloud — "not competitors in traditional sense"
- Claude Code wins for: interactive debugging, complex refactoring, full-environment tasks, custom workflows, solo dev
- Codex wins for: batch tasks, team-scale delegation, safety-first environments, GitHub-native workflows, lower barrier to entry

**Lessons Learned:**
- Claude Code pricing: usage-based API or Claude Max ($100/mo 5x, $200/mo 20x); no free tier
- Codex pricing: bundled in ChatGPT Pro ($200/mo), Team, Enterprise; zero marginal cost if already subscribed
- Codex uses `AGENTS.md` (similar to `CLAUDE.md`) but lacks nested directory-level instructions and skills framework
- Codex sandbox: ephemeral container, network disabled by default — stronger default safety but less flexible
- Claude Code parallelism: bounded by local machine + user attention; Codex parallelism: bounded by subscription tier
- Codex models: codex-mini (speed) + o4-mini (reasoning); Claude Code default: Sonnet 4.6, complex: Opus 4.6

**Action Items:**
- Article links to internal pages: `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, `/blog/codex-vscode`, `/compare/claude-code-vs-cursor` — verify these exist before publishing
- Article ends with LoreAI subscribe CTA — confirm `/subscribe` route is live