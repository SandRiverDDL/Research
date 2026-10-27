---
type: paper
node_id: paper:chen2026_branching_onpolicy_distillation
title: "Branching On-Policy Distillation"
authors: ["Dongyang Chen", "Shudong Liu", "Shubo Li", "Duoxun Tang", "Jinwei Liang", "Zehuan Wu", "Lewei Lu"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2610.13481"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-22T09:36:35Z
---

# Branching On-Policy Distillation

## One-line thesis
【作者方法】BranchOPD 在高不确定／高分歧位置分叉 student 接续，复用前缀扩大监督覆盖，并以 PBR 修复协议边界。

## Problem / Gap

【作者问题】单条 student rollout 每处只实现一个接续，有限预算下无法覆盖其它行为；仅给同一轨迹重加权不会增加监督状态。[§§3–4](https://arxiv.org/html/2610.13481v1#S4)

## Method

【作者方法】student top-20 entropy 与局部师生分歧分别做轨迹内 rank normalization 后混合选 fork。Agent 先选 turn 再选 turn 内 token，恢复对应环境状态，以 student 策略接续；默认 B=3、每处 k=2，最多七条轨迹。共享前缀只计一次，teacher 对主轨迹及分支的 student token 评分。[§§4.1–4.3，Eqs.6–11](https://arxiv.org/html/2610.13481v1#S4.SS1)

PBR 对 EOS／多余 closing-thought tag 等协议事件施加 token 集合概率约束，不依赖 teacher 是否能纠正重复。条件无偏结论只针对已选 fork 的接续统计，并以正确恢复环境为前提。[§§4.2、4.4](https://arxiv.org/html/2610.13481v1#S4.SS4)

## Key Results

【作者报告，未复现】ALFWorld ID/OOD 为 57.86/55.22%，Vanilla OPD 为 42.14/43.28%；给 Vanilla 也加 PBR 后为 49.29/49.25%，分叉的剩余增益应与此比较。WebShop 为 33.59%，Vanilla+PBR 30.47%。[Table 2](https://arxiv.org/html/2610.13481v1#S5.T2)

数学 avg@16 的三集合平均 44.37%，Vanilla 25.82%、Vanilla+PBR 38.94%；不能将数学总增益全归于分叉。[Table 1](https://arxiv.org/html/2610.13481v1#S5.T1)

## Assumptions

【设定与阅读范围】首发 2026-10-09，读取 v1 §§3–5、主表与成本附录 B.4。Agent 主 student 为 Qwen3-4B，teacher 为 Qwen3-30B-A3B（WebShop/Search-QA 使用 GRPO checkpoint）。需要 teacher token 评分、可恢复的环境和正确 continuation 分布；评测只执行单条 student 轨迹。[§5.1](https://arxiv.org/html/2610.13481v1#S5.SS1) 完整元数据：[arXiv](https://arxiv.org/abs/2610.13481)。

## Limitations / Failure Modes

【作者成本口径】相对七条独立 rollout，ALFWorld/WebShop 的 student 生成 token 节省 19.1%/31.2%，不含 teacher scoring、反传和 replay。另一个仅增加两条接续的 ALFWorld 设置，相对单 rollout 仍需 2.55×生成、3.02×环境步骤；不可将它混写为默认七条配置。[§5.4、Appendix B.4](https://arxiv.org/html/2610.13481v1#A2.SS4)

【解释】不可 replay 的真实工具难以直接应用；PBR 带来显著收益，比较必须控制该辅助项。所读主表未提供独立训练 seed 方差，不据此声称统计稳定。

## Reusable Ingredients

【解释】复用已访问前缀、将预算分散到多个信息量高的决策、只训练分支新生成后缀，以及把可形式化的协议错误从 teacher 语义评分中拆出。[§4](https://arxiv.org/html/2610.13481v1#S4)

## Open Questions

【开放问题】计入 teacher forward、环境恢复和 wall-clock 后，分叉相对独立 rollout 的优势还有多大？在 student 逐渐变得确定或环境存在隐藏状态时，分叉覆盖收益能否保持？

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

【直接相关】为 [G1](../gap_map.md#g1) 状态覆盖与成本、[G2](../gap_map.md#g2) 探索覆盖提供直接机制。已有不确定性／分歧选点和 student 分叉，不能再把这些本身当新贡献。

## Abstract (original)

> On-policy distillation (OPD) provides teacher supervision on student-generated trajectories, but a single trajectory realizes only one continuation at …

