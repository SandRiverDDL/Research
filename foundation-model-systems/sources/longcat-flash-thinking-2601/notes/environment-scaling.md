# LongCat-2601 Environment Scaling

```yaml
---
source_id: longcat-flash-thinking-2601
section_type: tool-agent-training
stage: midtraining-rl
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- LongCat 认为 agentic reasoning 的瓶颈是环境交互能力：长 horizon、异构环境、long-tailed dynamics 要求数据、环境、RL 和 infra 联合设计。[2]
- Midtraining 先暴露 moderate-scale structured agentic trajectories，避免 RL 阶段从 raw model 开始低效探索。[2-3]
- Agentic data synthesis 分 text-driven synthesis、environment-grounded synthesis 和 planning-oriented augmentation 三路。[3-4]
- 环境构建从 domain specification 自动生成 tool set、database schema、tool code、unit tests、dependency graph，再用可执行 tool chain 扩展环境。[5-6]

## Why It Matters

这是 agentic RL 最值得学的部分：不是“给模型 bash 工具然后 RL”，而是先定义可执行、可验证、可扩展的环境族，让模型在结构化多域环境中学习可迁移交互模式。

## Mechanism Sketch

1. 从文本中挖 multi-step workflow，抽取 tool schemas，合成 multi-turn trajectories。
2. 从已有 tool definitions 构建 lightweight Python environments，并显式建模工具依赖。
3. 用 reverse synthesis 从执行路径反推 user/system prompt，并通过代码执行验证 final state。
4. 对 existing trajectories 做 planning-oriented augmentation，把线性轨迹变成多候选决策过程。
5. 对 domain graph 做 BFS-style expansion，只添加依赖已满足的工具，保持数据库状态一致和 reward 可验证。

## Details / Evidence

- 2601 把 32K/128K 阶段分配 500B tokens，256K 阶段额外 40B tokens，并在 midtraining 加入 agentic data。[3]
- 自动 pipeline 从 schema-level designs 到可执行 tool implementations 的成功率超过 95%。[6]
- 每个 domain graph 包含 60+ tools，覆盖 20+ domains，并配套 database schema implementations。[6]

## Gaps / Open Questions

- Tool/domain specification、task generator prompts、quality filters 和 rubric validation 没有完全公开。
- 需要和 MiMo/Qwen-Coder/Step 的 agentic environment 比较：LongCat 写环境最细，但开放实现仍需核查。

## Lookup-only

- 具体环境数量、token 数、domain 数可以作为 lookup，不需要背。[3, 6]

## Evidence Anchors

- 2-4: midtraining and agentic data synthesis.
- 5-8: executable environment construction.

