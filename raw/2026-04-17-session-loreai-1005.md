# Session Capture: loreai

**Date:** 2026-04-17
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** LoreAI daily brief output — AI news digest for 2026-04-17

**Key Exchanges:**
- No interactive Q&A — session was a read-only news feed delivery

**Decisions Made:**
- None recorded

**Lessons Learned:**
- **Opus 4.7 launched**: Better coding, computer use, finance, general knowledge. Boris Cherny (Claude Code creator) notes it takes a few days to learn to use effectively. Hard benchmark data: Cursor internal bench 58% → 70%, Notion +14% lift with 1/3 fewer tool calls.
- **Opus 4.7 known issues**: (1) Adaptive thinking treats non-code/math as "low effort" with no manual override — Mollick flags worse outputs on non-technical tasks. (2) Day-one rate limit bug for long-context requests — patched same day.
- **Opus 4.7 context window**: 1M context is a double-edged sword — enables complex agentic tasks but introduces context pollution risk. Requires deliberate context management.
- **Claude Mythos Preview**: First model to complete UK AISI's cyber challenge — confirms frontier models crossing real capability thresholds.
- **Qwen3.6-35B-A3B**: Open-source sparse MoE, 35B total / 3B active params, Apache 2.0. Competitive agentic coding on a laptop.
- **OpenAI GPT Rosalind**: Domain-specific frontier model for biology/drug discovery.
- **Codex** (OpenAI): Biggest single feature drop — Mac computer use, in-app browser, image gen, 90+ plugins (JIRA, GitLab, CircleCI), GitHub review comments, remote devbox SSH.
- **Latent Space**: "RIP Pull Requests (2005–2026)" — argues agentic AI is killing the PR workflow.
- **@ClaudeDevs**: New official Anthropic channel for Claude Code changelogs and API updates.
- **CodeBurn**: Open-source tool to analyze Claude Code token usage by task.

**Action Items:**
- Evaluate Opus 4.7 on non-code workflows (compare vs 4.6 for content/writing tasks)
- Follow @ClaudeDevs for Claude Code updates
- Check Qwen3.6-35B-A3B for local agentic use cases
- Review context management strategy for long agentic sessions with Opus 4.7