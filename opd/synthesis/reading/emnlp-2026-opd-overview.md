# EMNLP 2026 OPD 相关论文分类与摘要级总结

> 2026-10-06 整理：阅读导航；保留原文的时间与覆盖口径，不代表当前全库。最新具体机制见 [failure-mode 诊断](../failure-modes/concrete-failure-modes.md)。

核查日期：2026-10-05。范围为此前从官方报告日程筛出的 38 篇 MAIN/FIND 候选，不声称全会议 OPD 全集。

会议身份依据：官网 https://2026.emnlp.org/program/ 链接的 Google Sheets；本地快照及来源说明见 `../tmp/emnlp-2026-index/README.md`。MAIN=M，FIND=F。分类是本报告的阅读组织方式，不修改 card taxonomy。

证据层级：33 篇读取原始 arXiv 摘要；TGPO 另读原文方法 3.1；MoralSteer 仅核对搜索引擎索引中的原始 PDF 摘要，直接下载被 403 拦截；4 篇未找到可核实摘要/全文，不能提供具体方法或结果。以下结论是作者在其设置中的报告，未经独立复现或全文实验审计。原始摘要证据保存在 `../tmp/emnlp-2026-index/opd-abstract-evidence.json`。

| 主类 | 已有摘要证据 | 主要问题 |
|---|---:|---|
| 1. 目标、梯度与监督分配 | 6 | teacher 信号怎样成为有效更新？ |
| 2. Rollout 构造与训练效率 | 3 | 在什么状态学，何时停止生成？ |
| 3. OPD 与 RL 的配合及机制分析 | 5 | 训练顺序、探索和置信度怎样变化？ |
| 4. 特权信息、长程交互与 credit | 7 | teacher 多看到什么，如何定位需要监督的动作？ |
| 5. 可控行为、知识更新与能力保持 | 8 | 如何改目标行为而不破坏其他行为？ |
| 6. 多模态、压缩与部署 | 5 | OPD 在特定模型或部署场景中怎样适配？ |
| 待证据 | 4 | 暂不凭标题总结方法和实验 |

## 1. 目标、梯度与监督分配：6 篇

- **PowerOPD（6742-MAIN）**：[原文](https://arxiv.org/abs/2606.17199)。诊断 sampled reverse-KL 的无界 log-ratio 奖励引起高方差和不稳定，用 Box–Cox 幂变换构造有界、保留奖惩符号的奖励。数学实验报告相对 vanilla OPD 更稳定且更强，最高 benchmark 平均 Avg@8 增益为 6.37；改变了监督变换，并非只是训练后缩放。
- **AOPD（903-FIND）**：[原文](https://arxiv.org/abs/2605.06387)。正优势 token 保留正向强化；非正优势区域改用局部散度最小化，避免只惩罚学生采出的 token 却不给替代方向。数学实验报告强/弱初始化下平均增益分别为 4.09/8.34，并维持较高策略熵。
- **TGPO（4395-FIND）**：[原文 §3.1](https://arxiv.org/html/2605.13230v2)。在每个学生访问的前缀上取得 teacher top-1 token，直接提高学生对该 token 的概率，并结合 GRPO 的结果奖励。大 teacher–student 分歧设置中优于比较的 RKL 方法；关键是由评价已采动作改为给出替代动作监督，不是让 teacher 接管 rollout。
- **SCOPE（3230-MAIN）**：[原文](https://arxiv.org/abs/2604.10688)。错误 rollout 用 teacher 困惑度加权 KL，正确 rollout 用 student 困惑度加权 MLE；组内归一化用于校准权重。六个推理 benchmark 报告 Avg@32/Pass@32 平均相对提升 11.42%/7.30%，核心是按正确性和信号可靠性分路训练。
- **Unified Per-Token Gating Family（4068-FIND）**：[原文](https://arxiv.org/abs/2609.11768)。用四系数 sigmoid 门控统一熵、样本信号、teacher–student gap 和 bias，控制 FKL/RKL 混合。短输出分类的扫描中多数比较有正向趋势，但三种子复验增益更小且不显著；新版主要将其定位为统一比较坐标系，不是已验证的普适强方法。
- **OISD（5049-FIND）**：[原文](https://arxiv.org/abs/2605.29089)。最终层作为 detached 内部 teacher，向中间层蒸馏 logits 和 attention，并与 GRPO 结合使用带符号优势加权的 JS alignment。不需要外部 teacher 或特权上下文，四个数学任务报告优于比较的推理 RL baseline；与通常的上下文特权 OPSD 不同。

## 2. Rollout 构造与训练效率：3 篇

- **ADWIN（1199-MAIN）**：[原文](https://arxiv.org/abs/2605.28396)。日常训练使用短前缀；延迟完成的全轨迹 probes 检查前缀更新和完整更新的对齐程度，再调整窗口，并处理 probe 陈旧性。数学、代码实验报告最高 4.1 倍训练成本下降而精度相当或更好，说明完整生成不总是每次更新所必需。
- **KAT / Escaping the KL Agreement Trap（5562-MAIN）**：[原文](https://arxiv.org/abs/2606.09471)。发现坏前缀下 teacher 可能也同意退化续写，出现低 KL 但无纠正力的陷阱；用动态阈值检测持续低 KL 并提前终止 rollout。四个数学 benchmark 报告准确率改善且平均 rollout 长度下降 59.73%，关键结论是低 KL 不一定意味着有效学习。
- **Persistent Teacher Anchoring（9793-MAIN）**：[原文](https://arxiv.org/abs/2609.04773)。teacher 验证学生提出的文本块，只有整轮工具调用也被验证后才允许执行；persistent lookahead 提前推进并跨更新保留未完成样本。检索和视觉工具任务中，下游 RL 的 macro best@4 分别提高 2.5/2.8 点，lookahead 吞吐提高 24%；它改的是 rollout 进入环境的方式。

## 3. OPD 与 RL 的配合及机制分析：5 篇

- **Sequential Beats Joint（2441-FIND）**：[原文](https://arxiv.org/abs/2609.04108)。比较联合优化和先 OPD 后 RL：作者解释 OPD 扩展 teacher 支持的解空间，RL 再在这个范围内强化成功行为，联合信号可能干扰。在其逻辑和数学设置中两阶段方案优于比较的联合 baseline，并用 OPD 验证集分数判断切换时机；不能外推为所有任务的规律。
- **Sparse-to-Dense Reward Principle（2459-FIND）**：[原文](https://arxiv.org/abs/2605.12483)。先对强 teacher 做 RL，再 FKL warmup 和 OPD 压缩到小学生，必要时继续学生 RL。固定 1.7B 部署学生时，MATH/AIME24 分别为 79.3/25.2，对比直接学生 GRPO 的 75.9/19.8；原始 teacher 的直接迁移反而较差，重点是稀缺可验证数据该用在哪个模型上。
- **TS-OPSD / Policy Reheater（6650-FIND）**：[原文](https://arxiv.org/abs/2606.00755)。对熵塌缩 RL checkpoint 的自身 logits 加高温，作为 self-teacher，再将平滑分布蒸馏进参数后继续 RL。两个 Qwen3 Base 模型实验中优于直接续训和只提高 rollout 温度；主要改变输出尖锐程度，较好保留原有候选集合与中间表征。
- **Long-Context Recipe（8082-FIND）**：[原文](https://arxiv.org/abs/2605.12227)。以学生 rollout 的结果奖励做 GRPO，用更强 teacher 提供密集 token regularization 替代普通 reference anchoring；另构建 LongBlocks。消融报告结合初始化、teacher anchoring 和数据混合的方案比单独 GRPO/OPD 更稳定有效，并保留短上下文能力；与 Sequential 的结论需要按任务和训练配置比较。
- **Post-Training Shifts Confidence / PosConf（6141-FIND）**：[原文](https://arxiv.org/abs/2607.13753)。将置信度拆成 CoT 前的难度估计、CoT 中的早停、CoT 后的答案聚合。受控数学实验发现 OPD/SFT/RL 分别更擅长这三个用途，且 OPD 后段可能反向校准；按位置选取可靠区间的 PosConf 改善聚合和早停，属于机制诊断加使用策略。

## 4. 特权信息、长程交互与 credit：7 篇

- **Guided-OPD（4203-MAIN）**：[原文](https://arxiv.org/abs/2606.15912)。在 rollout 中混合 teacher 和 student 生成的轮次，逐步将 teacher 接管概率退火到零，防止早期错误把学生带出 teacher 熟悉的状态范围。ALFWorld、ScienceWorld、WebShop 上，相对 vanilla OPD 的平均 Score/Success Rate 增益为 21.1%/25.5%，小学生改善更大。
- **MAIGO（2675-MAIN）**：[原文](https://arxiv.org/abs/2605.27186)。teacher 在中间轮去掉历史 assistant 回复以减轻错误自污染；最终回答轮看到完整用户侧需求，再蒸馏到学生自己的多轮轨迹。Qwen2.5-7B 的 SHARDED 准确率由 52.8 到 66.1，FULL 能力保持在 2.3 点以内；不用额外 verifier 或推理时 scaffold。
- **OPD-Evolver（3133-FIND）**：[原文](https://arxiv.org/abs/2606.17628)。快环在分层 memory 中读、用、写、维护经验；慢环利用结果校准的记忆归因和 hindsight 特权，将这些能力蒸馏进策略。多领域实验报告优于比较的 memory 系统和训练方法，说明目标是学会经验管理全流程，而非只把更多记忆放进 prompt。
- **HINT-SD（593-FIND）**：[原文](https://arxiv.org/abs/2605.17873)。先从完整轨迹 hindsight 定位失败相关动作，只在这些动作片段上进行反馈条件化 self-distillation。BFCL v3/AppWorld 上，相比逐轮密集反馈 baseline 报告最高 18.80% 改善，训练每步时间低 2.26 倍，核心是选对要纠正的位置。
- **StepOPSD（808-FIND）**：[原文](https://arxiv.org/abs/2605.27140)。按 action-centered step 切轨迹，用 hindsight teacher 重评分，将 token logprob 差转为保留原优势符号、每 step 归一化 credit budget 的 shaping，再做 GRPO。摘要报告长程 Agent 任务的收益；贡献是 step 级 credit 重分配，而不只是更换特权 prompt。
- **SGSD（4807-FIND）**：[原文](https://arxiv.org/abs/2605.28791)。从经验 skill bank 检索技能构造多个 teacher，共同评分同一学生 rollout；verifier 校验支持/反对的方向，门控压制不确定和极端信号。数学实验中优于 GRPO，并与参考答案特权 OPSD 竞争；研究的是较弱、不可靠特权信息怎样安全用于蒸馏。
- **CNY / Call Neighbours Yourself（6024-MAIN）**：[原文](https://arxiv.org/abs/2608.29588)。把图邻居选择变成可学习 graph-walk 动作；看到目的节点内容后，由 destination-conditioned self-teacher 回评之前的选择。TAG 推理实验报告优于固定上下文 baseline，并迁移到未见图和未训练过的图级任务；OPSD 是探索的延迟 credit 机制。

## 5. 可控行为、知识更新与能力保持：8 篇

- **SafeSteer（1446-MAIN）**：[原文](https://arxiv.org/abs/2606.02530)。activation steering 构造 safety teacher，再挑出安全相关 token，仅在这些位置做 RKL 蒸馏。只用 100 个有害样本，在七个安全 benchmark 改善安全、五个通用 benchmark 仅小幅退化；重点是局部改行为以减轻 alignment tax。
- **SecOPD（3136-MAIN）**：[原文](https://arxiv.org/abs/2608.21500)。学生对注入攻击输入生成，冻结初始化 teacher 对对应干净输入评分同一输出，得到 token 级防御信号。在 PISmith 自适应攻击中报告 ASR 9.0%，对比 Meta-SecAlign 的 94.0%，另测工具调用迁移；不能把该单项优势推广为所有攻击都同等改善。
- **CC-OPD（2902-MAIN）**：[原文](https://arxiv.org/abs/2609.27421)。teacher 依次去掉每条约束，以 leave-one-out token log-likelihood 差量化各约束贡献，再求和、截断并加到普通 OPD 奖励。两个模型配对、七个 benchmark 中平均表现最佳，1.5B 学生在 MulDimIF 超过自己的 7B RL teacher；蒸馏时不需外部 verifier。
- **OSPD（6649-MAIN）**：[原文](https://arxiv.org/abs/2609.34418)。teacher 看到完整角色设定，学生只看到简述；按角色关键 token 和普通话语的置信度结构切换散度，并逐步遮蔽角色特质。三个角色/社交 benchmark 报告优于 SFT 和多轮 RL，重点是角色知识内部化与监督目标适配。
- **MoralSteer（4612-MAIN）**：[原始 PDF 索引](https://openreview.net/pdf/755231b3dfbed482c2fb9c86108d48c77540b30a.pdf)。将 Moral Foundations Theory 推理链作为 teacher 特权，按角色道德复杂度调整 KL 混合、轨迹混合和课程，以减轻反派被改写成好人的问题。索引摘要报告角色保真度提升 5.8–9.9%，五个安全 benchmark 保持在基座 ±1 个百分点；仅核对摘要，未完成全文审计。
- **CaMOPD（6445-MAIN）**：[原文](https://arxiv.org/abs/2605.27115)。将通用能力恢复与领域能力保持拆为交替更新，用 teacher–student logprob gap 筛出更需要纠正的 proxy prompt。角色扮演和医疗 QA 中恢复通用能力同时保持领域行为，梯度分析支持减少相互抵消；不要求复原通用 teacher 的隐藏训练数据。
- **RoCo-ACE（5664-MAIN）**：[原文](https://arxiv.org/abs/2607.24771)。对同一学生 rollout，比较有/无参考资料上下文的 likelihood，将额外监督集中给有参考支持的 token；ACE 对 rollout 遗漏的权威事实增加稀疏 anchor correction。三种知识注入设置、六个保持 benchmark 中，作者报告注入准确率最佳且保持接近基座，兼顾选中事实和遗漏事实。
- **CODE（2677-FIND）**：[原文](https://arxiv.org/abs/2605.28303)。诊断孤立事实覆盖会和旧知识发生逻辑冲突，以因果叙事 bootstrapping 加非对称 OPSD 内部化知识变化。Llama/Qwen 实验报告自我否定率降低到 1.8%，多跳准确率最高 83.5%；贡献包含机制诊断、因果更新表示及训练配方。

## 6. 多模态、压缩与部署：5 篇

- **H-OPD（572-MAIN）**：[原文](https://arxiv.org/abs/2607.02592)。不为每个样本固定一个 teacher，而是按 token 的 confidence 混合视觉语言和纯文本 teacher，并通过视觉描述让文本 teacher 获得图像语义。11 个推理 benchmark 报告收益，关键是同一轨迹中视觉 grounding 和抽象推理需要不同 teacher。
- **ViCuR（866-MAIN）**：[原文](https://arxiv.org/abs/2606.05718)。将 teacher 的答案特权替换为输入中的视觉线索，并用 prefill 时 sink-token cross-attention 聚合可恢复的视觉证据。七个 benchmark 上，相对答案条件 OPSD，2B/8B 平均改善约 1.19/1.24；强调 teacher 信息应可由部署时输入恢复。
- **X³-OPD（5980-MAIN）**：[原文](https://arxiv.org/abs/2607.21550)。音频学生生成自己的推理，文本 teacher 看匹配文本和已验证答案提供 token 监督；构造语音化文本、音频事件和带副语言线索对话三个层次的数据。四个音频推理 benchmark 报告改善，并在域偏移下较好保持原能力；不是仅把文字题目转语音。
- **Draft-OPD（3258-MAIN）**：[原文](https://arxiv.org/abs/2605.29343)。针对 drafter 不能稳定独立生成的问题，先用 target-assisted rollout 得到稳定续写，再从 verification 暴露的错误位置重放 drafting，对接受和拒绝的 proposal 都学习。报告 thinking 模型最高超过 5 倍无损加速，相对 EAGLE-3/DFlash 加速改善 23%/13%；目标是提高 speculative acceptance。
- **Compact Rerankers（1866-FIND）**：[原文](https://arxiv.org/abs/2609.01947)。先以 off-policy GRPO 和 judge 反馈优化 4B teacher，再让 1B 学生采样排序并获得 teacher-derived soft reward。MAIR-11 nDCG@6 为 0.7670，比 offline listwise KD 高 4.6 点；控制比较表明收益不只是普通 on-policy GKD，而与学生排序空间中的 reward-based transfer 有关。

## 7. 待证据：4 篇

四篇均在官方日程中，但目前没有找到可核实的方法摘要或全文。以下仅标注标题提示的阅读位置，不写具体创新和结论，不把相似博客或别的论文当它们的证据。

| 官方 ID | 标题 | 暂定阅读位置 / 证据缺口 |
|---|---|---|
| 543-MAIN | Beyond Top-k: Mass-Aware Support Sampling for On-Policy Distillation | 候选支持集采样；作者主页亦列出录用，但没有论文链接。 |
| 1728-MAIN | Self-Supervised On-Policy Distillation for Omni-Modal Video Captioning | 多模态视频描述；未取得摘要/全文，不能用 AVSCap 等相似论文代替。 |
| 2835-MAIN | MosaicAudio: Multi-Teacher On-Policy Distillation for Controllable Video-to-Audio Generation | 视频到音频、多教师；未取得摘要/全文。 |
| 3171-FIND | CE-GAD: Curriculum-Efficient On-Policy Adversarial Distillation of Large Language Models | 课程/对抗蒸馏；未取得摘要/全文，无法确认具体目标和结果。 |

## 阅读取舍（解释，而非质量评级）

通用 OPD 方法优先看第 1–3 类；Agent/OPSD 优先看第 4 类及 PTA；第 5–6 类按研究问题选择。不要将 38 篇候选视为 38 个独立通用方法。尤其值得对读的三组是 PowerOPD/AOPD/TGPO（负信号与替代方向）、ADWIN/KAT（截短的不同依据）、Sequential/Long-Context Recipe（顺序与联合优化的不同实验条件）。
