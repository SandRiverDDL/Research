---
type: paper
node_id: paper:wang2026_madopd_breaking_ceiling
title: "MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate"
authors: ["Jianze Wang", "Ying Liu", "Jinlong Chen", "Xuchun Hu", "Qilong Zhang", "Yu Cao", "Jun Wang", "Hua Yang", "Yong Xie", "Qianglong Chen"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2605.01347"
  doi: null
  s2: null
tags: ["adjacent", "agent", "debate"]
added: 2026-10-15T03:47:15Z
---

# MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate

## One-line thesis

MAD-OPD 让多个独立 teachers 在 student states 上 debate，再以自报 confidence 加权 token 监督。

## Problem / Gap

【作者问题】单 teacher 的能力上限和简单多 teacher 平均限制 student。

## Method

【事实】默认两 teachers/两轮，先独立回答再读取共同历史修订；student 不看 debate context。最终 confidence0–100 经 softmax 加权，各 teacher force-decode 同 student action；agent JSD、code reverse-KL，full vocabulary；OPAD 每 environment step 重新 debate（§4）。

## Key Results

【作者报告】Qwen3 14B+8B→4B，agent/code Avg25.69/48.12 vs强单 teacher23.26/44.41、naive MT24.14/41.97（Table 1）；debate无confidence weighting23.95/46.60（App.C Table 3）。

## Assumptions

shared vocabulary 和 teacher token distributions；teacher-only privileged debate transcript。

## Limitations / Failure Modes

自报 confidence 非 verifier correctness；K×R 调用与 context/step 增长，排除 API-only black box。non-thinking 主设置；非独立 domain-RL specialists consolidation（§6）。

## Reusable Ingredients

【解释】debate context 与 confidence weighting 分离对照。

## Open Questions

【开放问题】教师一致但共同错误时，如何避免 confidence 放大错误？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

邻近多 teacher deliberation OPD，保留供 aggregation/成本比较。

读取：2026-10-15，2605.01347v1 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2605.01347v1#S4)；[元数据](https://arxiv.org/abs/2605.01347v1)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
