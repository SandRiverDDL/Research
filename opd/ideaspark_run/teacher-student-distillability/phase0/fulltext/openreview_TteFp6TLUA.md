# Rethinking the Capacity Gap in On-Policy Distillation for Large Language Models

paper_id: openreview:TteFp6TLUA
tier: A
source_used: failed
warning: fetch failed across all paths; intro filled with abstract; method empty

## Intro

> **一句话**：capacity gap 假设的直接重审。 论文聚焦 OPD 中仍未充分研究的 capacity-gap issue：已有 gap work 多在 off-policy KD 中讨论 teacher assistant / router，本篇把问题放回 student-generated prefixes 上，问 frozen teacher 的分布是否对当前 student 可模仿。 实操含义：如果 teacher signal 超出 student 当前可表达/可搜索范围，OPD 可能只提供密集但不可用的目标。 - [作者 ack paper brief §2]: 相关 work 多处理 off-policy KD 的 teacher-student gap，OPD 中的 capacity gap 仍 underexplored。 - [作者 ack paper brief §3.1]: 论文以 student policy、frozen teacher 和 prefix-conditioned next-token distribution 建立 OPD 记号。 - [作者 ack paper brief §3-4]: capacity gap 被转化为 student-visited states 上 teacher signal 是否可学的问题。 - 上游：TAID (2025) — 通过 temporally adaptive interpolation 处理 student competence frontier。 - 同期：Rethinking OPD of LLMs (2026) — 都强调 teacher capability 必须能转化为 student 可利用方向。 - 同期：TGPO / Trust Region OPD (2026) — 都在处理 large policy divergence 下 teacher signal 失效。 - ✅ [作者 ack paper brief §2-4]: 直接挑战 OPD 中“teacher 越强越好”的默认假设。 - ⚠️ [作者 ack paper brief §5]: OpenReview 候选仍需核验接收状态、代码和实验可复现性。 未从 paper brief 核到 Table/Fig anchor 的数字不放入 headline number。

## Method


