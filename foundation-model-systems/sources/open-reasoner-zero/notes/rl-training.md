# Open-Reasoner-Zero RL Training

```yaml
---
source_id: open-reasoner-zero
section_type: rl-training
stage: post-training
substage: rl-training
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 该 recipe 有意使用 vanilla PPO，而不是再发明一个新的 policy objective。[4-6]
- 在 terminal binary reward 且 `γ=λ=1` 时，token advantage 简化成 `R - V(s_t)`，不会对长 reasoning horizon 做指数衰减。[5-6]
- 不使用 KL loss 或 KL-shaped reward，使 policy 可以离开 base distribution，同时省去 reference model 的计算与显存。[6]
- 同一 recipe 从 0.5B 扩到 32B，但最终能力仍显著依赖 model scale。[3-9]

## Why It Matters

ORZ 是检验复杂 RL 算法“是否真有必要”的强 baseline。新方法至少应对比正确实现的 PPO：带 critic、long-horizon GAE、足够数据，并且不默认加 KL constraint。

## Mechanism Sketch

1. 用 current/old policy 为每个 prompt 采样一组回答。
2. 只在终局赋 binary correctness reward。
3. 训练 value model，从每个 token state 预测最终 return。
4. 使用 `γ=λ=1` 计算 GAE。
5. 同时优化 clipped PPO policy loss 与 value loss。
6. 直接从 base model 开始，不做 SFT，也不使用 reference-policy KL。[4-7, 20-21]

## Details / Evidence

- 较低 γ 会缩短 effective horizon，可能鼓励提前结束；报告中 λ<1 也产生较差的 reward/length dynamics。[5-8]
- 在 7B ablation 中，去掉 KL 后稳定性和 response-length scaling 更好，同时降低系统与调参成本。[6, 9]
- Inner epoch、policy freshness 与 batching 同样重要；仅说“使用 PPO”不足以复现。[17-21]

## Gaps / Open Questions

- 多 seed 方差，以及 critic 在 trillion-scale MoE 上的稳定性未知。
- No-KL 对 narrow verifiable reasoning 可能安全，但在 general assistant mixed-domain training 中可能造成行为漂移。
- 与 R1-Zero 的直接比较仍受 data、training steps 与 implementation 差异影响。

## Lookup-only

- PPO clip、batch/group size、sequence length 与 learning rate：第 17-19 页。
- 完整 pseudocode：第 20-21 页。

## Evidence Anchors

- 4-7：算法与设计原则。
- 8-10：关键消融。
- 20-21：实现 pseudocode。
