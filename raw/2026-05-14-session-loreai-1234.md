# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Daily Anthropic/Claude Code signal triage — routing 21 signals from Twitter, blogs, GitHub, and RSS into content actions for the LoreAI wiki/blog pipeline.

**Key Exchanges:**
- Triage classified 21 signals into 10 actionable (refresh or refresh_and_create) and 11 ignored (duplicates, off-topic, insufficient signal)

**Decisions Made:**
- **Claude Opus 4.7 fast mode** (signal 0/1/5): Routed to refresh model comparison pages. 3× faster, same intelligence, research preview. Duplicates correctly collapsed.
- **`claude agents` CLI command** (signal 2): New CLI orchestration layer for managing multiple sessions. Refresh CLI FAQ.
- **Weekly limits +50% through July 13** (signal 4/7/9): Time-bounded promotion for Pro/Max/Team/Enterprise. Refresh pricing pages. Three duplicate RTs correctly ignored.
- **Agent SDK monthly credit starting June 15** (signal 8): New billing dimension — separate from regular usage limits, covers `claude -p`, third-party apps (OpenClaw, Conductor), custom scripts. Create new FAQ.
- **Agent view research preview** (signal 11): Background sessions with status tracking and inline reply — replaces raw terminal tabs. Create tutorial.
- **claude-code-setup official plugin** (signal 13): Anthropic-built plugin that inspects project → recommends hooks, skills, MCP servers, subagents. Create tutorial.
- **MCP knowledge graph server — 94% tool call reduction** (signal 14): Open source, 19+ languages, fully local. Create blog post on the approach.
- **Claude Code v2.1.141** (signal 20): `terminalSequence` in hook JSON (notifications without TTY), auto-mode permission dialogs explain which rule triggered, Rewind adds "Summarize up to here." Refresh all hooks content + create blog.
- **Anthropic cybersecurity case study** (signal 12): First-party case study of Claude Code building a threat detection platform. Create blog for security engineering angle.
- **Desktop remote control default-on** (signal 10): Refresh remote session blog posts to reflect new frictionless default.

**Lessons Learned:**
- Dedup logic working well — 5 duplicate RTs correctly collapsed (signals 5, 7, 9, 16, 18)
- Signal quality filter working: ignored Simon Willison's 30GB RAM observation (signal 3) as anecdotal without reproducible fix; ignored Cat Wu vision interview (signal 19) as speculative; ignored ANIMA/ARCTERMINAL (signal 15) as unrelated product
- Truncated tweet bodies (signal 6) correctly punted rather than guessed at

**Action Items:**
- Process the 6 `refresh` actions: update model comparison, CLI FAQ, pricing FAQ/topic hub, remote session blogs
- Process the 4 `refresh_and_create` actions: Agent SDK credit FAQ, agent view tutorial, claude-code-setup tutorial, knowledge-graph MCP blog, hooks terminalSequence blog, cybersecurity case study blog
- Note time-sensitive content: weekly limits promo expires July 13; Agent SDK credit starts June 15