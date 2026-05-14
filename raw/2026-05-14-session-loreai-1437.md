# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Ingesting/reviewing a detailed comparison article on OpenAI Codex vs ChatGPT for coding workflows (source appears to be from LoreAI blog).

**Key Exchanges:**
- Codex is OpenAI's autonomous coding agent — runs in cloud sandbox, clones repos, writes code, runs tests, opens PRs. It's an async delegation model, not conversational.
- ChatGPT is conversational and ad-hoc — excels at architecture discussions, learning, quick syntax, non-code tasks.
- Codex is NOT a separate product — included in ChatGPT Pro ($200/mo), Team ($25/user/mo), Enterprise. No free tier (students get $100 credits).
- Codex reads the actual repo for context (broad but shallow on intent); ChatGPT relies on conversation context (narrow but deep on intent).

**Decisions Made:**
- Best practice workflow: ChatGPT for thinking/design phase → Codex for well-scoped implementation → review PR. This maps to the agentic coding model of delegation vs collaboration.

**Lessons Learned:**
- Codex value scales with: (1) test coverage in the project, (2) clarity of task descriptions. Poor tests or vague specs = poor Codex output.
- Codex sweet spots: bug fixes with repro steps, test generation, dependency updates, multi-file refactoring — all well-scoped, verifiable, tedious work.
- ChatGPT sweet spots: ambiguous/exploratory work, architecture tradeoffs, learning, prototyping, non-code tasks.
- Canvas mode narrows the gap but still operates on individual files, not projects.
- Key decision question for teams: "Is my bottleneck thinking through problems (→ ChatGPT) or doing well-scoped implementation (→ Codex)?"

**Action Items:**
- Wiki pages to create/update: `openai-codex.md` (product page), update `chatgpt.md` if exists, consider `agentic-coding.md` concept page
- Cross-reference with existing wiki coverage of Claude Code / agentic coding tools for competitive landscape context