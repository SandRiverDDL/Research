---
type: paper
node_id: paper:yin2026_slowfast_multiteacher_onpolicy
title: "Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation"
authors: ["Xiaofei Yin", "Tong Chu", "Jiyuan Fu", "Jun Lan", "Shuheng Zhou", "Huijia Zhu"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.02324"
  doi: null
  s2: null
tags: ["core", "multimodal", "capability-preservation"]
added: 2026-10-15T03:47:15Z
---

# Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation

## One-line thesis

SF-MOPD 以慢速 EMA reference 修正 teacher 的 log-prob 方向，兼顾视觉领域学习与一般能力保留。

## Problem / Gap

【作者问题】multimodal MOPD 破坏 general capability，而固定初始化约束又限制新学习。

## Method

【事实】slow=student parameter EMA（α=.999）；student→EMA 与 student→teacher log-prob differences 经 CenterNorm，内积为负时删除冲突投影，ridge=.001。修正 target JSD 加 β×原 MOPD JSD，8B β=.1、2B/4B β=1（§2 Eq.2–10）。

## Key Results

【作者报告】四 visual experts、同数据/预算，一 epoch：Qwen3-VL-8B general/domain/all avg=76.4/60.4/67.7，vanilla=73.3/59.0/65.5（Table 1）；删除 slow-fast projection 后 all avg 64.0（Table 2）。

## Assumptions

可比较 token distributions、额外 EMA model state/forward；训练与评测均为视觉语言。

## Limitations / Failure Modes

projection 在 log-prob distribution space，不是 parameter-gradient surgery。未给足以量化端到端额外成本的 timing 表；EMA 保留能力是设计假设。

## Reusable Ingredients

【解释】固定初始化、EMA constraint、冲突方向投影三者分离对照。

## Open Questions

【开放问题】文本独立 experts、teacher pool 更大或 EMA 漂移较快时能否保留原一般能力？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心多模态 MOPD；保留能力的直接证据，不能照搬为文本 MOPD 结论。

读取：2026-10-15，2610.02324v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.02324v1#S2)；[元数据](https://arxiv.org/abs/2610.02324v1)。发现来源：seed-sources.md。未保存本地 PDF。
