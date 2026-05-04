# Session Capture: loreai

**Date:** 2026-05-04
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Signal triage batch (indices 21–29) for the Claude Code knowledge base — evaluating GitHub trending repos and Twitter mentions for wiki/blog relevance.

**Decisions Made:**
- **Signal 21 (slop-review):** Refresh `blog/claude-code-review-agents` and `faq/claude-code-skills` — Monaco-powered inline diff comments read back by agent is a novel review pattern worth documenting.
- **Signal 22 (swiftui-design-skill):** Light refresh to `faq/claude-code-skills` — the cross-platform skill portability angle (one SKILL.md across Claude Code, Cursor, Codex, OpenCode) is the real story, not the SwiftUI subject matter.
- **Signal 26 (GPT-5.5 vs Opus 4.7):** Refresh `compare/claude-code-vs-codex` — Codex leads on raw coding, Opus still leads on Japanese-language output. Language-specific nuance worth capturing.
- **Signal 28 (4-way community poll):** Refresh `compare/claude-code-vs-cursor` and `compare/claude-code-vs-codex`; **create** new `compare/claude-code-vs-cline` page (keyword: "claude code vs cline") — identified as a genuine content gap.
- **Signal 29 (/insights command):** Refresh `faq/claude-code-skills` and `faq/claude-code-cli` — the recurring self-report + bad-habits analysis workflow is a novel pattern not yet covered.
- **Signal 23 (OpenTor):** Ignored — dark-web tooling carries editorial/reputational risk despite being technically a Claude Code skill.
- **Signals 24, 25, 27:** Ignored — no extractable content or too tangential.

**Lessons Learned:**
- Editorial risk filter applied correctly: a skill can be technically relevant but editorially toxic (OpenTor case). Reputational risk > coverage value.
- Empty-summary signals (Signal 25) are not actionable — bare tweet titles without substance can't drive content.
- Cross-platform skill portability (SKILL.md working across multiple AI IDEs) is an emerging pattern worth tracking as a wiki concept.

**Action Items:**
- Create `compare/claude-code-vs-cline` — new comparison page flagged as content gap
- Refresh 5 existing pages across the actioned signals (review-agents blog, skills FAQ, CLI FAQ, vs-codex compare, vs-cursor compare)
- Track the /insights self-report ritual as a reusable workflow pattern in skills/CLI docs