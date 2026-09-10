# Ling / Ring 2.6 Post-training

```yaml
---
source_id: ling-ring-2.6
section_type: rl-training
stage: post-training
substage: rl-training
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 该 family 主动把即时响应（Ling）与深度 reasoning/agent 行为（Ring）拆成两条 post-training 路线，而不是让一个 policy 同时硬扛 latency 与 deliberation 两个目标。[13-16]
- Ling 的核心目标是 capability per output token：在保持正确率和 instruction following 的同时，压缩不必要的程序性 reasoning。[14-15]
- Ring 把更多训练容量放到 environment-grounded long-horizon behavior，并接受更高的 inference cost。[15-19]

## Why It Matters

这是“产品目标决定后训练结构”的当前案例。Fast 与 thinking 不只是 inference switch；它们在 specialist、data 和 reward priority 上都不同，会影响 mixed-policy consolidation 与 eval 的设计。

## Mechanism Sketch

### Ling

1. 构建覆盖广泛的 SFT corpus。
2. 分别训练 reasoning/general specialists。
3. 演化并过滤 CoT 数据。
4. 优化 linguistic units，并蒸馏 shortest correct response。
5. 用 bidirectional preference alignment 平衡回答质量与 verbosity。[13-15]

### Ring

1. 从具备 function calling 的 cold-start model 开始。
2. 建立 coding、search 与 general tool-use environments。
3. 按有效性和当前 policy pass rate 过滤任务。
4. 运行 long-horizon environment RL。
5. 用 KPop 控制 training-inference mismatch。[15-19]

## Details / Evidence

- Evolutionary CoT 是数据改进过程，不只是采样更长的 trace。[14]
- Shortest-correct-response distillation 把 token budget 作为训练目标，而不是仅在 decoding 阶段截断。[14-15]
- Bidirectional preference alignment 试图避免 policy 单向滑向冗长 reasoning 或过度简短回答。[15]
- Ring trajectory 可以延伸到数百个 environment steps，因此 rollout system 本身进入了 learning recipe。[17-18]

## Gaps / Open Questions

- Specialist routing、consolidation 顺序与各 objective 权重披露不完整。
- Token-efficiency optimization 是否损害知识型回答中的必要展开仍不清楚；报告也把它列为限制。[33]
- Native multimodal agent training 仍是 future work，不能把 2.6 归为 fully multimodal agentic TR。

## Lookup-only

- Family size、SFT mixture 数字与 benchmark entries：第 13-26 页。

## Evidence Anchors

- 13-15：Ling post-training。
- 15-19：Ring data、agent RL 与 KPop。
- 33：限制与 future direction。
