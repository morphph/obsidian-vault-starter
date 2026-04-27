# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Generated a Chinese-language AI newsletter (blog2video/AI精读 style) covering major AI news for April 27, 2026.

**Key Exchanges:**
- No interactive Q&A — this was a single-turn article generation session.

**Decisions Made:**
- Article framing: led with DeepSeek V4 on Huawei Ascend + OpenAI retiring SWE-bench as the paired narrative ("一个在造路，一个在拆桥")
- Included a "模型小课堂" section explaining benchmark saturation for general readers
- 今日精选 focused on the SWE-bench retirement as the deepest insight

**Lessons Learned:**
- **DeepSeek V4 Pro**: 1.6T params / 49B activated, runs on Huawei Ascend — first frontier-class model on domestic Chinese chips; also fully open-source
- **OpenAI retired SWE-bench Verified**: official rationale — frontier models saturated near ceiling, score differences reflect test-taking skill not real ability
- **GPT-5.5**: 50% token reduction, 33% speed gain, slight accuracy uptick (Notion benchmark)
- **Opus 4.7 regression warning**: Abacus AI reports it underperforms Opus 4.6 — upgrade ≠ improvement
- **AI Agent production DB deletion**: real incident, reinforces need for sandbox + least-privilege permissions before granting DB write access to agents
- **MCP supply chain attack**: already happening in the wild; MCP servers hold credentials and system access — treat them like privileged processes, not browser plugins
- **NVIDIA $5T market cap**: fastest company to reach this milestone (~2 years from $1T)

**Action Items:**
- Ingest DeepSeek V4 and SWE-bench retirement as wiki pages if raw sources are added
- Consider adding MCP security as a standalone wiki topic (supply chain risk angle)
- Flag Opus 4.7 regression finding — worth re-checking when more eval data arrives