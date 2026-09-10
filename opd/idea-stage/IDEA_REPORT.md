# Agentic OPD Failure Mode × Setting 报告

**方向**：寻找一个不落入 turn/prefix/reweighting 主战场、可用 8×A100 快速否证的 agentic OPD 方法题。  
**生成时间**：2026-08-22  
**流程结果**：7 个机械去重候选 → 1 个条件推荐 → 1 个 backup → 5 个归档。  
**审查等级**：same-family Codex reviewer，结论为 provisional；尚无 pilot。

## Landscape Summary

近四个月的 agentic OPD 已快速覆盖 rollout depth、step/turn loss allocation、teacher prefix/bridge、state-reference matching、privileged guidance 和 repetitive-loop agreement。因而“错误累积后何时截断、何时介入、怎样重加权”不再是安全蓝海。

另一个正在成形但还没有被 agentic OPD 充分占据的问题是：环境中可能存在多条功能等价的成功路线，而 token-level teacher distribution 会偏好其中少数表面路线。已有工作已经表明 on-policy self-distillation 可能提高 pass@1 同时压低功能/语义多样性，但尚未把这个现象变成可执行 agent 的 failure mode：首选工具失效后，student 是否还保留能完成同一环境效果的备用路线。

OpenAgent 已经提供 action/observation shift 的可控 sandbox；Tool-Call Drift 说明 token support 与工具行为不是同一回事。这两者使“execution-equivalent route preservation”成为可测的 setting，但不能替代本题所需的 OPD-specific 因果证据。

## 推荐 Idea：Quotient-OPD / Execution-Equivalent Route Preservation

- **Method（实际做什么）**：
  1. 在确定性工具环境中执行 student rollouts，把到达同一 canonical state/effect 的不同工具路径聚成一个 execution-equivalence class。
  2. 将 teacher/student 的 trajectory probability push forward 到效果类，只蒸馏“更应该到达哪个效果类”，不强迫 student 模仿 teacher 在同一正确类中的某一条表面路径。
  3. 在每个正确效果类内部保留 reference student 的路径概率比，或显式约束不同首工具的有效覆盖，避免 teacher preference 把所有质量压到单一路线。
  4. 训练时所有冗余工具可用；测试时禁用训练后最常用的首工具，直接验证备用路线是否仍存在。
- **Failure mode × Setting**：标准 OPD 在“有多条 execution-equivalent 成功工具路径的 multi-tool agent”中压掉备用路线；原分布 success 不降，但工具失效后的 robustness 显著下降。
- **Hypothesis**：与 RL/SFT 相比，token OPD 在匹配 pass@1/success 时更容易集中到 teacher-preferred route；quotient/effect-class objective 能保留备用路线并提高 tool-outage robustness。
- **为什么是方法论文而非纯诊断**：训练目标直接改变 supervision space，并以类内 ratio preservation 修复；不是只报告 diversity 曲线。
- **最小实验**：两个确定性 tool DAG；每题 2–4 条不同首工具、相同终态的正确路线；Qwen3-1.7B student、Qwen3-8B teacher；三 seed 比较 SFT、GRPO、token OPD、entropy OPD、support-union、Quotient-OPD。
- **成功门槛**：vanilla OPD 在原分布 success 不弱于 SFT/RL 时，禁用首选工具后至少下降 15 点；Quotient-OPD 在两个环境族恢复至少 10 点，原分布损失不超过 2 点，并领先 entropy/support-union 至少 5 点。
- **停止门槛**：vanilla OPD 不稳定地降低备用路线覆盖；简单 entropy/support-union 与方法差距不超过 3 点；或 effect class 只能靠人工枚举而不能由 executor terminal state 自动得到。
- **Novelty**：6.5/10（provisional）。
- **Feasibility**：8/10。pilot 预计不超过 24 A100-hours；完整三 seed 约 160–320 A100-hours。
- **Risk**：MEDIUM。
- **Contribution type**：new method + agent failure mode。
- **Pilot result**：SKIPPED；当前还没有可运行的 OPD agent pipeline。
- **Reviewer 最强反驳**：匹配 equivalence-class 总概率并不会自动保留类内多条路线；如果还要枚举所有路径或提供 oracle 终态标签，方法会退化为玩具 DAG 技巧。

## 最危险近邻

| Paper | 已覆盖内容 | 本题必须留下的增量 |
|---|---|---|
| On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity (arXiv:2606.26091) | 证明 self-distillation 会压低 functional/semantic diversity，flatten pass@k | 把 diversity collapse 变成 executor-verifiable 的备用工具路线丢失，并给出 effect-class training objective |
| Better State Exploration Using Action Sequence Equivalence (arXiv:2110.10632) | 利用不同 action sequences 产生相同效果的先验改善 RL exploration | 目标改为 OPD supervision quotient 与 class-internal route preservation，而非探索策略 |
| Tool-Call Drift (arXiv:2607.07050) | top-k support 遗漏行为切换 token导致 tool over-calling | 研究完整执行路径的效果等价类与 tool outage robustness，而非单个 tool-entry token |
| OpenAgent (arXiv:2607.01084) | SFT/RL 在 open-world action/observation shift 下退化 | 证明 OPD 相比非蒸馏基线有特有的等价路线坍缩并修复 |

## Backup：Schema-Invariant Action OPD

语义相同、schema 不同产生 false disagreement；表面名字相同、语义改变产生 false agreement。其工程可行性更高，但 novelty 风险也更高：TSCG、OpenAgent 和普通 schema augmentation 都可能吃掉贡献。只有当 canonical action OPD 稳定领先统一编译器和 schema augmentation 至少 5 点时才值得继续。

## 归档候选

| Candidate | Decision | 主要原因 |
|---|---|---|
| Executable-action support mismatch | PARK | effect label 与多步时序对齐可能依赖 oracle；Sub-goal Distillation / GAPD 很近 |
| Stale-teacher under tool evolution | ARCHIVE | FutureBridge 与 progress-based OPD filtering 已占据验证 teacher signal 的核心机制 |
| Privileged-observation leakage | ARCHIVE | privileged policy distillation、SMRC-SD、AR-OPD 和 POMDP 工作已非常接近 |
| Irreversible-action risk blindness | PARK | 容易变成 safe RL / risk-weighted KL；真实不可逆动作复现困难 |
| Observation-equivalent latent states | ARCHIVE | 容易退化为 belief state、memory 或 state matching |

## 这个 Idea 来自哪个 xxPO Pattern

不是“把某个 XXPO 名字搬进 OPD”，而是迁移下面这个结构：

> 当多个行为得到相同 reward / outcome 时，优化器是否不必要地改变它们之间的相对概率？

在 reasoning GRPO 中，这通常表现为 exploration / diversity / clipping 问题；在 agentic OPD 中，可以落到一个更可测的对象：多个 action paths 是否到达同一环境效果，以及首选工具失效后是否仍能切换到等价路线。

以后抽取 xxPO pattern 时，固定只记四项：

1. **failure**：原算法在哪种分布或轨迹上坏；
2. **observable**：作者用什么量证明它真的坏；
3. **intervention**：改的是 sampling、advantage、constraint、support 还是 granularity；
4. **boundary**：什么条件下方法不再有效。

论文名、公式和 acronym 只是证据，不是 pattern 本身。

## 建议执行顺序

1. 先做 model-free tool DAG 与 equivalence-class evaluator。
2. 用现成模型只跑 rollout，确认每题确实存在多个可行首动作。
3. 只训练 vanilla OPD，验证备用路线是否比 SFT/GRPO 更快消失。
4. failure 不出现则立即停止；出现后才实现 Quotient-OPD。
5. pilot 过门槛后再迁移到 OpenAgent redundant-tool / tool-error 场景。
