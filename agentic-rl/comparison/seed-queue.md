# Agentic RL Seed Queue

> Agentic RL future queue。当前可以独立开会话抽卡；抽卡时只处理核心贡献在 RL learning loop 的 papers。

## Survey / Overview Seeds

| Priority | Paper / topic | Why keep | Status |
|---|---|---|---|
| S | The Landscape of Agentic Reinforcement Learning for LLMs: A Survey | Agentic RL 概念入口；定义 single-step LLM RL vs temporally extended POMDP / Agentic RL。 | card written |
| S | From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models | 机制型 seed；credit assignment 是 long-horizon agentic RL 的核心瓶颈。 | card written |
| A | Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning | rollout / filter / control / replay 机制 seed；有 data overlap。 | card written |
| S | Environment Scaling for Interactive Agentic Experience Collection | 把 environment 当作 agentic experience producer，关系到 interactive data / feedback / rollout。 | note moved |
| A | Agentic Reasoning for Large Language Models | 区分 in-context reasoning 与 post-training/agentic reasoning，可能作为 bridge survey。 | queue |
| B | A Brief Overview: Agentic Reinforcement Learning In Large Language Models | Agentic RL 概念入口；暂被 Landscape survey 替代为主 seed。 | background |

## Method / Environment Seeds

| Priority | Paper / topic | Why keep | Status |
|---|---|---|---|
| S | ToolRL | tool-use RL reward design / policy learning anchor。 | card written |
| S | Tool-R0 | zero-data / self-play tool learning，可能是 Agentic RL frontier candidate。 | queue / arXiv exception pending |
| A | ToolGym | open-world tool-use environment and data curation；若核心是 environment / RL loop，放这里。 | queue |
| A | ASTRA | synthetic agentic trajectories + reinforcement arenas，SFT/RL bridge；本项目后续看 reinforcement arena / RL side。 | queue |
| A | Environment scaling / benchmark family | environment/task generation、interactive feedback、agentic experience collection。 | queue |

## Current First-Batch Follow-up

见 `comparison/selected-literature-from-survey-seeds.md`。当前优先从机制轴抽卡，不按 deep research / web / GUI 场景直接铺开。

## Expanded Candidate Queue

更宽的候选池见 `comparison/expanded-candidate-queue.md`。当前已确认旧队列过窄；需要从 credit assignment taxonomy、search/deep-research、web/GUI、code/software、tool-use 多个 lane 做 recall。

## Boundary Rule

如果一篇论文的核心贡献是 environment rollout、reward、RL policy update、online exploration 或 long-horizon credit assignment，就放这里，不放 `/Users/chy/Research/agent-data/`。

如果一篇论文的核心贡献是 training data generation、filtering、verification、repair 或 curriculum，即使服务 RL，也放 `/Users/chy/Research/agent-data/`，这里只记录 cross-link。
