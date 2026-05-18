# Session Capture: loreai

**Date:** 2026-05-18
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafted/reviewed a comparison article: Claude Code vs OpenAI Codex.

**Key Exchanges:**
- Comprehensive feature comparison covering execution model, context systems, workflow integration, and use-case recommendations for both tools.

**Decisions Made:**
- **Core framing:** The tools are not direct substitutes — Claude Code optimizes for interactive complexity, Codex for async task throughput. Many teams use both.
- **Winner logic:** Claude Code wins on environment access, context/customization (CLAUDE.md/SKILL.md/hooks/MCP stack), and steering mid-task. Codex wins on parallelism (fire-and-forget sandbox model) and accessibility for non-terminal users.
- **Recommendation heuristic:** "Pick Claude Code if bottleneck is complex engineering; pick Codex if bottleneck is task throughput."

**Lessons Learned:**
- The execution model (local terminal vs cloud sandbox) is the single architectural decision that shapes every other tradeoff — iteration speed, environment fidelity, security boundary, parallelism.
- Claude Code's customization advantage compounds over time (CLAUDE.md → SKILL.md → hooks → MCP), while Codex is faster to start with (zero config) but harder to fine-tune.
- Codex's async model mirrors delegation to a junior dev (assign → review → merge); Claude Code's sync model mirrors pair programming.
- Codex has ecosystem plays for adoption: free tiers for open-source maintainers and students.

**Action Items:**
- Article references several other posts (`/blog/claude-code-complete-guide`, `/blog/codex-complete-guide`, etc.) — ensure all linked pages exist in wiki or drafts.
- Cross-link from existing wiki pages on [[Claude Code]] and [[OpenAI Codex]] if they exist.
- Consider ingesting this comparison into `wiki/` as a knowledge page (e.g., `wiki/claude-code-vs-codex.md`) for future `/query` retrieval.