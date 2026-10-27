---
type: paper
node_id: paper:kim2026_pain_more_gain
title: "No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation"
authors: ["Seonghyeon Kim", "Chaeyun Jang", "Noah Lee", "Boseop Kim", "Juho Lee"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.34745"
  doi: null
  s2: null
tags: ["core", "initialization", "merging"]
added: 2026-10-15T03:47:15Z
---

# No Pain, More Gain: Iterative Merging for Effective Multi-Teacher On-Policy Distillation

## One-line thesis

IM-MOPD 在 OPD 过程中用 validation recovery 选择未恢复领域，迭代注入对应 teacher task vectors。

## Problem / Gap

【作者问题】固定 merge initialization 的初始分数不能预测 OPD recovery，最终系数与加入时机都会影响整合。

## Method

【事实】teacher/student 共享 reference，τ_i=φ_i−θ_ref；uniform merge 初始化。每 H=25 次 routed reverse-KL update 测 recovery，将未达 γ 的 task vectors 以 δ=.3 加到 student，继续 OPD（§3.2 Algorithm 1）。累计系数不局限 convex simplex。

## Key Results

【作者报告】Recovery 每域以 reference=0、对应 domain teacher=1 归一化，再对五域等权平均。Qwen3-4B：Uniform Merge+MOPD 53.8%、SFT Warm-up+MOPD 59.0%、IM 86.9%；1.7B 为 46.3%/46.5%/76.0%（Table 1）。固定最终累计系数，4B 全部训练前/训练后/迭代注入为 79.0%/23.3%/86.9%（Table 2）。

## Assumptions

共同 parameter reference、兼容架构、可访问 teacher weights；需周期性 validation。

## Limitations / Failure Modes

每次决策有 validation 开销，Tool Use 128 tasks、其余每域 256 prompts（App.A.4）；未核得完整端到端计时。不直接适用于参数空间不兼容的 teachers。

## Reusable Ingredients

【解释】固定最终 task-vector 系数、只改变注入时机的因果对照。

## Open Questions

【开放问题】validation 决策频率与额外成本的权衡，以及新域到来时的可扩展性？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心初始化与训练中 weight-space 注入；与 Δ-MOPD 的 logit-space shift 区分。

读取：2026-10-15，2609.34745v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.34745v1#S3)；[元数据](https://arxiv.org/abs/2609.34745v1)。发现来源：seed-sources.md。未保存本地 PDF。
