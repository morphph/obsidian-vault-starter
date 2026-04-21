---
type: concept
created: 2026-04-19
last-updated: 2026-04-19
sources:
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-04-21-anthropic-agent-skills-docs.md
tags: [wiki, principle, agentic, failure-mode, governance]
---

# Context Rot

## Summary
[[garry-tan|Garry Tan]]'s name for the slow, silent decay of a [[resolvers|resolver]] over time. Day 1 every skill is registered, every trigger accurate. Day 90 the resolver is a **historical document** — an artifact of what the system *used to* be able to do. New skills get built by sub-agents, trigger descriptions stop matching how users phrase things, capabilities go dark. The system still works — but only because the builder knows which skill to call. That's not a system, that's "a person with a filing cabinet."

## Details

### The 90-day decay curve (Garry's observation)
| Day | State |
|-----|-------|
| 1 | Routing table perfect. Every skill registered. Every trigger accurate. You feel like a genius. |
| 30 | Three new skills exist that nobody added to the resolver — built by sub-agents running at 3 AM. |
| 60 | Two trigger descriptions don't match how users actually phrase things. Skill handles "track this flight" but users say "is my flight delayed?" |
| 90 | Resolver is a historical document. Skills now get invoked by direct instruction (`read skills/flight-tracker/SKILL.md`) because the resolver doesn't have the right triggers. |

### The tell-tale symptom
> Skills were being invoked by direct instruction — "read skills/flight-tracker/SKILL.md" — instead of through the resolver, because the resolver didn't have the right triggers. The system worked because I knew which skill to call. That's not a system. That's a person with a filing cabinet.

When the builder is the routing layer, the resolver has rotted.

### Why it happens (not user error)
- Sub-agents create new skills in response to real needs
- Users' phrasings drift from the descriptions written at skill-creation time
- No one owns maintenance of the resolver table
- Manual audits don't scale past ~10 skills; Garry's system had 40+

### The defenses (in increasing order of sophistication)
1. **Mandate that every new skill register in the resolver** (process discipline — breaks down at scale)
2. **[[trigger-evals]]** — test that correct skills fire for sample inputs (catches drift in descriptions)
3. **[[check-resolvable]]** — weekly reachability audit (catches new unregistered skills)
4. **Self-healing resolver (RLM loop, forward-looking)** — system observes every task dispatch, nightly rewrites the resolver from traffic evidence

### The RLM idea (origin: a YC CTO in office hours)
> Could an RLM be used to solve context rot particularly around resolvers?

A reinforcement-style loop where the system observes every task dispatch — which skill fired, which didn't, which tasks matched the wrong skill, which had no match — and periodically rewrites the resolver based on observed evidence.

> Eight hundred task dispatches over a month. The system sees that "is my flight on time" never triggers flight-tracker but "check my flight" does. It rewrites the trigger description.

Not a human maintaining a table. **The table maintaining itself.**

### Claude Code AutoDream as a primitive version
[[claude-code]]'s [[dreaming|AutoDream]] system — memory consolidation during idle time — is already a primitive version of this. It reviews accumulated context and compresses it. Apply the same principle to the resolver specifically and you get a routing table that improves with use.

### Generalizes beyond resolvers
Context rot is the agentic-system equivalent of documentation drift, config drift, and dead-code accumulation. Any document that sits between **intent** and **execution** and is updated asymmetrically (easy to add paths, hard to audit) will rot. The pattern:
- Low write cost + no reachability signal → additions exceed corrections → drift
- Cure: make the reachability signal automatic (trigger evals + check-resolvable)

### The mechanism, quantified (2026-04-21 Anthropic Skills docs)
Context rot isn't just a metaphor — it has a **specific mechanical cause** in Claude Code:

> "All skill names are always included, but if you have many skills, **descriptions are shortened to fit the character budget, which can strip the keywords Claude needs to match your request.** The budget scales dynamically at 1% of the context window, with a fallback of 8,000 characters."

Thresholds:
- **1,536 chars per skill** (combined `description` + `when_to_use`)
- **1% of context window** total listing budget
- Escape hatch: `SLASH_COMMAND_TOOL_CHAR_BUDGET`

**Concrete failure mode:** you add the 30th skill. Its description is 2,000 chars (over cap). Claude Code truncates to 1,536 chars, **slicing off your `when_to_use` trigger phrases**. User asks a question that would have matched those phrases. No skill fires. You think the skill doesn't work. It works — Claude just can't see the trigger anymore.

Garry's 90-day decay curve is the same phenomenon across multiple skills simultaneously: additions + silent truncation + user-phrasing drift = the routing table becomes invisible.

## Connections
- Related: [[resolvers]], [[trigger-evals]], [[check-resolvable]], [[garry-tan]], [[thin-harness-fat-skills]], [[context-management]], [[context-noise-governance]], [[assumptions-expire]], [[dreaming]], [[silent-fallback-antipattern]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Initial creation |
