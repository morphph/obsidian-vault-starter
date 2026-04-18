---
type: entity
created: 2026-04-18
last-updated: 2026-04-18
sources:
  - raw/2026-04-18-garrytan-thin-harness-fat-skills.md
tags: [wiki, person, vc, builder]
---

# Garry Tan

## Summary
President & CEO of Y Combinator. Designer/engineer turned VC. Author of "Thin Harness, Fat Skills" (2026-04-11), an architectural treatise on AI agent design that crystallized the post-Claude-Code-leak consensus on how to build with LLMs. 1.3M views, 10.7K bookmarks — became one of the most-shared agentic-AI essays of 2026.

## Details
- **Role**: President & CEO at Y Combinator; founder of @garryslist; creator of GStack & GBrain
- **Position**: Builder-VC who teaches founders the architectural patterns he sees succeed at YC
- **Bio self-description**: "designer/engineer who helps founders—SF Dem accelerating the boom loop"
- **Key contribution to the field**: Coined and codified [[thin-harness-fat-skills]] — a 5-definition framework (skill files, harness, resolvers, latent-vs-deterministic, diarization) that explains why the same Claude model produces 100x productivity gaps between users
- **Trigger event**: Read the entire Claude Code source code after Anthropic's accidental npm publish on 2026-03-31 (512K lines). Says it "confirmed everything I'd been teaching at YC."
- **Operating principle he gives his agents** (viral tweet, 1K+ likes, 2.5K bookmarks):
  > "You are not allowed to do one-off work. If I ask you to do something twice, you failed. First time: do it manually on 3-10 items. Show me. If I approve, codify it into a skill file. If it should run automatically, put it on a cron."
- **Key claim**: Yegge's reported 100x productivity gap is real and replicable — but the explanation is *architectural*, not model-quality. "The 2x people and the 100x people are using the same models."
- **Building system in production**: YC Startup School matching engine (6,000 founders at Chase Center, July 2026) demonstrates the full [[thin-harness-fat-skills]] stack — `/enrich-founder`, `/match-breakout`, `/match-lunch`, `/match-live`, `/improve` skills with self-rewriting feedback loop
- **Notable phrase**: "Markdown is a more perfect encapsulation of capability than rigid source code, because it describes process, judgment, and context in the language the model already thinks in."

## Connections
- Related: [[thin-harness-fat-skills]], [[skill-as-method-call]], [[latent-vs-deterministic]], [[diarization]], [[resolvers]], [[harness-design]], [[claude-code]], [[ralph-wiggum]], [[boris-cherny]], [[openclaw]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-18 | raw/2026-04-18-garrytan-thin-harness-fat-skills.md | Initial creation — full bio + framework attribution |
