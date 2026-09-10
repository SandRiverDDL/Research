---
title: "Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL"
year: 2025
venue: arxiv
paper_type: core-rl-method
lifecycle_role: frontier-candidate
boundary_risk: infra

failure_modes: [rollout-cost, sparse-delayed-reward, exploration-collapse]
design_knobs: [rollout-source, environment-interface, trajectory-filtering]

rl_env: web
rl_interaction: online
rl_reward: sparse
rl_credit: trajectory
---

## 一句话定位

用 fully asynchronous GRPO 支撑超长 search-agent rollout。

## 难题 / Failure Modes

| Failure mode | 本文诊断 | 本文处理方式 | 仍未解决 |
|---|---|---|---|
| `rollout-cost` | 长 search trajectories 会造成 straggler，GPU 等最慢工具调用。 | fully asynchronous trajectory rollout，rollout 和 training 解耦。 | 这更偏系统/infra，非新的 advantage 估计。 |
| `sparse-delayed-reward` | search agent 只在最终答案处拿 sparse reward。 | 仍用 GRPO group relative reward，并做 dynamic filtering。 | 没有细粒度 step credit。 |
| `exploration-collapse` | 小 turn limit 学不到复杂 search strategy。 | 把 turn limit 扩到 32/128，并用长轨迹 online RL 激活 search 行为。 | 探索主要靠 rollout scale 和数据难度。 |

## 方法机制

ASearcher 把 search/browser agent 训练成长 horizon online RL 闭环：每个问题采样一组 trajectories，用 GRPO 根据同组 relative rewards 更新；reward 是 trajectory completion sparse reward，本地 RAG setting 用 format reward 和 F1，相对真实 web setting 用 LLM-as-judge。[brief p.11] 核心系统设计是 fully asynchronous RL：trajectory rollouts 并行执行，工具等待不阻塞整个 batch，rollout 和 model update 解耦，以支持 100+ tool calls 的长 search trajectories。[brief p.1-p.3, p.9-p.10] 训练中还过滤全同 reward 的 queries，避免 zero-advantage group 浪费更新。[brief p.11]

## 相对方法

| 对比对象 | 对方问题 | 本文改动 | 代价 / 风险 |
|---|---|---|---|
| Search-R1 / R1-Searcher | turn limit 和 search/browse 能力不足。 | search + browsing tools，长 horizon online RL。 | 主要是 search application/system。 |
| 同步 GRPO agent training | 等最慢 trajectory，长工具调用导致吞吐低。 | fully asynchronous rollout + decoupled training。 | off-policy/lag 问题需要系统实现处理。 |
| DeepResearcher / WebDancer | 强应用基线，但训练机制不一定可迁移。 | 开源 large-scale async RL pipeline。 | 方法比较混合了数据、工具、评测和系统。 |

## 设计决策 / Design Knobs

| Design knob | 本文选择 | 常见替代选择 |
|---|---|---|
| `rollout-source` | asynchronous online search/browser trajectories. | synchronous rollout / offline traces / replay. |
| `environment-interface` | search engine + browser tool with long turn budget. | search-only / local RAG / fixed workflow. |
| `trajectory-filtering` | remove groups with identical rewards and zero advantage. | train all groups / difficulty filtering / rejection sampling. |

## 方法优缺点 / 适用边界

- 优势：把“长 horizon agent rollout 的系统瓶颈”显式纳入 GRPO training loop，是 search-agent 里少见的 core infra method。
- 优势：对后续 web/deep-research agent 很重要，因为 rollout cost 和 straggler 是真实训练瓶颈。
- 不足 / 风险：`boundary_risk: infra` 高，若做 algorithm comparison，应和 objective/credit 方法分开。
- 不足 / 风险：credit 仍是 trajectory-level sparse reward，核心算法性不如 Tree-GRPO/SPEAR。

<!-- meta:
authors: [Jiaxuan Gao, Wei Fu, Minyang Xie, et al.]
url: https://arxiv.org/abs/2508.07976
arxiv_id: 2508.07976
pdf: papers/2508.07976-asearcher-beyond-ten-turns.pdf
brief: _meta/briefs/papers/2508.07976_asearcher-beyond-ten-turns.md
survey: SPEAR backward reference [49]
rl_optimizer: grpo-like
rl_data_reuse: none
rl_warm_start: standard
-->
