# Kimi K2.5 Post-training Summary

```yaml
---
source_id: kimi-k2.5
stage: post-training
summary_role: current-practice
priority_for_post_training: S
confidence: high
---
```

## Verdict

Kimi K2.5 的独特点是把 multimodal capability、reasoning RL 与 agent swarm training 连起来：视觉对齐在 joint pretraining 建立，SFT 可以只用 text traces，之后 joint text/vision RL 激活能力；PARL 则只训练 orchestrator 学会何时并行调用 frozen subagents。[2-8, 14-15]

## Pipeline

```text
early low-ratio joint text/vision pretraining
-> text-only reasoning / instruction SFT
-> joint text + vision RL
-> token-level ratio clipping/masking
-> PARL training of swarm orchestrator over frozen subagents
```

- Zero-vision SFT 是反直觉设计：不使用人工视觉 reasoning trajectories，以避免其分布质量不足破坏 pretraining alignment。[3-4]
- Joint multimodal RL 同时覆盖 text/vision tasks；报告称部分 text benchmark 也受益，说明视觉任务可能提供额外结构化 reasoning signal。[2-4]

## Core Mechanisms

### Token-efficient RL

- Objective 采用 token-level log-ratio clipping/masking：超出安全 ratio 区间的 token 梯度置零，而非对完整 response 使用标准 PPO surrogate。[8]
- 目标是减少极端 off-policy tokens 对长 reasoning trajectory 的不稳定影响；它更像 selective gradient mask。

### Agent Swarm / PARL

- Orchestrator 是 trainable policy，subagents frozen；reward 结合 task success、finish behavior 和 parallelism，使 orchestrator 学会拆任务、分配 bounded contexts 和汇总结果。[4-6]
- Agent Swarm 被定位为 proactive context management：在主 context 溢出前并行分片，而不是事后压缩全部历史。[14-15]

### Multimodal Data Decision

- Early、低比例视觉融合优于 late/high-ratio；SFT 阶段是否继续加视觉数据不是“越多越好”，取决于 trajectory quality 与 modality alignment。[2-4]

## Failure Modes / Controls

- 人工视觉 CoT 的 distribution mismatch 可能伤害已建立对齐，因而采用 zero-vision SFT。
- Swarm 可能无意义地开 subagents、重复探索或增加延迟；parallel/finish reward 必须与 task success 联合设计。
- Frozen subagents 限制 credit assignment：orchestrator 只能改调度，不能修复 worker 固有错误。

## Openness and Evidence

- Open weights + full TR，核心 pipeline/机制可核查；data、environment、reward details 和完整训练代码未 fully open。
- K2.6 只有 release-level delta，不应替代 K2.5 作为 method anchor。

## Transfer to Current Work

- 做 `vision-SFT vs zero-vision-SFT` 对照时必须保证 base 已有可测的 multimodal alignment。
- PARL 最小实验应同时报告 success、subagent count、parallel wall time、total tokens 与 context-overflow rate。
- Token mask 方法需记录被 mask token 比例和位置，判断是否只是丢弃困难学习信号。

## Evidence Anchors

- [multimodal-training.md](multimodal-training.md): joint pretraining and zero-vision SFT pages 2-4。
- [rl-training.md](rl-training.md): pages 7-8。
- [agent-swarm.md](agent-swarm.md) 或 tool/agent note: pages 4-6, 14-15。
- [claims-and-gaps.md](claims-and-gaps.md): evidence boundary。
