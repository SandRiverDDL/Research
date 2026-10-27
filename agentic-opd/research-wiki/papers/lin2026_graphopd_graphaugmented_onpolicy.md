---
type: paper
node_id: paper:lin2026_graphopd_graphaugmented_onpolicy
title: "GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents"
authors: ["Bohan Lin", "Liyi Chen", "Zhuoning Guo", "Muyang Li", "Qimeng Wang", "Yan Gao", "Yao Hu", "Yudong Zhang"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2610.08959"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent", "boundary-self-distillation"]
added: 2026-10-22T09:36:35Z
---

# GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents

## One-line thesis
【边界相关：自蒸馏】GraphOPD 用环境依赖图与行为快照分歧加权 KL，联合 GRPO；teacher 是 student 的 rollout 前快照。

## Problem / Gap

【作者问题】单靠局部分歧选择监督步骤，可能错过上游偏移，也可能高估对结果无关的动作差异。作者以轨迹结构补充分歧；但其训练设定是 GRPO 加 student 行为快照锚定，不是从外部专家迁移能力。[§§1、3.1](https://arxiv.org/html/2610.08959v2#S3.SS1)

## Method

【作者方法】规则式 State Transition Footprint 从动作／观察文本抽取实体状态变化，建立依赖边、回溯边和弱顺序边；依赖边按实体稀有度降权。图的随机游走稳态分布给出结构分数，与 action token 的当前 student／旧快照 log-prob 差异融合，再在每条轨迹内标准化成 sigmoid 软 mask。[§§3.2–3.4，Eqs.1–9](https://arxiv.org/html/2610.08959v2#S3.SS2)

最终是 mask 归一化的 forward KL 加 GRPO，固定系数 0.05；teacher 为每批 rollout 开始前冻结的 student 快照，非外部强 teacher。[§3.1、§3.4，Eqs.10–11](https://arxiv.org/html/2610.08959v2#S3.SS4)

## Key Results

【作者报告，未复现】Table 1 的 Qwen2.5-3B：ALFWorld Avg 88.6%，同表最佳基线 OPID 82.8%（+5.8 pp）；WebShop success 78.9%，GEPO 75.3%。同表 7B 的 SearchQA Avg 47.3%，低于 RLSD 49.0%，不能概括成所有设置均最优。[Table 1](https://arxiv.org/html/2610.08959v2#S4.T1)

结构分数的 executed-replay audit 报告 Spearman ρ=0.58、Hit@10%=0.48，样本为 30 条 7B 轨迹、每条 10 个决策、每处 4 个替代动作。[§4.4](https://arxiv.org/html/2610.08959v2#S4.SS4)

## Assumptions

【设定与阅读范围】首发 2026-10-06；读取 v2（2026-10-13）的方法、实验设置／主表、消融、分析及成本表。需要 terminal task reward、同 token 空间的行为快照及环境特定 footprint extractor。三种 student 为 Qwen3-1.7B、Qwen2.5-3B/7B-Instruct。[§4.1](https://arxiv.org/html/2610.08959v2#S4.SS1) 摘要仅保留短摘录，完整元数据见 [arXiv](https://arxiv.org/abs/2610.08959)。

## Limitations / Failure Modes

【解释】规则实体匹配可能漏掉隐式依赖或引入伪边；结构中心性是代理，局部 replay audit 不构成所有环境的因果信用保证。论文没有检验该 mask 对外部专家 teacher 的迁移收益。[§§3.1–3.2、4.4](https://arxiv.org/html/2610.08959v2#S3.SS2)

【成本口径】Table 6 的图构建占每训练 step 的 0.13%–0.31%，只衡量图处理开销，不是整个方法相对其它算法的总成本下降。[Table 6](https://arxiv.org/html/2610.08959v2#A2.T6)

## Reusable Ingredients

【解释】从已有环境日志提取依赖结构、按实体稀有度抑制伪边、轨迹内相对软 mask；核心训练不为每个状态额外生成反事实 rollout。Audit 的分支是分析成本。[§3.2、§4.4](https://arxiv.org/html/2610.08959v2#S3.SS2)

## Open Questions

【开放问题】换成外部固定 teacher 并保持相同 RL／teacher／预算时，结构与师生分歧融合是否仍有效？规则 extractor 的收益能否迁移到隐式状态、自由文本工具接口？

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

【边界收录】本次用户指定补录，故保留为 self-distillation 近邻；不计入外部 teacher Agentic OPD 的直接方法证据。可作为 [G5](../gap_map.md#g5) 结构信用路线的邻近 baseline，不能因此认定外部 teacher 的信用分配已被解决。

## Abstract (original)

> On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the …

