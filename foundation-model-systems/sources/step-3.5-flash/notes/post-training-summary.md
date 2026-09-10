# Step 3.5 Flash Post-training Summary

```yaml
---
source_id: step-3.5-flash
stage: post-training
summary_role: efficient-agent-reference
priority_for_post_training: A
confidence: high
---
```

## Verdict

Step 3.5 Flash 的post-training主线是 `shared SFT -> domain RL experts -> self-distillation -> scalable RL`，并以MIS-PO的token/trajectory双层binary filtering处理long-horizon off-policy mismatch；architecture/MTP则为agent rollout latency服务。[15-17]

## Pipeline

```text
shared instruction / reasoning SFT
-> domain-specific RL experts
-> expert-to-generalist self-distillation
-> scalable long-horizon RL with MIS-PO
-> deployment under low-active-parameter / MTP stack
```

- Experts先在不同domain爬升，再把能力蒸馏回generalist，属于specialize-then-consolidate路线。[15-16]
- 196B total / 11B active、3:1 SWA/full attention和MTP-3的意义是降低多轮agent decoding成本，而非post-training method本身。[4-8]

## Core Mechanisms

### MIS-PO

- 不连续加权所有off-policy samples，而在token与trajectory两层做binary retain/drop，把保留样本近似当on-policy训练。[16-17]
- 直觉是避免长trajectory中少数极端importance ratios放大方差；代价是丢弃数据并引入选择偏差。

### Expert Self-distillation

- Domain experts提供能力上限，generalist吸收后再继续RL；与MOPD的区别取决于监督是trace、logits还是rewarded samples，报告披露需按现有stage note解释。
- Consolidation后必须做per-domain retention，不应只用总平均宣布成功。

## Failure Modes / Controls

- Binary filtering阈值过严会浪费rollouts，过松则off-policy variance回归；应同时报告retention rate和effective tokens。
- SWA/low-active architecture可能在complex multi-hop agent tasks上损失quality，需和latency共同评估。
- Expert packing可能产生capacity conflict与弱域遗忘。

## Openness and Evidence

- Open weights + full TR，pipeline和MIS-PO方向明确；data、expert composition、filter thresholds和training code未fully open。
- Step 3.7是较新release但没有同等full training TR；3.5仍是recipe anchor。

## Transfer to Current Work

- 比较continuous IS、token-only mask与token+trajectory binary filtering，固定有效rollout compute。
- 记录discard原因、sample age、trajectory length和gradient variance。
- 将success/token、wall time、active FLOPs和consolidation regression一起作为效率指标。

## Evidence Anchors

- [post-training-rl.md](post-training-rl.md): pages 15-17。
- [architecture-inference.md](architecture-inference.md): pages 4-8。
- [eval-release-delta.md](eval-release-delta.md): agent/effectiveness evaluation。
- [claims-and-gaps.md](claims-and-gaps.md): Step 3.5 anchor vs 3.7 delta。
