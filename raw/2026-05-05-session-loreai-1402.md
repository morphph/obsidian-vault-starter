# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing/ingesting a comparison article on Claude Code vs OpenAI Codex (coding AI agents).

**Key Exchanges:**
- Comprehensive architectural comparison: Claude Code = local agent (pair programming), Codex = cloud worker (task delegation)
- Security model difference: Claude Code has full local permissions; Codex runs in network-isolated sandbox containers
- Context systems differ: Claude Code has persistent hierarchical memory (CLAUDE.md, skills); Codex starts fresh per task from repo clone

**Decisions Made:**
- The two tools are complements, not competitors: Claude Code for interactive/exploratory work, Codex for async/parallelizable tasks
- Recommended workflow: Claude Code for exploration → Codex for parallel implementation → Claude Code for integration/debugging → Codex for maintenance

**Lessons Learned:**
- Codex (2025) is NOT the old Codex model (2021-2023) — completely different product, shares name only
- Codex cannot access local services (databases, Docker, localhost APIs) — critical limitation for certain workflows
- Claude Code's persistent context advantage compounds over time on long-lived projects
- Pricing crossover: light users (<$100/mo) favor Claude Code per-token; heavy/team users favor Codex's $200/mo flat rate via ChatGPT Pro
- Error handling diverges: Claude Code asks for clarification on ambiguity; Codex guesses and you discover during review

**Action Items:**
- Consider creating wiki pages: `claude-code.md` (update with local agent architecture details), `openai-codex.md` (new page for the 2025 cloud agent product), `coding-agents-comparison.md` (synthesis page)
- Raw file should be saved to `raw/` if not already ingested