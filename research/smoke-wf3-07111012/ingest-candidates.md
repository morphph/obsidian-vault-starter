# Ingest Candidates — LLM 输出的结构化 JSON：schema 约束与校验实践
> 圈选后才 `/ingest`。对 `raw/` 已扫描去重：本话题 raw/ 无直接源，全部为新候选。
> 源纯度（方法论话题强烈优先官方源）：官方 API 文档 / 库作者 repo = 首选；第三方标注确认。

## 官方 / 一手源（优先）
- [ ] https://openai.com/index/introducing-structured-outputs-in-the-api/ — 官方：Structured Outputs 发布，约束解码 + benchmark，点名 Instructor（事实轴锚）
- [ ] https://developers.openai.com/api/docs/guides/structured-outputs — 官方：strict 模式硬规则与限制（additionalProperties/required/子集/编译延迟）
- [ ] https://platform.claude.com/docs/en/build-with-claude/structured-outputs — 官方：Anthropic 原生 `output_config.format`（推翻「只能 forced tool use」旧叙事，必收）
- [ ] https://ai.google.dev/gemini-api/docs/structured-output — 官方：Gemini `responseSchema` + `responseMimeType`（第三方补全，ingest 前直取官方 canonical）
- [ ] https://github.com/567-labs/instructor — 官方 repo：validate-and-reask 范式参考实现，6M+ 月下载
- [ ] https://python.useinstructor.com/concepts/reask_validation/ — 官方 docs：校验失败回灌错误重问的具体机制
- [ ] https://github.com/dottxt-ai/outlines — 官方 repo：route(b) FSM/regex 约束解码参考
- [ ] https://github.com/guidance-ai/llguidance — 官方 repo：运行时即时 mask，性能极
- [ ] https://github.com/BoundaryML/baml — 官方 repo：容错解析器 DSL + 可选 retry（另一路线）
- [ ] https://pydantic.dev/docs/ai/core-concepts/output/ — 官方 docs：agent 框架侧结构化输出+校验

## 学术 / 基准
- [ ] https://arxiv.org/pdf/2501.10868 — JSONSchemaBench：~10k schema × 6 框架，延迟/覆盖率经验证据
- [ ] https://arxiv.org/pdf/2604.06066 — 约束解码 alignment tax（correctness-vs-quality，contested，需两面读）

## 第三方（ingest 前确认纯度）
- [ ] https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers/ — (第三方) 跨厂商对比；可靠性数字未经一手核验，仅作方向参考
- [ ] https://www.youtube.com/watch?v=AFUww-Df0C4 — (第三方) Rémi Louf/.txt「Unix moment」愿景讲座
