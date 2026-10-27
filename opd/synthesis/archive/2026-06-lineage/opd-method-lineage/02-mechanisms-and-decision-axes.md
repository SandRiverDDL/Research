# 02. 机制与决策轴

> 2026-10-06 整理：历史快照；保留原文的时间与覆盖口径，不代表当前全库。最新具体机制见 [failure-mode 诊断](../../../failure-modes/concrete-failure-modes.md)。

> 本卷回答：OPD 方法为什么这样设计。重点不是逐篇复述，而是把方法选择拆成可干预的轴。

## OPD 的最小抽象

一个 OPD 方法至少由六个问题决定：

1. **State source**：训练 prefix 来自 teacher、offline data、student，还是 mixed rollout？
2. **Signal source**：teacher 给 logits、hidden state、outcome reward、verifier、rubric，还是 preference？
3. **Objective / estimator**：用 forward-KL、reverse-KL、skew-KL、JSD、advantage、MSE，还是 adaptive routing？
4. **Trust/filter**：哪些 state/token/step 不该蒸？
5. **Granularity**：监督单位是 token、step、segment、trajectory，还是 cross-rollout group？
6. **Update interpretation**：训练收益来自更密监督，还是来自进入特定 state / parameter subspace？

当前 71 张 L1 cards 的 decision index 显示：`rollout=student` 已经占多数，`signal=logit` 仍占主流，`filter=none` 仍很多。这说明主流 OPD 已经接受 on-policy state，但对 teacher reliability 和 granularity 的控制还不成熟。证据：[`_meta/generated/research-map.md`](../../../../_meta/generated/research-map.md)。

## 1. Rollout：修复 exposure bias 但引入 reliability mismatch

teacher / offline rollout 的优点是状态更干净，teacher supervision 更在分布内；缺点是 student 推理时不会只访问这些状态。student rollout 的优点是覆盖实际推理 prefix；缺点是 bad prefix 上的 teacher signal 可能不可执行。

| 选择 | 代表 | 解决什么 | 主要风险 |
|---|---|---|---|
| teacher/offline | SeqKD, TAID, Lightning-OPD | 干净 supervision、低生成成本 | exposure bias |
| mixed | GKD, MiniLLM, DistiLLM, TrOPD | 在稳定性与 on-policy coverage 间折中 | mixture / scheduler 超参 |
| student | 大多数 2026 OPD | 训练 state 接近推理 state | flawed-prefix trap、teacher reliability mismatch |
| teacher-selected | BRTS | teacher trajectory 也做筛选 | 额外 teacher sampling budget |

解释：OPD 的核心不再是“student rollout 越多越好”。更合理的说法是：需要让 student 访问关键 states，同时只在 teacher signal 可信的 states 上学习。

## 2. Loss：KL 选择逐渐变成 routing 问题

Forward-KL 更 mode-covering，适合保留 teacher distribution 的多样性，但可能把 student 拉向 void region。Reverse-KL 更 mode-seeking，适合聚焦高概率路径，但可能丢掉合理 continuation。Skew-KL 用 mixture denominator 稳定梯度，adaptive-KL 则尝试按 source、target difficulty 或 token entropy 分流。

| Loss family | 方法 | 机制含义 | 适合场景 |
|---|---|---|---|
| forward-KL | GKD, TIP | 覆盖 teacher support | teacher signal 可靠、希望保留多样性 |
| reverse-KL | MiniLLM, many OPD | mode-seeking | reasoning 主路径清晰、避免 void region |
| skew-KL | DistiLLM, DistiLLM-2 | 有界梯度、source-aware | q 接近 0 或 SGO 成本高 |
| adaptive-KL | TAID, EOPD, SCOPE, TrOPD | 条件 routing | capacity gap、token entropy、trust region |
| advantage / reward | G-OPD, BOPD, PBSD | RL-style reward shaping | 需要超越 teacher 或 black-box signal |
| MSE representation | OPRD | 避开 output-space estimator 方差 | teacher/student representation compatible |

开放问题：loss routing 现在多是手工规则。真正有价值的是学习或估计 routing policy：什么时候用 coverage，什么时候用 seeking，什么时候直接拒绝 teacher signal。

## 3. Sequence-level、token-level、sampled-token：估计器差异

MiniLLM 的 sequence-level reverse-KL 更接近完整 trajectory objective。当前 token 的梯度会耦合未来所有 log-ratio：

```text
current token action -> future trajectory -> future teacher/student log-ratio -> current gradient
```

这就是 future reward / future log-ratio coupling。优点是理论目标更完整；缺点是长序列里未来项噪声会回传到早期 token，方差很大。

Token-level surrogate 则把每个 prefix 的 next-token distribution 当作局部监督目标。它切断了长程 coupling，因此方差低，但不再是完整 sequence-level objective 的无偏估计。

Sampled-token surrogate 是更窄的一类：只用 student 实际采到的 token 的 log-ratio 或 reward 近似整个分布。它更省算，但容易出现 three mismatch：

- **sampled-token imbalance**：多数 sampled tokens reward 为负，少数局部正 token 主导更新，信号高度不平衡。
- **support mismatch**：student prefix 或 sampled token 落到 teacher 低支持区域，teacher 仍给局部概率但方向不可用。
- **special-token mismatch**：EOS、BOS、tokenizer 边界或 special token 的概率比较被实现细节扭曲。

Revisiting OPD 的 top-K local support matching 是对此的直接修复：只在 teacher local support 内比较截断 distribution，并 mask special tokens。证据：[`notes/26_revisiting-opd.md`](../../../../notes/26_revisiting-opd.md)。

## 4. Signal：dense 不等于可信

White-box logits 提供最密 supervision，但也最依赖 teacher distribution 的局部正确性。Black-box textual/rubric reward 更通用，但 credit 粗。Representation signal 绕开 output-space 方差，却引入 layer/projector/architecture compatibility 问题。

| Signal | 代表 | 优点 | 代价 |
|---|---|---|---|
| logit | GKD, DistiLLM, TIP, OPSD | dense、token-level、可直接 KL | white-box；bad prefix 上可能假精确 |
| representation | OPRD | 避开 LM head 和 score-function 方差 | 需要 hidden access；跨架构复杂 |
| verifier/outcome | Segment-Level, SSOPD | 和最终成功更贴近 | sparse 或 coarse |
| verbal/rubric | ROPD, Lion | API-only 友好、可解释 | process credit 弱 |
| discriminator reward | BOPD | black-box teacher 可用、动态 reward | judge/discriminator 复现链条弱 |

解释：signal interface 是方法 novelty 的重要空间，但必须和 credit granularity 绑定。只把 logits 换成 rubric，如果仍然 sequence-level 打分，通常不能解决 process credit。

## 5. Filter 与 trust：OPD 的核心控制量

Filter 不是工程 trick，而是 OPD 的主轴。不同 filter 对应不同 trust 假设：

| Filter | 代表 | 判断依据 | 风险 |
|---|---|---|---|
| support truncation | Revisiting, Prune-OPD, TrOPD, SimCT | teacher/student support overlap | 只看 support 不看 rank/probability gap |
| score threshold | TIP, EOPD, Rock Tokens | entropy、divergence、loss、token utility | 局部指标可能错过 future consequence |
| trajectory-level | SCOPE, TRD, Near-Future | correctness、future trajectory、refinement | 粒度粗、算力更高 |
| step/segment-level | SOD, Segment-Level | tool/observation boundary、local return alignment | 需要明确任务结构 |
| verifier-pass | HDPO, MOPD, SSOPD | pass/fail group structure | verifier 噪声和多 rollout 成本 |
| hardness/curriculum | TAID, PACED, Rethinking | student competence frontier | 训练前估计不准会错筛 |

开放问题：当前 filter 多是单指标。一个强方法应当联合 state reliability、teacher entropy、student entropy、support overlap、future consequence、verifier outcome、prefix depth，而不是只看 KL 或位置。

## 6. Granularity：监督单位应随任务结构变化

Token-level 适合局部 teacher signal 可靠且 token action 与最终 outcome 关系较直接的场景。Step-level 适合 tool / agent，因为 tool call 会改变 observation state。Segment-level 适合 long-horizon agent route。Trajectory-level 适合错误来自 path 而非单 token 的 reasoning。

一个实用决策树：

```text
是否有明确 tool/observation boundary?
  yes -> step/segment-level route first
  no  -> 局部 token 是否能预测 future consequence?
          yes -> token-level selection
          no  -> near-future / trajectory refinement
```

注意：granularity 不是越细越好。token 粒度 credit 密，但更容易被 flawed prefix 和 local mismatch 污染；trajectory 粒度稳，但会丢掉局部可修复信号。

## 7. Privilege 与 multi-rollout：credit 的两种来源

Privilege 路线把额外信息放进 teacher context，例如 ground truth、answer、hint、system rule。它能把 sparse reward 转成 dense process signal，但必须区分 PI 类型：

- shared latent rule：更可能内化，例如稳定偏好、系统规则、通用证明策略。
- instance-specific clue：推理期不可得，容易学成多个 PI-conditioned teachers 的聚合，泛化差。

Multi-rollout 路线从同 prompt 的多个 student samples 中取结构：成功 peer、失败 peer、shortest correct、longest wrong、frontier prompt。它不需要外部 PI，但需要 verifier 和多样本预算。

解释：这两条线都在回答同一个问题：final outcome 如何变成 process-level credit。区别是 privilege 用外部条件，multi-rollout 用内部对比。

## 8. Geometry：为什么 dense supervision 可能只产生 sparse updates

Dense Supervision, Sparse Updates 和 Geometry OPD 的共同信号是：OPD 虽然在每个 token 上给 dense teacher signal，但参数更新可能小、稀疏、低维、谱集中。EffOPD 的 parameter extrapolation 进一步假设：OPD 早期已经锁定主要 update direction，后续训练只是在补 magnitude。

这对方法设计的含义是：不要只问“怎样得到更多 token supervision”，还要问：

- 哪些 states 激活了真正有用的 subspace？
- 哪些 token/window 只是高损耗但低贡献？
- early update direction 是否能预测最终收益？
- filter 是否应该同时看 token utility 和 parameter utility？

开放问题：现有 geometry 多是 post-hoc analysis。把它变成训练前/训练中 controller，仍是空白。
