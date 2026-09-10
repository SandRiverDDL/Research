# Arcee Trinity Large Post-training Summary

```yaml
---
source_id: arcee-trinity-large
stage: post-training
summary_role: negative-scope-reference
priority_for_post_training: B
confidence: high
---
```

## Verdict

Arcee Trinity Large 不应被包装成post-training recipe：公开材料的主要价值是400B/13B-active MoE pretraining、Muon、SMEBU、17T-token data与Nano/Mini/Large scaling ladder；当前没有足够高价值SFT/RL/consolidation披露。[1-9]

## What the Source Actually Covers

- Architecture：local/global attention、QK-Norm、gated attention、DeepSeekMoE-style experts、sigmoid routing和depth-scaled norms。[5-8]
- Training stability：Muon与QK-Norm；SMEBU用magnitude-aware、soft-clamped expert bias update减少router oscillation。[5-7]
- Data/pretraining：17T tokens，20T mix按13:4:3组织，含synthetic web/code/STEM；具体post-training不是报告主线。[9]
- Scaling ladder：Nano/Mini用于验证data、architecture、recipe和infra，再扩到Large。[2]

## Post-training Evidence Boundary

- 没有足够材料复原SFT data、preference optimization、reasoning RL、reward/verifier、agent environments或capability consolidation。
- 如果存在instruct checkpoint或发布评测，只能说明模型被后训练过，不能推出recipe。
- 因而本文件的结论是“off-scope for current post-training”，不是为了补齐模板而猜测流程。

## Why Keep It

- 它提供未来base-model intuition：MoE routing stability、optimizer choice、data scaling ladder会影响后续policy可塑性和RL成本。
- 与OLMo 3对比可区分“大规模开放pretraining disclosure”和“fully-open end-to-end model flow”。
- 当研究post-training regression是否源于base/router instability时，Trinity可作为architecture/pretraining reference。

## Openness and Evidence

- Open weights + pretraining TR；不是fully-open post-training project。
- 对当前工作优先级B，不应占用RL/agent recipe精读预算。

## Transfer to Current Work

- 唯一直接可迁移项是训练前诊断：确认base checkpoint、MoE routing与long-context behavior稳定，再归因post-training失败。
- 不从其benchmark或instruct model表现反推未公开alignment method。

## Evidence Anchors

- [architecture-stability.md](architecture-stability.md): pages 5-8。
- [pretraining-data.md](pretraining-data.md): pages 2, 9。
- [claims-and-gaps.md](claims-and-gaps.md): post-training disclosure boundary。
- [../README.md](../README.md): source-level verdict。
