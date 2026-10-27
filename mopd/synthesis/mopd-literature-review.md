# MOPD 文献综述与证据边界

更新：2026-10-15。当前交付为 **36 篇有正文的 ARIS paper pages：15 篇 seed、21 篇补搜**。[分组文献表与论文导航](../research-wiki/topics/multi-teacher-opd.md)；[gap状态](../research-wiki/gap_map.md)；[自动索引](../research-wiki/index.md)。没有生成 idea、实验或 proof claim 节点。

**当前问题主题**：[领域图景与范围筛选](mopd-gap-analysis.md)将原七项收敛为 G15–G18 四项：跨 teacher 学习收益兼容、多来源专长兼容组合、互补能力在单一 student 中的使用，以及新增 teacher 的边际价值。原1/6剔除，原2/3收窄合并，原4收窄，原5/7保留并限定边界。四项仅通过多 teacher 相关性筛选，尚未确认为高价值 gap；G1–G14及旧关系仅保留历史语义。本次未重新核查原文、检索或查新；下文来源与原文阅读说明属于先前建库记录。

## 跨论文综合

【事实与解释】MOPD 的基础操作是让多个 teachers 在 student 自采样的轨迹上提供蒸馏监督，但“多 teacher”包含不同拓扑：[MOPD](../research-wiki/papers/ma2026_mopd_multiteacher_onpolicy.md) 是独立领域 RL experts，[SMOPD](../research-wiki/papers/wang2026_smopd_multireward_reinforcement.md) 是同域 reward-priority specialists，[PromptSD](../research-wiki/papers/ma2026_one_student_many.md) 共享冻结 backbone、只区分 learned prefixes；[AVSD](../research-wiki/papers/nguyen2026_avsd_adaptiveview_selfdistillation.md) 区分 privileged views，[MT-SDPO](../research-wiki/papers/he2026_learn_from_whoever.md) 让外部 critiques 最终通过 privileged EMA self-teacher 产生 token target。这些工作可以互相启发，不能把其性能数字当作同一种能力整合问题的直接比较。

【事实与解释】正确 domain assignment 只是一个设计轴。[Open-MOPD](../research-wiki/papers/gao2026_openmopd_diagnosing_fixing.md) 调整 token budget 与 inner-update reward，[DN-MOPD](../research-wiki/papers/li2026_beyond_teacher_assignment.md) 校准 feedback dispersion，[D³-MOPD](../research-wiki/papers/sun2026_d³mopd_dynamic_domain.md) 调整 prompt sampling。这三者改变的统计对象不同。[TrustMOPD](../research-wiki/papers/sun2026_distill_what_you.md) 和 [MOPD-Router](../research-wiki/papers/xu2026_mopdrouter_rethinking_teacher.md) 再将 supervision allocation 移到 token 位置；[TGOPD](../research-wiki/papers/zhang2026_verify_before_you.md) 与 [VG-OPD](../research-wiki/papers/xu2026_who_teaches_which.md) 引入外部验证。Entropy、reference displacement、criterion gain 和答案正确率是不同 reliability proxies；现有结果没有给出跨 teacher family 与任务均成立的统一优胜规则。

【事实与解释】信号进入共享 student 后，还经过 loss averaging、词表支持、数值精度与 optimizer。[Gradients→Capabilities](../research-wiki/papers/zhu2026_from_gradients_capabilities.md) 表明 Adam momentum 能掩盖 teacher 差异、BF16 舍入能掩盖大量小参数变化；[tool-call drift](../research-wiki/papers/shen2026_when_topk_misses.md) 显示保留几乎全部 teacher mass 仍可能遗漏决策坐标。[PMOPD](../research-wiki/papers/liu2026_pmopd_task_ordering.md)、[Road](../research-wiki/papers/tian2026_beyond_domainrouted_supervision.md)、[UP](../research-wiki/papers/zhu2026_upmopd_update_projection.md) 分别保护历史更新子空间、同轨迹辅助 teacher 梯度、实际 optimizer displacement。这些保护对象不能混称为“解决梯度冲突”；局部可行性与长期 benchmark 保留仍有证据间隙。

【事实与解释】初始化、目标和 teacher 制备也影响整合。[IM-MOPD](../research-wiki/papers/kim2026_pain_more_gain.md) 在训练中注入 task vectors，[Δ-MOPD](../research-wiki/papers/sang2026_composing_what_each.md) 传递 teacher-minus-precursor 的 function-space shifts，[Latent-MOPD](../research-wiki/papers/fang2026_latentmopd_latent_multiteacher.md) 增加 hidden-state targets；它们分别需要兼容 weights、准确 precursor、可比 representations。[Beyond Best Teacher](../research-wiki/papers/lu2026_beyond_best_teacher.md) 主动构造互补 experts，但其各 task domain 分开实验，不证明同一个 student 的三域组合。[One Training Example](../research-wiki/papers/fu2026_rethinking_onpolicy_distillation.md) 与 [DF-OPD](../research-wiki/papers/li2026_datafree_onpolicy_distillation.md) 降低问题数量依赖，却保留反复 rollouts/scoring；“少数据”不能直接解释为“低训练成本”。

【事实与解释】方法判断需要强对照。[Rethinking Capability Merging](../research-wiki/papers/xie2026_rethinking_selfdistillation_multiteacher.md) 在独立调参和高质量 teacher corpus 下，SFT/Soft-KD 可匹配部分 ID recovery，但 OOD retention 有差别；[Fusion Paradigms](../research-wiki/papers/wu2026_consolidating_rlvr_capabilities.md) 中静态 merge、MixRL、standard MOPD 各有领域优势；[ACLArena](../research-wiki/papers/wang2026_aclarena_agent_continual.md) 在四阶段 Agent curriculum 中也未找到所有域一致改善的共享 checkpoint。这限制了“优于 vanilla MOPD 即证明新机制必要”的推断。它们同样没有证明任意规模、异源 teachers 或组合任务上离线蒸馏必然等价；[sequence-level theory](../research-wiki/papers/di2026_understanding_off_onpolicy.md) 则在更严格假设下区分 arithmetic/geometric objectives，不能当作现成大模型 recipe。

## 不能混用的指标

| 原文口径 | 需要保留的限定 |
|---|---|
| MOPD normalized headroom recovery | 以对应初始化和领域 teacher headroom 归一化，非绝对准确率 |
| Open-MOPD recovery | 指定 SFT→RouteRL gap；与 Trust 的 oracle pool、IM 的 domain recovery 不同 |
| D³-MOPD .97 vs .63 | 各 benchmark 分别取峰值；单 best-average checkpoint 为 .73 vs .48 |
| IM-MOPD recovery | 每域 reference=0、对应 teacher=1，再五域等权平均 |
| Latent-MOPD Norm=1.05 | base=0、per-benchmark best-teacher envelope=1，不是105%准确率 |
| Few-shot MOPD 101% | full-data student gain 的恢复比例，不是绝对分数，也未少训练步骤 |
| AVSD 摘要提升 | math子集与五任务Avg不同；wiki采用Table1全五项 |
| MT-SDPO Gap/Worst | Gap缩小可能伴随Macro下降；最弱域可以变化 |
| Avg@K / pass@K | 平均正确率与至少一次成功率不同，不能互换 |
| Video/system overall | 可混合IoU、judged scores或前置RL贡献，不能直接与文本accuracy横比 |

## 成本证据

以下数字是作者报告，不能横向排行；来源表号与精确设置见链接论文页。

| 工作 | 报告成本 | 边界 |
|---|---|---|
| UP-MOPD | late-window logged step约1.42× | 包含domain gradient replay；不是只计QP |
| TrustMOPD | 相对Uniform training/evaluation GPU cost +7.3% | Uniform本身已查询多teacher；不是相对单teacher +7.3% |
| TGOPD | 指定35B CodeIO step time +5.9% | teacher三次自回归probe仍有成本 |
| VG-OPD | 完整146.8 vs RL-only94.7s/step | +55%；稀疏mask不省完整teacher forward |
| AVSD | 指定4B update 1.13× | 多views teacher forward；非任意规模常数 |
| Δ-MOPD | 一项单teacher acquisition allocated GPU-h −34.7% | 每update反而+27.3%；exclude held-out eval，非所有MOPD设置 |
| Rethinking | online/SFT完整runs为14.8×/23.1× | exclude一次性teacher data generation及全部tuning成本 |
| Fusion Paradigms | 含teacher制备总成本1.14×/1.19× expert-training reference | fusion单独<.2×不等于全流程<.2× |

【范围边界】全流程成本包括teacher RL/SFT、问题生成、验证、calibration、validation selection、rollout、scoring与optimizer replay。缺完整计时本身只是evidence gap，不列为MOPD核心gap。当前仅保留新增teacher的非冗余、可迁移能力能否抵偿整合成本，以及是否优于强化已有teacher的问题；其高价值gap地位尚未成立。见[问题主题④ G18](mopd-gap-analysis.md#g18)。

## 检索与收录边界

本轮从 seed 的15个 canonical arXiv IDs 起步，以 `multi-teacher + on-policy + distillation`、`MOPD + routing/merging`、data-free、fair fusion 等别名补搜，再回到原论文方法/实验/限制。补搜21篇均在主题文献表中标为“补搜”。以 arXiv ID 去重，版本更新不另建论文页。

实际来源：版本化 arXiv HTML、abs 元数据、web discovery；扩展 [文献目录](https://github.com/gyanchow/awesome-multi-teacher-distillation) 仅提供候选入口，未作为正式页技术事实依据。arXiv search helper确实调用但API超时，随后用官方网页完成元数据核查。Open-MOPD因摘要与正文限定差异，另核对同版PDF局部；其余主读HTML。没有下载PDF或导入Zotero。

补查了 **Windows Zotero 9.0.6** 的本地只读API：通过WSL2镜像网络的localhost访问。当前本地user library的40条非attachment records中，与36篇wiki按arXiv ID/规范化标题匹配为0；一篇单teacher imitation-learning背景留在既有OPD范围。没有声称覆盖其他Zotero groups、云端未同步条目或PDF annotations。当前会话未暴露Zotero MCP不等于桌面API不可用；本轮已实际验证并修正此前判断。Obsidian未使用。

### 尚未建正式页的扩展入口

以下是扩展目录发现的代表性遗漏入口；未把二手目录描述升级为已核实结论，也未声称这是完整待读清单。

Planning、MAGA、Poly-OPD在先前工作中留有局部阅读记录，但未建完整paper pages。本轮不把旧gap段落内的结论用作依据；这些入口只标示覆盖边界，不据其判断问题已解决或尚无人研究。

| 候选入口 | 后续价值与当前边界 |
|---|---|
| [MiMo-V2-Flash](https://arxiv.org/abs/2601.02780) | 早期industrial MOPD formulation；本轮仅通过已读论文引用定位 |
| [Nemotron-Cascade 2](https://arxiv.org/abs/2603.19220) | staged RL/domain checkpoint consolidation；report待读 |
| [DeepSeek-V4](https://arxiv.org/abs/2606.19348) | frontier full-vocabulary consolidation；report待核查 |
| [Nemotron 3 Ultra](https://arxiv.org/abs/2606.15007) | 大teacher pool规模化成本；report待读 |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | reasoning-effort×domain teachers；report待读 |
| [One to More, More to One](https://arxiv.org/abs/2609.23377) | SWE experts构造与整合；垂直Agent方法待核查 |
| [Long-Horizon Planning](https://arxiv.org/abs/2607.24720) | 先前有§3/6局部阅读记录，未建完整页；本轮仅保留覆盖入口 |
| [Cross-Domain Hybrid OPD](https://arxiv.org/abs/2608.02101) | search/general recovery；待区分RL与distillation贡献 |
| [UI-MOPD](https://arxiv.org/abs/2607.04425)、[MAGA](https://arxiv.org/abs/2607.29320) | UI先前仅摘要；MAGA有局部阅读记录，未建完整页；本轮仅保留覆盖入口 |
| [Poly-OPD](https://arxiv.org/abs/2608.04349) | 异latent-space方向的局部阅读入口，未建完整页；不纳入本轮gap证据链 |
| [CollectionLoRA](https://arxiv.org/abs/2605.25378) | 多effect teacher pool；待读扩展性证据 |

传统离线multi-teacher KD、纯parameter merging、peer/self-play以及更远的protein/flow应用未批量入库。必要的离线/RL/merging对照已通过受控比较论文覆盖；这些领域仍可在具体任务需要时定点补读。**36篇是本轮范围内的有证据知识页，不是穷尽检索声明。**

## 验证范围

本轮gap综合仅检查本地来源、结构与链接；未重新核查原文。以下描述先前文献建库的验证范围。

正文由原文定向阅读完成；30篇分片结果经过各分片只读复核，修正了指标定义、理论假设范围和一处Trust对照描述。其余6篇由主协作者读取原文方法/主表后写入。结构、ID去重、seed覆盖、本地链接、版本化source anchors另做程序检查；这些检查不等价独立复现实验或正式citation audit。

`research-wiki/query_pack.md` 已由ARIS helper重建。当前helper的paper摘要按文件名顺序截断，不保证代表性排序；完整阅读应从主题文献表进入。graph为关系唯一来源；没有手写或改写受保护的Connections段，也未修改上游skills/helpers。
