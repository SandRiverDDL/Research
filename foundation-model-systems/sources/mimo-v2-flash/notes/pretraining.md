# MiMo-V2-Flash Pretraining

```yaml
---
source_id: mimo-v2-flash
section_type: pretraining-engineering
stage: pretraining
substage: staged-data-schedule
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Pretraining 是 27T tokens 的三阶段 schedule：general 32K -> code/synthetic reasoning mid-training -> 256K context extension。[9-10]
- Data emphasis 从通用高质量语料转向 long-range dependency：long-form web documents、repository-level code、pull requests、issues、commit histories。[10]
- Stage 2 upsample code-centric data，并加入约 5% synthetic reasoning data，用来增强 logical reasoning 和 program synthesis。[10]
- Stage 3 保持 Stage 2 distribution，但扩 context 到 256K，并上采 long-range dependency data。[10]

## Why It Matters

MiMo 的 pretraining 没有 MAI 那种 scale-ladder mixture search 细节，但给了一个清晰的工程路线：如果目标是 coding / agentic / long-context，mid-training 和 context extension 会明显偏向 code repository、PR、issue、commit history 这类长依赖数据。

## Mechanism Sketch

1. Stage 1: 0-22T，32K context，general-purpose corpus。
2. Stage 2: 22-26T，调整 data mixture，upsample code-centric data，加入约 5% synthetic reasoning。
3. Stage 3: 26-27T，context extension 到 256K，继续 Stage 2 distribution，并上采 long-range dependency data。
4. 全程结合 Hybrid SWA 和 MTP，使长上下文和推理/推理速度目标一致。

## Details / Evidence

- TR 明确说 data processing pipeline largely follows MiMo-7B，但 MiMo-V2-Flash 有 deliberate shift toward long-range dependency data。[10]
- Code corpora 包括 repository-level code、pull requests、issues、commit histories，目标是增强 extended contextual relationships 和 multi-step reasoning。[10]
- Training hyperparameters 给得较具体，包括 AdamW、LR schedule、gradient clipping、batch size 和 expert bias update factor，但这些主要是 lookup-only。[10]

## Gaps / Open Questions

- 没有完整 source-family proportions，不能像 MAI 那样分析 data mixture selection philosophy。
- Synthetic reasoning data 的生成方法、teacher、filtering、contamination audit 没披露。
- MiMo-7B pipeline 被引用但没有在本 TR 中展开，不应当把 MiMo-7B 细节默认继承为 V2-Flash 事实。

## Lookup-only

- Stage 1: 0-22T tokens, 32K context。[10]
- Stage 2: 22-26T tokens, code upsampling, about 5% synthetic reasoning。[10]
- Stage 3: 26-27T tokens, context extension to 256K。[10]
- AdamW beta1 0.9, beta2 0.95, weight decay 0.1, grad clip 1.0。[10]

## Evidence Anchors

- 9-10: pretraining data scheduler and hyperparameters。
