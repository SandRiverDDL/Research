# 已抽卡 OPD 方法完整索引

> 2026-10-06 整理：阅读导航；保留原文的时间与覆盖口径，不代表当前全库。最新具体机制见 [failure-mode 诊断](../failure-modes/concrete-failure-modes.md)。

更新：2026-09-28。范围：registry 识别的 **77 张正式卡片**，每张恰好出现一次。只总结已抽卡集合，不代表完整领域覆盖。[先读短版](opd-method-map.md)。

这些分组是本次阅读导航，不改变项目 taxonomy、准入标准或卡片 schema。跨类论文只列一个主类；邻近方法和机制分析单列，不把 77 张卡片当成 77 个严格 LLM OPD 算法。

**证据口径**：下面是现有卡片的保守转述，卡片链接可追到原论文和已有章节锚点；不是本轮逐篇全文复核后的结论。旧卡可信度不均，不将摘要中的推测升级为领域定论。没有统一复核开源状态、作者机构、benchmark 或性能，因而不补造这些字段，也不做可信度排名。

## 1. 基础目标与梯度估计（10）

如何把 teacher 分布变成 student 更新。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [GKD](../../notes/24_gkd.md) | 在 student 自生成 prefix 上接受 teacher 监督，允许独立选择 divergence 与离线/在线混合比例。 |
| [MiniLLM](../../notes/24_minillm.md) | 围绕 sequence-level reverse-KL 推导策略梯度，用混合采样、分解和长度归一化稳定训练。 |
| [DistiLLM](../../notes/24_distillm.md) | 用 skew divergence 稳定分布匹配，并以 replay 复用生成样本；兼属效率路线。 |
| [DistiLLM-2](../../notes/25_distillm-2.md) | 按 teacher/student 样本来源配置 SKL/SRKL，并以 curriculum 调整平滑强度。 |
| [EOPD](../../notes/26_eopd.md) | 根据 teacher entropy 给 reverse-KL 补充 forward-KL，避免所有 token 固定使用同一目标。 |
| [OPD+](../../notes/26_opd-plus.md) | 检查 f-divergence 中 student-dependent 项的停梯度位置，修正 advantage 的梯度估计。 |
| [Revisiting OPD](../../notes/26_revisiting-opd.md) | 用 teacher top-K 支持集匹配与 special-token masking 修补 sampled-token 监督；兼属诊断。 |
| [TrOPD](../../notes/26_trust-region-opd.md) | 可信 token 用 sampled reverse-KL，异常位置切到 top-K forward-KL，并逐步撤去 teacher prefix。 |
| [ReOPOLD](../../notes/26_reopold.md) | 用 reward clipping、选择性 token 更新和阶段调度抑制极端信号及过早熵收缩。 |
| [GNDPO](../../notes/26_gndpo.md) | 在 batch 内归一化 token KL reward，缓解极端 log-ratio 主导多模态推理更新。 |

## 2. 样本与 token 选择（9）

监督预算应分给哪些 prompt、轨迹和 token。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [BRTS](../../notes/26_brts.md) | 筛选正确且对齐的 teacher 轨迹，再结合 teacher-context 与 student-context 监督。 |
| [FiRe-OPD](../../notes/26_global-token-filter.md) | 先按 teacher 轨迹似然硬过滤，再结合 teacher 置信度和 student 不确定性做 token 软加权。 |
| [ReNIO](../../notes/26_renio.md) | 从错误轨迹的 student-teacher 偏差中定位关键 token，重加权负轨迹的学习贡献。 |
| [Rock Tokens](../../notes/26_rock-tokens.md) | 分析持续高损失位置的功能贡献，以窗口重加权或冻结减少低贡献区域的训练。 |
| [TIP](../../notes/26_tip.md) | 联合 entropy 与 divergence 选 token，兼顾不确定位置与自信但错误的位置。 |
| [SCOPE](../../notes/26_scope.md) | 按正误分流：错误轨迹做 teacher 可靠性加权 KL，正确轨迹强化 student 低置信的成功行为。 |
| [PACED](../../notes/26_paced.md) | 用 student empirical pass rate 把 prompt 采样集中在能力边界。 |
| [Uni-OPD](../../notes/26_uni-opd.md) | 平衡难度和正误以改善状态采样，同时用 outcome-guided margin 校准监督排序。 |
| [PW-OPSD](../../notes/26_position-weighted-opsd.md) | 按位置调整 OPSD 监督权重，并结合 branch viability 分析可靠性；兼属自蒸馏。 |

## 3. 轨迹修复与训练效率（10）

走多远、何时停止局部监督，以及怎样减少训练开销。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [ESR](../../notes/26_early-stopping-rollout.md) | 限制 rollout 长度，减少深层 student prefix 上可能退化的监督和生成开销。 |
| [Progressive / Truncated OPD](../../notes/26_full-rollouts-necessary.md) | 比较逐步扩展 horizon 与固定短 prefix，检验完整 rollout 是否必要。 |
| [KAT](../../notes/26_kl-agreement-trap.md) | 用局部 KL 统计触发 rollout 终止，针对退化 prefix 上的低 KL 假一致。 |
| [Prefix Teach, Suffix Fade](../../notes/26_prefix-teach-suffix-fade.md) | 诊断后缀 local teachability 下降，并引入按轨迹释放监督的规则。 |
| [Prune-OPD](../../notes/26_prune-opd.md) | 用 top-k overlap 监测兼容性，漂移后递减权重并动态截断。 |
| [Supervision Fidelity Decay / LGR](../../notes/26_supervision-fidelity-decay.md) | 诊断 prefix 延长时的信号退化，并引入 one-step lookahead teacher confidence。 |
| [TRD](../../notes/26_trajectory-refined-distillation.md) | 先修复 reasoning trajectory 再蒸馏，针对单点修正难挽回的路径错误。 |
| [Trajectory-aware OPD](../../notes/26_near-future-guidance.md) | 比较同一 prefix 后的短未来，以 OT 对齐构造多位置监督；勿与 Truncated OPD 混淆。 |
| [Lightning OPD](../../notes/26_lightning-opd.md) | 在 teacher consistency 等条件下用离线轨迹和校正近似在线训练；不等同于每步 student rollout。 |
| [EffOPD](../../notes/26_effopd.md) | 沿早期参数更新方向外推，由验证集接受或拒绝候选，以减少后续训练步数。 |

## 4. Context 与自蒸馏（9）

teacher 可以拥有额外上下文，也可以由 student 自己构造。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [OPSD](../../notes/26_opsd.md) | 同模型 teacher 看参考解、student 不看，在 student rollout 上蒸馏条件化分布。 |
| [OPCD](../../notes/26_on-policy-context-distill.md) | 将经验或 system prompt 放入 teacher context，在 student 轨迹上将行为内化到参数。 |
| [SDFT](../../notes/26_sdft.md) | 用 demonstration-conditioned teacher 指导 student rollout，并通过 EMA teacher 组织持续学习。 |
| [OEL](../../notes/26_online-experiential.md) | 从部署轨迹抽取经验，再用 on-policy context distillation 写回参数，形成迭代循环。 |
| [AR-OPD](../../notes/26_ar-opd.md) | 以去掉答案的 partial-oracle teacher 为 anchor，将 full-view 信号作为缩放 residual。 |
| [RLCSD](../../notes/26_rlcsd.md) | 对比正确/错误 hint 的条件信号，尝试抵消共享风格成分、提取任务监督；兼属 RL。 |
| [SGSD](../../notes/26_sgsd.md) | 构造 skill-conditioned teacher pool，依据 verifier 结果门控、反转或丢弃信号。 |
| [MOPD](../../notes/26_multi-rollout-peer.md) | 将同 prompt 的成功和失败 peer rollouts 纳入 teacher context，利用跨轨迹对比。 |
| [SSOPD](../../notes/26_ssopd.md) | 以同组短正确 completion 指导长错误 completion 的 prefixes，并聚焦正误并存的 prompt。 |

## 5. 与 RL 耦合（7）

如何组合模仿、探索与 outcome credit。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [KDRL](../../notes/25_kdrl.md) | 结合规则奖励 policy gradient 与 teacher reverse-KL，用蒸馏先验辅助探索。 |
| [AlignDistil](../../notes/25_aligndistil.md) | 由 preference 隐式 reward 构造 token teacher 分布；属于 alignment/distillation 近邻，不默认视作完整 rollout OPD。 |
| [G-OPD / ExOPD](../../notes/26_g-opd-reward-extrapolation.md) | 在 KL-constrained RL 视角调节 teacher reward 强度，探索超出直接模仿的更新。 |
| [HDPO](../../notes/26_hdpo.md) | 在 GRPO 同 prompt 全失败时，引入 ground-truth-conditioned 自蒸馏补充梯度。 |
| [CAST](../../notes/26_cast.md) | 不用答案特权，以 self-teacher 和轨迹正误塑造 token advantage，处理全对/全错组。 |
| [Internalize the Temperature](../../notes/26_internalize.md) | 以高温 self-teacher 的 on-policy 蒸馏恢复探索分布，再继续 RL。 |
| [TGPO](../../notes/26_tgpo.md) | 将逐步 teacher guidance 加入 GRPO，并逐渐减弱，兼顾早期指导与后期探索。 |

## 6. 监督接口与隐私约束（5）

标准同 tokenizer、white-box logits 接口并非总可用。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [BOPD](../../notes/25_bopd.md) | 用 teacher 文本训练 discriminator，以动态判别信号作为 student 的 on-policy reward。 |
| [ROPD](../../notes/26_ropd.md) | 从 teacher/student 对比归纳 rubric，以语义评分替代 white-box token logits。 |
| [OPRD](../../notes/26_oprd.md) | 在 student rollout 上匹配 hidden representations，将监督对象移到输出分布之前。 |
| [SimCT](../../notes/26_simct.md) | 以双方 tokenizer 可表达的短 multi-token continuation units 恢复跨 tokenizer 监督。 |
| [DP-OPD](../../notes/26_dp-opd.md) | 由冻结 teacher 指导 student continuations，student 侧采用 DP-SGD 满足隐私约束。 |

## 7. 长程 agent（4）

监督和预算需要处理 step、turn 与环境反馈。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [SOD](../../notes/26_sod.md) | 按累计 step divergence 调弱不兼容步骤的蒸馏，针对错误 tool call 与 observation 的污染。 |
| [Segment-Level OPD / CHOP](../../notes/26_segment-level-opd.md) | 用局部监督与最终成功的对齐诊断及在线代理做 segment routing。 |
| [TurnOPD](../../notes/26_turnopd.md) | 周期性 full-depth probe 调节 turn horizon，并逐步转向 turn-balanced loss；兼属效率路线。 |
| [PBSD](../../notes/26_pbsd.md) | 将答案条件化 teacher/student 似然比转为 turn-level Bayesian credit；兼属特权自蒸馏。 |

## 8. 多模态与具身（6）

不同论文改变的不只是应用名称，也包括 teacher 可见信息和监督对象。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [VOLD](../../notes/25_vold.md) | 用 text-only teacher 指导 VLM on-policy reasoning 并结合 GRPO，强调分布对齐的 cold start。 |
| [Decomposed OPD](../../notes/26_decomposed-opd.md) | 分离 language prior 与 visual grounding，偏转视觉梯度并约束语言能力损伤。 |
| [Video-OPD](../../notes/26_video-opd.md) | 在视频定位上用 teacher token 评分做 OPD，通过 TVDF 筛掉不可靠监督并选择分歧轨迹。 |
| [X-OPD](../../notes/26_x-opd.md) | speech student 自身 rollout，由 text teacher 提供推理监督，实现跨模态能力对齐。 |
| [ViCuR](../../notes/26_vicur.md) | 用从输入图像可恢复的 visual cues 构造特权 teacher，区别于额外答案/推理链条件；兼属自蒸馏。 |
| [FA-OPD](../../notes/26_fa-opd.md) | 学习 Flow Matching teacher，在 student visits 上给 action target 和 discriminator reward；属于具身 imitation learning。 |

## 9. 邻近方法（8）

帮助理解 OPD 的设计选择，但不等同于完整 student-rollout OPD。

| 方法 / 卡片 | 一句话机制与边界 |
|---|---|
| [Lion](../../notes/23_lion.md) | API teacher/referee/generator 迭代发现 student 弱点并生成指令，核心是 student-aware 数据课程。 |
| [AKL](../../notes/24_akl.md) | 按 head-tail 分布差距混合 FKL/RKL，是 divergence 选择的 KD 背景方法。 |
| [SPIN](../../notes/24_spin.md) | 用旧模型回复作负例、SFT 示范作正例迭代 self-play，核心是偏好式自提升。 |
| [LUFFY](../../notes/25_luffy.md) | 将强策略的 off-policy 推理轨迹引入 RL，通过校正促进探索。 |
| [Pangu Embedded](../../notes/25_pangu-embedded.md) | 组合能力感知筛选、model merging、RL 与快慢系统，是多阶段训练 recipe。 |
| [TAID](../../notes/25_taid.md) | 在 student/teacher logits 间构造逐步移动的中间目标，缓解 KD 能力差距。 |
| [HPD](../../notes/26_hpd.md) | 在离线 expert prefixes 上加入 student token sampling 与局部混合 KL 修正，是近似 on-policy。 |
| [SPoT / Surgical Post-Training](../../notes/26_surgical-distill.md) | 用最小编辑正负样本与解耦 BCO 更新纠错并保留知识，属于邻近 post-training。 |

## 10. 机制与边界分析（9）

这些论文可能包含修复方案或 recipe，但这里优先按诊断贡献索引。

| 论文 / 卡片 | 一句话机制与边界 |
|---|---|
| [Rethinking the Capacity Gap](../../notes/26_capacity-gap-rethinking.md) | 讨论 student prefixes 上 teacher 目标是否可学；现有卡片算法细节不足，暂作诊断入口。 |
| [Dense Supervision, Sparse Updates](../../notes/26_dense-supervision-sparse-updates.md) | 分析参数更新的坐标稀疏性与谱集中，区分监督密度和参数变化。 |
| [Distributional DAgger](../../notes/26_distributional-dagger.md) | 区分 divergence 与梯度估计，研究 rich-feedback/self-distillation 的策略改进条件。 |
| [Extrapolation Cliff](../../notes/26_extrapolation-cliff.md) | 分析近确定结构化输出上的 reward 外推阈值与格式崩溃风险。 |
| [Geometry of OPD](../../notes/26_geometry-opd.md) | 用子空间旋转、谱漂移与更新重叠分析 OPD 的参数几何。 |
| [Many Faces of OPD](../../notes/26_many-faces-opd.md) | 系统研究 teacher、loss 和 privileged information 的适用边界，同时给修复建议。 |
| [Rethinking OPD](../../notes/26_rethinking-opd-llm.md) | 从 thinking-pattern 兼容性与新增能力分析 teacher 选择，并给 cold start/prompt selection recipe。 |
| [Stage-1 Controls the Entropy Regime](../../notes/26_stage1-entropy-regime.md) | 比较小数据 VLM 的 SFT/OPD warm-start 和后续 RL，检验初始探索差异是否转化为最终收益。 |
| [States, Not Tokens](../../notes/26_states-not-tokens.md) | 以访问状态与监督来源统一比较 SFT、RL、OPD，提供概念框架。 |

## 本轮原始来源核查与限制

- [GKD 原始摘要](https://arxiv.org/abs/2306.13649)：核对 student 自生成序列与可选 divergence，因此不把 GKD 简化为固定 forward-KL。
- [HPD 原始摘要](https://arxiv.org/abs/2604.20244)：明确 off-policy data 加 lightweight approximate on-policy sampling；离线 prefix 的细节见卡片 §4.2 锚点，因此与完整 student rollout 分开。
- [FA-OPD 原始页面](https://arxiv.org/abs/2605.27095)：当前标题为 *Adversarial Dual On-Policy Distillation from Expressive Teacher*，与旧卡略有变化；保留旧卡，本表使用简称。
- [Many Faces 原始页面](https://arxiv.org/abs/2605.11182)：作为经验边界研究入口，不将部分 PI 设置下的失败推广到所有 self-distillation。

本轮没有重新逐页精读全部 PDF，没有统一复核代码、数据、机构、算力和录用情况。分类用于检索，不是性能排行榜或 novelty 查新的替代；选择 baseline 时仍需回到原文和代码。
