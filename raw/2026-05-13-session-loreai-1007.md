# Session Capture: loreai

**Date:** 2026-05-13
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** 用户完成了 2026-05-13 的 AI 日报 newsletter 撰写（中文，面向 AI builder 读者）。

**Key Exchanges:**
- 完整撰写了一期包含 7 个板块的日报：发布动态、开发者工具、研究前沿、技术实战、行业洞察、值得一试、模型小课堂
- 三个头条：Opus 4.7 fast mode（2.5x 提速）、OpenAI Symphony（多 Agent IDE）、DeepMind 后光标交互实验

**Decisions Made:**
- 今日精选选了 DeepMind 的交互层实验，而非 Opus 4.7 或 Symphony — 理由是这是更根本的平台之争（交互层 = 平台控制权）
- 模型小课堂选了投机解码（Speculative Decoding），配合 Opus 4.7 fast mode 头条形成呼应
- Claude for Legal 被定位为 Anthropic 从通用模型转向行业解决方案的信号

**Lessons Learned:**
- Opus 4.7 fast mode 定价与 Opus 4.6 fast mode 一致（$30/$150 per 1M tokens），waitlist 准入制
- OpenAI Symphony 和 Claude Code agent view 直接竞争，多 Agent IDE 成为新战场
- Simon Willison 发现 Claude Code 单实例可占 30GB 内存 — 实际已知问题，非 edge case
- Needle 项目：26M 参数模型复刻 Gemini tool-calling，比原模型小 1000 倍 — Agent 成本结构可能需要重新评估
- Sakana AI 的 KAME 用 tandem 架构做实时语音，与 OpenAI/xAI 的单模型路线分化
- Thinking Machines 去掉了传统 VAD，用原生交互模型处理对话轮替

**Action Items:**
- 日报已完成草稿，需 ingest 到 wiki 更新相关页面（anthropic、openai、google-deepmind 等）
- 关注 Google I/O 发布（Gemini Omni 传闻）
- 跟踪 Opus 4.7 fast mode waitlist 开放进度
- LangChain 1.3.0 大版本更新，如有使用需迁移 v3 stream_events