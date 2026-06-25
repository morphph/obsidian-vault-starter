---
type: concept
created: 2026-06-25
last-updated: 2026-06-25
sources:
  - raw/2026-06-21-feitong-yang-ten-commandments-product.md
tags: [product, ai-agent, zero-to-one, research]
---

# Capability vs Product

## Summary
A capability is an input; a product is the translation of that input into a met need. The translation — figuring out whose problem this solves and how anyone would actually use it — is the entire job, not a footnote to the breakthrough. Especially dangerous in the AI era where model capability jumps create the illusion that breakthrough → product is automatic.

## Details

**The trap:**
> "The researcher is wired to push the frontier, and demonstrating something that was impossible yesterday is thrilling on its own terms. The engineer who meets a new capability falls into the oldest trap there is, the belief that a good hammer entitles you to beat every nail."

**Why ChatGPT looks like a counterexample but isn't:**
- GPT model existed before ChatGPT product did
- Even the product's early retention was "atrocious" (Sam Altman)
- The plain chat box wrapper was a product decision, not the research result
- OpenAI shipped GPT-3 API in 2020 (2+ years before ChatGPT) and *learned its way* toward a product from developer usage

**Three distinct jobs — not one:**
1. **Research:** Push capability frontier
2. **Translation:** Figure out whose problem this solves + how they'd use it
3. **Product:** Wrap the translation in a form users understand

ChatGPT created the myth that these three collapse into one. They don't. Cursor and Claude Code each required dedicated product effort on top of capability, not a research result "left to speak for itself."

**[[feitong-yang]]'s team's mistake (Minecraft):**
- Agent could build a diamond pickaxe; multi-agent team could build 300+ items together
- Viral on X and HN
- "Never clear the attention reflected a need anyone actually had"

**The honest test:** Are you building a product (met need), or answering a research question (capability frontier)? The two require different resources, different timelines, and different success metrics. Trying to do both at once produces neither.

**Exception:** Research genuinely needs research infrastructure — but don't couple it with product infrastructure too early; they serve different goals and tangling them corrupts both.

## Connections
- Related: [[product-reality-evasion]], [[feitong-yang]]
- Parallels [[latent-vs-deterministic]] — both are "what's the right tool for this problem" taxonomies
- [[claude-code]] and [[openclaw]] cited as examples where real product work produced real fuel
- [[agent-vs-workflow]] — similar "name the thing you're actually doing" discipline

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-06-25 | raw/2026-06-21-feitong-yang-ten-commandments-product.md | Created from Ten Commandments essay |
