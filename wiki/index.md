# Index

## Entities

- [[anthropic]] — AI safety company, creator of Claude models and Claude Code
- [[claude-code]] — Anthropic's official agentic CLI tool, 6-pillar architecture
- [[claude-model-family]] — Anthropic's LLM models (Sonnet, Opus, Haiku) with different capability/cost tiers
- [[claude-memory-compiler]] — Hook-based persistent memory for Claude Code, compiles conversations into knowledge articles
- [[prithvi-rajasekaran]] — Anthropic Labs researcher, author of harness design blog post

## Concepts

- [[harness-design]] — Multi-agent architectures for long-running LLM tasks, inspired by GANs
- [[query-loop]] — 12-step state machine driving agentic iteration in Claude Code
- [[context-management]] — Four-layer compression system; context window as scarcest resource
- [[context-anxiety]] — Failure mode where agents prematurely wrap up as context fills
- [[self-evaluation-bias]] — Failure mode where agents overconfidently approve their own mediocre work
- [[multi-agent-architecture]] — Specialized LLM agents collaborating with distinct roles
- [[permission-system]] — Seven-layer defense-in-depth security architecture in Claude Code
- [[assumptions-expire]] — Principle: strip scaffolding as model capabilities improve
- [[zero-friction-capture]] — Hook-based automatic knowledge capture without user action
- [[compiler-analogy]] — Architecture framework: source → compiler → executable → test → runtime
- [[index-over-rag]] — At personal scale, structured index outperforms vector similarity for retrieval
- [[time-gated-compilation]] — Capture all day, compile after time gate (e.g., 6 PM)
- [[connection-articles]] — Cross-cutting insights as first-class standalone wiki pages
- [[agent-sdk-vs-claude-code]] — When to use Agent SDK (unattended) vs CLI (interactive)
- [[two-pipeline-architecture]] — External + internal knowledge converging at raw/ into one wiki

## Connections

- [[connection-context-anxiety-and-zero-friction-capture]] — Human context anxiety mirrors LLM context anxiety; both solved at harness level

## Visuals

- [[visual-harness-design]] — Problem → pattern → architecture → implementation flow across the harness design ecosystem
- [[visual-wiki-architecture]] — Full system: two pipelines → raw/ → LLM compiler → wiki/ → four operations

## Sources

- [[source-anthropic-harness-design]] — Anthropic engineering blog on GAN-inspired multi-agent coding architectures (2026-03-24)
- [[source-claude-reviews-claude]] — 17-chapter Chinese-language deep-dive into Claude Code architecture (2026-04-06)
- [[source-claude-memory-compiler]] — GitHub repo: hook-based persistent memory for Claude Code (2026-04-07)
