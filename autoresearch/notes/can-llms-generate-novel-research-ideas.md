---
title: Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers
year: 2025
venue: ICLR 2025
paper_type: benchmark-eval
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [cherry-picked-showcase, hallucinated-novelty, evidence-tier-mixing]
design_knobs: [evaluation-protocol, evaluation-judge, novelty-check, iteration-control]
---

## 一句话定位

100+ NLP 专家 blind review 的人 vs LLM ideation 首个统计显著对照，novelty 上 LLM 赢。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `cherry-picked-showcase` | 早期 AI Scientist 类工作只用 1-3 个 reviewer 或全 LLM judge，样本量不足以做显著性判断 [PDF §1] | 招募 79 名专家做 blind review，49 idea × 3 condition，统一格式 + topic 匹配控制混淆 | 只覆盖 NLP 一个域；ideation 单步，未测 execution（后续 Si 2025b 补） |
| `hallucinated-novelty` | LLM idea 被判 novelty 更高（p<0.05），但 feasibility 略弱；单条判断难以确认这个 novelty 是否真实 | 承认 novelty judgment 本身就难，proposal 一个 end-to-end 执行研究做后续验证 | 未回答"novelty 高"是否等价于"idea 好" |
| `evidence-tier-mixing` | 前作大多用 LLM judge 替代人工，混淆 self-report 与 third-party | 全人工专家 blind review + 严格 Bonferroni 校正的 Welch t 检验 | 专家判断也有分歧，κ 一致性不高 |

## 方法机制

- 三 condition：expert-written、AI-generated、AI-generated + expert rerank；每 condition 49 个 idea [PDF §1, Fig 1]。
- LLM agent = retrieval augmentation + overgenerate-and-rerank（inference-time scaling）；关键设计"多生成后由 LLM 或人挑最好的一批" [PDF §1]。
- 主结果 [Fig 2]：AI idea 在 **novelty** 上显著高于人类（p<0.05），feasibility 略低，overall 与 excitement 也 AI 更高。
- 结论页明确列出两个 open problem：**LLM self-evaluation 失效** + **generation 多样性差**——这直接铺垫了后续 taste-gap（本项目已入 measuring-gap 卡）研究。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| AI Scientist v1 (Lu 2024) 类 | 用 LLM-as-reviewer 评自己产出，样本 1-3 篇 | 100+ 专家 + Bonferroni 严格控制 | 只测 NLP、只测 ideation |
| Baek 2025 (ResearchAgent) 类小规模评测 | 5-10 名 reviewer 打分 | 79 blind reviewer | 招募成本极高 |
| Measuring-Gap Chen 2026 | 逐条 novelty 打分 | 提供 baseline，被 measuring-gap 升级为分布评法 | 单条判断的 ceiling 已被 measuring-gap 揭示 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `evaluation-protocol` | Blind review + topic matching + style normalization + Bonferroni | LLM-as-judge / small human panel |
| `evaluation-judge` | 79 名 NLP 专家 | LLM reviewer / crowd worker |
| `novelty-check` | 人类 1-10 打分（novelty / excitement / feasibility / effectiveness / overall） | embedding similarity / LLM 判断 |
| `iteration-control` | overgenerate-and-rerank 一轮，无迭代 | multi-round refine / debate |

## 方法优缺点 / 适用边界

- 优势：
  - 该领域**方法学锚点**，后续所有 ideation 评测都在回应它，砍不掉。
  - 严格控制混淆（topic、style、格式统一），把"AI idea 看着新"从 anecdote 变成 p 值。
  - 承认 novelty 判断本身难，主动提议 execution 后续（Si 2025b 兑现）。
- 不足 / 风险：
  - 只测 NLP 域、只测 ideation 一步、只测一轮 rerank 后的 top idea——对"AI idea 分布长啥样"没答案。
  - 专家评审 novelty 一致性并不高，作者自己承认；单条打分方法学的天花板正是 measuring-gap（Chen 2026）用分布距离想突破的。
  - agent baseline 简单（RAG + rerank），未必反映 SOTA autoresearch pipeline 的真实水平。

<!-- meta:
authors: [Chenglei Si, Diyi Yang, Tatsunori Hashimoto]
url: https://arxiv.org/abs/2409.04109
arxiv_id: 2409.04109
pdf: papers/2409.04109-can-llms-generate-novel-ideas.pdf
brief: _meta/briefs/papers/2409.04109.md
survey: measuring-gap-human-llm-research-ideas
-->
