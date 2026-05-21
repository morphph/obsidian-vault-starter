# Session Capture: loreai

**Date:** 2026-05-21
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Processing a comprehensive comparison article: Claude Code vs OpenAI Codex (mid-2026 snapshot)

**Key Exchanges:**
- Detailed feature comparison between Claude Code (Anthropic) and OpenAI Codex as AI coding agents
- Claude Code = interactive, terminal-native, deeply configurable (CLAUDE.md + SKILL.md + hooks + MCP)
- Codex = async/fire-and-forget, cloud-sandboxed, ChatGPT-integrated, AGENTS.md config only

**Decisions Made:**
- Article positions the tools as complementary, not competing — different workflows suit different tools
- Claude Code recommended for: complex/ambiguous tasks, teams with strong conventions, large coordinated changes, terminal-native devs
- Codex recommended for: well-defined task backlogs, security-sensitive environments, async-first teams, predictable subscription costs
- Verdict: senior devs/strong-convention teams → Claude Code; high-volume well-specified tasks → Codex; many teams should use both

**Lessons Learned:**
- Claude Code's extension stack (CLAUDE.md → SKILL.md → hooks → MCP) has no Codex equivalent — significant customization advantage
- Codex's sandboxed isolation is a genuine security advantage for regulated industries
- Claude Code agent teams enable coordinated parallel sub-agents; Codex parallelism is embarrassingly parallel (independent tasks only)
- Config files are NOT interchangeable: CLAUDE.md ≠ AGENTS.md — teams using both maintain separate configs
- Codex can't ask clarifying questions mid-task — ambiguous prompts get best-guess treatment
- Pricing models diverge: Claude Code = per-token or subscription tiers ($20-200/mo); Codex = bundled in ChatGPT subscriptions ($30-200/mo)

**Action Items:**
- This content should be ingested into wiki as a source document covering Claude Code capabilities, Codex comparison, and AI coding agent landscape (mid-2026)
- Pricing details flagged as freshness-sensitive — needs periodic review
- Cross-references needed: links to `/blog/claude-code-vs-cursor` comparison mentioned but not yet processed