# GLM-5.1 Post-training Summary

```yaml
---
source_id: glm-5.1
stage: post-training
summary_role: release-delta
priority_for_post_training: B
confidence: low
---
```

## Verdict

GLM-5.1 不是独立 post-training recipe source，而是 GLM-5 到 GLM-5.2 之间的版本边界：官方只披露 coding、long-horizon、long-context 与 tool-use 能力增强，没有足够证据确定新增 SFT/RL/data/infra 方法。

## What Is Public

- Release positioning 强调 agentic engineering、coding、reasoning、long-horizon task 和 tool calling。
- 没有找到与 GLM-5 同级的独立 full TR，也没有可核查的 stage-wise post-training pipeline。
- 因此 GLM-5 的 SFT/reasoning RL/agentic RL/general RL/cross-stage distillation只能作为 lineage background，不能写成“GLM-5.1 明确采用”。

## Safe Lineage Interpretation

```text
GLM-5 full-TR anchor
-> GLM-5.1 capability/product delta (method underdisclosed)
-> GLM-5.2 current-practice delta (critic PPO / anti-hack / parallel OPD)
```

- 5.1 的价值是避免把 5.2 相对旧版本的所有能力变化直接归因到 GLM-5 TR。
- 它可用于 release chronology和eval target变化，不应用于抽取新RL recipe。

## Evidence Gaps

- SFT data、reasoning traces、agent environments、reward、policy objective、distillation与training infra均未披露。
- Release benchmark不能反推训练方法；tool-use提升也不能证明新增agentic RL。
- 任何“继承GLM-5”的说法都应标为假设，除非5.1 materials明确确认。

## Transfer to Current Work

- 无直接可复现recipe。
- 方法学价值是提醒：版本delta必须把capability evidence与training-recipe evidence分开。
- Comparison中只保留一行版本边界，不投入PDF精读预算。

## Evidence Anchors

- [release-delta.md](release-delta.md) 或 dossier现有release note。
- [claims-and-gaps.md](claims-and-gaps.md): 未披露项。
- [../README.md](../README.md): source role and lineage boundary。
