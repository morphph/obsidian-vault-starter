# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal analysis run for LoreAI knowledge base — 20 Claude Code signals from April 13–14, 2026 triaged for wiki/content action.

**Key Exchanges:**
- Signal triage produced 20 signals: 11 actionable (refresh or create), 5 ignored, rest informational
- Signals sourced from Twitter/X accounts including @trq212, @bcherny, @ClaudeCodeLog, @_akhaliq

**Decisions Made:**
- **Create new pages** for: `/usage` command FAQ, Bedrock/Vertex simplified auth tutorial, /ultraplan web planning blog, Houtini LM MCP cost-optimization blog, Claude Code security hardening (prompt injection) blog, v2.1.105 release notes blog, claude-code-best-practices synthesis blog
- **Refresh existing pages** for: MCP setup (TurboTax connector, Houtini LM), free alternatives blog (Gemma4+Ollama, 122B local model), skills FAQ (narrator-ai-cli skill, 'expertise' renaming technique), vs-cursor and vs-codex compare pages, CLI reference FAQ (CLAUDE_CODE_NO_FLICKER, /ultraplan, v2.1.105)
- **Ignore:** GLM-5.1 benchmark (anecdotal, category mismatch), Japanese secondary coverage, Hermes agent tweet (no substance), Chinese trending roundup (duplicates signal 8), Lovecode items

**Lessons Learned:**
- "Expertise" framing for SKILL.md files (vs "skills") is a community-discovered prompting technique worth testing
- Claude Code v2.1.105: 37 CLI changes, non-Anthropic DO NOT TRIGGER tag blocking, 5-min stalled stream auto-abort
- CLAUDE_CODE_NO_FLICKER=1 enables new opt-in renderer
- /ultraplan bridges Plan Mode with web UI for cross-device plan editing
- Real-world prompt injection attacks against Claude Code CLI documented in the wild — security hardening content gap identified
- Harness-owned context makes Claude Code ↔ Codex switching stateful and costly (tool-hopping anti-pattern)

**Action Items:**
- Create 7 new content pages (FAQ, tutorial, and blog formats) from the flagged signals
- Refresh ~8 existing pages with new examples and version data
- Prioritize security hardening blog (prompt injection) and v2.1.105 changelog — high search intent, currently uncovered