---
type: paper
node_id: paper:fang2026_latentmopd_latent_multiteacher
title: "Latent-MOPD: Latent Multi-Teacher On-Policy Distillation"
authors: ["Zhengyu Fang", "Seoyeon Hong", "Jie Yang", "Muyang Li", "Koyoshi Shindo", "Brandon Joseph Lwowski", "Jing Li"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2610.02381"
  doi: null
  s2: null
tags: ["core", "representation"]
added: 2026-10-15T03:47:15Z
---

# Latent-MOPD: Latent Multi-Teacher On-Policy Distillation

## One-line thesis

Latent-MOPD 结合 routed token OPD 与 teacher hidden-state 对齐，以每 teacher crossfade schedule 协调监督。

## Problem / Gap

【作者问题】token-only OPD 不利用 specialist 内部表示，多 teacher latent targets 又存在深度、宽度和时序不兼容。

## Method

【事实】domain-pure updates 轮转 math/code/logic；teacher 同时给 token/hidden-state target。L2-normalized representation MSE；同族最后三层 identity map，跨设置最后一层 shared linear projector、最后 2000 tokens。每 teacher 独立时钟从 latent crossfade 至 token-only（§3 Eq.1–3/App.A）。

## Key Results

【作者报告】Norm 以 base=0、per-benchmark best-teacher envelope=1 归一化。same-family 1.5B、62 updates：Norm .90→1.05，9/9 benchmarks 超过 token-only（Table 1）。三只 7B teachers→1.5B：Norm .16→.26，AIME24 36.5→39.4（Table 2）。所谓 cross-family 仍同 Qwen backbone、共享 tokenizer。

## Assumptions

固定领域标签、可访问 hidden states、共享 tokenizer；手设 representation coefficient。

## Limitations / Failure Modes

domain-pure 91.7 vs interleaved 43.2 的 collapse 证据来自 all-layer representation-only control，不代表所有混合 MOPD。3/28 层节省 89.3% 是 selected target-state storage，非完整训练成本（§5/App.J）。

## Reusable Ingredients

【解释】token/latent 两监督 channel 及 schedule/batch-organization 分离对照。

## Open Questions

【开放问题】不同 backbone/tokenizer 下共享 projector 是否足够？表示收益是否覆盖 target storage 和 forward 成本？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心 latent supervision 方法；62 步处理 1,984 prompt presentations，不把 17,856 pool size 当处理量。

读取：2026-10-15，2610.02381v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2610.02381v1#S3)；[元数据](https://arxiv.org/abs/2610.02381v1)。发现来源：seed-sources.md。未保存本地 PDF。
