---
type: idea
node_id: idea:teach-back-independent-teacher-target
title: "先让 student 复述执行，再蒸馏 teacher 修正"
stage: proposed
outcome: pending
added: 2026-10-14T15:02:56Z
based_on: []
target_gaps: []
tags: ["agentic-opd", "method", "idea-creator-2026-10-14", "reserve"]
---

# 先让 student 复述执行，再蒸馏 teacher 修正

**stage:** `proposed`  ·  **outcome:** `pending`

2026-10-14 idea-creator：S8；生成模型 `gpt-6.1-sol`；未验证储备。同家族模型评审为provisional，未运行pilot。见[排序报告](../../idea-stage/IDEA_REPORT.md)及[原始候选](../../idea-stage/candidates-2026-10-14.json)。

## Thesis
具体方法：

1. 在 student 访问状态，teacher 给一个只依据现有可见信息的短提示。
2. student 据提示生成可执行 action，作为其理解方式的 teach-back。
3. teacher 依据原状态和 teach-back 输出最终正确 action 分布；student 在不含提示和 teach-back 的原历史上学习该独立 teacher target。

更新规则：a_b~π_S(·|h,hint_T)，随后 L=KL(q_T(·|h,hint_T,a_b)||π_S(·|h))；black-box teacher 可用其最终 action CE。训练目标始终来自独立 teacher，不使用 hinted student distribution 充当 teacher。

待验证假设：teacher 看到 student 如何误解提示后，能给出针对执行缺口的监督；擦除提示训练可将这种纠正转化为无 teacher 的行动能力。

查新结论（早期文献核查，不是效果验证）：C。[LENS](https://arxiv.org/html/2609.33409#S4)已有hint与hint-free内化，[OLIVE](https://arxiv.org/html/2609.36246#S3.SS2)已有teacher continuation。独立teacher最终target符合scope；剩余是**teach-back使teacher标签改变且更可学**，仅替换self teacher不足。

最小验证：比较直接 teacher action、hint-conditioned teacher action、hint→student teach-back→teacher correction；所有标签都来自独立 teacher，匹配总 teacher tokens，评测 teacher-free success。

同数据、同总成本的关键对照：相同teacher tokens：直接标签、hint-conditioned标签、teach-back后标签；部署均无hint。

## Key risks
交互只是在更贵地重现 teacher 本来就能给出的标签；最终 target 也可能过度依赖提示措辞。

评审补充：teacher可能本来就能直接给相同标签；额外交互只是更贵标注。

证伪条件：移除 teach-back 后效果不变，或匹配 teacher tokens 后优于基线的收益消失。

资源条件：独立 teacher 的两次短输出；student 一次额外训练期 action proposal；白盒分布或黑盒最终 action 均可。无需环境分叉。

估算：先做 10^3 个 student states；每状态约两次短 teacher 输出与一次 student teach-back。预计一至两周完成 pilot，部署维持单个无提示 student actor。 本轮没有GPU计时与效果数据。

## Connections
最近前作及剩余差异见上方查新结论；完整证据见[查新表](../../idea-stage/novelty-evidence-2026-10-14.md)。

