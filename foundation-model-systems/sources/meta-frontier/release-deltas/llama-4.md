# Llama 4 Release Delta

```yaml
---
delta_id: llama-4
parent_source: meta-frontier
release_date: 2025-04
role: lineage-reference
confidence: medium
status: stub
openness: open-weights-partial
---
```

## 定位

Llama 4 是 Meta 2025-04 推出的第一代 frontier MoE 系列（Maverick / Scout / Behemoth）。发布后被广泛视为 frontier 落后一档，本文件作为 **lineage-reference + behind-frontier 样本**保留，不进入 current-practice 横向总结。

## 关键 release（lineup）

- **Llama 4 Maverick** — MoE，主打通用 chat。
- **Llama 4 Scout** — 长 context 主打（claim 10M context）。
- **Llama 4 Behemoth** — 旗舰，未正式 GA，训练过程外界报道有问题。

## 公开 / 半公开信号

- **架构**：MoE 设计；具体 expert 拓扑、routing、激活比 在 model card 有部分披露但不完整。
- **长 context**：Scout claim 10M context；多个独立第三方在常见 long-context eval 上无法复现宣称水平。
- **agent / tool use**：blog 提了 multimodal + tool calling，但没给训练 pipeline 或 trajectory data 的细节。
- **benchmark gaming 风波**：发布后 LMSYS / 独立 eval 与 Meta 自报 benchmark 出现明显口径分歧；后续 Meta 调整对外口径。
- **Behemoth 训练问题**：多次推迟，Meta 自己 blog 措辞从 "coming soon" 退到 "still training"。

## Agent data 视角的能用之处

- **基本没有**。Llama 4 model card 在 agent / trajectory data / verifier / RL 上披露程度低于 Qwen3 / GLM-5 / DeepSeek V4 / Kimi K2 这一档；不要把它当 agent-data current-practice 引用。
- 唯一可写进 lens / comparison 的：作为"frontier 阵营 disclosure 下限"的样本——同样 frontier 级模型，公开材料密度可以从 Qwen3 那种 35-page TR 一直退到 Llama 4 这种 blog + 残缺 model card。

## Source

- Release blog: https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- Model card / repo: https://github.com/meta-llama/llama-models
- 第三方独立 eval / 长 context 复现：进 stage notes 时再补具体 URL。

## 升级 trigger

- 一般情况下**不升级**；它的研究价值已经覆盖完。
- 例外：Meta 后续若公开 Llama 4 训练失败的 post-mortem 或详细 architecture / data pipeline，可升级到 stage notes 用作 frontier failure case study。

## Caveats

- 任何 benchmark / long-context claim 必须配第三方独立 eval anchor，不能只引 Meta blog。
- 不要拿 Llama 4 数字进 frontier comparison 主线；只能作为"behind-frontier disclosure floor"参考。
- "10M context" 这种宣称数字本身要带 quote 和复现状态，不要复述成 fact。
