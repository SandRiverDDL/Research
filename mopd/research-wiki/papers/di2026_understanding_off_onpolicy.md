---
type: paper
node_id: paper:di2026_understanding_off_onpolicy
title: "Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives"
authors: ["Qiwei Di", "Xuheng Li", "Kaixuan Ji", "Chenggong Zhang", "Heyang Zhao", "Quanquan Gu"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.38666"
  doi: null
  s2: null
tags: ["theory", "aggregation"]
added: 2026-10-15T03:47:15Z
---

# Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives

## One-line thesis

sequence-level forward/reverse KL 分别对应 arithmetic/geometric teacher 聚合；reverse-KL aggregate 的 token conditionals 还依赖 continuation。

## Problem / Gap

【作者问题】多 teacher off/on-policy 的目标与 sample complexity 是否等价？

## Method

【事实】tabular sequential distillation 每轮抽一个 teacher；forward-KL 用 teacher-prefix frequency 和 smoothing，reverse-KL 用 student triples 的 teacher log-probs、optimistic bonus 与 backward recursion（§3–5）。

## Key Results

【作者报告】无 LLM benchmark 主表。Theorem4.3 expected-regret≤4SA^H log T；Theorem5.5 为 Õ(B²H²SA^H log T)。Fig.1 合成 N=10/expert weight .9 的聚合正确率在 q≈.7617 交叉（§6）。

## Assumptions

tabular horizon；reverse-KL 分析另要求 full-support reference 与 teacher/reference log-ratio 有界 B（Assumption 5.3），forward-KL 分析不依赖这两项。

## Limitations / Failure Modes

state space 随 H 指数增长，不能视为可规模化 LLM recipe。sequence-level geometric optimum 的 token conditional 不等于简单逐 token geometric average。

## Reusable Ingredients

【解释】区分 data source 与 divergence target，以及低权重错误自信 teacher 的影响。

## Open Questions

【开放问题】实际 LLM function approximation 和 teacher-support truncation 下哪些定性结论保持？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增聚合理论；不将理论/合成数字混入实证排行榜。

读取：2026-10-15，2609.38666v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.38666v1#S3)；[元数据](https://arxiv.org/abs/2609.38666v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
