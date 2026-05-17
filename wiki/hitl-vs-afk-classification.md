---
type: concept
created: 2026-05-17
last-updated: 2026-05-17
sources:
  - raw/2026-05-17-adityapuri-matt-pocock-5-skills.md
  - raw/2026-05-17-tessmann-agent-teams-ralph-hybrid.md
tags: [wiki, classification, workflow, afk]
---

# HITL vs AFK Classification

## Summary
Per-issue labeling pattern from Matt Pocock's `/to-issues` skill and the Tessmann hybrid: every backlog item is tagged either **HITL** (human-in-the-loop, needs judgment) or **AFK** (away-from-keyboard, agent-executable). The AFK queue is what feeds autonomous loops; HITL items stay manual. The "missing piece" that makes Ralph runnable in production.

## Details

### Decision rule
Ask: **Can a script return pass/fail on this work's output?**
- Yes → AFK
- No → HITL

(Tessmann's formalization: "machine-verifiable → loop, not verifiable → human.")

### AFK-suitable
- Well-scoped implementations with passing tests as success
- Refactors with type/test gates
- Test backfill (uncovered lines → cover)
- Migration passes
- Doc generation with format/structure checks
- Lint cleanup
- Mechanical data transforms

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
- Tessmann's hybrid: lives in the team brief; planner agent assigns

## Connections
- Source skill: [[mattpocock-skills-library]] (`/to-issues`)
- Hybrid pattern: [[shared-contracts-pattern]] (Tessmann)
- Execution layer: [[ralph-wiggum]], [[sandcastle]]
- Phase context: [[idea-to-afk-agent-flow]] (Phase 5 dispatcher input)
- Related: [[llm-judgment-vs-scripts]]

## Source Log
| Date | Source | What changed |
|------|--------|-------------|
| 2026-05-17 | Aditya walkthrough + Tessmann hybrid | Initial creation |
