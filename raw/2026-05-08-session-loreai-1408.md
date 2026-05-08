# Session Capture: loreai

**Date:** 2026-05-08
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Claude Code vs Codex (OpenAI)

**Key Exchanges:**
- Article covers architecture (local agent vs cloud sandbox), security models, pricing, model capabilities, enterprise adoption, and use-case recommendations
- Claude Code = interactive local agent, permission-based security, $20/mo entry; Codex = async cloud worker, sandbox isolation, $200/mo entry
- Codex uses `codex-1` (RL fine-tuned for SWE tasks); Claude Code uses Opus/Sonnet with extended thinking + 1M token context

**Decisions Made:**
- Framing: not "which is better" but "two philosophies" — interactive collaboration vs async delegation
- Verdict recommends using both together: Claude Code for active dev sessions, Codex for batch/parallel tasks
- Positioned Claude Code as better for beginners, deep reasoning, custom workflows, budget-conscious; Codex for batch processing, security-sensitive codebases, open source maintenance at scale

**Lessons Learned:**
- Codex free tier for open source maintainers is a strategic adoption play worth tracking
- Claude Code's programmable layer (hooks, skills, MCP, CLAUDE.md) is a key differentiator — rewards investment over time
- Codex's isolation-first security model satisfies compliance more readily out of the box; Claude Code's is more flexible but requires responsible config
- Enterprise adoption patterns differ: Claude Code via individual dev toolchains, Codex via team task queues

**Action Items:**
- This content should be ingested into wiki as knowledge about Claude Code ecosystem and competitive landscape
- Relevant wiki pages to update/create: Claude Code capabilities, Codex comparison, AI coding tools landscape
- Article references multiple blog posts (hooks mastery, extension stack, skills guides, enterprise adoption) — these could be future `/ingest` targets for deeper wiki coverage