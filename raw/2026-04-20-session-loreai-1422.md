# Session Capture: loreai

**Date:** 2026-04-20
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language comparison draft article: "Claude Memory vs CLAUDE.md：两套记忆系统到底有什么区别？"

**Key Exchanges:**
- Draft produced for the LoreAI blog comparing two Claude context persistence mechanisms: Claude Memory (auto, cross-session, personal) vs CLAUDE.md (manual, project-scoped, team-shared)

**Decisions Made:**
- Article positioned as a "compare" post (`category: tools`, `related_compare: [claude-memory-vs-claude-md]`)
- Three-layer framing: CLAUDE.md = project law, Memory = personal assistant, SKILL.md = task SOP
- Cross-linked to existing blog posts: `claude-code-memory`, `anthropic-claude-memory-upgrades-importing`, `claude-code-seven-programmable-layers`, `9-principles-writing-claude-code-skills`, `claude-code-extension-stack-skills-hooks-agents-mcp`

**Lessons Learned:**
- Key distinction worth encoding: CLAUDE.md is deterministic (injected verbatim into system prompt), Memory is probabilistic (model decides what to retain) — this is the core architectural difference
- CLAUDE.md is version-controlled and team-shared; Memory is local (`~/.claude/`) and personal-only
- Conflict resolution: CLAUDE.md takes precedence over Memory when they conflict

**Action Items:**
- Draft at `drafts/` — needs human review and polish before publishing to LoreAI
- Verify all internal blog links (`/zh/blog/...`) resolve correctly before publish