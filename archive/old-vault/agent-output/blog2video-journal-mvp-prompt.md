---
source: agent
date: 2026-03-10
type: prompt for blog2video Claude Code
purpose: 最小化改造支持 building journal 视频
---

# Prompt（直接复制给 blog2video 的 Claude Code）

---

## 需求

我要用现有的 blog2video 管线做一个新系列 **"Vibe Coding 实战"**，内容是我自己的 building journal（第一人称开发实践分享），不是翻译外部英文博客。

需要**最小化改造**，让管线支持两种品牌模式：现有的"精读AI"和新的"Vibe Coding 实战"。

## 改造范围（只改这几个地方）

### 1. 新增 brand config 机制

在 `.claude/skills/blog2video/prompts/` 下新建 `brands.md`：

```markdown
# Brand Configurations

## brand: jingdu (默认)
- 频道名: 精读AI
- 定位语: AI 世界很吵，每期读透一篇。
- 开场: "这里是精读AI。AI 世界很吵，每期帮你从全球顶级 AI 团队的一手文献里，读透一篇最值得读的。今天我们精读的是 [来源名称]。"
- 收尾: "AI 世界很吵，精读一篇，胜过刷一百条。我们下期再见。"
- 系列标签: "精读AI · [topic]"
- CTA 品牌行: "精读AI × LoreAI"
- CTA 标语: "扫码关注 · 每期读透一篇"
- CTA 副标: "AI 世界很吵，每期帮你读透一篇"
- CTA URL: "loreai.dev/zh/subscribe"
- CTA QR: "qr-subscribe-zh.png"

## brand: vibe-coding
- 频道名: vfan builds
- 定位语: 非科班 builder 的 AI 开发日记。
- 开场: "我是 vfan，一个非科班出身的 builder。这个系列记录我用 AI 工具造东西过程中的真实发现。今天聊的是——[主题]。"
- 收尾: "如果你也在 vibe coding，欢迎关注，我们一起边做边学。下期见。"
- 系列标签: "vfan builds · [topic]"
- CTA 品牌行: "vfan builds"
- CTA 标语: "关注我 · 边做边学"
- CTA 副标: "非科班 builder 的 AI 开发日记"
- CTA URL: "loreai.dev/zh/subscribe"
- CTA QR: "qr-subscribe-zh.png" (先复用同一个 QR)
```

### 2. 修改 script-writer.md

在 script-writer.md 里把现在硬编码的品牌文案替换为引用 brands.md 的对应 brand。具体来说：

- 把 L11-22 的固定品牌文案改成：`参考 brands.md 中对应 brand 的开场/收尾模板`
- 在 prompt 开头加一行：`品牌模式由 video_plan.json 的 "brand" 字段决定，默认 "jingdu"`

**不改其他任何叙事风格规则**（语气、人称、字数、TTS 规则全部保留）。

### 3. 修改 content-analyzer.md

在 video_plan.json 的 output schema 里加一个字段：

```json
{
  "brand": "jingdu | vibe-coding",
  ...其他字段不变
}
```

默认值 `"jingdu"`。当用户指定 `--brand vibe-coding` 或在 prompt 里说明是 building journal 时，设为 `"vibe-coding"`。

### 4. 修改 CtaSlide.tsx

把硬编码的品牌文案改为从 slide config data 读取：

```tsx
// 从 props.data 读取，带默认值（兼容旧配置）
const brandLine = data.brand_line || "精读AI × LoreAI";
const tagline = data.tagline || "扫码关注 · 每期读透一篇";
const subtitle = data.subtitle || "AI 世界很吵，每期帮你读透一篇";
const ctaUrl = data.cta_url || "loreai.dev/zh/subscribe";
const qrImage = data.qr_image || "qr-subscribe-zh.png";
```

### 5. 修改 render-all.mjs

在自动追加 CTA slide 时，根据 video config 里的 brand 字段注入对应的 brand data：

```js
// 读取 brand，从 video_plan.json 或 video config
const brand = config.brand || "jingdu";
// 从 brands config 获取对应 CTA 文案，注入到 cta slide data
```

### 6. 修改 slide-data-generator.md

把 cover slide 的系列标签从硬编码的 `精读AI · [topic]` 改为根据 brand 字段选择对应标签。

## 不改的东西

- 视频规格（1080×1920, 30fps, 暗色主题）
- TTS 管线（MiniMax API, YunxiNeural）
- Slide 类型和渲染逻辑
- Puppeteer 截图流程
- 叙事风格规则（语气、人称、字数限制）
- design-system.md 的颜色/字体（两个品牌共享视觉风格）
- 发布流程（PUBLISH-RULES.md, STYLE_GUIDE.md 暂不改）

## 验证标准

改完后，用以下方式验证：

1. **默认模式不受影响**：不指定 brand 时，行为和改造前完全一致（"精读AI" 品牌）
2. **新品牌模式可用**：指定 `brand: "vibe-coding"` 时，开场/收尾/CTA 全部使用新文案
3. **第一个测试内容**：用 `agent-output/vibe-coding-script.md`（已有的口播稿）作为输入，生成一个 vibe-coding 品牌的视频
