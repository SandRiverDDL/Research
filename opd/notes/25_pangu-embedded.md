---
title: "Pangu Embedded: An Efficient Dual-system LLM Reasoner with Metacognition"
authors: [Pangu Team]
org: huawei-noah
year: 2025
venue: arxiv
arxiv_id: 2505.22375
url: https://arxiv.org/abs/2505.22375
zotero_key:

confidence: 3
verified: a

addresses:
  - capacity-gap
  - teacher-staleness

decisions:
  rollout: teacher
  loss: forward-kl
  signal: outcome
  iteration: iterative
  filter: hardness
  extra: none
---

> **一句话**：工业级 reasoning 蒸馏与 RL recipe 参考。

## 核心做法

把"teacher 数据全量 SFT"换成 **student-capability-aware 的迭代 distillation**：每轮都按 student 当前的复杂度评分（Eq. 1）筛 teacher 生成的 long-CoT，倾向中等偏易，避免太难数据被 student 内化为噪声；轮间用 model merging 缓解 catastrophic forgetting；之后再 GRPO + MARS（rule reward + LLM judge）+ curriculum mixing 做 RL；最后叠加 fast/slow dual-system 控制（manual + adaptive）。

## 谱系位置

vs. DeepSeek-R1 蒸馏（直接 800k teacher 输出 SFT 小模型，无难度筛选、无迭代 merging）：Pangu Embedded 把 student 当前能力反馈进 data selection 闭环，并在 SFT 阶段做多轮 + parameter merging；vs. 一般 GRPO RLHF：MARS 把 deterministic verifier 与 LLM judge 异质 reward 在数学/代码/通用任务间动态调配，并配 latency-tolerant scheduler 适配 Ascend NPU stale-sync RL。

## Method

1. Stage 1 — SFT：从 teacher 蒸出 long-CoT pool，用 model-aware complexity score 筛"balanced→稍难"子集（Table 1：balanced 50.42 > mostly-hard 48.75 > mostly-easy 45.42 > all 43.33），跑 3 轮 iterative SFT，轮间 model merging（Table 5/6 显示每轮 AIME 单调上升，merging 在 AIME/LCB/GPQA 一致正向）。
2. Stage 1 — RL：GRPO + MARS（correctness verifier + preference RM + 其他 task reward）+ curriculum data mixing + cold start，code RL 仅 300 steps 在 LiveCodeBench 上 +6% 绝对值（§4.7）；clip-higher ε_high=0.28。
3. Stage 2 — Dual-system：manual `<thinking>`/`<no-thinking>` 切换 + adaptive 复杂度感知 router；7B 总参，benchmark 见 §4.2 Table 2。

## 优缺点

- ✅ [作者 ack §2.3.1]: 按 student 当前能力筛选中等难度 teacher CoT，直接针对 capacity gap。
- ⚠️ [作者 ack §2-4]: 主线仍偏 offline teacher SFT + RL recipe，不是严格 student-rollout OPD。

## headline number

- Pangu 7B thinking system reaches AIME24 81.9 / GPQA 68.0 / LiveCodeBench 67.1（§4.2 Table 2）

## Evidence

- TL;DR 7B 数字 81.9 / 68.0 / 67.1 来自 §4.2 Main Comparison Settings（"Thinking system2"段落）
- "balanced 50.42 vs mostly-hard 48.75 vs mostly-easy 45.42" 来自 §2.3.1 Table 1
- Iterative SFT 单调改进 + merging 一致正向 来自 §4.5 Table 5/6
- LiveCodeBench RL +6% / 300 steps 来自 §4.7 Initial RL Validation on Code

<!-- pdf: §2 Method / §4 Experiments -->
