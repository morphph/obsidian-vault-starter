# Session Capture: loreai

**Date:** 2026-05-19
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese comparison article (Codex Subagents vs Custom Agents) for the blog.

**Key Exchanges:**
- Produced a full `/zh/blog/` comparison post covering OpenAI Codex's two multi-agent patterns: Subagents (system-driven parallel task splitting) and Custom Agents (user-defined roles via `agents.json`)

**Decisions Made:**
- **Framing:** Positioned the two as complementary, not competing — Subagents = execution engine, Custom Agents = engineering-standards encoder
- **Recommendation pattern:** Layer them — Custom Agents define roles/constraints, Subagents handle parallel execution within those roles
- **Related content linking:** Connected to existing posts (codex-complete-guide, codex-vscode, effective-harnesses, coding-agents-reshaping-epd, 9-principles-writing-claude-code-skills)

**Lessons Learned:**
- Subagents' parallel execution can compress 10+ file tasks to 30-50% of serial time (claimed benchmark)
- Custom Agents configs live in `agents.json` or `.codex/agents/` at project root — version-controllable, team-shareable
- Subagent parallelism requires cloud infrastructure; local Codex CLI only supports Custom Agent config loading, not full Subagent parallelism

**Action Items:**
- Article needs to be saved to `drafts/` and committed/pushed per git workflow rules
- Verify factual claims against source material in `raw/` (especially Subagent performance numbers and Custom Agents config format details)