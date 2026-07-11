# Research Plan: AI coding agent 的上下文窗口管理入门
> depth: quick · ⚠️ 互动数据：X/YouTube 本机无 scanner，将标「推断·未实测」
> ⚠️ headless: plan checkpoint skipped（WF3 driver 调起，无人应答暂停）
> ⚠️ 消歧自决已记录（见下「消歧块」）

## 渠道① Web / 官方站   ← 现在最硬的实测源
- 查询：
  - `AI coding agent context window management` official docs
  - `context management` site:anthropic.com（Claude Code / harness design）
  - `context window` site:openai.com（Codex agent loop / compaction）
  - `context rot` LLM agent long context degradation
  - `Cursor` context management rules `.cursorrules` docs
  - `prompt caching` context window cost coding agent
  - `compaction` vs `clear` coding agent session
  - `subagent context isolation` coding agent
- 点名直查：anthropic.com/engineering · docs.claude.com · openai.com/index · cursor.com/docs ·
  latent.space · simonwillison.net
- 搜法：官方文档 / 原始出处优先（这一渠道喂事实核验最准）——本话题事实锚点几乎全在官方博客/docs

## 渠道② X / Twitter
- 查询：
  - `"context management" coding agent min_faves:50 site:x.com`
  - `"context rot" site:x.com`
  - `"compact" OR "rewind" Claude Code context site:x.com`
  - `context window Codex Cursor site:x.com`
- 搜法：按收藏(bookmark)加权；抓 long-article 格式；记 作者@handle + 互动 + 是否长文
- ⚠️ 本机无 `bird` → 互动数标「推断·未实测」

## 渠道③ YouTube
- 查询：
  - `Claude Code context management tutorial 2026`
  - `context window management AI coding agent`
  - `/compact /clear Claude Code`
- 搜法：近 60 天优先；实操 > 理论
- ⚠️ 本机无 `summarize`/`last30days` → 观看/互动标「推断·未实测」

## 消歧块（headless 自决，已记录）
- 话题措辞是「AI coding agent」（泛指），非单一工具 → **自决：不锁死到 Claude Code**。
  按「以 Claude Code 为主锚（vault 存量最厚 + 事实最全），横向带 OpenAI Codex / Cursor 做
  跨工具对照」处理。理由：(a) 措辞用了通用词「AI coding agent」而非具体产品名；(b) 现有
  draft `claude-code-context-management-guide.md` 已吃透纯 Claude Code 角度，跨工具入门才有增量。
- 「入门」= 面向 audience-profile 的「能上手但非资深工程师」读者 → 事实轴给底层机制的干净定义，
  增长轴优先实操/框架类角度，不下沉到源码级实现。

## 综合契约（提醒后面 step 5）
- report.md 按双轴综合：事实轴（锚官方源）+ 增长轴（按渠道排 Top-N + 形式拆解 + 角度）
- 候选源对 raw/ 去重（本 vault raw/ 已有大量 Claude Code / Codex 官方源，命中即标「已在库」）
- 拿不到的数据标「推断·未实测」，绝不瞎编
- ⚠️ 重复预警已知：`drafts/claude-code-context-management-guide.md` 命中同话题 → report §0 显著标注，
  outline `prior_coverage` 逐条声明增量
