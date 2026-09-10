# Nemotron-Cascade 2 Cascade RL

```yaml
---
source_id: nemotron-cascade-2
section_type: rl-training
stage: post-training
substage: cascade-rl
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- Cascade RL 的核心是按 domain 顺序训练，而不是把所有 RL data 混进一个统一 stage；这样能针对每个 domain 调 response length、verifier cost、reward 和 hyperparameters。[10-12]
- 完整顺序是 IF-RL -> multi-domain RL -> MOPD -> RLHF -> long-context RL -> code RL -> SWE RL。[10]
- 它坚持 strict on-policy GRPO：每个 iteration 从当前 policy 采样 group rollouts，只做一次 gradient update，让采样 policy 和更新 policy 匹配。[11]
- 他们把 KL divergence term 移除，entropy loss coefficient 也常设为 0；这使 objective 更接近 group-normalized REINFORCE + token-level loss。[11-12]
- Multi-domain RL 只在 response length 和 verification cost 相近、且没有明显 cross-task interference 时合并训练；这是很实用的 domain grouping 标准。[12]

## Why It Matters

Cascade 2 的价值在于它把“RL 顺序”当成 recipe 本体。很多后训练失败不是因为 GRPO 不会写，而是 domain 混合、verifier latency、response length、reward sparsity 和 forgetting 没处理好。Cascade RL 给了一套可操作的组织原则。

## Mechanism Sketch

1. SFT 建基础能力和 chat template。
2. IF-RL 先补 instruction adherence，后续阶段再恢复人类偏好能力。
3. Multi-domain RL 合并 MCQA、agentic tool calling、structured output，因为它们 response / verification cost 相近。
4. MOPD 用 intermediate best teachers 做能力合并/回归修复。
5. RLHF 改善 human preference / creative writing / non-verifiable tasks。
6. Long-context、Code、SWE RL 单独放后面，因为它们长序列/环境成本高，混训会拖慢或干扰其他 domains。

## Details / Evidence

- IF-RL 使用 batch 128、每 prompt 16 responses、temperature/top-p 1.0，约 180 steps。[12, 25]
- Multi-domain RL mixture 约 55% MCQA、30% agentic tool calling、15% structured output；合并原因是任务没有明显互相伤害，且 response length / verification time 相近。[12]
- Long-context RL 单独训练，因为和其他 domains 混合会影响 unrelated benchmarks；input 限 32K，max sequence 49K。[15]
- SWE RL 放最后，因为 rollout 慢、context 长、环境复杂；这与 MiMo/Qwen 的 agentic coding训练瓶颈一致。[15-16]

## Gaps / Open Questions

- Domain ordering 是经验规则，缺少系统 search / ablation。
- Reward/verifier 具体实现仍分散在 appendix / datasets / repo，第一版 notes 未完全审计。
- Strict on-policy 单次 update 的计算效率和 sample efficiency tradeoff 需要和 GLM/verl/slime 类异步框架对比。

## Lookup-only

- Table 8/9: IF-RL、multi-domain RL、MOPD、RLHF、long-context RL、Code RL hyperparameters。[25]

## Evidence Anchors

- 10-12: Cascade RL stage order and GRPO configuration。
- 14-16: RLHF / long-context / code / SWE RL。
- 25-26: hyperparameters。
