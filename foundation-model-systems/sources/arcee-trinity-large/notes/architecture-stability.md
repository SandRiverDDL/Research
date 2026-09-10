# Arcee Trinity Large Architecture / Stability

```yaml
---
source_id: arcee-trinity-large
section_type: architecture
stage: architecture
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Trinity Large 是 400B total / 13B active sparse MoE，主线是高效大模型 + 稳定训练，而不是后训练能力展示。[1-2]
- Attention 使用 3:1 local/global pattern：三层 local SWA with RoPE 后接一层 global NoPE；同时使用 QK-Norm 和 gated attention。[5-6]
- MoE 使用 DeepSeekMoE-style routed/shared experts、sigmoid routing、expert bias top-k selection、sequence-wise auxiliary loss。[6-8]
- SMEBU 是最独立的稳定性贡献：把 sign-based expert-bias update 改成 tanh soft-clamped、magnitude-aware、带 momentum 的连续更新。[7]
- Depth-scaled sandwich norm 和宽度缩放初始化也服务于稳定训练。[8]

## Why It Matters

这份 TR 的价值在“MoE 训练稳定性 taste”：当模型规模、专家数和 Muon optimizer 放大后，router/expert load 的微小振荡可能变成训练风险。SMEBU 提供了一个具体、可比较的稳定控制点。

## Mechanism Sketch

1. Local layers 用 RoPE + SWA，global layers 不加位置编码。
2. Attention output 加 gated attention，降低 attention sinks 和大激活。
3. Router 用 sigmoid scores；选择 experts 时用 score + bias，但输出 gating 只用 router score。
4. SMEBU 计算每个 expert 的 normalized load violation，经 tanh soft-clamp 后居中，再用 momentum 平滑更新 expert bias。
5. 额外 sequence-wise load-balance loss 保证序列内部负载。

## Details / Evidence

- QK-Norm 的理由是 Muon 下 maximum attention logits 更需要稳定控制，GLM-4.5 也报告过类似观察。[5]
- SMEBU 的动机是标准 aux-loss-free sign update 永远是正负固定步长，接近最优时会 oscillate；tanh 允许更新收敛到 0，momentum 用于 damp noise。[7]
- 线性 unclamped update 初期降低 MaxVio 快，但后期不稳定，因此 bounded updates 被认为必要。[7]

## Gaps / Open Questions

- SMEBU 的 ablation、失败案例、对不同 expert 数/批大小的泛化需要更细读或复现。
- Gated attention 与 long-context extrapolation 的因果证据仍偏经验。

## Lookup-only

- SMEBU 的 `lambda/beta/kappa` 具体值按需查询。[7]
- Tokenizer 细节如 200k vocab、digit chunking 放 lookup。[2-4]

## Evidence Anchors

- 5-8: attention, MoE, SMEBU, norm/init.

