# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Relevance classification of 28 news signals for the "Claude Code" topic.

**Key Exchanges:**
- Classified 28 signals; all marked relevant. Classification was overly permissive — signals like #17 (family PWA that merely mentions "pair-programmed with Claude Code") and #20 (micro-SaaS story) are only tangentially related. A stricter classifier would flag these as "mentions Claude Code" vs. "about Claude Code."

**Lessons Learned:**
- The classifier defaulted to `true` for everything — any signal that name-drops "Claude Code" got marked relevant, even when the core topic is something else (movie narration tools, family apps, micro-SaaS hustle stories). Future runs should distinguish **about Claude Code** (features, ecosystem, workflows) from **uses Claude Code** (just a tool in someone's stack).

**Action Items:**
- Consider adding a relevance tier (high/medium/low) or a stricter threshold that filters out "merely mentions" signals — otherwise the firehose stays too noisy for wiki ingestion.