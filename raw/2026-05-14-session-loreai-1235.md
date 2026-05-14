# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage session — evaluating 9 signals (21–29) from Twitter and GitHub for wiki/content routing.

**Key Exchanges:**
- Evaluated 9 signals; 3 marked `ignore`, 3 marked `refresh`, 3 marked `refresh_and_create`

**Decisions Made:**
- **Signal 21 → refresh_and_create**: Claude Code Fast mode now on Opus 4.7 ($30/$150 per 1M tokens, `/fast` toggle). Updates pricing FAQ + CLI reference. New FAQ on Fast vs standard mode.
- **Signal 23 → refresh_and_create**: `/goal` command ships — autonomous long-running background tasks (official @ClaudeDevs). Updates skills FAQ, warrants standalone blog on use cases and how it differs from `/batch`.
- **Signal 25 → refresh_and_create**: CoralOS multi-agent harness coordinating Hermes + Claude Code on SWE Atlas. Updates subagents examples page, blog angle on inter-agent coordination patterns.
- **Signal 27 → refresh**: src-hunter-skill (bug bounty Claude Code skill, 19 attack playbooks) — community skill example for skills FAQ.
- **Signal 28 → refresh**: User confirms `/goal` runs multi-hour YouTube research workflow — social proof to weave into skills FAQ (duplicate of signal 23 create action).
- **Signal 29 → refresh**: Anthropic clarifies SDK/API rate limits are separate from subscription; Max 200 plan gets $200 API credit across Claude Code, Chat, OpenClaw. Updates pricing FAQ and model options FAQ.
- **Ignored**: Higgsfield Virality Predictor (thin Claude Code angle), ALgoat deployment tip (just a paste-file mention), pixel art mascot (novelty widget).

**Lessons Learned:**
- Deduplication matters: signal 28 was correctly scoped to `refresh` only since signal 23 already handled the `create` action for `/goal`.
- "Incidental Claude Code mention" is a valid ignore reason — prevents thin content from third-party product promos.

**Action Items:**
- Create/refresh wiki pages: `claude-code-pricing`, `claude-code-cli`, `claude-code-vs-cursor`, `claude-code-skills`, `claude-code-subagents-examples`
- Draft blog: `/goal` command background tasks use cases
- Draft blog: Multi-agent coordination patterns (CoralOS case study)
- Draft FAQ: Claude Code Fast mode vs standard mode tradeoffs