# Google Gemini Family

```yaml
---
source_id: google-gemini
source_type: blog-bundle
org: Google DeepMind
release_date: ongoing
priority: A
status: stub
openness: closed-weights
confidence: medium
lineage: google-gemini
role: family-bundle
---
```

## 一句话

Gemini 系列是 frontier closed-weights 中**唯一**还在出 TR/技术报告级材料的 family（Gemini 1.5 / 2.5 都有较完整 paper），加上 Project Mariner、Astra、Jules 等 agent 产品的 blog 披露，对 agent data / long-horizon trajectory / multimodal agent 的覆盖独特。

## 为什么重要（对本项目）

- 它是 closed-weights 阵营里少数有 paper-level material 的家族，可在 comparison 中扮演"半开放 frontier baseline"。
- Project Mariner（web agent）、Astra（multimodal real-time agent）、Jules（coding agent）是 frontier agent system 的另一组样本；与 OpenAI Operator / Anthropic Claude Code 三方对照。
- multimodal native + agent 组合是 Qwen3.5 native multimodal 的天然 frontier 对比对象。

## Family Lineup

- Gemini 1.5（Pro / Flash）—— long-context、multimodal 起点。
- Gemini 2.0（Flash）—— Astra、Mariner 早期演示。
- Gemini 2.5（Pro / Flash / Flash-Lite, Deep Think）—— TR 级材料；agent eval 较系统。
- Gemini 3（Pro/Flash 等，2026）—— 需在 release-delta 里跟踪。
- Agent 产品：Project Mariner、Astra、Jules、Gemini CLI / Gemini Code。

## 已知公开材料

- **TR-like papers**：Gemini 1.5 paper、Gemini 2.5 paper（含 long context / agent eval / Deep Think 段落）。
- **System / model card**：每代 Gemini 都有 model card 或 safety report。
- **Agent product blog**：Mariner、Astra、Jules、Gemini CLI 的 DeepMind / Google blog post。

## Source Bundle

见 `source-bundle.md`。

## 收录策略

- family 级目录 + release-delta 文件。
- 优先级：
  1. `release-deltas/gemini-2.5.md` —— TR 级材料 + agent eval anchor，是当前最有内容的 release。
  2. `release-deltas/gemini-3.md` —— 当前主线，需要持续跟踪。
  3. `release-deltas/project-mariner.md` —— web agent，agent data 视角主源之一。
  4. `release-deltas/astra.md`、`release-deltas/jules.md` —— 视信息量决定。
- Gemini 2.5 如果 TR 信息量够（与 DeepSeek V4 / Qwen3 量级），后续可以从 release-delta 升级为独立 dossier `sources/gemini-2.5/`，但**默认先放在 family 下**。

## Caveats

- Gemini paper 信息量在 frontier closed-weights 里算多的，但仍远低于 DeepSeek / Qwen TR；不要把 paper 长度当作 disclosure 完整度。
- multimodal / agent 评测 setup 频繁变；引用具体数字要带 evaluation date snapshot。
- "Project ..." 类产品命名有时不对应真实 model checkpoint；区分 demo / GA / API 三个状态。
