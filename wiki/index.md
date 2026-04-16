# Index

## Entities

- [[anthropic]] — AI safety company, creator of Claude models and Claude Code
- [[claude-code]] — Anthropic's official agentic CLI tool, 6-pillar architecture
- [[claude-model-family]] — Anthropic's LLM models (Sonnet, Opus, Haiku) with different capability/cost tiers
- [[akshay-pachaar]] — Tech content creator, co-author of "Anatomy of an Agent Harness"
- [[claude-memory-compiler]] — Hook-based persistent memory for Claude Code, compiles conversations into knowledge articles
- [[openclaw]] — Platform for building AI assistants, used by Ryan Sarver to build "Stella"
- [[prithvi-rajasekaran]] — Anthropic Labs researcher, author of harness design blog post
- [[ryan-sarver]] — VC who built "Stella," production-grade AI chief of staff on OpenClaw
- [[troy-hua]] — Researcher at EverMind, PhD CMU; reverse-engineered Claude Code's 7-layer memory system
- [[boris-cherny]] — Creator of Claude Code at Anthropic; 388K followers, published viral best practices threads
- [[tw93]] — Chinese open-source dev (Kaku, Pake); published 2.8M-view Claude Code engineering guide
- [[geoffrey-huntley]] — Creator of the Ralph Wiggum technique; built CURSED lang, coined "the loop is the hero"
- [[matt-pocock]] — Developer and content creator behind AI Hero; authored definitive Ralph Wiggum practical guide
- [[blog2video]] — AI精读 video pipeline: articles/tweets → narrated slide videos for Chinese platforms
- [[loreai]] — loreai.dev SEO/content platform with glossary, FAQ, and programmatic content pipeline
- [[claude-managed-agents]] — Anthropic's managed agent hosting service (beta 2026-04-09): containers, tools, events, sessions
- [[claude-code-monitor-tool]] — Event-driven background monitoring tool in Claude Code (v2.1.98): stdout lines wake the session
- [[ralph-orchestrator]] — Production Rust implementation of Ralph Wiggum (2,702 stars): hats, waves, Telegram HITL, multi-backend

## Concepts

- [[harness-design]] — Multi-agent architectures for long-running LLM tasks, inspired by GANs
- [[query-loop]] — 12-step state machine driving agentic iteration in Claude Code
- [[context-management]] — 7-layer memory architecture; context window as scarcest resource
- [[context-anxiety]] — Failure mode where agents prematurely wrap up as context fills
- [[self-evaluation-bias]] — Failure mode where agents overconfidently approve their own mediocre work
- [[multi-agent-architecture]] — Specialized LLM agents collaborating with distinct roles
- [[permission-system]] — Seven-layer defense-in-depth security architecture in Claude Code
- [[orchestration-loop]] — TAO (Thought-Action-Observation) cycle; the heartbeat of any agent harness
- [[verification-loops]] — Quality assurance via rules-based, visual, and LLM-as-judge approaches (2-3x improvement)
- [[assumptions-expire]] — Principle: strip scaffolding as model capabilities improve
- [[zero-friction-capture]] — Hook-based automatic knowledge capture without user action
- [[compiler-analogy]] — Architecture framework: source → compiler → executable → test → runtime
- [[index-over-rag]] — At personal scale, structured index outperforms vector similarity for retrieval
- [[time-gated-compilation]] — Capture all day, compile after time gate (e.g., 6 PM)
- [[connection-articles]] — Cross-cutting insights as first-class standalone wiki pages
- [[agent-sdk-vs-claude-code]] — When to use Agent SDK (unattended) vs CLI (interactive)
- [[kaizen-loop]] — Self-improving AI system: scheduled environmental scanning + daily friction learning
- [[llm-judgment-vs-scripts]] — Design principle: LLMs handle judgment, scripts handle deterministic operations
- [[two-pipeline-architecture]] — External + internal knowledge converging at raw/ into one wiki
- [[session-memory]] — Claude Code Layer 3: continuous note-taking by forked subagent; enables free compaction
- [[dreaming]] — Claude Code Layer 6: cross-session memory consolidation, modeled after biological sleep
- [[forked-agent-pattern]] — Foundation for all Claude Code background ops; isolated context + shared cache
- [[prompt-cache-optimization]] — Cross-cutting: 200x cost difference drives every architectural decision
- [[infrastructure-layer]] — The "4th layer" beyond weights/context/harness: multi-tenancy, RBAC, state persistence, coordination
- [[context-noise-governance]] — Context as noise problem, not capacity; MCP cost breakdown, layering strategy, Compact Instructions
- [[documentation-layers]] — Meta-convention: table in CLAUDE.md mapping change types to correct documentation layers, prevents Layer 1 bloat
- [[silent-fallback-antipattern]] — Hard stops over silent quality degradation; preflight gate pattern as remedy
- [[content-distribution-china]] — 微信视频号 + 小红书 platform strategies: social-driven vs search-driven
- [[keyword-grouping-engine]] — SEO keyword clustering: intent classification, content type assignment, reusable prompt engine
- [[managed-agents-architecture]] — Brain/hands/session decoupling: stateless harness, lazy containers, append-only event log
- [[managed-agents-outcomes]] — Rubric-driven self-evaluation with separate grader context (research preview)
- [[managed-agents-multiagent]] — Coordinator + specialized agent threads sharing container (research preview)
- [[managed-agents-memory-stores]] — Persistent workspace-scoped memory across sessions with versioning (research preview)
- [[claude-code-sandboxing]] — OS-level filesystem + network isolation for Claude Code; security foundation for AFK Ralph
- [[ralph-wiggum]] — Autonomous AI coding loop: agent chooses tasks from PRD, HITL→AFK progression, feedback loops
- [[software-entropy]] — AI-accelerated codebase deterioration; "the repo wins" — agents amplify existing code quality

## Synthesis

- [[knowledge-compiler-design]] — Full roadmap: 9 Agent SDK use cases across 3 phases (foundation → automation → intelligence)

## Connections

- [[connection-context-anxiety-and-zero-friction-capture]] — Human context anxiety mirrors LLM context anxiety; both solved at harness level
- [[connection-llm-judgment-vs-scripts-and-harness-design]] — Convergent evolution: VC and AI lab independently discover same LLM/scaffolding boundary
- [[connection-assumptions-expire-and-tool-evolution]] — Tool evolution (AskUserQuestion, TodoWrite, Search) as concrete evidence that scaffolding built for weak models becomes shackles
- [[connection-silent-fallback-and-verification-loops]] — Pipeline input degradation as the gap verification-loops miss; preflight gates as input guardrails
- [[connection-compiler-analogy-and-content-pipelines]] — Compiler analogy generalizes beyond knowledge systems to video and content pipelines

## Visuals

- [[visual-harness-design]] — Problem → pattern → architecture → implementation flow
- [[visual-wiki-architecture]] — Two pipelines → raw/ → LLM compiler → wiki/ → four operations
- [[visual-agent-sdk-roadmap]] — CLI (interactive) vs Agent SDK (unattended): 3-phase rollout plan

## Sources

- [[source-anthropic-harness-design]] — Anthropic engineering blog on GAN-inspired multi-agent coding architectures (2026-03-24)
- [[source-claude-reviews-claude]] — 17-chapter Chinese-language deep-dive into Claude Code architecture (2026-04-06)
- [[source-claude-memory-compiler]] — GitHub repo: hook-based persistent memory for Claude Code (2026-04-07)
- [[source-rsarver-ai-chief-of-staff]] — Ryan Sarver's viral X post on building AI chief of staff "Stella" on OpenClaw (2026-04-07)
- [[source-anatomy-of-agent-harness]] — 11 components + 7 decisions of production agent harnesses; benchmarks across frameworks (2026-04-07)
- [[source-troyhua-claude-code-7-layers]] — Troy Hua's 135K-view reverse-engineering of Claude Code's 7-layer memory architecture (2026-04-01)
- [[source-bcherny-claude-code-best-practices]] — Boris Cherny's 3 viral threads: personal setup, team tips, hidden features (2026-03/04)
- [[source-rohit-harness-from-claude-code-leaks]] — Rohit's 298K-view blueprint for building agent harness from Claude Code source (2026-04-08)
- [[source-tw93-claude-code-architecture-governance]] — Tw93's 2.8M-view Chinese guide on Claude Code architecture, governance & engineering (2026-03-12)
- [[source-claude-md-self-audit]] — Internal exercise: applied Boris + Tw93 frameworks to audit and restructure our own CLAUDE.md (2026-04-09)
- [[source-internal-sessions-2026-04-08-09]] — 9 Pipeline B session captures: blog2video, LoreAI, SEO tooling (2026-04-08~09)
- [[source-claude-code-official-docs]] — Official Anthropic docs cross-reference for Claude Code features (2026-04-09)
- [[source-anthropic-managed-agents-docs]] — Complete official docs for Claude Managed Agents: 10 pages, launch day (2026-04-09)
- [[source-managed-agents-engineering-blog]] — "Scaling Managed Agents: Decoupling the brain from the hands" (2026-04-09)
- [[source-agent-capabilities-announcement]] — New API capabilities announcement: code exec, MCP connector, Files API, caching (2026-04-09)
- [[source-claude-code-monitor-tool-docs]] — Official docs + community analysis on Monitor tool (2026-04-11)
- [[source-tips-ai-coding-ralph-wiggum]] — Matt Pocock's 11 tips for autonomous AI coding with Ralph Wiggum (2026-04-15)
- [[source-ghuntley-ralph-wiggum-original]] — Geoffrey Huntley's original Ralph Wiggum blog post (2025-07)
- [[source-anthropic-ralph-wiggum-plugin]] — Official Anthropic Ralph Wiggum plugin for Claude Code (2025-12)
- [[source-ghuntley-how-to-ralph-wiggum]] — Geoffrey Huntley's official Ralph methodology playbook
- [[source-anthropic-sandboxing]] — Anthropic's Claude Code sandboxing engineering blog + official docs
- [[source-humanlayer-brief-history-ralph]] — Dex Horthy's complete timeline of Ralph Wiggum (Jun 2025 → Jan 2026)
- [[source-devinterrupted-ralph-wiggum]] — Geoffrey Huntley interview on Ralph philosophy, Gas Town, MEOW
- [[source-aihero-getting-started-ralph]] — Matt Pocock's step-by-step Ralph quickstart guide
- [[source-ralph-orchestrator]] — Ralph Orchestrator GitHub Deep Scan: Rust framework, hat system, waves (2,702 stars)
- [[source-thariq-session-management-1m]] — Thariq (Anthropic): session management with 1M context, rewind, compact vs clear (2026-04-16)
