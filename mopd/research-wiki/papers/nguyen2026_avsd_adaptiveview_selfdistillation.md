---
type: paper
node_id: paper:nguyen2026_avsd_adaptiveview_selfdistillation
title: "AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals"
authors: ["Duy Nguyen", "Hanqi Xiao", "Archiki Prasad", "Zaid Khan", "Anirban Das", "Austin Zhang", "Sambit Sahu", "Hyunji Lee", "Elias Stengel-Eskin", "Mohit Bansal"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2605.20643"
  doi: null
  s2: null
tags: ["adjacent", "self-distillation", "aggregation"]
added: 2026-10-15T03:47:15Z
---

# AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals

## One-line thesis

AVSD 将多个 privileged views 的 geometric consensus 与经一致性约束的 arithmetic residual 结合成自蒸馏目标。

## Problem / Gap

【作者问题】直接平均多视角 privileged supervision 会丢失互补证据或引入 artifacts。

## Method

【事实】同一模型在 solution/answer/partial-solution 或 code/algorithm/feedback views 下评价同一 student prefix。qGtilde=exp(mean log q_m)，qA=mean q_m；J=log qA−log qGtilde≥0，λ=C×R，重建 target normalize(qGtilde exp(λJ))，reverse-KL 更新 student（§2 Eq.2–3）。

## Key Results

【作者报告】Table 1 五项 math/code Avg@8：Qwen3-4B AVSD/OPSD=59.9/58.2，8B=62.1/59.2；4B 每 update 46.7 vs41.5s，1.13×（App.B Table 2）。摘要 +5.5/+2.2 等指 math 子集，非全五任务。

## Assumptions

可用且高质量 privileged views；同 backbone teacher branches；训练 LoRA rank64、200 steps；Qwen3 训练时关闭 thinking mode。

## Limitations / Failure Modes

不是多个独立 frozen domain-expert consolidation。主要 math/code；advantage guarantee 未扩展至其他 losses，1.13× 只对指定硬件/4B 设置成立（App.A/C）。

## Reusable Ingredients

【解释】几何共识/算术残差分解及 gated residual≤|A_G| 的信号约束。

## Open Questions

【开放问题】独立 experts 的 base mismatch 会否破坏共识/残差解读？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

邻近 multi-view OPSD；证明多个 GT/privileged views 已有方法，不能直接宣称新贡献。

读取：2026-10-15，2605.20643v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2605.20643v1#S2)；[元数据](https://arxiv.org/abs/2605.20643v1)。发现来源：seed-sources.md。未保存本地 PDF。
