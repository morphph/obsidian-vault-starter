# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working on a comprehensive comparison article: Codex CLI vs Claude Code — positioning, architecture, pricing, and use-case guidance.

**Key Exchanges:**
- Codex CLI = async, cloud-sandboxed, parallel task executor (OpenAI). Claude Code = sync, local-execution, interactive collaborator (Anthropic).
- Codex runs in isolated containers from repo snapshots; cannot see local changes or services. Claude Code works with live local environment.
- Security model difference: Codex = zero-trust sandbox (can't cause local damage). Claude Code = permission-gated (full shell access with approval layers + hooks).

**Decisions Made:**
- Decision rules articulated for choosing between tools:
  - Independent, well-defined tasks → Codex CLI (batch & review PRs)
  - Iterative, ambiguous, local-state-dependent tasks → Claude Code (pair-program)
  - Security-first orgs → Codex sandbox model
  - Deep customization needs → Claude Code (7 programmable layers, SKILL.md, hooks, MCP)
- "Many teams use both" is the recommended stance — not competitors, different points on autonomy spectrum

**Lessons Learned:**
- Codex limitation: works from point-in-time snapshot; no access to local services, dev DB, running containers
- Claude Code limitation: one-developer-one-agent (partially addressed by remote sessions + background agents)
- Pricing crossover: Claude Code variable costs can exceed $200/month for power users, making Codex Pro competitive
- Monorepo edge: Claude Code wins because local filesystem access avoids full-clone overhead
- Multi-file changes: Codex plans upfront (review full diff); Claude Code edits incrementally (can redirect mid-task)

**Action Items:**
- Article appears ready for `drafts/` — contains full structure with H2 sections, FAQ, verdict, and CTA
- Pricing data (ChatGPT Pro $200/mo, Team $30/user/mo, Claude Code ~$2-50/day variable) should be cross-referenced for freshness — may need updating given 2026 date context