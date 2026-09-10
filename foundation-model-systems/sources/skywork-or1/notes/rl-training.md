# Skywork-OR1 RL Training

```yaml
---
source_id: skywork-or1
section_type: rl-training
stage: post-training
substage: rl-training
depth: deep
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- MAGIC 是一组协同控制，而不是单个 objective：data filtering、rejection sampling、context curriculum、temperature、policy freshness、entropy floor 与 KL choice 会相互作用。[7-18]
- 模型从 DeepSeek-R1-Distill-Qwen checkpoints 开始，因此实验衡量的是“如何继续强化已有 long-CoT policy”，不是从 base 涌现 reasoning。[35-37]
- Multi-stage training 逐步扩大 context length，在早期节省 compute，同时为后期长解答保留训练路径。[8-16, 36]
- 最终 recipe 不使用 KL loss，因为消融中 KL constraint 限制了后期提升。[16-18]

## Why It Matters

Skywork 表明 stable long-CoT RL 是一个 control-system problem。只比较 optimizer 公式而忽略 task pass rate、truncation、temperature 与 rollout freshness，会得到误导性结论。

## Mechanism Sketch

1. 筛选 verifiable、非平凡的 math/code prompts。
2. 做 offline difficulty filtering 与 online rejection sampling。
3. 从较短 context 开始，分阶段扩大。
4. 使用 temperature 1 保持 exploration。
5. 使用 on-policy rollout/update，并限制 reuse。
6. 只在 entropy 低于 target floor 时启用 adaptive entropy control。
7. 不使用 KL，并同时监控 held-out performance，而不是只看 train reward。[7-18]

## Details / Evidence

- All-correct/all-wrong groups 没有相对 advantage，因此会被 rejection sampling 删除。[7]
- 最终 recipe 没使用 truncated-response advantage mask；消融显示 masking 并没有如预期解决 noisy signal。[11-14]
- High-temperature sampling 早期可能更差，但最终表现更好，说明不能根据短 run 过早 early stop。[14-16]
- 不同 variant 使用不同 context/group schedule，不应把整个 family 压成一个虚构的统一 config。[35-36]

## Gaps / Open Questions

- 组件之间的 interaction ablation 没覆盖完整组合空间。
- 结果可能依赖 distilled base 已有的 entropy 与 reasoning style。
- General assistant regression 与 safety 不是主要训练 gate。

## Lookup-only

- Stage steps、context、batch/group size：第 36 页。
- Learning rate、clip、target entropy、sampling settings：第 35-36 页。

## Evidence Anchors

- 7-18：MAGIC 与 component ablations。
- 35-37：最终配置与 evaluation。
