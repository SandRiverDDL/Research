---
type: idea
node_id: idea:student-draft-teacher-edit-policy
title: "把 teacher 的局部修正学成 student 编辑策略"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: []
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 把 teacher 的局部修正学成 student 编辑策略

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S5；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. student 在当前状态先生成完整 action draft。
2. 独立 teacher 以明确 edit 操作修复 draft 的工具名、参数或必要行动内容，而非重新写一套轨迹。
3. student 学习条件编辑策略；部署时由同一个 student 先 draft、再编辑并执行。

更新规则：L_edit=-log p_S(e_T|h,a_draft)，e_T 为 teacher 的编辑序列；修复后 action 由确定性 patch 应用得到。draft actor 可保留普通 OPD。全部编辑标签来自独立 teacher，不用 student 自身输出作 teacher target。

待验证假设：teacher 的完整示范可能超出 student 当前执行能力；围绕 student 自己的 draft 学习可执行修正，更容易内化为部署时的纠错能力。

查新结论（早期文献核查，不是效果验证）：C。与A8属**暂定同家族**；[SCoRe](https://proceedings.mlr.press/v306/lyu26j.html)、[DCR](https://arxiv.org/abs/2407.02397)覆盖纠错训练大框架，剩余是显式patch执行策略。

最小验证：比较普通 OPD、相同两遍推理预算的 self-review、teacher 全量重写蒸馏、teacher edit 蒸馏；测端到端 success、修正率与误改率。

同数据、同总成本的关键对照：固定draft、同修复信息、同部署tokens：patch、全量重写、普通self-review。

## Key risks
多一次 student 推理增加延迟；局部编辑不适合需要整体改换策略的错误。

评审补充：与A8相同；开放edit表示还容易变成普通重写监督。

证伪条件：收益只来自第二遍推理；或编辑后的正确内容被破坏，使 success 不升。

资源条件：独立 text teacher；可解析 action 格式；student 两遍推理。无需 teacher 部署调用或环境分叉。

估算：先收集 10^3–10^4 个 student drafts；每个新增一次 teacher edit 输出。预计一至两周实现，必须将部署第二遍 tokens 计入成本。 本轮没有GPU计时与效果数据。

## Connections
最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

