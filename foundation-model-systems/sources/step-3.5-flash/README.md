# Step 3.5 Flash Source Dossier

```yaml
---
source_id: step-3.5-flash
source_type: model-tr
org: StepFun
release_date: 2026-02-23
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: step-flash
role: full-tr
base_source: step-3
---
```

## 一句话

Step 3.5 Flash 是 StepFun 当前最完整的公开训练 TR：196B total / 11B active MoE，以 agent latency/cost 为设计中心，结合 3:1 SWA/full attention、MTP-3、Muon 稳定训练、专家模型自蒸馏和 MIS-PO off-policy RL。[1-5, 15-17]

## 为什么重要

它补的是“高效率 frontier-ish agent model”这一类：不追求最大参数，而是把低 active params、低延迟、多轮 agent 推理和可扩展 RL 放在一起优化。对后训练来说，MIS-PO 和 expert -> generalist self-distillation 是重点。

## 核心机制 / Takeaways

- 架构目标是 agentic workload：大量 context prefilling + 长时间 multi-turn decoding，所以 attention、MoE、MTP 都围绕 latency 设计。[4-7]
- 3:1 SWA/full attention 降低 long-context 成本；增加 SWA query heads 和 head-wise gated attention 弥补质量损失。[7-8]
- MTP-3 作为 speculative decoding 友好组件，训练上多数阶段只优化 MTP-1，最后轻量训练 MTP-2/3。[7]
- Post-training 是 shared SFT foundation -> domain-specific RL experts -> self-distillation -> scalable RL。[15-16]
- MIS-PO 不做连续 importance weighting，而是 token/trajectory 双层 binary filtering，把保留样本近似当 on-policy，降低长 horizon off-policy 梯度方差。[16-17]

## Source Bundle

- technical report: https://arxiv.org/abs/2602.10604
- tech-report-pdf: https://arxiv.org/pdf/2602.10604
- repo: https://github.com/stepfun-ai/Step-3.5-Flash
- model: https://huggingface.co/stepfun-ai/Step-3.5-Flash
- blog: https://static.stepfun.com/blog/step-3.5-flash/
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/step-3.5-flash/step-3.5-flash.pdf`
- last checked: 2026-06-23

## Version Check

- Latest StepFun model found: Step 3.7 Flash, released May 2026, model card/blog style disclosure with native multimodal support.
- Latest full training TR found: Step 3.5 Flash, arXiv v2 dated 2026-02-23.
- Handling rule: use Step 3.5 Flash as full TR anchor; record Step 3.7 Flash as release delta if needed, not as replacement full TR.

## Citation Labels

- default TR pages: page-only anchors.
- non-TR labels: `[repo]`, `[hf-3.5]`, `[hf-3.7]`, `[blog-3.5]`.

## 最大证据缺口

- MIS-PO 的 reward/verifier、off-policy data generation 和 exact filtering thresholds 没有完全公开。
- Step 3.7 Flash 的训练细节不足，不能直接继承 Step 3.5 的全部训练事实。

## Lens Hooks

- architecture: latency-first MoE, SWA/full attention, MTP.
- rl-training: MIS-PO, truncation-aware value bootstrapping, routing confidence.
- consolidation: expert model construction and self-distillation.
- eval: PaCoRe / long-context agent eval setting.

## 阅读入口

- `notes/architecture-inference.md`: 低延迟架构。
- `notes/post-training-rl.md`: self-distillation 和 MIS-PO。
- `notes/eval-release-delta.md`: eval 方法和 Step 3.7 关系。

