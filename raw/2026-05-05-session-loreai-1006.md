# Session Capture: loreai

**Date:** 2026-05-05
**Project:** loreai
**Source:** Claude Code session (auto-captured via hooks)
**Fetch method:** Pipeline B — SessionEnd/PreCompact hook → flush.py → Agent SDK

---

**Context:** 生成 2026-05-05 AI 日报，覆盖 DeepSeek V4 Pro、Anthropic 创意战略、Unity Agent 化等主题。

**Key Exchanges:**
- DeepSeek V4 Pro 声称跑分超 Opus 4.7 和 GPT 5.5，成本低 10 倍，MoE 架构是关键
- Anthropic 官宣 Claude 进军创意领域（写作、设计、艺术协作）— 战略转向信号
- Unity 编辑器内置 AI Agent + AI Gateway + MCP Server，基础设施级变化
- Sierra 八个季度做到 $150M ARR，$15B+ 估值 — AI Agent 商业化最强数据点
- Anthropic Python SDK v0.98.0 / TS SDK v0.93.0：企业认证全家桶（Workload Identity Federation、OAuth、Auth Profiles）
- Claude Code v2.1.128：.zip 插件包、`/mcp` 诊断、`--channels` 认证
- Blueprint-Bench 2：GPT 5.5 第一，人类仍显著领先所有模型
- Context Engineering 被 Patrick Debois 定位为"能用"vs"生产级"的分水岭

**Decisions Made:**
- 日报精选选了 DeepSeek V4 Pro 作为头条 — 理由是成本曲线压缩对行业定价逻辑的冲击比单纯跑分更有战略意义
- 模型小课堂选了 MoE 架构科普，与头条呼应

**Lessons Learned:**
- DeepSeek V4 自我测试是双刃剑：正确时提升表现，错误时"自信地错下去"，不能替代外部测试
- Mollick 指出前沿 Agent 跑分正在失去信号 — harness vs API 结果差异大，做模型选型别只看排行榜
- AI 产品设计分化：Clippy（纯工具）vs Anton（有性格的协作者），Claude 选创意伙伴路线，GPT 选效率工具路线
- Cisco 收购 Astrix 确认 Agent 安全已成独立收购品类

**Action Items:**
- 跟踪 DeepSeek V4 Pro 跑分是否经得住独立验证
- 关注白宫可能对 AI 模型设新护栏的行政令动向
- wiki 应更新：Anthropic 创意战略转向、SDK 企业认证能力、DeepSeek V4 Pro MoE 成本优势