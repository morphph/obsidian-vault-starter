# Session Capture: loreai

**Date:** 2026-05-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Working with a draft article comparing OpenAI Codex (agentic coding agent) vs ChatGPT for software development workflows.

**Key Exchanges:**
- Detailed product comparison between OpenAI Codex and ChatGPT covering: repo access model, execution model (async agent vs interactive chat), code quality/verification, pricing, developer experience, and language support.

**Decisions Made:**
- Article framing: "Codex is a junior developer you assign tickets to; ChatGPT is a senior engineer you pair-program with"
- Verdict: complementary tools, not competing — Codex for autonomous project-level tasks, ChatGPT for interactive exploration and snippets

**Lessons Learned:**
- **Codex (codex-1 model):** Requires GitHub repo connection, runs in sandboxed cloud environment, async execution, can run tests/linters/type-checkers in a closed loop, produces PRs not chat responses. Requires Pro ($200/mo), Team, or Enterprise plan. Free access for students and open-source maintainers.
- **Codex best for:** well-defined + multi-file + benefits from verification — bug fixes with repro steps, feature implementation following existing patterns, test generation, refactoring, dependency updates.
- **ChatGPT best for:** exploratory/conversational work — debugging unclear root causes, architecture decisions, learning, quick utilities, non-coding tasks.
- **Combined workflow pattern:** ChatGPT to explore/plan → Codex to implement → ChatGPT to review PR diff → Codex for follow-up fixes.
- **Pricing tiers (as of article date):** Free (GPT-4o with limits), Plus ($20/mo), Pro ($200/mo, includes Codex), Team ($25/user/mo).
- Codex has VS Code extension; ChatGPT has no native IDE extension (that role is GitHub Copilot, a separate product).

**Action Items:**
- Consider ingesting this as a wiki source for pages on: OpenAI Codex, agentic coding tools comparison, AI coding tool pricing
- Article includes LoreAI subscribe CTA — confirm it's ready for publication in `drafts/`