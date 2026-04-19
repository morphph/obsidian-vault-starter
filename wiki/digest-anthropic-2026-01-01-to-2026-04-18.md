---
type: synthesis
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-anthropic-daily-backfill-2026-q1-q2.md
  - raw/2026-04-18-claude-daily-source-verification.md
tags: [wiki, digest, anthropic, claude, backfill]
---

# Anthropic + Claude Digest — 2026-01-01 → 2026-04-18

## Summary
**~70 unique items** across 5 categories, fetched 2026-04-18, window 2026-01-01..2026-04-18. Dedupe collapsed ~25 cross-source duplicates (e.g., Opus 4.7 launch appeared on news + API release notes + blog + Claude Code changelog → single item).

**Backfill scope (Option B):** Websites + RSS only. X handles will be included in daily mode going forward.

**Known gaps:** claude.com/blog pagination (pages 2-8) not fetched — older Q1 blog posts may be missing. Claude Code CHANGELOG has no explicit per-version dates; ~45 versions in window with dates correlated only for v2.1.105-v2.1.114 via Atom feed.

---

## 🤖 Models (released or deprecated in window)

- **Opus 4.7 launched (2026-04-16)** — Most capable GA model, step-change in agentic coding, $5/$25 per MTok (same as 4.6), 1M context, new tokenizer, no extended thinking but supports adaptive thinking. API breaking changes vs 4.6. → [[claude-opus-4-7]]
  - Sources: anthropic.com/news/claude-opus-4-7, platform.claude.com/docs/.../release-notes (also: claude.com/blog best-practices post, Claude Code v2.1.111)
- **Sonnet 4.6 launched (2026-02-17)** — Balanced speed+intelligence, 1M context beta, supports extended thinking. Code execution free with web search/fetch. Web search + programmatic tool calling now GA.
- **Opus 4.6 launched (2026-02-05)** — Most intelligent for long-horizon work, recommends adaptive thinking, no prefilling. Compaction API beta, data residency controls, 1M context beta.
- **Fast mode (research preview) for Opus 4.6 (2026-02-07)** — Up to 2.5x faster output at premium pricing.
- **1M context GA (2026-03-13)** — Opus 4.6 + Sonnet 4.6 at standard pricing, no beta header. Image/PDF limit raised 100→600.
- **Output 300k beta (2026-03-30)** — Message Batches API for Opus 4.6/Sonnet 4.6.
- **Deprecations:** Sonnet 4 + Opus 4 deprecated (2026-04-14, retire 2026-06-15). Sonnet 3.7 + Haiku 3.5 retired (2026-02-19). Haiku 3 deprecated (retire 2026-04-19). Opus 3 retired (2026-01-05). Opus 4 + Opus 4.1 deprecated in Claude product (2026-01-16).
- **Mythos Preview (2026-04-07)** — Invitation-only research preview for defensive cybersecurity (Project Glasswing).

## 🏢 Anthropic (company-level)

- **Claude Design by Anthropic Labs (2026-04-17)** — New Labs product for visual designs, prototypes, slides, one-pagers. (Also: support release-notes 2026-04-17)
- **Vas Narasimhan joins LTBT board (2026-04-14)** — Long-Term Benefit Trust governance update.
- **Google + Broadcom partnership expansion (2026-04-06)** — Multi-gigawatt next-gen compute infrastructure.
- **Australian Government MOU (2026-03-31)** — AI safety research collaboration.
- **$100M Claude Partner Network investment (2026-03-12)** — Major ecosystem expansion.
- **The Anthropic Institute launched (2026-03-11)** — New research and educational institution.
- **Sydney office opened (2026-03-10)** — Fourth Asia-Pacific location.
- **Mozilla/Firefox security partnership (2026-03-06)** — Browser security collaboration.
- **Department of War update (2026-03-05)** — Policy/organizational interactions.
- **Claude brand consolidation milestone (2026-01-12)** — `console.anthropic.com` redirects to `platform.claude.com`.

### Engineering blog (6 posts)

- **Auto mode safer permission skipping (2026-03-25)** — Eliminates permission prompts safely.
- **Harness design for long-running apps (2026-03-24)** — GAN-style multi-agent architecture patterns (foundational, already in [[harness-design]]).
- **Eval awareness in Opus 4.6 BrowseComp (2026-03-06)** — Model behavior shifts under evaluation contexts.
- **C compiler with parallel Claudes (2026-02-05)** — Multi-agent collaborative development demo.
- **AI-resistant technical evaluations (2026-01-21)** — Methods for un-gameable assessments.
- **Demystifying evals for AI agents (2026-01-09)** — Foundational benchmarking guide.

## 📱 Claude (consumer product)

- **Cowork journey (Jan→Apr)** — Research preview macOS desktop (Jan 12) → Pro plan access (Jan 16) → plugin marketplace + admin controls (Feb 24) → scheduled tasks (Feb 25) → persistent agent thread on iOS/Android pairing (Mar 17) → **General Availability macOS+Windows + Analytics API + OpenTelemetry (2026-04-09)** → Carta Healthcare case study (Apr 8) → enterprise-ready blog post (Apr 9). Cowork has its own section below.
- **Health & Fitness data on mobile (2026-01-12)** — iOS/Android, Pro/Max US users.
- **HIPAA-ready Enterprise plans (2026-01-12)** — Process PHI through compliant Claude.
- **Claude Code added to Team standard seats (2026-01-16)** — Every Team seat now includes Claude Code.
- **Claude for PowerPoint add-in (2026-02-05)** — Presentation creation/editing.
- **Claude for Excel enhancements (2026-02-05)** — Pivot tables, conditional formatting, native Excel ops.
- **Self-serve Enterprise plans (2026-02-12)** — Direct purchase without sales involvement.
- **Enterprise Analytics API (2026-02-13)** — Programmatic usage/engagement data.
- **Memory for free users (2026-03-02)** — Chat memory available to all tiers.
- **Excel/PowerPoint integration improved (2026-03-11)** — Conversation context sharing, LLM gateway.
- **Custom charts & visualizations (2026-03-12)** — Interactive diagrams inline.
- **Computer Use research preview (2026-03-23)** — Pro/Max access to control computer functionality.
- **Interactive apps on mobile (2026-03-25)** — iOS/Android with live charts and shareable assets.
- **Role-Based Access Controls (2026-04-09)** — Enterprise admin user groups with custom permissions.
- **Claude Design (2026-04-17)** — See Anthropic section above.

## 🔌 Claude API (developer)

- **Major model launches** — see Models section above (Opus 4.6 Feb 5, Sonnet 4.6 Feb 17, Opus 4.7 Apr 16).
- **Claude Managed Agents beta (2026-04-08)** — Fully managed agent harness with sandboxing, built-in tools, SSE streaming. Beta header `managed-agents-2026-04-01`. Already documented in [[claude-managed-agents]]. (Also: claude.com/blog managed-agents post 2026-04-08)
- **`ant` CLI (2026-04-08)** — Command-line client, native Claude Code integration, YAML versioning.
- **Advisor tool beta (2026-04-09)** — Pair fast executor with high-intelligence advisor model for long-horizon agentic workloads. Beta header `advisor-tool-2026-03-01`. (Also: claude.com/blog advisor strategy post 2026-04-09)
- **Bedrock Messages API research preview (2026-04-07) → GA (2026-04-16)** — `/anthropic/v1/messages` endpoint, 27 regions, zero operator access.
- **Compliance API (2026-03-30)** — Audit Claude Platform activity. (Source: blog post)
- **Automatic prompt caching (2026-02-19)** — Single `cache_control` field, system manages breakpoints automatically.
- **Compaction API beta (2026-02-05)** — Server-side context summarization for infinite conversations (Opus 4.6).
- **Effort parameter GA (2026-02-05)** — Replaces `budget_tokens` for thinking depth. (Was beta since Nov 2025)
- **Structured outputs GA (2026-01-29)** — Sonnet 4.5, Opus 4.5, Haiku 4.5. `output_format` moved to `output_config.format`.
- **Models API capability fields (2026-03-18)** — `max_input_tokens`, `max_tokens`, `capabilities` object.
- **Thinking display field (2026-03-16)** — `thinking.display: "omitted"` for faster streaming with `signature` preserved.
- **Data residency controls (2026-02-05)** — `inference_geo` parameter, US-only at 1.1x pricing.
- **Fine-grained tool streaming GA (2026-02-05)** — All models, no beta header.
- **Tool GA wave (2026-02-17)** — Web search, programmatic tool calling, code execution, web fetch, tool search, memory tool, tool use examples — all GA.
- **Web search + fetch dynamic filtering (2026-02-17)** — Code execution filters results before context.

## 💻 Claude Code

### Major themes (Feb→Apr)

- **Opus 4.7 support + agentic primitives (v2.1.111-v2.1.114, 2026-04-16→04-18)** — `xhigh` effort level (between high and max), `/effort` interactive slider, **`/ultrareview`** command for cloud code review (3 free/mo for Pro/Max), Auto mode for Max+Opus 4.7, `--enable-auto-mode` no longer required. Already documented in [[claude-opus-4-7]], [[xhigh-effort-level]], [[task-budgets]], [[adaptive-thinking]].
- **Auto mode (2026-03-24, blog + engineering post)** — Safer way to skip permissions, autonomous execution. (Also: anthropic.com/engineering 2026-03-25)
- **Routines (2026-04-14, blog)** — New automatable workflow patterns.
- **Desktop redesign for parallel agents (2026-04-14, blog)** — UI/UX for concurrent agents.
- **Claude Code session management + 1M context (2026-04-15, blog)** — Already in raw, contributed to [[context-management]].
- **Multi-agent coordination patterns (2026-04-10, blog)** — Five approaches for managing multiple agents.
- **Subagents in Claude Code (2026-04-07, blog)** — When and how to use them.
- **Best practices for Opus 4.7 with Claude Code (2026-04-16, blog)** — Already documented in [[claude-opus-4-7]].
- **Seeing like an agent (2026-04-10, blog)** — Tool design philosophy.

### Notable feature additions (CHANGELOG, undated but in window)

- **Monitor tool (v2.1.98)** — Event-driven background monitoring. Already documented in [[claude-code-monitor-tool]].
- **Native sandboxing (v2.1.98)** — Subprocess sandboxing with PID namespace on Linux. Already in [[claude-code-sandboxing]].
- **PreCompact + PostCompact hooks (v2.1.105, v2.1.76)** — New hook events.
- **`/tui` command (v2.1.110)** — Flicker-free fullscreen rendering.
- **Push notification tool (v2.1.110)** — Remote Control notifications.
- **Recap feature (v2.1.108)** — Returning to sessions context.
- **`/proactive` alias for `/loop` (v2.1.105)** — Recurring task command.
- **`/team-onboarding` (v2.1.101)** — Ramp-up guide command.
- **Background monitor support for plugins (v2.1.105)** — Plugin extensibility.
- **Bedrock support via Mantle (v2.1.94)** — AWS deployment path.
- **`/powerup` interactive lessons (v2.1.90)** — Animated demos for learning.
- **`/effort` slash command (v2.1.76)** — Effort control without API params.
- **1M context for Opus 4.6 by default (v2.1.75)** — Large-context default.
- **Voice push-to-talk improvements (multiple versions)** — `/voice` command stability.
- **`--bare` flag (v2.1.81)** — Scripted `-p` calls, ~14% faster.
- **`--channels` permission relay (v2.1.81)** — Research preview.
- **PowerShell tool (v2.1.84)** — Windows preview.
- **MCP elicitation support (v2.1.76)** — `Elicitation` and `ElicitationResult` hooks.

### Security & permission improvements (recurring theme)

Multiple versions hardened sandbox boundaries, fixed permission bypasses (env-var prefixes, backslash-escaped flags, compound bash commands, `find -exec`, `dangerouslyDisableSandbox`, deny rules wrapped in `env`/`sudo`/`watch`). v2.1.78 and v2.1.97 had explicit security fixes.

### Versions in window

v2.1.70 → v2.1.114 (~45 releases). Atom feed dates v2.1.105-v2.1.114 from 2026-04-13 to 2026-04-18.

## 🤝 Claude Cowork

Already covered in Claude (consumer) timeline above. Highlights:

- **Research preview launch (2026-01-12)** — Claude Desktop macOS, "Claude Code's agentic capabilities for knowledge work."
- **Pro plan access (2026-01-16)** — Expanded beyond Max.
- **Plugins & admin controls (2026-02-24)** — Plugin marketplace, org-level management for Team/Enterprise.
- **Scheduled tasks (2026-02-25)** — Recurring + on-demand tasks via Customize section.
- **Persistent agent thread (2026-03-17)** — Mobile-pairing-ready via iOS/Android.
- **General Availability (2026-04-09)** — macOS + Windows, Analytics API, OpenTelemetry, RBAC.
- **Carta Healthcare case study (2026-04-08)** — Domain-specific clinical reasoning.
- **Cowork for enterprise (2026-04-09 blog)** — Enterprise-grade readiness.

Also: support release notes mentions "Persistent agent thread via Claude Desktop or Claude for iOS/Android" for task management.

---

## Wiki entities to update or create

Items in this digest that warrant updating an existing wiki page or creating a new one (deferred — flag for future runs):

**Update existing:**
- [[claude-model-family]] — add Sonnet 4.6, Opus 4.6 entries
- [[anthropic]] — add Sydney office, Anthropic Institute, $100M Partner Network
- [[claude-managed-agents]] — already has Apr 8 launch detail; cross-link `ant` CLI
- [[claude-code]] — note routines, desktop redesign, /ultrareview as new primitives
- [[blog2video]] / [[loreai]] — none directly relevant

**Possibly create:**
- `claude-cowork.md` — entity page (currently no dedicated page, only mentioned)
- `claude-design.md` — new Anthropic Labs product
- `anthropic-institute.md` — new entity
- `claude-managed-agents-ant-cli.md` — `ant` CLI tool
- `advisor-tool.md` — concept (executor + advisor pattern, related to [[harness-design]])
- `claude-mythos-glasswing.md` — defensive cybersecurity preview

These are NOT created in this run — too many to do well in a single sweep. Flag in `wiki/log.md` as backlog.

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-anthropic-daily-backfill-2026-q1-q2.md | Initial backfill digest, 10 sources, ~70 items deduped |
