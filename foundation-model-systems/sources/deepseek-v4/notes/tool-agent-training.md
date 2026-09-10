# DeepSeek-V4 Tool / Agent Training

```yaml
---
source_id: deepseek-v4
section_type: tool-agent-training
stage: post-training
substage: tool-agent-training
depth: working
confidence: medium
need_expert_review: false
---
```

## Scope / Coverage

- 覆盖页段：TR pages 30-36。
- 覆盖阶段：tool calling、reasoning trace management、agentic sandbox / rollout infrastructure。
- 子问题：
  - DeepSeek-V4 如何组织 tool calling interface？
  - tool-calling conversations 和 general conversation 的 reasoning trace 管理有什么不同？
  - DSec sandbox 和 rollout infra 是 training recipe 的一部分，还是 eval 附属品？

## Core Summary

- 事实：Tool calling 使用带 special token 的 `DSML` XML-like schema，动机是降低 escaping failures 和 tool-call errors。[30]
- 事实：工具调用场景跨 turn 保留完整 reasoning history；普通聊天在新 user message 到来时丢弃前序 reasoning。[31]
- 事实：Post-training infrastructure 包括 preemptible rollouts 的 token-granular WAL、million-token RL/OPD data 的 shared-memory dispatch。[34-35]
- 事实：DSec sandbox platform 支撑 agentic AI post-training and evaluation，包含 trajectory logging、preemption-safe resumption、provenance 和 deterministic replay。[35-36]
- 解释：DeepSeek 的 agentic recipe 不只是 RL objective；schema、trace retention、sandbox replay 和 long-context economics 共同决定 agentic training 是否可行。[30-36]

## Mechanism Map

### Tool Interface

- DSML 用 special tokens 包裹 XML-like schema，目标是减少 escaping failures 和 tool-call errors。[30]
- 解释：这是 product/training interface choice，不只是 prompt formatting；schema 稳定性会影响训练数据、rollout replay 和 eval parsing。

### Reasoning Trace Management

- Tool-calling conversations 跨 turn 保留完整 reasoning history；general conversation 在新 user message 到来时丢弃前序 reasoning。[31]
- 解释：retained tool reasoning traces 把 long-context architecture 和 agentic post-training 连起来；如果工具任务跨 turn 保留完整 history，attention/KV 成本会直接影响可行性。[31]

### Sandbox / Rollout Infrastructure

- Token-granular WAL 支持 preemptible rollouts；shared-memory dispatch 支持 million-token RL/OPD data。[34-35]
- DSec sandbox 提供 trajectory logging、preemption-safe resumption、provenance 和 deterministic replay。[35-36]
- 解释：这些不是单纯 eval 工具，而是 agentic training recipe 的基础设施，因为它们决定能否稳定收集、恢复、审计和 replay trajectories。[34-36]

## Gaps / Open Questions

- Tool-call training data 的规模和来源没有公开。
- DSec sandbox 的 task distribution、environment isolation 和 grading logic 没有完整公开。
- Retained reasoning traces 对性能和安全的 tradeoff 没有 ablation。
- Million-token rollout data path 和普通 open recipe 的可复现差距很大，迁移时需要降级设计。

## Transfer Hooks

- worth-internalizing: agentic capability 依赖 interface + trace policy + replayable environment，不只是 RL 算法。
- try-at-small-scale: 先复刻 tool schema、trajectory logging、deterministic replay、provenance，而不是复刻 million-token dispatch。
- lookup-only: DSec sandbox 的具体平台实现和 WAL / shared-memory dispatch 细节，除非写 infra lens。

## Split Check

- current scope: tool schema、trace management、sandbox / rollout infra。
- if this file grows beyond ~220 lines, split by: tool interface vs sandbox infrastructure。

## Evidence Anchors

- 30-31: DSML tool-call schema 和 interleaved thinking trace management。
- 34-36: post-training infra 和 DSec sandbox platform。
