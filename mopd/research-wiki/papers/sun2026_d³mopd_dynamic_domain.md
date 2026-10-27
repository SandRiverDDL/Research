---
type: paper
node_id: paper:sun2026_d³mopd_dynamic_domain
title: "D³-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation"
authors: ["Zechen Sun", "Zhiwei Zhang", "Fei Zhao", "Juntao Li", "Mu Chuan", "Huayu Deng", "Guojian Zhan", "Wenliang Chen", "Yao Hu", "Min Zhang"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2608.24987"
  doi: null
  s2: null
tags: ["core", "scheduling", "budget"]
added: 2026-10-15T03:47:15Z
---

# D³-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation

## One-line thesis

D³-MOPD 依据已有 reverse-KL 的相对量与下降速度，动态调整领域 prompt sampling。

## Problem / Gap

【作者问题】固定 mixture 在不同收敛速度的领域间浪费训练预算。

## Method

【事实】异步 watcher 用每域 EMA KL/初始 KL 与多窗口下降速度构成分数，经 softmax、domain floor、batch jitter 更新采样；loss、routing、prefill 不变（§3/App.B.3）。

## Key Results

【作者报告】Qwen3.6-35B-A3B 四域、256 steps：best-average checkpoint 七任务62.34 vs61.36（Table 1），单 checkpoint recovery .73 vs.48（App.D Table 6）。摘要 .97/.63 来自逐 benchmark 各取 peak。吞吐520 vs531 tokens/GPU/s。

## Assumptions

可分域 KL 日志、异步调度与固定 expert pool；无额外 teacher call。

## Limitations / Failure Modes

KL 反弹可让未收敛域失去预算；App.I 有可选修正。不能用 per-benchmark peaks 宣称一个 student 达97% recovery；长度 mixture 会影响吞吐。

## Reusable Ingredients

【解释】采样权重与 loss 权重分离、single-checkpoint 与 teacher-envelope 区分。

## Open Questions

【开放问题】KL 进度是否稳定代表 benchmark 进度，尤其在 non-monotonic learning 下？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心 scheduling；与 Open/DN loss weighting 不同。HTML 匿名，作者来自 abs 元数据。

读取：2026-10-15，2608.24987v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2608.24987v2#S3)；[元数据](https://arxiv.org/abs/2608.24987v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
