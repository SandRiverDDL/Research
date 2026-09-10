# Agentic OPD：Failure Mode × Setting 候选集

**生成时间**：2026-08-22  
**约束**：8×A100 可快速试验；避开 step/turn reweighting、rollout depth、prefix replay、teacher handoff、state-reference matching、重复循环和通用 OPD+RL。  
**判定边界**：以下仅为供独立 reviewer 审核的候选，不代表 novelty 或推荐结论。

## 已占据的近邻

- OpenAgent（arXiv:2607.01084）：SFT/RL 在 query、action、observation、domain shift 下的脆弱性，并用 perturbation-augmented SFT 修复。
- Tool-Call Drift（arXiv:2607.07050）：top-k teacher support 漏掉行为切换 token，导致多 teacher OPD 工具过调用。
- SMRC-SD（arXiv:2608.05219）：privileged reference 与当前 student state 不匹配。
- FutureBridge-OPD（arXiv:2608.01953）：用 teacher bridge 及后续 student continuation 验证局部干预。
- TurnOPD / Guided-OPD / ReOPD / SOD：分别占据 rollout 深度、teacher turn curriculum、prefix replay 和 step weighting。
- Mismatch Matters（arXiv:2608.09836）：repetitive loop 造成 degenerate token agreement。
- TSCG（arXiv:2605.04107）：工具 schema 的确定性序列化/编译，但不做 OPD。
- GAPD（arXiv:2605.29584）：用 KBQA gold actions 和 state anchors 提供 agent RL 的 on-policy distillation。

## 机械去重后的候选

### C1 — Schema-induced false agreement / disagreement

- **dedup_key**：`schema-semantic-aliasing-opd`
- **failure_mode**：token-level OPD 把工具调用的表面字符串当作动作。语义相同但 tool name / argument schema 不同时产生虚假高 KL；名称相同但工具语义版本改变时产生虚假低 KL。
- **setting**：teacher 与 student 使用语义同构但序列化不同的工具接口；或同一工具的 v1/v2 schema。
- **OPD-specific**：OPD 的 teacher signal 本身以 token distribution 表示；一旦动作语义与 token identity 脱钩，监督度量不再对应要迁移的 policy。
- **最小 method**：Schema-Invariant Action OPD。把可执行工具调用映射到 canonical operation/argument-role ID；teacher 和 student 各自在自己的 schema 下给候选 canonical actions 打分，在 action space 做 KL，非 action 文本仍用普通 token OPD。
- **最小实验**：OpenAgent 的 tool rename、identity erasure、semantic trap；Qwen3-1.7B student、Qwen3-8B teacher；比较 token OPD、perturbation SFT、paired-schema consistency、canonical-action OPD。
- **危险近邻/反驳**：OpenAgent 已做 action shift；PAFT 已做 schema perturbation。若 canonical map 是人工给定，reviewer 可能认为只是工程 adapter。
- **8 卡成本**：pilot 约 8–24 A100-hours；完整三 seed 约 100–220 A100-hours。

### C2 — Executable-action support mismatch

- **dedup_key**：`asymmetric-tool-support-opd`
- **failure_mode**：teacher 的高概率动作位于 student 不可执行的 action support；mask 掉 unavailable tools 会删除监督，却不会告诉 student 如何用 primitive tools 实现相同意图。
- **setting**：teacher 拥有 composite/macro tools，student 只有 primitive tools；两者解决同一环境任务。
- **OPD-specific**：标准 KL 默认 teacher/student 在相同动作空间；这里该假设直接失效，raw-token distillation 会教 student hallucinate unavailable tools 或在 masking 后失去关键信号。
- **最小 method**：Effect-Space OPD。将 teacher macro action 与 student primitive action/短序列映射到共同的 information-goal 或 environment-effect label，在 effect space 蒸馏，再由 student 自己实现该 effect。
- **最小实验**：OpenAgent Path Planning 的 composite-tool / missing-tool 扰动，或一个确定性 tool-DAG 子集；先做 1-to-many macro→primitive 映射。
- **危险近邻/反驳**：Sub-goal Distillation、GAPD state anchors、semantic action abstractions；如果 effect label 需要人工 oracle，容易被认为是 privileged annotation。
- **8 卡成本**：pilot 约 16–40 A100-hours；完整三 seed 约 150–300 A100-hours。

### C3 — Stale-teacher negative transfer under tool evolution

- **dedup_key**：`stale-teacher-tool-version-opd`
- **failure_mode**：工具行为或 schema 更新后，frozen teacher 的参数记忆仍偏向旧版本；continuous OPD 可能覆盖 student 从新环境反馈中学到的适应行为。
- **setting**：non-stationary tool agent；训练前半使用 v1 工具，随后切换 v2，teacher/student 同时看到新文档但 teacher 更受旧习惯影响。
- **OPD-specific**：teacher 通常被默认始终更可靠；环境改变后，teacher KL 可能成为持续的负迁移源。
- **最小 method**：Feedback-Validated OPD。根据动作是否通过当前 executor、是否产生预期 observation，把 teacher signal 分为 supported / contradicted；只在当前环境证据支持时蒸馏。
- **最小实验**：OpenAgent semantic trap、calculation shift、tool redirection；对比 frozen teacher OPD、同步 teacher、自适应 gating、纯 RL。
- **危险近邻/反驳**：generic imperfect-teacher filtering、environment-feedback weighting；若 teacher 实际比 student 更能适应 v2，则 failure 不出现。
- **8 卡成本**：pilot 约 12–30 A100-hours；完整三 seed 约 120–250 A100-hours。

### C4 — Privileged-observation leakage

- **dedup_key**：`privileged-observation-leakage-opd`
- **failure_mode**：teacher 看到完整 environment state，student 只有 partial observation；teacher 的最佳动作依赖 student 不可获得的信息，密集 OPD 将不可实现策略当成目标。
- **setting**：部分可观测 agent；teacher 训练时有数据库/ground-truth state，student 部署时只有工具 observation。
- **OPD-specific**：privileged conditioning 改善 teacher accuracy，却可能破坏可蒸馏性；teacher target 不再是 student information set 下的可实现 policy。
- **最小 method**：Information-Set OPD。对 privileged state 做反事实重采样，只保留在所有与 student observation 一致的 latent states 上稳定的 teacher action preference。
- **最小实验**：构造可枚举 latent states 的 ALFWorld/OpenAgent 子环境；比较 full-state teacher、observation-only teacher、information-set aggregation。
- **危险近邻/反驳**：teacher-student learning under partial observability 已有成熟理论；SMRC-SD/privileged self-distillation 很接近。可能不是 LLM OPD 独有。
- **8 卡成本**：pilot 约 20–50 A100-hours；完整三 seed 约 180–350 A100-hours。

### C5 — Irreversible-action risk blindness

- **dedup_key**：`irreversible-action-risk-opd`
- **failure_mode**：token likelihood 不区分可撤销探索与不可撤销动作；teacher 在高不确定 state 上的少量概率质量可能通过 OPD 增加 catastrophic action，而平均 KL/成功率难以显露。
- **setting**：有 consumable resources、删除/提交/购买等不可逆 action 的 agent sandbox。
- **OPD-specific**：普通 OPD 对所有动作偏差使用同一 divergence；动作后果的非对称性未进入 teacher-student alignment objective。
- **最小 method**：Recoverability-Constrained OPD。利用可 snapshot 环境估计候选 action 的 recoverability，将 KL 分成 reversible 与 irreversible 支持，并对后者施加 conservative constraint。
- **最小实验**：可 checkpoint 的 deterministic tool environment；注入少量 irreversible choices，比较平均成功率、catastrophic rate、task progress。
- **危险近邻/反驳**：safe RL、AgentRewind、constrained policy optimization 已覆盖大概念；如果只是给危险动作加权，不足以构成 OPD 新方法。
- **8 卡成本**：pilot 约 20–60 A100-hours；完整三 seed 约 200–450 A100-hours。

### C6 — Observation-equivalent but transition-different states

- **dedup_key**：`state-alias-transition-opd`
- **failure_mode**：相同 textual observation 可对应不同 latent environment states；teacher/student token agreement 在一个 alias 下正确，在另一个 alias 下导致错误转移。
- **setting**：history-dependent、partially observable agent，环境提供同样 observation 但 inventory、permissions 或 hidden flags 不同。
- **OPD-specific**：OPD 把文本 prefix 当作 state；state aliasing 使同一监督 context 混合不同最优动作。
- **最小 method**：Transition-Identifiable OPD。用历史中能够区分 latent transitions 的最小 sufficient trace 对 teacher conditioning 或 loss 分桶。
- **最小实验**：ALFWorld/ScienceWorld 中人为构造 observation aliases；测 action entropy、错误转移率和 success。
- **危险近邻/反驳**：POMDP belief-state learning、MemOPD、state-matched routing；若补齐 history 就能解决，会被认为是常规 memory engineering。
- **8 卡成本**：pilot 约 16–40 A100-hours；完整三 seed 约 150–300 A100-hours。

### C7 — Outcome-equivalent action multiplicity

- **dedup_key**：`execution-equivalence-multimodal-opd`
- **failure_mode**：多个不同工具序列产生相同有效结果，reverse-KL mode seeking 可能把 student 拉向 teacher 的单一路径并损失替代路径；在某个工具失效时鲁棒性反而下降。
- **setting**：有 redundant tools / alternate routes 的 multi-tool agent，并在测试时随机禁用一路工具。
- **OPD-specific**：teacher token distribution 表达的是一种 surface policy，不是所有 execution-equivalent policies；OPD gain 可能以 action diversity 和故障恢复为代价。
- **最小 method**：Equivalence-Class OPD。把到达同一 canonical state/effect 的多条 action paths 归为一类，蒸馏类概率而非单一 token path。
- **最小实验**：OpenAgent redundant tool / error return 场景；训练时工具都可用，测试时一条 route 失效；比较成功率与替代路径保留率。
- **危险近邻/反驳**：mode collapse、sequence-level distillation、multi-rollout peer methods；需要证明这不是普通多样性正则。
- **8 卡成本**：pilot 约 16–40 A100-hours；完整三 seed 约 160–320 A100-hours。

## 客观可行性门

七个候选都可在公开、确定性或可控 sandbox 中建立最小版本，没有因算力或数据不可得被机械淘汰。C2、C4、C5、C6 需要额外环境标注或 simulator access，工程风险高于 C1、C3、C7。
