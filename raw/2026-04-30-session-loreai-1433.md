# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft/review of a blog article comparing OpenAI Codex vs ChatGPT for coding tasks (likely for LoreAI blog).

**Key Exchanges:**
- Comprehensive comparison of Codex (autonomous agent) vs ChatGPT (interactive assistant) for software development workflows

**Decisions Made:**
- Article structure follows a task-complexity spectrum framework: simple (ChatGPT wins), medium (Codex wins), complex (use both)
- Verdict: recommend ChatGPT Plus as starting point, upgrade to Pro/Team for Codex when needed
- "Use both together" positioning: ChatGPT = thinking partner, Codex = execution partner

**Lessons Learned:**
- **Codex pricing (as of early 2026):** Requires ChatGPT Pro ($200/mo), Team ($25/user/mo), or Enterprise. NOT included in Plus ($20/mo). Free credits available for students.
- **Codex sweet spot:** Multi-file changes, test-dependent work, batch task execution, async/hands-off execution
- **ChatGPT sweet spot:** Learning, quick debugging, design discussions, mixed coding+non-coding work, zero-setup scenarios
- **Codex integration model:** Web UI + VS Code extension + GitHub PR creation. Runs in sandboxed cloud containers with full repo clone.
- **Key Codex limitation:** Cannot install arbitrary system packages or access external services (APIs, databases) from its sandbox
- **Workflow pattern:** Plan with ChatGPT → Execute with Codex → Review with ChatGPT

**Action Items:**
- This content should be ingested into wiki as competitive intelligence on OpenAI's developer tools lineup (Codex, ChatGPT coding features, pricing tiers)