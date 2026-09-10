# Nemotron-Cascade 2 Post-training Summary

```yaml
---
source_id: nemotron-cascade-2
stage: post-training
summary_role: open-recipe-anchor
priority_for_post_training: S
confidence: high
---
```

## Verdict

Nemotron-Cascade 2 是 18 个 source 中与实际 post-training 最直接的一条公开 pipeline：它把 strict on-policy GRPO、domain-wise Cascade RL、mid-pipeline MOPD、RLHF、long-context RL、code RL 和 SWE RL 按顺序组织，并释放 checkpoint 与 SFT/RL data collection。[1, 10-14]

## Pipeline

```text
SFT
-> instruction-following RL
-> multi-domain RL
-> MOPD over intermediate best teachers
-> RLHF
-> long-context RL
-> code RL
-> SWE RL
```

- Cascade 的核心不是增加阶段数量，而是避免一个大 mixture 同时混合 verifier cost、response length、task difficulty 和 domain curriculum。[10-12]
- 每个阶段可独立选择数据、reward、长度与 curriculum；MOPD 放在中段恢复前面已学能力，再继续后续 alignment/agentic stages。[10]

## Core Mechanisms

### Strict On-policy GRPO

- 每次从当前 policy 采 group rollouts，只执行一次 gradient update；importance ratio 视为 1，移除 KL term，接近 group-normalized REINFORCE/token loss。[11]
- 优点是 objective 与 rollout policy 一致、便于诊断；代价是 rollout 成本高，无法重复利用 trajectory。

### Cascade Scheduling

- Domain 顺序是显式 design variable。它承认 sequential RL 会遗忘，但认为分阶段控制比大 mixture 更容易调试。
- 关键评测不只是当前 stage improvement，还必须维护 all-domain regression matrix。

### MOPD Repair

- Intermediate best checkpoints 充当 teachers，给当前 student dense token-level distillation advantage；相比 sparse sequence reward，报告称达到目标所需 steps/samples 更少。[13-14]
- MOPD 不是最终压缩步骤，而是 cascade 中的 capability recovery / merge stage。

## Failure Modes / Controls

- Sequential ordering 可能造成 catastrophic forgetting；MOPD 与跨阶段 eval gate 是主要修复机制。
- Strict on-policy 提高数据新鲜度，但受 rollout吞吐和 tail latency 限制。
- 每个阶段的 reward/verifier 可被不同方式 game，不能把一个 domain 的 anti-hack 规则直接复用到全部阶段。

## Openness and Evidence

- 模型 checkpoint、SFT data 和 RL data collection 明确开放，开放程度高于普通 open-weight TR。
- 仍需核查完整 code/config/logs 是否覆盖所有阶段；“开放 data collection”不自动等于一键复现。

## Transfer to Current Work

- 最值得做的 baseline 是 `mixed-domain GRPO` vs `ordered cascade`，固定总 rollout compute，并画完整 regression matrix。
- 在发生明显遗忘后比较 MOPD、replay mixing、trace SFT 三种 repair，而不是默认 MOPD 必胜。
- 训练日志应记录每阶段的 prompt distribution、pass-rate、response length、verifier cost 和 regression gate。

## Evidence Anchors

- [cascade-rl.md](cascade-rl.md): pages 10-12。
- [mopd.md](mopd.md): pages 13-14。
- [eval.md](eval.md): claim support and evidence limits。
- [../README.md](../README.md): full pipeline verdict。
