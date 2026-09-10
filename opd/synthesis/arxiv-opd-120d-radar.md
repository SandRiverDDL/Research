# OPD arXiv Radar：近 120 天

窗口：2026-03-31 至 2026-07-29。检索时间：2026-07-29。

口径：标题或摘要明确涉及 on-policy distillation，并以 LLM、agent 或 MLLM 为主要对象。排除 diffusion/flow、传统机器人控制、蛋白质等同名但偏离当前项目的问题。该口径得到 103 篇候选：4 月 11 篇、5 月 43 篇、6 月 27 篇、7 月 22 篇。

这是一份高召回 radar，不等于 103 篇都可信或值得抽卡。以下判断主要基于 arXiv metadata 与摘要；是否开源、实验是否可靠、是否已录用仍需逐篇核验。

## 最值得先读的论文

| 论文 | 一句话贡献 | 对应瓶颈 |
|---|---|---|
| [Rethinking OPD](https://arxiv.org/abs/2604.13016) | OPD 成功要求 teacher–student thinking pattern 兼容，且 teacher 真正带来 student 未见能力。 | teacher–student mismatch |
| [TIP](https://arxiv.org/abs/2604.14084) | 有效 token 不只来自高 student entropy，也来自低 entropy、高 teacher–student divergence。 | uniform token supervision |
| [The Illusion of Certainty](https://arxiv.org/abs/2604.16830) | privileged teacher 能提升准确率，却会系统性制造部署时过度自信。 | train–deployment information mismatch |
| [TCOD](https://arxiv.org/abs/2604.24005) | 逐步增加 agent trajectory depth，避免长程误差把 student 推出 teacher 的有效支持域。 | long-horizon error compounding |
| [MAD-OPD](https://arxiv.org/abs/2605.01347) | 用 multi-agent debate 生成比单 teacher 更强的监督，尝试突破 teacher ceiling。 | single-teacher ceiling |
| [Uni-OPD](https://arxiv.org/abs/2605.03677) | 把瓶颈归纳为 informative-state exploration 不足和 teacher supervision 不可靠。 | state coverage + signal reliability |
| [Near-Policy](https://arxiv.org/abs/2605.05940) | generation/training 异步化并过滤过旧样本，主攻 OPD 吞吐。 | synchronous rollout cost |
| [Rubric-based OPD](https://arxiv.org/abs/2605.07396) | 用 teacher 生成的语义 rubric 代替 logits，实现 black-box OPD。 | white-box teacher dependency |
| [SimCT](https://arxiv.org/abs/2605.07711) | 以共同可实现的短 continuation 恢复 cross-tokenizer 时丢失的监督。 | tokenizer mismatch |
| [Prune-OPD](https://arxiv.org/abs/2605.07804) | 只在长轨迹中的关键部分调用或保留 teacher 信号。 | long-horizon cost/noise |
| [The Extrapolation Cliff](https://arxiv.org/abs/2605.08737) | 指出近确定性结构化输出中，student 离开 teacher 支持后会出现外推崩溃。 | local support mismatch |
| [The Many Faces of OPD](https://arxiv.org/abs/2605.11182) | 系统检查 OPD 何时有效、何时伤害以及常见修补手段。 | mechanism ambiguity |
| [Prefix Teach, Suffix Fade](https://arxiv.org/abs/2605.13643) | teacher 信号沿 reasoning trajectory 后段衰减，局部 teachability 并不恒定。 | supervision fidelity decay |
| [Post-Training Is About States, Not Tokens](https://arxiv.org/abs/2605.22731) | 把 SFT/RL/OPD 的关键差异重述为访问什么 state，而非只看 token loss。 | state-distribution coverage |
| [Not All Disagreement Is Learnable](https://arxiv.org/abs/2605.26844) | teacher–student disagreement 不等于可学习纠错信号。 | token teachability |
| [Your Teacher Can't Help You Here](https://arxiv.org/abs/2605.30833) | student 走远后 teacher 在该 prefix 上的监督质量下降。 | supervision fidelity decay |
| [Are Full Rollouts Necessary?](https://arxiv.org/abs/2605.31490) | 检验完整 rollout 是否必要，直接挑战 OPD 的主要计算成本。 | rollout efficiency |
| [Near-Future Guidance](https://arxiv.org/abs/2606.00305) | 用未来局部信息连接当前错误 prefix 和可恢复轨迹。 | error localization/recovery |
| [Trust Region OPD](https://arxiv.org/abs/2606.01249) | 限制 policy drift，避免 student rollouts 进入 teacher 监督失真的区域。 | policy drift |
| [On the Geometry of OPD](https://arxiv.org/abs/2606.07082) | 从梯度和分布几何解释 OPD 信号为何稀疏或冲突。 | optimization geometry |
| [Escaping the KL Agreement Trap](https://arxiv.org/abs/2606.09471) | 指出低 KL/agreement 不必然代表学习到了正确能力。 | agreement–correctness mismatch |
| [Dense Supervision, Sparse Updates](https://arxiv.org/abs/2606.13657) | 虽然 teacher 提供 dense logits，真正主导更新的 token/state 仍很稀疏。 | effective-signal sparsity |
| [AsyncOPD](https://arxiv.org/abs/2606.24143) | 直接测量 OPD 能容忍多旧的 rollouts，为异步训练寻找边界。 | staleness–throughput trade-off |
| [On the Position Bias of OPD](https://arxiv.org/abs/2606.22600) | 研究监督有效性随 token position 变化，而非默认各位置同质。 | position-dependent reliability |
| [DOPD](https://arxiv.org/abs/2606.30626) | 在不同来源的 privileged supervision 之间动态路由。 | single-source supervision |
| [Demystifying OPD](https://arxiv.org/abs/2607.13399) | 将 OPD 解释为 exploration catalyst，并诊断 mismatch 与 length exploitation。 | signal quality + objective gaming |
| [SEED](https://arxiv.org/abs/2607.14777) | 从完成的 agent trajectory 提炼 hindsight skill，再蒸馏回当前 policy。 | sparse agent credit |
| [OPD²](https://arxiv.org/abs/2607.15161) | 蒸馏 reasoning teacher 相对其 base model 的 policy delta，而非绝对分布。 | teacher baggage/capability isolation |
| [Direct-OPD](https://arxiv.org/abs/2607.05394) | 把弱模型 RL 前后的 log-ratio 当隐式 reward，向更强 student 迁移 RL 增量。 | weak-to-strong transfer |
| [Tool-Call Boundary Drift](https://arxiv.org/abs/2607.07050) | 局部结构 token 的小信号可导致全局 tool over-calling，aggregate KL 看不见。 | local signal/global behavior mismatch |
| [Outcome-Confounded Local Supervision](https://arxiv.org/abs/2607.23731) | 局部 agreement/disagreement 都被最终 outcome 混淆，无法定位失败从哪里变得不可恢复。 | causal credit localization |
| [Pass the Baton](https://arxiv.org/abs/2607.26057) | 检测错误分叉后让 teacher 短暂接管，再把轨迹交还 student。 | prefix failure |

## 完整候选清单

### 2026-04（11 篇）

- 04-30 [Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://arxiv.org/abs/2604.28123)
- 04-27 [TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/abs/2604.24005)
- 04-25 [Efficient Rationale-based Retrieval: On-policy Distillation from Generative Rerankers based on JEPA](https://arxiv.org/abs/2604.23336)
- 04-18 [The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation](https://arxiv.org/abs/2604.16830)
- 04-15 [TIP: Token Importance in On-Policy Distillation](https://arxiv.org/abs/2604.14084)
- 04-14 [Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](https://arxiv.org/abs/2604.13016)
- 04-14 [Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation](https://arxiv.org/abs/2604.13010)
- 04-12 [SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting](https://arxiv.org/abs/2604.10688)
- 04-09 [Demystifying OPD: Length Inflation and Stabilization Strategies for Large Language Models](https://arxiv.org/abs/2604.08527)
- 04-06 [DP-OPD: Differentially Private On-Policy Distillation for Language Models](https://arxiv.org/abs/2604.04461)
- 04-01 [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626)

### 2026-05（43 篇）

- 05-31 [OmniOPD: Logit-Free On-Policy Distillation via Speculative Verification](https://arxiv.org/abs/2606.01476)
- 05-31 [Trust Region On-Policy Distillation](https://arxiv.org/abs/2606.01249)
- 05-31 [OPD+: Rethinking the Advantage Design for On-Policy Distillation](https://arxiv.org/abs/2606.01039)
- 05-30 [Decomposed On-Policy Distillation for Vision-Language Reasoning](https://arxiv.org/abs/2606.00564)
- 05-29 [Bridging Reasoning Trajectories via Near-Future Guidance](https://arxiv.org/abs/2606.00305)
- 05-29 [Are Full Rollouts Necessary for On-Policy Distillation?](https://arxiv.org/abs/2605.31490)
- 05-29 [Trust-Region Behavior Blending for On-Policy Distillation](https://arxiv.org/abs/2605.31159)
- 05-29 [Your Teacher Can't Help You Here](https://arxiv.org/abs/2605.30833)
- 05-28 [Same Evidence, Different Answers](https://arxiv.org/abs/2605.30251)
- 05-28 [GAPD: Gold-Action Policy Distillation for Agentic RL](https://arxiv.org/abs/2605.29584)
- 05-28 [Draft-OPD](https://arxiv.org/abs/2605.29343)
- 05-27 [ADWIN: Adaptive Windows for Horizon-Aware OPD](https://arxiv.org/abs/2605.28396)
- 05-27 [From Fact Overwriting to Knowledge Evolution](https://arxiv.org/abs/2605.28303)
- 05-27 [Data-Efficient OPD for Automatic Speech Recognition](https://arxiv.org/abs/2605.28139)
- 05-26 [Counteraction-Aware Multi-Teacher OPD](https://arxiv.org/abs/2605.27115)
- 05-26 [Not All Disagreement Is Learnable](https://arxiv.org/abs/2605.26844)
- 05-25 [Extreme Region Policy Distillation](https://arxiv.org/abs/2605.25582)
- 05-22 [EDGE-OPD](https://arxiv.org/abs/2605.23493)
- 05-21 [Post-Training is About States, Not Tokens](https://arxiv.org/abs/2605.22731)
- 05-21 [Visual-Advantage OPD](https://arxiv.org/abs/2605.21924)
- 05-18 [Vision-OPD](https://arxiv.org/abs/2605.18740)
- 05-18 [A Brief Overview: On-Policy Self-Distillation](https://arxiv.org/abs/2605.18141)
- 05-18 [$f$-OPD](https://arxiv.org/abs/2605.17862)
- 05-17 [Self-Supervised OPD for Reasoning Language Models](https://arxiv.org/abs/2605.17497)
- 05-16 [Decoupling KL and Trajectories](https://arxiv.org/abs/2605.16826)
- 05-15 [Offline Semantic Guidance for VLA Policy Distillation](https://arxiv.org/abs/2605.16241)
- 05-13 [Reward-Weighted OPD for NL-to-SVA](https://arxiv.org/abs/2605.13501)
- 05-12 [Multi-Rollout OPD via Peer Successes and Failures](https://arxiv.org/abs/2605.12652)
- 05-12 [Beyond GRPO and OPD](https://arxiv.org/abs/2605.12483)
- 05-12 [Learning to Foresee](https://arxiv.org/abs/2605.11739)
- 05-11 [The Many Faces of OPD](https://arxiv.org/abs/2605.11182)
- 05-11 [Unmasking OPD](https://arxiv.org/abs/2605.10889)
- 05-10 [OPD with Best-of-N Teacher Rollout Selection](https://arxiv.org/abs/2605.09725)
- 05-10 [Rock Tokens in OPD](https://arxiv.org/abs/2605.09253)
- 05-09 [The Extrapolation Cliff](https://arxiv.org/abs/2605.08737)
- 05-08 [KL for a KL](https://arxiv.org/abs/2605.07865)
- 05-08 [Prune-OPD](https://arxiv.org/abs/2605.07804)
- 05-08 [SOD](https://arxiv.org/abs/2605.07725)
- 05-08 [SimCT](https://arxiv.org/abs/2605.07711)
- 05-08 [Rubric-based OPD](https://arxiv.org/abs/2605.07396)
- 05-07 [Asymmetric OPD](https://arxiv.org/abs/2605.06387)
- 05-05 [Uni-OPD](https://arxiv.org/abs/2605.03677)
- 05-02 [MAD-OPD](https://arxiv.org/abs/2605.01347)

### 2026-06（27 篇）

- 06-30 [One Student, Many Teachers](https://arxiv.org/abs/2607.18293)
- 06-29 [Behavior Cloning is Not All You Need](https://arxiv.org/abs/2606.30923)
- 06-29 [DOPD](https://arxiv.org/abs/2606.30626)
- 06-29 [MOPD](https://arxiv.org/abs/2606.30406)
- 06-26 [ATOD](https://arxiv.org/abs/2606.27814)
- 06-24 [V-Zero](https://arxiv.org/abs/2606.25319)
- 06-23 [AsyncOPD](https://arxiv.org/abs/2606.24143)
- 06-23 [Blockwise Policy-Drift Gating](https://arxiv.org/abs/2606.24084)
- 06-22 [ReNIO](https://arxiv.org/abs/2606.23104)
- 06-22 [A Formula-Driven Survey and Research Agenda for OPD](https://arxiv.org/abs/2606.22793)
- 06-21 [On the Position Bias of OPD](https://arxiv.org/abs/2606.22600)
- 06-20 [Prefix-Guided OPD](https://arxiv.org/abs/2606.21994)
- 06-17 [SAGE-OPD](https://arxiv.org/abs/2606.19659)
- 06-16 [OPD-Evolver](https://arxiv.org/abs/2606.17628)
- 06-15 [PowerOPD](https://arxiv.org/abs/2606.17199)
- 06-14 [Curriculum Turn-level Guidance](https://arxiv.org/abs/2606.15912)
- 06-11 [Dense Supervision, Sparse Updates](https://arxiv.org/abs/2606.13657)
- 06-10 [RLCSD](https://arxiv.org/abs/2606.11709)
- 06-09 [Anchored Residual Guidance](https://arxiv.org/abs/2606.10385)
- 06-08 [Escaping the KL Agreement Trap](https://arxiv.org/abs/2606.09471)
- 06-08 [Breaking the Tokenizer Barrier](https://arxiv.org/abs/2606.09456)
- 06-08 [SG-OPD](https://arxiv.org/abs/2606.09304)
- 06-08 [Global Normalization for MLLM OPD](https://arxiv.org/abs/2606.09091)
- 06-05 [On the Geometry of OPD](https://arxiv.org/abs/2606.07082)
- 06-04 [ViCuR](https://arxiv.org/abs/2606.05718)
- 06-01 [Filter, Then Reweight](https://arxiv.org/abs/2606.02684)
- 06-01 [SafeSteer](https://arxiv.org/abs/2606.02530)

### 2026-07（22 篇，截至 07-29）

- 07-28 [Pass the Baton](https://arxiv.org/abs/2607.26057)
- 07-26 [Outcome-Confounded Local Supervision](https://arxiv.org/abs/2607.23731)
- 07-24 [Cross-Tokenizer OPD via Byte-Prefix Marginalization](https://arxiv.org/abs/2607.22334)
- 07-23 [X³-OPD](https://arxiv.org/abs/2607.21550)
- 07-22 [SOPD-SocialNav](https://arxiv.org/abs/2607.19850)
- 07-21 [Contrastive OPD](https://arxiv.org/abs/2607.19046)
- 07-18 [CADENCE](https://arxiv.org/abs/2607.16955)
- 07-16 [SEED](https://arxiv.org/abs/2607.14777)
- 07-15 [Post-Training Shifts Confidence](https://arxiv.org/abs/2607.13753)
- 07-15 [Demystifying OPD: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399)
- 07-14 [ShortOPD](https://arxiv.org/abs/2607.13124)
- 07-14 [Med-OPD](https://arxiv.org/abs/2607.16303)
- 07-13 [EasyOPD](https://arxiv.org/abs/2607.11012)
- 07-08 [Tool-Call Boundary Drift](https://arxiv.org/abs/2607.07050)
- 07-07 [TurnOPD](https://arxiv.org/abs/2607.05804)
- 07-06 [Direct-OPD](https://arxiv.org/abs/2607.05394)
- 07-06 [Rethinking On-Policy Self-Distillation for Thinking Models](https://arxiv.org/abs/2607.05184)
- 07-06 [Multi-Turn OPD with Prefix Replay](https://arxiv.org/abs/2607.04763)
- 07-06 [Trust Region Policy Distillation](https://arxiv.org/abs/2607.04751)
- 07-05 [UI-MOPD](https://arxiv.org/abs/2607.04425)
- 07-04 [Reward-Gated OPD](https://arxiv.org/abs/2607.04037)
- 07-01 [H-OPD](https://arxiv.org/abs/2607.02592)

## 检索边界

- 日期按 arXiv 首次提交日，而不是最近修订日。
- 这是关键词高召回，不保证覆盖标题与摘要完全不用 OPD 术语的近邻工作。
- 全量表不代表抽卡建议；正式 L1 仍执行 `doc/card-acceptance.md`。
- 深读前必须重新核验代码、数据、模型、实验规模、作者机构与会议状态。
