# MiMo-V2-Flash Architecture

```yaml
---
source_id: mimo-v2-flash
section_type: architecture
stage: architecture
substage: hybrid-swa-moe-mtp
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- MiMo-V2-Flash 是 309B total / 15B active 的 MoE 模型，目标不是最大能力，而是高速度 reasoning / coding / agentic foundation model。[1, 5-6]
- Architecture 采用 Hybrid SWA + Global Attention：48 layers 中 39 SWA、9 GA；每个 hybrid block 是 5 个 SWA blocks 加 1 个 GA block，window size 128。[5-6]
- 关键经验是 attention sink bias：没有 sink 的 128-window hybrid SWA 会掉质量，加入 sink 后能恢复甚至超过 all-GA baseline。[7-8]
- Lightweight MTP 同时服务训练和推理：训练中作为 multi-token prediction objective，推理中作为 native draft model 做 speculative decoding，也能缓解 RL rollout bottleneck。[9, 21-22]
- FP8 mixed precision 类似 DeepSeek-V3，但 attention output projection、embedding/head 保持 BF16，MoE router 保持 FP32 以维持稳定。[6]

## Why It Matters

MiMo 的 architecture 价值在于 speed-cost tradeoff。它用小 active params、SWA 稀疏局部注意力、MTP speculative decoding 来换部署和 RL rollout 效率。这和 GLM-5.2 的长上下文/serving co-design可以形成横向对比：两者都把模型结构和推理成本放在核心位置。

## Mechanism Sketch

1. 用 MoE 扩大 total params，但每 token 只激活 8/256 experts。
2. 用 Hybrid SWA/GA 降低长序列 attention 成本，同时保留周期性 global attention。
3. 给 SWA 加 attention sink bias，缓解短 window 对全局信息的破坏。
4. 用轻量 MTP block 预测多步 token，推理时作为 draft model 提升 decoding speed。

## Details / Evidence

- Table 1 给出主要配置：48 layers，SWA heads 64/8 Q/KV，GA heads 64/4 Q/KV，head dims QK/V 为 192/128，256 total experts、8 activated experts。[6]
- RoPE 只部分施加在 query/key 前 64 维。[6]
- Architecture ablation 显示 hybrid SWA without sink 在 general benchmarks 下降，with sink 后恢复；128 window 在 long-context/reasoning 上优于 512 window 和 all-GA 的部分设置。[7-8]
- MTP 被刻意设计得 lightweight，避免 draft model 自身成为推理瓶颈。[9]

## Gaps / Open Questions

- Hybrid SWA 的设计空间仍然有限；结论页也承认 architecture exploration preliminary。[22]
- Attention sink bias 的实现细节、不同 sink 参数化方式和长期训练稳定性没有深入披露。
- MTP 层数、训练 loss weight、draft/verify implementation 细节对质量和速度的 tradeoff 仍需看代码或补充材料。

## Lookup-only

- 309B total / 15B active。[1, 10]
- 39 SWA / 9 GA; window size 128。[5-6]
- MTP 3-layer speculative decoding 可以达到最高 3.6 accept length 和 2.6x speedup 的 headline claim。[1, 22]

## Evidence Anchors

- 5-6: architecture and config table。
- 7-8: hybrid SWA ablations。
- 9: MTP motivation/design。
- 21-22: MTP inference speed analysis。
