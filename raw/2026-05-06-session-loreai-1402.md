# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/content comparing Claude Code vs OpenAI Codex — likely being ingested or drafted for publication.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code runs locally (pair programming model), Codex runs in isolated cloud sandbox (task queue model)
- Configuration systems: Claude Code uses layered CLAUDE.md + SKILL.md + hooks + MCP; Codex uses single AGENTS.md + setup script
- Pricing: Claude Code = token-based API billing; Codex = bundled in ChatGPT Pro ($200/mo)

**Decisions Made:**
- Framing: "not interchangeable — they solve different problems with different architectures"
- Hybrid approach recommended: Claude Code for interactive complex work, Codex for batch/parallel well-scoped tasks
- Target audiences differ: Claude Code → senior/terminal-native engineers with complex workflows; Codex → teams wanting parallel task execution with simpler setup

**Lessons Learned:**
- Codex sandboxes are network-isolated — no external API calls during execution, tests must be self-contained
- Claude Code's local execution model matters for regulated industries (code never leaves infra except as API payloads)
- Codex's network isolation is actually a security *advantage* against agent-initiated exfiltration
- Maintaining two config systems (CLAUDE.md + AGENTS.md) is the main cost of using both
- Codex feedback loop is submit→wait→review→resubmit (no mid-task steering)
- OpenAI gives free Codex access to verified OSS maintainers + $100 credits for students

**Action Items:**
- This content should be ingested into wiki as a page (e.g., `wiki/claude-code-vs-codex.md`) covering the competitive landscape
- Cross-reference with existing wiki pages on [[Claude Code]] tools/workflows if they exist
- Pricing data ($200/mo ChatGPT Pro) is as of the article date — may need future updates