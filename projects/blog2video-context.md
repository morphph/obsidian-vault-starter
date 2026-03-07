---
status: active
role: content-pipeline
last-updated: 2026-03-04
repo: ~/Desktop/Project/blog2video
---

# [[blog2video]]

English tech blogs → Chinese narrated videos for Xiaohongshu and WeChat Video.
Brand: AI精读. Built as Claude Code slash command pipeline.

---

## Auto-synced from repo
<!-- Updated by /sync-project. Do not edit manually. -->

**Architecture:** 4-stage subagent pipeline orchestrated via Claude Code slash commands. Input (blog URL, PDF, YouTube, GitHub repo, Twitter/X article) → Content Analyzer → Script Writer (Chinese narration) → Slide Data Generator → Remotion Render + Edge TTS. Each stage reads/writes files independently (no shared state). Post-render SCP delivery to remote publishing queue.

**Tech stack:** Claude Code (orchestration), Claude API Sonnet (content analysis + script generation), Remotion 4.0 (React video rendering), Edge TTS (zh-CN-YunxiNeural), Puppeteer (Twitter/screenshots), pdfminer, yt-dlp, Node.js 18+, Python 3.8+

**Recent activity:**
- Add post-render delivery: auto SCP videos to publish queue
- Add Twitter/X long-form articles as input type (Puppeteer-based)
- Add content preprocessors for all input types (Step 0.5)
- Fix slide timing accuracy and add --skip-tts flag
- Ban --- separators in script to prevent TTS timing failures
- Add series episode transitions, rename brand to 精读AI
- Optimize cover photo and hook prompts for 小红书 scroll-stopping power
- Prepare for npm package publishing

**Current status:** 11+ video series shipped. Supports 6 input types. Auto-delivery to remote publishing service (Claudiny) for 小红书/视频号 distribution.

---

## Human context

### Why this project exists
[Write: why Chinese video content from English tech blogs?]

### Current state and bottleneck
[Write: what works, what doesn't?]

### Key decisions and reasoning
- Chinese narration, not translation — cultural context matters
- Target platforms: Xiaohongshu, WeChat Video — reason: [fill in]
- Explored agent-optimized approach (llms.txt, npm package) from YC "Agent Economy" research

### Connections to other projects
- Final output serves [[LoreAI]] content production module
- Explored Remote Control feature for monitoring long-running pipeline runs

### Open questions
- Video pacing for Xiaohongshu — too fast?
- ROI measurement: views vs [[LoreAI]] traffic conversion?

### Learnings
- [Add as you go]
