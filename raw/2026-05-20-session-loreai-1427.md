# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a comprehensive comparison article: Claude Code vs Codex CLI (OpenAI).

**Key Exchanges:**
- Detailed feature-by-feature comparison covering: execution model (local vs cloud sandbox), context/customization systems, workflow integration (sync vs async), pricing, safety/sandboxing, and task-fit scenarios.

**Decisions Made:**
- Claude Code positioned as stronger general-purpose interactive agent; Codex CLI positioned as better for async multi-repo batch delegation
- Verdict: complementary tools, not competitors — most teams benefit from using both
- Claude Code advantages: local execution, layered context (CLAUDE.md/SKILL.md/hooks/MCP), interactive debugging, deep customization
- Codex CLI advantages: cloud sandbox safety, async parallel task processing, multi-repo management, subscription pricing simplicity

**Lessons Learned:**
- Codex CLI runs tasks in isolated cloud containers (cloned repo only) — cannot access local filesystem, services, or credentials. Output is always a reviewable diff/PR.
- Codex CLI bundled with ChatGPT Plus ($20/mo) or Pro ($200/mo); Claude Code is usage-based API billing (pay-per-token) or Max plan subscription
- OpenAI introduced `AGENTS.md` convention (analogous to `CLAUDE.md`) but ecosystem is newer/less documented
- Codex has no equivalent to Claude Code's hooks or MCP servers — narrower customization surface
- Codex CLI has free programs for open-source maintainers and students
- Large monorepos favor Claude Code (local filesystem access); Codex incurs setup latency cloning into sandbox
- Task-fit heuristic: if task needs mid-execution judgment or local env → Claude Code; if fully specifiable upfront and parallelizable → Codex CLI

**Action Items:**
- This content should be ingested into wiki as a page (e.g., `wiki/claude-code-vs-codex-cli.md`) covering the competitive landscape
- Consider updating `wiki/codex-cli.md` (or creating it) with Codex CLI's architecture, pricing, and capabilities
- Cross-reference with existing wiki pages on [[Claude Code]], [[MCP]], and any pricing/model pages