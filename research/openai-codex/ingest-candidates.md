# Ingest Candidates: OpenAI Codex 指南

> 人圈选后才 `/ingest`。默认全不勾。方法论/工具类话题**强烈优先官方源**（developers.openai.com / openai.com）；第三方标注。
> 去重说明：`raw/` 已有 Codex 的 **hooks / skills / subagents / cloud-environments / automations / cookbook trilogy / long-horizon / plans-md / chrishayduk** 源。下列**官方核心页（cli/config/models/agents-md/pricing/changelog/mcp/ide）在 vault 中尚无对应 raw/ 源**——是真正的新增缺口，优先补。

## 官方源（优先）

- [ ] https://developers.openai.com/codex/cli — OFFICIAL 锚点页：Codex 是什么 + 安装 + 登录。上手指南脊柱，vault 尚无。
- [ ] https://developers.openai.com/codex/ide — OFFICIAL：IDE 扩展 surface（VS Code/JetBrains）。四 surface 里 vault 缺 IDE/CLI/App 页。
- [ ] https://developers.openai.com/codex/guides/agents-md — OFFICIAL：AGENTS.md 三级优先级 + 旋钮。核心配置原语，vault 无独立源。
- [ ] https://developers.openai.com/codex/config-basic — OFFICIAL：`approval_policy` / `sandbox_mode` / `model` / MCP 配置基础。
- [ ] https://developers.openai.com/codex/config-reference — OFFICIAL：完整 `config.toml` 穷举 reference。
- [ ] https://developers.openai.com/codex/models — OFFICIAL：当前模型阵容 + 选型（GPT-5.5 默认）；解模型命名陷阱的一手源。
- [ ] https://developers.openai.com/codex/mcp — OFFICIAL：Codex 的 MCP server 配置（精确 TOML 语法待此页确认）。
- [ ] https://developers.openai.com/codex/pricing — OFFICIAL：plan 档位 + ChatGPT plan 附带 + rate limit；定价数字的权威源。
- [ ] https://developers.openai.com/codex/changelog — OFFICIAL：带日期的 2026 功能投放；「有什么新」的 source of truth。
- [ ] https://openai.com/index/introducing-gpt-5-5/ — OFFICIAL：GPT-5.5 发布 + Codex 调优（省 40% 输出 token 的数字出处）。
- [ ] https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan — OFFICIAL（help center）：终端用户 plan 接入细节。

## 第三方源（ingest 前确认，勿当官方事实）

- [ ] https://www.freecodecamp.org/news/the-codex-handbook-a-practical-guide-to-openai-s-coding-platform/ — (第三方) 结构最佳的完整实操 handbook；作为「指南形态」范本参考，非事实源。
- [ ] https://simonwillison.net/tags/codex/ — (第三方) 高信号独立 practitioner；Claude Code→Codex 切换叙事 + 亲测；引外部视角用。
- [ ] https://blakecrosley.com/blog/codex-vs-claude-code-2026 — (第三方) Codex vs Claude Code 架构/定价/benchmark 对比；数字必核。
- [ ] https://www.mindstudio.ai/blog/codex-vs-claude-code-2026 — (第三方) 第二份对比，交叉核验 benchmark claim 用。
