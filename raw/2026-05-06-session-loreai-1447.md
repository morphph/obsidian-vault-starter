# Session Capture: loreai

**Date:** 2026-05-06
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Drafting/reviewing a comparison article: OpenAI Codex vs Claude Code multi-agent architectures.

**Key Exchanges:**
- Detailed architectural comparison produced: Codex = share-nothing containers (each task gets fresh repo clone), Claude Code = hierarchical agent model (parent spawns typed sub-agents)
- Environment isolation: Codex uses full container sandbox (network-restricted), Claude Code uses git worktrees (process-level isolation with real environment access)

**Decisions Made:**
- Framing as complementary tools, not competitors: "Codex for batch/async delegation, Claude Code for coordinated interactive work"
- Article includes FAQ section addressing common reader questions (inter-agent communication, parallel limits, custom models, open-source use)

**Lessons Learned:**
- Codex practical limit: tasks must be independent and well-scoped; cross-cutting concerns require manual sequencing (run task → merge → run dependent task)
- Claude Code practical limit: 3-5 concurrent sub-agents is practical ceiling; beyond that, context management becomes bottleneck
- Key architectural distinction for customization: Codex = platform-level config (centralized), Claude Code = repo-level config (SKILL.md/CLAUDE.md travel with code, version-controlled)
- Codex agents cannot access local dev server, staging DB, or real integration tests (sandbox tradeoff)
- Claude Code sub-agents don't see parent's full conversation — they get self-contained prompts + inherit CLAUDE.md/SKILL.md context

**Action Items:**
- Article references several internal links (`/glossary/agentic-coding`, `/blog/claude-code-extension-stack-skills-hooks-agents-mcp`, etc.) — ensure these pages exist or are created
- Article ends with subscribe CTA for LoreAI — confirms this is publication-ready content for loreai.dev