# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage run for Claude Code content intelligence — 20 signals from Twitter, GitHub trending, and official blogs scanned on 2026-04-29/30.

**Key Exchanges:**
- 7 signals marked **refresh** or **refresh_and_create**, 13 ignored as duplicates/noise/off-topic
- Strongest new content gaps identified: (1) "How to onboard Claude Code to an existing project" tutorial (signal 7, from official Anthropic blog), (2) "Skills vs MCP vs Plugins" comparison page (signals 9 & 20 — two independent high-engagement demand signals), (3) "How to learn Claude Code free" blog linking Anthropic's 13 certified courses (signal 14), (4) MCP `alwaysLoad` FAQ from v2.1.121 release (signal 19)

**Decisions Made:**
- The Skills/MCP/Plugin triarchy is the top conceptual gap — two separate signals (Japanese guide + @ClaudeCode_love) converged on the same unmet need. Mental model: Skills=cognition, MCP=access, Plugin=execution.
- CLAUDE.md content should shift from "static config file" framing → "self-improving infrastructure" framing (mistake→rule, repeat→workflow, break→guardrail) per signal 17.
- Ethan Mollick's "build it during the meeting" pattern (signal 4) is a citable non-developer adoption tactic for PM/non-coding pages.
- Leaked system prompts repo (signal 11) is a primary source for competitive compare pages (vs Cursor, vs Codex).

**Lessons Learned:**
- Japanese-language Claude Code community is producing high-quality power-user guides — worth monitoring as leading indicators of content gaps
- Developer success story pattern (struggle → CLAUDE.md discovery → revenue) is the strongest social proof format for the memory blog (signal 15: $8,400 first client in one month)
- Claude Code v2.1.121 shipped `alwaysLoad` for MCP, `plugin prune`, `/skills type` filter — feature velocity means FAQ/reference pages go stale fast

**Action Items:**
- Create compare page: "Claude Code Skills vs MCP vs Plugins" (dedupe signals 9 & 20 into one brief)
- Create tutorial: "How to onboard Claude Code to an existing project" (source: signal 7 official blog)
- Create blog: "Free Anthropic courses learning path" (source: signal 14)
- Create FAQ: "MCP alwaysLoad option" (source: signal 19, v2.1.121)
- Refresh `blog/claude-code-memory` with: self-improving infrastructure framing (signal 17) + developer success story (signal 15) + five-layer power stack model (signal 13)
- Refresh `blog/claude-code-is-not-a-coding-tool` with: Mollick meeting tactic (signal 4) + narrator-ai skill (signal 8) + open-design repo (signal 12)
- Refresh compare pages with leaked system prompts evidence (signal 11)