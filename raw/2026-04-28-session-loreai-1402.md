# Session Capture: loreai

**Date:** 2026-04-28
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: Claude Code vs OpenAI Codex for the LoreAI blog.

**Key Exchanges:**
- Comprehensive feature-by-feature comparison covering: context systems, developer experience, coding capability, security, pricing, and use-case recommendations.

**Decisions Made:**
- **Framing:** Position Claude Code and Codex as complementary, not competing tools — different workflows, not different quality tiers.
- **Decision rules as structure:** Each section ends with a concrete "Decision rule" one-liner — effective format for comparison content.
- **Verdict formula:** Claude Code → senior terminal-native engineers wanting steering control; Codex → teams scaling AI-assisted dev across varying skill levels.

**Lessons Learned:**
- Claude Code advantage = persistent context (CLAUDE.md, SKILL.md) + local execution + interactive steering. Codex advantage = async fire-and-forget + self-verification via test suite + parallel task slots.
- Codex relies on repo-level context only (no CLAUDE.md equivalent) — misses unwritten conventions. Important gap for complex projects.
- Security architecture difference is fundamental: Claude Code is local-first (code stays on machine), Codex is cloud-first (repo cloned to sandboxed containers). This is a hard constraint for some orgs.
- Pricing asymmetry: Claude Code entry at $20/mo (Pro), Codex bundled into $200/mo ChatGPT Pro or $30/user Team plans. Codex has free tiers for OSS maintainers and students.
- Code quality depends more on task-tool fit than raw model capability — context-heavy tasks favor Claude Code, test-verified scoped tasks favor Codex.

**Action Items:**
- Article references several internal links (`/blog/claude-code-hooks-mastery`, `/blog/codex-vscode`, `/blog/codex-complete-guide`, etc.) — ensure all target pages exist before publishing.
- Consider ingesting this into wiki as a `claude-code-vs-codex.md` page for the AI/LLM industry knowledge layer.