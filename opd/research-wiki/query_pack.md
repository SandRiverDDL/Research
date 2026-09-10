# Research Wiki Query Pack

_Auto-generated. Do not edit._

# Agentic OPD 索引

用途：先定位 agent 场景的 failure mode 和决策点，再进入单篇 card 或原文。本文件是人工维护的导航页，不复制每篇论文的实验细节，也不再拆新的 taxonomy 文件。

## 问题地图

| 决策点 | Agent 场景中的核心问题 | 观察指标 |
|---|---|---|
| Rollout depth | 生成到第几个 turn；完整后缀是否仍值得付出生成和 teacher 前向成本 | 成功完成深度、turn KL、survival、wall time |
| Prefix reliability | 错误 action/tool observation 后，teacher 在 student bad prefix 上是否仍能提供有效纠正 | turn/step divergence、重复、tool error、outcome |
| Loss allocation | 浅层 token 多、存活轨迹多，是否吞掉深层决策的更新预算 | 各 turn 的 loss share、gradient/update share |
| Action boundary | aggregate KL 是否掩盖少量但决定行为的 tool/action token | tool-call rate、结构 token KL、boundary error |
| Termination stability | OPD 是否强化循环、超长 generation 或无法关闭 tool call | repetition、length、EOS/tool-close、truncation rate |

## 论文地图

| 论文 | 主要处理什么 | 关键动作 | 当前证据状态 |
|---|---|---|---|
| [SOD](../notes/26_sod.md) | tool error 后的 step-level signal degradation | 按累计 step divergence 降低后续蒸馏权重 | 已有卡；需回原文核公式与阈值 |
| [TCOD](https://arxiv.org/abs/2604.24005) | 长程 agent 早期直接训练深 turn 不稳定 | front-to-back 逐步开放 trajectory depth | 待抽卡；当前仅作近邻定位 |
| [Are Full Rollouts Necessary?](../notes/26_full-rollouts-necessary.md) | full rollout 的后缀成本与监督退化 | progressive / fixed truncated rollout | 已有卡；主要实验并非多轮 agent |
| [TurnOPD](../notes/26_turnopd.md) | 固定 horizon 浪费尾部计算，trajectory mean 压低深 turn 权重 | adaptive depth controller + progressive turn-normalized loss | 已精读原文并抽卡 |
| [Multi-Turn OPD with Prefix Replay](https://arxiv.org/abs/2607.04763) | 多轮轨迹的 prefix/state coverage | replay 关键 prefix 再训练 | 待核，不把标题主张当结论 |
| [Tool-Call Boundary Drift](https://arxiv.org/abs/2607.07050) | 小量结构 token 信号造成全局 tool behavior 漂移 | 聚焦 tool-call boundary 的局部诊断 | 待核 |
| [Pass the Baton](https://arxiv.org/abs/2607.26057) | student 进入坏分叉后 teacher 只能续写坏 prefix | 检测分叉并让 teacher 短暂接管 | 待核 |

## 当前跨论文判断

- **事实**：现有工作已分别修改 rollout horizon、step/turn loss 和 prefix 来源；“agentic OPD”不是一个单一方法类别。
- **解释**：最底层矛盾不是“后段 KL 大还是小”，而是 observed KL 同时被真实能力差、坏 prefix、模板化 continuation 和存活样本选择影响。
- **开放问题**：TurnOPD 解决算力分配，不直接解决复读 token 是否进入 loss；SOD 解决加权，不一定能识别低-KL 的重复 attractor。两者都不能替代显式 termination/repetition guard。
- **实践入口**：先读 SOD → full-rollout → TurnOPD；需要研究新 idea 时，再核 Prefix Replay、Tool-Call Boundary Drift 和 Pass the Baton。

## 维护规则

- 新论文只加一行：它改变哪个 agentic OPD 决策点、证据是否已核。
- 只有跨论文判断改变时才改“当前跨论文判断”。
- 当单表超过约 30 篇或某个 failure mode 已有稳定证据链时，再拆专题 synthesis；目前一个索引文件足够。
