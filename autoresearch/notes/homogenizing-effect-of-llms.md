---
title: The Homogenizing Effect of Large Language Models on Human Expression and Thought
year: 2026
venue: Trends in Cognitive Sciences
paper_type: position
lifecycle_role: critique-anchor
boundary_risk: adjacent

failure_modes: [hallucinated-novelty, evidence-tier-mixing]
design_knobs: [evaluation-scope, evaluation-protocol]
---

## 一句话定位

跨语言学/心理/认知科学的 position paper：LLM 系统性把语言、观点、推理都推向 WEIRD 中位数。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `hallucinated-novelty` | LLM 输出看似流畅多样，实际统计上向 WEIRD 中位数收敛；协作写作让**用户自己**的观点也向 LLM 靠拢 [PDF §3-5] | 汇总跨学科证据（sociolinguistics、心理学实验、认知科学）指出这不是 surface 问题 | position 论文，无新实验 |
| `evidence-tier-mixing` | 讨论 taste homogenization 时常把 stylistic 收敛、观点收敛、reasoning 收敛混谈 | 明确拆三档：linguistic / perspectival / reasoning，每档独立列证据 | 三档之间的因果关系未量化 |

## 方法机制

- 综合三个维度证据 [PDF §3, §4, §5]：
  1. **Language diversity**：LLM polish 后写作在文风上收敛，author trait（政治倾向、性格、性别、年龄）的可预测性下降；temperature scaling / persona prompt 不管用。
  2. **Perspectival diversity**：LLM 输出比人类样本方差小得多，向 WEIRD (Western/Educated/Industrialized/Rich/Democratic) 中位数偏移；co-writing 让用户观点也漂移。
  3. **Reasoning diversity**：CoT 促收敛式推理，wisdom-of-crowds 类任务上 LLM 会向"idealized"答案坍缩，失去 variance；LLM-assisted ideation 产出 idea 更多但**语义相似度更高**。
- 核心机制解释：next-token prediction + RLHF 双重作用下，模型学"统计上典型"的表达，把长尾表达平滑掉；训练数据本身 WEIRD 偏，形成 recursive feedback loop（用户用 LLM 写→写进网络→再训 LLM）。
- 对 measuring-gap（本项目 anchor 论文）的意义：Chen 2026 的 bridge/synthesis 收敛是这个 homogenization 现象在 research ideation 场景下的**具体实例**，不是孤立现象。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Measuring-Gap (Chen 2026) | 只测 ideation 分布 | 上升到跨领域跨行为的一般机制 | 无量化，只作理论上位 |
| Tong 2026 (AI Can Learn Taste) | 主张 taste 可训 | 反驳：即使训了，仍受 pretraining 分布约束（论文明确说这一点） | 未提供反驳的实证 |
| Meincke 2024 (prompting for diversity) | 认为 prompt trick 能扩多样性 | 汇总证据说 prompt 变体只增 surface 多样性，深层同质化不动 | 未列具体阈值 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `evaluation-scope` | Cross-domain（语言 + 观点 + 推理） | 单任务 benchmark |
| `evaluation-protocol` | Meta-review of existing empirical work | New experiment |

## 方法优缺点 / 适用边界

- 优势：
  - 给本项目 taste-gap 问题提供**上位理论框架**。measuring-gap 是这个理论在 research ideation 域的一个数据点。
  - 明确指出 CoT / RLHF **加剧**同质化——正好和 measuring-gap 的 thinking-mode ablation（thinking 让分布更窄）机制一致，形成交叉证据。
  - Recursive feedback loop 论述：用户用 LLM 写作 → 输出被训进下一代 → 长期同质化加速。这是对 autoresearch 的长期风险最重要的一个 framing。
- 不足 / 风险：
  - Position paper 无原创实验，全部靠综合他人证据；conclusion 强度取决于所引研究的质量。
  - "WEIRD 中位数"这个说法在 research ideation 场景不完全适用（科研 taste 未必按国家/文化分层）。
  - 未提供可复用的量化协议——本项目要用它当 anchor，需要自己找可测量的 proxy。
  - 论文本身有强 normative 色彩（引用 Orwell、McDonaldization），使用时要区分事实 claim 和价值主张。

<!-- meta:
authors: [Zhivar Sourati, Alireza S. Ziabari, Morteza Dehghani]
url: https://arxiv.org/abs/2508.01491
arxiv_id: 2508.01491
pdf: papers/2508.01491-homogenizing-effect-of-llms.pdf
brief: _meta/briefs/papers/2508.01491.md
survey: measuring-gap-human-llm-research-ideas
-->
