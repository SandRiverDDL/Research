---
type: paper
node_id: paper:kotoge2025_can_compact_language
title: "Can Compact Language Models Search Like Agents? Distillation-Guided Policy Optimization for Preserving Agentic RAG Capabilities"
authors: ["Rikuto Kotoge", "Mai Nishimura", "Jiaxin Ma"]
year: 2025
venue: "ACL 2026 Main（arXiv comments 自报）"
external_ids:
  arxiv: "2508.20324"
  doi: null
  s2: null
tags: ["agentic-opd", "text-agent"]
added: 2026-10-14T14:09:06Z
---

# Can Compact Language Models Search Like Agents? Distillation-Guided Policy Optimization for Preserving Agentic RAG Capabilities

## One-line thesis
【作者方法】DGPO 先从独立 teacher 的正确轨迹做 cold-start KD；RL 阶段仅对错误预测加入 teacher KL guidance，保留成功 student 的探索。

## Problem / Gap
【作者问题】0.5–1B compact search agent 初始表现弱，RL 奖励稀疏、训练不稳。 [原文 §4、Table 2、Limitations](https://arxiv.org/html/2508.20324v4)

## Method
【作者方法】DGPO 先从独立 teacher 的正确轨迹做 cold-start KD；RL 阶段仅对错误预测加入 teacher KL guidance，保留成功 student 的探索。 [原文 §4、Table 2、Limitations](https://arxiv.org/html/2508.20324v4)

## Key Results
【作者报告，未复现】Table 2：Qwen2.5 3B→0.5B，七 QA 均值 DGPO .329，PPO .238，teacher .353；仅部分数据集超过 teacher。 [原文 §4、Table 2、Limitations](https://arxiv.org/html/2508.20324v4)

## Assumptions
【证据边界】阅读层级：摘要＋§4、主表与局限；依据 §4、Table 2、Limitations。未做代码审计或独立复现。

## Limitations / Failure Modes
【原文边界与本项目解释】实验集中于 Qwen2.5/Llama3 的 0.5–1B students 与文本 RAG；3B teacher 的额外时间9.5%只适用于该设置。提出 ARCap 不使其成为 benchmark-only 论文。 [原文 §4、Table 2、Limitations](https://arxiv.org/html/2508.20324v4)

## Reusable Ingredients
【解释】将冷启动、错误条件下的 teacher 监督及成功轨迹探索分开控制。

## Open Questions
【开放问题】在相同 teacher、任务、状态覆盖与总训练预算下，本文机制的独立收益是否稳定？

## Claims
本轮未建立经过独立验证的 claim；以上实验结果均为作者报告。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
【本轮定位】方法／报告。对应 [G2](../gap_map.md#g2)。完整筛选与跨论文比较见 [本轮调研](../awesome-agentic-opd-review.md)。原论文：[原文 §4、Table 2、Limitations](https://arxiv.org/html/2508.20324v4)。

## Abstract (original)

仅保留开头摘录；完整摘要见 [arXiv](https://arxiv.org/abs/2508.20324)。

> Reinforcement Learning has emerged as a dominant post-training approach to elicit agentic RAG behaviors such as search and planning from …
