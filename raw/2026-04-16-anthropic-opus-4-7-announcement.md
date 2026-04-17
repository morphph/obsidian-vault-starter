# Introducing Claude Opus 4.7

**Source:** https://www.anthropic.com/news/claude-opus-4-7
**Publication Date:** 2026-04-16
**Fetch method:** WebFetch

## Overview

Anthropic has released Claude Opus 4.7, a significant advancement over its predecessor with notable improvements in advanced software engineering, vision capabilities, and reasoning tasks. The model is now generally available across all Claude products, APIs, and cloud platforms.

## Key Capabilities

**Software Engineering:** Users report confidently delegating complex, long-running coding tasks previously requiring close supervision. The model demonstrates rigor in handling intricate assignments, precise instruction adherence, and self-verification capabilities before reporting results.

**Vision Improvements:** Opus 4.7 processes images up to 2,576 pixels on the long edge (approximately 3.75 megapixels)—more than three times the resolution of earlier Claude models. This advancement supports computer-use agents, data extraction from complex diagrams, and pixel-perfect reference work.

**General Performance:** While less broadly capable than Claude Mythos Preview, Opus 4.7 shows improvements across numerous benchmarks compared to Opus 4.6.

## Safety and Cybersecurity

Following Project Glasswing's announcement, Anthropic deliberately reduced Opus 4.7's cyber capabilities compared to Mythos Preview. The model includes automated safeguards detecting and blocking high-risk cybersecurity requests. Security professionals may apply to the Cyber Verification Program for legitimate research, penetration testing, and red-team activities.

## Pricing and Availability

**Cost:** $5 per million input tokens; $25 per million output tokens (unchanged from Opus 4.6)

**API Access:** Use `claude-opus-4-7` via Claude API

**Platforms:** Available through Claude products, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry

## Notable Features

**Instruction Following:** Opus 4.7 interprets instructions more literally than predecessors. Previous prompts may produce unexpected results requiring re-tuning.

**Effort Control:** New `xhigh` effort level provides granular control between `high` and `max` effort, balancing reasoning depth and latency.

**Memory:** Enhanced file system-based memory retention across multi-session work.

**Claude Code Updates:**
- New `/ultrareview` command for dedicated code review sessions
- Pro and Max users receive three complimentary ultrareviews
- Extended auto mode for Max subscribers

## Migration Considerations

**Tokenizer Changes:** Updated tokenization increases token mapping by approximately 1.0–1.35× depending on content type.

**Output Tokens:** Higher effort levels produce more thinking tokens, particularly in agentic multi-turn scenarios, improving reliability on difficult problems.

A detailed migration guide addresses upgrading strategies and token usage optimization.

## Industry Recognition

Early-access testers reported substantial improvements:

- Financial technology platform VP: "Catches logical faults during planning, accelerates execution far beyond previous Claude models"
- Cursor CEO: "Meaningful jump in capabilities...clearing 70% versus Opus 4.6 at 58%"
- Notion AI Lead: "Plus 14% over Opus 4.6 at fewer tokens and a third of tool errors"
- XBOW CEO: "98.5% on visual-acuity benchmark versus 54.5% for Opus 4.6"
- Rakuten GM: "Resolves 3x more production tasks than Opus 4.6"

## Safety Assessment

Opus 4.7 maintains a similar safety profile to Opus 4.6, showing low rates of deception, sycophancy, and misuse cooperation. The model improves on honesty and resistance to prompt injection attacks but shows modest weakness in controlled substance harm-reduction guidance. Anthropic's alignment assessment concluded the model is "largely well-aligned and trustworthy, though not fully ideal in its behavior."
