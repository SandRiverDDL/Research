# Ling / Ring 2.6 RL Infrastructure

```yaml
---
source_id: ling-ring-2.6
section_type: infra
stage: infra
substage: none
depth: deep
confidence: high
need_expert_review: true
---
```

## Core Design / Innovation

- KPop 认为 training-inference mismatch 与 token probability 有关：固定 ratio bound 会过度 mask 低概率 token，因此改用 sampled-token vs remaining mass 的 symmetric binary KL。[18-19]
- ARouter 优化的是 rollout step completion time，而不是单请求 latency；它迁移 tail requests，并把残余 rollout 与 training overlap。[28-29]
- Partial-rollout asynchronous RL 使用全局 token budget，持久化未完成 trajectory，并限制 policy staleness，而不是等待最慢样本。[30-31]
- 数值一致性被显式处理：optimizer master weights、FP32 LM head，以及按 module 选择 FP8/BF16。[29]

## Why It Matters

Agentic RL 的吞吐由 tail latency 与 environment wait 决定，不只是 tokens/sec。Infrastructure 会改变哪些 trajectories 被纳入训练、它们有多 stale、哪些 tokens 被 mask，因此它是 optimization method 的一部分。

## Mechanism Sketch

1. ARouter 持续分发 rollout。
2. 迁移 straggler，或把它们 spill 到独立 inference group。
3. 达到全局 generated-token budget 后形成一个 optimization batch。
4. 把未完成 rollout 连同 version/KV-cache metadata 持久化。
5. Bounded-staleness manager 决定接纳或丢弃 segments。
6. Sandbox/tool backends 计算 reward。
7. 对 train/infer probability 偏差过大的 token 应用 KPop mask。[18-19, 28-31]

## Details / Evidence

- ASystem 分离 control flow 与 data flow，并允许替换 training、inference、reward backends。[28]
- Agent 通过标准 chat API 发起调用；proxy 记录交互并构建 trajectory tree。[29-30]
- Individual mode 只训练当前 turn；concat mode 用 terminal reward 训练完整 trajectory。系统还能抽取 main chain，并控制 exploration branches 是否参与训练。[30]

## Gaps / Open Questions

- `need_expert_review`：真正实现前，需要用代码核对 KPop 与 partial rollout 的交互。
- Staleness threshold、bias correction 与 discarded-token rate 没有给出可迁移的完整配置。
- Throughput/reward gain 与具体 hardware/topology 强相关，不能直接外推。

## Lookup-only

- Throughput speedup、FP8 配置与 max-staleness mechanics：第 28-31 页。

## Evidence Anchors

- 18-19：KPop objective。
- 28-31：ASystem、ARouter、FP8 alignment 与 asynchronous RL。
