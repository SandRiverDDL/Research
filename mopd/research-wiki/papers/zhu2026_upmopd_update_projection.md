---
type: paper
node_id: paper:zhu2026_upmopd_update_projection
title: "UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation"
authors: ["Taojie Zhu", "Jing Jin", "Yuan Xia", "Chenyang Ding", "Qunshan He", "Wanke Xia", "Tao Sun", "Yan Chen", "Jian Wang", "Jinjie Gu", "Tao Feng"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.08398"
  doi: null
  s2: null
tags: ["core", "update-protection"]
added: 2026-10-15T03:47:15Z
---

# UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation

## One-line thesis

UP-MOPD 直接投影 AdamW 实际候选 displacement，而非仅修正送入 optimizer 的梯度。

## Problem / Gap

【作者问题】动量、逐坐标缩放及 weight decay 可破坏梯度投影的一阶可行性。

## Method

【事实】原始混合梯度更新 AdamW state 并得到 Δ0；在相同 trajectories replay 各域梯度 G，求 min 0.5||Δ−Δ0||² s.t. GᵀΔ≤0 的 domain-dimensional dual QP，直接提交 Δ*，保留原 optimizer state（§2 Eq.1–14）。

## Key Results

【作者报告】Qwen3-4B medical–general 八指标 mean：M-OPD/GP/UP=59.13/59.00/60.03（Table 1，最后三 checkpoint 平均）。SmolLM3-3B 六任务 avg：Open/GP/UP=30.85/31.63/32.67（Table 2）。8×H200 late 200-step window step time 66.55→94.76s，约 1.42×（App.D.3 Table 9）。

【作者报告，gap重审补充】medical–general设置中，UP的HealthBench-Hard38.57接近medical teacher39.06；IFEval80.90优于M-OPD77.94，仍低于initial/general teacher86.88。general teacher监督使用DAPO数学prompts；这些数字显示能力残差，未确诊其原因（[§3.1/Table 1](https://arxiv.org/html/2610.08398v1#S3.T1)）。

## Assumptions

可按 active domain 分解的可微损失；需要额外 domain gradient replay。

## Limitations / Failure Modes

只保证 current-batch first-order non-increase，不保证有限步长下损失或 benchmark 单调（§2.3）。仅两/三个 teacher；QP 低维不意味着完整训练开销低。

## Reusable Ingredients

【解释】把 gradient、optimizer state、最终 displacement 分开检查；GP 与 UP 同设置对照。

## Open Questions

【开放问题】更多 teacher 的梯度 replay 与可行域收缩，会怎样影响有效学习速度？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心 optimizer/update 方法；成本证据比只报告 projection 运算耗时更完整。

读取：2026-10-15，2610.08398v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.08398v1#S2)；[元数据](https://arxiv.org/abs/2610.08398v1)。发现来源：seed-sources.md。未保存本地 PDF。
