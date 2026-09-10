---
title: "SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving"
year: 2026
venue: arxiv
paper_type: trajectory-curation
lifecycle_role: frontier-candidate
boundary_risk: recipe

failure_modes: [failure-signal-waste, step-label-noise, reward-hacking-data]
data_knobs: [step-level-masking, difficulty-curriculum, reward-hacking-filter, verifier-design]

agent_domain: code
data_object: trajectory
data_source: teacher
selection_signal: verifier
adaptivity: curriculum
failure_use: mask
training_consumer: sft
---

## 一句话

SWE agent 的局部错误 mask recipe。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `failure-signal-waste` | 长 SWE 轨迹里坏步骤会污染后续，但整条丢弃浪费可学片段。 | step-level error masking，只 mask 错误 step / token。 | mask 的自动化质量依赖 verifier / trajectory parser。 |
| `reward-hacking-data` | Git hacking 会虚高 SWE-bench 表现并污染训练轨迹。 | hack-free evaluation 和 Git-hacking filtering。 | 其他 evaluator shortcut 仍需项目内 guardrail。 |

## 核心做法

SWE-Lego 把 SWE issue resolving 的 SFT 拆成数据、训练和 TTS 三块；本项目只关心前两块。数据上，它混合真实 GitHub PR 任务和 synthetic bug injection，形成 32k executable task instances 和 18k validated expert trajectories。[Brief] 训练上，它不是非黑即白丢弃失败轨迹，而是做 step-level error masking，再按交互难度做 curriculum。[arXiv Abstract] 结果上，SWE-Lego-Qwen3-8B / 32B 在 SWE-bench Verified 达到 42.2% / 52.6%，说明“干净可执行数据 + 局部监督”本身可以支撑很强的 agent SFT。[arXiv Abstract]

## Data Mechanism / Design Knobs

| Data knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `step-level-masking` | 错误 step 局部 mask。 | 整条成功保留 / 失败丢弃。 |
| `difficulty-curriculum` | 按交互轮数组织 SFT 难度。 | 随机混合所有轨迹。 |
| `reward-hacking-filter` | 识别 Git hacking 轨迹和评测污染。 | 只看最终 resolve label。 |

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| 普通 SWE SFT | teacher 轨迹噪声大，失败轨迹利用粗糙。 | executable validation + local masking + curriculum。 | 依赖代码环境和轨迹级诊断。 |

## 谱系位置

- 上游：SWE-bench、SWE-smith、SWE-rebench。
- 同期：SWE-Master、Open-SWE-Traces、DeNovoSWE。
- 下游：benchmark bad-case driven step mask / failure repair 数据包。

## 和 Agentic RL 的关系

- agentic_rl_overlap: false
- 核心贡献是 SFT data recipe；TTS/verifier 是增强推理，不是本卡主线。
- 不需要登记到 `agentic-rl`。

## 优缺点

- 优势：最贴你当前 M5 自检和 M4 failed-loop-switch 的数据处理方式，尤其是“坏轨迹里的好步骤”。
- 不足 / 风险：主要是 SWE 域；迁到 docs / data-analysis / browser 时，需要重做 verifier 和 step attribution。

<!-- meta:
authors: [Chaofan Tao, et al.]
url: https://arxiv.org/abs/2601.01426
arxiv_id: 2601.01426
pdf:
brief: _meta/briefs/papers/2601.01426_swe-lego.md
survey: user known-item
agentic_rl_overlap: false
agentic_rl_queue: none
-->
