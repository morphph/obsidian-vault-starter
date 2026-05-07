# Session Capture: loreai

**Date:** 2026-05-07
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Draft article comparing OpenAI Codex vs Claude Code sub-agent architectures for agentic coding workflows.

**Key Exchanges:**
- Detailed architectural comparison: Codex = cloud-first, container-per-task, async model; Claude Code = local-first, shared-context, interactive model
- Codex parallelism is horizontal (many independent tasks), Claude Code parallelism is vertical (decomposing one complex task)
- Claude Code's `codex-rescue` agent type enables hybrid workflows — Claude Code orchestrates, Codex executes in sandbox

**Decisions Made:**
- Article frames both tools as complementary, not competitive — recommended combo: Claude Code for design/orchestration → Codex for scale execution → Claude Code for review
- Verdict: Claude Code for interactive, context-rich multi-agent work; Codex for team-scale async task processing
- Pricing comparison structured by workflow type (10 bug fixes vs 1 complex refactoring vs daily team usage) rather than raw per-token math

**Lessons Learned:**
- Codex cold-start penalty (clone + install + build per task) is the main tradeoff for its strong isolation
- Codex agents cannot communicate mid-task — coordination must happen via merged PRs or external orchestration
- Claude Code worktree isolation provides container-like safety without cold-start cost
- Claude Code's layered config (CLAUDE.md → SKILL.md → agent prompts) is more powerful but higher learning curve than Codex's flat instruction files
- Practical Claude Code sub-agent limit is 2-5 parallel agents per workflow, constrained by tokens and system resources

**Action Items:**
- This content references several internal links (`/blog/...`, `/glossary/...`) that should be verified or created as wiki pages if they represent real concepts worth tracking
- Consider ingesting this as a wiki page covering [[codex-vs-claude-code]] or [[agentic-coding-tools-comparison]]
- The pricing section may need updating as both platforms' pricing evolves — flag for periodic review