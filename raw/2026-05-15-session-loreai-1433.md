# Session Capture: loreai

**Date:** 2026-05-15
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article draft (likely for LoreAI blog) comparing OpenAI Codex vs ChatGPT for coding workflows.

**Key Exchanges:**
- No interactive exchanges — this was a complete article draft provided as context, not a working session.

**Decisions Made:**
- None captured in this session.

**Lessons Learned:**
- **Codex runs codex-1** — a model fine-tuned from o3 specifically for software engineering (RL on coding objectives: diffs, repo conventions, test passing). Not the same model as ChatGPT.
- **Codex pricing gate**: Requires Pro ($200/mo), Team, or Enterprise. Free tiers exist for students and open-source maintainers. ChatGPT coding available at $20/mo or free.
- **Codex is async + repo-aware**: Clones full repo, runs your test suite in sandbox, produces structured diffs/PRs. ChatGPT is synchronous, snippet-level context only.
- **Complementary workflow pattern**: ChatGPT for planning/exploration/debugging → Codex for multi-file implementation → ChatGPT for review questions on Codex output.
- ChatGPT Code Interpreter is Python-only, designed for data analysis — not a substitute for running a project's actual toolchain.

**Action Items:**
- This article content should be ingested into the wiki via `/ingest` to create/update pages on OpenAI Codex, codex-1 model, and the Codex vs ChatGPT comparison. It contains structured pricing, capability, and workflow data relevant to `wiki/` coverage of AI coding tools.