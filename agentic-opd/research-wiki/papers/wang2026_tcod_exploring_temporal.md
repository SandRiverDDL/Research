---
type: paper
node_id: paper:wang2026_tcod_exploring_temporal
title: "TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents"
authors: ["Jiaqi Wang", "Wenhao Zhang", "Weijie Shi", "Yaliang Li", "James Cheng"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2604.24005"
  doi: null
  s2: null
tags: ["agentic-opd", "temporal-curriculum", "rollout-depth", "teacher-support"]
added: 2026-10-14T13:05:39Z
---

# TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents

## One-line thesis
【作者报告】TCOD 用由短到长的轨迹深度课程缓解多轮 OPD 的 KL 不稳定，并在三个文本 Agent 环境中提高成功率。

## Problem / Gap
【事实：作者实验】在 ALFWorld 上直接使用 full-rollout OPD 时，部分小 student 出现 KL 上升与成功率坍塌；逐 turn 的 KL 也随交互深度增大。作者将其称为 Trajectory-Level KL Instability。[§4.1 / Fig. 2，PDF pp. 3-4](https://arxiv.org/html/2604.24005v3#S4.SS1)

【作者解释】早期 action 错误会改变后续状态和 prefix，使 teacher supervision 难以利用。正文同时承认，KL 增大可能来自 student 模仿能力不足，也可能来自 teacher 在 OOD 状态下的不确定性；这些观察尚不能单独确定因果方向。

## Method
【事实】TCOD 改变训练时 student 暴露的轨迹深度，而不是提出新的蒸馏目标。论文将目标写为 student rollout 上的 `KL(teacher || student)`；此处按论文记号记录，未核对代码中的具体 loss estimator。[§3 / Eq. (2)](https://arxiv.org/html/2604.24005v3#S3)

1. **F2B：从起点逐步走远。** Student 从初始环境状态开始，先只 rollout 最多 `k` 个交互步，再逐渐扩展到完整 horizon；teacher 在 student 生成的 histories 上提供监督，无需成功 teacher demonstration。
2. **B2F：从成功轨迹末端逐步往前学。** 先用 teacher 的成功轨迹在环境中执行前缀，使环境到达中间状态，再交给 student 自采样续写；teacher 执行部分不参与梯度。随着 `k` 增大，teacher 前缀缩短，最终 student 从初始状态完成任务。它仍需在线环境交互，不是只重放文本 prefix 的离线训练。
3. **课程调度。** `k = k_start + floor(n / eta)`，并受任务长度 / 最大 horizon 限制；`n` 为 update step，`eta` 越大，扩展越慢。主设置 `k_start=1, eta=2`，另比较 `eta=4,6`。[§4.2 / Eqs. (3)-(5)、Algorithms 1-2，PDF pp. 5-6](https://arxiv.org/html/2604.24005v3#S4.SS2)
4. **实际训练闭环。** Actor / learner 异步运行，把轨迹拆为 sub-trajectory entries，并丢弃 policy version 差超过 2 的经验。因此实际数据有受控 staleness，不能理解成每个 update 都使用刚采样的当前 policy 轨迹。[§4.3，PDF pp. 6-7](https://arxiv.org/html/2604.24005v3#S4.SS3)

## Key Results
【事实：作者报告；未复现实验】主指标为 task success rate（SR，%）；差值用百分点，而非相对百分比。对照包括 zero-shot student、成功 teacher 轨迹上训练的 SFT 和 full-rollout vanilla OPD。

| Student / 评测设置 | Vanilla OPD | TCOD-F2B | TCOD-B2F | 原文 |
|---|---:|---:|---:|---|
| Qwen2.5-3B / ALFWorld Valid Unseen | 60.45 | 79.19 | 70.90 | Table 2，PDF p. 8 |
| Qwen2.5-7B / ALFWorld Hard | 13.22 | 18.18 | 20.66 | Table 2，PDF p. 8 |
| Qwen3-1.7B / 三环境 SR 均值，eta=2 | 0.17 | 18.57 | 18.64 | Table 3，PDF p. 9 |
| Qwen3-4B / 三环境 SR 均值，eta=2 | 27.64 | 29.54 | 29.41 | Table 3，PDF p. 9 |
| Qwen3-4B / WebShop，eta=6 | 30.12 | 29.87 | 29.05 | Table 3，PDF p. 9 |

Table 2 使用 ALFWorld GRPO-tuned Qwen2.5-7B teacher；Table 3 使用 Qwen3-30B-A3B-Instruct teacher，不能把跨表差异归因于单一设计因素。[§5.1 / Table 2](https://arxiv.org/html/2604.24005v3#S5.SS1)、[§5.2 / Table 3](https://arxiv.org/html/2604.24005v3#S5.SS2)

- ALFWorld Hard 的 teacher SR 为 6.61%；7B student 的 B2F 为 20.66%，比 teacher 高 14.05 个百分点。Hard 为从 **training split** 中按 teacher pass@10 失败筛出的 121 个任务；不能据此称为独立未见任务上的普遍超越 teacher。[§5.3，PDF p. 9](https://arxiv.org/html/2604.24005v3#S5.SS3)
- ScienceWorld / Qwen3-4B 的训练耗时：OPD 9.6 h、F2B 6.6 h、B2F 8.55 h；ALFWorld / Qwen2.5-7B：7.18 h、4.9 h、5.5 h。最大节省约 32%，不代表每个变体都省 32%。[§5.4 / Fig. 6，PDF p. 10](https://arxiv.org/html/2604.24005v3#S5.SS4)

## Assumptions
- 【事实】Teacher 能对 student histories 提供分布监督；评测为 ALFWorld、WebShop、ScienceWorld 的文本交互接口。ALFWorld 虽是 embodied task，这里的模型输入不是视觉 / VLA。[§5.1](https://arxiv.org/html/2604.24005v3#S5.SS1)、[Appendix A](https://arxiv.org/html/2604.24005v3#A1)
- 【事实】B2F 需要预先收集成功 teacher 轨迹，并能通过在环境中执行其 action prefix 到达中间状态。成功轨迹使用 teacher pass@10 收集；F2B 无此依赖。[§4.2 / §5.1](https://arxiv.org/html/2604.24005v3#S4.SS2)
- 【事实】报告配置为 250 training steps、8×H20；ALFWorld / ScienceWorld 最大 30 turns，WebShop 为 15 turns。Appendix D.4 的 evaluation history length 为 2 steps，因此不应把实验理解为不受限的完整长历史推理。[Appendix D.3-D.4，PDF pp. 17-18](https://arxiv.org/html/2604.24005v3#A4.SS3)

## Limitations / Failure Modes
- 【作者承认】B2F 的成功 teacher 轨迹有额外采集成本；固定课程进度未必适配其他环境或 teacher-student 组合。本文只验证三个文本环境。[Appendix A，PDF p. 14](https://arxiv.org/html/2604.24005v3#A1)
- 【事实】收益有明显模型依赖。1.7B 的大幅收益主要体现为从 OPD collapse 中恢复；4B 的平均提升较小，部分 domain / eta 设置下降，3B 的 F2B 在 ALFWorld Hard 也由 10.74 降至 9.92。[Tables 2-3，PDF pp. 8-9](https://arxiv.org/html/2604.24005v3#S5.SS2)
- 【证据缺口】已检查的 Tables 2-3 没有 seed 方差 / 置信区间；Appendix D.3 列 seed=42。亚百分点差异的统计可信度未确立。
- 【证据缺口】Fig. 6 没有拆清 teacher 成功轨迹预采集是否计入耗时；curriculum 也改变 rollout 数量和 token 总量，当前证据不足以证明 equal-total-cost 下仍有相同收益。[§5.4 / Fig. 6](https://arxiv.org/html/2604.24005v3#S5.SS4)
- 【解释】KL 和 SR 同时改善支持 temporal curriculum 的实用性，但未把 teacher OOD 失准与 student 容量 / 优化困难完全分离，不能将前者视为已被独立证实的唯一机制。

## Reusable Ingredients
- 【事实 → 可复用设计】用 student rollout horizon 作为 curriculum knob，并显式区分 F2B 的早期状态覆盖与 B2F 的 teacher-prefix warm start。[§4.2](https://arxiv.org/html/2604.24005v3#S4.SS2)
- 【事实 → 可复用诊断】联看 per-turn KL、trajectory KL、SR、action rounds 与 response length，定位 late-turn error accumulation，而不只看平均 loss。[Figs. 2 / 4 / 5](https://arxiv.org/html/2604.24005v3#S4.SS1)
- 【解释】比较方法时同时记录成功 teacher 轨迹成本、student 自采样步数、teacher query 和 policy staleness；这有助于区分监督稳定性改善与减少训练工作量带来的加速。

## Open Questions
- 【开放问题】在 teacher 预采集、环境交互、teacher query 与训练 token 的总预算一致时，TCOD 的收益还剩多少？
- 【开放问题】Late-turn KL 上升中，teacher 在 student 状态上的错误指导与 student 无法拟合正确指导各占多大作用？
- 【开放问题】更长 horizon、完整历史与更强 student 下，固定课程仍必要吗？自适应进度是作者提出的后续方向，本文没有验证。[Appendix A](https://arxiv.org/html/2604.24005v3#A1)

## Claims
_No claims tracked yet — populate via /proof-checker._

以上实验结果是论文作者报告，不是本项目验证过的 claim；本次未运行实验或 proof-checker。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【解释】这是本项目的直接方法论文：它通过控制 student 访问的交互深度和 teacher 介入位置，研究多轮 OPD 的监督稳定性。可用于比较 rollout-depth、teacher-intervention 与训练成本；关联 [G1：深度增加时的监督可靠性](../gap_map.md#g1)。关系事实以 [graph/edges.jsonl](../graph/edges.jsonl) 为准。

**收录判断：** 非 self-distillation / OPSD；使用独立、冻结的外部 teacher（即使某些 student 与 teacher backbone 同规模）。本文是方法论文，使用 benchmark 做实验，不是 benchmark 论文；本文验证的是文本 Agent，不属于多模态或 VLA。

**来源与阅读范围（2026-10-14）：** [arXiv 2604.24005v3](https://arxiv.org/abs/2604.24005v3) · [原论文 HTML](https://arxiv.org/html/2604.24005v3) · [本地 PDF](../../papers/tcod-2604.24005v3.pdf) · [作者代码链接](https://github.com/kokolerk/TCOD)（未审计或运行）。本页使用原论文 §§3-5、Appendix A / D；PDF pp. 5、6、8、9、10 已渲染目视核对算法、Tables 2-3 与 Fig. 6，pp. 17-18 提取文字核对配置。未使用 alphaXiv / deepxiv 二手总结，未声称逐页精读全部 20 页。

**召回入口：** [Awesome-Agentic-OPD](https://github.com/Zenghuang-Fu/Awesome-Agentic-OPD)，仅作候选发现；以上论文事实以原论文为依据。

## Abstract (original)

> On-policy distillation (OPD) has shown strong potential for transferring reasoning ability from frontier or domain-specific models to smaller students. While effective on static single-turn tasks, its behavior in multi-turn agent settings remains underexplored. In this work, we identify a key limitation of vanilla OPD in such settings, which we term Trajectory-Level KL Instability. Specifically, we observe that KL divergence increases together with a drop in success rate, and even after convergence, the KL remains high, leading to unstable training. This instability arises from inter-turn error compounding: as errors accumulate, the student is driven beyond the teacher's effective support, rendering the supervision signal unreliable. To address this, we propose TCOD (Temporal Curriculum On-Policy Distillation), a simple yet effective framework that controls the trajectory depth exposed to the student and progressively expands it from short to long with a curriculum schedule. Experimental results across four student-teacher pairs on three multi-turn agent benchmarks (ALFWorld, WebShop, ScienceWorld) show that TCOD mitigates KL escalation and enhances KL stability throughout training, improving agent performance by up to 18 points over vanilla OPD. Further evaluations show that TCOD can even surpass the teacher's performance and generalize to tasks on which the teacher fails. Our code is available at https://github.com/kokolerk/TCOD.
