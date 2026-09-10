# MiMo-V2-Flash Source Dossier

```yaml
---
source_id: mimo-v2-flash
source_type: model-tr
org: Xiaomi LLM-Core
release_date: 2026-01-06
priority: A
status: section-notes
openness: open-weights
confidence: high
lineage: mimo-v2
role: full-tr
base_source: none
---
```

## 一句话

MiMo-V2-Flash 的核心价值不是榜单，而是公开了一条小 active-parameter MoE 模型的系统路线：Hybrid SWA + lightweight MTP 降低推理/RL rollout 成本，三阶段 pretraining 建 256K context，再用 SFT -> domain-specialized RL teachers -> MOPD 把多个 specialist 能力合并回一个 student。

## 为什么重要

这份 TR 对后训练尤其值得读，因为 MOPD 披露得比很多大厂 blog 更具体：student 自己 on-policy rollout，domain teachers 给 token-level reverse-KL dense reward，再和 ORM / GRPO advantage 合并。它可以直接拿来和 GLM-5.2 的 parallel OPD、DeepSeek 的 OPD/consolidation、MAI 的 specialist consolidation 对比。

## 核心机制 / Takeaways

- Architecture 主线是 speed-oriented MoE：309B total / 15B active，48 layers，39 SWA + 9 GA，SWA:GA = 5:1，window 128，并加入 attention sink bias 避免 hybrid SWA 质量退化。[5-8]
- MTP 不是只为 pretraining 辅助 loss，而是直接服务 speculative decoding 和 RL rollout 加速；TR 把 MTP 视为让 small-batch on-policy RL 更实际的系统组件。[9, 21-22]
- Pretraining 分三阶段：0-22T general 32K，22-26T upsample code + 约 5% synthetic reasoning，26-27T context extension 到 256K 并上采 long-range dependency data。[9-10]
- Post-training 是三阶段：SFT 激活 instruction following，domain-specialized RL 训练多个 teacher，MOPD 用 student on-policy rollouts 和 teacher token-level rewards 做 multi-teacher consolidation。[11-18]
- MOPD 的关键公式是 teacher/student log-prob ratio 形成 token-level advantage，并通过 training-inference importance sampling 丢弃 policy discrepancy 大的 token；默认再叠加 ORM advantage。[18]
- Agentic RL 数据和 infra 写得比较实：code agent、terminal agent、search/general agent，包含 GitHub issues、Dockerized env、Kubernetes pods、atomic tools 和 scaling curves。[15-17, 20-21]

## Source Bundle

- technical report: https://arxiv.org/abs/2601.02780
- model card:
  - https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash
- announcement / blog:
  - https://mimo.xiaomi.com/blog/mimo-v2-flash
  - V2.5: https://mimo.xiaomi.com/mimo-v2-5/
  - V2.5-Pro: https://mimo.xiaomi.com/mimo-v2-5-pro/
- code / repo: https://github.com/XiaomiMiMo/MiMo-V2-Flash
- weights: see HF / GitHub links in `source-bundle.md`
- external eval: none deeply audited in this first pass
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/mimo-v2-flash/mimo-v2-flash-tech-report.pdf`
- last checked: 2026-06-22

## Lineage / Delta

- lineage: MiMo-V2
- role: full TR anchor for MiMo-V2-Flash
- base source: none
- delta from: MiMo-7B / MiMo-V2 prior releases are background only
- carries over: MiMo data-processing lineage is mentioned, but not treated as sufficient detail for MiMo-V2-Flash
- newly disclosed: Hybrid SWA experiments, 27T schedule, SFT stability metric, domain-specialized RL, MOPD formula, MTP inference/RL acceleration
- not safe to inherit: MiMo-V2.5 / V2.5-Pro recipe details; they currently have blog/model card disclosure, not a full TR

## Citation Labels

- default TR pages: `[11-18]`
- non-TR source labels used:
  - `[blog-v2-flash]`
  - `[v2.5-pro-blog]`
  - `[hf-model-card]`

## 最大证据缺口

- MOPD 给了公式，但没有披露 teacher routing、domain classifier、teacher serving cost、epsilon thresholds、ORM details、alpha tuning 和 prompt mixture。
- Domain-specialized RL 的 reward models / verifiers 没有完整公开，尤其是 open-ended helpfulness/safety 和 agentic reward。
- Pretraining data composition 只给阶段和大类，没有完整 source family proportions、filtering thresholds、decontamination audit。
- V2.5 / V2.5-Pro 没有找到完整 TR；不能把 V2-Flash 的 recipe 直接当作 V2.5-Pro 的事实。

## Lens Hooks

- architecture: Hybrid SWA + GA, attention sink bias, lightweight MTP。
- pretraining: 27T staged schedule, code/synthetic reasoning upsampling, 256K extension。
- rl-training: domain-specialized RL teachers, code/terminal/search/general agent environments。
- opd: MOPD as on-policy multi-teacher distillation with reverse-KL token advantage + ORM advantage。
- eval: open/closed model comparison, MOPD ablation, agentic eval settings。
- infra: MTP rollout acceleration, request-level prefix cache, ToolBox / Tool Manager, Kubernetes scale。

## 阅读入口

- `section-index.md`: 回 PDF 页码和 source bundle。
- `notes/mopd.md`: MOPD 机制、公式和评价。
- `notes/rl-training.md`: SFT、domain-specialized RL、agentic environments 和 rollout infra。
- `notes/architecture.md`: Hybrid SWA、MoE、MTP architecture。
- `notes/pretraining.md`: data scheduler 和 27T training schedule。
- `notes/eval.md`: eval 设计、MOPD ablation 和可比性。
- `notes/inference.md`: MTP speculative decoding、request prefix cache、tool infra。
- `notes/claims-and-gaps.md`: comparison 前先读。
