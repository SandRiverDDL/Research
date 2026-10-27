---
type: paper
node_id: paper:huang2026_katcoderv25_technical_report
title: "KAT-Coder-V2.5 Technical Report"
authors: ["Bo Huang", "Fengxiang Li", "Hao Xu", "Haoyang Huang", "Hongyi Fu", "Jinhua Hao", "Kun Yuan", "Minglei Zhang", "Pengcheng Xu", "Shiyang Liu", "Wenhao Zhuang", "Yuze Shi", "Zongxian Feng", "Chao Wang", "Cheng He", "Chongling Rao", "Deyu Cao", "Fan Yang", "Gang Xiong", "Haochen Liu", "Jiabao Li", "Jian Liang", "Jinghui Jia", "Jingwen Chang", "Jun Du", "Junyu Shi", "Min Li", "Mingqi Wu", "Qiang Gao", "Shangpeng Yan", "Shaotong Qi", "Shu Xu", "Shuo Zhou", "Tiankuo Xu", "Tong Zheng", "Weilun Zhao", "Xiancheng Meng", "Xianda Sun", "Xiaoyu Jiang", "Xunhao Jia", "Yao Xia", "Yimeng Xu", "Yinghan Cui", "Yingpeng Chen", "Yiwen Ning", "Yong Wang", "Yuxuan Sun", "Zhongsheng Liu", "Ming Sun", "Cheng Luo", "Chen Yang", "Han Li", "Kun Gai"]
year: 2026
venue: "arXiv"
external_ids:
  arxiv: "2607.05471"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# KAT-Coder-V2.5 Technical Report

## One-line thesis
【作者方法】KAT-Coder-V2.5 先做 expert-trajectory cold start，再按领域路由 reverse-KL OPD；依据 teacher/student top-k overlap 降权或屏蔽漂移后缀，使用 length-stratified batching。

## Problem / Gap
【作者问题】长 student 前缀漂移后，领域 teacher 的监督可能失准。 [原文 §5–5.1、§6.2、Table 4](https://arxiv.org/html/2607.05471v1)

## Method
【作者方法】KAT-Coder-V2.5 先做 expert-trajectory cold start，再按领域路由 reverse-KL OPD；依据 teacher/student top-k overlap 降权或屏蔽漂移后缀，使用 length-stratified batching。 [原文 §5–5.1、§6.2、Table 4](https://arxiv.org/html/2607.05471v1)

## Key Results
【作者报告，未复现】§6.2／Table 4：PinchBench Avg 94.9；未隔离 cold start、truncation 与 MOPD 的贡献。 [原文 §5–5.1、§6.2、Table 4](https://arxiv.org/html/2607.05471v1)

## Assumptions
【证据边界】阅读层级：摘要＋方法与主结果；依据 §5–5.1、§6.2、Table 4。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】top-k overlap 是可靠性代理；完整模型分数不能单独证明该代理或 MOPD 有效。 [原文 §5–5.1、§6.2、Table 4](https://arxiv.org/html/2607.05471v1)

## Reusable Ingredients
【解释】对长前缀监督明确记录截断条件及被丢弃的状态覆盖。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G3](../gap_map.md#g3)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §5–5.1、§6.2、Table 4](https://arxiv.org/html/2607.05471v1)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2607.05471)。

> We present KAT-Coder-V2.5, a coding-focused agentic model trained to act autonomously inside real, executable repositories rather than as a single-turn …
