# MiMo-V2-Flash Post-training Summary

```yaml
---
source_id: mimo-v2-flash
stage: post-training
summary_role: current-practice-mopd-anchor
priority_for_post_training: S
confidence: high
---
```

## Verdict

MiMo-V2-Flash 是当前最清楚的 MOPD method anchor：student 从自身 policy 采样 trajectories，多个 domain teachers 提供 token-level reverse-KL dense advantages，再与 ORM/GRPO signal 合并，从而把 specialists 合并成统一模型。[11-18]

## Pipeline

```text
general SFT
-> domain-specialized RL teachers
   (reasoning / code / terminal / search / general agent)
-> student on-policy rollouts
-> teacher token-level reverse-KL advantages
-> ORM / task reward fusion
-> unified MOPD student
```

- SFT 先激活 instruction following；多个 domain teachers 分别通过 RL 达到更高能力上限。[11-17]
- MOPD 不直接训练 student 模仿 teacher-generated traces，而是在 student rollout 上查询 teachers，降低纯 offline imitation 的 distribution mismatch。[18]

## Core Mechanisms

### Dense Teacher Advantage

- Teacher/student log-prob ratio形成 token-level distillation advantage，使每个 token 都获得比 sequence ORM 更密集的学习信号。[18]
- Reverse-KL orientation 更偏向 teacher high-probability modes，适合能力 packing，但可能降低 diversity；teacher routing/weighting决定冲突域的结果。

### Reward Fusion

- 默认把 teacher dense advantage 与 ORM / GRPO-style task advantage叠加，因此 MOPD 既追随 teachers，也保留 executable correctness signal。[18]
- Training-inference importance sampling 过滤 policy discrepancy 过大的 tokens，避免 rollout policy 与 learner policy lag 导致不稳定。

### System Co-design

- 309B total / 15B active、hybrid SWA 与 lightweight MTP 降低 decoding/rollout 成本；MTP 同时服务 speculative decoding 与 RL generation。[5-9, 20-22]
- Agentic environments 使用 GitHub issues、Docker/Kubernetes、terminal/search tools 和可执行验证，说明 MOPD 的质量依赖 domain teachers 与 environment fidelity。[15-17, 20-21]

## Failure Modes / Controls

- Teachers 之间可能产生 token-level conflict；报告没有完整公开 per-domain routing 与 advantage normalization。
- Dense distillation signal 可能压过 ORM correctness，必须测 reward-scale sensitivity 与 teacher错误继承。
- Off-policy lag 通过 token filtering 缓解，但过滤过多会降低 sample efficiency；需同时报告 retention rate。

## Openness and Evidence

- Open weights + TR，MOPD 公式与流程比多数 frontier blog 具体；训练 code/data/teacher checkpoints 未完全开放。
- 适合作为方法 comparison anchor，不等于端到端可复现 recipe。

## Transfer to Current Work

- 最小实验：两个 domain teachers、student-generated rollouts、selected-token teacher logits，并和 teacher-trace SFT / mixed-domain GRPO 比较。
- 必须记录 token filter rate、teacher disagreement、ORM-vs-teacher gradient conflict 和 domain regression。
- 先验证 MOPD 是否真的改善 consolidation，再考虑 full-vocabulary logits 和大规模 teacher serving。

## Evidence Anchors

- [rl-training.md](rl-training.md): SFT pages 11-12、RL pages 12-17 与 agent environments。
- [mopd.md](mopd.md): pages 17-19。
- [architecture.md](architecture.md): pages 5-10, 21-22。
