# Kimi K2.5 Agent Swarm

```yaml
---
source_id: kimi-k2.5
section_type: stage-note
stage: agent-systems
depth: working
confidence: high
need_expert_review: true
---
```

## Core Design / Innovation

- Agent Swarm 是 Kimi K2.5 最独特的 agent 系统设计：不是简单多 agent prompt，而是用 PARL 训练 orchestrator 动态创建、调度、协调 frozen subagents。[4-6]
- 训练时只让 orchestrator 更新，subagents 来自 intermediate policy checkpoints 并冻结，避免所有 agent 一起 RL 带来的 credit assignment 和 instability。[4-5]
- Reward 明确鼓励并行但防止滥用：`r_parallel` 防止退化成串行，`r_finish` 防止无意义地开太多子任务，最终 reward 还包含任务表现。[5-6]
- Agent Swarm 被定义为 proactive context management：通过任务分解和局部上下文隔离扩展有效上下文，而不是等主 agent 超长后再 truncate/summarize。[14-15]

## Why It Matters

这和 GLM/LongCat 的 context management 思路不同：GLM 更偏 keep-recent / discard-all 这种轨迹内压缩，Kimi 把 context 压力转化成 parallel decomposition 问题。如果未来做 research/search/coding agent，这个方向比“更长 context window”更像系统能力。

## Mechanism Sketch

1. Orchestrator 接收复杂任务，决定是否拆分、何时创建 subagent、给 subagent 什么局部目标。
2. Subagents 冻结执行局部任务，保持独立 bounded context。
3. Orchestrator 收集局部结果，不把所有低层轨迹塞回全局上下文。
4. PARL 用环境反馈学习 parallel policy，先用小 subagents，再迁移到更大 subagents。

## Details / Evidence

- PARL reward 包含 parallel reward、finish reward 和 task performance reward；parallel/finish 系数会 anneal to zero，避免最终优化目标被 shaping reward 主导。[5-6]
- Critical Steps 指标把主 agent steps 和同一阶段并行 subagent 的最大 steps 合并，用来衡量 wall-clock-like latency，而不是总 tool call 数。[6]
- Agent Swarm 在 BrowseComp、WideSearch 和 In-house Swarm Bench 上展示相对 single-agent 提升，并在 WideSearch 中报告达到目标性能所需 execution time 可降低 3x-4.5x。[13-15]

## Gaps / Open Questions

- Orchestrator action space、subagent checkpoint selection、训练任务分布和真实成本没有完整公开。
- In-house Swarm Bench 很重要但不可复现，适合当方向证据，不适合当强可比 benchmark。
- 多 agent 系统可能提高推理成本；TR 强调 wall-clock 节省，但 GPU/API 总成本需要另算。

## Lookup-only

- Agent Swarm result table 和 latency curve 回查 `[13-15]`。
- Prompt construction categories 回查 `[6]`。

## Evidence Anchors

- 4-6: PARL design and reward.
- 13-15: Agent Swarm eval and proactive context management.
