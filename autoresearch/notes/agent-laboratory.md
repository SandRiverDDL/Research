---
title: Agent Laboratory - Using LLM Agents as Research Assistants
year: 2025
venue: arxiv
paper_type: core-method
lifecycle_role: canonical-anchor
boundary_risk: none

failure_modes: [reviewer-model-hacking, verifier-blind-spot, weak-experimental-design, hallucinated-novelty, human-in-the-loop-hidden]
design_knobs: [pipeline-scope, stage-decomposition, agent-role-organization, verifier-type, human-intervention-point, tool-grounding, literature-access, iteration-control]
---

## 一句话定位

Human idea + agent 执行的 end-to-end 对立命题：明说 LLM 应 complement 而非 replace 人，实证 auto reviewer 比 human 高估 2.3 分。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `reviewer-model-hacking` | 用 NeurIPS-style criterion 对同 15 paper 分别让 auto-reviewer 与 human 打分：**auto 6.1/10 vs human 3.8/10，overall 相差 2.3 分**，split-violin plot 证明 auto 系统性高估 [§4.1.1 Fig 6] | 明确 report 双列，说 auto 分数不 predictive of human | 未探讨为何 auto reviewer 会高估 2.3 分；未测异模型 auto reviewer |
| `verifier-blind-spot` | mle-solver 的 program scoring 也是 LLM self-eval（打 0-1 与目标对齐度）——同源盲区仍在 [§3.2] | Top program sampling + batch-parallel 保 diversity | Score 与真实科研 metric 的相关性未测 |
| `weak-experimental-design` | 人评 NeurIPS 指标：quality 1.7-2.3/4, soundness 1.7-2.2/4, contribution ~2.1/4 全跨 backend 都低 [§4.1.1] | 报出所有 backend 分数 | 未定位 root cause——backend 强就够了还是需要方法学改动 |
| `hallucinated-novelty` | 未直接 audit；作者引用 Si 2024 说 LLM 弱在 feasibility/implementation → 用 human idea 作为 grounding 避开这个问题 [§1] | 让 human 提供 idea，system 只负责执行 | 未测 "全自主 idea generation vs human idea" 直接对比 |
| `human-in-the-loop-hidden` | **反向态度**：明说 "co-pilot mode 显著提升质量"，把 human involvement 视为 feature 而非 hidden cost，与 AI Scientist "autonomous" 叙事对立 [§4.2] | Autonomous vs copilot 两 mode 都 report；copilot 全指标提升（quality +0.75, soundness +0.48, overall +0.58） | 未 report copilot mode 下 human effort 时间 |

## 方法机制

- **三 phase pipeline** [§3]：
  1. **Literature Review**：PhD agent + arXiv API + 3 action (summary / full text / add paper) 迭代至 N_max。
  2. **Experimentation**：PhD + Postdoc 对话确定 plan → ML Eng + SW Eng 数据准备（Python + compiler + HF search）→ **mle-solver** 跑实验。
  3. **Report Writing**：paper-solver 生成 report。
- **mle-solver 五步循环** [§3.2, Fig 3]：
  - A. Command Execution：EDIT（替换指定行范围）/ REPLACE（整文件重生）两种 op；类比 AIDE tree search 但打分**代码 + outcome** 而非纯 accuracy。
  - B. Code Execution：compiler 编译 + 自动 repair。
  - C. Program Scoring：LLM 打 0-1 分（与实验目标对齐度）。
  - D. Self-Reflection：succeed 反思如何提分，fail 反思如何修 bug。
  - E. Performance Stabilization：维护 top program 池 + batch-parallelization（N 个 modification 并行，最好那个替换池底）。
- **Multi-agent role split** [Fig 2]：PhD / Postdoc / ML Engineer / SW Engineer——比 AI Scientist v1/v2 单 agent 多角色更明确的角色分工。
- **人评 setup** [§4.1]：5 topic × 3 backend = 15 paper，10 PhD × 3 paper each 打 Experimental / Report / Usefulness (1-5)。
- **NeurIPS-style eval** [§4.1.1]：quality / significance / clarity / soundness / presentation / contribution，同 15 paper 让 auto-reviewer 与 human 分别打。

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| AI Scientist v1 (Lu 2024) | Autonomous ideation + LLM auto-reviewer 单源 | 强制 human 提供 idea + copilot mode 每 stage 可插 feedback | 需要 human effort（未量化）；不 test LLM ideation 能力 |
| AI Scientist v2 (Yamada 2025) | Tree search + VLM 但仍 fully autonomous 定位 | 明确定位 assistant 而非 replacement | 未与 v2 定量对比 |
| AIDE (Schmidt 2024) | 只针对 Kaggle，score 只取 accuracy | mle-solver 打分**代码 + outcome** 兼评；MLE-Bench 上 claim SOTA | Score 定义主观化，未 ablation |
| ResearchAgent (Baek 2024) | 只做 ideation | 端到端 code+report | 舍弃 ideation 能力测试 |
| Si 2025b (execution gap) | 揭示 idea→execution 有 gap | 从根源上让 human 提供 idea 绕开这个 gap | 不 measure 系统能否**判断** idea 好坏 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `pipeline-scope` | End-to-end 但 idea 由 human 提供 | 全自主 / 单子任务 |
| `stage-decomposition` | 3 phase (lit review / experiment / report) 明确 stopping criteria | Linear / tree-search |
| `agent-role-organization` | 多 agent role-specialized (PhD/Postdoc/ML Eng/SW Eng) | 单 agent 多 role prompt 切换 |
| `verifier-type` | mle-solver 内部 LLM 打分 + compiler + human feedback (copilot mode) | Pure LLM reviewer / execution-check only |
| `human-intervention-point` | Idea 层强制 + 每 stage 可插 feedback | 无人 / 只 end review |
| `tool-grounding` | arXiv API + HF datasets + Python compiler | 单一 LLM 内知识 |
| `literature-access` | 3 action iterative retrieval (summary/full text/add) | Post-hoc single query |
| `iteration-control` | Top program pool + batch-parallel + self-reflection | Fixed rounds |

## 方法优缺点 / 适用边界

- 优势：
  - **对立命题的 canonical anchor**：与 AI Scientist "fully autonomous" 叙事直接对立，为本项目 idea vs execution 分离的论点提供正面案例。
  - **auto vs human reviewer 2.3 分落差**是本项目最硬的 `reviewer-model-hacking` 定量证据——比 SoundnessBench 74% FPR 更直接对应"生成 pipeline 的 auto reviewer"场景。
  - AMD 官方 + JHU + ETH，作者 tier 高，公开代码 + 详细 cost breakdown。
  - 多 agent role split + mle-solver 的 EDIT/REPLACE + top pool + batch-parallel 是可复用的设计 pattern。
  - Copilot vs autonomous 对比明确 report human involvement 的边际价值（quality +0.75）。
- 不足 / 风险：
  - **未 test LLM 独立 ideation 能力**——研究设定直接绕开了 v1/v2 最脆弱的环节，比较不完全对等。
  - Copilot mode 下 **human effort 时间未量化**（Beel 2025 报的 25h/paper 对标缺失），"$2.33/paper" claim 只算 API cost 不算人时。
  - `human-in-the-loop-hidden` 在这里不是缺陷但也不是免费：将其视为 feature 掩盖了"到底需要多少人"的问题。
  - mle-solver program score 仍是 LLM self-eval，同源 verifier 问题结构上未解，只是 human idea 输入让下游 verify 压力变小。
  - 只到 4.0/10 overall（人评），距离 workshop accept（约 6+）还差；未 report NeurIPS/ICLR main track 提交结果。
  - 无独立第三方 audit。

<!-- meta:
authors: [Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum]
url: https://arxiv.org/abs/2501.04227
arxiv_id: 2501.04227
pdf: null
brief: _meta/briefs/papers/2501.04227.md
survey: AI-Scientist-v2-RW & measuring-gap-adjacent
-->
