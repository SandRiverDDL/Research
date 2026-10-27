# Teacher–student mismatch / capacity gap

> 2026-10-06 状态：保留的 mismatch 专题，覆盖范围仍是下述旧卡快照；末尾选题推荐属于历史解释，未经新的 novelty／实验核查，不作为当前已确认方向。具体数值信号与估计器问题先读[最新 failure-mode 综合](concrete-failure-modes.md)。

> 覆盖说明：对当前 76 张 cards 做全文召回，再精读 22 张候选卡；主表保留 20 篇直接改变 mismatch 决策的工作。旧 YAML taxonomy 只用于召回，不作为归类依据。

## 现象

“强 teacher 带弱 student”不是一个单一 gap，而是四层问题：

1. **Pair mismatch**：teacher 有能力，但 reasoning pattern 或可表达分布不适合该 student。
2. **Data mismatch**：pair 可以蒸，但 prompt 太易、太难，或不需要 teacher 的新增能力。
3. **Local-support mismatch**：当前 state 上，sampled token、teacher support 与 student support 没有形成可靠更新。
4. **Trajectory mismatch**：prefix 尚可教，student drift 后的 suffix 已经不可教。

**事实**：[Rethinking OPD](../../notes/26_rethinking-opd-llm.md) 将成功条件拆为 pattern compatibility 与 new capability；[Revisiting OPD](../../notes/26_revisiting-opd.md) 进一步说明 sampled-token estimator、local support 与 flawed prefix 会把这种不兼容变成错误梯度；[Prefix Teach, Suffix Fade](../../notes/26_prefix-teach-suffix-fade.md) 和 [Supervision Fidelity Decay](../../notes/26_supervision-fidelity-decay.md) 表明 compatibility 还会沿 trajectory 动态衰减。

## Diagnosis

一次 OPD 至少要同时满足：

- **Usefulness**：teacher 提供 student 尚未掌握的能力。
- **Global compatibility**：teacher 的 reasoning pattern 对该 student 可模仿。
- **Local teachability**：当前 prompt、state 和 token support 仍在可学习区域。
- **Temporal validity**：teacher signal 没有随 prefix drift 退化。

**综合判断（解释，不是单篇论文结论）**：token-level disagreement 要成为有效监督，还需同时满足三个条件：

$$
\text{effective teacher signal}
=
\text{teacher reliability}
\times
\text{outcome relevance}
\times
\text{student teachability}.
$$

- **Teacher reliability**：teacher 在当前 student prefix 上仍能给出可信方向，而非被 bad prefix、privileged information 或自身错误误导。
- **Outcome relevance**：分歧改变任务结果或关键决策，而非风格、格式、tokenizer 或等价表达。
- **Student teachability**：teacher correction 仍落在 student 当前可吸收的局部 support；高 KL 本身不等于可学。

现有方法通常只覆盖其中一部分：TrOPD 主要抑制 sampled-token gradient outlier，TA-OPD 主要估计 local teachability，Near-Future Guidance 用短未来轨迹近似 outcome/trajectory relevance；三者都没有独立证明 teacher 语义正确。

**当前判断：**

- capacity gap 不是参数量差，而是 `teacher × student × data × state × time` 的联合属性。
- overlap 不是单调指标：太高可能没有新增能力，太低可能不可学；低 KL 甚至可能是退化状态下的假 agreement。
- 现有工作已覆盖 teacher/data/target/state/token/horizon 几乎所有干预位置；再加一个权重或截断规则，novelty risk 很高。
- 真正空缺仍是统一测量：先区分“没新知识”“不兼容”“数据难度不对”“途中开始失真”，再决定是否蒸、蒸什么和何时停止。
- [Capacity Gap Rethinking](../../notes/26_capacity-gap-rethinking.md) 直接形式化 realizability，但仍是 OpenReview 候选，只能作为 novelty risk。

## 方法 × 决策点

| 干预位置 | 方法 | 判定信号 | 选择什么 | mismatch 时怎么做 | 仍未回答 |
|---|---|---|---|---|---|
| **Pair / 初始化** | [Rethinking OPD](../../notes/26_rethinking-opd-llm.md) | pattern compatibility + new capability | teacher、prompt、是否直接 OPD | teacher rollout cold start；换 aligned prompt | 如何低成本、跨 pair 预测 |
|  | [Capacity Gap Rethinking](../../notes/26_capacity-gap-rethinking.md) | student-visited state 上的 realizability | teacher signal 是否可学 | 将 capacity gap 变成可蒸馏性判断 | proxy 与实验可信度仍不足 |
|  | [VOLD](../../notes/25_vold.md) | cross-modal support distance | 是否先对齐 VLM 与 text teacher | SFT cold start 后再 OPD | teacher 不看图像时的可靠边界 |
|  | [X-OPD](../../notes/26_x-opd.md) | speech/text capability gap | text scaffold 是否可迁移 | 先缩小 cross-modal distribution gap | cross-modal 理论与强对照不足 |
| **Data / curriculum** | [PACED](../../notes/26_paced.md) | student pass rate | competence-frontier prompts | 降低过易/过难样本权重 | 不判断 teacher pattern |
|  | [Uni-OPD](../../notes/26_uni-opd.md) | difficulty + correctness + outcome order | informative states 与可靠 token signal | data balancing + margin calibration | recipe 组件多，归因困难 |
| **Target / objective** | [TAID](../../notes/25_taid.md) | loss 相对变化 | 每阶段揭示多少 teacher target | student→teacher 自适应插值 | offline KD，不处理 prefix drift |
|  | [TGPO](../../notes/26_tgpo.md) | policy divergence / training stage | teacher guidance 强度 | 早期给方向，后期退回 RL | schedule 仍需调；可能限制探索 |
|  | [REOPOLD](../../notes/26_reopold.md) | log-ratio、entropy、reward threshold | 哪些 token reward 可信 | clipping + exploration/refinement schedule | 仍依赖 token-level teacher reward |
| **Local support / state** | [Revisiting OPD](../../notes/26_revisiting-opd.md) | teacher Top-K support、sample imbalance、special token | 比较哪些 token support | truncated local RKL + top-p rollout + masking | support matching 仍不等于 task success |
|  | [BRTS](../../notes/26_brts.md) | teacher rollout correctness + student alignment | 哪条 teacher trajectory | Best-of-N curation + teacher-context supervision | 额外 teacher sampling 昂贵 |
|  | [TrOPD](../../notes/26_trust-region-opd.md) | sampled-token likelihood ratio / gradient outlier | 哪些 token 可稳定做 RKL | trust token 用 RKL；outlier 用 Top-K FKL；teacher-prefix guidance | 概率比只表示优化稳定，不保证语义可靠 |
|  | [Many Faces](../../notes/26_many-faces-opd.md) | teacher choice、Top-K stability、PI 类型 | teacher/loss/privilege 是否适用 | Top-K fix、RLVR teacher、SFT stabilization | empirical boundary 能否跨任务复现 |
| **Trajectory / horizon** | [Full Rollouts Necessary](../../notes/26_full-rollouts-necessary.md) | horizon 与后缀 reliability | rollout 多长 | progressive 或 truncated rollout | 固定/渐进 horizon 仍较粗 |
|  | [ESR](../../notes/26_early-stopping-rollout.md) | off-policy teacher decay | 前多少 token 值得生成 | 只蒸前 N 个 token | 固定位置不能适配所有 trajectory |
|  | [Position-Weighted OPSD](../../notes/26_position-weighted-opsd.md) | position + branch viability | 各位置监督权重 | position-weighted surrogate | 固定 schedule 不是 state-adaptive |
|  | [Prefix Teach, Suffix Fade](../../notes/26_prefix-teach-suffix-fade.md) | trajectory-specific teachability | 何时释放 teacher 约束 | release unreliable suffix | 跨 pair、跨任务泛化未知 |
|  | [Supervision Fidelity Decay](../../notes/26_supervision-fidelity-decay.md) | one-step lookahead teacher confidence | 哪些 continuation 仍可修复 | Lookahead Group Reward | tree/segmented scoring 增加复杂度 |
|  | [Prune-OPD](../../notes/26_prune-opd.md) | student/teacher top-k overlap | suffix loss 与 response budget | 动态降权并截断 | overlap 忽略 rank/probability gap |
|  | [KL Agreement Trap](../../notes/26_kl-agreement-trap.md) | 退化 state 中的异常低 KL | 何时停止 rollout | adaptive KL threshold termination | 低 KL 的多种成因仍难区分 |

## 邻接边界

- [DistiLLM-2](../../notes/25_distillm-2.md) 处理 teacher-/student-generated source 与 divergence 的 mismatch；属于 objective/source interface，不直接判断 teacher pattern。
- [SimCT](../../notes/26_simct.md) 处理 tokenizer interface mismatch；若 tokenizer 不同，它是前置必要条件，但不是 capacity gap 本身。
- Geometry / Dense-Sparse Updates 是 post-hoc update diagnostics；可以提供 predictor feature，但尚未形成 mismatch 决策方法。
- EOPD、TIP、SCOPE、SOD 更偏 uncertainty 或 credit granularity；只有证明其信号能区分“不可蒸”与“暂时困难”，才应并入本 failure mode。

## 残余瓶颈

缺少一个统一的 **distillability measurement + routing protocol**：

1. 训练前判断 teacher–student–dataset 是否值得蒸；
2. 训练中判断当前 state 该继续、降权、切换 teacher path、转 off-policy 还是停止；
3. 用共同 ground truth 比较 overlap、KL、entropy、pass rate、lookahead confidence 等 proxy，而不是每篇论文自定义“可靠性”。

最难之处是监督标签本身：最终 OPD gain 要靠完整训练得到，而 token-level teacher agreement 又不等于 outcome improvement。没有 counterfactual 或 held-out transfer，predictor 很容易只学到 dataset-specific 难度。

## 最短顶会入口

仍推荐：**preflight distillability predictor**，但不能只是再提一个 overlap metric。

最低门槛：

- 输出实际决策：选哪个 teacher、哪些 data、是否先 cold start，而非只报告 correlation；
- baseline 至少含 Rethinking、PACED、TAID、Revisiting，以及“直接跑短 OPD”；
- 在 held-out teacher family 或 held-out dataset 上预测最终 gain/ranking；
- 报告预测成本与错误选择造成的 regret。

如果做不到跨 setting 排序，这个方向会被 reviewer 视为又一个局部 reliability proxy。
