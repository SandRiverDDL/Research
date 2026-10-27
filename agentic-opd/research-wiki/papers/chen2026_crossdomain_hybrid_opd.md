---
type: paper
node_id: paper:chen2026_crossdomain_hybrid_opd
title: "Cross-Domain Hybrid OPD for Generalizable Search Agents"
authors: ["Hongzhan Chen", "Xiaoyu Liu", "Dengming Zhang", "Minzhou Huang", "Dongliang Xu", "Jingcheng Xie", "Dongxiang Fang", "Bowen Qin", "Minsheng Hao", "Yaozong Shen", "Xiaojun Quan", "Mona Zhou", "Haosheng Zou", "Jeff Chen"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2608.02101"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# Cross-Domain Hybrid OPD for Generalizable Search Agents

## One-line thesis
【作者方法】Cross-Domain Hybrid OPD 将搜索 GRPO 与数学／代码／逻辑／科学专家 OPD 混合；专家先用中等难度 curriculum，再扩展全难度。

## Problem / Gap
【作者问题】搜索专项 RL 损害通用能力，产生 alignment tax。 [原文 §4.3、Algorithm 1、Table 2、§7](https://arxiv.org/html/2608.02101v1)

## Method
【作者方法】Cross-Domain Hybrid OPD 将搜索 GRPO 与数学／代码／逻辑／科学专家 OPD 混合；专家先用中等难度 curriculum，再扩展全难度。 [原文 §4.3、Algorithm 1、Table 2、§7](https://arxiv.org/html/2608.02101v1)

## Key Results
【作者报告，未复现】Table 2：GPQA 73.23→Stage I 69.95→Stage II 76.64；FS-O 55.00→50.00 是反例。 [原文 §4.3、Algorithm 1、Table 2、§7](https://arxiv.org/html/2608.02101v1)

## Assumptions
【证据边界】阅读层级：摘要＋混合目标、主表与局限；依据 §4.3、Algorithm 1、Table 2、§7。范围：间接相关：OPD 作用于通用 responses，搜索轨迹仍用 GRPO。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】不提供 teacher 逐步纠正搜索错误前缀的证据；也不能说所有通用能力均提高。 [原文 §4.3、Algorithm 1、Table 2、§7](https://arxiv.org/html/2608.02101v1)

## Reusable Ingredients
【解释】把搜索能力与通用能力保持分别评测，不混淆 OPD 实际监督对象。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。边界：间接相关：OPD 作用于通用 responses，搜索轨迹仍用 GRPO。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §4.3、Algorithm 1、Table 2、§7](https://arxiv.org/html/2608.02101v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2608.02101)。

> Recent advances in Reinforcement Learning (RL) have substantially improved the capabilities of autonomous search agents, enabling sophisticated planning, and iterative …
