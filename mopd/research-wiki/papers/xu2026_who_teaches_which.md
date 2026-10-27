---
type: paper
node_id: paper:xu2026_who_teaches_which
title: "Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning"
authors: ["Xun Xu", "Zaixi Zhang"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.15404"
  doi: null
  s2: null
tags: ["core", "verification", "rl-hybrid"]
added: 2026-10-15T03:47:15Z
---

# Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning

## One-line thesis

VG-OPD 按 criterion 验证 teacher 许可，在 student disagreement tokens 上加入稀疏蒸馏 advantage。

## Problem / Gap

【作者问题】整题 teacher selection 不能定位科学推理中谁应监督哪些 token。

## Method

【事实】四 capability LoRA experts；缓存 greedy probes，仅 criterion gain>δ 授权，teacher最低10% token log-prob±1 dilation作 mask，重叠处选一个。k̂=min(exp Δ−Δ−1,10)，detached负 advantage=−w k̂，加进 GRPO stream（§3 Eq.9–10）。

## Key Results

【作者报告】Qwen3-8B：GPQA-D/SciBench/ChemBench47.3/59.1/70.9，MOPD44.1/56.1/67.2（Table 1）。完整 median146.8s/step vs RL-only94.7s，+55%（App.B.6）。

## Assumptions

criteria bank、deterministic/graded verifiers、独立 RL-trained LoRA teachers，共享 base。

## Limitations / Failure Modes

detached sampled-token penalty，不是 full-vocab KL 直接回传；稀疏 mask 不省完整 teacher forward。text-only science4B/8B；单独 KD stream 可加速 entropy collapse，故联合 RL。

## Reusable Ingredients

【解释】who/where/how much 分离，以及 probe、scoring、verification 分账。

## Open Questions

【开放问题】criterion verifier 误差与 entropy collapse 如何随任务复杂度变化？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心多专家 OPD/RL hybrid；与 MT-SDPO 的 verified critique 路线区分。

读取：2026-10-15，2609.15404v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.15404v2#S3)；[元数据](https://arxiv.org/abs/2609.15404v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
