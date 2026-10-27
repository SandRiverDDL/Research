---
type: paper
node_id: paper:zhao2026_capable_teacher_myopic
title: "Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation"
authors: ["Shu Zhao", "Tan Yu"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2610.28586"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-22T09:36:35Z
---

# Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation

## One-line thesis
【作者方法】R2S 将接管轨迹知情的评分蒸馏回 teacher，再冻结 teacher 做普通 OPD，以缩小 rollout–scorer gap。

## Problem / Gap

【作者问题】teacher 能从 student 访问状态接管完成任务，却不代表其普通 next-token 评分会惩罚长程无效拖延；称之为 rollout–scorer gap。Table 1 的接管／rescued 诊断不能单独证明 student 已学会恢复。[§§3.2–3.3](https://arxiv.org/html/2610.28586v1#S3.SS3)

## Method

【作者方法】用初始 student 采轨迹，按 thinking token 平均 sampled reverse-KL 每 episode 取最大分歧 turn；最多 2,400 个状态，每状态 K=8 次 teacher takeover。按 consensus／judge 选可用接管，并取相应组最短轨迹作额外上下文。[§4、Appendix C](https://arxiv.org/html/2610.28586v1#S4)

冻结原 teacher 对未改写的 student 后缀 token 计算 takeover-informed 分布，再训练 teacher 副本在看不到 takeover 时拟合它；实现缓存并重归一化 top-16 targets，全参数训练 text decoder 一 epoch。重新冻结后替换普通 OPD scorer，student 不接收 takeover 示范。[Eq.3、Appendix C](https://arxiv.org/html/2610.28586v1#A3)

## Key Results

【作者报告，未复现】9B→4B 外部 teacher 设置：ALFWorld/WebShop/ScienceWorld success 为 81.9/55.9/47.8%，Vanilla OPD 65.8/34.6/34.6%；ALFWorld、ScienceWorld 是 seen/unseen 平均，WebShop 是 500 canonical goals。[Table 2](https://arxiv.org/html/2610.28586v1#S5.T2)

每个 cell 仅一条训练 run，± 是 final checkpoint 三次 sampled decodes 的 std，不能当训练 seed 方差。Consensus 和 judge 均优于 Vanilla，但主表三环境分别混用选择规则；并非统一单一 consensus 配置。[§5.1、Table 4、Appendix C](https://arxiv.org/html/2610.28586v1#S5.T4)

## Assumptions

【设定与阅读范围】首发 2026-10-20，读取 v1 §§3–5、主要表、Limitations 与附录 C。主 teacher 为 Qwen3.5-9B、Qwen3-30B-A3B-Instruct-2507，student 分别为 Qwen3.5-2B/4B、Qwen3-4B/8B。需要可 replay 环境、可训练 teacher 和 token 概率；文本工具任务，关闭 native reasoning mode，但 response 有短 deliberation。[§5.1](https://arxiv.org/html/2610.28586v1#S5.SS1) 完整元数据：[arXiv](https://arxiv.org/abs/2610.28586)。

## Limitations / Failure Modes

【作者成本】OPD 前额外支付初始 student 轨迹、最多 19,200 次接管、选择和一次 teacher fine-tune；各方法随后同为 150 steps，不代表总计算预算相同。仅 Qwen3/3.5 和三个文本环境，依赖 replay。[Limitations](https://arxiv.org/html/2610.28586v1#Sx1)

【解释与原文细节】Reward-free 不等于无验证信号：ScienceWorld 主配置使用环境 completion message，WebShop 用 judge；consensus／judge 也可能选错。一次静态修复能否覆盖训练后期新错误状态尚待验证。[Appendix C](https://arxiv.org/html/2610.28586v1#A3)

## Reusable Ingredients

【解释】将 teacher 的交互能力与 scorer 质量分开检验；让“看过接管结果”的 teacher 给 student 原 token 打软标签，再把知情评分蒸馏为无额外上下文的 frozen scorer。区别于直接对 takeover 做 label-SFT，也区别于在 student rollout 中持续接管。[§4、§5.3](https://arxiv.org/html/2610.28586v1#S5.SS3)

## Open Questions

【开放问题】匹配总接管／teacher fine-tune／OPD 计算后，相比在线介入方法还剩多少收益？Student 状态分布变化后，冻结 scorer 的可靠性如何漂移？Reward-free 筛选的错误率是否足以解释部分环境差异？

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

【直接相关】为 [G1](../gap_map.md#g1) 的错误前缀监督和 [G2](../gap_map.md#g2) 的 teacher 可靠性提供直接方法，纠正“teacher 会做就能打好 token 分数”的隐含假设。只将外部 teacher 主实验计为本项目证据；Table 3 的同模型自蒸馏另标边界。

## Abstract (original)

> Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. …

