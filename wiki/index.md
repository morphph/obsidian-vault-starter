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

## Synthesis

- [[knowledge-compiler-design]] — Full roadmap: 9 Agent SDK use cases across 3 phases (foundation → automation → intelligence)

## Connections

- [[connection-context-anxiety-and-zero-friction-capture]] — Human context anxiety mirrors LLM context anxiety; both solved at harness level
- [[connection-llm-judgment-vs-scripts-and-harness-design]] — Convergent evolution: VC and AI lab independently discover same LLM/scaffolding boundary

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
