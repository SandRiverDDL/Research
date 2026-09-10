# Open-R1 Claims and Gaps

```yaml
---
source_id: open-r1
section_type: claims-and-gaps
stage: claims-and-gaps
substage: none
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- 强证据：项目开放可运行的 SFT/GRPO/data-generation/evaluation code，以及多批 datasets/checkpoints。[repo, hf-org]
- 强证据：R1-Distill-style capability 可以用公开 verified traces 与 SFT recipe 复现到接近水平。[repo]
- 不成立的笼统表述：整个 DeepSeek-R1 原始 pipeline 已经被逐项、端到端精确复现。[blog-launch, repo]

## Why It Matters

Living repository 必须按 milestone 判断。“项目目标”“存在代码路径”“已发布 checkpoint 并复现结果”是三个不同状态。

## Mechanism Sketch

1. Blog claim 只作为 dated scope。
2. Repository code/config 是 operational evidence。
3. Dataset/checkpoint 加 matched eval 才算完成 milestone。
4. 任何实验前先 pin commit。

## Details / Evidence

- Repository 明确把 Step 1（distillation）标为完成，而 Steps 2-3 是更广的 project goals。[repo]
- Hardware 与 dependency assumptions 有记录，但不保证跨平台直接可复现。[repo]

## Gaps / Open Questions

- 每个结果表对应的 frozen release/commit。
- End-to-end compute 与 failure logs。
- 与 ORZ/Skywork recipe 的 matched ablation。
- Verifiable reasoning/code 之外的覆盖范围。

## Lookup-only

- Stars、commit count 等瞬时 repository metadata 不作为 durable research fact。

## Evidence Anchors

- `[blog-launch]`：initial scope。
- `[repo]`：当前 implementation 与 milestones。
- `[hf-org]`：published artifacts。
