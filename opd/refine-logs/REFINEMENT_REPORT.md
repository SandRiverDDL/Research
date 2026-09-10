# Refinement Report

**Problem**：长程 agent OPD 的 first critical disagreement curriculum。
**Initial Approach**：earlier-first prompt sampling + post-divergence token truncation + online resampling。
**Date**：2026-08-24
**Rounds**：3 / 5
**Final Score**：8.4 / 10
**Final Verdict**：REVISE

## Problem Anchor

最终版本保持用户原始问题：用关键分歧位置而非整题正确率控制 prompt sampling，并在分歧后监督失真前停止；但不把 raw disagreement 或 earlier-first 当作未经验证的真理。

## Output Files

- Review summary: `refine-logs/REVIEW_SUMMARY.md`
- Final proposal: `refine-logs/FINAL_PROPOSAL.md`
- Score history: `refine-logs/score-history.md`
- Raw reviews: `refine-logs/round-1-review.md`, `round-2-review.md`, `round-3-review.md`

## Score Evolution

| Round | Problem Fidelity | Method Specificity | Contribution Quality | Frontier Leverage | Feasibility | Validation Focus | Venue Readiness | Overall | Verdict |
|-------|------------------|--------------------|----------------------|-------------------|-------------|------------------|-----------------|---------|---------|
| 1 | 6.0 | 5.0 | 5.5 | 7.0 | 5.0 | 6.5 | 4.5 | 5.6 | RETHINK |
| 2 | 8.0 | 7.5 | 8.0 | 8.5 | 6.5 | 8.5 | 6.0 | 7.7 | REVISE |
| 3 | 8.5 | 8.5 | 8.5 | 9.0 | 7.5 | 8.0 | 6.5 | 8.4 | REVISE |

## Round-by-Round Review Record

| Round | Main Concern | Change | Result |
|---|---|---|---|
| 1 | 组合感强，核心 variable 不可辨识 | 定义 simulator-grounded paired branch test，收成单一 acquisition claim | 从 RETHINK 到明确路线 |
| 2 | method choices 与成本仍未冻结 | 固定 greedy teacher continuation、two-hit censoring、wall-clock cost | conceptually coherent |
| 3 | 两个局部 protocol ambiguity | 补全状态转移，拆 attribution/end-to-end baseline | pilot-ready |

## Final Proposal Snapshot

- 冻结 teacher/student 和 standard reverse-KL OPD。
- 在 raw action disagreement 处，对 student action 与 teacher action 做同一 greedy teacher continuation 的 paired terminal comparison。
- 只把 `A^T=1` 的首次 action fork 记为 teacher-improvable。
- 两次连续 probe 确认 first-fork 后移后，才增加 prompt priority。
- 主 comparison 计入完整 probe wall-clock；no-probe vanilla OPD 是必要 end-to-end baseline。
- earlier-first 只在受控 conditional analysis 成立后加入。

## Method Evolution Highlights

1. 从表面分歧改成 action-local terminal consequence。
2. 从静态 earlier-first 改成 confirmed fork-progress。
3. 从“三个组件贡献”压成一个 prompt acquisition contribution。

## Pushback / Drift Log

| Round | Reviewer Said | Author Response | Outcome |
|---|---|---|---|
| 1 | 可加 recoverability/value model | 拒绝；会撞 PCL/ReOrder 并制造新校准闭环 | 保持零新增 trainable component |
| 2 | 改写 Problem Anchor | 保留冻结 anchor，在 operational interpretation 中说明 earliness conditional | reviewer 接受无 substantive drift |
| 3 | 继续需要实证 | 接受；不以添加模块掩盖 negative pilot | final verdict 保持 REVISE |

## Remaining Weaknesses

1. `A^T,d,L` 是否在 ReOrder continuation reliability 之外提供增量预测，未知。
2. 标准 reverse-KL 是否能学会 teacher-improvable action fork，未知。
3. Branch probe 是否在 end-to-end wall-clock 上回本，未知。
4. Snapshot/replay 限制了首版环境范围。

## Raw Reviewer Responses

三轮原始 reviewer response 已逐字保存在：

- `refine-logs/round-1-review.md`
- `refine-logs/round-2-review.md`
- `refine-logs/round-3-review.md`

Calibration 为 none；review independence 为 same-family，结论只能视为 provisional。

## Why the Loop Stops at Round 3

Round 3 reviewer 明确判断“no blocking conceptual redesign remains”。剩余低分来自没有实验，而继续做两轮文本 review 无法产生真实证据。为避免通过堆模块追分，当前版本冻结为 REVISE，下一步只运行 causal pilot。

## Next Steps

1. 冻结 tool-DAG、teacher/student、`H`、action schema 与 wall-clock instrumentation。
2. 先跑 Claim 1：比较 pass rate、raw disagreement、ReOrder reliability 与 `A^T/d` 对 one-update gain 的增量预测。
3. 任一 gate 失败即停止；通过后再进入 ForkProgress sampler 训练。

