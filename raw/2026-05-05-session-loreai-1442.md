# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Article draft comparing OpenAI Codex (autonomous coding agent) vs ChatGPT for development workflows.

**Key Exchanges:**
- Codex = async task executor (clones repo, makes changes, opens PR); ChatGPT = sync interactive collaborator (request-response chat)
- Codex uses `codex-1` model fine-tuned on SWE workflows with AGENTS.md instruction format
- Codex is GitHub-only at launch (no GitLab/Bitbucket/local repos)
- Combined workflow pattern: Explore with ChatGPT → Plan with ChatGPT → Execute with Codex → Review PR → Debug with ChatGPT

**Decisions Made:**
- Pricing tiers documented: Free (no Codex), Plus $20/mo (limited Codex), Pro $200/mo (expanded Codex), Team $25/user/mo
- Codex best for: clearly scoped tasks, multi-file changes, verifiable correctness, tasks describable in 1-3 paragraphs
- ChatGPT best for: immediate feedback, exploratory work, self-contained context, explanation over execution, learning

**Lessons Learned:**
- Codex self-verifies by running tests — a key advantage over chat-based code generation
- Both tools produce lower-quality output on poorly documented/tested codebases, but Codex at least sees the mess
- Codex task quotas are metered within subscription plans — heavy use requires Pro tier
- Copilot (autocomplete) and Codex (full tasks via PR) are complementary, not competitive

**Action Items:**
- Article references internal links: `/blog/codex-vscode`, `/blog/codex-complete-guide`, `/blog/codex-for-open-source`, `/blog/codex-for-students`, `/faq/codex-download`
- Could create wiki page: `openai-codex.md` covering the agent's capabilities, pricing, and positioning vs ChatGPT/Copilot
- Could update wiki page on AI coding tools landscape if one exists