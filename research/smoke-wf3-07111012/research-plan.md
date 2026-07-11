# Research Plan: LLM 输出的结构化 JSON — schema 约束与校验实践
> depth: quick · ⚠️ 互动数据：X/YouTube 本机无 scanner，将标「推断·未实测」
> ⚠️ headless（WF3 driver 调起）：plan checkpoint skipped；消歧自决并记录于下

## 渠道① Web / 官方站   ← 现在最硬的实测源（quick 深度主力）
- 查询：
  - OpenAI structured outputs JSON schema `site:platform.openai.com`
  - Anthropic tool use / structured output JSON schema `site:docs.anthropic.com`
  - "constrained decoding" grammar JSON schema LLM
  - Pydantic AI / Instructor library structured output validation
  - "JSON schema" strict mode reliability LLM 2026
  - Outlines / Guidance / llguidance constrained generation
  - function calling vs response_format json_schema 差异
  - retry / re-ask on validation failure pattern LLM
- 点名直查：platform.openai.com/docs（Structured Outputs）· docs.anthropic.com（tool use / JSON mode）·
  github.com/jxnl/instructor · ai.pydantic.dev · github.com/dottxt-ai/outlines · json-schema.org
- 搜法：官方文档 / 原始 repo 优先（这一渠道喂事实核验最准；方法论话题**强烈优先官方源**）

## 渠道② X / Twitter
- 查询："structured outputs" json schema min_faves:50 site:x.com ·
  "constrained decoding" site:x.com · pydantic instructor llm site:x.com
- 搜法：按收藏加权；抓 long-article / thread；记 作者@handle + 互动 + 是否长文
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」

## 渠道③ YouTube
- 查询："structured outputs" openai tutorial · "instructor" pydantic llm youtube ·
  constrained decoding json schema 2026
- 搜法：近 60 天优先；实操 > 理论
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」

## 消歧块（headless 自决并记录）
- "schema 校验" 在本话题语境 = **对 LLM 生成的 JSON 做结构约束（生成期）+ 事后校验（Pydantic/Zod/JSON Schema validator）**，
  非数据库 schema、非 GraphQL schema。→ 判据：topic 明含「LLM 输出的结构化 JSON」，锁定 LLM 生成场景。
- "结构化 JSON" 覆盖三条技术路线：(a) 供应商原生 Structured Outputs / JSON mode（response_format）；
  (b) 约束解码 constrained/guided decoding（grammar/FSM）；(c) 应用层库 re-ask 校验（Instructor/Pydantic AI）。
  → 三条都扫，report §1 分清「生成期保证」vs「事后校验」两层。

## 综合契约（提醒后面 step 5）
- report.md 按双轴综合：事实轴（锚官方源，逐条 ✅/⚠️/❌）+ 增长轴（按渠道排 Top-N + 形式拆解 + 排序角度）
- 候选源对 raw/ 去重（本话题 raw/ 无直接源，预期全为新候选）；拿不到的互动数据标「推断·未实测」，绝不瞎编
- 源纯度：官方 API 文档 / 库作者 repo 为 Tier-3 首选；第三方教程标「(第三方，ingest 前确认)」
