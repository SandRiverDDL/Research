# GLM-5 Post-training Summary

```yaml
---
source_id: glm-5
stage: post-training
summary_role: lineage-reference
priority_for_post_training: A
confidence: high
---
```

## Verdict

GLM-5 是 GLM lineage 的完整 post-training/infra anchor：SFT、reasoning RL、agentic RL、general RL 和 on-policy cross-stage distillation 依次训练，并用 slime 与 fully asynchronous rollout 处理长 agent trajectory 的 GPU idle 和 policy lag。[10-17]

## Pipeline

```text
SFT
-> Reasoning RL
-> Agentic RL
-> General RL
-> On-Policy Cross-Stage Distillation
```

- Reasoning RL 建立数学、代码和复杂推理；Agentic RL 转向 executable coding/search/terminal environments；General RL 修 instruction/helpfulness；最后 cross-stage distillation 降低多阶段遗忘。[10-14]
- 这条顺序是 lineage-reference。GLM-5.2 已明确加入 critic PPO、anti-hacking 与 parallel OPD，当前实践应以后者为准。

## Core Mechanisms

### Asynchronous Agentic RL

- 长 episode 的 wall time 方差使同步 batch 等待最慢 rollout，GLM 用 decoupled training/inference/rollout 与 Multi-Task Rollout Orchestrator 服务化任务。[12-17]
- `slime` 提供 rollout execution、task orchestration 和训练侧连接；方法收益高度依赖系统能否保持 GPU goodput。

### Stability Controls

- TITO、direct double-sided importance sampling、stale/noisy sample dropping 和 DP-aware routing 控制异步策略偏差与 MoE routing不一致。[12, 16-17]
- DSA indexer freeze/deterministic top-k 等 architecture control 同样影响 rollout reproducibility。

### Cross-stage Distillation

- 最后在 on-policy data 上聚合前序阶段能力，目标不是压缩模型规模，而是降低 reasoning/agent/general alignment 的相互覆盖。[13-14]
- 报告对 teacher target、loss 与 stage weighting 的披露不足，方法级理解应与 GLM-5.2 parallel OPD 分开。

## Failure Modes / Controls

- Tail latency、stale rollout、policy mismatch 和 environment instability 是主要系统失败面。
- 多阶段训练容易遗忘 earlier capability；必须维持跨阶段 regression suite。
- 异步吞吐提高不能以过旧 policy samples 为代价，需报告 sample age distribution 和 discard rate。

## Openness and Evidence

- Open weights + full TR；stage flow、slime 和 agentic eval 较具体，data/reward/config 仍不完整。
- 当前 GLM 总结不能停在 GLM-5：5.2 的明确 delta 覆盖其部分 RL/consolidation 设计。

## Transfer to Current Work

- 先测 rollout tail distribution、GPU idle、policy lag 与 discard rate，再优化 RL objective。
- 将 async/sync 对比固定在相同有效 on-policy tokens 与 wall-clock budget，避免只比较吞吐。
- 对 agent environments 保留 executable artifact、tool trace 和 deterministic replay。

## Evidence Anchors

- [agentic-rl.md](agentic-rl.md): post-training pages 10-14、async infra pages 12-17。
- [eval.md](eval.md): pages 19-23。
- [../README.md](../README.md): GLM-5/5.2 lineage boundary。
