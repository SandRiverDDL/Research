# Awesome-Agentic-OPD 文献调研

2026-10-14 · ARIS research-lit · 当前轮完整筛选

> 2026-10-15：当前研究gap已基于这24篇论文[重新生成](gap_map.md)。本文G1–G4保留调研时的分类含义；当前方法问题、证据边界与旧编号迁移以新gap map为准。

来源：[Awesome-Agentic-OPD 固定版本](https://github.com/Zenghuang-Fu/Awesome-Agentic-OPD/blob/8c232bdda042fab0378514d5710277fe5994fe68/README.md)。71条记录，按 arXiv ID 去重后70篇；DeepSearch-World跨两节出现，只计一次。全部70篇元数据已与原 arXiv API 核对。

**正式保留24篇：19篇方法／技术报告、1篇框架、4篇基础背景。排除46篇：40篇以自蒸馏／OPSD为主因，5篇以多模态或混合视觉范围为主因，1篇benchmark-only。排除原因可重叠，以上按主因互斥计数。本清单未发现单独的VLA条目。**

范围按用户指定仓库及排除条件执行，不扩展成全领域检索。单轮基础与综述仅作背景，不能作为多轮Agent机制的直接证据。CAST为solver教师边界类；Cross-Domain Hybrid OPD仅间接相关：OPD作用于通用responses，搜索轨迹本身仍用GRPO。

多模态按实际任务／视觉输入判断，不因Qwen3.5 backbone本身直接排除。Agents-A1含视觉评测、Orchard含GUI视觉分支，按本轮保守范围整篇不入正式清单；这不等于其文本分支没有参考价值。EasyOPD为通用实现框架，仅提取普通／step-wise OPD，排除其中OPSD实验分支。

阅读深度：19篇方法／报告与EasyOPD核查原HTML的摘要及相关方法／结果章节；TCOD、ReOPD复用已有更详细阅读。4篇背景仅读原摘要。其余排除项依据原题／摘要，HindSearch、StepOPSD、SGCD、UI-MOPD等易误判项补查正文。全部数字为作者报告，未复现、未做代码审计；这是一轮调研级综合，不是24篇全文精读。

来源覆盖：仓库用于确定对象，arXiv用于核实原题、作者、版本、摘要和正文；复用本地wiki与两篇已存PDF对应的阅读成果，本轮未新增PDF。补充arXiv主题搜索已执行，只用于观察仓库覆盖边界，不把清单外论文混入本轮统计。当前未提供Zotero／Obsidian连接工具，因此这两类未贡献来源，也未向Zotero导入。

引用年份为首次arXiv年份；会议信息仅在原arXiv comments明确自报接收／发表时列出并注明。其余写arXiv（会议状态未核验），不根据GitHub标签推断已同行评审。

## 方法与技术报告（19）

| 论文／作者、年份 | Venue | 方法 | 作者报告的结果 | 本项目定位 | 原文依据 |
| --- | --- | --- | --- | --- | --- |
| [TCOD](papers/wang2026_tcod_exploring_temporal.md)<br>Jiaqi Wang et al., 2026 | arXiv；会议状态未核验 | TCOD 用 F2B 增加 student 交互深度，或用 B2F 从成功 teacher prefix 逐渐移交给 student。 | Table 2：Qwen2.5-3B ALFWorld unseen SR，OPD 60.45→F2B 79.19。 | G1：多轮 rollout 越深，teacher supervision 与 student 优化越容易不稳定。 | [§§3–5、Table 2](https://arxiv.org/html/2604.24005v3) |
| [ReOPD](papers/liao2026_multiturn_onpolicy_distillation.md)<br>Baohao Liao et al., 2026 | arXiv；会议状态未核验 | ReOPD 重放 teacher actions/observations，只让 student 自采样当前 action，并按 step-decay 采样训练位置。 | Table 4：8B→4B 数学均值 51.0→53.7；Table 5 搜索均值 40.6→40.5，不是各项均提高。 | G1：重复在线执行多轮 student rollout 昂贵，teacher 对 student histories 的监督也未必可靠。 | [§§3–6、Tables 4–6](https://arxiv.org/html/2607.04763v3) |
| [FutureBridge-OPD](papers/chen2026_look_ahead_before.md)<br>Chishui Chen et al., 2026 | arXiv；会议状态未核验 | FutureBridge-OPD 恢复候选 turn 的环境，插入 teacher bridge，并比较两条 student continuation 的 teacher-preferred token ratio，仅接受改善该代理指标的 bridge。 | Table 1：1.7B student ALFWorld SR 40.4±3.4，OPD 21.5±3.0。 | G2：高 teacher–student disagreement 能定位介入机会，却不能保证 teacher action 有用。 | [§3.2、§4.1、Table 1、Appendix G](https://arxiv.org/html/2608.01953v2) |
| [SOD](papers/zhong2026_sod_stepwise_onpolicy.md)<br>Qiyong Zhong et al., 2026 | arXiv；会议状态未核验 | SOD 按 tool observations 之间的 response 划 step，依据 sampled-token log-prob gap 衰减高 divergence step 的蒸馏权重，并联合 GRPO；teacher 为独立训练的较大模型。 | §5主表：0.6B student AIME2025 average@32 为 26.13±1.07，OPD 22.95±0.97。 | G2：错误工具调用导致状态离散漂移，后续 dense OPD 可能不稳定。 | [§4、§5.1、§5.4及主结果表](https://arxiv.org/html/2605.07725v3) |
| [Guided-OPD](papers/li2026_onpolicy_distillation_curriculum.md)<br>Gengsheng Li et al., 2026 | arXiv；会议状态未核验 | Guided-OPD 按 turn 概率混合 teacher/student 执行，并逐渐将 teacher 介入概率降到零；student turns 用 reverse KL、teacher turns 用 forward KL。 | 摘要报告相对 vanilla OPD，平均 Score +21.1%、SR +25.5%；保留作者原指标口径。 | G1：错误累积后 teacher 在 student 访问状态上的监督可能失效。 | [Abstract、§3、§4.1](https://arxiv.org/html/2606.15912v2) |
| [SAGE-OPD](papers/zhou2026_sageopd_selective_agentguided.md)<br>Yuhang Zhou et al., 2026 | arXiv；会议状态未核验 | SAGE-OPD 基于 environment feedback、teacher 判断和 confidence，选择 Skip/Weak/Strong 监督强度并归一化 loss；这里 intervention 是监督选择，不是 teacher 接管。 | §4：8B→1.7B，ALFWorld unseen SR 从 OPD 61.94→70.15。 | G2：无差别 KL 可能惩罚有效替代动作，或强化重复行为及坏历史。 | [§3.1–3.3、§4主结果](https://arxiv.org/html/2606.19659v1) |
| [ATOD](papers/tan2026_atod_annealed_turnaware.md)<br>Qitai Tan et al., 2026 | arXiv；会议状态未核验 | ATOD 逐步降低 OPD、提高 GRPO 系数；T-DUR 结合 disagreement 与 student uncertainty，保留高分歧或高不确定 turn，衰减两者均低的 turn。 | Table 1：1.7B student 平均 SR 71.58，OPD 64.91。 | G2：OPD 前期学得快，但可能受 teacher ceiling 限制。 | [§4.2–4.3、§5.1、Table 1](https://arxiv.org/html/2606.27814v6) |
| [TurnOPD](papers/zhou2026_turnopd_making_onpolicy.md)<br>Yuhang Zhou et al., 2026 | arXiv；会议状态未核验 | TurnOPD 结合 probe-based adaptive rollout depth 与渐进 turn-normalized KL weighting，分配环境交互和蒸馏预算。 | Table 2：ALFWorld-1.7B 的 100步时间 4.42h→1.93h，同步数 accuracy 83.00→86.29。 | G4：长 rollout 尾部可能消耗预算，token objective 也可能过度偏向浅层 turn。 | [§6、Table 2](https://arxiv.org/html/2607.05804v2) |
| [CAST](papers/wang2026_cast_game_solvers.md)<br>Yu Wang et al., 2026 | arXiv；会议状态未核验 | CAST 用独立游戏 solver 的 state/action value 构造 turn advantage，经 asinh/RMS 变换后用于 DAPO/RLVR；在特定假设下联系 OPD，并非直接匹配 LM logits。 | Table 1：三游戏平均 ID/Unseen SR 62.1/28.4，DAPO 44.7/18.7。 | solver teacher 边界类 | [§3.1–3.2、Table 1、Appendix C.5](https://arxiv.org/html/2607.25308v1) |
| [DASH-OPD](papers/xia2026_dashopd_discrepancyaware_switching.md)<br>Yuchen Xia et al., 2026 | arXiv；会议状态未核验 | DASH-OPD 在 action tokens 上累计方向性 teacher/student likelihood-ratio evidence，以不同阈值及 hysteresis 双向切换；student/teacher turns 分别用 reverse/forward KL。 | Table 1／§5.2：4B ScienceWorld SR 22.40%，最佳对比方法 20.34%。 | G1：介入调度不仅要决定多少，还要决定何时接管、何时归还。 | [§5.1–5.2、Table 1](https://arxiv.org/html/2607.29078v4) |
| [MemOPD](papers/liu2026_memopd_onpolicy_distillation.md)<br>Zhiyuan Liu et al., 2026 | arXiv；会议状态未核验 | MemOPD 记录并重构真实 invocation，保持 action mask、position 与 causal visibility，联合 full-vocabulary reverse KL 和 PPO；3B student 与独立 frozen 7B teacher。 | §4.5／Fig.3a matched control：恢复 teacher state 比 persistent-history scoring 再提高 F1 7.0%（相对）。 | G3：memory rewriting 后 flatten history 会改变评分时的位置和可见性，使 teacher 看到的状态偏离 rollout state。 | [§3.3–3.4、§4.1、§4.5／Fig.3a](https://arxiv.org/html/2608.07068v1) |
| [KAT-Coder-V2](papers/li2026_katcoderv2_technical_report.md)<br>Fengxiang Li et al., 2026 | arXiv；会议状态未核验 | KAT-Coder-V2 将分别 SFT/RL 的五个领域专家按任务路由到 student rollout，返回 sampled-token log-prob，联合优化 RL 和 OPD。 | §4.1／Table 2：SWE-bench Verified 79.6；这是完整模型配方结果，未隔离 OPD 效果。 | G3：多领域能力冲突以及离线专家轨迹的 exposure bias。 | [§3.4、§4.1–4.2、Table 2](https://arxiv.org/html/2603.27703v1) |
| [MAD-OPD](papers/wang2026_madopd_breaking_ceiling.md)<br>Jianze Wang et al., 2026 | arXiv；会议状态未核验 | MAD-OPD 在 student-visited state 上让多个独立 teacher debate，并按自报 confidence 加权监督；agent 场景用 JSD，code 用 reverse KL。 | Table 1：14B＋8B→4B，agent average 从单 teacher OPD 23.26→25.69。 | G3：单 teacher 错误限制 student，多步环境交互进一步放大错误。 | [§4、§5.1–5.2、Table 1、§6](https://arxiv.org/html/2605.01347v1) |
| [KAT-Coder-V2.5](papers/huang2026_katcoderv25_technical_report.md)<br>Bo Huang et al., 2026 | arXiv；会议状态未核验 | KAT-Coder-V2.5 先做 expert-trajectory cold start，再按领域路由 reverse-KL OPD；依据 teacher/student top-k overlap 降权或屏蔽漂移后缀，使用 length-stratified batching。 | §6.2／Table 4：PinchBench Avg 94.9；未隔离 cold start、truncation 与 MOPD 的贡献。 | G3：长 student 前缀漂移后，领域 teacher 的监督可能失准。 | [§5–5.1、§6.2、Table 4](https://arxiv.org/html/2607.05471v1) |
| [Top-K Drift](papers/shen2026_when_topk_misses.md)<br>Jiabin Shen et al., 2026 | arXiv；会议状态未核验 | Top-K Drift 用 frozen full-vocabulary audit、entry-coordinate restoration 和对照诊断 tool-call drift，比较 support union、loss shaping 与 decoding bias。teacher 为分别 SFT 的独立专家。 | 摘要及正文：三 seed 全位置 restoration，over-calling 14.2±2.1%→3.7±0.5%，同时 call recall 损失12.4点。 | G3：top-k 保留概率质量很高，也可能漏掉工具调用的决策关键 token。 | [§2、§5、§6、Appendix A.3](https://arxiv.org/html/2607.07050v6) |
| [MOPD / HMPO](papers/team2026_machmind4flash_technical_report.md)<br>Foundation Model Team, 2026 | arXiv；会议状态未核验 | Mach-Mind-4-Flash 用十余冻结 RL specialists 按 domain routing 监督 student rollout，使用 sampled reverse-KL log-ratio 与 clipped policy-gradient surrogate；另有 HMPO reasoning 压缩。 | Appendix C／Table 4：加入 code teacher 后 LCB-V6 78.63→82.44，BFCL 76.30→76.39。 | G3：mixed-reward RL 存在跨领域能力的 see-saw。 | [§4.8、§5.1、§6、Appendices B–C](https://arxiv.org/html/2607.09375v1) |
| [MOPD](papers/men2026_physics_multiturn_longhorizon.md)<br>Tianyi Men et al., 2026 | arXiv；会议状态未核验 | 在受控文本 crafting 环境改变预训练轨迹质量和 planning templates，对比 OPD/GRPO；顺序蒸馏三个独立域专家，检验 shared/conflicting patterns。 | Table 6／§6.2：4 Opt.:4 Sub.(a) 中，只蒸馏 FA teacher，未见 LF 中等难度 avg@8 34.92→52.58。 | G3：planning pattern、procedural knowledge 与多教师兼容性对长程学习的作用未分清。 | [§5.2、§6.2–6.3、Table 6](https://arxiv.org/html/2607.24720v1) |
| [Yuanbao Search Agent](papers/chen2026_crossdomain_hybrid_opd.md)<br>Hongzhan Chen et al., 2026 | arXiv；会议状态未核验 | Cross-Domain Hybrid OPD 将搜索 GRPO 与数学／代码／逻辑／科学专家 OPD 混合；专家先用中等难度 curriculum，再扩展全难度。 | Table 2：GPQA 73.23→Stage I 69.95→Stage II 76.64；FS-O 55.00→50.00 是反例。 | 间接相关：OPD 作用于通用 responses，搜索轨迹仍用 GRPO | [§4.3、Algorithm 1、Table 2、§7](https://arxiv.org/html/2608.02101v1) |
| [DGPO](papers/kotoge2025_can_compact_language.md)<br>Rikuto Kotoge et al., 2025 | ACL 2026 Main（arXiv comments 自报） | DGPO 先从独立 teacher 的正确轨迹做 cold-start KD；RL 阶段仅对错误预测加入 teacher KL guidance，保留成功 student 的探索。 | Table 2：Qwen2.5 3B→0.5B，七 QA 均值 DGPO .329，PPO .238，teacher .353；仅部分数据集超过 teacher。 | G2：0.5–1B compact search agent 初始表现弱，RL 奖励稀疏、训练不稳。 | [§4、Table 2、Limitations](https://arxiv.org/html/2508.20324v4) |

## 文本OPD实现框架（1）

| 论文／作者、年份 | Venue | 方法 | 作者报告的结果 | 本项目定位 | 原文依据 |
| --- | --- | --- | --- | --- | --- |
| [EasyOPD](papers/sun2026_easyopd_easytouse_onpolicy.md)<br>Jie Sun et al., 2026 | arXiv；会议状态未核验 | EasyOPD 在 verl 上分开用户配置、方法监督逻辑与分布式执行，为 loss、rollout metadata、reward、tokenizer alignment 和 teacher computation 提供扩展边界。 | Table 4：1.7B student／独立4B teacher 的 step-wise 示例，OPD平均34.81、SOD39.95；这是框架内的具体配置结果。 | 仅提取普通／step-wise OPD 接口，不纳入 OPSD 分支 | [§3、§4.1、Table 4](https://arxiv.org/html/2607.11012v1) |

## 基础背景（4；非多轮直接证据）

| 论文／作者、年份 | Venue | 方法 | 作者报告的结果 | 本项目定位 | 原文依据 |
| --- | --- | --- | --- | --- | --- |
| [GKD](papers/agarwal2023_onpolicy_distillation_language.md)<br>Rishabh Agarwal et al., 2023 | ICLR 2024（arXiv comments 自报） | GKD 在 student 自生成序列上查询 teacher，并允许选择不同 divergence 或与 RL 结合。 | 摘要报告在摘要、翻译、推理和 instruction tuning 上有效；本轮未核对正文数值。 | 仅背景；单轮自回归生成基础工作，不能直接证明多轮环境状态覆盖或纠错能力。 | [Abstract](https://arxiv.org/html/2306.13649v3) |
| [MiniLLM](papers/gu2023_minillm_onpolicy_distillation.md)<br>Yuxian Gu et al., 2023 | ICLR 2024（arXiv comments 自报） | MiniLLM 使用 reverse KL 与 on-policy 优化，将较大白盒 teacher 的分布迁移给小 student。 | 摘要报告覆盖 120M–13B 模型，改善 instruction following、calibration 和长文本生成；未核对正文效果量。 | 仅背景；单轮语言生成基础，不提供多轮工具状态上的 teacher 可靠性证据。 | [Abstract](https://arxiv.org/html/2306.08543v6) |
| [SKD](papers/xu2024_speculative_knowledge_distillation.md)<br>Wenda Xu et al., 2024 | ICLR 2025（arXiv comments 自报） | SKD 让 student 提议 token，teacher 按自身排序替换质量较差的 token，交错生成训练序列。 | 摘要报告在翻译、摘要、数学与指令任务上优于对比 KD 方法；本轮未核对正文数值。 | 仅背景；token 层交错采样不等于多轮环境的 teacher 接管；不能直接外推 agent 收益。 | [Abstract](https://arxiv.org/html/2410.11325v3) |
| [Survey](papers/song2026_survey_onpolicy_distillation.md)<br>Mingyang Song et al., 2026 | arXiv；会议状态未核验 | Survey 按 objective functions、signal sources、training dynamics 梳理 OPD、失败模式及与 KL-constrained RL 的联系。 | 提供分类与开放问题，不是提出新算法的实验效果证据；本轮仅读原摘要。 | 仅背景；综述只作导航；其中 OPSD 与其他排除分支不计入本轮方法清单。 | [Abstract](https://arxiv.org/html/2604.00626v4) |

## 跨论文综合：事实、解释与缺口

【事实】现有保留项并不共享同一个“on-policy”范围。TCOD、Guided-OPD和DASH-OPD改变执行前缀或teacher接管；ReOPD固定teacher histories，仅在当前action内student自采样；TurnOPD同时改变交互深度和turn权重；SAGE-OPD的intervention是监督强度选择。**【解释】比较时需分别记录谁生成环境状态、谁执行action、teacher对哪个context评分。** 这些差异对应[G1](gap_map.md#g1)，不能仅凭OPD名称把它们视为同一训练分布。[TCOD §3](https://arxiv.org/html/2604.24005v3#S3)、[ReOPD §4](https://arxiv.org/html/2607.04763v3#S4)、[SAGE-OPD §3](https://arxiv.org/html/2606.19659v1#S3)。

【事实】SOD对高divergence step降权，ATOD的T-DUR则保留高disagreement或student uncertainty的turn，FutureBridge再用student continuation核验候选bridge。**【解释】分歧既可能是teacher在坏状态失准，也可能是student尚未学会关键行为；这些论文的模型、目标和任务不同，方向不同尚不构成可直接判定的实验矛盾。** 【开放问题】在共同错误状态和预算下，怎样区分上述两类情况？FutureBridge的验证仍是teacher-relative proxy，尚非独立环境正确性的保证。[SOD §4](https://arxiv.org/html/2605.07725v3#S4)、[ATOD §4](https://arxiv.org/html/2606.27814v6#S4)、[FutureBridge §3](https://arxiv.org/html/2608.01953v2#S3)。见[G2](gap_map.md#g2)。

【事实】MemOPD定位invocation重建后的位置／可见性失配；Top-K Drift定位teacher support漏掉决策token，且修复over-calling会牺牲call recall。多教师工作还包括debate、domain routing和顺序专家蒸馏，完整技术报告常混合多种训练阶段。**【解释】teacher能力、teacher评分接口正确性、teacher组合兼容性需分别审查；技术报告的最终模型分数不能自动归因于OPD。** 【开放问题】在state-aligned/full-vocabulary控制下，组合收益与跨域损失各剩多少？[MemOPD §3–4](https://arxiv.org/html/2608.07068v1#S3)、[Top-K Drift §5–6](https://arxiv.org/html/2607.07050v6#S5)、[KAT-Coder-V2 §3.4](https://arxiv.org/html/2603.27703v1#S3.SS4)。见[G3](gap_map.md#g3)。

【事实】ReOPD节省student环境调用，TurnOPD缩短rollout；MAD-OPD增加多teacher debate，FutureBridge增加continuation；DGPO有cold-start阶段。跨论文均值、任务、模型、teacher预算和seed口径不同。**【解释】本轮不能排出可信的跨论文性能总榜，也不能将最后几个checkpoints的波动当作训练seed方差。** 【开放问题】统一核算teacher训练／采集／评分、环境调用、额外continuation及端到端时间后，方法排序是否稳定？EasyOPD能减少实现差异，但共享backend本身不保证公平评测。[ReOPD §5](https://arxiv.org/html/2607.04763v3#S5)、[TurnOPD §6](https://arxiv.org/html/2607.05804v2#S6)、[EasyOPD §3–4](https://arxiv.org/html/2607.11012v1#S3)。见[G4](gap_map.md#g4)。

## 完整排除记录（46）

以下每项均链接原论文。40项自蒸馏、5项多模态／混合视觉范围、1项benchmark按主因计数；某些条目同时命中多类。排除理由是本轮scope判断，不是对论文质量的评价。

| 清单条目 | 原文／判定依据 |
| --- | --- |
| [OPSD](https://arxiv.org/abs/2601.18734) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [HindSearch](https://arxiv.org/abs/2608.01597) | 自蒸馏：外部judge生成critique，但KL teacher为student的frozen initialization＋privileged critique；§3.3–4。 |
| [Group Relative Self-Distillation](https://arxiv.org/abs/2603.24533) | 自蒸馏，并涉及视觉GUI；原摘要明确Group Relative Self-Distillation。 |
| [StepOPSD](https://arxiv.org/abs/2605.27140) | OPSD：真实标题含Self-Distillation；§2.3–2.4使用自身旧policy的privileged prefix。 |
| [TurnSight](https://arxiv.org/abs/2608.04007) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [AgentOPSD](https://arxiv.org/abs/2608.05987) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [π-Distill / OPSD](https://arxiv.org/abs/2602.04942) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [Skill-SD](https://arxiv.org/abs/2604.10674) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [π-Play](https://arxiv.org/abs/2604.14054) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [SDAR](https://arxiv.org/abs/2605.15155) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [HINT-SD](https://arxiv.org/abs/2605.17873) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [SD-Search](https://arxiv.org/abs/2605.18299) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [CCOPD](https://arxiv.org/abs/2605.30251) | 自蒸馏：原摘要明确same base model分别作FULL teacher与sharded student。 |
| [PBSD](https://arxiv.org/abs/2606.09348) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [HERO](https://arxiv.org/abs/2606.11559) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [UCOB](https://arxiv.org/abs/2606.29502) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [KbSD](https://arxiv.org/abs/2606.29863) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [OVCSD](https://arxiv.org/abs/2607.27937) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [CRPO](https://arxiv.org/abs/2607.28026) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [GRSD](https://arxiv.org/abs/2607.28076) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [TransMem](https://arxiv.org/abs/2607.29032) | 自蒸馏：原摘要明确evidence-only teacher与student共享frozen backbone。 |
| [EviSD](https://arxiv.org/abs/2608.01359) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [PCSD](https://arxiv.org/abs/2608.01837) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [ADRS](https://arxiv.org/abs/2608.03223) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [OCSD](https://arxiv.org/abs/2608.04788) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [PI Bias Score](https://arxiv.org/abs/2608.04794) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [SMRC-SD](https://arxiv.org/abs/2608.05219) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [GEAR](https://arxiv.org/abs/2605.11853) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [SGCD](https://arxiv.org/abs/2606.12634) | 自教师credit weighting：§1、§4使用同policy在credit-reference context重评分；外部LLM只总结reference，没有独立teacher-matching actor loss。 |
| [CRAFT](https://arxiv.org/abs/2606.29476) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [MAGA](https://arxiv.org/abs/2607.29320) | 多模态GUI：§3.1输入包含当前visual observation。 |
| [Agents-A1](https://arxiv.org/abs/2606.30616) | 混合视觉范围：报告含HiPhO视觉评测；本轮保守整篇不入库，文本jidomain-routed OPD仍有参考价值。 |
| [UI-MOPD](https://arxiv.org/abs/2607.04425) | 多模态GUI：Qwen-VL、截图／grounding；最新v2标题是Unified GUI Agents。 |
| [OPD-Evolver](https://arxiv.org/abs/2606.17628) | 自蒸馏：摘要与§3明确同policy的privileged hindsight slow loop。 |
| [OPID](https://arxiv.org/abs/2606.26790) | 自蒸馏：原摘要明确old policy在普通／skill-augmented contexts重评分。 |
| [DeepSearch-World](https://arxiv.org/abs/2607.07820) | 自蒸馏，且包含环境：原摘要明确DeepSearch-Evolve self-distillation，跨两节重复只计一次。 |
| [SEED](https://arxiv.org/abs/2607.14777) | 自蒸馏，并含视觉任务：current policy既分析skills又在skill context重评分。 |
| [CoARS](https://arxiv.org/abs/2604.10029) | 自蒸馏：原题／摘要为self-distilled recommender agents。 |
| [HyperEyes](https://arxiv.org/abs/2605.07177) | 多模态搜索：原题与摘要明确multimodal search及grounded queries。 |
| [Asymmetric-View Policy Optimization](https://arxiv.org/abs/2605.22240) | OPSD：原摘要明确privileged view of the same policy。 |
| [Search-E1](https://arxiv.org/abs/2605.22511) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [SA-OPSD](https://arxiv.org/abs/2607.17136) | 多模态自蒸馏：原摘要明确multimodal segment-aggregated OPSD；主因计自蒸馏。 |
| [FA-SD](https://arxiv.org/abs/2607.17558) | 自蒸馏／OPSD：原题或原摘要研究privileged self-teacher、hindsight/skill-conditioned自身监督。 |
| [TT-OPD](https://arxiv.org/abs/2605.02943) | 自蒸馏＋环境：原摘要明确gradient-free EMA teacher使用outcome privilege；主因计自蒸馏。 |
| [Orchard](https://arxiv.org/abs/2605.15040) | 混合视觉范围：框架含Orchard-GUI视觉分支；本轮保守整篇不入库，SWE文本OPD为可另行提取的参考。 |
| [QVal](https://arxiv.org/abs/2606.32034) | benchmark-only：原摘要为training-free dense-supervision testbed，不是训练新policy的OPD方法。 |

## 版本与证据边界

- 原arXiv题目修正：StepOPSD清单漏掉Self；UI-MOPD v2题目由Continual GUI Agent Learning改为Unified GUI Agents。正式metadata以原论文为准。
- 正式保留项使用核查时最新HTML版本，版本号记录在每个原文链接中；尤其ATOD v6、Top-K Drift v6、DASH-OPD v4、TurnOPD v2，不沿用旧版本的默认结论。
- 原摘要开头仅保留简短摘录，完整摘要链接arXiv。背景4篇仅读摘要，不伪装成全文阅读。
- Wiki的index列出全部24篇；query pack是有固定截断预算的压缩入口，当前helper按文件名取至多12篇后再裁到1800字符，并非相关性排名，也不保证覆盖全部论文。后续综合需读本报告和index。Connections仍以graph中的关系为准。
- 当前没有ideas、experiments或独立验证的claims；此次工作不触发idea生成、方法细化或实验。
