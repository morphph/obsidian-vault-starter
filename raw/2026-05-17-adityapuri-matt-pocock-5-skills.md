# Matt Pocock's 5 Claude Code Skills Made Me Rewrite How I Work With AI Agents

**Source:** https://adityakumarpuri.medium.com/matt-pococks-5-claude-code-skills-made-me-rewrite-how-i-work-with-ai-agents-d71853c3056c
**Author:** Aditya Kumar Puri (Medium)
**Fetch method:** WebFetch
**Fetched:** 2026-05-17

## Author's Problem

Oscillated between two extremes:
- Delegating everything → unreviewed complexity
- Delegating nothing → burnout

Breakthrough: treat AI agents as junior engineers with constraints, not smart autocomplete.

## The Five Skills in Sequence

### 1. /grill-me
Three-sentence skill automating thorough planning. "Relentless interviews" about design decisions. Draws from Frederick P. Brooks' _The Design of Design_ — walks user through decision trees systematically.

Author's first session: 38 clarifying questions before implementation began — revealing crucial design considerations not initially considered.

### 2. /grill-with-docs
Enhanced variant maintaining CONTEXT.md glossary. Solves terminology consistency by:
- Challenging ambiguous language ("account" → "customer or user?")
- Cross-referencing code against claims
- Updating terminology inline as discussions crystallize

Example impact: replacing verbose explanations with domain-specific terms like "materialization cascade."

### 3. /to-prd
Transforms planning conversations into formal PRDs. Generates user stories emphasizing behavior ("as a mobile customer, I want..."). Identifies **deep modules** — components with simple interfaces hiding complex implementations — based on John Ousterhout's architectural principles.

### 4. /to-issues
Breaks requirements into **independently shippable vertical slices** (schema + API + UI + tests), not horizontal layers.

**Critical classification:** each issue receives HITL (requires human decisions) or AFK (agent-executable) label. Enables autonomous Ralph loops where agents pull AFK work, implement, and merge without supervision.

### 5. /improve-codebase-architecture
Applies the **deletion test** — what complexity vanishes if this module is removed? Deepens shallow modules. Prevents garbage codebases from degrading agent output quality.

## Key Workflow Transformation

- **Before:** Half-finished PRs with architectural debt accumulating invisibly
- **After:** Reinforcing loop where architecture improves quarterly, enabling progressively higher-quality agent work

## /tdd Example

Vertical slice testing:
- **Honest tests** exercise observable behavior through public interfaces
- **Deceptive tests** mock internals or query databases, breaking during refactors despite unchanged behavior

## Integration Model

Closed loop:
```
planning → specification → vertical slicing →
test-driven implementation → architectural cleanup →
feedback into next planning cycle
```

Critical element: stage 5's closing edge. Skipping architecture work transforms pipeline into deteriorating output quality.

## Connections to Wiki

- HITL/AFK classification on issues is the **missing piece** for our [[ralph-wiggum]] cluster — it's how you decide what to put in the loop
- Deep modules = direct application of [[thin-harness-fat-skills]] philosophy
- The closed loop with feedback resembles [[agent-improvement-flywheel]] but for codebase architecture rather than agent harness
- Vertical slicing as a unit-of-work pattern is new and valuable
