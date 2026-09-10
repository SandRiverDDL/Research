# Kimi K2.5 RL Training

```yaml
---
source_id: kimi-k2.5
section_type: stage-note
stage: rl-training
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Kimi K2.5 的 RL 不只是 reasoning RL，而是 text、vision、agent、computer-use 一起优化的 joint RL。
- Token-level clipping/masking 是重要稳定性机制：按 log-ratio 判断 token 是否在区间内，区间外 token 梯度置零。[8]
- Reward system 是混合的：verifiable tasks 用 rule/outcome reward，general tasks 用 GRM，不同 visual tasks 用 F1、IoU、edit distance、counting、LLM verifier 等任务奖励。[8-9]
- Token Efficient RL 用 Toggle 在 budget-limited phase 和 standard scaling phase 间切换，目标是减少输出长度而不损失推理质量。[9]

## Why It Matters

Kimi K2.5 的后训练提醒：多模态 agent 模型的 RL reward 必须任务特化，不能靠单一 judge 覆盖全部任务。另一个重点是 token efficiency，2026 的 reasoning model 不只追求答对，还要控制推理预算。

## Mechanism Sketch

1. SFT 先用 K2/K2 Thinking/proprietary expert model 生成候选，再做人类标注、prompt engineering 和 multi-stage verification。
2. RL 对 text / vision / agent tasks 使用不同 reward source。
3. 对 token log-ratio 超出 clipping interval 的位置 mask gradient，抑制极端 policy shift。
4. Token Efficient RL 交替施加 budget pressure 和标准能力 scaling，减少冗长输出。

## Details / Evidence

- SFT 数据优先 interactive reasoning 和 precise tool-calling，并通过多模型候选、人类标注和 verification 构建。[8]
- GRMs 为 chat、coding agents、search agents、artifact-generating agents 等不同任务设计 rubrics，用多 rubric 降低 reward hacking。[9]
- Token Efficient RL 报告可减少 25-30% output tokens，同时尽量保持性能。[9]
- DEP multimodal infra 将 vision encoder 计算从 backbone pipeline 解耦，使多模态训练效率接近 text-only training 的 90%。[9-10]

## Gaps / Open Questions

- Token-level masking 的区间、loss 形式、advantage 处理和与 PPO/GRPO 的关系需要更细数学审计。
- GRM 训练数据、rubric 质量和 reward hacking 防御细节未充分公开。

## Lookup-only

- 具体 benchmark/token count table 回查 `[12-13]`。
- DEP 训练效率细节回查 `[9-10]`。

## Evidence Anchors

- 8-10: SFT, RL objective, rewards, token-efficient RL, DEP.
