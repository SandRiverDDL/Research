# MiniMax-M2 Series Source Dossier

```yaml
---
source_id: minimax-m2-series
source_type: model-tr
org: MiniMax
release_date: 2026-05-31
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: minimax-m2
role: full-tr
base_source: minimax-m1
---
```

## 一句话

MiniMax-M2 Series 是 MiniMax lineage 的完整训练系统资料，但不是当前最新模型线：主线是 229.9B/9.8B active MoE、agent-driven data pipelines、Forge agent-native RL、interleaved thinking 和 M2 -> M2.5 -> M2.7 self-evolution；总结“当前 MiniMax 先进实践”时必须优先检查 M3 / MSA / M3 model card 的后续改动。[1-2, 7-20, 24-30]

## 为什么重要

它是近期 open-weight recipe 中最贴近“后训练 + agentic data + RL infra + 自我迭代”的完整资料。MiniMax-M3/MSA 更新，主要披露 long-context sparse attention、native multimodality 和 serving/context 能力；因此 M2 series 适合作为训练 recipe 的 lineage-reference，M3 是 current-practice delta。

## 核心设计 / Takeaways

- 小 active footprint 是主叙事：M2 flagship 229.9B total / 9.8B active，目标是在每 token 计算更小的情况下靠数据、RL infra 和 agent harness 接近 frontier real-world tasks。[1-3]
- Architecture 回到 full GQA attention，而不是沿用 MiniMax-Text-01 hybrid attention；原因是 hybrid/SWA 在 complex multi-hop reasoning 和 agent tasks 上质量不足。[3-6]
- Data pipeline 是最大价值：SWE/AppDev/Terminal/Cowork/Reasoning/Conversation/Role-play 都围绕 executable workspace、artifact-aligned reward、Agent-as-a-Verifier 和多模型教师 trajectory 组织。[7-16]
- Forge 把 arbitrary agents、white-box/black-box API agents、training/inference side、middleware data pool 解耦，目标是在 throughput、stability、agent flexibility 的 impossible triangle 中取平衡。[19-23]
- Interleaved thinking 保留跨 turn reasoning state，让 plan-act-reflect loop 显式进入上下文；这对 long-horizon agent 任务比 front-loaded CoT 更合适。[24-25]
- M2.5/M2.7 是同一 recipe 的进化节点；TR 用 within-series progression 说明 agentic data、Forge 和 self-evolution 共同带来持续提升。[25-30]

## Source Bundle

- technical report: https://arxiv.org/abs/2605.26494
- tech-report-pdf: https://arxiv.org/pdf/2605.26494
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/minimax-m2-series/minimax-m2-series.pdf`
- MiniMax-M3 / MSA architecture delta:
  - MSA paper: https://arxiv.org/abs/2606.13392
  - MSA repo: https://github.com/MiniMax-AI/MSA
  - M3 model card: https://huggingface.co/MiniMaxAI/MiniMax-M3
  - M3 release blog: https://www.minimax.io/blog/minimax-m3
  - local MSA pdf: `/Users/chy/Research/foundation-model-systems/papers/minimax-m3/minimax-msa.pdf`
- last checked: 2026-07-21

## Lineage / Delta

- lineage: MiniMax M2
- role: full TR anchor for M2 / M2.5 / M2.7 series; lineage-reference for later MiniMax summaries.
- MiniMax-M3 role: current-practice architecture/long-context sparse attention delta, not standalone full training anchor in this pass.

## Citation Labels

- default M2 series TR pages: page-only anchors like `[7-16]`
- non-main labels:
  - `[m3-msa:1-6]`: MiniMax Sparse Attention paper.
  - `[m3-model-card]`: MiniMax-M3 model card.

## 最大证据缺口

- M2 series disclose many pipeline patterns, but exact data volumes, filtering thresholds, reward model training, stage ratios and RL hyperparameters are still underdisclosed.
- Forge 的 system abstraction 很有价值，但 implementation / scheduling / off-policy / stability ablation 仍需深读。
- M3/MSA 提供 architecture evidence，但不能自动继承为 M2.5/M2.7 training recipe。

## Lens Hooks

- agentic-data: SWE/AppDev/Terminal/Cowork executable data and verifier design.
- rl-infra: Forge, gateway/data pool, white-box/black-box agent RL.
- thinking: interleaved thinking and reasoning state persistence.
- release-lineage: M2 -> M2.5 -> M2.7 progression and M3 architecture delta.
- eval: long-horizon coding/cowork/workspace eval under shared scaffold.

## 阅读入口

- `section-index.md`: 35 页 TR + M3 delta 回读地图。
- `notes/architecture-pretraining.md`: M2 architecture, pretraining, long-context extension。
- `notes/agentic-data-forge.md`: agentic data pipelines and Forge RL infra。
- `notes/release-deltas.md`: M2.5/M2.7/M3 的版本关系。
- `notes/release-minimax-m3.md`: M3 current-practice delta 与 post-training disclosure boundary。
- `notes/eval.md`: eval 方法和可比性。
- `notes/claims-and-gaps.md`: comparison 前先读。
