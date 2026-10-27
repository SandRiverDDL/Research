---
type: paper
node_id: paper:tian2026_beyond_domainrouted_supervision
title: "Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation"
authors: ["Shi-Yu Tian", "Yong Liu", "Ximan Liu", "Tianrui Zhu", "Sule Bai", "Xinwei Yang", "Ruiqi Liu", "Kun-Yang Yu", "Ming Yang", "Zhi Zhou", "Yu-Feng Li", "Yipeng Sun", "Gu Simiu"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.13521"
  doi: null
  s2: null
tags: ["core", "cross-teacher", "gradient"]
added: 2026-10-15T03:47:15Z
---

# Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation

## One-line thesis

Road MOPD 在同一 student trajectory 上引入辅助 teachers，以 token agreement 和受约束梯度修正保护跨域能力。

## Problem / Gap

【作者问题】domain routing 分离监督来源，但共享参数仍发生 math/code 与 medical 能力退化。

## Method

【事实】保留主 teacher，其余 teacher 同轨迹作辅助 critic。相对冻结 reference 的 log-prob 信号经 tanh agreement 调制；主/辅助 OPD 梯度冲突时，逐 tensor 部分投影，并以主梯度 norm floor 限制修改，多辅助依次处理，再执行 AdamW（§3 Eq.1–11）。无新增 rollout。

## Key Results

【作者报告】Qwen3-4B Math×Medical：Medical avg 39.45→48.23，总 avg 42.71→47.92（Table 1）；三域 Math×Code×Medical 总 avg 49.76→52.89（Table 3）。Math Avg@32、Code Avg@4、Medical Avg@1，先域内再域间平均。

## Assumptions

辅助 teacher 偏好只作 compatibility signal，不要求其能解决主域任务；需要额外 scoring 和辅助梯度。

## Limitations / Failure Modes

约束是同轨迹 auxiliary loss 的局部梯度，不能保证 AdamW 后辅助域 benchmark 不退化（§3.3）。最多三域；App.D 未给统一 overhead 倍率。

## Reusable Ingredients

【解释】token 调制与梯度约束的分离对照、同轨迹的辅助教师约束。

## Open Questions

【开放问题】非主域 teacher 的偏好何时能预测该域能力保留？更多 teachers 的评分和反传成本是否可控？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心跨域干扰方法。与 UP-MOPD 的 optimizer 后投影属于机制对照，未核实两篇直接互引。

读取：2026-10-15，2610.13521v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.13521v1#S3)；[元数据](https://arxiv.org/abs/2610.13521v1)。发现来源：seed-sources.md。未保存本地 PDF。
