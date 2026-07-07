# /learn-note — headless 精读+白板图作业书

> 由 `obsidian-content learn` 无头 spawn（`claude -p "/learn-note <args>"`）。外壳只认磁盘产物，你的自述不作数。
> **Headless 铁律**：绝不暂停提问；歧义自决并记录在精读文末「文末注记」；只写本作业书列出的文件——不更新 index/log、不调 record-ingest、不建其他 wiki 页、不 git。

## Arguments

`$ARGUMENTS` = `<source-path> <slug> [skip-visual]`
（例：`raw/2026-07-05-founder-mode.md founder-mode`）

## Step 1 — 精读

1. 完整读 `.claude/skills/ingest/references/structured-close-reading.md` 并严格遵循。
2. 读源文件 `<source-path>`。
3. 写 `wiki/source-<slug>.md`：
   - frontmatter：`type: source-summary`、`created`/`last-updated`（今天）、`sources:` 列源路径、`tags: []`
   - 正文：`# 精读：{原文标题}`，其下一个 `## 精读` section 装全部内容——元信息头（含 `**一句话主旨**：` 行，逐字用这个字段名）→ 按原文章节序的正文精读 → `## 精读收尾`（一句话总结/关键引语/与 vault 的连接/视频适配自评）。
   - 若该文件已存在（修订重跑）：按当前源与格式重写整个 `## 精读` section，frontmatter 的 `last-updated` 更新。

## Step 2 — 白板图（跳过条件：args 含 `skip-visual`）

1. 完整读 `.claude/skills/excalidraw-diagram/SKILL.md`（尤其 **Step Annotation & Layered Export** 节）+ `references/color-palette.md` + `references/element-templates.md`。
2. **可图则图判断**：如果文章没有可空间化的论证结构（纯叙事/清单/太短），不要硬画——输出末行 `LEARN_NO_VISUAL=<一句话原因>` 并跳到 Step 4。
3. 设计**一张论证型白板图**（Diagrams ARGUE, not DISPLAY）：把原文的核心论证空间化，按论证顺序给每个元素标 `customData.step`（5-7 步）+ 每步一个 `stepLabel`。
   - 白板风：`roughness: 1`、白底、配色系统：橙红手写章节标题 / 粉珊瑚椭圆=核心概念节点 / 绿色矩形=输入输出 / 白底黑框=流程盒 / 灰圆柱=存储 / 黑箭头；标签中英混排（术语保英文）。
4. 写 `visuals/<slug>/<slug>-diagram.excalidraw`（文件名必须带 slug 前缀——防 Obsidian 同名嵌入歧义）。
5. **强制渲染回环**（2-4 轮）：
   ```bash
   cd .claude/skills/excalidraw-diagram/references && \
   uv run python render_excalidraw.py ../../../../visuals/<slug>/<slug>-diagram.excalidraw
   ```
   用 Read 工具看生成的 PNG，修重叠/越界/配色问题，直到合格。
6. 分层导出：
   ```bash
   uv run python render_excalidraw.py ../../../../visuals/<slug>/<slug>-diagram.excalidraw \
     --export-layers ../../../../visuals/<slug>/
   ```

## Step 3 — 嵌入

在 `wiki/source-<slug>.md` 里图最相关章节的精读末尾插入：

```
> [!note] 白板图示：{一句话说明图讲什么}

![[<slug>-diagram.png]]
```

## Step 4 — 收尾

- 精读文末补「### 文末注记（headless 消歧自决）」列出你自决过的歧义（没有就写"无"）。
- 最终输出行（必须是最后一行、逐字格式）：
  - 成功：`LEARN_DONE=wiki/source-<slug>.md`
  - 精读无法完成（源文件损坏/为空等）：`LEARN_FAILED=<一句话原因>`
