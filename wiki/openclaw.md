---
type: entity
created: 2026-04-07
last-updated: 2026-05-16
sources:
  - raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-03-19-tw93-agent-architecture-and-engineering.md
tags: [wiki, product, platform, ai-assistant, harness]
---

# OpenClaw

## Summary
Platform for building AI assistants that unlocked capabilities previously impossible with raw AI APIs. Used by [[ryan-sarver|Ryan Sarver]] to build "Stella," a chief-of-staff-level AI assistant managing fundraising, meeting prep, task management, and relationship tracking. Also used by [[garry-tan|Garry Tan]] (YC CEO), who has codified usage rules from his instance into widely-shared discipline. In Garry's 2026-04-15 piece, referred to interchangeably as **"OpenClaw or Hermes Agent"** — the **thin-harness conductor** layer that executes [[gstack]] skills against [[gbrain]] knowledge.

## Details
- Mentioned as the enabling platform — Sarver had previously tried building an AI EA as a product with early AI APIs and failed. OpenClaw made it viable.
- Has an active builder community — Sarver's [[kaizen-loop]] includes weekly scanning of OpenClaw community for new patterns
- @ryancarson also built an assistant on OpenClaw and posted about it (referenced by Sarver)
- Enables integration with external tools: Granola API (meeting notes), Todoist (tasks), WhatsApp (notifications), Gmail (email triage)
- Supports cron jobs for automated routines (Sarver's Friday research scan)
- **[[garry-tan|Garry Tan]] is a public OpenClaw practitioner** publishing patterns from his instance.

### "If I ask twice, you failed" — Garry's OpenClaw rule
Originally a tweet that drew ~1,000 likes and 2,500 bookmarks, then expanded into the [[thin-harness-fat-skills]] article. The instruction Garry gives his OpenClaw:

> You are not allowed to do one-off work. If I ask you to do something and it's the kind of thing that will need to happen again, you must: do it manually the first time on 3 to 10 items. Show me the output. If I approve, codify it into a skill file. If it should run automatically, put it on a cron. **The test: if I have to ask you for something twice, you failed.**

Why it's not a prompt trick but an architectural discipline: every codified skill becomes a permanent upgrade — doesn't degrade, doesn't forget, runs at 3 AM, automatically benefits from the next model release. See [[thin-harness-fat-skills]] and [[skill-as-method-call]] for the full pattern.

### Garry's three-layer open-source stack (2026-04-15)
Garry's followup reveals the full architecture around OpenClaw:

| Layer | Project | Role |
|-------|---------|------|
| Harness | **OpenClaw / Hermes Agent** | Thin CLI loop; runs sessions; executes crons |
| Skills | [[gstack]] (72K+ ★) | Fat markdown skills |
| Knowledge | [[gbrain]] | Resolver + filing rules + compiled memory |

The governance layer that prevents OpenClaw-at-scale from becoming a junk drawer is also his contribution: [[resolvers]], [[trigger-evals]], [[check-resolvable]], and the defense against [[context-rot]]. Production scale: 200 inputs/day, 25K files.

### OpenClaw's 5-layer architecture (per [[tw93|Tw93]]'s 2026-03-19 deep-dive)

Tw93's "你不知道的 Agent" walks through the OpenClaw stack as the worked example for the article's principles:

| Layer | Component | Role |
|-------|-----------|------|
| 1 | **Gateway** | WebSocket service that routes all incoming messages — Channel and Agent never talk directly |
| 2 | **Channel adapters** | 23+ channel integrations behind a uniform interface — adding a new channel doesn't touch Agent code |
| 3 | **Pi Agent** | Maintains the main loop, session state, scheduling — the agentic core. Completely decoupled from Channel layer |
| 4 | **Tool set** | shell / fs / web / browser / MCP — designed by ACI (Agent-Computer Interface) principle |
| 5 | **Context + memory** | Skills lazy-load + MEMORY.md. **50% token threshold triggers automatic consolidation** |

### Critical engineering decisions Tw93 highlights

- **MessageBus between Channel and Agent.** Once cron + heartbeat exist (i.e., the system has non-user message sources), this decoupling is mandatory. Channel only sends/receives; AgentLoop only processes.
- **`dispatch` is non-`await`** — different sessions process concurrently and don't block each other.
- **But same-session messages must serialize** — otherwise concurrent history-write + compact triggers race conditions. Production needs a per-`sessionKey` queue or mutex.
- **Session managed by AgentLoop, not by Channel.** Swap Discord for Lark for WhatsApp — Agent core code doesn't change.
- **Three trigger modes** with different system prompts loaded: regular session (full prompt) · sub-agent (Tooling/Workspace/Runtime only — no Skills / no Memory, for permission isolation) · heartbeat (just `HEARTBEAT.md`, polls for pending tasks every ~5 min)
- **Crash recovery is mandatory for >30-minute tasks** — task progress writes to disk; restart resumes from breakpoint (not from scratch)

### Sub-agent safety limits (Tw93's two rules)
- **Depth limit** — prevents infinite recursion of grand-sub-agents
- **Minimum system prompt** — sub-agents get only Tooling / Workspace / Runtime sections; **no Skills and no Memory directives** (avoids permission leakage and preserves isolation boundary)

### Prompt injection defense — source-sink model (Tw93)
> "Input filtering alone won't catch it. **The point isn't to identify all attacks — it's to make sure that even if the Agent is injected, it can't actually execute any dangerous action.**"

Four operational rules:
- **Don't give Agent tools it doesn't need** — no sink → injection can't land
- **Write operations require explicit user confirmation** — never silent
- **Mark external content with source attribution** — declare which content is untrusted
- **Critical operations get independent LLM review** — same-context Agent can't reliably self-detect injection

## Connections
- Related: [[ryan-sarver]], [[garry-tan]], [[tw93]], [[gbrain]], [[gstack]], [[kaizen-loop]], [[thin-harness-fat-skills]], [[skill-as-method-call]], [[resolvers]], [[check-resolvable]], [[trigger-evals]], [[context-rot]], [[llm-judgment-vs-scripts]], [[agent-vs-workflow]], [[agent-evaluation-traps]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md | Initial creation |
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Added Garry Tan as practitioner; "if I ask twice you failed" rule |
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Added "OpenClaw or Hermes Agent" alt naming; GBrain + GStack relationship; governance layer (resolvers, trigger evals, check-resolvable, context rot); 200 inputs/day + 25K files scale |
| 2026-05-16 | raw/2026-03-19-tw93-agent-architecture-and-engineering.md | Added Tw93's 5-layer architecture deep-dive (Gateway/Channel/Pi-Agent/Tools/Context+Memory); MessageBus + per-sessionKey serialization; three trigger modes (regular/sub-agent/heartbeat); sub-agent safety limits (depth, minimum system prompt); source-sink prompt-injection defense model |
