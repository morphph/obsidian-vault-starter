# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive Claude Code vs OpenAI Codex comparison article for LoreAI blog.

**Key Exchanges:**
- Detailed architectural comparison: Claude Code = local-first (terminal agent, runs on your machine), Codex = cloud-first (sandboxed containers, async task queue)
- Customization stack comparison: Claude Code has 4 layers (CLAUDE.md → SKILL.md → hooks → MCP), Codex has AGENTS.md only — simpler but less extensible
- Interaction model: Claude Code = synchronous/conversational (pair programming), Codex = asynchronous/task-oriented (ticket queue)
- Gap is narrowing: Claude Code added background/remote agents; Codex added interactive follow-up

**Decisions Made:**
- Article takes a "neither is universally better" stance — recommends by workflow type
- Hybrid approach positioned as the pragmatic recommendation for teams
- Quality framed as system-level (skills, test sandboxing) rather than raw model comparison — avoids benchmark wars
- Pricing comparison kept factual: Claude Code = per-token API billing, Codex = bundled with ChatGPT tiers ($20-$200/mo)

**Lessons Learned:**
- Claude Code's skill system is a **compounding** quality advantage — improves over time as skills are refined
- Codex's sandbox gives automatic verification (tests pass = code works), eliminating local env config burden
- Security architecture differs fundamentally: local-only vs cloud-sent — matters for data residency/IP concerns
- Enterprise adoption channels differ: Claude Code via engineering teams (Ramp, Shopify, Spotify), Codex via existing ChatGPT/OpenAI enterprise relationships
- Codex strategic moves: free tier for open-source maintainers + $100 student credits to build adoption

**Action Items:**
- Article references several internal links that need to exist: `/blog/claude-code-hooks-a-complete-guide`, `/blog/claude-code-agent-teams`, `/blog/do-skills-actually-improve-your-agents-output`, `/blog/codex-vscode`, `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/compare/claude-code-vs-cursor`
- Wiki pages to create/update: `claude-code.md`, `openai-codex.md`, `ai-coding-agents.md` with key comparison points
- Consider ingesting this article as a raw source once published