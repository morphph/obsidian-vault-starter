---
type: entity
created: 2026-04-19
last-updated: 2026-05-11
sources:
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
  - raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md
  - raw/2026-05-09-garry-tan-meta-meta-prompting.md
tags: [wiki, person, vc, ai-builder, open-source]
---

# Garry Tan

## Summary
President & CEO of Y Combinator, 756K X followers, designer-engineer turned investor. Active AI builder publishing architecture frameworks from his hands-on use of [[claude-code]] and [[openclaw]]. **Six-part agent-building series** spanning Apr-May 2026: Thin Harness Fat Skills → Resolvers → The LOC Controversy → Naked Models Are Stupider → Skillify Manifesto → Meta-Meta-Prompting. The first two and the sixth are in our wiki. Open-sourced full personal stack ([[gbrain]] + [[gstack]] + OpenClaw/Hermes harness). **Production scale as of 2026-05-09: 100,000 brain pages, 100+ skills, 100+ daily crons, 87,000+ GitHub stars on GStack.**

## Details
- **Role**: President & CEO @ycombinator. Founder @garryslist. Creator of GStack & GBrain. Self-described "designer/engineer who helps founders." Based in San Francisco.
- **Bio tagline**: "SF Dem accelerating the boom loop" — political identity tied to SF tech revival narrative.
- **Builds on [[openclaw]]**: Runs his own OpenClaw instance (referenced in skill-rule tweets). Joins [[ryan-sarver]] as a public OpenClaw practitioner publishing patterns.
- **YC Startup School example**: His "Thin Harness, Fat Skills" article uses YC's own July 2026 Chase Center event (6,000 founders) as the worked example — /enrich-founder, /match-breakout, /match-lunch, /match-live, /improve skills running on a thin CLI harness over a deterministic foundation (SQL, GitHub, CrustData).
- **Key contributions from "Thin Harness, Fat Skills" (2026-04-11)**:
  - Coined / popularized [[thin-harness-fat-skills]] as the architectural slogan
  - Articulated [[skill-as-method-call]] — skills take parameters (TARGET/QUESTION/DATASET); same procedure, different worlds
  - Distinguished [[latent-vs-deterministic]] as the "most common mistake in agent design"
  - Defined [[resolvers]] — routing tables for context (skill descriptions in [[claude-code]] are the canonical example)
  - Defined [[diarization]] — model reads everything about a subject, writes one-page structured profile; the SAYS-vs-ACTUALLY-BUILDING gap is the canonical output
  - Codified the **"if I have to ask you for something twice, you failed"** rule: 3-10 manual samples → approve → skill file → optional cron
- **Key contributions from "Resolvers" follow-up (2026-04-15)**:
  - Reframed [[resolvers]] as the **governance / management layer** of an agent system (not a technical pattern — an org chart)
  - Invented [[check-resolvable]] — meta-skill that audits reachability across `AGENTS.md → skill → code` (first run: 6/40 = 15% dark capability)
  - Codified [[trigger-evals]] — 50-sample test suite for routing correctness (false negative / false positive)
  - Named [[context-rot]] — 90-day resolver decay curve
  - Articulated "resolvers are fractal" — same routing pattern at skill / filing / context layers
  - Floated the **self-healing resolver** (RLM loop that rewrites routing from traffic evidence; idea came from a YC CTO in office hours); [[dreaming|AutoDream]] in Claude Code as primitive version
  - Open-sourced the full stack: [[gbrain]] (knowledge), [[gstack]] (72K+ stars, skills), [[openclaw|OpenClaw]]/Hermes Agent (harness)
- **Key contributions from "Meta-Meta-Prompting" (2026-05-09)** — the personal/operational piece:
  - Confirmed [[skillify-meta-skill|/skillify]] as a **real production meta-skill** that creates new skills (the operational mechanism for "if I ask twice, you failed")
  - Coined [[book-mirror]] — chapter-by-chapter two-column book→life mapping pattern (he's done 20+ books)
  - Coined [[filing-cabinet-vs-nervous-system|"filing cabinet vs nervous system"]] — the framing that distinguishes active KB from passive storage
  - Attributed GBrain's design to **Karpathy's LLM Wiki gist** as the original inspiration
  - Production scale at this point: **100,000 brain pages, 100+ skills, 100+ daily crons, GStack at 87K stars**
  - Confirmed multi-model orchestration as standard: Opus 4.7 1M (precision), GPT-5.5 (recall), DeepSeek V4-Pro (creative / generic detection), Groq+Llama (speed) — `cross-modal-eval` skill picks per task
  - Thesis statement: *"The future belongs to individuals who build compounding AI systems, not to individuals who use corporate-owned centralized AI tools."*
- **Read the Claude Code source leak**: Confirms 3/31/2026 npm leak (512K lines), credits it as confirming what he'd been teaching at YC.
- **Public influence on AI tooling discourse**: 1.4M views on Thin Harness, 293K on Resolvers, 1.1M on Meta-Meta-Prompting; GStack trajectory 72K (Apr 15) → 78K (Apr 21) → 87K (May 11).

## Connections
- Related: [[thin-harness-fat-skills]], [[skill-as-method-call]], [[diarization]], [[resolvers]], [[trigger-evals]], [[check-resolvable]], [[context-rot]], [[skillify-meta-skill]], [[book-mirror]], [[filing-cabinet-vs-nervous-system]], [[gbrain]], [[gstack]], [[latent-vs-deterministic]], [[openclaw]], [[ryan-sarver]], [[harness-design]], [[claude-code]], [[llm-judgment-vs-scripts]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Initial creation — entity from "Thin Harness, Fat Skills" |
| 2026-04-19 | raw/2026-04-15-garry-tan-resolvers-routing-table-for-intelligence.md | Added "Resolvers" follow-up: governance reframe, check-resolvable, trigger evals, context rot, self-healing RLM; open-source stack (GBrain, GStack, OpenClaw/Hermes); 200 inputs/day and 25K files scale |
| 2026-05-11 | raw/2026-05-09-garry-tan-meta-meta-prompting.md | Added Meta-Meta-Prompting (6th piece): /skillify as production meta-skill, book-mirror pattern, filing-cabinet-vs-nervous-system framing, Karpathy attribution, 100K-page production scale, 87K GStack stars, multi-model cross-modal-eval standard |
