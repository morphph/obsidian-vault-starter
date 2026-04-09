# Session Capture: unknown

**Date:** 2026-04-08
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---



**Context:** LoreAI dashboard and pipeline visualization improvements

**Key Exchanges:**
- Fixed `DASHBOARD_SECRET` missing from VPS `.env` (was in PM2 env vars, lost on restart)
- Merged standalone HTML pipeline health report into the web dashboard as a new "Health Report" tab with score, stages, infrastructure checks, and auto-generated action items
- User asked about an old pipeline flow diagram — none existed as a saved file, so we generated one from scratch
- Iterated on the pipeline flow diagram multiple times: cron-based → reorganized by logical purpose (Content stream, Knowledge stream, SEO/AEO Engine stream)

**Decisions Made:**
- Pipeline flow diagram organized by **data flow purpose**, not cron schedule: Content Consumption, Knowledge Extraction, SEO/AEO Authority Pipeline, Feedback Loop
- Light mode background for the diagram (white/gray instead of dark)
- Label human-blocking steps (Flagship Discovery requires `--approve`) with yellow badge
- Label reactive vs proactive stages (Freshness = reactive, Discovery = proactive)
- Created `/pipeline-flow` skill so the diagram can be regenerated anytime after code changes

**Lessons Learned:**
- PM2 env vars don't persist across restarts — always put secrets in `.env` file
- Organizing pipeline diagrams by cron time is confusing; organizing by business purpose (news intake → content consumption → authority building) is much clearer
- Pipeline visualization needs to be regenerable (not static) since the pipeline evolves — hence the slash command

**Action Items:**
- `/pipeline-flow` skill created — reads `PIPELINE.md` + crontab, generates HTML+SVG to `data/review/pipeline-flow-YYYY-MM-DD.html`, auto-opens in browser