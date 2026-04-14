# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese comparison article between Claude Code and OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Article produced: "Claude Code vs Codex：终端 Agent 与云端 Agent，开发者该选谁？" — slug `claude-code-vs-codex`, category `tools`, lang `zh`
- Core framing: Claude Code = "终端里的 AI 同事" (local, interactive, real-time); Codex = "云端的 AI 外包团队" (async, parallel, PR-delivery)

**Decisions Made:**
- Article format follows established compare template (frontmatter with `item_a/item_b`, related links, FAQ section, TL;DR opener)
- Positioned Claude Code vs Codex as complementary tools rather than direct competitors — key differentiator is interactive vs async workflow, not model quality
- Codex described as still in research preview; enterprise maturity gap vs Claude Code noted

**Lessons Learned:**
- Codex free tier details worth noting: open-source maintainers and students each get $100/month API credits — useful for future Codex-related articles
- Codex default: no network access inside sandbox — important constraint to remember when comparing task suitability
- Claude Code Pro = $20/mo, Max = $100–200/mo; ChatGPT Pro (includes Codex) = $200/mo — pricing anchors for future compare articles

**Action Items:**
- Publish article at `/zh/compare/claude-code-vs-codex`
- Cross-link from `claude-code-vs-cursor` compare page and Codex deep-dive guide once live
- Update wiki index if a `codex.md` or `claude-code.md` wiki page exists to reference this compare