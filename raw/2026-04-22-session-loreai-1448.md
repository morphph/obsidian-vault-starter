# Session Capture: loreai

**Date:** 2026-04-22
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language FAQ SEO page for the keyword "claude code model options" for the LoreAI site.

**Key Exchanges:**
- Skill invoked to produce a `/zh/faq/claude-code-model-options` page covering Opus/Sonnet/Haiku model tiers, CLI switching methods (`--model`, env var, `/fast`), and `--append-system-prompt` usage
- Source material was SERP + internal cluster links; no external fabrication

**Decisions Made:**
- Default model framed as Sonnet (balanced cost/capability); Opus for complex reasoning; Haiku for low-complexity/high-frequency tasks
- `/fast` mode clarified as speed-optimized Opus, not a model downgrade — important distinction to preserve in wiki if a Claude Code page exists
- Internal links selected: seven-programmable-layers, extension-stack, 5-skills-i-use-every-day, hooks-mastery, 9-principles-writing-skills

**Action Items:**
- If wiki page `claude-code.md` or `claude-code-models.md` doesn't exist yet, consider ingesting this FAQ's model-tier framing into it
- Verify frontmatter `related_glossary: agentic-coding` resolves to a real wiki page (`/zh/glossary/agentic-coding`)