---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-repo-mattpocock-skills.md
  - raw/2026-05-17-aihero-5-agent-skills.md
tags: [wiki, classification, workflow, afk]
---

# HITL vs AFK Classification

## Summary
Per-issue labeling pattern from Matt Pocock's `/to-issues` skill: every backlog item is tagged either **HITL** (human-in-the-loop, needs judgment) or **AFK** (away-from-keyboard, agent-executable). The AFK queue is what feeds autonomous loops; HITL items stay manual. The "missing piece" that makes Ralph runnable in production.

## Details

### Source
Matt Pocock's [[mattpocock/skills repo|mattpocock-skills-library]] `/to-issues` skill description (from the repo's README):
> "Break any plan, spec, or PRD into independently-grabbable GitHub issues using vertical slices."

Each issue produced gets classified for autonomy boundary.

### Decision rule
The pragmatic question per issue: **does the agent need human judgment to call this done?**
- No → AFK (agent self-executes)
- Yes → HITL (human reviews)

### AFK-suitable
- Well-scoped implementations with passing tests as success
- Refactors with type/test gates
- Test backfill (uncovered lines → cover)
- Migration passes
- Mechanical data transforms
- Lint cleanup

### HITL-required
- Architecture decisions
- UX copy and microcopy
- API design (the public-interface shape itself)
- New feature framing
- Code review of risky changes
- Any work where "good" requires taste

### Why labels matter
Without classification, two failure modes:
1. **All-HITL** → no autonomy benefit; treating Ralph as expensive copilot
2. **All-AFK** → agent ships confident garbage on judgment work; reputation cost

### Where the label lives
- GitHub: as labels on issues (`afk`, `hitl`)
- Local backlog: column header in TODO file

## Connections
- Source skill: [[mattpocock-skills-library]] (`/to-issues`)
- Execution layer: [[ralph-wiggum]], [[sandcastle]]
- Phase context: [[idea-to-afk-agent-flow]] (Phase 5 dispatcher input)
- Related: [[llm-judgment-vs-scripts]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | Matt's skills repo README + AI Hero 5 skills writeup | Initial creation |
