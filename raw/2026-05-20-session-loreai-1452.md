# Session Capture: loreai

**Date:** 2026-05-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparative article on Claude Code subagents vs Codex custom agents for the LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code uses parent-child single-session model (subagents spawned inline, share context, return results to parent); Codex uses task-queue multi-session model (independent containers, fresh repo clones, PR output)
- Claude Code subagent types: Explore (read-only), general-purpose (full tools), code-reviewer, Plan — each with defined tool surfaces
- Codex custom agents configured via setup commands + behavioral instructions; environment is imperative/explicit vs Claude Code's declarative/contextual (CLAUDE.md inheritance)

**Decisions Made:**
- Framing: not competitors but complementary tools for different workflow shapes (interactive vs batch)
- Claude Code → interactive/exploratory/coordinated work; Codex → batch/isolated/independent tasks
- Many teams should use both: Claude Code for hands-on sessions, Codex for overnight backlog processing

**Lessons Learned:**
- Claude Code subagents require good prompt discipline — subagent has zero parent context, must be briefed like a new colleague
- Worktree isolation enables speculative refactoring without committing to an approach
- Codex tasks can't share intermediate results — two tasks on overlapping code will produce conflicting PRs
- Practical parallel subagent limit: 2-4 concurrent (context window + token cost constraints)
- Codex setup cost paid per task (no state persistence between runs) — tradeoff for reproducibility
- Cost model difference: Claude Code per-token (multiplied by parallel agents), Codex flat-rate per plan

**Action Items:**
- Article references several internal links (`/blog/claude-code-subagents-examples`, `/glossary/agentic-coding`, etc.) — ensure these wiki pages exist or are created
- Consider ingesting this as a wiki page covering multi-agent architecture patterns (spans both Anthropic and OpenAI ecosystems)