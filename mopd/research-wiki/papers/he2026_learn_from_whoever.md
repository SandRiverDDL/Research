---
type: paper
node_id: paper:he2026_learn_from_whoever
title: "Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs"
authors: ["Xixiang He", "Xingming Li", "Baiqi Wu", "Qiyao Sun", "Xuanyu Ji", "Ao Cheng", "Qingyong Hu"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.02548"
  doi: null
  s2: null
tags: ["adjacent", "verified-feedback", "self-distillation"]
added: 2026-10-15T03:47:15Z
---

# Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs

## One-line thesis

MT-SDPO 缓存答案验证后的合格 teacher 集，将外部 critiques 与组内正确 self-anchor 合成 privileged EMA self-teacher。

## Problem / Gap

【作者问题】domain-matched teacher 未必答对具体样本，需要 sample-level reliability allocation。

## Method

【事实】每 teacher 预先回答 MCQ，verifier 缓存合格集合；对错误 student rollout 请求合格 teachers critiques，经 lexical sanitizer 后连接。排除自身的组内正确 peer 作 self-anchor；EMA teacher 看 privileged context，student 不看；masked importance-weighted top100+tail JSD（§4 Eq.2–7/App.B.1）。

## Key Results

【作者报告】matched teacher coverage 52.94%、任一合格 65.69%（Fig.3）。Qwen3-8B 科学三域、100 updates、每域79 held-out samples Avg@16：Macro 62.47→67.11，Worst 49.29→64.08，Gap 20.96→5.30（Table 1）。

## Assumptions

可验证 single-reference MCQ、可获得文本 critiques；EMA τ=.05。

## Limitations / Failure Modes

缓存一次正确答案不证明后续 critique 正确，lexical sanitizer 不保证排除 paraphrased leakage。小 Qwen 的 gap 缩小同时 Macro 下降；Llama 无 online 净增益。反复 critique 成本随错误 rollouts/eligible teachers 增长。

## Reusable Ingredients

【解释】verified eligibility、feedback aggregation、self-anchor 的分离消融。

## Open Questions

【开放问题】开放式答案、非 lexical leakage 与无正确 teacher 样本如何可靠处理？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

邻近专家反馈自蒸馏；直接 token target 来自 privileged EMA self-teacher，非多个外部 logits 的直接平均。

读取：2026-10-15，2609.02548v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.02548v1#S4)；[元数据](https://arxiv.org/abs/2609.02548v1)。发现来源：seed-sources.md。未保存本地 PDF。
