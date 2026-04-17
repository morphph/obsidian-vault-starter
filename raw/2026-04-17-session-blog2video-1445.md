# Session Capture: blog2video

**Date:** 2026-04-17
**Project:** blog2video
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Evaluating HeyGen Hyperframes as potential optimization for the blog2video (AI精读) video creation pipeline.

**Key Exchanges:**
- Hyperframes is an agent-native, HTML-based video framework: write HTML with timing attributes + GSAP timeline → headless Chrome renders MP4 directly
- Current blog2video pipeline: narration.md → slide_config.json → HTML → Puppeteer PNG screenshots → Remotion composites PNG+audio → MP4
- Hyperframes could collapse the last three stages (PNG → Remotion → MP4) into one (HTML → MP4), but requires reimplementing TTS/subtitle pipeline

**Decisions Made:**
- Recommended **Path 1 (low effort, high value)**: steal visual ideas from Hyperframes block catalog, implement as new Remotion slide types — no migration needed
- Prioritized blocks: `x-post`/`reddit-post` (matches existing Twitter input flow), `logo-outro` (brand consistency), `data-chart` (data-heavy blogs), marker highlights (小红书 style emphasis)
- Full migration (Path 3) deemed not worth it — current Remotion setup works fine, no walls being hit

**Lessons Learned:**
- Hyperframes block catalog has 30+ ready-made visual patterns (social embeds, charts, flowcharts, transitions, marker highlights) that map well to blog2video content types
- Hybrid approach (Path 2: Hyperframes for hero slides, Remotion for orchestration) is viable but adds complexity
- The real value isn't the rendering engine — it's the visual vocabulary (richer slide types beyond current 6)

**Action Items:**
- Prototype 2-3 new Remotion slide types inspired by Hyperframes catalog (x-post, logo-outro, data-chart)
- No decision yet made by user on which path to pursue — conversation ended at recommendation stage