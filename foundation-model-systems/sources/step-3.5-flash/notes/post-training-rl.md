# Step 3.5 Flash Post-training / MIS-PO

```yaml
---
source_id: step-3.5-flash
section_type: rl-training
stage: post-training
depth: working
confidence: high
need_expert_review: true
---
```

## Core Design / Innovation

- Post-training 从 unified SFT model 出发，先做 domain-specific RL experts，再把 experts 生成的 trajectories self-distill 回 generalist，最后做 scalable RL。[15-16]
- Expert domains 包括 Math、Code、STEM、Tool-use、Long Context Understanding、Human Preference、Agentic Reasoning。[15]
- Self-distillation 用 shared SFT prompt distribution 让 experts 生成高质量 trajectories，并用 rejection sampling 去掉 language mixing / overthinking 等坏模式。[16]
- MIS-PO 用 token-level 和 trajectory-level binary masks 过滤 off-distribution samples，避免 continuous importance weights 的高方差。[16-17]
- 额外稳定组件包括 truncation-aware value bootstrapping 和 routing confidence monitoring。[17]

## Why It Matters

Step 的后训练重点是 off-policy RL 如何在 MoE + 长 horizon 上不炸。MIS-PO 和 Qwen3 的 on-policy distillation、MiMo/Nemotron 的 MOPD 是不同路线：它不是 teacher-logit 蒸馏，而是用分布过滤让 off-policy rollout 更像 trust-region 内的 on-policy 样本。

## Mechanism Sketch

1. 大规模 multi-domain SFT 建 shared foundation。
2. 第二阶段 SFT 加 OOD expert-level chemistry trajectories 和 synthetic arithmetic，提升 reasoning density。
3. 各 domain 通过 RL 得到 expert models。
4. Expert models 生成 trajectories，经 rejection sampling 后蒸馏到从 midtrain checkpoint 初始化的 student。
5. Scalable RL 阶段用 MIS-PO：保留 token ratio 和 trajectory geometric mean ratio 都在阈值内的样本。

## Details / Evidence

- MIS-PO 的 actor loss 使用 `I(x_t) * I(rho_bar(tau)) * log pi_theta(a_t|s_t) * A_t`，用离散 mask 替代连续 importance weighting。[17]
- Token ratio 比较 training policy 和 vLLM inference policy 的概率差异；trajectory ratio 用全序列几何平均过滤整体 drift。[17]
- Truncation-aware value bootstrapping 把 context-truncated trajectories 视为 horizon interruption，而非直接给零 reward。[17]
- Routing Confidence 用 activated experts 的概率质量作为 MoE 稳定性 proxy，低 routing confidence 意味着更脆弱，需要更强稳定手段。[17]

## Gaps / Open Questions

- `rho_min/rho_max`、advantage estimator、reward/verifier、off-policy rollout freshness 等关键超参未充分披露。
- MIS-PO 和 PPO/GRPO/GSPO 的严格理论关系需要单独核查，不应只按名字理解。

## Lookup-only

- Figure 5: MIS-PO vs PPO reward、grad norm、entropy 曲线。[16]
- Appendix D: SFT/RL details and ablations。[35-39]

## Evidence Anchors

- 15-17: post-training overview and MIS-PO.
- 21: agent infrastructure.
- 35-39: appendix post-training details.

