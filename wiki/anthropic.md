---
type: entity
created: 2026-04-06
last-updated: 2026-05-22
sources:
  - raw/2026-04-06-anthropic-harness-design-long-running-apps.md
  - raw/2026-04-06-claude-reviews-claude-overview.md
  - raw/2026-04-09-anthropic-managed-agents-docs.md
  - raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
  - raw/2026-04-09-anthropic-agent-capabilities-announcement.md
  - raw/2026-04-16-anthropic-opus-4-7-announcement.md
  - raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md
  - raw/2026-05-22-repo-anthropics-skills.md
  - raw/2026-05-22-anthropic-equipping-agents-skills-blog.md
tags: [wiki, company, ai-lab]
---

# Anthropic

## Summary
AI safety company and creator of the Claude model family. Publishes engineering research on agentic architectures and long-running LLM applications. Operates Anthropic Labs where researchers explore multi-agent systems.

## Details
- Builds the [[claude-model-family]] (Sonnet, Opus, Haiku)
- Builds [[claude-code|Claude Code]] — official CLI tool with 6-pillar architecture (42+ tools, 12-step query loop, 4-layer context compression, 7-layer security)
- Launched [[claude-managed-agents]] (2026-04-09, beta) — fully managed agent hosting service with containers, tools, event streaming, sessions. SDKs in 7 languages + `ant` CLI.
- Anthropic Labs publishes applied research on agentic coding patterns
- Developed [[harness-design]] patterns for multi-agent architectures
- New API capabilities (2026-04-09): code execution tool, MCP connector, Files API, extended prompt caching (1-hour TTL)
- Released [[claude-opus-4-7]] (2026-04-16) — current flagship, first Claude model with high-res vision (3.75MP) and model-native agentic controls ([[xhigh-effort-level]], [[task-budgets]]). Safety posture: deliberately reduced cyber capabilities relative to the unreleased Mythos Preview (Project Glasswing).
- Research staff includes [[prithvi-rajasekaran|Prithvi Rajasekaran]] (harness design work)
- **[[computer-and-browser-use|Computer & Browser Use]]** — API capability (`computer_20251124` tool type) letting Claude drive a real computer/browser via screenshots + click/keystroke output. Built-in prompt-injection classifier runs free with the official tool. 2026-05-13 best-practices post (Lucas Gonzalez + Luca Weihs) compresses a year of production lessons. See also [[demonstration-based-teaching]].
- **[[anthropics-skills-repo|anthropics/skills]]** (138.9K⭐, last commit 2026-05-22) — official Skills repo, 17 example SKILL.md files + the canonical [[anthropic-skill-creator|skill-creator]] meta-skill. Distributed as Claude Code plugin marketplace. The canonical implementation of [[agent-skills-standard]].
- **[[source-anthropic-equipping-agents-skills-blog|"Equipping Agents for the Real World with Agent Skills"]]** (2025-10-16, Barry Zhang + Keith Lazuka + Mahesh Murag) — the **foundational engineering blog post** that introduced Agent Skills publicly. Establishes onboarding-guide framing, progressive-disclosure 3-tier architecture, "effectively unbounded" context philosophy, and the recursive vision ("agents to create, edit, and evaluate Skills on their own") that subsequent meta-skills implement.

## Connections
- Related: [[claude-model-family]], [[claude-code]], [[claude-managed-agents]], [[harness-design]], [[multi-agent-architecture]], [[computer-and-browser-use]], [[anthropics-skills-repo]], [[anthropic-skill-creator]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-06 | raw/2026-04-06-anthropic-harness-design-long-running-apps.md | Initial creation from engineering blog post |
| 2026-04-06 | raw/2026-04-06-claude-reviews-claude-overview.md | Added Claude Code as product, architecture details |
| 2026-04-09 | raw/2026-04-09-anthropic-managed-agents-docs.md | Added Claude Managed Agents as product, API capabilities |
| 2026-04-17 | raw/2026-04-16-anthropic-opus-4-7-announcement.md | Added Opus 4.7 release |
| 2026-05-16 | raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md | Added Computer & Browser Use as product surface; `computer_20251124` tool type with free prompt-injection classifier |
