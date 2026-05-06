# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex (2025)

**Key Exchanges:**
- Comprehensive feature comparison covering architecture, DX, context systems, code quality, pricing, and enterprise fit

**Decisions Made:**
- Article positions the two as complementary rather than competitors — "not interchangeable, optimize for different workflows"
- Verdict framework: quality bottleneck → Claude Code; throughput bottleneck → Codex
- Strongest setup = both together (Claude Code for complex interactive, Codex for batch well-scoped)

**Lessons Learned:**
- **Architecture cascade:** Claude Code = local terminal (full env access, single machine); Codex = cloud sandbox (isolated, no network during execution, parallelizable). This one difference drives every other tradeoff.
- **2025 Codex ≠ 2021 Codex:** New product is an autonomous agent built on codex-1 (fine-tuned o3), not the old code-generation model that powered early Copilot.
- **Context maturity:** Claude Code's CLAUDE.md + SKILL.md + 7 programmable layers is more granular than Codex's AGENTS.md + setup script. Teams invested in skills get better consistency from Claude Code.
- **Pricing models:** Claude Code = per-token API or Max plan ($100-200/mo); Codex = bundled in ChatGPT Pro ($200/mo) / Team ($30/user/mo). Light users favor Codex subscription; heavy users on Sonnet/Haiku may find Claude Code cheaper per task.
- **Codex limitations:** No network in sandbox → tests requiring external services fail unless mocked. Must handle all deps in setup script.
- **Quality risk pattern:** Async model (Codex) increases temptation to merge without deep review → quality regression risk (citing speed-vs-quality study).
- **Enterprise signals:** Claude Code adopted at Ramp, Shopify, Spotify. Codex fits GitHub Issues → PR pipeline for backlog-clearing teams.

**Action Items:**
- Article references several internal links (`/blog/...`, `/compare/...`) — ensure those pages exist or are planned
- Consider ingesting this as a wiki page covering Claude Code vs Codex competitive positioning