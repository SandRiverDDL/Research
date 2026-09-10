# Agentic RL Acceptance Rules

> 本文档只规定本项目“什么论文可以进入 queue / 抽正式 L1 card”。“怎么找论文”写在 `doc/retrieval-strategy.md`。这些是项目本地规则，不写入全局 skill。

## 基本原则

- Queue 可以宽，formal L1 card 要严。
- `search / GUI / code / tool / skill` 只是应用场景，不自动决定是否是 core。
- 真正判断看论文是否改了可迁移的 RL training loop 设计位点。
- 不确定时先 `queue / review`，不要直接抽卡。

## Hard Gates

正式 L1 card 必须满足：

- 有 original paper PDF / HTML / source brief。
- 有明确 RL mechanism，不只是 prompt、数据、模型发布或 benchmark。
- 默认必须开源：official code、training/eval implementation、project page 或可复现环境之一。

不开源只允许进入 `queue / review`，除非满足以下例外之一：

- 经典 anchor。
- 大厂 / frontier lab 论文，存在保密或产品化理由。
- 被多个近期 core papers 反复作为 baseline / direct related work。
- 有明确社区影响力背书。

## Time / Venue Gate

### 2025 年之后

优先接受：

- 开源 + 顶会 / strong venue。
- 开源 + 新 arXiv + 明确 core mechanism。
- 开源 + 大厂背书。
- 开源 + 社区背书 / 被近期 core papers 反复引用。

新 arXiv 可以没有稳定 venue，但需要 Codex 判断可靠性：

- 方法 delta 清楚。
- baselines 合理。
- ablation 能拆出机制贡献。
- 没有明显数据泄漏 / prompt trick / weak baseline。
- 有代码或项目页。

### 2025 年之前

默认不新增正式 card，除非是：

- 经典 paper / canonical anchor。
- 被近期 agentic RL core papers 反复引用。
- 对当前 comparison 不可替代的 substrate / baseline。

### 非顶会旧论文

非顶会且不新的论文，除非满足以下至少一项，否则不抽卡：

- 大厂 / frontier lab 背书。
- 社区影响力或代码使用量明确。
- 被近期 core methods 作为 direct baseline。
- 提出本项目必须理解的独特 RL mechanism。

## Core Method Gate

算 `core-rl-method` 的条件：论文主贡献改了可迁移的 RL training loop 设计位点，例如：

- objective / optimizer。
- advantage estimation / credit assignment。
- rollout sampling / branching / tree search。
- replay / off-policy correction / self-imitation。
- reward shaping / verifier-to-policy update。
- trajectory filtering / curriculum。
- async rollout / environment feedback interface。
- prompt-action interface，如果它直接影响 policy update。

不自动算 core：

- 只是把 GRPO / DAPO / PPO 跑到 search、GUI、code、CLI、web、tool。
- 主要贡献是 benchmark、环境、数据、prompt、workflow、model release。
- 主要是 application recipe，机制不可迁移。

## Substrate Rule

GRPO / DAPO / Dr.GRPO / PPO / RLOO 这类是 substrate，不自动算 agentic RL core。

它们可以作为：

- background。
- baseline。
- `substrate-method` / substrate anchor。

只有当论文把 substrate 改造成 agent loop 里的新机制时，才进入 agentic core，例如：

- SPEAR：给 GRPO/GiGPO 加 self-imitation replay 和 curriculum intrinsic reward。
- SimpleTIR：给 multi-turn tool GRPO 加 feedback masking 和 void-turn filtering。
- Tree-GRPO：把 rollout 和 advantage 改成 agent-step tree structure。

## Boundary Handling

边界项必须写清：

- 为什么可能是 core。
- 为什么可能只是 recipe / application / data / infra。
- 需要核查什么证据。

常见边界：

- `boundary_risk: recipe`：方法像训练 recipe，但包含可迁移 RL delta。
- `boundary_risk: data`：skill / memory / data pipeline 强，但直接影响 RL update。
- `boundary_risk: reasoning`：主要是 reasoning / tool-reasoning，外部环境较弱。
- `boundary_risk: infra`：核心是 rollout/training system，但改变了 RL learning loop 可行性。

## Queue vs Card

进入 queue 的最低条件：

- 有可靠来源可验证。
- 有一句明确 `recall_reason`。
- 有初步 `paper_type` 和 `boundary_risk`。

写正式 L1 card 的最低条件：

- 通过 hard gates。
- 通过 time / venue gate 或有明确 exception。
- 通过 core method gate，或者明确标成 application / infra / survey 等非 core 类型。
- 有 bounded original paper brief。

## One-Line Checklist

抽卡前按顺序问：

1. 有原文和 source verification 吗？
2. 开源吗？不开源是否有经典 / 大厂 / 社区 / baseline 例外？
3. 是 2025 年之后吗？如果不是，是否经典或不可替代？
4. 是顶会 / strong venue / high-quality arXiv 吗？
5. 是否真的改了 RL training loop，而不是换场景跑 GRPO？
6. 边界风险是什么？
7. 不确定是否应该先 `queue / review`？
