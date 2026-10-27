---
type: paper
node_id: paper:wu2026_consolidating_rlvr_capabilities
title: "Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms"
authors: ["Siye Wu", "Kai Yang", "Yuchen Cai", "Xin Xu", "Peng-Yuan Wang", "Jiaxuan Wang", "Jiashun Liu", "Jiafei Lyu", "Yangkun Chen", "Saiyong Yang", "Yanghua Xiao"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2608.27409"
  doi: null
  s2: null
tags: ["evidence", "fair-baselines", "cost"]
added: 2026-10-15T03:47:15Z
---

# Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms

## One-line thesis

同源五域 experts/data 下，Merge、Mix RL 和 standard MOPD 呈现不同能力与成本取舍。

## Problem / Gap

【作者问题】不同 fusion paradigms 在共同基础上何时更有效？

## Method

【事实】共享 base/五域 data；Merge=θ0+.6Στ_i，Mix RL=混域 GRPO，MOPD=五 full-parameter experts 的 routed sampled-token reverse-KL，不含 fusion verifier reward（§3–4）。

## Key Results

【作者报告】Qwen3-4B 八 benchmarks 等权 mean@32：Merge63.70、MixRL62.26、MOPD63.31；IFBench41.0/39.8/47.3（Table 1）。含 teachers 制备的 MOPD 成本是 expert-training reference 的1.14×/1.19×（4B/8B，Table 2），fusion单独<.2×。

## Assumptions

共享初始化、参数兼容、可访问 full-weight experts。

## Limitations / Failure Modes

共享数据/teachers 不等于等计算预算；MixRL 更长训练。Teacher-bounded 是此 standard setup 的观察，不是所有 MOPD 的定理；未测 shift/iterative merge variants（App.F）。

## Reusable Ingredients

【解释】teacher preparation 与 fusion 成本分账、领域分数与非域平衡总体 mean 同时报。

## Open Questions

【开放问题】更异质 experts 或同域组合泛化会否改变三类方法相对优势？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增直接公平对照与成本证据；标准静态 merge 不能代表 IM-MOPD。

读取：2026-10-15，2608.27409v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2608.27409v2#S3)；[元数据](https://arxiv.org/abs/2608.27409v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
