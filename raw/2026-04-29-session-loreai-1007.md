# Session Capture: loreai

**Date:** 2026-04-29
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** User compiled and formatted the daily AI newsletter digest for April 29, 2026.

**Key Exchanges:**
- Newsletter covers 20+ items across AI industry news, model releases, and tooling updates
- Three headline stories: Claude's Blender MCP connector, Mistral Workflows (durable execution), GPT-5.4 Pro cracking an Erdős conjecture
- Model Literacy section explains "durable execution" — checkpointed agent state that survives crashes

**Decisions Made:**
- Pick of the Day: GPT-5.4 Pro + Erdős conjecture — framed as a category shift from "useful assistant" to "research collaborator"
- Durable execution selected as the conceptual explainer — ties together Mistral Workflows and Sakana Fugu launches

**Lessons Learned:**
- **OpenAI is now multi-cloud**: Models coming to Amazon Bedrock after Microsoft exclusivity dissolution — enterprise procurement implications
- **Durable execution** is the missing reliability layer separating demo agents from production agents (checkpoint + resume on failure)
- **IP ownership of AI-generated code** is becoming a real legal question as agentic coding scales to enterprise codebases
- **Claude entering creative tooling** via Blender MCP connector signals Anthropic expanding beyond coding assistant positioning

**Action Items:**
- Wiki pages to create/update: [[openai-bedrock]], [[durable-execution]], [[mistral-workflows]], [[talkie-model]], [[vibevoice]], [[claude-blender-mcp]], [[erdos-conjecture-ai]], [[claude-code-ip-ownership]]
- Track OpenAI's $8 tier impact on consumer AI economics — 122M subscriber projection vs Pro cannibalization
- Track Anthropic APAC expansion (Sydney office, Theo Hourmouzis as ANZ GM)
- Update [[anthropic]] with Blender connector and Sydney office
- Update [[openai]] with Bedrock deal, $8 tier, Erdős result, Codex GPT-5.5 migration