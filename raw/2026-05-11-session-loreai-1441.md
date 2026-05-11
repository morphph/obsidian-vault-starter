# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article — Codex subagents vs Claude Code subagents for multi-agent workflows.

**Key Exchanges:**
- Comprehensive architectural comparison between Codex (OpenAI) cloud-sandbox model and Claude Code's parent-child orchestration model
- Codex scales horizontally (independent parallel tasks); Claude Code scales vertically (deep coordination on complex tasks)

**Decisions Made:**
- Framing: tools complement rather than compete — they optimize for different shapes of work
- Codex wins for batch-style, independent task delegation (high parallelism, strong isolation, async)
- Claude Code wins for coordinated, context-rich workflows (shared context, real-time oversight, SKILL.md in version control)
- Practical parallel limit for Claude Code: 3-5 subagents on typical dev machine; Codex scales with cloud resources (50+ tasks trivially)

**Lessons Learned:**
- Codex custom agents = system instructions + sandbox config, defined upfront, no inter-agent communication by design
- Claude Code custom agents = compositional (built-in types like Explore/Plan + SKILL.md + dynamic orchestration at runtime)
- Claude Code subagents share filesystem by default (risk of conflicts); git worktree isolation is opt-in
- Codex isolation is default — each task gets fresh container clone
- Cost model differs: Codex = cloud sandbox compute (bundled in ChatGPT plan); Claude Code = API tokens only (no sandbox overhead)
- For enterprise: Codex better for isolation guarantees; Claude Code better for data residency / keeping code local

**Action Items:**
- Article references `/blog/claude-code-subagents-examples` and `/blog/codex-complete-guide` — ensure these exist or are queued
- Article references `/blog/9-principles-writing-claude-code-skills` and `/blog/5-claude-code-skills-i-use-every-single-day` — verify cross-links
- Consider ingesting this into wiki as a page on multi-agent architecture patterns (covers both ecosystems)