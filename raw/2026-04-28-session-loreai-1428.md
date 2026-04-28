# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comprehensive comparison article: Claude Code vs Codex CLI for the LoreAI blog.

**Key Exchanges:**
- Full feature-by-feature comparison drafted covering: context systems, extensibility, pricing, model capabilities, safety/trust, and use-case recommendations

**Decisions Made:**
- Verdict: Claude Code recommended for most professional dev teams; Codex CLI better for open-source, security-constrained, and open-source-control-focused workflows
- Framed as complementary tools, not mutually exclusive — teams can use both for different scenarios
- Pricing comparison kept deliberately hedged ("treat these details as current at time of writing, April 2026") given rapid market shifts

**Lessons Learned:**
- Claude Code's key differentiators: CLAUDE.md/SKILL.md context system, hooks, MCP servers, agent teams — these compound over time on the same codebase
- Codex CLI's key differentiators: network-disabled sandbox (genuine isolation, not just permission prompts), Apache 2.0 open source, bring-your-own-key pricing, no platform fee
- Safety models are philosophically different: Codex = "agent can't do harm" (isolation); Claude Code = "agent can't do harm without approval" (transparency + control)
- Extension philosophy difference: Claude Code = structured extension points; Codex CLI = fork the source code
- Neither tool supports the other's model ecosystem — model preference should drive tool choice

**Action Items:**
- Article references multiple internal blog links (`/blog/claude-code-agent-teams`, `/blog/codex-complete-guide`, etc.) — ensure all linked pages exist before publishing
- Article includes a subscribe CTA at the bottom — confirm `/subscribe` route is live
- Pricing section will need periodic updates as both platforms evolve