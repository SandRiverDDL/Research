---
type: paper
node_id: paper:zhu2026_from_gradients_capabilities
title: "From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation"
authors: ["Siqi Zhu", "Suozhi Huang", "Kaixuan Zhang", "Yuheng Yang", "Zhanyang Jin", "Yihang Sun", "Jiaxuan You"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.02179"
  doi: null
  s2: null
tags: ["evidence", "optimization", "precision"]
added: 2026-10-15T03:47:15Z
---

# From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation

## One-line thesis

损失平均、Adam momentum 与数值精度会改变 teacher 信号的表观几何；更接近完整词表梯度并不稳定提升能力。

## Problem / Gap

【作者问题】teacher supervision 如何转为参数变化与 benchmark 能力，现有解释缺少受控拆分。

## Method

【事实】domain-routed student OPD；分解 global-token、domain-token、domain-response weighting；对比 sampled-token PG、top-k intersection KL、full-vocab gradient audits，并固定 optimizer state 做单步探测（§2–5）。

## Key Results

【作者报告】五 seeds、四任务：Adam-PG 三 averaging 的 mean 范围仅 .28 pp（Table 1）。DT/DR gradient cosine .68，经同 state Adam 更新为 .96（§3/Fig.2）。FP32 master weights 约97%变化，BF16舍入后仅7–9%（§4/Fig.5）。

## Assumptions

有限模型族/规模、四域 testbed；冻结当前 prefixes 的局部梯度探测。

## Limitations / Failure Modes

BF16 差分稀疏不证明实际学习稀疏；Adam shared momentum 的 aligned updates 不证明 teacher signals 对齐。SGD 优于 Adam 的结果限该 PG recipe（§4/7）。

## Reusable Ingredients

【解释】δU_d=U(g_d;H)−U(0;H) 去除 momentum baseline；FP32 master-weight 审计。

## Open Questions

【开放问题】更大模型下，局部 teacher 兼容性与长期能力增益的关系是否稳定？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增直接诊断证据；限制只凭 gradient cosine、loss scale 或 BF16 deltas 下结论。

读取：2026-10-15，2610.02179v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.02179v1#S3)；[元数据](https://arxiv.org/abs/2610.02179v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
