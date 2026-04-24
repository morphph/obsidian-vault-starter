# Session Capture: loreai

**Date:** 2026-04-24
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing a comparison article between Claude Code and OpenAI Codex, likely for ingestion into the wiki under builder tools.

**Key Exchanges:**
- No interactive exchanges — the session consisted of reviewing a single long-form article: "Claude Code vs. Codex" comparison piece published/drafted for LoreAI

**Decisions Made:**
- N/A (no decisions were made in this session)

**Lessons Learned:**
- Claude Code = local execution, interactive/conversational, CLAUDE.md + SKILL.md config, persistent memory, per-token API billing (~$20/mo Pro)
- Codex = cloud sandbox, async/task-based, AGENTS.md config, no persistent memory, requires ChatGPT subscription ($200/mo Pro, $25/user Team)
- Key differentiator: Claude Code can access local env (DBs, services, secrets); Codex cannot (network disabled by default in sandbox)
- Claude Code better for: debugging with real infra, complex multi-step interactive work, solo devs
- Codex better for: parallel task execution, team scale, well-defined specs, async review workflows
- Safety tradeoff: Codex sandboxed = safer by default; Claude Code has broader attack surface but permission system mitigates
- Pricing for solo devs: Claude Code Pro ($20) dramatically cheaper than Codex (requires ChatGPT Pro at $200)

**Action Items:**
- Consider ingesting this article into `raw/` and creating a `wiki/claude-code-vs-codex.md` page covering the comparison for builder tools knowledge base