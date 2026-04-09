# Session Capture: unknown

**Date:** 2026-04-08
**Project:** unknown
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Improving diagram generation logic in blog2video's `scripts/lib/diagram-gen.ts` for Episode 2 article about Claude Code's Agent Loop.

**Key Exchanges:**
- User pointed out D2 architecture diagram was unnecessary for this article — it's about process/flow, not system architecture. Mermaid with branches (like the error recovery flowchart) is the right fit.
- User also caught that the D2 diagram was placed in the wrong section — "会话层/单轮层" concept appears in QueryEngine section but diagram was under "Agent Loop 是什么".
- After prompt fix, LLM correctly chose 3 mermaid + 1 table, no D2. Content and positions verified on live site.

**Decisions Made:**
- D2 architecture diagrams should only appear when the article genuinely describes multi-layer system architecture (e.g., Episode 1 全景篇), not for process/mechanism articles.
- Mermaid flow diagrams with decision branches are preferred for articles explaining workflows and loops.
- The diagram-gen prompt was updated to evaluate article type first before choosing diagram types.

**Lessons Learned:**
- Simple LR mermaid chains (`A --> B --> C --> D --> E`) render as very thin horizontal strips (~45px height) — nearly invisible. Avoid this pattern or switch to TD layout for short chains.
- Vercel CDN cache can show stale content (old D2 images) even after deploying new version — don't trust initial deploy checks, verify actual content source.
- CJK word counting behaves differently with added mermaid/table markup — word count drops (5266→2780) don't necessarily mean content loss; verify by checking section count and line count instead.

**Action Items:**
- Consider fixing the thin mermaid rendering issue for simple linear chains (45px height problem persists across versions).