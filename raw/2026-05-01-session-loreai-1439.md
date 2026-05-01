# Session Capture: loreai

**Date:** 2026-05-01
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Raw source content — a comprehensive comparison article of OpenAI ChatGPT vs Codex for coding workflows (likely destined for LoreAI blog).

**Key Exchanges:**
- Article maps ChatGPT as conversational coding assistant vs Codex as autonomous repo-aware engineering agent
- Codex runs on **codex-1**, derived from o3, RL-trained specifically on coding edit-test-iterate loops
- ChatGPT uses GPT-4o (default), o3, o4-mini — general-purpose, not engineering-optimized
- Codex spins up a cloud sandbox, clones the repo, installs deps, runs tests, produces a PR-ready diff
- Codex requires Pro ($200/mo), Team ($25/user/mo), or Enterprise — not available on Free or Plus

**Decisions Made:**
- None (this is source material, no editorial decisions captured)

**Lessons Learned:**
- Codex's sweet spot: multi-file refactors, bug fixes with test suites, automated backlog processing (GitHub issues → PRs)
- ChatGPT's sweet spot: quick snippets, learning/exploration, code review, budget-constrained developers
- Key framing: they are **complementary layers**, not competitors — ChatGPT for conversational work, Codex for engineering work
- The $20 → $200 jump (Plus → Pro) is the real decision point; Codex justifies itself only when copy-paste-test friction is high
- Codex has no standalone access path — it's a feature inside ChatGPT platform
- OpenAI offers targeted free Codex access for students and open-source maintainers

**Action Items:**
- This content should be ingested into wiki as a raw source covering OpenAI Codex and ChatGPT product positioning/pricing/capabilities (relevant to `wiki/` pages on OpenAI, AI coding tools, pricing models)