# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex (coding agent) vs ChatGPT for software development workflows.

**Key Exchanges:**
- Codex = async delegation tool (clones repo, produces PRs); ChatGPT = sync collaboration tool (conversational, no repo context)
- Codex requires GitHub integration; no GitLab/Bitbucket support at time of writing
- Codex bundled into ChatGPT Pro ($200/mo), Team, or Enterprise — not standalone

**Decisions Made:**
- Article frames them as complementary, not competing: "ChatGPT for thinking, Codex for executing"
- Decision framework: Codex wins for multi-file production tasks (features, test suites, refactors, dependency upgrades); ChatGPT wins for learning, brainstorming, quick scripts, explanations
- ROI threshold: "Do you ship enough GitHub PRs per week that automated PR generation saves you meaningful time?"

**Lessons Learned:**
- Codex output quality depends heavily on task specificity — vague prompts → vague PRs
- ChatGPT's manual transfer step (copy code → paste → test → iterate) compounds into significant friction at scale
- Codex has queue latency even for simple tasks — no instant feedback loop
- Free Codex access exists for open-source maintainers and students (credit program)

**Action Items:**
- Article includes internal cross-links to other LoreAI blog posts (Codex for students, Codex VS Code extension, multi-agent workflows, Codex complete guide, Codex for open source) — ensure those referenced pages exist in wiki or drafts
- Consider creating/updating wiki pages: `openai-codex.md`, `chatgpt-coding.md`, `ai-coding-tools-comparison.md`