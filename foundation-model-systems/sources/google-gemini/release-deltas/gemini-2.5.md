# Gemini 2.5 Release Delta

```yaml
---
delta_id: gemini-2.5
parent_source: google-gemini
release_date: 2025-03  # Pro 首次 announce；后续 Flash / Flash-Lite / Deep Think 陆续 GA
role: release-delta
confidence: medium-high
status: section-notes
openness: closed-weights
---
```

## 定位

Gemini 2.5 是 frontier closed 阵营**唯一**有 paper-level 材料的当代 release：覆盖 long context、multimodal、reasoning（含 Deep Think）、以及 agent 评测段落。它是 closed-weights 阵营里 §8 第二档证据中**证据强度最高**的样本，可作为"closed 阵营到底能披露多少"的上限参考。

## 关键 release（lineup）

- **Gemini 2.5 Pro** — 2025-03 首次 announce，paper 形式材料；reasoning + long context 旗舰。
- **Gemini 2.5 Flash / Flash-Lite** — 性价比层，与 Pro 共享 paper 框架。
- **Gemini 2.5 Deep Think** — extended reasoning 模式，paper / blog 都有专门段落。
- **Project Mariner（基于 2.5）** — browser agent 演示 / 评测，是 paper 中 agent 部分的产品对应。

## 公开材料范围

- **Gemini 2.5 paper / TR**：arxiv 上有 paper（具体 ID 在 stage notes 时核对，不在此文件硬写以防记错），含 architecture framing、long context eval、agent task eval（含 Mariner-style web task）、Deep Think。
- **Model cards / system cards**：Pro / Flash / Flash-Lite 各自有 model card。
- **DeepMind blog**：发布、Deep Think 模式、Mariner 演示文章。
- **API docs**：Gemini API 在 ai.google.dev 上有 long context、tool use、多模态调用细节。

具体 URL / arxiv ID / 页码 anchor 留到 stage notes 引用时核对。

## Agent data 视角的可用信号

> confidence: medium-high（相对 §8 其他 closed 样本），因为有 paper-level 段落而不是单纯 blog framing。

- **Long-horizon web/agent eval（Mariner-style）**：paper 的 agent 段落给出**任务集 + 评测 setup**的描述，是 closed 阵营**唯一**有 paper page anchor 的 agent eval 公开材料。可作为 OpenAI Operator system card / Anthropic Claude 4.5 Computer Use 的对照样本。
- **Long context + multimodal 联合 eval**：paper 给了 long context 在 audio / video / 大码库等模态下的 needle-in-haystack 类评测，间接说明 trajectory / context 数据可能在训练时混合长序列与 multimodal token。但**具体合成 pipeline 仍未公开**。
- **Deep Think 模式**：paper / blog 把 extended reasoning 当独立模式公开，包括"切换 cost"和能力提升的对照。这是与 Qwen3 thinking-mode-fusion / Qwen3.6 Thinking Preservation 的 frontier 对照样本——前者是开源公开机制，Gemini 是 closed 但有 paper anchor。
- **Tool use / function calling 集成**：API docs 暴露了 tool schema + parallel function calling 的产品形态，与训练时 tool-use trajectory 的组织方式存在间接联系。

## 不能从 Gemini 2.5 推出的事

- **训练数据规模 / mixture / agent trajectory 合成**：paper 在 data 层披露**远低于** Qwen3 / DeepSeek V4 / MiniMax M2 这一档；不要把"有 paper"等同于"披露到 TR 程度"。
- **verifier / reward design / RL recipe**：零公开。
- **Mariner trajectory 来源**：paper 在 eval 部分有任务描述，但训练 trajectory 是否使用 Mariner-style 数据、合成方式如何——未公开。
- **Deep Think 训练 vs inference scaffolding**：paper 没明说 Deep Think 是独立 fine-tune、混合训练还是纯 inference-time 机制。

## 与本项目其他 source 的横向对照（待 lens 沉淀）

- vs **OpenAI Operator system card**：Operator 给 browser agent 评测 setup 详细但无 paper；Gemini 2.5 paper 给了 Mariner 评测的 paper anchor 但任务集详细度不及 Operator → 两者在 closed 阵营 GUI agent 评测上各占优势。
- vs **Qwen3 thinking-mode-fusion**：Qwen3 在开源 TR 里把 thinking / non-thinking 双模融合机制讲到训练流程层；Gemini 2.5 Deep Think 是 closed 阵营对应物，但 paper 只到机制 framing + capability claim，没到训练 recipe。
- vs **Anthropic Computer Use / Claude 4.5**：Anthropic 公开 product 设计 + system card eval；Gemini 2.5 公开 paper-level eval + DeepMind blog product framing → frontier closed 阵营两种 disclosure 风格的样本。

## Source

- 引用必须落到具体 paper 页码 / blog URL / model card 字段，标签遵循 `sources/google-gemini/source-bundle.md`：`[paper-gemini-2.5]`、`[blog-dm-...]`、`[model-card-2.5-pro]`、`[api-docs]`。
- stage notes 升级时按以下顺序锚定：
  1. Gemini 2.5 paper（agent eval / long context / Deep Think 段落）
  2. Pro / Flash model cards（capability tier / context length）
  3. Mariner / Astra blog（agent product framing）
  4. Deep Think blog（extended reasoning 模式）
  5. API docs（tool use schema）

## 升级 trigger

- **可考虑**升级为独立 dossier `sources/gemini-2.5/`：因为 paper-level 信息量与本项目第一档 TR 样本（DeepSeek V4 / Qwen3 / Kimi K2.5）有可比性。但**默认**先维持在 family release-delta 形式；只有出现 ≥3 个 stage notes 的内容时再独立。
- 不需要为 Pro / Flash / Flash-Lite 各自单独 release-delta；它们共用 paper 框架，差异在 capability tier 不在训练 recipe。

## Caveats

- closed-weights、paper 信息密度有限：paper 不等于 TR，不要按 Qwen3 / DeepSeek V4 那种 35 页 TR 的标准引用 Gemini 2.5。
- arxiv ID / 页码必须在 stage notes 时实际打开核对；不要从记忆中写 ID。
- "Deep Think 提升 X%"这种数字是 capability eval 不是 training recipe；引用时区分 evaluation domain 和训练设计。
- Mariner 在 paper 里以 eval 形态出现，在 blog 里以 product 形态出现，引用时区分两个 framing。
