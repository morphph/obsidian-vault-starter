# Session Capture: loreai

**Date:** 2026-05-11
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Codex CLI vs Claude Code for AI-assisted development.

**Key Exchanges:**
- Detailed architectural comparison: Codex CLI = async cloud containers (sandboxed), Claude Code = interactive local terminal sessions
- Model comparison: Codex uses codex-1 (fine-tuned o3); Claude Code uses Sonnet 4 / Opus 4 with flexible switching
- Pricing parity at entry ($20/mo both platforms), diverges at heavy usage tiers ($100-200/mo for Claude Max, $200/mo for ChatGPT Pro)

**Decisions Made:**
- **Verdict favors Claude Code** for most daily dev work — local execution, richer extension stack (skills/hooks/MCP/agent teams), tighter feedback loops
- **Codex CLI wins** for async delegation, sandboxed safety, parallel independent tasks
- Positioned as complementary tools, not competitive — many devs use both

**Lessons Learned:**
- Execution environment and tooling ecosystem matter more than raw model capability for day-to-day coding
- Codex CLI's sandbox tradeoff: strong isolation but can't access local services (DBs, internal APIs, private registries)
- Claude Code's "Ralph Wiggum" pattern and structured skills emerged from community, adopted broadly
- Large monorepos favor Claude Code (no container cloning overhead)
- Neither replaces GitHub Copilot — agents vs autocomplete are complementary
- AGENTS.md (Codex) vs CLAUDE.md + skills (Claude Code) — project context config quality matters more than model differences for output quality

**Action Items:**
- Article references several internal links (`/blog/claude-code-complete-guide`, `/blog/codex-complete-guide`, etc.) — ensure these exist or are planned
- Article ends with `/subscribe` CTA for LoreAI — confirm this is wired up
- Consider ingesting this comparison into `wiki/` as a reference page (e.g., `wiki/codex-cli-vs-claude-code.md`)
- Reassess comparison in ~6 months as both tools evolve rapidly