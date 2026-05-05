# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article on OpenAI Codex vs Claude Code subagents and custom agents.

**Key Exchanges:**
- Detailed architectural comparison: Codex = cloud-first disposable containers with frozen repo snapshots; Claude Code = local-first with direct Agent tool control and typed subagents (Explore, Plan, codex-rescue)
- Customization stack comparison: Codex relies on per-session prompts (no persistent agent personas); Claude Code uses layered skill files + CLAUDE.md + hooks (version-controlled, team-shareable)

**Decisions Made:**
- Article frames it as a "both/and" verdict — many teams adopting hybrid (Claude Code for real-time pairing, Codex for async batch work)
- Security axis: Codex wins on container isolation (architecturally enforced); Claude Code wins on flexibility (permission-based + hooks guardrails)
- Customization axis: Claude Code wins — upfront investment in skill files compounds across sessions/team members; Codex ceiling is the prompt itself

**Lessons Learned:**
- Codex agents cannot observe each other mid-task — they merge results at completion only. This makes coordination predictable but limits dynamic collaboration
- Claude Code's custom agents emerge from the extension stack (skills → CLAUDE.md → hooks), not from a declarative config file — same pattern this wiki repo uses
- Key differentiator for teams: Claude Code agent definitions are collaborative artifacts living in the repo; Codex agent behavior is per-session platform-determined

**Action Items:**
- Article references several internal links (`/blog/claude-code-agent-teams`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — these should be verified or created as wiki pages if the concepts are worth tracking
- Consider ingesting this as a wiki page covering [[codex-vs-claude-code]] comparison or updating existing [[claude-code]] and [[codex]] pages with the subagent/custom-agent details