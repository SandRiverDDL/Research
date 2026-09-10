# Agent Post-Training Data Seed Sources

> 第一轮 seed 只服务 agent post-training data generation / filtering / verification / repair / masking / distillation。默认优先 2026；最早放宽到 2025Q4。RL-heavy seed 放到 `/Users/chy/Research/agentic-rl/`。

当前脚本主队列是 `comparison/queue.md`。本文件保留 seed / anchor 背景，不再手动维护完整候选状态。

## Current Priority Seeds

| Priority | Paper | Date | Why seed | Status |
|---|---:|---|---|---|
| S | [Agentic Tool Use in Large Language Models](https://arxiv.org/abs/2604.00835) | 2026-04 | 只读取 supervised tool learning、tool-call data、action grammar、tool trajectory、evaluation landscape 部分；reward-driven tool policy learning 迁到 Agentic RL。 | card written |
| S | [Alignment Tuning for Large Language Models: A Data-Centric Lens on Alignment Data Pipelines](https://arxiv.org/abs/2605.26442) | 2026-04 | 提供 data-centric pipeline lens：response synthesis、evaluation/preference signal、data filtering、data instantiation。 | card written |

## 2026 Known-Item Queue Seeds

| Priority | Paper / topic | Why |
|---|---|---|
| S | SWE-Lego | failure-aware SWE agent SFT data curation：step-level error masking、trajectory curriculum、Git hacking filtering。 |
| S | ASTRA | synthetic multi-tool trajectory + rule-verifiable executable environment；连接 SFT 和 verifiable RL。 |
| S | daVinci-Agency | real GitHub PR sequence as long-horizon supervision；验证 real-world logs 是否优于合成长程轨迹。 |
| S | ProAct | environment-derived trajectory + Monte-Carlo Critic lookahead distilled into SFT；边界靠近 RL。 |
| S | ProCUA-SFT | large-scale GUI agent step-level synthetic trajectories + negative transfer analysis。 |
| A | MARS | metacognitive reflection / failure-switching scaffold；改进有限，先 review。 |
| B | MIRROR | metacognitive calibration benchmark；不是训练方法，只作为 data synthesis / scaffold 启发。 |

## Method / Anchor Seeds

第一轮 card 队列只保留直接影响 Agent Data 机制的方法。

| Priority | Paper / topic | Why |
|---|---|---|
| S | FireAct | language agent fine-tuning 早期 anchor；重点看 trajectory / tool-use demonstrations 如何构造。 |
| S | STeP | self-reflected trajectories + partial masking；重点看轨迹监督和 masking 决策。 |
| S | InSTA | internet-scale agent training；synthetic tasks、trajectory completion、trajectory judgment。 |
| A | MAG-V | multi-agent synthetic data generation and verification for tool-call trajectories。 |
| A | Exploring Expert Failures | failed expert trajectories 如何转化为有用 training data。 |
| A | DataEnvGym | 仅当其贡献是 student-feedback-driven data generation / teacher environment data 时收录；如果核心是 environment RL，迁到 `agentic-rl/`。 |

## Moved To Agentic RL

以下不在当前项目抽完整卡，已放到 `/Users/chy/Research/agentic-rl/comparison/seed-queue.md`：

- `A Brief Overview: Agentic Reinforcement Learning In Large Language Models`
- `Environment Scaling for Interactive Agentic Experience Collection`
- `Agentic Reasoning for Large Language Models`
- ToolRL
- Tool-R0
- ToolGym
- ASTRA

## Historical Background

以下旧综述已经降级到 `notes/archive/historical-background/`。只有在需要查定义、术语、早期经典引用时才读，不作为当前 seed：

- `23_llm-autonomous-agents-survey.md`
- `23_llm-based-agents-rise-survey.md`
- `23_tool-learning-foundation-models-survey.md`
- `25_instruction-tuning-survey.md`

## First Recall Rule

第一轮不做全网系统检索。只做：

1. 从 current priority seeds 抽取 references / related work 中的 agent post-training data mechanism 方法。
2. known-item recovery：确认 2026 known-items 和 method / anchor seeds 是否入队。
3. 只抽核心贡献在 data generation / filtering / verification / repair / masking / curriculum / distillation 的 papers。
4. 遇到 RL algorithm paper，写入 `/Users/chy/Research/agentic-rl/comparison/seed-queue.md`，不要在本项目抽完整卡。

## Seed Reading Questions

读每篇 seed 时，不照搬综述目录，回答：

- 它的数据对象是什么：task、prompt、trajectory、tool-call、observation、replay buffer？
- 数据从哪里来：human、teacher、self-generated、environment-generated、synthetic、web？
- 它有没有明确 selection / filtering / verification signal？
- 它如何处理 failure trajectory？
- 它的数据机制服务 SFT、pre-RL、RL，还是 eval-only？
- 它是否越界到 Agentic RL；如果是，越界部分只记到 `agentic-rl` queue。
