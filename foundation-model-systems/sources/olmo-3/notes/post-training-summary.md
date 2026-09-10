# OLMo 3 Post-training Summary

```yaml
---
source_id: olmo-3
stage: post-training
summary_role: fully-open-anchor
priority_for_post_training: S
confidence: high
---
```

## Verdict

OLMo 3 的核心价值不是 frontier score，而是 fully-open model flow：base/midtrain/long-context、Think/Instruct、SFT/DPO/RLVR、RL-Zero、数据、代码、checkpoints、logs 与 eval/decontam tools 可以被联结起来研究。[1, 4-6, 63-64]

## Pipeline

```text
Dolma 3 Mix base pretraining
-> Dolmino reasoning/tool midtraining
-> Longmino long-context extension
-> branch A: Think (long reasoning + RLVR)
-> branch B: Instruct (short answers + function calling + preference alignment)
-> branch C: RL-Zero directly from base for causal study
```

- Think 与 Instruct 是不同产品目标，不强求统一：前者追求 test-time scaling，后者追求低延迟、function calling 和 concise behavior。[5-6]
- RL-Zero 从 base 直接做 RLVR，主要价值是隔离 SFT/cold-start 的影响，研究 base data 对 RL learnability 的贡献。[4, 6, 63-64]

## Core Mechanisms

### Open Model Flow

- 每阶段 checkpoint、实际训练 tokens、data pools、training/eval/decontam code 与 logs 公开，使研究者能定位能力在哪个阶段出现或退化。[1, 5]
- 这比只开放 final weights 更适合做 recipe ablation 和 regression diagnosis。

### SFT / DPO / RLVR Separation

- SFT 建 instruction/format behavior，DPO 调 preference，RLVR 拉可验证 reasoning；三者目标分开，便于测每阶段 marginal effect。
- Think/Instruct 分支允许直接观察 reasoning verbosity 与 general utility 的 tradeoff。

### Base-data to RL Link

- Midtraining 上采 reasoning、tool-use 与高质量 science/code，long-context extension 为后续 post-training 提供 prior；RL-Zero 用于验证哪些能力可从 base 被 reward 激活。

## Failure Modes / Controls

- Fully open 不代表 recipe 自动 SOTA；scale、teacher/reward quality 与数据预算不同，不能直接外推 frontier effectiveness。
- Public benchmark/decontam pipeline更透明，但仍需关注 benchmark-specific optimization。
- Think/Instruct 分支降低 interference，却增加两个 checkpoints 的维护与 downstream selection成本。

## Openness and Evidence

- 本批唯一明确的 fully-open auditability anchor；适合作为所有“开放 recipe”声明的参照系。
- 事实可追到 artifacts，而不仅是 TR claim，因而在因果分析上权重高于大多数 industrial sources。

## Transfer to Current Work

- 用 OLMo flow 设计最小可复现基线：固定 base，依次加入 SFT、DPO、RLVR并保存每阶段 checkpoint/log。
- 复现 RL-Zero 与 cold-start RL 的对照，重点看 sample efficiency、format stability 和 reward hacking。
- 将 decontam 与 eval harness版本固定为训练 artifact，避免后续无法解释分数变化。

## Evidence Anchors

- [post-training.md](post-training.md): Think/Instruct、SFT/DPO/RLVR。
- [post-training.md](post-training.md): RL-Zero pages 63-64 与 Think/Instruct flow。
- [pretraining-data.md](pretraining-data.md): Dolma/Dolmino/Longmino。
- [claims-and-gaps.md](claims-and-gaps.md): fully-open artifact coverage。
