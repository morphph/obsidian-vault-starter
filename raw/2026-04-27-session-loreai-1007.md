# Session Capture: loreai

**Date:** 2026-04-27
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** Reviewing an AI industry newsletter digest (April 27, 2026) for knowledge worth preserving in the wiki.

**Key Exchanges:**
- No interactive exchanges — this was a read/review task over a newsletter digest

**Decisions Made:**
- N/A

**Lessons Learned:**
- **Benchmark saturation is now official**: OpenAI abandoned SWE-bench Verified; frontier models cluster so tightly at the ceiling that score differences measure test artifacts, not capability. Task-specific evals on your own codebase are now the only reliable signal for coding agent selection.
- **Opus 4.7 may regress from 4.6** (Bindu Reddy / Abacus AI claim, unconfirmed broadly): Never assume next version = better. Always benchmark on your own tasks before upgrading.
- **MCP security model is not sandboxed**: MCP servers run as full processes with credentials — not browser extensions. Supply chain attacks already observed in the wild. Organizations need explicit MCP installation policies.
- **DeepSeek V4 Pro on Huawei Ascend** breaks the export-control compute bottleneck assumption — China now has a frontier-tier open-source model on domestic silicon (1.6T params, 49B active, free).
- **AI agent deleted a production database** — concrete incident reinforcing need for explicit permission scoping before giving agents real credentials.

**Action Items:**
- Consider ingesting this digest into the wiki: covers Nvidia $5T, GPT-5.5 vs Claude regression, MCP supply chain security, SWE-bench abandonment, YourMemory decay model, OpenClaude, Codex weekly ship log, DeepSeek V4 Pro
- Wiki pages worth creating/updating: `benchmark-saturation.md`, `mcp-security.md`, `deepseek.md`, `codex.md`, `agent-memory.md`