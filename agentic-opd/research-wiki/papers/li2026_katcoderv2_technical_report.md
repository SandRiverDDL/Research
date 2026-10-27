---
type: paper
node_id: paper:li2026_katcoderv2_technical_report
title: "KAT-Coder-V2 Technical Report"
authors: ["Fengxiang Li", "Han Zhang", "Haoyang Huang", "Jinghui Wang", "Jinhua Hao", "Kun Yuan", "Mengtong Li", "Minglei Zhang", "Pengcheng Xu", "Wenhao Zhuang", "Yizhen Shao", "Zongxian Feng", "Can Tang", "Chao Wang", "Chengxiao Tong", "Fan Yang", "Gang Xiong", "Haixuan Gao", "Han Gao", "Hao Wang", "Haochen Liu", "Hongliang Sun", "Jiabao Li", "Jingwen Chang", "Jun Du", "Junyi Peng", "Leizhen Cui", "Meimei Jing", "Mingqi Wu", "Shangpeng Yan", "Shaotong Qi", "Suzhe Xu", "Wenxuan Zhao", "Xianda Sun", "Xuan Xie", "Yanbo Wang", "Yao Xia", "Yinghan Cui", "Yingpeng Chen", "Yong Wang", "Yuze Shi", "Zhiwei Shen", "Ziyu Wang", "Ming Sun", "Lin Ye", "Bin Chen"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2603.27703"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# KAT-Coder-V2 Technical Report

## One-line thesis
【作者方法】KAT-Coder-V2 将分别 SFT/RL 的五个领域专家按任务路由到 student rollout，返回 sampled-token log-prob，联合优化 RL 和 OPD。

## Problem / Gap
【作者问题】多领域能力冲突以及离线专家轨迹的 exposure bias。 [原文 §3.4、§4.1–4.2、Table 2](https://arxiv.org/html/2603.27703v1)

## Method
【作者方法】KAT-Coder-V2 将分别 SFT/RL 的五个领域专家按任务路由到 student rollout，返回 sampled-token log-prob，联合优化 RL 和 OPD。 [原文 §3.4、§4.1–4.2、Table 2](https://arxiv.org/html/2603.27703v1)

## Key Results
【作者报告，未复现】§4.1／Table 2：SWE-bench Verified 79.6；这是完整模型配方结果，未隔离 OPD 效果。 [原文 §3.4、§4.1–4.2、Table 2](https://arxiv.org/html/2603.27703v1)

## Assumptions
【证据边界】阅读层级：摘要＋专家融合方法和主结果；依据 §3.4、§4.1–4.2、Table 2。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】§3.4 承认融合略有性能下降，与引言 lossless 表述有张力；不能把模型总分归因于 OPD。 [原文 §3.4、§4.1–4.2、Table 2](https://arxiv.org/html/2603.27703v1)

## Reusable Ingredients
【解释】分别记录专家来源、任务路由和可获取的 teacher log-prob 接口。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §3.4、§4.1–4.2、Table 2](https://arxiv.org/html/2603.27703v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2603.27703)。

> We present KAT-Coder-V2, an agentic coding model developed by the KwaiKAT team at Kuaishou. KAT-Coder-V2 adopts a "Specialize-then-Unify" paradigm that …
