---
title: "ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL"
authors: [Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, Aviral Kumar]
year: 2024
venue: ICML 2024
url: https://arxiv.org/abs/2402.19446
arxiv_id: 2402.19446

lane: environment-rl
paper_type: core-rl-method
lifecycle_role: canonical-anchor
data_overlap: false

rl_axes:
  environment: mixed
  interaction_mode: online
  reward_signal: sparse
  optimizer: actor-critic
  credit_assignment: step
  data_reuse: off-policy
  sft_warm_start: unclear
---

## 一句话

早期 multi-turn LLM agent RL anchor：高层 off-policy critic + 低层 token policy。

## 机制表

| 维度 | 本文设定 | 为什么重要 | 证据 |
|---|---|---|---|
| Environment / task | web/tool/human-interaction style multi-turn agent tasks。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |
| Interaction loop | multiple turns of interaction with external environment。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |
| Reward / feedback | delayed scalar rewards。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |
| Optimizer / update | hierarchical actor-critic；high-level off-policy value learning + low-level token policy。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |
| Credit assignment | utterance/turn-level value function 给低层 token policy 提供 credit。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |
| Exploration / replay | 非主轴。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |
| Warm start / data | unclear。 | 定义 Agentic RL learning loop 的可复用机制。 | `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md` |

## 核心增量

**事实 [PDF abstract, p.1]**: ArCHer 认为现有 LLM RL 多关注 single-turn reward maximization，无法训练模型在多轮交互中 seek/incorporate information、perform credit assignment、reason about past actions。

**事实 [PDF abstract, p.1]**: 论文提出 hierarchical RL framework：高层 off-policy RL 训练 value function 聚合 utterance-level reward；低层 RL 用高层 value function 来训练每个 turn 内 token-by-token policy。

**事实 [PDF abstract, p.1]**: 作者报告在 multi-turn tasks 上提升 efficiency/performance，sample efficiency 约为 existing on-policy methods 的 100x，并开源项目页和代码。

**解释 [本项目判断]**: 这是 credit assignment / off-policy multi-turn RL 的 canonical anchor，虽然年份早于当前 seed cutoff，但被新 survey 用作方法基础，应该补卡。

**收录依据 [queue/audit]**: survey 正文提到 + ICML/PMLR + 官方代码，直接抽卡。代码：`https://github.com/YifeiZhou02/ArCHer`。

## 谱系位置

- 上游：single-turn RLHF / PPO。
- 同期：early multi-turn LM agent RL。
- 下游：Agent Lightning、credit assignment survey、GiGPO。

## 优缺点

- ✅ [PDF abstract, p.1]: 清楚定义 single-turn RL 无法解决 multi-turn credit assignment。
- ✅ [PDF abstract, p.1]: high-level critic + low-level policy 是明确机制。
- ⚠️ [本项目判断]: 任务和模型规模较早；作为机制 anchor，不作为 frontier performance anchor。

## Evidence

- paper brief: `_meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md`
- PDF / HTML: `papers/2402.19446-archer-hierarchical-multiturn-rl.pdf`
- survey windows: Credit Assignment / GFCR
- PDF: `papers/2402.19446-archer-hierarchical-multiturn-rl.pdf`
- source anchors: abstract p.1; introduction p.1-2。

<!-- pdf: papers/2402.19446-archer-hierarchical-multiturn-rl.pdf -->

<!-- brief: _meta/briefs/papers/2402.19446_24_archer-hierarchical-multiturn-rl.md -->

<!-- survey: Credit Assignment / GFCR -->
