# Nemotron-Cascade 2 Source Dossier

```yaml
---
source_id: nemotron-cascade-2
source_type: model-tr
org: NVIDIA
release_date: 2026-03-16
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: nemotron-cascade
role: full-tr
base_source: nemotron-3-nano-30b-a3b-base
---
```

## 一句话

Nemotron-Cascade 2 是当前最值得优先读的 2026 open post-training recipe：它把 SFT、严格 on-policy GRPO、Cascade RL、multi-domain RL、MOPD、RLHF、long-context RL、code RL 和 SWE RL 串成一条 domain-wise 后训练管线，并公开 model checkpoint 与 SFT/RL data collection。

## 为什么重要

它比很多 frontier TR 更接近“可学习的后训练方法论文”。核心不是 30B-A3B 模型本身，而是 Cascade RL 的训练顺序和 MOPD 如何在复杂 RL 阶段之间恢复 regression、合并 intermediate teachers。对你当前后训练方向，Cascade 2 是 MiMo MOPD 之后最应该加入 comparison 的 source。

## 核心机制 / Takeaways

- Cascade RL 的设计原则是按 domain 顺序训练，而不是把所有 RL tasks 混成一个巨大 mixture；这样可以为每个阶段调 curriculum、reward、response length 和 verifier 成本。[10-12]
- 它坚持 strict on-policy GRPO：每次从当前 policy 采样 group rollouts，然后只做一次 gradient update；importance ratio 等于 1，并移除 KL 项，objective 退化到 group-normalized REINFORCE/token-level loss。[11]
- Cascade 顺序是 IF-RL -> multi-domain RL -> MOPD -> RLHF -> long-context RL -> code RL -> SWE RL；MOPD 放在中间，用 intermediate best teachers 恢复/合并前面阶段的能力。[10]
- MOPD 的优势被写成 dense token-level distillation advantage，相比 GRPO 的 sparse sequence reward 更 sample/step efficient；TR 给了 AIME 和 ArenaHard 的效率对比。[13-14]
- 开放性比一般 open-weight TR 更高：abstract/landing page 明确 release model checkpoint、SFT data 和 RL data collection。[1]

## Source Bundle

- technical report: https://arxiv.org/abs/2603.19220
- model card: https://huggingface.co/nvidia/Nemotron-Cascade-2-30B-A3B
- data:
  - https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-SFT-Data
  - https://huggingface.co/datasets/nvidia/Nemotron-Cascade-2-RL-Data
- code / repo: https://github.com/NVIDIA-NeMo/RL
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/nemotron-cascade-2/nemotron-cascade-2.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: Nemotron-Cascade
- role: full TR for Cascade 2
- base source: Nemotron-3-Nano-30B-A3B-Base
- delta from: Nemotron-Cascade 1 and Nemotron 3 Nano
- carries over: Nemo-RL / Nemo-Gym infrastructure lineage
- newly disclosed: broad Cascade RL ordering, multi-domain OPD/MOPD, IF-RL, long-context/code/SWE RL recipe details
- not safe to inherit: Nemotron 3 Ultra/Super pretraining architecture details

## Citation Labels

- default TR pages: `[10-14]`
- non-TR source labels used:
  - `[hf-model-card]`
  - `[sft-data]`
  - `[rl-data]`

## 最大证据缺口

- MOPD teacher routing、teacher logit serving cost、multi-teacher weighting 和 regression recovery criteria 没有完全公开。
- 各 RL domain 的 reward/verifier 实现仍需回读 appendix / repo / datasets。
- 尽管公开数据 collection，完整训练 infra、hardware scale 和 exact rerun reproducibility 仍需审计。

## Lens Hooks

- rl-training: Cascade RL ordering, strict on-policy GRPO, IF-RL, long-context/code/SWE RL。
- opd: multi-domain MOPD with dense token-level teacher advantage。
- eval: IMO/IOI/ICPC gold-medal evaluation and agentic benchmark caveats。
- infra: Nemo-RL, Nemo-Gym, domain-specific verifier cost control。

## 阅读入口

- `section-index.md`: 回 PDF 页码。
- `notes/cascade-rl.md`: Cascade RL 的阶段顺序和 on-policy GRPO。
- `notes/mopd.md`: MOPD 机制和与 MiMo 的对比入口。
- `notes/eval.md`: eval 设计和可信度。
