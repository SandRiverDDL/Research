---
type: paper
node_id: paper:shen2026_when_topk_misses
title: "When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation"
authors: ["Jiabin Shen", "Guang Chen", "Chengjun Mao"]
year: 2026
venue: "arXiv preprint (venue unverified)"
external_ids:
  arxiv: "2607.07050"
  doi: null
  s2: null
tags: ["evidence", "agent", "logit-support"]
added: 2026-10-15T03:47:15Z
---

# When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation

## One-line thesis

teacher top-K 可保留几乎全部概率质量，却遗漏纠正 student 工具调用决策所需的低概率坐标。

## Problem / Gap

【作者问题】两 teacher routed OPD 的 over-calling 不能仅用整体 loss 或 token exposure 解释。

## Method

【事实】tool/response teachers 在 student prefixes 上做 top-32 renormalized JSD；full-vocab frozen audits、forced-entry replay、首位置/全位置 support restoration 与非工具 placebo 隔离遗漏机制；再比较 union support、loss shaping、decoding bias（§2–5）。

## Key Results

【作者报告】Qwen3.5-9B response top32 保留 .999900 teacher mass，却仅 .4% 的500 prompts 含 <tool_call>（Table 1）。全位置恢复使 over-calling 14.20±2.08%→3.73±.51%，required-call recall 91.45→79.07%（三 seeds，Table 2）。

【作者报告，gap重审补充】support union：APIGen误调用14.2→7.4%、recall91.5→87.0%；BFCL local dialogue exact7.04→4.12%、required coverage92.90→81.22%。返回坐标+21.5%、steady-state step time+16%；同训练步数并非等计算预算（[§4.2](https://arxiv.org/html/2607.07050v6#S4.SS2)、[Tables 4–5](https://arxiv.org/html/2607.07050v6#S5.T4)）。

## Assumptions

top-K 接口、可额外审计完整词表；主要因果链限定 Qwen，Llama 复制支持不对称。

## Limitations / Failure Modes

降低 over-calling 同时牺牲 required calls 与 dialogue exact；不能只用单一行为指标判优。Support union 有额外 queries/训练成本，loss shaping 不补回遗漏坐标（§4–6）。

有full-vocab frozen audits，但没有full-vocab training对照；不能推断完整监督仍失败。BFCL local exact为作者执行/状态指标，未计最终自然语言质量；restricted-renormalized JSD机制不能自动外推为所有MOPD目标。

## Reusable Ingredients

【解释】mass retention、coordinate coverage、gradient fidelity、完整 interaction success 联合诊断。

## Open Questions

【开放问题】其他决策 token 或多域生成中，关键 tail support 是否同样重要？

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

新增 Agent 直接证据；旧检索名 Behavior Leverage Imbalance 属同 ID 旧版，本页核查 v6（2026-09-05）。

读取：2026-10-15，2607.07050v6 HTML 的方法、主要实验与相关限制，非逐页全文精读。来源：[原文章节](https://arxiv.org/html/2607.07050v6#S3)；[元数据](https://arxiv.org/abs/2607.07050v6)。发现来源：补搜 web/arXiv；扩展目录仅用于发现。未保存本地 PDF。
