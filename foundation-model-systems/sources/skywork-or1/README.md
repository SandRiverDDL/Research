# Skywork Open Reasoner 1 Source Dossier

```yaml
---
source_id: skywork-or1
source_type: open-project
org: Skywork AI
release_date: 2025-05-29
priority: A
status: section-notes
openness: fully-open
confidence: high
lineage: skywork-open-reasoner
role: full-tr
base_source: deepseek-r1-distill-qwen
---
```

## 一句话

Skywork-OR1 是 math/code long-CoT RL 的高开放 recipe：从 DeepSeek-R1-Distill-Qwen 起步，以 MAGIC 组合 model-aware data filtering、multi-stage context curriculum、on-policy updates、high-temperature sampling、no-KL training 与 adaptive entropy control，并对 entropy collapse 和 verifier/sandbox failure 做了大量消融。[7-37]

## 为什么重要

- 它不是 pure-RL-from-base；它回答的是怎样继续用 RL 强化已经会 reasoning 的 distilled policy。
- 最有研究价值的不是发布分数，而是 entropy collapse、on-policy freshness、rollout resource allocation 和 data/verifier quality 的系统消融。
- 模型、训练数据和代码开放，适合作为 Open-Reasoner-Zero 的互补 recipe。

## 核心机制 / Takeaways

- MAGIC：离线/在线筛选、rejection sampling、多阶段 context、截断处理、high-temperature rollout、on-policy training、adaptive entropy control、no KL。[7-18]
- 数据按 verifiable/correct/challenging 三层筛选，并用当前 base model 的 rollout pass rate 删除全对/全错问题。[31-33]
- Adaptive entropy control 只在 entropy 低于 target 时施加控制，目标是防止 premature collapse 而不是无条件提高随机性。[16-18, 24-26]
- On-policy updates 比重复复用 rollout 更能避免 entropy collapse；增加 rollout batch/group size 通常比增加同一数据上的 SGD reuse 更有效。[18-30]
- Math verifier 和 code sandbox 自身会产生 false positive/negative、hang、memory leak，因此被当作 recipe 一部分审计。[34-35]

## Source Bundle

- technical report: https://arxiv.org/abs/2505.22312
- repository: https://github.com/SkyworkAI/Skywork-OR1
- training data: https://huggingface.co/datasets/Skywork/Skywork-OR1-RL-Data
- local PDF: `/Users/chy/Research/foundation-model-systems/papers/skywork-or1/skywork-or1.pdf`
- last checked: 2026-07-21

## Lineage / Delta

- base：DeepSeek-R1-Distill-Qwen-7B/32B。
- role：post-distillation RL recipe，不是 R1-Zero reproduction。
- variants：Math-7B、7B、32B 共享 framework，但使用不同 mixture/context schedule。

## 最大证据缺口

- 结论集中在 math/code，尚不能代表 general/agentic RL。
- Adaptive entropy control 与特定 batch/learning-rate/config 耦合，跨框架迁移需重做控制实验。
- Fully-open artifacts 仍继承不透明的 DeepSeek-R1 teacher traces和 Qwen pretraining。

## Lens Hooks

- RL 训练：entropy collapse、on-policy freshness 与 context curriculum。
- data：model-aware difficulty 与 human/LLM quality filtering。
- reward-verifier：parser 与 sandbox reliability。
- infra：rollout budget 与 SGD reuse 的取舍。

## 阅读入口

- `section-index.md`: MAGIC、entropy、data/verifier 的页码地图。
- `notes/rl-training.md`: MAGIC 主流程。
- `notes/entropy-control.md`: entropy collapse 证据。
- `notes/data-verifier.md`: 数据和 verifier。
- `notes/claims-and-gaps.md`: 可迁移边界。
