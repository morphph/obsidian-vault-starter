# Session Capture: loreai

**Date:** 2026-04-14
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Configuring Claude Code global thinking settings (adaptive thinking + effort level)

**Key Exchanges:**
- User asked to disable adaptive thinking and maximize thinking budget
- Clarified the two knobs: `effortLevel: "high"` controls thinking **depth**; `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` ensures thinking is **never skipped** (even on simple tasks)
- User confused "always thinks deeply" — clarified it's two separate effects: (1) always engages thinking, (2) thinks at "high" level when it does

**Decisions Made:**
- Keep `effortLevel` at `"high"` (not `"max"`) — user explicitly chose this
- Disable adaptive thinking via env var in `~/.claude/settings.json`
- Applied globally (affects all projects)

**Lessons Learned:**
- `~/.claude/settings.json` is **not** in any git repo — can't commit/push. Must SCP or manually sync to other machines (e.g., VPS)
- Running Claude Code sessions need a **restart** to pick up global settings changes
- Two independent thinking controls: `effortLevel` (depth) vs adaptive thinking toggle (whether to think at all)

**Action Items:**
- If setting up new machines with Claude Code, remember to sync `~/.claude/settings.json`