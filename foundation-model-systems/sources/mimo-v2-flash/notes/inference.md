# MiMo-V2-Flash Inference / Rollout Efficiency

```yaml
---
source_id: mimo-v2-flash
section_type: infra
stage: infra
substage: mtp-rollout-inference
depth: working
confidence: medium
need_expert_review: true
---
```

## Core Design / Innovation

- MTP 被复用为 native draft model 做 speculative decoding，不只是训练辅助目标；这让 MiMo 的 architecture 直接服务部署速度。[9, 21-22]
- TR 明确把 MTP 和 RL rollout 连接起来：rollout 是 RL 主要瓶颈，MTP 可以用 token-level parallelism 缓解 small-batch on-policy RL 的 GPU 利用率问题。[9]
- Request-level prefix cache 用于 RL rollout，复用同一 request 先前 turn 的 KVCache 和 MoE routed experts，同时避免跨 request output cache sharing 导致 sampling inconsistency。[20]
- Toolbox / Tool Manager 用 Ray 做工具资源调度、QPS/配额控制、environment pre-warming 和 sequence-level asynchronous reward computation。[21]

## Why It Matters

MiMo 把“推理加速”和“RL 训练吞吐”放在同一条线上看，这个 taste 很重要。对 agentic RL，rollout 不是附属环节，而是训练成本和可扩展性的核心瓶颈。MTP、prefix cache、tool resource manager 都是在让 on-policy / agentic RL 更可承受。

## Mechanism Sketch

1. Pretraining 中训练 MTP block。
2. Inference 时用 MTP 作为 draft model，主模型并行 verify 多个 draft tokens。
3. RL rollout 中，用 MTP 缓解长尾小 batch 的 GPU idle。
4. 多轮 agent request 中，用 request-level prefix cache 复用同一 request 历史 KV / routing。
5. Tool Manager / Toolbox 负责工具环境调度和异步 reward，降低 agentic training 的系统阻塞。

## Details / Evidence

- MTP 对 RL 的两点作用：让 small-batch on-policy RL 更实际；缓解 long-tail stragglers 在 rollout 末尾造成的 GPU idleness。[9]
- Figure 7 显示 next-token prediction entropy 和 average accept length 高相关，说明不同数据集/任务的 MTP 加速效果和 token uncertainty 相关。[21]
- Table 10 给出不同 batch size 和 accept length 下的 decoding speedup；结论是 speedup 大致随 accept length 线性增加。[22]
- Request-level prefix cache 不同于 radix cache，目标是避免 re-prefill 和 inter-request output cache sharing，同时保证 routed experts sampling consistency。[20]

## Gaps / Open Questions

- MTP speculative decoding 的 production implementation、verify kernel、batching details 没有完整披露。
- Request-level prefix cache 的一致性/性能 tradeoff 没有 ablation。
- Toolbox / Tool Manager 的 reward queue、failure handling、tool timeout、sandboxing 策略没有详细披露。

## Lookup-only

- Headline: 3 MTP layers, up to 3.6 accept length and 2.6x decoding speedup。[1, 22]
- Table 10 speedup grid。[22]
- Tool stack: Ray, Toolbox, Tool Manager。[21]

## Evidence Anchors

- 9: MTP for decoding and RL rollout。
- 20-21: request-level prefix cache and tool manager。
- 21-22: MTP accept length and speedup。
