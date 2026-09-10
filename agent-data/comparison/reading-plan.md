# Reading Plan

> 本项目是 goal-driven literature map，不是领域综述。阅读目标是服务 30B A3B MoE agent SFT 的 benchmark-driven data improvement。

## Core Question

```text
benchmark bad case -> data action -> ablation / mixture -> stronger model
```

每篇论文只有在能改变以下至少一项时才值得精读：

- 该合成 / 挖掘什么 agent SFT 数据。
- 该如何筛选、mask、修复、重加权轨迹。
- 该如何把 tool observations / artifacts / execution feedback 转成监督。
- 该如何做数据包 ablation、mixture search 或 regression guardrail。

## Tracks

### Core Agent SFT Data

回答“造什么 agent 数据”。优先级最高。

| status | paper | why |
|---|---|---|
| done | ACC | trajectory -> long-context QA；贴近 30B A3B MoE 和 observation grounding。 |
| done | Agent Data Protocol | 统一异构 agent 数据格式，适合作内部 schema seed。 |
| done | SWE-Master | SWE post-training recipe：teacher trajectories、curation、long-horizon SFT。 |
| done | Open-SWE-Traces | real PR trajectory mining + Qwen3-30B-A3B。 |
| done | DeNovoSWE | whole-repo synthetic/verifiable long-horizon data。 |
| done | DataMind | 数据分析 agent 数据合成，贴用户最弱 benchmark slice。 |
| done | PC Agent-E | 少量人工 GUI trajectories + teacher action augmentation。 |
| done | ProCUA-SFT | large-scale GUI step-level SFT + negative transfer。 |
| done | SWE-Lego | step-level error masking、Git hacking filtering、自检。 |
| done | ASTRA | tool trajectories + rule-verifiable executable environments。 |
| done | daVinci-Agency | real-world long-horizon PR supervision。 |
| done | ProAct | search / critic / lookahead -> SFT。 |

### Supporting Data Flywheel

回答“这些数据怎么选、怎么配、怎么消融”。不是 agent-specific，但服务 agent SFT。

| status | paper | why |
|---|---|---|
| done | FastMix | 快速 data mixture optimization。 |
| done | Dr. Post-Training | target data 与 general data 的 regularization tradeoff。 |
| done | Data Mixing Optimization for SFT | 用 validation loss 优化 SFT 数据配比。 |
| done | Bilevel Data Curation | offline selection 与 online generation 的统一优化视角。 |

### Supporting Agent Patterns

回答“哪些 inference-time agent behavior 值得蒸进 SFT”。先不写 formal paper card，后续可放 `comparison/supporting-agent-patterns.md`。

- Anthropic Building Effective Agents: orchestrator-workers / evaluator-optimizer。
- Anthropic Think Tool: tool-result 后显式检查规则、证据和下一步。
- Anthropic Multi-Agent Research System: task decomposition、parallel context budget。
- Anthropic Advanced Tool Use: tool selection / tool search / context-efficient tool use。

## Do Not Prioritize

- broad agent survey，除非能给 core paper seed。
- pure RL optimizer / GRPO variants，除非直接改变 SFT data selection。
- generic LLM post-training survey，除非抽 data mixture / selection method。
- benchmark-only paper，除非改变 verifier / data collection protocol。

## Next Concrete Steps

1. 基于 18 张 L1 写第一版 synthesis：`benchmark failure -> data package -> ablation -> guardrail`。
2. 把 `comparison/benchmark-to-data-actions.md` 升级成可执行训练数据 backlog：每个数据包含 source、selection signal、expected win、regression risk。
3. 只在 synthesis 暴露证据缺口后，再补 MARS / MIRROR 或 canonical anchors。
