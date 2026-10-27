# OPD 当前状态

## Semi-OPD 定位、局限可解性与作者核查（2026-10-23）

- 用户进一步质疑：Semi 相对 Lightning 是否主要经验／机制贡献，限制能否真正转化为可解决的方法 gap，并询问作者／机构与研究背景。继续聊天交付，不调用 ARIS、不跑实验。
- 原文 §2.2 明示 Semi 基本移除 Lightning 前置 teacher-SFT；核心离线缓存与当前 student log-prob 更新相近，不把它说成独立新更新机制。§5/PDF p.8 明确弱初始轨迹导致 Semi 退化、适合较好 instruct 初始化；在线 rollout equilibrium 是作者开放问题。top-64 overlap 是跨17组的相关指标，不当作充分因果准则。冻结数据无法无条件提供新前缀 teacher 分数属于助手的信息约束推断；动态刷新／SFT 方向已有 Relay／Lightning，不能自动当 novelty。
- PDF首页核实：Siyan Zhao 与 Yonggan Fu 共同一作；NVIDIA 主导、UCLA 合作，Siyan 在 NVIDIA 实习完成。Siyan 主页列 UCLA 高年级博士；ICML 2026 官方 OPSD 论文第一作者，官方入口 `https://proceedings.mlr.press/v306/zhao26be.html`。Yonggan 主页为 NVIDIA Research Senior Research Scientist，领导 Hymba 等项目；Aditya Grover 为 UCLA 导师；Pavlo Molchanov 的 NVIDIA 官方作者页为 Distinguished Research Scientist／DLER 负责人。声誉评价依据公开履历，不编造引用量或把身份当论文结论背书。

## 本月性能方法的直接对照与历史比较定位（2026-10-22）

- 用户要求：确认过去一个月哪些工作是性能提升算法、通常对比哪些同期方法，举直接比较实例并解释优劣，同时找回以前类似总结。
- 优先检索本地比较材料，再核对原始实验表的 baseline／数字／预算；区分同表直接比较与跨论文结果，不按不同设定的增益排统一榜。沿用不调用 ARIS、不运行实验、不自动抽卡／导入 Zotero，聊天交付，不新增分类体系。已定位旧材料：`synthesis/reading/opd-method-map.md`／`opd-method-catalog.md`（2026-09-28，77 卡机制地图／索引）、`emnlp-2026-opd-overview.md`（10-05 摘要级候选总结）以及 `synthesis/archive/2026-06-lineage/` 的旧谱系；不是统一性能榜。
- 本轮核查 14 篇原始 HTML 的 baseline 与实验表；证据为 `tmp/arxiv-opd-20261022/comparison-evidence.json`。DIAL／Branch 的 HTML 表格未结构化提取，baseline 依据原文实验段落，不编造表值。
- 可直接报告的同表例子：IPD 0.6B 数学 Avg@32 38.47 vs Relay 36.96 vs Vanilla OPD 27.83；Semi-OPD 4B 低 overlap 57.4 vs FastOPD 52.5 vs Vanilla 44.9，高 overlap例子 Semi／OPD 均74.1、Fast74.8；ActionOPD Tau test pass¹ 40.0 vs OPD39.6，但 pass⁴14.2 vs17.5（四次全成功，非 pass@4）；JOLT Terminal-Bench2.1 pass@1 6.56 < GRPO8.25，JOLT+10.96，单训练run；R2S ALFWorld 2B77.9 vs Guided63.6，主表误差来自重复decode，不是多训练seed。
- R2S／STI 常见对手为 TCOD、Guided、FutureBridge，但主表不足以排序 R2S／STI／Graph／Action。Nash 主对照 Fixed、D³-MOPD，不据此宣称胜过 PMOPD／UP-MOPD。未独立复现、未审计全部预算；不把不同论文的最大提升跨设置排序。当前无 say，无法语音通知。

## OPD→RL 收益来源的有依据实验设计（2026-10-22）

- 用户要求判断 teacher alignment 与 retained uncertainty 的收益能否区分；建议实验必须有已核实顶会类似实验或明确方法学依据，不能把助手自拟设计称为社区共识。
- 聊天提供有来源的最小实验方案，区分预测、干预与因果归因；不调用 ARIS、不运行训练。上一条“同熵比较 alignment／同 alignment 比较熵”仅是概念设计，需核查两者是否真能独立控制，以及 temperature／训练改动带来的混杂。已核实可用先例：Born Again Neural Networks（ICML 2018，§3.2／PDF p.5 的 DKPP 保留 argmax、置换非 argmax 概率）；Beyond the 80/20 Rule（NeurIPS 2025，解码温度干预）；Understanding the Impact of Entropy on Policy Optimization（ICML 2019，§3.1 的可精确计算梯度环境，区分采样与优化）；统计依据 Agarwal et al.（NeurIPS 2021）。
- 建议由三个互补实验组成：teacher 非 argmax 语义信息的保熵破坏；同 checkpoint 的采样熵干预／救援测试；小型可枚举环境的 sampled vs exact-gradient 对照。OPD→RL 组合方案是基于先例的迁移设计，不是已发表的同任务结论或社区统一协议。
- 因果边界：teacher target 熵保持不等于学生熵保持；temperature 改变行为分布与 teacher alignment，不能称纯 entropy 干预；同均值熵不等于同有效策略覆盖；实际 sampler 概率需与 RL 更新一致；真实 LLM 上不承诺可唯一分摊收益比例。共同 prefix 上测量 JS／熵，使用实际训练种子的不确定性。
- 证据摘录：`tmp/opd-rl-attribution/source-excerpts.json`、`entropy-intervention-excerpts.json`；`permutation-check.json` 数学验证置换保持 entropy／argmax 且改变 JS。未运行训练或把实验建议当成结果。当前无 say，无法语音通知。

## Horizon／监督区域控制论文的录用状态（2026-10-22）

- 用户要求核实前述 14 篇方法的顶会录用；只查询公开出版／录用证据，区分主会、Findings、workshop 与未确认，不把搜索无命中当拒稿。
- 已确认两篇：TCOD 对应 COLM 2026 Conference，官方 pre-proceedings：`https://proceedings.colm.cc/paper_files/paper/2026/hash/c3af3531df85264decc31382cb319781-Abstract-Conference.html`（标题省略 TCOD 前缀，作者吻合）；Prefix/FastOPD 为 Findings of ACL 2026，`https://aclanthology.org/2026.findings-acl.1276/`，不是 ACL main。
- 其余 12 篇（Prune、Flash、Suffix Fade、ESR、ADWIN、POPD/TOPD、KAT、TurnOPD、ShortOPD、Adaptive FastOPD、STRIDE、STOPD）本轮未找到公开录用证据。已检索标题／别名、官方域名并检查 14 篇 arXiv 最新 metadata；未确认不等于被拒，不能由预印本方法数量推出顶会已经认可这些方法。未核实 ICLR／ICML／NeurIPS 主会录用。

## 截断、监督区域控制与 RL 干预迁移（2026-10-22）

- 用户新增筛选约束：认为 teacher 接管、生成中动态截断带来高 infra 改造与运行开销；后续选题需优先复用完整 rollout 后已有数据、修改 loss／样本选择／下一批预算。不能把概念简单等同实现轻量；此前推荐的生成中查询暂停与接管方向应降级。
- 成本原文核查：Flash 附录 C.3 明确 vLLM 在验证循环保持活跃、预留验证显存、复用评分，E.1 报告额外验证开销仍被长度缩短抵消；DASH §5.2 的 efficiency 主要是部署交互轮数，不能当训练提速；STI §4.4 声明比标准 OPD 增加训练时间。以上是论文实现／计时口径核查，未审计代码或复现实测。
- 用户追问 Prune-OPD／Flash-OPD／Suffix Fade 的分类、同类工作、具体操作及可迁移的 RL 干预；继续禁止 ARIS，聊天交付，不运行实验、不新增卡片或 taxonomy。
- 原文方法核查纠正：Prune-OPD v3 §3 用累计低 overlap 事件衰减奖励，并按 batch hit ratio 调整下一步共享长度上限；不是逐样本即时停止。Flash-OPD §4.2 缓存生成与验证交替、逐轨迹停止，实际验证点可越过首次越界点。Suffix Fade §3 是 BIC 变点后 loss mask＋保留前缀权重归一化，不等同停止 rollout。
- 定向清单核实 14 篇：Prefix/FastOPD 2602.15260、TCOD 2604.24005、Prune 2605.07804、Suffix Fade 2605.13643、ESR 2605.27028、ADWIN 2605.28396、POPD/TOPD 2605.31490、KAT 2606.09471、TurnOPD 2607.05804、ShortOPD 2607.13124、Adaptive FastOPD 2607.29494、STRIDE 2609.14636、Flash 2610.06105、STOPD 2610.21337。清单有边界，不宣称领域穷尽；三篇核心读方法，其余按原始摘要及部分方法核对。
- RL 迁移近邻：STRIDE 已有 stop/restart；STI 2610.10878、DASH 2607.29078 已有 teacher 干预／双向切换；BranchOPD 2610.13481 已有分叉；FTB 2608.01953 已用 student continuation 检验 teacher bridge；SOD v3 §5.3 明确讨论非单调恢复；IG-calibrated OPD 2610.20664 已用检索后信息效用校正监督。不能把这些基本操作本身当新颖贡献。
- 候选仅为待验证推断：分离 teacher 查询与环境继续、以学生恢复收益控制干预、截断下未来反馈的目标完整性；HER 式子目标重标注是更高风险备选。已核对 Recovery RL、SafeDAgger、Backplay、Time Limits in RL、HER 原始来源；未完成候选 claim-level 查新或实验验证。

## 最近一个月 OPD 论文的 limitation 与 gap 核查（2026-10-22）

- 用户要求基于上一轮 30 篇论文寻找 research gaps，重点核查作者 limitation／future work。沿用不调用 ARIS、不运行实验、不自动抽卡／导入 Zotero，聊天交付。
- 先定位原论文明确限制、讨论与未来工作，再区分作者明示问题和跨论文推断；优先 agentic OPD，保留通用机制问题。对已被其他论文覆盖的简单方向降级；候选 gap 不冒称完成查新或已验证方法。已回查 30/30 原始 HTML 中的 limitation／discussion／future-work／conclusion，摘录保存在 `tmp/arxiv-opd-20261022/limitation-excerpts.json`；未声称 30 篇全文精读。补核 9 篇近邻原始摘要，见同目录 `gap-neighbor-evidence.json`。
- 优先保留为待验证 gap：Projected Distillation 的多轮可执行最小修正；ActionOPD 固定查询预算下的稀疏语义匹配；Vanishing Learning Signals 的实际 AdamW 更新与表示限制区分。其他明确开放问题包括 R2S 不可回放环境适用性、OPD→RL 的 alignment／uncertainty 因果分离、Nash-MOPD 跨领域耦合预算分配。
- 需降级的泛化提案：PI 自动选择已有 Predicting PI Effectiveness／RSD，普通多教师冲突已有 PMOPD／UP-MOPD，teacher 接续与结果筛选已有 R2S／OG-OPD／SERO，不能直接当作新颖贡献。IPD 原型两项限制在同篇后续章节已处理，不视为未解决 gap。搜索遇到 2608.04408 原站标为 withdrawn／false information，不作为有效证据。
- 原文摘录已检查 30 篇唯一来源与可读取性；候选仅定向近邻核查，未完成 claim-level 查新、实验或可投性验证。当前无 say，无法语音通知。

## 最近一个月 arXiv OPD 分类总结（2026-10-22）

- 用户要求重新总结过去一个月 arXiv 发布的 OPD 相关论文，重点分类、降低阅读负担。按首次提交时间 2026-09-22 至 2026-10-22 检索；直接 OPD、OPSD、agentic 与机制分析分清，采用少量机制主类和代表作，不把旧论文更新当新发表。
- 本轮聊天交付；不调用 ARIS，不抽卡、不导入 Zotero、不运行实验，不改既有 taxonomy。已完成 arXiv API 首次提交日期过滤与关键词检索（318 条宽召回命中，非正式相关论文数），选择 30 篇代表作按 8 条主要贡献线索聊天总结；原始摘要、首次提交时间与链接保存在 `tmp/arxiv-opd-20261022/shortlist-evidence.json`。30/30 去重与日期检查通过。以摘要级综合为主，R2S／ASTEROID 另打开原始 HTML；不声称全量精读、穷尽检索或独立复现实验。

## OPD 方法迁移到 agentic 场景的选题筛查（2026-10-19）

- 用户明确禁止使用 ARIS skills；要求从已有 OPD 方法出发，寻找 agentic 场景使其前提失效／缺陷暴露／failure mode 改变后，可用聚焦改进形成顶会级方法贡献的方向。
- 本轮仅做本地索引召回、原论文与近期近邻核查、聊天交付；不启动实验、自动抽卡、Zotero 导入或完整 idea workflow。重点区分已覆盖迁移与待验证方法机会，不承诺录用或把场景替换视作创新。
- 已完成定向核查，优先候选为：STOPD 迁到依赖完整轨迹的 hindsight agentic OPD（截断不仅删位置，还使保留位置缺少原 teacher target）；EOPD 迁到可执行行为分支覆盖（token entropy／语义一致率不等于有效行为分布覆盖）。均为助手待验证提案，不是已确认新颖或用户已选题。
- 关键原文：STOPD（2610.21337，§3/App.A 的 local-feedback 不变条件）、SEED（2607.14777，§3.2/3.3 的完整轨迹 skill 与 paired scoring）、HERO（2606.11559，§3.1–3.2 的 full-trajectory reflection）；EOPD（2603.07079，§4），ActionOPD（2610.19820，§2/App.A.1 明确 agreement 不保留 teacher modes）、ASL（2506.17697，已有执行状态转移语义）。简单加 FKL／语义匹配不作为新颖贡献。
- 排除／降级：SOD v3（2605.07725 §5.3）已明确覆盖 non-monotonic recovery 与 hard-mask 缺陷，不能声称重新开启监督本身新；SSPO（2608.12764 §3）已研究答案／证据特权压缩搜索路径；GraphOPD（2610.08959）、BranchOPD（2610.13481）、STI-OPD（2610.10878）、FTB（2608.01953）覆盖结构选步、分叉和 teacher bridge 等直接迁移。截断后选择性 teacher 查询仅留为较弱候选。
- 证据边界：定向章节核查与近邻检索，不是全领域逐篇查新；未运行训练或验证实际收益。STOPD 候选只针对蒸馏项，联合 GRPO 的终局奖励、组归一化需另处理；局部 proxy 与 hindsight 梯度若不相关，残差校正不会有效降方差。当前无可用语音命令。

## SFT→OPD 与 OPD→RL 阶段关系检索（2026-10-16）

- 用户要求找以阶段关系为核心问题的研究，明确排除仅使用相应 recipe 的擦边论文；聊天交付，不启动 ARIS、实验、抽卡或 Zotero 导入。
- OPD→RL 的专门研究：Sequential Beats Joint（2609.04108，§4–6/App.C）、RL Starts before RL（2609.28145，§4–7/App.A.3）、Stage-1 Controls the Entropy Regime（2606.09059，§2/§4–8），已核对原始 HTML 对应段落。后者 small-data VLM 中未见稳定最终优势，不能把前两篇正面结果推广为普遍结论。
- RL Starts before RL 发现初始 accuracy/pass@k 不足以解释后续收益，student-prefix FKL/RKL 排名在 RL 后反转；alignment＋retained uncertainty 仍是作者假说。报告 checkpoint 选择标准未明确、总预算未对齐、objective 对照未估多 seed 方差。
- SFT→OPD 的直接证据是专门章节／消融：Rethinking OPD（2604.13016v2 §5.1）、IPD（2609.37170 §4.3 Fig.6）、Scaling Properties（2609.32722 §6.2/App.J），已回查原文；分别展示冷启动获益、降低依赖、weak-to-strong 冷启动有害，不称为三篇都以 SFT 冷启动为整篇主问题。本轮未找到全面回答冷启动内容／强度／切换准则的独立系统研究，非不存在的证明。

## Rock Tokens 的具体方法切口（2026-10-16）

- 用户指出 mask Rock 会掉分，要求具体 gap 与新的 token selection；延续不调用 ARIS，聊天交付，不启动训练、不自动抽卡。
- 原文核查：Rock-Freeze 同时屏蔽候选 token 与关联窗口，不能把掉分归因于候选 token 单独损失；推理 knockout 也不等于训练更新价值。
- 待验证候选：按 Rock 更新对后续内容更新的促进效应选择 occurrence／小组，并检验更新顺序；直接收益、两步交互与最终任务收益分开测。二维解析例子验证机制可能存在，不代表真实 OPD 已证实。
- 查新风险：Filter-then-Weight（2604.00001v2）已做 optimizer-aware 集合互补；AlphaToken（2606.01635）已做后续计算路径影响；BLADE（2606.18650）已做双层数据选择。两步 lookahead 形式本身不作为 novelty，尚未完整查新或形成已验证方案。

## Rock Tokens 近邻与持续残差机制（2026-10-16）

- 用户要求查 OPD 与更广泛领域的近邻，并解释结构／风格 token 为何仍不对齐；延续不调用 ARIS，仅研究解释，不运行训练、不自动抽卡。
- 已定向读 Rock Tokens v4（2605.09253）§2、§3.2–3.3、§4.2–4.3、附录 B/D.2。类别包括格式／边界、discourse 与数字；不能把全部 Rock Tokens 等同无用风格词。§4.3 明确存在冻结后的性能差距，较稳表述为低边际收益而非完全无贡献；未引用正文不一致的 speedup 数字。
- §2.6 测的是每个 token type 的平均 logit-gradient 向量范数，不等于单次梯度范数均值；Adam 高频抑制是作者未验证假说。高频本身不推出有效更新趋零，正的 logit-space alignment 也不能证明实际参数更新足以降低对应损失。
- 新近邻：Why OPD Sometimes Fails: Vanishing Learning Signals（2610.11247，已读 §5.1/§6）；广域近邻 Does KD Really Work（2106.05945）、Heavy-Tailed Class Imbalance（2402.19449，Rock 原文直接引用）、Softmax Bottleneck（1711.03953）、RHO-LOSS（2206.07137）、Dataset Cartography（2009.10795）。其余主要核对原始摘要，不声称为直接后续或已证 Rock 成因。
- 助手解释保持待验证：跨上下文表示／梯度冲突、有效优化步长不足、on-policy 访问分布变化与统计聚合。固定 teacher 在固定完整 prefix 上目标不变；词汇风格不重要只能解释任务指标不敏感，不能解释 KL 必然有残差。已用二分类共享参数例子验证正残余 KL 与零总梯度可共存，非真实模型实验。

## DIAL-OPD 与非熵 token selection（2026-10-16）

- 用户要求用易懂语言判断 DIAL 干预的理论合理性，并从 SFT／RL 搜集非熵、非普通不确定性的 token selection 灵感；延续禁止调用 ARIS，不把普通接续或已有筛选套路直接当新方法。
- DIAL（2610.11659v1）已核对方法、实验与附录：β=1 等于按绝对概率差筛选位置，选中位置保留原 signed OPD reward；40% loss 保留率不等于减少 60% 总计算。完整 reverse-KL 本身已通过采样频率体现概率尺度，DIAL 改变的是选择准则与实际更新分布。
- 检索入口：LESS（2402.04333，样本级）、BRIDGE（2609.22943，SFT token 级）、ssToken（2510.18250）、Critical Tokens Matter／cDPO（2411.19943）、CFT（2510.10974）、OPPO（2605.21851）、CSCR（2607.27888）、GRAD-MATCH（2103.00123，通用样本级）。BRIDGE、CFT、cDPO 已定向读方法，其余主要核对原始摘要；不构成候选方法的完整查新。
- 助手拟议的可试方向是任务更新方向一致性、成功／失败的判别性、历史可学习性与 token 集合的更新互补性；均有已有近邻，不宣称新颖或顶会就绪。聊天交付，不启动训练，不新增 cards／报告／wiki。

## Rethinking OPD 机制与后续研究核查（2026-10-15）

- 用户要求汇总 Rethinking OPD（2604.13016v2）的全部机制解释，区分社区支持、已有后续与可否证结论，并讨论顶会研究切口；明确禁止调用 ARIS。本轮只读研究与聊天交付，不运行训练，不自动抽卡／导入 Zotero／写 wiki。
- 用户纠正：DuoOPD 是单轮 multi-task OPD，不是 agentic OPD；不得把普通 teacher 接续、接续择优或重加权直接包装为新方法。本轮不强行迁移到 agentic 设定。
- 已核对原文 §2–6 与相关附录，以及 One-Shot、OPSA、Many Faces、Unmasking、ResOPD 的相关原文段落；其他近邻主要核对原始摘要。较稳的共同观察是 teacher endpoint 不保证收益、student-prefix 可能削弱监督；新增知识必要性、同结果推断同分布、共享 support 普遍充分性与梯度抵消仍需区分证据强度。
- 重要后续入口：Rethinking OPD II（2609.04172）、OPSA（2608.31046v2）、Unmasking（2605.10889）、Many Faces（2605.11182v2）、TT-OPD（2609.34447）、ResOPD（2610.04882）、Semi-OPD（2610.11291）、TS-OPD（2610.05974）。不能把摘要核查当完整查新或因果验证。
- 公开代码核查：thunlp/OPD commit `ac26e38d6f1572eb027597b48a9f4e01f6915ef8` 中 intersection 与 symmetric-difference 分支的概率权重 normalization 不同；论文 Eq.5 的 conditional KL 在 k=1 必为零，公开 top-1 reward 分支可非零，已做标量数学检查。尚未复现历史 run，不据此宣称论文结果错误。
- 研究切口仅为助手候选判断：优先区分 teacher-specific 信息迁移与 student-only 概率校准，检验共享 support 消融中的尺度／质量混淆；普通 tail correction、teacher 接续、gradient surgery 已有密集近邻，不直接视为新方法。未启动实验或 claim-level 查新。

## 创新 pattern 与候选 idea 发散（2026-10-15）

- 用户新增评价标准：按“最容易、最常见地产出顶会 idea”给创新 pattern 排序。本轮给 OPD 方法论文场景的研究判断，区分 pattern 的选题效率与具体候选的实现难度，不声称统计过各 pattern 的接收率；未选定方向或授权实验。
- 用户进一步要求：除跨论文结论冲突外，梳理其他创新 pattern，并给出对应 OPD idea。沿既有偏好以 agentic OPD 方法贡献为主；本轮交付 pattern、具体干预、近邻与否证方式，不运行实验或完整 ARIS 流程，不自动抽卡／写 wiki。
- 采用 research-codex-workflow 综合，并补 idea-creator 的有界发散阶段；两个只读独立视角生成候选。所有 idea 保持待验证，初筛检索不等于 claim-level 查新。
- 新核查近邻入口：SCOUT（2609.38360）、Look Ahead Before You Distill（2608.01953）、EOS semantic stopping action（2609.20511）、State-OPD（2610.13238）、MemOPD（2608.07068）、VC-OPD（2610.14939）、RT-OPD（2609.28778）。仅记录与候选重合风险，不据摘要认定完整方法边界。
- 发散完成：六个候选为执行效果分布蒸馏、因果偏序计划蒸馏、学生可达目标投影、以学生接续成功训练 teacher、证据变化引发的动作偏好变化蒸馏、保留未来决策信息的记忆压缩。两个生成视角均已返回；不做录用式 verdict 或 novelty 排名，用户未选题。
- 关键否证对照分别为动作规范化、独立步骤随机置换／同执行器、给 teacher 学生工具规范＋DePO（2203.02214）、固定 teacher 候选经学生接续择优、同反事实数据的普通 OPD、等长度任务导向摘要。候选在聊天交付，遵循本项目最小产物约束，不新增报告、自动 trace 或 wiki。

## 跨论文结论冲突分析（2026-10-15）

- 用户希望从已总结 OPD 论文中的冲突结论寻找 idea 切口；本轮做跨论文解释和候选问题分析，未启动完整 idea workflow、实验、抽卡或 Zotero 导入。
- 重点回查原文：PW-OPSD 的递增位置权重 vs Prefix Teach, Suffix Fade 的后缀 release；OPSD 正面结果 vs Rethinking OPSD 的长预算 thinking 退化；TIP 高分歧纠错 vs Rock Tokens 高损失低功能贡献；AsyncOPD vs f-OPD 的陈旧性边界。TurnOPD 用于补充深层监督不足的 agent 证据。
- 结论边界：目前是不同设定下的机制张力，未证明同条件下结果不可兼容；尤其 position、token occurrence/type、局部动作估计/整条轨迹分布不能混用。优先候选为信息不对称对搜索行为的影响，以及监督可靠性是否能随新观察恢复；均未完成查新，用户尚未选定。
- 现有 AR-OPD、PBSD、TurnOPD 等已覆盖部分修复路线；不得把简单 privilege 拆分、credit 转换或自适应截断当作已确认的新 idea。聊天交付，不新增报告或改旧卡。当前无 `say`，无法语音通知。

## 强 teacher 可教性机制检索（2026-10-12）

- 用户要求查找能区分同家族强 teacher 蒸馏失败的分布重合、容量、能力增量与推理步骤跳跃解释的研究；重点 OPD，补 SFT 证据。仅检索与解释，不运行实验、不自动抽卡或导入 Zotero。
- 原文核查重点：Rethinking OPD（2604.13016v2）、Unmasking OPD（2605.10889）、TS-OPD（2610.05974）、FP-OPD（2608.01263v2）；最新 Semi-OPD（2610.11291）仅核对原始摘要。
- 最直接的 Capacity Gap 论文为 OpenReview TteFp6TLUA：本轮原站 PDF 被 challenge 阻断，结合原始 PDF 搜索索引与现有 bounded brief 核查 §5/Table 2–6；旧 L1 的 realizability 概括不足以代表其 entropy-shape / destructive-token 实验，未改旧卡。
- SFT 对照：Small Models Struggle（2502.12143v3）、Revisiting Capacity Gap（2604.08880）、The Signal is in the Steps（2510.03988v2；旧标题 Local Naturalness）。最终在聊天给阅读矩阵与因果证据边界；不能把低 overlap、有限采样不成功或局部不可达直接等同硬容量上限。

## synthesis 整理与具体 failure-mode 综合（2026-10-06）

- 用户要求整理堆积的 synthesis Markdown，并单独保存具体、可观测的 failure modes；授权范围仅本主题文件组织和综合，不改 cards/schema，不运行实验。
- 入口 `synthesis/README.md`：阅读导航移入 `reading/`；旧 71 卡谱系、07-29 截止检索和早期选题判断移入 `archive/`；保留原文并标注历史范围，迁移／回滚表在入口。`synthesis/queue.md` 为流程依赖，原位保留。
- 新增 `synthesis/failure-modes/concrete-failure-modes.md`：14 个具体诊断，区分观测、作者机制、方法对应和限制；显式映射 TrOPD、REOPOLD、TOP-D。基于卡片召回、相关卡片定向复读及本轮原文核查，未逐篇重读全库或审计全部 EMNLP 候选。
- `teacher-pattern-mismatch.md` 保留为专题，标明旧覆盖与历史选题判断。reading 中 77 卡地图和会议候选仍是原日期快照，不冒称当前全库。
- 迁移同步修复本地引用和本状态里的旧路径；原有未提交改动保留。
- 验证：333 个本地 Markdown 链接无断链；88 cards 的 validator 为 0 errors／0 warnings；11 份原已跟踪的迁移文件对照 Git 原文，除状态提示和链接目标外正文一致。当前无 `say`，无法语音通知。

## 当前任务：用户指定 NeurIPS 2026 OPD 19 篇（2026-10-04）

- 用户授权对指定的 19 篇论文抽卡；已存在的卡只需更新 NeurIPS 2026 身份信息，不批量迁移旧 schema。
- 清单覆盖 f-OPD、AsyncOPD、Behavior Cloning is Not All You Need、Rock Tokens、KL for a KL、Learning to Foresee、Proposing Better Rollouts、REOPOLD、SEAD、SimCT、Many Faces、Trust Region Policy Distillation、Position-Weighted OPSD、Supervision Fidelity Decay、CoTrek、Co-Evolving Policy Distillation、Variational Policy Distillation、Rethinking On-Policy Self-Distillation for Thinking Models、Harness Self-Distillation。
- 执行：查重；核对官方会议身份与原论文；缺失项按现有 L1 模板抽卡；已有项局部更新；完成后运行 validator。未授权 Zotero 导入或实验。
- 本轮用户明确指定论文，视为本次收录范围；代码、数据及组织证据在正文记录，不因旧准入规则静默遗漏清单项目。无法核实的 venue 保留原值并报告。
- 完成 17/19：7 张已有卡更新 venue；10 张新卡基于原 PDF 写入。19 个标题均匹配 NeurIPS 官方 `https://neurips.cc/Downloads/2026`，官方 virtual 详情页当前未开放；匹配清单暂存 `tmp/neurips-2026-opd/official-matches.json`。
- 已更新：`notes/26_rock-tokens.md`、`26_effopd.md`、`26_reopold.md`、`26_simct.md`、`26_many-faces-opd.md`、`26_position-weighted-opsd.md`、`26_supervision-fidelity-decay.md`。保留旧正文/schema；REOPOLD 同时改会议标题并纠正 org 为 Microsoft。
- 已新增：`notes/26-f-opd.md`、`26-asyncopd.md`、`26-noisy-expert-opd.md`、`26-vopd.md`、`26-sead.md`、`26-copd.md`、`26-vpd.md`、`26-rethinking-opsd-thinking.md`、`26-ophsd.md`、`26-top-d.md`。正文记录组织、代码/数据证据与实验边界，不增加 schema 字段。
- 身份区别：清单 TOP-D（arxiv:2607.04751）不是旧 TrOPD（arxiv:2606.01249）；旧 `notes/26_trust-region-opd.md` 保持 arxiv，不以相似名称覆盖。
- 待全文的 2 篇不写正式 L1：CoTrek（官方条目 `https://neurips.cc/virtual/2026/poster/154397`）；Proposing Better Rollouts（`https://neurips.cc/virtual/2026/poster/155190`，作者确认录用 `https://csr16.github.io/`，但未链接全文）。已向用户请求论文链接；不把会议标题或作者概览图当完整论文证据。
- 验证：`uv run --frozen python scripts/autoresearch.py validate` 为 88 cards、0 errors、0 warnings；已视觉核对 vOPD、SEAD、OPHSD、TOP-D 关键表格。当前环境无 `say`，无法语音通知。

> 只保存下次启动所需状态；任务路由见项目 `AGENTS.md`。

## 环境与 smoke test：2026-09-29

- 用户要求兼容 Mac 与 WSL；当前 Research 在 WSL，未来仍可能回 Mac。共享依赖以根目录 `pyproject.toml` / `uv.lock` 为准，各机器分别运行 `uv sync --frozen`，不复制 `.venv` 或写死机器路径。
- Research `.venv` 已恢复；在 OPD 中用 `uv run --frozen python` 执行。WSL 的 Zotero 插件 0.1.2 已安装；Windows Zotero 位于 `D:\1000_study\Zotero`。9 月 29 日的端口阻塞已在 10 月 4 日解决，最新验证见下文。
- 抽卡 smoke test：按经典论文准入新增 `notes/20-imitkd.md`（EMNLP 2020，arXiv:2009.07253）；会议正式 PDF 下载至 `tmp/pdfs/imitkd-2020.pdf`，pypdf 提取成功，并视觉核对算法页。查重无旧卡；写卡后全库 78 张，validate 为 0 errors / 0 warnings，URL lookup 可命中。
- 原文显示 ImitKD 支持退火混合比例和 hard/full 两种监督；旧 GKD 卡中“固定 λ=0.5、只用 forward-KL”不应当作原文事实，本轮未迁移旧卡。抽卡链路通过不代表 Zotero 连接通过。

## Zotero 全流程验证：2026-10-04

- Windows Zotero 9.0.6 已开启 Local API；WSL 插件经 `http://127.0.0.1:23119` 访问 Local API 与 Connector 均为 200。
- 复用 ImitKD 卡完成查重、书目导入、PDF 附件保存、全文读取、BibTeX 导出、引用插入和 card validate。导入到已有 `LLM` collection（`8BRAC9IG`），顶层条目数由 1 增至 2；只新增 1 个论文条目 `H43RU8K9` 和 1 个 PDF 附件 `MD6GZ9QM`，重查无重复。
- 附件为 `imported_url`，保存于 Windows Zotero storage；WSL 直接读取成功，13 页，SHA256 与会议正式 PDF 相同。Zotero 全文索引为 13/13 页，含方法正文。
- BibTeX key 为 `lin_autoregressive_2020`；测试导出 `tmp/imitkd-smoke-test.bib` 含 1 条，`tmp/imitkd-citation-smoke-test.md` 引用插入成功且未重复追加 BibTeX。现有卡库 78 张，validate 为 0 errors / 0 warnings。
- Zotero 9 的 `/connector/saveItems` 只保存书目，不自动下载 payload 中的 attachments。已通过同一 session 的 `/connector/saveAttachment` 上传原 PDF bytes；用 `/connector/updateSession` 将本次条目移动到既有 LLM collection。实现依据为 Zotero 官方 `xpcom/server/saveSession.js` 与 `server/server_connector.js`；通用插件 helper 的 RIS 导入不能被默认等同于已保存 PDF。Mac 环境尚未重测。

## 当前流程

- 目标：形成可投顶会的 OPD 工作，并从经典机制和近期录用论文中学习 idea pattern。
- 现有 71 张 L1 cards 主要由自动流程生成，只作低可信 recall，不视为已验证的领域积累或继续选择 OPD 的理由。
- 默认检索：全部 cards → 10–20 张相关 card → 3–8 篇原文。
- 新卡使用极简 YAML 和无标题正文；正文按“一句话 / Failure mode / 核心做法 / 方法增量 / 关键证据与边界”组织，只有明确因果证据时才增加“瓶颈（作者诊断）”。旧卡保持原样并由 registry 兼容。
- Synthesis 按 failure mode 分 Markdown、以决策点为表格列；新卡默认只加表格行，只有研究结论变化时才改文字判断。
- `_meta/`、旧 queue 和 generated files 是历史材料，不再维护。

```bash
cd /Users/chy/Research/opd
scripts/autoresearch.py status
scripts/autoresearch.py validate
scripts/autoresearch.py lookup <paper-id-or-url>
```

## 近期研究入口

- `synthesis/reading/agentic-opd.md`：agentic OPD 的单页索引，按 rollout depth、prefix reliability、loss allocation、action boundary 与 termination stability 导航；TurnOPD 已精读并写入 `notes/26_turnopd.md`。
- `synthesis/archive/2026-07-radar/arxiv-opd-120d-radar.md`：2026-03-31 至 2026-07-29 的 103 篇 LLM/agent/MLLM OPD arXiv 高召回候选；32 篇重点一句话。
- `synthesis/archive/2026-07-radar/arxiv-opd-120d-synthesis.md`：近 120 天热点、瓶颈、idea pattern 与可信度边界；已记录 token-selection 效率口径和 privileged-information 三类混淆。
- `synthesis/archive/2026-06-lineage/opd-method-lineage-report.md`
- `synthesis/failure-modes/teacher-pattern-mismatch.md`：首份 failure-mode 综合；覆盖 pair/data/local-support/trajectory 四层 mismatch 与 20 篇核心方法。
- `synthesis/archive/2026-06-lineage/opd-method-lineage/04-idea-hooks.md`
- `synthesis/archive/2026-06-lineage/opd-method-lineage/05-evidence-and-limits.md`

## 研究约束

- 实习期间可较方便使用 8–16 卡算力。
- 当前仍在入门阶段并依赖 autoresearch，需要优先选择短反馈周期、可先做小实验否证的方向。

## 用户偏好

- 2026-10-12：用户倾向 ARIS idea 生成分阶段执行，担心一口气跑到底偏离要求；本轮咨询 human checkpoints 的设置，尚未确认具体检查点或授权修改 skill／启动 workflow。
- 2026-10-12：用户希望停止维护原有自定义文献脚本／pipeline，最多保留 card 模板；后续优先普通 Markdown 与现成工具，不新增专用脚本或重复卡片库。本轮未删除旧脚本、迁移卡片或切换到 ARIS wiki；是否采用 wiki 尚未决定。
- 2026-10-12：用户咨询 agentic OPD 的 ideation lens 选择，偏好方法贡献，尽量避免以审计为主的选题；尚未选定 lens，未要求运行 idea 生成流程或修改自定义 skill。
- 2026-10-12：用户表示后续研究重心倾向 agentic OPD，尚未确定具体问题或方法；本轮仅咨询 ARIS 分工与检索组织，未授权新一轮检索、抽卡、idea workflow 或实验。现有入口为 `synthesis/reading/agentic-opd.md`。
- 输出简短、可快速扫描。
- Card 优先优化可读性、信息密度和学习 research taste 的效率。
- 不因 schema 改动批量重写旧卡。
- 默认执行最小规则，不主动扩展系统。

## 当前选题评估：2026-09-05

- 用户要求独立重判 OPD research gap、潜在蓝海与初学者适合的方向；旧方向结论仅作参考，不作前提。
- 用户确认首篇目标为 2–3 个月完成投稿，优先反馈快、工程可控；以可持续多篇产出为取向。
- 本轮是选题分析，尚未确认具体研究方向或授权启动实验。
- 已补查 2026 年 8 月原论文，重点包括 OPSA（2608.31046）、OPD generalization（2608.16647）、TIDE（2608.09836）、CROP（2608.13387）与工具调用漂移 v5（2607.07050）。助手倾向优先验证短轨迹、可程序评测的工具决策语义保真；这是尚未实验、尚未被用户采纳的候选判断。

## 进行中：2026 三会 OPD 抽卡

- 本轮按 `doc/card-acceptance.md` 保守处理，只抽“直接 OPD”；该准入规则当前不含 ACL，因此 ACL main / Findings 未写卡。
- ICML 2026 direct OPD 已新增 5 张：FA-OPD、Decomposed OPD、Video-OPD、SDFT、HPD；EOPD、OPSD 已有旧卡，不重复写。另新增 TurnOPD 卡；全库现为 77 张，validate 为 0 errors / 0 warnings。
- 上述 5 张已按新正文结构重写：Failure mode 必写、瓶颈可选、Pattern 删除。
- GenRe² 的主贡献是 decoding-based regression RL，OPD 只是辅助 credit-assignment 组件，本轮排除。
- ICML 高相关机制：On-policy Expert Corrections、SDPO、SRPO、TMS。
- ACL main 高相关机制：BEPA、DGPO、CurioSFT、REDI；没有标题/摘要明确的标准 LLM OPD。
- ACL Findings direct OPD：Prefix OPD、COPSD、CORD、Veto；近邻包括 SmartAD、P-BRIDGE。
- 未决：OPD 高相关机制论文是否也写正式 L1 card，还是只在 synthesis 中记录；用户尚未确认。

## ARIS 接入：2026-09-28

- 2026-10-12 更新：按用户要求 `git pull --ff-only` 至 `26b95cfa0d8747078e9e43b42e20952709e561b8`（上游 10 月 7 日提交），使用 `--skip-new --quiet --no-doc` 重新安装原五个 Codex skills 与 shared-references。6 个链接及 5 份 SKILL.md 均通过检查；源码工作区干净，OPD AGENTS.md 与自定义 generate-method-ideas 未改变。未安装新增 Lean skill 或配置 MCP 服务。9 月 28 日版本为历史安装记录，当前恢复请以本条版本为准。
- 用户授权在 code/external 下 clone 最新 ARIS 并安装到 OPD；旧独立 aris 目录先核查重要内容。
- 源码 `~/code/external/aris/`，本次版本 `341f914024d270dc5c8fa51337d1ad38829273aa`；恢复原五个研究 skills 和 shared-references，使用 --no-doc。
- 旧 `Research/aris/` 本机仅有 AGENTS.md，暂保留；不能据此判断旧电脑未提交内容是否存在。
- 旧 research-refine 补丁未应用，触发限制移入本项目 AGENTS.md。未新建或修改 wiki、未迁移总结、未运行研究流程。验证发现 OPD 原有 research-wiki/（含旧 query_pack、ideas），后续流程可能自动读取，需核对时效性。
- 安装与恢复说明：`../doc/aris-setup.md`（相对 OPD）。

## 当前任务：已抽卡 OPD 方法分类（2026-09-28）

- 用户确认执行：短版方法地图 + 覆盖全部现有卡片的一句话分类表。以机制分类，单篇只列一个主类，必要时注明跨类；不改旧卡或 schema。
- 已确认 registry 为 77 张；区分直接 OPD、邻近方法与机制分析，不把 77 张都当成独立 OPD 算法。
- 输出计划：`synthesis/reading/opd-method-map.md`、`synthesis/reading/opd-method-catalog.md`。基于卡片作索引，关键边界抽查原论文；不声称全部重新精读或完成开源资源审计。

- 已完成：两份 synthesis 均已写入；77/77 卡片各出现一次，分类数量与本地链接检查通过，card validator 为 0 errors / 0 warnings。原始来源抽查覆盖 GKD、HPD、FA-OPD、Many Faces；未重新精读全部 PDF。

## EMNLP 2026 官方名单入口核查（2026-10-05）

- 用户要求重新核查 XML 之外的论文列表下载入口；已找到官网 `/program/` 链接的公开 Google Sheets 报告日程。
- 下载到 `tmp/emnlp-2026-index/emnlp-2026-presenter-schedule.csv` 与同名 `.xlsx`；核查说明在同目录 `README.md`。5611 个唯一 ID/title：MAIN 2710、FIND 2487、IND 265、DEMO 86、TACL 50、CL 13；CSV/XLSX 解码后逐行一致。
- 此表无摘要、完整作者或全文链接，属于报告日程快照，不声称最终录用全集。官网 Main/Findings 仍是占位页；Anthology master 完整文件树尚无对应 XML；OpenReview 主会投稿不公开；Underline 535 注明 10 月 17 日向注册者开放。
- 未启动全库摘要补齐、OPD 抽卡或 Zotero 导入。

## EMNLP 2026 OPD 数量初筛（2026-10-05）

- 用户询问数量与阅读负担；在官方 MAIN/FIND 5197 条日程记录中，完整 on-policy … distill / 独立 OPD、OPSD 标题命中 33 篇（MAIN 20 / FIND 13）。
- 原始摘要补漏 RoCo-ACE、PTA、HINT-SD、StepOPSD、SGSD 五篇，共至少 38 篇 OPD 相关候选（MAIN 22 / FIND 16）；包含 OPSD、机制分析和多模态应用，不声称 38 种通用算法或完成全库摘要扫描。
- 候选与纳入依据：`tmp/emnlp-2026-index/opd-shortlist.md`。未自动抽卡、导入 Zotero 或启动逐篇精读。

## EMNLP 2026 OPD 分类与摘要级总结（2026-10-05）

- 用户要求对此前 38 篇逐篇分类、总结核心创新和结论。已写 `synthesis/reading/emnlp-2026-opd-overview.md`，按 6 个阅读类别组织；未修改 cards 或 taxonomy。
- 33 篇核对原始 arXiv 摘要，TGPO 另读 §3.1；MoralSteer 依据原始 PDF 的搜索索引摘要，下载 403，未经全文审计。原始摘要证据保存在 `tmp/emnlp-2026-index/opd-abstract-evidence.json`。
- 4 篇无可核实摘要/全文，只记录标题与证据缺口：Beyond Top-k、Self-Supervised OPD for Omni-Modal Video Captioning、MosaicAudio、CE-GAD。不以相似论文替代证据。
- 完成 38/38 官方 ID 覆盖与唯一性检查，33 份摘要均有标题/正文/URL；所有总结限于作者报告的实验条件，不声称独立复现或完成全会议摘要扫描。

## TGPO 全文精读（2026-10-05）

- 用户要求 failure mode、方法、实验、结论和局限；复用 `scripts/cache_paper_sources.py` 下载/抽取 v2，缓存 `tmp/tgpo/`，PDF 14 页。
- L2：`notes/l2/26-tgpo-deep-dive.md`；视觉核对 pp.5/6/8/13。主方法为 student-prefix teacher top-1 CE + GRPO，guidance 0.002 线性降至第 200 步为零，总 300 steps。
- 明确边界：7B vs KDRL ID +3.9，但 vs LUFFY +1.2；1.5B vs GRPO++ +1.3。无 multi-seed 显著性、hard/soft 比较及系统成本测量；paper Eq.3 存在 max-RL 与 positive-CE 的符号不一致。未改旧 L1 卡或运行实验。
