# Outline: 约束解码 vs 校验重试 — 让 LLM 稳定吐结构化 JSON 的两层心智模型 + 失败模式清单
> 基于角度: report §7 角度1（推荐）· 目标渠道/形式: 博客长文（含三路线对比表 + 失败模式 callout）

## prior_coverage（强制字段——对「已表达角度清单」逐条声明关系）
- 无旧角度——首次覆盖该话题。`wiki/index.md` 无直接页，`drafts/` 无成稿（grep 命中的 json/validation 均为其他指南顺带提及，非本话题）。
- 可嫁接的相邻立场（非重合，属框架复用）：[[latent-vs-deterministic]] / [[silent-fallback-antipattern]] / [[llm-judgment-vs-scripts]] / [[verification-loops]]——本文是它们在「结构化输出」上的具体落地，属**新证据推进**而非重复。

## take 占位（Gate 1 由作者填，3–5 句: thesis / 不同意主流叙事哪点 / 对 AI builder 的含义）
> ⏳ 待作者 take —— 本 outline 的每个主张段都要能挂到 take 上，writer 无 take 不开工。
> 候选编辑立场（供作者定夺，非成稿）：主流教程把「结构化输出」讲成「调对 API 参数」，但真正的心智模型是两层——生成期约束（格式一定对）+ 事后校验（值也得对）；且「strict」有 refusal/截断/schema 子集三条静默泄漏路径，是 deterministic guardrail 而非黑箱，必须 verify。

## 结构（逐节: 论点 + 挂哪些 report 论断/出处 + 预估篇幅占比）
1. **钩子 + 一句话价值 + 谁该读** — 论点：你以为吐 JSON 靠 prompt 求配合，其实早该是两层工程问题 — 证据：[外部: https://openai.com/index/introducing-structured-outputs-in-the-api/]（老模型 ~40% vs 新 100%）— ~8%
2. **两层心智模型（本文骨架）** — 论点：生成期保证（约束解码）≠ 事后校验（Pydantic/Zod），二者叠用 — 证据：[外部: OpenAI 公告] [外部: https://python.useinstructor.com/concepts/reask_validation/] [内部/Tier-1: latent-vs-deterministic] — ~20%
3. **三条技术路线对比表**（此处加对比表 + 加引用来源，GEO） — 论点：原生 SO / 开源约束解码 / 校验重试库，各自何时用 — 证据：[外部: OpenAI docs] [外部: https://platform.claude.com/docs/en/build-with-claude/structured-outputs] [外部: https://ai.google.dev/gemini-api/docs/structured-output] [外部: github outlines/llguidance/instructor] — ~22%
4. **纠正过时叙事**（此处加引用来源） — 论点：Anthropic 已原生 `output_config.format` GA，「只能 forced tool use」已过时 — 证据：矛盾留档① [外部: platform.claude.com docs] [外部: https://x.com/simonw/status/1989800630416990475] — ~12%
5. **失败模式清单（callout）**（此处加统计/具体限制） — 论点：strict 的三条静默泄漏——refusal / `max_tokens` 截断 / schema 子集（无递归/数值/长度约束）— 证据：[外部: OpenAI+Anthropic docs] [内部/Tier-1: silent-fallback-antipattern] — ~18%
6. **反直觉两则**（此处加统计数据，GEO） — 论点：(a) 约束解码常更快（llguidance ~6–9ms<基线）；(b) 但可能税掉推理质量（contested，两面写）— 证据：[外部: https://arxiv.org/pdf/2501.10868] [外部: arXiv 2604.06066]（矛盾留档②）— ~12%
7. **落地清单 + 角色化入口** — 论点：按「简单抽取 / 业务规则 / 自托管 / 需推理」四场景选路线，任何路线都外包一层校验+硬停 — 证据：report §6 最佳实践清单 [内部/Tier-1: verification-loops] — ~8%
