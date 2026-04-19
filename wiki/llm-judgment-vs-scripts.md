---
type: concept
created: 2026-04-07
last-updated: 2026-04-19
sources:
  - raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md
  - raw/2026-04-11-garry-tan-thin-harness-fat-skills.md
tags: [wiki, principle, system-design, harness-engineering]
---

# LLM Judgment vs Scripts

## Summary
Design principle: LLMs handle judgment (synthesis, prioritization, drafting, reasoning), and deterministic scripts handle everything else (reading files, calling APIs, sending messages, comparing timestamps). When you push deterministic work through an LLM, things break unpredictably and you stop trusting the system.

## Details
- **Formulated by [[ryan-sarver]]** from building Stella on [[OpenClaw]]
- **The failure mode:** Routing deterministic operations through LLMs introduces stochastic errors in places that should be reliable. Users lose trust in the system.
- **The rule:** Anything with a known-correct answer (file I/O, API calls, timestamp comparison, sending messages) goes in Python. LLM only handles tasks requiring judgment: synthesis, prioritization, drafting, reasoning about ambiguous situations.
- **Examples in Sarver's system:**
  - ✅ LLM: synthesize meeting notes, prioritize tasks, draft emails in user's voice, research and filter information
  - ✅ Script: pull from Granola API, sync to Todoist, send WhatsApp notifications, generate daily note files, run cron jobs
- **Convergent evolution with [[harness-design]]:** Anthropic's principle is "LLM as reasoning center; Harness provides perception, action, memory, and constraints." Sarver independently discovered the same boundary — LLM reasons, everything else is scaffolding. Different domain (personal assistant vs coding agent), same principle.
- **[[garry-tan|Garry Tan]]'s reformulation as [[latent-vs-deterministic]]** (2026-04-11): same line, different vocabulary. "Latent space is where intelligence lives. Deterministic is where trust lives." Garry's emphasis is on the *capability* failure mode — forcing combinatorial work (e.g., seating 800 people) into latent space produces hallucinated outputs that look plausible but are wrong. Sarver's emphasis is on the *trust* failure mode — stochastic errors in deterministic places erode user trust. Together they cover both halves of why the line matters.
- **Applies to this wiki:** `/ingest` uses LLM for extraction and synthesis, but file creation, index updates, and log appends are deterministic operations handled by the harness

## Connections
- Related: [[harness-design]], [[ryan-sarver]], [[openclaw]], [[claude-code]], [[garry-tan]], [[latent-vs-deterministic]], [[thin-harness-fat-skills]], [[connection-llm-judgment-vs-scripts-and-harness-design]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-04-07 | raw/2026-04-07-rsarver-ai-chief-of-staff-openclaw.md | Initial creation |
| 2026-04-19 | raw/2026-04-11-garry-tan-thin-harness-fat-skills.md | Added Garry Tan's reformulation as [[latent-vs-deterministic]]; capability vs trust failure-mode framing |
