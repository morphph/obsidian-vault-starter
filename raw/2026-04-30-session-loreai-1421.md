# Session Capture: loreai

**Date:** 2026-04-30
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article/draft comparing Codex CLI vs Claude Code as AI coding agents — architectural differences, workflows, pricing, and recommendations.

**Key Exchanges:**
- Codex CLI = sandboxed, async, fire-and-forget execution (cloud containers, GitHub-centric). Claude Code = interactive, local environment, real-time pair programming.
- Permission models differ fundamentally: Codex uses hard sandbox boundary; Claude Code uses permission prompts + hooks system for programmatic safety.
- Claude Code's extensibility is significantly more mature: 7 programmable layers (CLAUDE.md, skills, hooks, MCP, agent teams) vs Codex's "configure the prompt" approach.

**Decisions Made:**
- Article verdict: complementary tools, not competitors. If forced to pick one → Claude Code for terminal-first devs wanting deep project understanding; Codex for async batch delegation with sandbox safety.
- Strongest teams use both: Codex for bulk/batch (issue triage, multi-repo patches), Claude Code for complex interactive sessions.

**Lessons Learned:**
- Codex safer for junior devs and untrusted repos (hard sandbox boundary). Claude Code more powerful but requires trust + review discipline.
- Codex's async model maps naturally to CI/CD pipeline triggers; Claude Code's interactive model better for judgment-call-heavy tasks.
- Pricing comparison is usage-dependent: Codex bundled with ChatGPT Pro ($200/mo); Claude Code is per-token API billing or Max subscription ($100-200/mo). Light users may pay less with Claude Code; heavy parallel usage may favor Codex subscription.
- Model quality differences are marginal for typical tasks — execution model (sync vs async, sandboxed vs local) matters more than model capability differences.
- Claude Code's persistent context (CLAUDE.md, memory across sessions) gives edge for codebases you work in repeatedly.

**Action Items:**
- This content should be ingested into wiki as a comparison page (e.g., `codex-cli-vs-claude-code.md`) covering the AI coding tools landscape.
- Update wiki entries for Claude Code and Codex CLI with cross-references if they exist.
- Pricing data is time-sensitive (article acknowledges frequent changes) — flag for periodic review.