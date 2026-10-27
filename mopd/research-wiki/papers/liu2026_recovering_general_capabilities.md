---
type: paper
node_id: paper:liu2026_recovering_general_capabilities
title: "Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation"
authors: ["Ziyuan Liu", "Jiao Ou", "Jian Liang", "Ruiming Tang", "Cheng Luo"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2608.26735"
  doi: null
  s2: null
tags: ["core", "capability-preservation", "filtering"]
added: 2026-10-15T03:47:15Z
---

# Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation

## One-line thesis

UCMOPD 用双温采样与 entropy-calibrated endorsement 筛选轨迹和 token，恢复一般能力并保留 specialization。

## Problem / Gap

【作者问题】领域 SFT 后，恢复一般能力时探索与监督可靠性难以兼顾。

## Method

【事实】source-label routing；T=1 anchor/T=1.5 exploration，保留平均正 advantage 不低于 anchor 的轨迹。s=exp(min(log p_T+H_T,0))，正/负 advantage 分别以 s/1−s 概率保留（§3）。

## Key Results

【作者报告】4B role-play、同八 rollout 预算：general54.43 vs53.31、vertical45.00 vs43.38（Table 7）；medical general55.88 vs51.81（Table 2）。

【作者报告，gap重审补充】Table 2 medical主结果：UCMOPD的vertical avg60.95接近SFT specialist60.96，但general avg55.88仍低于base59.48，IFEval71.53低于base84.66。此处vertical为三个medical benchmarks，与CaMOPD原论文两项均分不同（[Table 2](https://arxiv.org/html/2608.26735v2#S4.T2)）。

## Assumptions

领域标签、teacher entropy、额外候选 trajectories 与 teacher scoring。

## Limitations / Failure Modes

endorsement 是分布内 proxy，不是外部正确性证明；没有核实 wall-clock 增量。采样过滤不等同免除前置生成开销。

## Reusable Ingredients

【解释】探索轨迹 admission 与 token endorsement 分开消融。

## Open Questions

【开放问题】teacher 过度自信时是否仍能可靠筛选？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心 recovery 方法；与 Trust 的跨 teacher allocation 区分。

读取：2026-10-15，2608.26735v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2608.26735v2#S3)；[元数据](https://arxiv.org/abs/2608.26735v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
