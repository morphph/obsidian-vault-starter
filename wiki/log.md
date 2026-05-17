# Log

## [2026-05-17] ingest-batch | Matt Pocock idea-to-AFK-agent flow research
sources:
  - raw/2026-05-17-repo-mattpocock-skills.md
  - raw/2026-05-17-mattpocock-grill-with-docs-skill.md
  - raw/2026-05-17-aihero-grill-with-docs-changelog.md
  - raw/2026-05-17-repo-mattpocock-sandcastle.md
  - raw/2026-05-17-amplitude-ralph-loop-102-features.md
  - raw/2026-05-17-tessmann-agent-teams-ralph-hybrid.md
  - raw/2026-05-17-alexandergekov-year-of-ralph-loop.md
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
  - raw/2026-05-17-aihero-5-agent-skills.md
  - raw/2026-05-17-mattpocock-chapter-creator-thread.md
pages-created:
  - source-mattpocock-skills-repo.md
  - source-mattpocock-grill-with-docs-skill.md
  - source-aihero-grill-with-docs-changelog.md
  - source-mattpocock-sandcastle-repo.md
  - source-amplitude-ralph-loop.md
  - source-tessmann-agent-teams-ralph.md
  - source-alexandergekov-year-of-ralph.md
  - source-adityapuri-matt-skills.md
  - source-aihero-5-agent-skills.md
  - source-mattpocock-chapter-creator-thread.md
  - mattpocock-skills-library.md (entity)
  - sandcastle.md (entity)
  - grill-with-docs.md (concept)
  - context-md-pattern.md (concept)
  - hitl-vs-afk-classification.md (concept)
  - vertical-slicing.md (concept)
  - shared-contracts-pattern.md (concept)
  - opportunity-finder-pattern.md (concept)
  - idea-to-afk-agent-flow.md (synthesis — the runbook)
pages-updated:
  - matt-pocock.md (major refresh — added skills library, sandcastle, methodology)
  - ralph-wiggum.md (added 2026 evolution: token tracking, .ralph/guardrails, dispatcher pattern, hybrid)
  - index.md (added 2 entities, 6 concepts, 1 synthesis, 10 sources)
note: skipped 3 X threads (URLs not preserved by user; X content not WebFetchable). Tier 1 + Tier 2 ingest completed minus X threads. Goal: personal runbook for practicing Matt Pocock's idea→AFK-agent methodology.


<!-- Append-only. Format: ## [YYYY-MM-DD] operation | Title -->

## [2026-05-14] ingest-batch | Build with Claude Code — official docs gap fill (11 sources, 13 URLs)
sources:
- raw/2026-05-14-anthropic-claude-code-agents-overview.md (https://code.claude.com/docs/en/agents.md)
- raw/2026-05-14-anthropic-claude-code-subagents.md (https://code.claude.com/docs/en/sub-agents.md)
- raw/2026-05-14-anthropic-claude-code-agent-teams.md (https://code.claude.com/docs/en/agent-teams.md)
- raw/2026-05-14-anthropic-claude-code-worktrees.md (https://code.claude.com/docs/en/worktrees.md)
- raw/2026-05-14-anthropic-claude-code-mcp.md (https://code.claude.com/docs/en/mcp.md)
- raw/2026-05-14-anthropic-claude-code-plugins.md + plugins-reference.md (https://code.claude.com/docs/en/plugins.md + discover-plugins.md + plugins-reference.md)
- raw/2026-05-14-anthropic-claude-code-hooks-guide.md + hooks-reference.md (https://code.claude.com/docs/en/hooks-guide.md + hooks.md)
- raw/2026-05-14-anthropic-claude-code-channels.md (https://code.claude.com/docs/en/channels.md)
- raw/2026-05-14-anthropic-claude-code-channels-reference.md (https://code.claude.com/docs/en/channels-reference.md)
- raw/2026-05-14-anthropic-claude-code-scheduled-tasks.md (https://code.claude.com/docs/en/scheduled-tasks.md)
- raw/2026-05-14-anthropic-claude-code-routines.md (https://code.claude.com/docs/en/routines.md)
- raw/2026-05-14-anthropic-claude-code-programmatic-usage.md (https://code.claude.com/docs/en/headless.md)
- raw/2026-05-14-anthropic-claude-code-deep-links.md (https://code.claude.com/docs/en/deep-links.md)
- raw/2026-05-14-anthropic-claude-code-skills-refresh.md (https://code.claude.com/docs/en/skills.md — refresh of 2026-04-21)
pages-created:
- source-claude-code-agents-overview.md
- source-claude-code-subagents-docs.md
- source-claude-code-agent-teams-docs.md
- source-claude-code-worktrees-docs.md
- source-claude-code-mcp-docs.md
- source-claude-code-plugins-docs.md
- source-claude-code-hooks-docs.md
- source-claude-code-channels-docs.md
- source-claude-code-channels-reference-docs.md
- source-claude-code-scheduled-tasks-docs.md
- source-claude-code-routines-docs.md
- source-claude-code-programmatic-usage-docs.md
- source-claude-code-deep-links-docs.md
- source-claude-code-skills-docs-2026-05.md
pages-updated:
- claude-code-monitor-tool.md (added Channels as 5th category in comparison table; cross-referenced sibling primitive)
- agent-skills-standard.md (added 6 new frontmatter fields, substitution variables, skillOverrides setting, bundled skills list)
- index.md (added 14 new source-* entries under Sources)
conflicts-resolved:
- Monitor vs Channels: NOT a conflict — different transport layers. Cross-referenced in both directions.
- Skills 2026-04-21 vs 2026-05-14: PURE ADDITIONS — no claims contradicted. Old source kept; agent-skills-standard.md updated additively.
context: User requested gap-fill of all 15 "Build with Claude Code" official nav items (3 already had: Agent View, Skills, Goals; 12 added in this batch + Skills refresh = 13 ingest tasks → 14 new wiki source pages because plugins bundle covered 3 URLs in 1 page, hooks 2 in 1, channels 2 in 2 separate, scheduled-tasks/routines 2 in 2 separate).

## [2026-04-06] ingest | Harness Design for Long-Running Application Development
source: raw/2026-04-06-anthropic-harness-design-long-running-apps.md
pages-created: anthropic.md, claude-model-family.md, prithvi-rajasekaran.md, harness-design.md, context-anxiety.md, self-evaluation-bias.md, multi-agent-architecture.md, assumptions-expire.md, source-anthropic-harness-design.md
pages-updated: (none — first ingest)

## [2026-04-06] ingest | Claude Reviews Claude — 架构总览
source: raw/2026-04-06-claude-reviews-claude-overview.md
pages-created: claude-code.md, query-loop.md, context-management.md, permission-system.md, source-claude-reviews-claude.md
pages-updated: anthropic.md, harness-design.md, multi-agent-architecture.md, context-anxiety.md

## [2026-04-07] ingest | claude-memory-compiler (GitHub Deep Scan)
source: raw/2026-04-07-repo-claude-memory-compiler.md
pages-created: claude-memory-compiler.md, zero-friction-capture.md, compiler-analogy.md, index-over-rag.md, time-gated-compilation.md, connection-articles.md, source-claude-memory-compiler.md
pages-updated: harness-design.md, claude-code.md

## [2026-04-07] internal-capture | Architecture discussion synthesis
source: conversation (internal knowledge — first Pipeline B content)
pages-created: agent-sdk-vs-claude-code.md, connection-context-anxiety-and-zero-friction-capture.md, two-pipeline-architecture.md
pages-updated: index.md (added Connections category)

## [2026-04-07] internal-capture | Agent SDK roadmap synthesis
source: conversation (multi-round discussion on Agent SDK use cases)
pages-created: agent-sdk-roadmap.md, visual-agent-sdk-roadmap.excalidraw
pages-updated: index.md (added Synthesis category, Visuals entries)

## [2026-04-07T17:58:32+08:00] compile | Ryan Sarver — AI Chief of Staff on OpenClaw
source: raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md
pages-created: ryan-sarver.md, openclaw.md, kaizen-loop.md, llm-judgment-vs-scripts.md, source-rsarver-ai-chief-of-staff.md, connection-llm-judgment-vs-scripts-and-harness-design.md
pages-updated: zero-friction-capture.md

## [2026-04-07] ingest | The Anatomy of an Agent Harness
source: raw/2026-04-07-anatomy-of-agent-harness.md
pages-created: orchestration-loop.md, verification-loops.md, akshay-pachaar.md, source-anatomy-of-agent-harness.md
pages-updated: harness-design.md, context-management.md, multi-agent-architecture.md, assumptions-expire.md, query-loop.md, permission-system.md

## [2026-04-08] ingest | Troy Hua — 7 Layers of Memory and Dreaming in Claude Code
source: raw/2026-04-08-troyhua-claude-code-7-layers-memory.md
pages-created: troy-hua.md, session-memory.md, dreaming.md, forked-agent-pattern.md, prompt-cache-optimization.md, source-troyhua-claude-code-7-layers.md
pages-updated: context-management.md, claude-code.md, context-anxiety.md

## [2026-04-09] ingest | Boris Cherny's Claude Code Best Practices (3 threads)
source: raw/2026-04-09-bcherny-claude-code-best-practices.md
pages-created: boris-cherny.md, source-bcherny-claude-code-best-practices.md
pages-updated: claude-code.md

## [2026-04-09] ingest | Rohit — How I Built Harness from Claude Code Leaks
source: raw/2026-04-09-rohit-harness-from-claude-code-leaks.md
pages-created: infrastructure-layer.md, source-rohit-harness-from-claude-code-leaks.md
pages-updated: claude-code.md, query-loop.md, harness-design.md, prompt-cache-optimization.md

## [2026-04-09] ingest | Tw93 — 你不知道的 Claude Code：架构、治理与工程实践
source: raw/2026-04-09-tw93-claude-code-architecture-governance.md
pages-created: tw93.md, context-noise-governance.md, connection-assumptions-expire-and-tool-evolution.md, source-tw93-claude-code-architecture-governance.md
pages-updated: assumptions-expire.md

## [2026-04-09] synthesis | 办公桌比喻：Tw93分层 × Boris Best Practices
pages-created: connection-context-layers-and-best-practices.md
pages-consulted: boris-cherny.md, tw93.md, source-bcherny-claude-code-best-practices.md, context-noise-governance.md
answer-filed: connection-context-layers-and-best-practices.md

## [2026-04-09] synthesis | Claude Code Best Practices完全指南
sources: raw/2026-04-09-bcherny-claude-code-best-practices.md, raw/2026-04-09-claude-code-official-docs-best-practices.md
pages-created: claude-code-best-practices-guide.md
pages-consulted: boris-cherny.md, claude-code.md, context-noise-governance.md, connection-context-layers-and-best-practices.md

## [2026-04-09] visualize | Best Practices Guide — 22 practices × 6 categories
scope: topic (claude-code-best-practices-guide)
source-pages: claude-code-best-practices-guide.md
output: visual-best-practices-guide.excalidraw

## [2026-04-09] visualize | Boris Best Practices × Tw93 Context Layers
scope: topic (connection-context-layers-and-best-practices)
source-pages: connection-context-layers-and-best-practices.md, boris-cherny.md, tw93.md, context-noise-governance.md
output: visual-context-layers-best-practices.excalidraw

## [2026-04-09] ingest | CLAUDE.md Self-Audit
source: raw/2026-04-09-claude-md-self-audit.md
pages-created: documentation-layers.md, source-claude-md-self-audit.md
pages-updated: context-noise-governance.md

## [2026-04-09T19:15:10+08:00] compile | Internal Sessions 2026-04-08~09 (Pipeline B)
source: raw/2026-04-08-session-unknown-{0953,1017,1126,1139,1216,1421,1644}.md, raw/2026-04-09-session-unknown-{1620,1915}.md
pages-created: blog2video.md, loreai.md, silent-fallback-antipattern.md, content-distribution-china.md, keyword-grouping-engine.md, source-internal-sessions-2026-04-08-09.md, connection-silent-fallback-and-verification-loops.md
pages-updated: claude-code.md, permission-system.md

## [2026-04-09T19:15:10+08:00] compile | Claude Code Official Docs Reference
source: raw/2026-04-09-claude-code-official-docs-best-practices.md
pages-created: source-claude-code-official-docs.md
pages-updated: claude-code.md, permission-system.md

## [2026-04-09T19:30:00+08:00] compile | Continuation: SEO audit + connections + preflight gate
source: raw/2026-04-09-session-unknown-1915.md (LoreAI SEO audit details)
pages-created: connection-compiler-analogy-and-content-pipelines.md
pages-updated: loreai.md (added SEO audit findings), verification-loops.md (added preflight gate pattern), blog2video.md (added compiler-analogy connection), index.md

## [2026-04-09] ingest | Claude Managed Agents — Official Documentation Suite (10 pages)
source: raw/2026-04-09-anthropic-managed-agents-docs.md
pages-created: claude-managed-agents.md, managed-agents-architecture.md, managed-agents-outcomes.md, managed-agents-multiagent.md, managed-agents-memory-stores.md, source-anthropic-managed-agents-docs.md
pages-updated: anthropic.md, harness-design.md, index.md

## [2026-04-09] ingest | Scaling Managed Agents: Decoupling the Brain from the Hands
source: raw/2026-04-09-anthropic-managed-agents-engineering-blog.md
pages-created: source-managed-agents-engineering-blog.md
pages-updated: managed-agents-architecture.md, harness-design.md

## [2026-04-09] ingest | New Capabilities for Building Agents on the Anthropic API
source: raw/2026-04-09-anthropic-agent-capabilities-announcement.md
pages-created: source-agent-capabilities-announcement.md
pages-updated: anthropic.md

## [2026-04-11] ingest | Claude Code Monitor Tool — Official Docs + Community Analysis
source: raw/claude-code-monitor-tool-docs-2026-04.md
pages-created: claude-code-monitor-tool.md, source-claude-code-monitor-tool-docs.md
pages-updated: claude-code.md

## [2026-04-14] lint
pages-scanned: 70
issues: orphans(0), stale(0), contradictions(1), index-drift(0), unresolved-links(7), thin(21)
auto-fixed: fixed 2× [[silent-fallback-degradation]]→[[silent-fallback-antipattern]] in connection-compiler-analogy-and-content-pipelines.md; fixed [[Claude Code]]→[[claude-code|Claude Code]] in permission-system.md; fixed 3× [[Prithvi Rajasekaran]]→[[prithvi-rajasekaran|Prithvi Rajasekaran]] in anthropic.md + source-anthropic-harness-design.md; added layer-count clarification note to context-management.md

## [2026-04-15] ingest | 11 Tips For AI Coding With Ralph Wiggum
source: raw/2026-04-15-tips-ai-coding-ralph-wiggum.md
pages-created: ralph-wiggum.md, matt-pocock.md, software-entropy.md, source-tips-ai-coding-ralph-wiggum.md
pages-updated: harness-design.md, orchestration-loop.md, verification-loops.md, context-anxiety.md

## [2026-04-15] ingest | Ralph Wiggum Comprehensive Knowledge Base (7 sources)
sources: raw/2026-04-15-ghuntley-ralph-wiggum-original.md, raw/2026-04-15-anthropic-ralph-wiggum-plugin.md, raw/2026-04-15-ghuntley-how-to-ralph-wiggum.md, raw/2026-04-15-anthropic-claude-code-sandboxing.md, raw/2026-04-15-humanlayer-brief-history-of-ralph.md, raw/2026-04-15-devinterrupted-inventing-ralph-wiggum-loop.md, raw/2026-04-15-aihero-getting-started-with-ralph.md, raw/2026-04-15-mattpocockuk-ralph-wiggum-xthread.md
pages-created: geoffrey-huntley.md, claude-code-sandboxing.md, source-ghuntley-ralph-wiggum-original.md, source-anthropic-ralph-wiggum-plugin.md, source-ghuntley-how-to-ralph-wiggum.md, source-anthropic-sandboxing.md, source-humanlayer-brief-history-ralph.md, source-devinterrupted-ralph-wiggum.md, source-aihero-getting-started-ralph.md
pages-updated: ralph-wiggum.md (major expansion — 9 sources total), claude-code.md, matt-pocock.md, index.md

## [2026-04-15] ingest | Ralph Orchestrator (GitHub Deep Scan)
source: raw/2026-04-15-repo-ralph-orchestrator.md
pages-created: ralph-orchestrator.md, source-ralph-orchestrator.md
pages-updated: ralph-wiggum.md (added production implementation section), index.md

## [2026-04-16] ingest | Using Claude Code: Session Management & 1M Context
source: raw/2026-04-16-thariq-claude-code-session-management-1m.md
pages-created: source-thariq-session-management-1m.md
pages-updated: context-management.md, context-anxiety.md, index.md

## [2026-04-17] ingest | Introducing Claude Opus 4.7
source: raw/2026-04-16-anthropic-opus-4-7-announcement.md
pages-created: claude-opus-4-7.md, task-budgets.md, xhigh-effort-level.md, source-anthropic-opus-4-7-announcement.md
pages-updated: claude-model-family.md, anthropic.md, claude-code.md, index.md

## [2026-04-17] ingest | What's new in Claude Opus 4.7 (official API docs)
source: raw/2026-04-16-claude-docs-opus-4-7-whats-new.md
pages-created: adaptive-thinking.md, source-claude-docs-opus-4-7-whats-new.md
pages-updated: claude-opus-4-7.md, task-budgets.md, xhigh-effort-level.md, index.md

## [2026-04-18] internal-capture | Anthropic & Claude Daily-Fetch Source Verification
source: raw/2026-04-18-claude-daily-source-verification.md (Playwright-verified 10 X handles + WebFetch-tested 12 sites)
pages-created: anthropic-daily-sources.md
pages-updated: index.md (added Synthesis entry)

## [2026-04-18] anthropic-daily | 2026-01-01..2026-04-18 (backfill, Option B)
window: 2026-01-01..2026-04-18
items: ~70 raw across 10 sources, ~70 unique after dedupe
pages-created: digest-anthropic-2026-01-01-to-2026-04-18.md
raw-saved: raw/2026-04-18-anthropic-daily-backfill-2026-q1-q2.md
gaps-flagged: claude.com/blog pagination, code.claude.com/docs (JS-rendered), gh-api dated releases

## [2026-04-19] anthropic-daily | Backfill gap-fix pass
fixes: (1) confirmed claude.com/blog has 16 posts in window — added 1 missing (claude-builds-visuals 03-12); (2) updated docs URL to code.claude.com/docs (Playwright); (3) fetched 88 dated CC releases via gh api
pages-updated: digest-anthropic-2026-01-01-to-2026-04-18.md, anthropic-daily-sources.md
raw-saved: raw/2026-04-19-anthropic-daily-backfill-gap-fixes.md

## [2026-04-19] anthropic-daily | First daily run after backfill
window: 2026-04-18..2026-04-19
items: 0 new across 6 websites + gh-api releases
findings: X content scraping unreliable without auth — only @AnthropicAI returns recent posts; @felixrieseberg shows "hasn't posted" despite 2,744 lifetime posts
pages-created: digest-anthropic-2026-04-19.md
pages-updated: anthropic-daily-sources.md (X-scraping caveat), index.md
raw-saved: raw/2026-04-19-anthropic-daily-run.md

## [2026-04-19] ingest | Garry Tan — Thin Harness, Fat Skills
source: raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
fetch-method: api.fxtwitter.com (WebFetch + Playwright to x.com both failed; fxtwitter API exposed full long-form article body)
pages-created: garry-tan.md, thin-harness-fat-skills.md, skill-as-method-call.md, diarization.md, resolvers.md, latent-vs-deterministic.md, source-garry-tan-thin-harness-fat-skills.md
pages-updated: harness-design.md, openclaw.md, claude-code.md, llm-judgment-vs-scripts.md, index.md

## [2026-04-19] ingest | Garry Tan — Resolvers: The Routing Table for Intelligence
source: raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
fetch-method: Playwright MCP (x.com JS-heavy, WebFetch gated)
pages-created: check-resolvable.md, trigger-evals.md, context-rot.md, gbrain.md, gstack.md, source-garry-tan-resolvers.md
pages-updated: resolvers.md (major expansion — fractal layers, Manidis misfiling, invisible skills, governance stack, management reframe, self-healing RLM), garry-tan.md, thin-harness-fat-skills.md, openclaw.md, claude-code.md, index.md

## [2026-04-21] ingest | Anthropic — Extend Claude with Skills (official docs)
source: raw/2026-04-21-anthropic-agent-skills-docs.md
fetch-method: WebFetch (3 redirects: docs.anthropic.com → docs.claude.com → code.claude.com)
pages-created: agent-skills-standard.md, source-anthropic-agent-skills-docs.md
pages-updated: resolvers.md (added official "description as canonical resolver" wording, 1,536-char cap, SLASH_COMMAND_TOOL_CHAR_BUDGET), check-resolvable.md, trigger-evals.md, context-rot.md (mechanistic explanation), claude-code.md, thin-harness-fat-skills.md, index.md

## [2026-04-21] ingest | GitHub Deep Scan — GBrain + GStack (Garry Tan's open-source stack)
source: raw/2026-04-21-gbrain-gstack-github-deep-scan.md
fetch-method: gh CLI (tree + README + RESOLVER.md + _brain-filing-rules.md + manifest.json + CLAUDE.md + SKILL.md samples)
pages-created: source-gbrain-gstack-deep-scan.md
pages-updated: gbrain.md (massive expansion — 9,718⭐, 17,888 pages production scale, 26 skills, real TS for check-resolvable & dry-fix, Minions job queue, BrainBench numbers, PGLite/Postgres pluggable engine), gstack.md (massive expansion — 78,692⭐, 23-skill specialist roster, 10-host template system, team mode), resolvers.md (three-layer artifact: RESOLVER.md + manifest.json + SKILL.md; two-dialect table), check-resolvable.md (confirmed as real code), trigger-evals.md (three-layer integrity reframe), thin-harness-fat-skills.md (10-host cross-vendor proof), agent-skills-standard.md, index.md

## [2026-05-09] ingest | Khairallah — Build a Team of AI Agents That Replace Your First 3 Hires
source: raw/2026-05-05-khairallah-3-ai-agents-replace-first-hires.md
fetch-method: Playwright MCP (x.com long-form article)
pages-created: 3-agent-starter-team.md, prompt-architecture-three-layer.md, quality-gate-loop.md, eng-khairallah.md, source-eng-khairallah-3-ai-hires.md
pages-updated: ryan-sarver.md (Stella as canonical Operations Agent), multi-agent-architecture.md (added 3-agent business templating), gbrain.md (shared-knowledge-base-for-agent-team use case), verification-loops.md (cross-link quality-gate-loop as sister pattern), index.md

## [2026-05-09] ingest | Thariq — The Unreasonable Effectiveness of HTML
source: raw/2026-05-08-thariq-unreasonable-effectiveness-of-html.md
fetch-method: Playwright MCP (x.com long-form article)
pages-created: html-as-output-format.md, throwaway-editors.md, thariq.md (entity, promoted from prior source-only mention), source-thariq-html-effectiveness.md
pages-updated: claude-code.md (HTML-output-format insight + throwaway editors), claude-opus-4-7.md (1M-context second-order effect on output formats), diarization.md (HTML as natural form factor for one-page profiles), index.md

## [2026-05-10] ingest | Thariq — Lessons from Building Claude Code: Prompt Caching is Everything
source: raw/2026-04-30-thariq-prompt-caching-is-everything.md
fetch-method: WebFetch (claude.com static blog, no fallback needed)
pages-created: plan-mode-as-tools.md (state-as-tool-call design pattern), source-thariq-prompt-caching-is-everything.md
pages-updated: prompt-cache-optimization.md (major expansion — 4-layer ordering, `<system-reminder>`, `defer_loading`, cache-safe compaction forking, SEV-level alerting, model-swap caveat, production cache-break bug catalog), thariq.md (third article + full name + MTS title), claude-code.md (Plan Mode as tools, defer_loading, compaction buffer), index.md

## [2026-05-11] ingest | Garry Tan — Meta-Meta-Prompting: The Secret to Making AI Agents Work
source: raw/2026-05-09-garry-tan-meta-meta-prompting.md
fetch-method: Playwright MCP (x.com long-form article)
pages-created: skillify-meta-skill.md, book-mirror.md, filing-cabinet-vs-nervous-system.md, source-garry-tan-meta-meta-prompting.md
pages-updated: garry-tan.md (6th article + production milestone 100K pages/100+ skills/100+ crons), gbrain.md (100K production scale, 39 installable skills, 97.6% LongMemEval recall, Karpathy attribution, filing-cabinet-vs-nervous-system framing, named production skills), gstack.md (87K stars), resolvers.md (skillify as production primitive), index.md

## [2026-05-12] ingest | Garry Tan — On the LOC Controversy (part 3 backfill)
source: raw/2026-04-18-garry-tan-loc-controversy.md
fetch-method: Playwright MCP
pages-created: source-garry-tan-loc-controversy.md
pages-updated: garry-tan.md (3rd article in series + complete series timeline), gstack.md (Apr 18 production snapshot — 75K stars, 14,965 installs, 305K invocations)

## [2026-05-12] ingest | Garry Tan — Naked Models Are Stupider (part 4 backfill)
source: raw/2026-04-19-garry-tan-naked-models-are-stupider.md
fetch-method: Playwright MCP
pages-created: source-garry-tan-naked-models-stupider.md
pages-updated: garry-tan.md (4th article), thin-harness-fat-skills.md (engine-vs-car metaphor; Kingsbury failure-case remedy table; aspirin/anesthesia analogy)

## [2026-05-12] ingest | Garry Tan — The Skillify Manifesto (part 5 backfill)
source: raw/2026-04-21-garry-tan-skillify-manifesto.md
fetch-method: Playwright MCP
pages-created: source-garry-tan-skillify-manifesto.md
pages-updated: skillify-meta-skill.md (MAJOR — full 10-step checklist, calendar-recall + context-now case studies, skillify-as-verb workflow, Hermes Agent comparison, recursive insight), trigger-evals.md (50+ test-case examples, "fucking shit" heuristic, test-process-not-output pattern), check-resolvable.md (3 specific gbrain doctor checks, DRY audit lane-matrix), latent-vs-deterministic.md (concrete case studies, recursive loop), garry-tan.md (5th article), index.md

## [2026-05-13] ingest | Claude Code — `/goal` + Code Review (official docs)
source: raw/2026-05-13-claude-code-goal-and-code-review.md
fetch-method: WebFetch (code.claude.com/docs/en/goal + /code-review) + WebSearch cross-ref to claude.com/blog + InfoQ
pages-created: claude-code-goal.md (concept — session-scoped autonomous turn-loop with Haiku evaluator), claude-code-review.md (concept — managed multi-agent PR review, $15–25/PR, REVIEW.md customization), source-claude-code-goal-and-review-docs.md (source summary)
pages-updated: index.md (registered three new entries under Concepts + Sources)

## [2026-05-13] correction | Replaced Code Review with Agent View (initial ingest misidentified the feature)
note: prior entry "ingest | Claude Code — `/goal` + Code Review" was based on a wrong identification of the second feature. Correct feature is **Agent View** (https://claude.com/blog/agent-view-in-claude-code, official docs https://code.claude.com/docs/en/agent-view). Code Review docs are a separate managed GitHub service and not the announced "agent view" feature.
pages-deleted: claude-code-review.md, source-claude-code-goal-and-review-docs.md
raw-renamed: raw/2026-05-13-claude-code-goal-and-code-review.md → raw/2026-05-13-claude-code-goal-and-agent-view.md (content rewritten for agent view)
pages-created: claude-code-agent-view.md (research-preview TUI, supervisor process, peek/attach/dispatch, worktree isolation, shell commands), source-claude-code-goal-and-agent-view-docs.md (updated source summary)
pages-updated: claude-code-goal.md (source reference + connection to agent view), index.md (swapped code-review entry for agent-view; swapped source-summary entry)

## [2026-05-14] lint
pages-scanned: 132
issues: orphans(0), stale(37, mostly stable foundational pages, no action), contradictions(0), index-drift(0), unresolved-links(6 real + ~11 false-positives), thin(43, mostly OK)
auto-fixed:
  - A: case-mismatch wikilinks ([[Anthropic]]→[[anthropic|Anthropic]], [[Claude Code]]→[[claude-code|Claude Code]], [[OpenClaw]]→[[openclaw|OpenClaw]], [[Prithvi Rajasekaran]]→[[prithvi-rajasekaran|Prithvi Rajasekaran]]) across 14 wiki pages (skipped log.md as append-only)
  - B: frontmatter `last-updated:` drift on 15 pages (check-resolvable, claude-code, claude-opus-4-7, context-anxiety, diarization, gbrain, gstack, harness-design, latent-vs-deterministic, multi-agent-architecture, resolvers, ryan-sarver, thin-harness-fat-skills, trigger-evals, verification-loops)
  - C: index summary refresh — gstack 72K→87K stars, garry-tan 2-piece→6-piece series, gbrain production-scale update
  - D: created 2 new concept pages from dangling wikilinks (cross-modal-review, sprint-contracts); cleaned 3 old danglings to redirect/plain-text (state-management → forked-agent-pattern+session-memory; subagent-orchestration → multi-agent-architecture; source-fetch-fallback-chain → silent-fallback-antipattern reference)
  - E: fixed `[[1️⃣]]`/`[[3️⃣]]` accidental wikilinks → plain emoji in skillify-meta-skill; `[[index.md]]` → `index.md` (code) in source-claude-code-goal-and-agent-view-docs
pages-created: cross-modal-review.md, sprint-contracts.md
pages-updated: 18 (case fixes + frontmatter + index + dangling cleanups)

## [2026-05-14] query | Agent view原理是什么，就是在每个任务都作为一个background跑吗
pages-consulted: claude-code-agent-view.md
answer-filed: chat only

## [2026-05-14] query | how many claude code related docs we have ingest
pages-consulted: index.md (Sources section), raw/ directory listing
answer-filed: chat only
notes: 45 curated externals total; 16 direct CC, 14 ecosystem (Ralph/Skills/GBrain), 15 adjacent. Plus 468 Pipeline B session captures.

## [2026-05-15] ingest | Chris Hayduk — Using Codex Goals Effectively
source: raw/2026-05-11-chrishayduk-using-codex-goals-effectively.md
fetch-method: Playwright MCP (x.com long-form article)
pages-created: chris-hayduk.md (first OpenAI-insider entity in wiki), agentic-loop-tracking-files.md (PLAN.md + EXPERIMENTS.md + SCRATCHPAD.md pattern for long-running /goal loops), source-chrishayduk-codex-goals-effectively.md
pages-updated: claude-code-goal.md (cross-vendor convergence with Codex /goal + Chris's 3 tips), sprint-contracts.md (200-checklist trick as canonical qualitative→quantitative example), verification-loops.md (feedback-loop-tightness-as-leverage; days→minutes scoring reduction), index.md

## [2026-05-16] ingest | Anthropic — Best Practices for Computer and Browser Use with Claude
source: raw/2026-05-13-anthropic-computer-and-browser-use-best-practices.md
fetch-method: WebFetch (claude.com static blog)
pages-created: computer-and-browser-use.md (the production playbook), demonstration-based-teaching.md (record-once-adapt-forever pattern), source-anthropic-computer-browser-use-best-practices.md
pages-updated: claude-opus-4-7.md (high-res vision as computer-use enabler; click precision = Sonnet 4.6), anthropic.md (computer-use as product surface), prompt-cache-optimization.md (batch-prune screenshots pattern), index.md

## [2026-05-16] ingest | Tw93 — 你不知道的 Agent：原理、架构与工程实践
source: raw/2026-03-19-tw93-agent-architecture-and-engineering.md
fetch-method: Playwright MCP (x.com long-form article)
pages-created: agent-vs-workflow.md (Anthropic taxonomy + 5 canonical patterns), agent-evaluation-traps.md (Pass@k vs Pass^k; eval-system-as-bug), source-tw93-agent-architecture-engineering.md
pages-updated: tw93.md (added 2nd major article), openclaw.md (5-layer architecture deep-dive, MessageBus, three trigger modes, source-sink prompt injection), harness-design.md (Harness > Model framing + OpenAI Agent-First case), prompt-cache-optimization.md (stable-large > dynamic-small system prompt counter-intuition), agent-skills-standard.md (Use-when/Don't-use-when + anti-examples 73→53→85% data), multi-agent-architecture.md (protocol-before-collaboration, JSONL inbox + worktree + task graph, error amplification), verification-loops.md (eval system itself as bug, transcript vs outcome), ralph-wiggum.md (Initializer + Coding Agent structured variant), index.md

## [2026-05-16] ingest | Steph Zhang (a16z) — From System of Record to System of Intelligence
source: raw/2026-05-14-stephzhang-system-of-record-to-system-of-intelligence.md
fetch-method: Playwright MCP
pages-created: system-of-intelligence.md (the thesis), steph-zhang.md (first a16z entity), source-stephzhang-system-of-intelligence.md
pages-updated: filing-cabinet-vs-nervous-system.md (cross-linked enterprise version), index.md

## [2026-05-16] ingest | Dan Koe — How to think like a strategic genius (5D thinking)
source: raw/2026-01-27-dankoe-how-to-think-like-strategic-genius.md
fetch-method: Playwright MCP
pages-created: five-levels-of-thinking.md (Ken Wilber's Integral framework + Dan Koe packaging), dan-koe.md (first content-creator entity), source-dankoe-strategic-genius-thinking.md
pages-updated: index.md

## [2026-05-16] ingest | Khairallah — How to Use Claude Skills to Automate Any Workflow
source: raw/2026-05-11-khairallah-how-to-use-claude-skills.md
fetch-method: Playwright MCP
pages-created: source-khairallah-claude-skills-automate-workflow.md
pages-updated: eng-khairallah.md (2nd article), agent-skills-standard.md (4-phase build playbook), skillify-meta-skill.md (10-skills-is-a-workforce + 6.5-week math), index.md

## [2026-05-16] ingest | Khairallah — How to Master Context Engineering
source: raw/2026-05-10-khairallah-how-to-master-context-engineering.md
fetch-method: Playwright MCP
pages-created: four-files-context-architecture.md (Identity / Audience / Standards / Project), source-khairallah-context-engineering.md
pages-updated: eng-khairallah.md (3rd article), context-management.md (Khairallah's three-layer model + Four-Files), index.md

## [2026-05-16] ingest | OpenAI Codex Cookbook Trilogy (3 articles, batch)
sources:
  - raw/2026-05-09-openai-cookbook-using-goals-in-codex.md (Raj Pathak + Stefano Fabbri)
  - raw/2026-05-11-openai-cookbook-build-iterative-repair-loops.md (Shreekant Agrawal)
  - raw/2026-05-12-openai-cookbook-agent-improvement-loop.md (Wesley Pasfield)
fetch-method: WebFetch (all three are static cookbook pages)
pages-created: iterative-repair-loop.md (Review→Repair→Validate three-phase pattern), agent-improvement-flywheel.md (6-step trace-to-harness-change loop), source-openai-codex-cookbook-trilogy.md (combined source summary for all three)
pages-updated: chris-hayduk.md (cross-referenced as the practitioner-heuristics version of these official-formalism docs), claude-code-goal.md (6-element strong-Goal formalism), verification-loops.md (iterative-repair + improvement-flywheel as siblings), index.md
