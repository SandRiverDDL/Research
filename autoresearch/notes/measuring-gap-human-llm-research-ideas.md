---
title: Measuring the Gap Between Human and LLM Research Ideas
year: 2026
venue: arxiv
paper_type: critique-audit
lifecycle_role: critique-anchor
boundary_risk: none

failure_modes: [hallucinated-novelty, cherry-picked-showcase, reviewer-model-hacking, evidence-tier-mixing]
design_knobs: [evaluation-protocol, evaluation-judge, novelty-check, evaluation-scope]
---

## 一句话定位

分布级 audit：LLM ideation 系统性坍缩到 bridge/synthesis 一小簇 research taste。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `hallucinated-novelty` | 单条 idea 看起来 novel/feasible，但整体分布只覆盖人类 taste 的窄区，是"看似新颖的模板化" | 用 11,683 篇人类论文构造 paired human vs LLM idea 语料，做分布对比而非逐条打分 [PDF §3, §4.2] | 只做 ML+Nat Comm 两个域；未验证 taste 收敛是否等价于 downstream 影响低 |
| `evidence-tier-mixing` | 现有 ideation 评测混用 novelty/feasibility/expert preference 三档，逐条评难反映分布性偏差 | 引入 opportunity pattern × method paradigm 两轴 taxonomy，用 GPT-5.4-mini 做自动标注（κ≈0.81-0.93）[Table 1] | 标注仍是 LLM-judge，二次 reviewer-model-hacking 风险；只做了 150 篇人工核对 |
| `reviewer-model-hacking` | thinking mode 反而把分布**推离**人类（Qwen3-8B bridge 49.7%→71.1%，synthesis 38.7%→52.2%）[Table 4] | 用分布距离而非"更好/更差"作为 metric | 未证明这与真实 review outcome 挂钩 |
| `cherry-picked-showcase` | 早前 human-vs-LLM ideation 研究只报最强 idea 的 novelty；本文取整批 | paired same-prior-work-context 生成 | 所选 prior work 由 LLM 反向抽取，可能自带 bias |

## 方法机制

- 每个样本 = 4-8 篇 related work 的 (title, abstract)，输出 = (motivation, method) 结构化 idea；human idea 从真实论文抽取 [PDF §3.1]。
- 两轴 taxonomy：**opportunity pattern**（7 类：puzzle/contradiction、explanation gap、scope mismatch、evidence gap、bridge opportunity、failure/risk gap、resource bottleneck）× **method paradigm**（7 类：synthesis、relax/extend、robustification、formal derivation、empirical mapping、artifact/system、optimization）[Fig 2]。
- taxonomy 从 NSF/NIH/AHRQ/DARPA 提案指南提炼，150 篇 held-out 上迭代 [PDF §3.3]。
- 分布距离用 TVD / JSD / normalized entropy；诊断分：surface stitching、bottleneck specificity、boilerplate [PDF §3.4, §4.3]。
- 主结果 [Table 1]：9 个模型全部远离 human，opportunity 轴上最好的 Gemini-3.1-Pro TVD=0.348；bridge opportunity 人 12.1% vs LLM 47.1-64.2%；synthesis 人 5.1% vs LLM 22.5-38.7%。
- Full-paper context ablation [Table 2]：给 LLM 读全文而非摘要，TVD **不降反升**（Qwen3-8B +0.054/+0.062），"给更多上下文"不是解药。
- Reasoning ablation [Table 4]：thinking mode 让分布进一步向 bridge+synthesis 收敛，即 CoT 放大而非缓解 taste bias。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Si et al. 2025a (NAACL "AI generates novel ideas") | 单条 idea 打分，只看 novelty/feasibility | 分布级对比，暴露 taste 收敛 | 依赖 LLM annotator；taxonomy 只 7×7，粗粒度 |
| AI Scientist v1/v2、Agent Laboratory | 端到端 pipeline，未刻画 ideation 环节的偏差 | 只测 ideation 单步、控制 prior-work 输入 | 无法说明这些系统在实际使用中最终产出的 taste 分布 |
| 通用 human-vs-LLM text 检测 (Gehrmann 2019, Guo 2023) | 关注 token/likelihood 层面差异 | 上升到 research contribution 类型层面 | taxonomy 归属仍是解释性判断，非可复现测量 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `evaluation-scope` | 只评 ideation 单步（motivation+method），控制 prior-work 输入 | 端到端 paper 产出 / experiment 成功率 |
| `evaluation-judge` | GPT-5.4-mini 自动标注 + 150 篇人工 κ 校验 | 全人工专家评分 / reviewer-model rubric |
| `novelty-check` | 抛弃"逐条 novelty"，改用与 human reference 分布的 TVD/JSD/entropy | embedding 相似度 / LLM-as-judge preference |
| `evaluation-protocol` | paired same-context ideation，同 prior-work 下 human vs LLM | 开放式 "propose an idea about X" |

## 方法优缺点 / 适用边界

- 优势：
  - 提供一个可复用的 ideation audit 协议，特别是"分布级"这一维度目前 autoresearch 评测里几乎没有。
  - 明确指出 chain-of-thought / full context 都不是万灵药，反而放大 taste bias——对 autoresearch pipeline 里"多让 agent 想更久"的直觉是反证。
  - taxonomy 跨 ML + 自然科学两域稳定，说明 bridge/synthesis 收敛不是 CS 独有。
- 不足 / 风险：
  - 关键判断仍靠 LLM annotator（GPT-5.4-mini），存在 annotator 与被测模型同源污染风险；κ 在 150 篇 held-out 上高，但未做 out-of-domain 稳定性测试。
  - "分布距离大 = idea 差"是隐含前提；人类 idea 分布是否本身就是 gold standard 未讨论（可能人类也有 taste bias，只是不同）。
  - prior-work 集合由 LLM 反向抽取，可能已经过滤掉 human 真正读过的非核心引用，导致 human 也在"受限 context"下工作。
  - 未刻画时间演化：LLM 生成的 idea 也许集中在 bridge，但 bridge idea 里是否有 downstream 影响力大的样本？paper 只测分布不测质量。

<!-- meta:
authors: [Ziyu Chen, Yilun Zhao, Arman Cohan]
url: https://arxiv.org/abs/2607.01233
arxiv_id: 2607.01233
pdf: papers/2607.01233-measuring-gap-human-llm-research-ideas.pdf
brief: _meta/briefs/papers/2607.01233.md
survey: user-provided
-->
