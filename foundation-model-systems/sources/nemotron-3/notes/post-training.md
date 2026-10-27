# Nemotron 3 Post-training

```yaml
---
source_id: nemotron-3
section_type: rl-training
stage: post-training
substage: multi-env-rl-mopd
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Super post-training 是 SFT -> multi-environment RLVR -> SWE-RL -> RLHF -> MTP healing；它把 agentic tasks 和 long-horizon SWE 作为主线，而不是附录。[Super:18-30]
- SFT 数据覆盖 agentic harnesses、long context、多工具、terminal/search/customer-service 等，强调多环境任务覆盖。[Super:18-26]
- RL Stage 1 是多环境 verifiable rewards，Stage 2 单独做 SWE-RL，因为 SWE rollout 慢、context 长、会成为混训 bottleneck。[Super:26-28]
- Super 使用 asynchronous GRPO，training 和 inference 解耦，rollouts 存到 buffer；这是和 Cascade 2 strict on-policy GRPO 不同的工程取舍。[Super:28-29]
- Ultra 把 post-training 进一步改为 MOPD 主线：specialized teachers、MOPD warmup、MOPD results、reasoning efficiency/control 和 RL infrastructure scaling。[Ultra:20-33]

## Why It Matters

Nemotron 3 说明 2026 open frontier post-training 已经从“单一 RLVR”进入系统化阶段：多环境 SFT、verifiable RL、SWE environment、RLHF、MOPD、MTP rollout acceleration、infrastructure scaling 都是一个系统。

## Method Blocks

### MOPD in Ultra

- 官方披露：Ultra post-training 包含 MOPD algorithm、specialized teachers、warmup、results and discussions。[Ultra:20-29]
- 合理解释：NVIDIA 正把 MiMo/Cascade 2 这种 MOPD 模式提升为 Nemotron 3 frontier release 的核心 consolidation 机制。
- 未披露 / 不能下结论：第一版未完整抽取 Ultra MOPD formula 和 teacher routing，后续需要深读。

### Async GRPO in Super

- 官方披露：Super 使用 asynchronous GRPO，训练和推理解耦，inference workers 持续生成 trajectories 并写入 rollout buffer。[Super:28-29]
- 合理解释：这是为数千 GPU RL 和多环境 rollout 吞吐服务的工程取舍。
- 未披露 / 不能下结论：staleness control、importance weighting、policy lag 上限需要进一步深读。

## Ultra Code / SWE Teachers 补核（2026-10-19）

- **事实**：SWE teacher 为 agentic SFT -> single-step PivotRL -> multi-turn end-to-end SWE GRPO；hidden tests 给 binary reward，unfinished trajectories mask loss，错误 reasoning/tool-call tokens 得 negative advantage。[Ultra:22]
- **事实**：SWE 环境物理删除 future commits，并在运行时阻止从网络恢复目标仓库 history / gold patch；这是防 reward leakage 的训练控制。[Ultra:22]
- **事实**：Competitive Coding teacher 从 General Reasoning teacher 继续 RL，使用带强 tests 的竞赛题；删除 teacher 在 8/8 rollouts 都答对的题，保留约 3.5K prompts。[Ultra:26]
- **事实**：不同 SFT pipelines 的 teachers 直接 MOPD 合并表现不佳；轻量 teacher-distribution SFT warmup 再 MOPD，在 agentic domains 的 ablation 有明确收益，不能推成所有 domains 必须 warmup。[Ultra:27]
- **原文入口**：https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf ，§3.3.2–3.3.3。

## Gaps / Open Questions

- Ultra MOPD 的公式/teacher selection 第一版没有完全展开。
- Super async GRPO 与 Cascade strict on-policy 的效果/稳定性 tradeoff 需要 comparison。
- GenRM / RLHF data 和 verifier details 需要回读。

## Evidence Anchors

- **2026-10-19 训练来源补核（事实）**：Super / Ultra SWE trajectories 从 SWE-Gym、R2E-Gym、SWE-rebench 等 task instances 生成；Ultra 还列 SWE-rebench-V2。Terminal SFT 使用 Terminal-Task-Gen：静态 math/code 等任务适配 + skill/seed synthetic tasks，不应把 trajectories 数量当独立环境数量。[Super:20,25; Ultra:17-18]
- **官方开放数据补核（事实）**：`nvidia/Nemotron-RL-Agentic-Terminal-Pivot-v1` 发布 31,111 个 next-action decision-point samples，来自 630 个 ATCB seed tasks / 2,716 successful trajectories；card 明确这些 seeds 用于 Nemotron Ultra 的 RL。发布数据是 history+reference-next-action，不能当作 31K 可自由 rollout 的完整 containers/verifiers。CC-BY-4.0。[terminal-pivot-card]
- 原文入口 [terminal-pivot-card]：https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Terminal-Pivot-v1

- Super 18-30: post-training pipeline。
- Ultra 20-33: MOPD and RL infrastructure。
