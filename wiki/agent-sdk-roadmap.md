---
type: synthesis
created: 2026-04-07
last-updated: 2026-04-07
sources:
  - raw/2026-04-07-repo-claude-memory-compiler.md
tags: [wiki, synthesis, roadmap, harness-engineering]
---

# Agent SDK Roadmap: Unattended LLM Operations

## Summary
Our wiki system uses Claude Code CLI for interactive operations (/ingest, /query, /lint, /visualize) and plans to use the Claude Agent SDK for all unattended operations — background knowledge capture, auto-compilation, connection discovery, and scheduled intelligence. This article captures the full picture: what we learned, what we decided, and what to build next.

## The Core Insight

From [[claude-memory-compiler]]: **hooks must be fast, LLM work is slow, so they must be separated.** The hook does local I/O in <10 seconds, spawns a detached background Python process, and exits. The background process uses Agent SDK (not CLI) because Claude Code is already closed when it runs.

This generalizes into a design rule: **any LLM task that doesn't need a human in the loop should use Agent SDK.** Claude Code CLI is the interactive tool; Agent SDK is the programmatic interface.

See [[agent-sdk-vs-claude-code]] for the full decision framework.

## Architecture Context

Our wiki has [[two-pipeline-architecture|two pipelines]]:
- **Pipeline A (External Knowledge)**: manual /ingest + Telegram bot via Claude Code Channels → `raw/`
- **Pipeline B (Internal Knowledge)**: Claude Code hooks → flush.py → Agent SDK → `raw/`

Both converge at `raw/`, compiled by the same LLM into `wiki/`. See [[visual-wiki-architecture]] for the full diagram.

## Agent SDK Use Cases: Current → Near-term → Future

### ✅ Decided (design complete, ready to build)

**1. Background Knowledge Flush (Pipeline B core)**
- **What:** SessionEnd + PreCompact hooks capture conversation transcripts. Detached flush.py process uses Agent SDK to extract decisions, lessons, patterns from LoreAI and blog2video coding sessions.
- **Why Agent SDK:** Runs after Claude Code closes. Headless, no user interaction.
- **Pattern from:** [[claude-memory-compiler]]
- **Recursion guard:** `CLAUDE_INVOKED_BY` env var prevents hook → SDK → Claude Code → hook loops
- **Cost:** ~$0.02-0.05 per session flush

**2. Time-Gated Auto-Compilation**
- **What:** After 6 PM, automatically run `/ingest scan` to compile all new `raw/` files accumulated during the day (from all three entry points: manual, Telegram, hooks).
- **Why Agent SDK:** Unattended scheduled task. Piggybacks on the last session flush of the day — no cron needed.
- **Pattern from:** [[time-gated-compilation]] in [[claude-memory-compiler]]
- **Cost:** ~$0.45-0.65 per compilation pass

**3. Auto Connection Discovery**
- **What:** During compilation, Agent SDK reads all existing wiki pages + the new content being compiled. If it discovers a non-obvious relationship between 2+ concepts, it creates a [[connection-articles|connection article]] automatically.
- **Why Agent SDK:** Requires LLM judgment (is this connection non-obvious and valuable?) but no human interaction.
- **Pattern from:** [[claude-memory-compiler]]'s compile.py creates `knowledge/connections/` articles
- **Example:** Our first connection article ([[connection-context-anxiety-and-zero-friction-capture]]) was created manually in this discussion. Future ones should be auto-discovered.

**4. GitHub Repo Deep Scan Extraction**
- **What:** When `/ingest` encounters a GitHub URL, the deep scan fetches README, file tree, deps, key source files. The pattern extraction (Harness Engineering / System Design / DX) could be done by Agent SDK in the background, especially for batch-ingesting multiple repos.
- **Why Agent SDK:** Heavy analysis (~60 seconds per repo). Background processing avoids blocking the CLI session.

### 🔜 Near-term (next to build after Pipeline B works)

**5. Telegram Bot Content Extraction**
- **What:** OpenClaw bot receives forwarded articles/tweets via Telegram. Agent SDK extracts core content, saves structured markdown to `raw/`. Smarter than WebFetch because Agent SDK can use tools (Read, Write, Bash) and reason about relevance.
- **Why Agent SDK:** Bot receives messages asynchronously. No human in the loop at extraction time.
- **Integration:** Claude Code Channels for Telegram

**6. Auto Weekly /lint**
- **What:** Every Sunday, Agent SDK runs all 7 lint checks (or just structural ones for free). Writes report to wiki. Flags issues for human review on Monday morning.
- **Why Agent SDK:** Scheduled, unattended.
- **Cost:** ~$0.15-0.25 (full lint) or $0.00 (structural only)

### 🔮 Future (when wiki grows bigger)

**7. Weekly Knowledge Digest**
- **What:** Every Monday 9 AM, Agent SDK runs: "What new knowledge was ingested this week? What cross-project patterns emerged? Any contradictions with prior knowledge?" Generates a digest → sends to Telegram or email.
- **Why Agent SDK:** Scheduled reporting, no interaction needed.
- **Value:** You see the wiki's growth without opening Obsidian.

**8. RSS Feed Intelligent Filter**
- **What:** Cron script fetches RSS feeds (AI newsletters, HN, etc.). Agent SDK reads each article title + summary, judges relevance to your domain focus (AI/LLM, content distribution, builder tools). Only saves relevant articles to `raw/`.
- **Why Agent SDK:** LLM-based filtering is far better than keyword matching. Runs unattended on schedule.
- **Scaling insight:** At ~2,000+ articles, add [[index-over-rag|hybrid RAG search]] (qmd by Tobi Lutke).

**9. Auto /visualize on Ingest**
- **What:** After each ingest that creates 3+ new pages, Agent SDK automatically generates an updated topic diagram showing how the new knowledge connects to existing wiki. Saves as `visual-*.excalidraw`.
- **Why Agent SDK:** Diagram generation is slow (~30-60s) and doesn't need human guidance.

## Implementation Priority

```
Phase 1: Pipeline B core (hooks + flush.py + time-gated compile)
    ↓
Phase 2: Auto connection discovery (during compile)
    ↓
Phase 3: Telegram bot integration (Claude Code Channels)
    ↓
Phase 4: Scheduled operations (weekly lint, digest, RSS filter)
    ↓
Phase 5: Auto-visualize on ingest
```

Each phase builds on the previous. Phase 1 is the foundation — once hooks + Agent SDK pipeline works, everything else is "just another Agent SDK script."

## Key Design Decisions

1. **One wiki, not two systems.** Internal knowledge (Pipeline B) flows into the same `raw/` → `wiki/` as external knowledge. Enables cross-source queries.
2. **Agent SDK for all unattended work.** CLI stays interactive. Background tasks use SDK. Clean separation.
3. **Time-gated, not real-time.** Accumulate all day, compile once. Cheaper, better quality (LLM sees full day context).
4. **Connection discovery is automatic.** Don't rely on humans to notice cross-concept bridges. LLM does this during compile.

## Connections
- Related: [[agent-sdk-vs-claude-code]], [[two-pipeline-architecture]], [[zero-friction-capture]], [[time-gated-compilation]], [[connection-articles]], [[compiler-analogy]], [[claude-memory-compiler]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | Internal discussion: Agent SDK use cases | Initial creation — full roadmap from multi-round discussion |
