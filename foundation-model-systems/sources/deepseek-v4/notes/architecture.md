# DeepSeek-V4 Architecture

```yaml
---
source_id: deepseek-v4
section_type: architecture
stage: architecture
substage: none
depth: working
confidence: medium
need_expert_review: true
---
```

## Scope / Coverage

- 覆盖页段：TR page 1, pages 4, 6-14, 24-26。
- 覆盖阶段：architecture overview、long-context attention、MoE setup、optimizer、training schedule、MoE stability。
- 子问题：
  - V4 的核心 architecture novelty 是什么？
  - 这些选择如何改变 long context / test-time scaling 的成本结构？
  - 哪些参数和超参是 lookup facts，哪些是值得内化的 design principle？

## Core Summary

- 事实：DeepSeek-V4 有两个 MoE 版本：V4-Pro 是 1.6T total / 49B active parameters，V4-Flash 是 284B total / 13B active parameters；两者都声称支持 1M-token context。[1]
- 事实：V4 保留 Transformer / MTP / DeepSeekMoE 路线，但新增 Manifold-Constrained Hyper-Connections (mHC)、hybrid CSA/HCA attention、Muon optimizer。[6-7]
- 事实：Hybrid CSA/HCA attention 是主要 architecture novelty；报告称 V4-Pro 在 1M context 下只需要 DeepSeek-V3.2 的 27% single-token inference FLOPs 和 10% KV cache。[9-14]
- 解释：V4 应该被读成 efficiency-first frontier system，而不是单纯 scale-up；核心赌注是降低 long-context economics 后，test-time reasoning 和 agentic workflows 才能进入新 regime。[1, 4, 13-14]
- 解释：model hyperparameters 和 layer/expert counts 有记录价值，但大多是 lookup facts，不需要背。[24-26]

## Stage Flow / Mechanism Map

### Long-context Motivation

- 报告把 V4 的核心定位放在 long-context / test-time-scaling architecture upgrade 上；降低 long-sequence attention cost 被视为 long-horizon tasks 和未来 online-learning-like paradigms 的瓶颈。[1, 4]
- 解释：这和 post-training 直接相关，因为 persistent reasoning/tool traces、million-token rollouts、OPD/RL data 都依赖长上下文成本能被压低。

### MoE Backbone

- MoE 主体仍是 DeepSeekMoE，包含 fine-grained routed experts 和 shared experts。[7]
- 相对 V3 的变化包括 routing affinity activation 改为 `Sqrt(Softplus)`、加入 slight sequence-wise balance loss、移除 routing target-node 约束、在初始 MoE layers 使用 Hash routing。[7]
- V4-Pro 有 61 layers、hidden size 7168、每个 MoE layer 384 routed experts、每 token 激活 6 个 experts；V4-Flash 有 43 layers、hidden size 4096、256 routed experts、每 token 激活 6 个 experts。[24-26]

### Hybrid CSA/HCA Attention

- CSA 先沿 sequence length 压缩 KV entries，再做 sparse attention；HCA 做更重的 KV compression，不做 sparse selection；两者都加 sliding-window branch 保留局部依赖。[9-13]
- V4-Pro 前两层 HCA，之后 interleaved CSA/HCA。[24-26]
- 解释：CSA/HCA 不是简单“context length 变长”，而是改变保存和查询长历史的成本结构，后续 comparison 里应作为 architecture lens 的核心。[9-13]

### Optimizer / Training Schedule / Stability

- Muon 用于大多数 trainable matrices；AdamW 保留给 embeddings、prediction head、mHC static biases/gates 和 RMSNorm weights。[14]
- Pretraining 从 4K context 开始，逐步扩到 16K、64K、1M。Sparse attention 在初始 dense-attention 阶段和 CSA indexer warmup 后引入。[25-26]
- 报告明确指出 trillion-parameter MoE 训练有 instability，并把 spike 归因到 MoE outliers / routing；mitigation tricks 是 Anticipatory Routing 和 SwiGLU clamping。[26]

## Gaps / Open Questions

- 报告里的收益有多少来自 architecture，多少来自 32T+ pretraining tokens，多少来自 post-training OPD，没有被拆开。
- CSA/HCA 是否会损失某些需要 early-token fine-grained details 的任务信息，需要更多任务级证据。
- Anticipatory Routing 是否能用于 DeepSeek MoE/infrastructure stack 之外，不清楚。
- 如果没有 released kernels 和 serving stack，efficiency claims 能复现到什么程度，不清楚。

## Transfer Hooks

- worth-internalizing: 先降低 attention/KV cost，再谈 long-horizon reasoning scaling；architecture 和 post-training infra 是耦合的。
- try-at-small-scale: 可以先验证“压缩长历史 + 保留局部窗口”的设计原则，而不是复刻 CSA/HCA 全实现。
- lookup-only: exact layer counts、expert counts、optimizer assignment、context extension schedule 和 FLOPs/KV 数字。

## Split Check

- current scope: architecture + training setup 的第一轮 working note。
- if this file grows beyond ~220 lines, split by: long-context attention vs MoE/training stability。

## Evidence Anchors

- 1: abstract、model size、1M context、FLOPs/KV reduction claims。
- 4: long-context test-time scaling motivation。
- 6-7: overall architecture 和 V3 inheritance。
- 9-13: CSA/HCA details。
- 14: Muon optimizer。
- 24-26: model/training setups 和 MoE stability tricks。
