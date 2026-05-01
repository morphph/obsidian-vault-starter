# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal monitoring sweep for Claude Code content strategy — 20 events analyzed from Twitter, GitHub trending, HN, and Anthropic blog (window: 2026-04-30 to 2026-05-01).

**Key Exchanges:**
- 20 signals evaluated against existing content inventory; 6 marked `ignore`, 7 `refresh`, 7 `refresh_and_create`
- High-priority new content gaps identified with suggested keywords and content types

**Decisions Made:**
- **Create new content for:** Claude Code vs Claude API (blog), Claude Security in Claude Code (faq), Plugins vs Skills vs MCP comparison (compare), prompt caching deep-dive (blog), Claude Code agent stack guide (blog), skill orchestrating external tools (tutorial), content policy refusal limits (faq), hooks security/malicious settings.json (faq)
- **Refresh existing pages:** MCP setup blog (add design-system MCP use case), memory blog (CLAUDE.md as "AI infra" framing), subagents blog (multi-advisor council pattern), hooks guides (supply chain attack warning), pricing FAQ (weekly caps + prompt caching cost insights), "not a coding tool" blog (LinkedIn automation + Blender animation examples)
- **Ignored:** ChainGPT blockchain MCP, basedbidx DeFi SDK, both too niche/crypto-adjacent

**Lessons Learned:**
- Real supply chain attack vector discovered: malicious PyPI package drops `.claude/settings.json` with hooks that steal AWS keys — all hooks content needs security warnings
- Community converging on a "three pillars" mental model: Skills = how to act, MCP = what to access, Plugin = how to run jobs — no single page covers this yet
- "Claude as agent stack" is becoming the power-user vocabulary (MCP + skills + subagents + memory + human review as unified concept)
- Prompt caching confirmed by Anthropic as the core cost driver for Claude Code — pricing FAQ currently doesn't address this
- Leaked system prompts repo trending on GitHub is strong comparison material for vs-Cursor/vs-Codex pages

**Action Items:**
- Urgent: Add supply chain security warning to all three hooks pages (signal 19)
- High priority: Create hooks security FAQ (`claude code hooks security risks malicious settings.json`)
- Create unified "Skills vs MCP vs Plugins" comparison page (signals 5 + 12 both point to same gap)
- Refresh pricing FAQ to cover: weekly rate limits, prompt caching cost mechanics, content policy refusal behavior
- Write "Claude Code agent stack" blog as the definitive full-stack architecture guide
- Incorporate prompt caching blog insights from Anthropic's official post into pricing FAQ and create standalone blog