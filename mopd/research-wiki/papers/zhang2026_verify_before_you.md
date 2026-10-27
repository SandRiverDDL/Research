---
type: paper
node_id: paper:zhang2026_verify_before_you
title: "Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation"
authors: ["Zhiwei Zhang", "Zechen Sun", "Fei Zhao", "Kang Peng", "Bin Liang", "Huayu Deng", "Yao Hu", "Kam-Fai Wong", "Mu Chuan"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2609.02998"
  doi: null
  s2: null
tags: ["core", "verification", "gating"]
added: 2026-10-15T03:47:15Z
---

# Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation

## One-line thesis

TGOPD 用 teacher 多次答案验证决定 prompt 是否接受 OPD，否则使用 GRPO fallback。

## Problem / Gap

【作者问题】teacher 在具体 prompt 上失败时，密集模仿会传播不可靠监督。

## Method

【事实】routed teacher 独立生成三次，经 domain verifier，至少两次成功才用 dense OPD；否则关掉蒸馏、用 GRPO，两种信号不相加（§3）。

## Key Results

【作者报告】三域199 steps：4B 七任务54.54 vs53.40，35B-A3B61.94 vs60.99（Table 2）。35B CodeIO matched500cycles step time+5.9%（App.D）。

## Assumptions

可靠 verifier、domain routing、teacher 自回归 probe。

## Limitations / Failure Modes

三次 probe 是粗估计；scoring 仍对所有 prompts 执行。Mask-only 也改善，4B MOPD 中优于 fallback，因此 fallback 非普遍必要（Table 5）。

## Reusable Ingredients

【解释】probe admission、mask-only、GRPO fallback 三组独立比较。

## Open Questions

【开放问题】probe 成本与可靠性提升之间，最有利的预算区间是什么？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增核心 reliability gating；HTML 的 AllSpark Team 与 abs full authors 分开记录。

读取：2026-10-15，2609.02998v2 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2609.02998v2#S3)；[元数据](https://arxiv.org/abs/2609.02998v2)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
