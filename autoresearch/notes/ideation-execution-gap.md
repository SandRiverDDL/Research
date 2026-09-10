---
title: The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas
year: 2025
venue: arxiv
paper_type: critique-audit
lifecycle_role: critique-anchor
boundary_risk: none

failure_modes: [hallucinated-novelty, reviewer-model-hacking, cherry-picked-showcase, weak-experimental-design, evidence-tier-mixing]
design_knobs: [evaluation-protocol, evaluation-scope, evaluation-judge, verifier-type]
---

## 一句话定位

真让人跑 AI 生成的 idea 100+ 小时，novelty/effectiveness 全面塌方，甚至翻盘输给人类。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `hallucinated-novelty` | Si 2025a 的 novelty 优势可能是 ideation 阶段的幻觉，落地时被 execution constraint 打回原形 [PDF §1] | 43 名专家 × 100+ 小时执行 × 4 页短论文，前后对比同一 idea 的分数 | 只测 NLP，且 43 人执行力异质性大 |
| `reviewer-model-hacking` | 前作只在 ideation 阶段评分，等价于 idea 迎合 reviewer 偏好；execution 强制引入 feasibility 反馈 | Study 1（ideation review）+ Study 2（execution review）同 idea 前后对比 | execution 分数仍由人类 reviewer 打，未做 metric-grounded 验证 |
| `weak-experimental-design` | 前作要么只执行 1-2 个 idea（Gottweis 2025, Ghareeb 2025）无法做显著性，要么完全不执行 | N=43 的 randomized assignment，两组 idea 相同任务分布 | 100 小时 budget 上限，未测复杂 project |
| `cherry-picked-showcase` | AI Scientist / Coscientist 类只展示成功案例 | 全部 random assign 结果都算，不挑 | idea 池仍是 rerank 后 top |
| `evidence-tier-mixing` | 混用 "LLM 自评"、"小规模 human"、"单个 execution 展示" | 全人工 blind review + 前后配对对比 | 未做独立第三方 audit |

## 方法机制

- 数据 = Si 2025a 里的 idea 集合；随机分给 43 名 NLP 专家，每人 100+ 小时执行成一份 4 页短论文 [PDF §1, Fig 1]。
- 双阶段评审：Study 1 = 只看 idea 打分（复用 Si 2025a）；Study 2 = 看执行后的短论文 blind review。
- 主结果 [PDF §1, Fig 2]：LLM idea 在 novelty / excitement / effectiveness / overall 四个 metric 上**下跌幅度都显著大于人类**（p<0.05）；execution 后 LLM 甚至在多个 metric 上被人类翻盘（差异未达显著但方向反转）。
- 核心命题：**ideation-execution gap 是当前 LLM idea 的系统性性质，不是运气不好**。评价 research idea 若不测 execution，等于测了假的东西。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Si 2025a（同作者前作） | 只测 ideation 阶段 novelty | 补上 execution → 揭示 ideation 结论的 fragility | 43 人 × 100 小时，代价极高 |
| Ghareeb 2025 / Gottweis 2025（domain autoresearch） | 只执行 1-2 idea 展示 | statistically-powered execution study | 只覆盖 NLP |
| Measuring-Gap (Chen 2026) | 分布评法，但仍在 ideation 层面 | 补执行侧证据 | 两条路径互补，未合并 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `evaluation-scope` | Ideation + Execution 双阶段，同 idea 前后配对 | 只 ideation / 只 execution |
| `evaluation-protocol` | 100+ 小时 real execution + 4 页短 paper + blind review | LLM-judge / auto-benchmark |
| `evaluation-judge` | Expert human blind reviewer | LLM reviewer / crowd |
| `verifier-type` | Human review of executed paper | Rule-based / execution-check / LLM reviewer |

## 方法优缺点 / 适用边界

- 优势：
  - **本项目最重要的 critique anchor 之一**：直接把"AI 出的 idea 更 novel"这个流行 claim 打上"ideation-only artifact"的标签。
  - 前后配对设计消除 idea 本身的难度混淆——同一批 idea 同时打两次分。
  - 揭示"评价 research idea 若不做 execution，就是自欺"的原则，直接影响本项目对 autoresearch 评测的判断。
- 不足 / 风险：
  - 只在 NLP，且执行者水平不一致（100 小时 short paper，非全职 PhD 项目）——execution quality 可能被人类因素主导而非 idea 本身。
  - 43 人分两组后每组 N ≈ 20 左右，功效边缘，翻盘部分未显著。
  - 未做 execution 阶段的独立第三方 audit（reviewer 仍是同批 NLP 专家），仍在同一评审圈内。
  - 100 小时天花板决定这只覆盖"能在一周内验证"的 idea，长周期/理论 idea 不适用。

<!-- meta:
authors: [Chenglei Si, Tatsunori Hashimoto, Diyi Yang]
url: https://arxiv.org/abs/2506.20803
arxiv_id: 2506.20803
pdf: papers/2506.20803-ideation-execution-gap.pdf
brief: _meta/briefs/papers/2506.20803.md
survey: measuring-gap-human-llm-research-ideas
-->
