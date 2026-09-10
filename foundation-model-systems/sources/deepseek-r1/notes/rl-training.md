# DeepSeek-R1 RL Training

```yaml
---
source_id: deepseek-r1
section_type: rl-training
stage: post-training
substage: rl-training
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- R1-Zero 回答一个相对干净的问题：强 base model 能否在没有 SFT warm start 的情况下，仅靠可验证 outcome RL 学会更长、更有效的 reasoning 行为。[2-5]
- DeepSeek 使用 GRPO 省去独立 critic：对同一问题采样一组回答，再用组内 reward 归一化得到 advantage。[2-3]
- R1 不是简单的“R1-Zero 再多跑一些 RL”；它在两段 RL 之间插入 supervised behavior repair，使 reasoning 能力与可读性、通用 assistant 行为重新整合。[6-8]

## Why It Matters

可迁移的核心是把 capability discovery 与 productization 分开。限制较少的 pure-RL run 用来探测 base policy 能自行发现什么；最终 assistant 还需要专门的数据与 reward 修复语言一致性、可读性、helpfulness 和 safety。

## Mechanism Sketch

1. 从 DeepSeek-V3-Base 开始。
2. R1-Zero：分组 rollout -> accuracy/format reward -> GRPO 更新。
3. 观察正确率、response length 和 reflection-like 行为随训练变化。
4. R1 先用少量 long-CoT 做 cold-start SFT。
5. 使用 accuracy 与 language-consistency reward 做 reasoning RL。
6. 生成并过滤 reasoning traces，与 non-reasoning data 混合后再次 SFT。
7. 最后用可验证任务的 rule reward，加上 general task 的 preference/safety reward 做 all-scenario RL。[6-8]

## Details / Evidence

### R1-Zero

- GRPO 虽然没有 value model，但报告中的 objective 仍包含 clipping 和 reference-policy KL；后续论文所说的“GRPO”未必采用相同配置。[2-3]
- Rollout 使用很长的 generation budget，并周期性刷新 reference policy。这些实现细节会显著影响稳定性，不能只比较算法名称。[3]
- 正确率与回答长度同时增长，支持“模型学会使用更多 test-time compute”的解释，但没有单独证明长度增长本身就是性能原因。[4-5]

### R1 两段 RL

- Cold-start traces 先约束出更可读的 reasoning 形态，再开始第一段 RL。[6]
- Language-consistency reward 缓解中英文混杂，但报告也显示它带来轻微能力代价；它是行为约束，不是 reasoning verifier。[7-8]
- 最终 RL 中，可验证 reasoning 继续使用 rule reward；general prompts 才使用 learned helpfulness/safety reward。[6-8]

## Gaps / Open Questions

- Prompt mixture、各 domain 训练预算和 sampling distribution 披露不完整。
- R1-Zero 的效果多大程度依赖 DeepSeek-V3-Base 的预训练能力，报告无法隔离。
- Critic-free GRPO 是否优于 critic-based PPO 并没有定论，应与 Open-Reasoner-Zero、Skywork-OR1 对照。

## Lookup-only

- R1-Zero learning rate、KL、group size、max length、reference 更新周期：第 3 页。
- 第一段 R1 RL 的超参和 language reward：第 7-8 页。

## Evidence Anchors

- 2-5：R1-Zero objective、reward 与训练动态。
- 6-8：R1 multi-stage pipeline 与两段 RL。
