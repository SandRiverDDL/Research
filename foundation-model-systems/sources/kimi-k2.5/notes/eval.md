# Kimi K2.5 Eval

```yaml
---
source_id: kimi-k2.5
section_type: stage-note
stage: eval
depth: working
confidence: medium
need_expert_review: false
---
```

## Core Design / Innovation

- Kimi K2.5 eval 覆盖 text reasoning、coding、agentic search、image/video、computer use，和它“multimodal agentic intelligence”的 claim 对齐。[10-12]
- Eval 的重点不应是背分数，而是看它如何把 Agent Swarm 的收益拆成 accuracy、critical steps 和 execution time 三类证据。[13-15]
- 对视觉/视频，它强调 long-video、多帧和 OCR/document understanding；这些直接对应 MoonViT-3D 和 temporal compression 的设计。[12-13]

## Why It Matters

Kimi K2.5 是一个适合比较“agent 系统设计是否真的带来能力”的 source。Agent Swarm 的 eval 比普通 benchmark 更有价值，因为它同时报告 single-agent baseline、parallel system 和时间节省。

## Mechanism Sketch

1. 主 benchmark suite 覆盖 reasoning/general、coding、agentic、image、video、computer-use。
2. Agent Swarm 单独用 BrowseComp、WideSearch、In-house Swarm Bench 评估。
3. 除最终分数外，用 critical steps / execution time 衡量并行带来的 wall-clock-like 改善。

## Details / Evidence

- Agent Swarm 在 BrowseComp / WideSearch 上相对 single-agent 有明显提升，TR 把收益解释为 parallel decomposition 和 proactive context sharding。[13-15]
- Computer-use eval 使用 OSWorld-Verified 和 WebArena，说明 K2.5 不只是 VQA 模型，而是 GUI/action agent 模型。[12-13]

## Gaps / Open Questions

- In-house Swarm Bench 不可复现；它适合支持方向，不适合单独支撑 SOTA claim。
- 多模态和 computer-use eval 的工具权限、scaffold、采样、judge 设置需要回 source 或外部 benchmark 文档。

## Lookup-only

- 完整分数表回查 `[12-13]`。
- Agent Swarm result table 和 execution-time curve 回查 `[13-15]`。

## Evidence Anchors

- 10-13: benchmark taxonomy and main results.
- 13-15: Agent Swarm eval, context sharding, time savings.
