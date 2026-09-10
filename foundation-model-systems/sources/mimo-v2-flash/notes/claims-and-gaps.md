# MiMo-V2-Flash Claims and Gaps

```yaml
---
source_id: mimo-v2-flash
section_type: claims-and-gaps
depth: working
confidence: medium
need_expert_review: false
---
```

## 问题

MiMo-V2-Flash 哪些公开 claim 值得信？哪些足够用于 OPD/RL comparison？哪些只是还需要补证据的 release/reporting claim？

## 可信 claim

- MOPD 是这份 TR 披露最充分的核心创新：有三阶段流程、technical formulation、importance sampling、ORM combination 和 ablation。[11-14, 18-19]
- Architecture 的 Hybrid SWA / attention sink / MTP ablation 有一定证据支撑，且和 speed-oriented goal 一致。[5-9, 21-22]
- Agentic RL environment scaling 写得较具体，包括 task types、real/synthesized split、containerized env、Kubernetes scale、minimal tools。[16-17]
- TR 对 limitations 有基本承认：和 strongest closed-weight models 仍有 gap，architecture exploration preliminary，未来要 scale MOPD teacher-student co-evolution。[22]

## 暂不信的 claim

- “preserves peak performance of the strongest teacher across all domains”需要谨慎；Table 7 自己显示若干 benchmark 低于 best teacher。[14]
- “perfectly master teacher expertise”属于 abstract-level rhetoric；MOPD 是有效 consolidation，不是无损合并。[1, 14]
- 和 closed models 的 final comparison 需要看 eval setting，不能只按 Table 9 排名判断。[20]
- V2.5-Pro 的训练细节不能从 V2-Flash TR 自动继承；目前没有找到 V2.5-Pro 专门 TR。

## 关键缺失信息

- MOPD teacher routing、teacher serving cost、epsilon thresholds、alpha、ORM implementation、teacher/domain prompt mixture。
- RL reward/verifier implementation，特别是 open-ended helpfulness/safety 和 agentic tasks。
- Pretraining data source proportions、filter thresholds、contamination/decontamination audit。
- Eval scaffold/tool/context/sampling/judge details。

## 值得内化

- Multi-specialist consolidation 最好不要只靠 offline SFT：student on-policy rollout + teacher token-level reward 能更直接处理 exposure bias 和 dense credit assignment。
- Agentic RL 的 bottleneck 是 rollout/environment/infra，不只是 policy loss；MTP、prefix cache、tool resource scheduling 都会影响训练规模。
- MoE 后训练需要稳定性指标；`num-zeros` 这种工程指标虽然朴素，但可能比抽象 loss 更早暴露 expert imbalance 或 overfitting。

## 随查随用

- Exact architecture config, hyperparameters, benchmark numbers, Table 7/9 entries, Table 10 speedups。

## Evidence Anchors

- 1: abstract/headline claims。
- 5-9: architecture and MTP。
- 9-10: pretraining。
- 11-19: post-training and MOPD。
- 20: final benchmark comparison。
- 21-22: inference speed and limitations。
