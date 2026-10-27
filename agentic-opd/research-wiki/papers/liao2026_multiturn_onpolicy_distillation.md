---
type: paper
node_id: paper:liao2026_multiturn_onpolicy_distillation
title: "Multi-Turn On-Policy Distillation with Prefix Replay"
authors: ["Baohao Liao", "Hanze Dong", "Christof Monz", "Xinxing Xu", "Li Dong", "Furu Wei"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.04763"
  doi: null
  s2: null
tags: ["agentic-opd", "prefix-replay", "teacher-support", "step-sampling"]
added: 2026-10-14T13:20:28Z
---

# Multi-Turn On-Policy Distillation with Prefix Replay

## One-line thesis
【作者报告】ReOPD 重放 teacher prefix、采样当前 student action，并优先监督早期 steps，以减少在线交互成本且维持 OPD 级效果。

## Problem / Gap
【事实：论文问题定义】多轮 OPD 每次重新执行 student rollout，会重复支付环境交互与 teacher query 成本。另一方面，让 prefix 更接近 student 的访问分布，并不保证 teacher 在这些 histories 上仍能给出可靠目标；作者称这种张力为 prefix trap。[§3，PDF pp. 6-8](https://arxiv.org/html/2607.04763v3#S3)

【作者分析】论文把目标差异拆为 student occupancy mismatch 与 teacher reliability 两项；结论依赖有界 loss 等假设，不能解释为 teacher 在所有 student prefix 上都会失效。

## Method
【事实】从预收集 teacher 轨迹池中选取交互位置，原样重放此前的 teacher actions 和 observations；student 只生成当前 action，teacher 沿这个 student action 的 token contexts 提供 `KL(student || teacher)` 监督。当前 action 不执行到环境中，也不生成新的 observation。[§4，PDF pp. 9-12](https://arxiv.org/html/2607.04763v3#S4)

默认按 `p(t) ∝ kappa^t` 采样监督位置，实验固定 `kappa=0.6`，让早期 steps 获得更多训练质量。论文讨论 sampling 与 loss weighting 两种估计方式，但实际实验使用 **sampling 后不再乘同一权重**。Step decay 是跨位置的粗略代理，不等同于理论里在同一步不同 histories 间调整密度比的精确 bridge。[§4 / Algorithm 1，PDF p. 12](https://arxiv.org/html/2607.04763v3#S4)

【边界】这里的 on-policy 是当前 action 内的 student-sampled token contexts；环境状态和 earlier prefix 仍来自 teacher pool，不是完整 student occupancy。它也不是对固定 teacher action 做普通 SFT。

## Key Results
【事实：作者报告，未复现】数学任务报告六个 benchmark 的 macro average，搜索报告七个 benchmark 的 micro average；两种均值不能直接混合。Table 4-6 中的 GRPO 是 teacher 参考结果，不是同规模 student 的竞争算法。

| Teacher → Student / 设置 | OPD | ReOPD | 原文 |
|---|---:|---:|---|
| Qwen3-8B → 4B / 数学均值 | 51.0 | 53.7 | Table 4，PDF p. 14 |
| Qwen3-30B-A3B → 4B / 数学均值 | 51.1 | 52.5 | Table 4，PDF p. 14 |
| Qwen3-30B-A3B → 8B / 数学均值 | 56.5 | 56.8 | Table 4，PDF p. 14 |
| Qwen3-4B → 4B / 搜索均值 | 40.6 | 40.5 | Table 5，PDF p. 15 |
| 分域 4B teachers → 共享 4B / 数学均值 | 55.4 | 55.3 | Table 6，PDF p. 16 |
| 分域 4B teachers → 共享 4B / 搜索均值 | 41.0 | 41.0 | Table 6，PDF p. 16 |

[Table 4](https://arxiv.org/html/2607.04763v3#S5.T4) · [Table 5](https://arxiv.org/html/2607.04763v3#S5.T5) · [Table 6](https://arxiv.org/html/2607.04763v3#S5.T6)。OPD / ReOPD 共享 teacher target、batch size 与 update steps；实验在 8×H100 上运行。[§5](https://arxiv.org/html/2607.04763v3#S5)

【成本边界】Student 蒸馏训练阶段为零 tool calls，作者报告每 rollout 至少快 4 倍；若 teacher RL 轨迹不可直接复用，额外计入一次 teacher 轨迹采集后仍快于 2 倍。该数值是论文实验的 rollout 计时，不是任意任务端到端训练都加速 4 倍。[§5.1 / Fig. 8，PDF p. 19](https://arxiv.org/html/2607.04763v3#S5.SS2.SSS0.Px5)

## Assumptions
- 【事实】需要带 observations 的 teacher 轨迹池。默认复用 teacher GRPO 训练期间的轨迹，因此它可能混合多个 policy checkpoints；另有最终 teacher 重新采集的对照。[Table 7，PDF p. 19](https://arxiv.org/html/2607.04763v3#S5.SS2.SSS0.Px4)
- 【事实】Teacher 先经过 cold-start SFT 和 GRPO，student 从 cold-start 版本初始化。实验中的同 backbone teacher / student 仍为不同训练状态的模型，不是用户排除的 privileged self-distillation / OPSD。[§5 Models](https://arxiv.org/html/2607.04763v3#S5.SS0.SSS0.Px1)
- 【事实】验证场景是 Python-tool 数学与文本搜索，未包含多模态或 VLA。生成 student action 时仍需 teacher 分布监督，零环境调用不等于零 teacher query。

## Limitations / Failure Modes
- 【作者承认】轨迹池的覆盖与质量限制可学习内容；step index 只是 reliability 的粗代理，没有直接测量每个 prefix 的可靠性。[§6 Limitations，PDF p. 19](https://arxiv.org/html/2607.04763v3#S6.SS0.SSS0.Px1)
- 【事实】总体均值接近不等于每项不退化。例如 4B teacher 的单环境搜索中，Bamboogle 从 OPD 的 44.0 降至 ReOPD 的 37.6。[Table 5，PDF p. 15](https://arxiv.org/html/2607.04763v3#S5.T5)
- 【证据缺口】Tables 4-6 未列多 seed 方差 / 置信区间，0.1-0.3 的差异不能直接判为有统计意义的优劣；未审计代码或独立复核理论证明。
- 【解释】Replay 不让 student 执行错误 action 后继续收集真实反馈，因此它不能直接提供完整 student-induced recovery states；是否足够覆盖长程纠错，需要额外评测。

## Reusable Ingredients
- 【事实 → 设计】把 environment rollout 与 action 内的 student 自采样分开：固定轨迹池也能提供 student-generated token contexts 的稠密蒸馏监督。
- 【事实 → 设计】用单参数 step-decay sampling 调整监督位置，明确区分“改变 prefix 来源”与“改变 step 权重”。[§4](https://arxiv.org/html/2607.04763v3#S4)
- 【解释】比较训练成本时分别核算已有 teacher RL 轨迹复用、独立 teacher 采集、student tool calls 和 teacher inference，避免把条件性零环境成本理解为全流程免费。

## Open Questions
- 【开放问题】固定 teacher-prefix pool 在更长 horizon、错误 action 恢复和更大环境变化下，何时会不够？
- 【开放问题】直接测量 prefix reliability 能否稳定胜过固定 `kappa=0.6`？本文提出后续方向，未给出通用结论。
- 【开放问题】在相同总 teacher inference / 轨迹采集预算下，它与 online temporal curriculum 的收益边界分别在哪里？

## Claims
_No claims tracked yet — populate via /proof-checker._

本页只记录作者报告与原文阅读判断；本项目未复现实验或运行 proof-checker。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【解释】直接对应 [G1：多轮监督可靠性](../gap_map.md#g1)。与 [TCOD](wang2026_tcod_exploring_temporal.md) 相比，TCOD 控制在线交互深度 / teacher warm-start，ReOPD 改用离线 teacher histories 上的 action 自采样与 step sampling；这是本项目的比较，不代表论文声明 extends / supersedes TCOD。真实关联见 [graph](../graph/edges.jsonl)。

**收录判断：** 外部 teacher 的 Agentic OPD 方法；非 OPSD / self-distillation、多模态、VLA 或 benchmark 论文。

**来源与阅读范围（2026-10-14）：** [arXiv 2607.04763v3](https://arxiv.org/abs/2607.04763v3) · [原论文 HTML](https://arxiv.org/html/2607.04763v3) · [本地 PDF](../../papers/reopd-2607.04763v3.pdf)。重点读取 §§3-6，PDF pp. 12、14、15、16、19 目视核对 algorithm / tables / cost figure；未逐页精读全部 25 页，未使用二手总结，未审计代码或复现实验。召回来自用户指定的 [Awesome-Agentic-OPD](https://github.com/Zenghuang-Fu/Awesome-Agentic-OPD)。

## Abstract (original)

> We study on-policy distillation (OPD) for agentic tasks, where an LLM agent interacts with an environment over multiple turns and a student imitates a teacher over these multi-turn interaction histories. Fully online OPD is costly because each update requires fresh student rollouts through the environment and teacher queries at visited histories. We propose Replayed-Prefix On-Policy Distillation (ReOPD), an off-environment alternative that reuses pre-collected teacher trajectories as replayed prefixes: the student acts at selected steps, while the teacher provides dense per-step supervision without executing new environment interactions. We show that multi-turn OPD introduces a prefix trap: making histories more student-on-policy improves relevance to the student, but can query the teacher on histories where its target is unreliable. This creates a two-sided distribution shift between student occupancy and teacher reliability. ReOPD addresses this by treating multi-turn OPD as a reliability-aware prefix distribution design and implements it with a simple step-decaying sampling schedule that emphasizes early, lower-shift prefixes. Across mathematical reasoning with Python and search environments over multiple teacher and student model scales, ReOPD preserves or improves OPD-level accuracy, uses zero tool calls during student training, and is at least 4$\times$ faster per rollout than OPD. ReOPD therefore turns expensive agent-environment interaction into a reusable offline resource, enabling scalable distillation across tools, tasks, and environments.

