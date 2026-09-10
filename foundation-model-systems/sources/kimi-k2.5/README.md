# Kimi K2.5 Source Dossier

```yaml
---
source_id: kimi-k2.5
source_type: model-tr
org: Moonshot AI
release_date: 2026-02-03
priority: S
status: section-notes
openness: open-weights
confidence: high
lineage: kimi-k2
role: full-tr
base_source: kimi-k2
---
```

## 一句话

Kimi K2.5 是 Kimi K2 lineage 当前最适合做 anchor 的完整 TR：核心不是单纯多模态，而是 joint text-vision pretraining / RL、zero-vision SFT、token-efficient RL 和 Agent Swarm / PARL，把 multimodal perception 与 parallel agent execution 结合起来。[1-6, 7-15]

## 为什么重要

对后训练，它最值得学的是“多模态 agent 能力并不一定靠人工视觉轨迹 SFT 激活”：Kimi 把视觉对齐前置到 joint pretraining，再用 text-only SFT 和 joint RL 激活能力。对 agent 方向，它的 Agent Swarm 是比单 agent context compression 更主动的 parallel context management。

## 核心设计 / Takeaways

- Joint optimization 是第一主线：早期、低比例视觉融合优于 late/high-ratio vision；联合 text-vision RL 不仅提升视觉任务，也能提升部分 text benchmark。[2-4]
- Zero-vision SFT 是反直觉重点：SFT 阶段只用 text traces，避免人工视觉 trajectory 的 distribution mismatch，同时依赖 pretraining 已建立的视觉-语言对齐。[3-4]
- RL objective 使用 token-level log-ratio clipping/masking，超出区间的 token 梯度置零；这更像稳定性 mask，不是标准 PPO surrogate。[8]
- Agent Swarm / PARL 把 orchestrator 作为 trainable policy，subagents 冻结，用 parallel reward / finish reward / task reward 学会何时开子 agent、如何调度。[4-6]
- Agent Swarm 被明确当作 proactive context management：把长任务拆成多个 bounded local context，而不是等 context 溢出后再截断。[14-15]

## Source Bundle

- technical report: https://arxiv.org/abs/2602.02276
- tech-report-pdf: https://arxiv.org/pdf/2602.02276
- model / release page: https://huggingface.co/moonshotai/Kimi-K2.5
- local pdf: `/Users/chy/Research/foundation-model-systems/papers/kimi-k2.5/kimi-k2.5.pdf`
- last checked: 2026-06-23

## Lineage / Delta

- lineage: Kimi K2
- role: full TR anchor for Kimi K2.5 and a useful base for Kimi K2.6 release-delta reading.
- previous source context: Kimi K2 / Kimi K2 Thinking / Kimi Researcher are cited by the TR, but not folded into this dossier unless needed.

## Citation Labels

- default TR pages: page-only anchors like `[4-6]`
- non-TR labels:
  - `[hf-model-card]`
  - `[kimi-docs]`

## 最大证据缺口

- Agent Swarm 的 training data、orchestrator policy details、subagent checkpoint selection 和 reward implementation 披露仍有限。
- Zero-vision SFT 的负例和 distribution mismatch 解释很关键，但需要更多 ablation 判断是否可泛化到其他 multimodal agent。
- Eval 很强但包含自建 In-house Swarm Bench，scaffold / cost / tool / timeout / judge 需要审计。

## Lens Hooks

- multimodal-training: joint text-vision pretraining/RL, zero-vision SFT, MoonViT-3D。
- rl-training: token-level clipping/masking, token-efficient RL, GRM/task-specific rewards。
- agent-systems: Agent Swarm, PARL, proactive context sharding。
- eval: multimodal + agentic + computer-use benchmark design。

## 阅读入口

- `section-index.md`: 30 页 TR 回读地图。
- `notes/multimodal-training.md`: joint text-vision training 和 zero-vision SFT。
- `notes/agent-swarm.md`: PARL、Agent Swarm 和 context sharding。
- `notes/rl-training.md`: RL objective、reward system、token efficiency。
- `notes/eval.md`: eval 设计和 claim 支撑。
- `notes/claims-and-gaps.md`: comparison 前先读。
