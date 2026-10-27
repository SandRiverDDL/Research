# Agentic OPD Current State

> 更新：2026-10-22。后续 session 先读本文件和项目 AGENTS.md。

## 当前任务与完成情况

- 当前任务已完成（2026-10-22，五篇补录）：用户指定 GraphOPD 2610.08959、STI-OPD 2610.10878、BranchOPD 2610.13481、ActionOPD 2610.19820、R2S 2610.28586，已用 canonical ARIS helper 新增5篇并基于原HTML补全正文，wiki现29篇、31 ideas、92 edges；索引与query pack已重建。GraphOPD v2 §3.1实际为GRPO行为快照自蒸馏，按指定清单作为boundary-self-distillation近邻保留，不计外部teacher方法；其余4篇以外部teacher主实验为依据。新增8条paper-gap关系。强调STI只校正固定context token采样、Branch token节省不含teacher/replay、ActionOPD状态选择和总预算口径、R2S额外修复成本及单run三次decode方差。29个唯一arXiv ID、5页schema/本地链接/45个原文锚点核查通过，原24篇papers与31 ideas正文hash未变。各页Assumptions记录实际阅读范围，非全文穷尽阅读／独立复现；未改旧gap map或启动idea／实验。临时原文缓存已清理；环境无可用语音命令，未能语音通知。

- 当前任务（2026-10-22，可实现gap筛选）：用户明确问既有Agentic OPD未覆盖且能做的问题；本轮仅做有界机制/可行性筛选及定向查新，未调用完整idea-creator／research-refine、未训练。不能把任意prefix的teacher可靠性视为可由分歧直接识别。新检索核查PivotOPD（2609.40285，方法包含privileged self-teacher，虽不纳入正式文本外部teacher库仍计prior art）、State-OPD（2610.13238）、AsyncOPD（2606.24143）、ActionOPD（2610.19820）；恢复、状态分叉、异步和跨tokenizer不能宣称空白。暂列部署剩余工具调用预算条件下的OPD为待验证候选：teacher/student同看(h,b)，保留原rollout/teacher前向，比较同预算曲线；区别于TurnOPD训练深度、BARD（2511.01470）CoT长度控制、When and What to Teach（2609.05513）teacher查询预算。尚未证明全领域新颖或收益，不是用户已选idea。工具接口等价监督与旧semantic-quotient/action候选及KAT harness randomization过近，不作为新推荐。未运行pilot或改原paper/idea/graph/索引。
- 当前讨论（2026-10-19，ATOD信号冲突）：定向回查v6 §4.1–4.3、§5.3–5.4、B.2/B.4、C.4/C.5。论文有退火消融及信号强度／训练动态，未找到OPD–GRPO梯度cosine、反号比例或冲突消融；B.2仅解释OPD梯度。Eq.8先相加advantage再做clipped update，反号时可抵消；T-DUR的disagreement是teacher–student分布差异，不是两目标冲突检测。以上抵消是公式推论，不是作者测得的冲突结果；未启动idea／实验。
- 当前讨论（2026-10-19，OPD与RL协同）：用户询问联合方法数量、协同结论及记忆中的sequential论文。只读检索邻近opd项目既有综述后找到Sequential Beats Joint（2609.04108v2），并回查原HTML；其Table2先OPD后GRPO的logic/math平均pass@1为80.6/31.8，KDRL-Annealing为68.9/30.0，数学增益远小于逻辑；同总steps非同总GPU预算，未直接比较ATOD。当前24篇库明确同student任务RL＋teacher监督的5篇为ATOD/SOD/MemOPD/DGPO/KAT-Coder-V2；Cross-Domain Hybrid OPD另计跨域混合边界项，不把纯PG蒸馏或teacher先RL计入联合。另核查TGPO（2605.13230v2）、Long-Context Recipe（2605.12227）、Sparse-to-Dense（2605.12483）：分别支持退火teacher-target指导、长上下文联合锚定、teacher-first分配再transfer及可选student-RL；无普适sequential优于joint结论。未做穷尽检索、实体入库或实验；未跨主题写文件。
- 当前讨论（2026-10-19，近邻发表与监督可靠性）：用户追问录用状态、CUSUM、LOLS具体流程，并质疑teacher成功不能证明能纠正student。官方来源确认LOLS=ICML2015、DAgger=AISTATS2011、Scheduled Sampling=NeurIPS2015、SafeDAgger=AAAI2017、Reverse Curriculum=CoRL2017；近期AdaSwitch-KD／Relay／trajectory-aware TOPD／TIP／POPD-Truncated TOPD／FiRe未查到正式录用证据，不记为拒稿或已录用。LOLS原Algorithm1为learner roll-in、逐候选action、每次rollout以beta选reference否则learner执行至终局、终局cost训练cost-sensitive policy；不是逐token混合。可靠性讨论区分teacher自执行能力、student接续收益、更新后自主学习收益；DASH分歧及FTB未来teacher-preference均为代理，不能当task correctness或learning gain保证。未启动新idea／实验。
- 当前讨论（2026-10-19，机制近邻溯源）：用户要理解现有Agentic OPD的idea如何形成，重点DASH／FutureBridge与通用reasoning OPD或其他领域的具体近邻；不是新一轮idea生成。已定向核查原HTML：DASH明确讨论AdaSwitch，沿用Guided的双KL；其累积证据与CUSUM相似仅为机制解释。FTB附录F明确对照trajectory-aware TOPD（2606.00305）及Relay-OPD（2607.26057），不得与truncated TOPD（2605.31490）混同；LOLS为跨领域机制类比。ATOD明确引用TIP（2604.14084），TIP已有entropy/divergence＋Soft-OR；TCOD与POPD、reverse curriculum，Guided与DAgger／scheduled sampling，SOD／SAGE与FiRe只标近邻，不声称作者实际灵感来源。无新方法、训练、完整查新或论文实体入库；ATOD／DASH／FTB仍缺直接交叉实验。
- 当前交付（2026-10-19，三个近邻迁移）：用户明确限定teacher-guided／交互式模仿学习、process supervision／credit assignment、Agentic preference optimization。报告 `research-wiki/stepwise-transfer-patterns.md` §0.4列8项来源机制与OPD改动，新增核查SafeDAgger §3及SCoRe §4.2–4.3（当前标题Student-Centered Distillation Narrows the Agentic Gap，ICML2026），其余复用已有原文核查。优先级判断分别按teacher预算、已有grouped reward、action-level目标给出，不作为用户已选idea；明确query head只预测deviation、SCoRe可多次纠正且需suffix/环境重置、局部credit进RL通道而非负KL权重。新增2个HTML/锚点和8行表结构通过，58个原paper/idea/graph/自动索引hash相对本轮新快照不变；未训练/完整查新。环境无语音命令，未能语音通知。
- Teacher来源核查（2026-10-19）：ATOD作者基于开源Qwen3在ALFWorld/WebShop/Search-QA分别做GRPO，6个task-specific teacher全部发布于`https://huggingface.co/TanQT24/ATOD_ckpt`（每域4B与30B-A3B）。已核作者README、HF模型卡及API实际safetensors/config/tokenizer列表，公开且未gated；4B约8.82GB、30B-A3B约61.07GB磁盘权重。已补原ATOD wiki页；未下载/运行权重。复用可跳过teacher训练，仍需匹配原环境接口；用户未选定模型或授权训练。
- Baseline公平性讨论（2026-10-19）：用户质疑ATOD的RL+OPD与其他agentic OPD对比混淆监督来源。回查SOD v1 §4.3 Eq.10已明确GRPO+加权OPD，ATOD还含SDAR及固定混合消融，不能记为“完全未比较混合方法”。开放问题是ATOD复现SOD是否保留原GRPO、固定系数是否充分调优，以及同teacher/reward/预算下是否隔离退火与reweight；未核代码。Table2已有annealed+uniform、fixed+T-DUR、annealed+T-DUR，未列完整fixed+uniform对照；Fig1已有一个OPD→GRPO硬切换。自己的reweight应在相同RL+OPD骨架中比较权重，不能把新增reward当权重收益。
- 用户纠正（2026-10-19）：研究领域／安全效率等目标分类不重要；要的是**能迁入Agentic OPD的现成方法机制**。上轮目标谱系与31篇数量不是用户认可交付；此前“按目标扩展”是assistant偏离，不能恢复为用户要求。后续以原OPD的teacher评分上下文、action分布、蒸馏目标、时序credit和student状态覆盖为入口；每项必须给出实际训练改动、所需信号、增加的生成／前向／环境成本及失效前提。既有报告仅作来源池；迁移效果与新颖性仍未验证，不自动运行完整idea流程或训练。
- 本次纠正后的交付（2026-10-19）：原报告新增§0，以OPD闭环列7项迁移/对照：结构化候选soft-KL、teacher评分context去污染、异常恢复状态OPD、implicit PRM局部task credit、条件性anti-loop偏好、熵/温度目标基线、OPD/RL尺度与质量守恒对照。均明确迁移草案/成本/失败前提，非原论文已验证OPD结果、非用户已选idea；HPL/CSO/CoBRA等依赖额外labels/分支的原方法不列廉价直接迁移。CPU验证候选概率与熵温度等价通过，58个原实体/索引文件hash不变；未训练/完整查新。
- 当前讨论（2026-10-19）：用户要求具体分析ATOD的低成本reweight指标与变换：除分歧、student/teacher熵外的统计量，gate、min–max及Soft-OR替代。已回查ATOD §4.3，定向核查EOPD、FiRe-OPD、SPOT、UECR与R²-OPD相关机制；本轮为有界方法讨论，未重跑全套idea生成／未启动训练。建议比较teacher-confidence门控、先联合token信号再pool到turn、稳健归一化和固定总体监督强度；均为待测建议，用户尚未选定。注意teacher高熵可表示可行多样性，H_S>H_T不能作硬门槛，loss gate不自动省teacher forward；仅CPU两组toy检查聚合顺序与过度自信反例。
- 当前任务已完成（2026-10-19，覆盖扩展）：用户指出stepwise pattern覆盖过窄，要求按性能／效率／安全／鲁棒及其他目标扩展Agentic DPO等训练家族。已扩充原 `research-wiki/stepwise-transfer-patterns.md` §7–12：12个目标轴；31篇方法/recipe的原HTML局部机制核查，另2篇SPrPO/SecOPD仅作邻近来源；保留待补读候选与排除理由。三个只读分片各发现17/14/15个候选，主线程补探索／澄清／memory／implicit credit／个性化5篇。33个方法源HTML与章节锚点检查通过，主要元数据由原arXiv核对；58个原paper／idea／graph／自动索引文件聚合hash不变。区分训练样本效率、训练吞吐与部署tokens/calls；昂贵方法保留谱系但单列成本。仍非穷尽/完整查新，未入库新实体、未细化自己的idea或训练。当前无语音命令，未能语音通知。
- 当前任务已完成（2026-10-19）：用户要可迁入通用、white-box Agentic OPD的stepwise操作pattern，来源包括tool-use、Agentic DPO／RL及其他领域；报告 `research-wiki/stepwise-transfer-patterns.md`，10类操作含预算、结果校准、历史分组、turn／segment credit、局部DPO、首错修复、工具信息收益、replay、优势回归。核查原HTML方法、主要外部条目metadata与本次结构／链接；原paper／idea、graph及自动索引58文件聚合hash不变。明确额外critic／生成／环境分支成本及signed advantage不能直接乘KL；这是代表性机制调研，不是全领域统计或完整查新，用户尚未选择方法／授权训练。无语音命令，未能语音通知。
- 用户反馈（2026-10-19，ActionOPD讨论）：指出每状态让student／teacher分别多次采样、再匹配或干预的方案与此前自动生成idea相似，担忧严重拖慢训练及rollout吞吐。后续评估方法需明确额外自回归生成、逐轮阻塞依赖、跨轨迹并行与总体资源成本；以固定wall-clock／总预算下效果核查价值，不能仅以同step／task starts的分数或“可异步”支持效率。未授权新一轮idea生成或skill修改。
- 最新用户反馈（2026-10-19）：明确否定本轮ATOD选题的创新度，举“在二维reweight中加入teacher熵”作为比原推荐更直接的机制例子。Assistant撤回将belief distillation与teacher control variate列为主推荐的判断；此前报告/idea保留为历史，不作为已认可方案。Teacher熵尚未被用户确认为选题，不自动启动细化／实验。后续必须从ATOD具体机制提出清晰、可检验的增量信息与训练规则，不能用经典框架迁移、理论潜力或大量诊断替代实际创新。
- 当前任务已完成（2026-10-19）：用户指定ATOD `2606.27814v6`，要求阅读全文，重点找未关注／欠缺之处并提出顶会潜力idea。正文§1–6、附录A–D、表1–4与图1–13均已读（HTML+内嵌SVG，无PDF）。报告：`idea-stage/atod-ideas-2026-10-19.md`；更新原ATOD wiki页。Astra/Sol各8项→15机械组→fresh Astra全部审阅；trace、全量原候选和输入在`.aris/traces/idea-creator/2026-10-19_run01/`。
- 本轮选题为assistant暂定推荐，用户尚未选择：主候选1 `bayes-consistent-hindsight-belief-distillation`（回看后验→在线信念），主候选2 `teacher-action-control-variate`（teacher辅助task-RL降方差，高风险）；`evidence-separated-decision-target`仅作错误reasoning污染靶点验证储备。其余12组以archived/pending保留本轮不投入原因，非实验否证。15个新idea全部pending；原16个ideas与其他23篇paper正文hash未变。现24 papers、31 ideas、84 edges。
- 本轮查新已核对OG-OPD、GammaOPD、RA/CoRA、JOLT、SERL、SOPD、ActionOPD、ActFirst、GC-OPD、SCOUT，及ASL/GAD/vOPD/Q-Prop/privileged POMDP相关方法；Meta-RL task inference、Prospective Hindsight、Belief-Aware GSAC等仅摘要。不能把收益加权／未来KL／action等价／control variate／belief learning本身称首次提出。最终新颖性和same-family模型审阅均provisional。
- 验证边界（2026-10-19）：新文件／本地链接／JSON／node ID／原文锚点核查完成，索引与query pack重建；仅CPU三行动枚举核查CV抵消恒等式及min–max性质，未运行训练、GPU pilot、代码复现。先做固定日志校准／梯度方差／目标污染诊断，只有用户进一步选题后才细化研究或安排实验。当前环境无say/espeak/spd-say，未能语音通知。

- 当前任务已完成（2026-10-15）：按用户要求汇总wiki论文的同期方法对照、student／teacher、环境和分数，报告 `synthesis/contemporary-method-comparison.md`。核查20篇方法／报告／框架的原HTML实验表，另解释4篇基础背景不入多轮榜；35张表保留同篇设置、metric／split、teacher任务训练、baseline变体、重跑／引用和预算／seed口径。重点ATOD、DASH、FutureBridge等局部对照，不排跨论文总榜。各分片转录回查、20篇source ID覆盖、22节／35表列数与本地链接检查通过。未复现、未代码审计、未新增idea；未改24篇paper正文或query pack。

- 当前任务已完成（2026-10-15）：按用户要求基于现有24篇论文重建 `research-wiki/gap_map.md`。当前五个方法gap为G1错误恢复与交互成本、G2纠错与自主探索、G5跨轮任务信用、G6新程序知识迁移、G7多专家整合；这是assistant综合，未被用户选为具体方向。G3保留历史入口并拆为接口前提／G7，G4改为共同成本评测约束。每项有已有覆盖、开放问题与降级条件；不将库内证据缺口当全领域新颖性。
- 本轮证据与验证（2026-10-15）：综合24页已有记录，回查10篇原HTML相关章节，新增Planning Physics §5.3程序知识错配证据。新增12条paper-gap关系，图共51条；原24页papers与16页ideas逐页hash未变。24篇覆盖、7个稳定gap ID、关系端点／去重、本次相关文件链接检查通过；gap map与query pack的strict scan通过。Query pack为4036字符、包含全部五项摘要。已更新原调研的历史分类提示、wiki log与派生入口。未查新、未生成新idea、未跑实验。
- 用户反馈（2026-10-14，idea报告后）：质疑本轮候选高度同质化，集中在状态h上的probe、分叉、额外评估等操作，认为其难以scale、过于工程化；要求核查生成是否被prompt锚定及公开保存的子agent输入。本轮A1/A2推荐是assistant意见，未被用户接受。后续选题应明确评估规模化训练适用性、额外开销能否摊销及方法贡献，不能继续默认可重置环境和逐状态probe。当前只核查并解释生成记录，未授权重跑或改skill。
- 当前任务已完成（2026-10-14）：用户显式运行 ARIS idea-creator，目标为文本Agentic OPD方法论文，排除OPSD/自蒸馏、多模态、VLA、benchmark-only。Astra xhigh与gpt-6.1-sol xhigh各生成8项，16项逐项查新及批评评审；推荐A1执行效果等价监督、A2条件控制器蒸馏，A6学习收益选演示作为高风险储备。报告：`idea-stage/IDEA_REPORT.md`；证据：`idea-stage/novelty-evidence-2026-10-14.md`；原始候选：`idea-stage/candidates-2026-10-14.json`。16个wiki ideas均proposed/pending，2推荐、14储备、0精确撞题淘汰；原24篇paper未改。未运行pilot/GPU任务，不能声称效果或最终新颖性已验证。生成/审阅记录在`.aris/traces/idea-creator/2026-10-14_run01/`；线程上限导致每模型两个lens共用fresh上下文，文献jury复用非生成线程，Astra批评续接生成线程；均same-family provisional。
- 选题目标修正（2026-10-14）：用户明确希望做**方法论文**，不想以机制审计／诊断为主要贡献。后续idea生成以具体训练机制、训练目标或teacher–student学习流程为候选主体；诊断仅服务方法验证。此前assistant建议优先G2/G3不是用户选定方向，不得恢复为既定选题。这一约束已用于上方idea-creator任务；旧gap未作为用户已选方向。
- 当前任务已完成（2026-10-14）：用户显式调用 ARIS `research-lit`，处理 Awesome-Agentic-OPD 全清单，排除 OPSD/自蒸馏、多模态、VLA、benchmark。71条记录／70篇去重；保留24篇（19方法／技术报告、1框架、4背景），排除46篇。综述与完整判定表：`research-wiki/awesome-agentic-opd-review.md`。新增22页、复用TCOD/ReOPD原页；方法类核查相关HTML章节，背景仅摘要，均非独立复现。Agents-A1/Orchard含视觉评测／分支，本轮保守不纳入；CAST solver-teacher与Cross-Domain Hybrid OPD间接相关均明确标边界。全70篇metadata由原arXiv批量核实；4个gap、20条关系，索引与query pack已更新。未启动idea或实验。
- 本轮核对通过：24个唯一arXiv ID与正式保留集一致；页面、相对文件链接、20条关系与G1–G4一致，无脚手架TODO，原有两页正文未覆盖。Query pack为3876字符；gap map压缩到1040字符以保留全部四个gap。临时HTML／元数据缓存已清理；没有新增永久检查脚本，内容判断来自原文阅读而非独立验证。
- 安装更新（2026-10-14）：按用户要求新增 ARIS `research-lit`，项目现为 8 skills + shared-references；链接与安装清单已核对，README 恢复命令已更新。仅安装，未启动调研或 idea 流程。
- 文档偏好（2026-10-14）：项目 AGENTS.md 保持简短、中文、易读，不叠加操作历史。
- 最新阅读规则（2026-10-14）：原论文有可用且版本一致的 HTML 时优先读 HTML、用 HTML 原文锚点引用；不默认下载 / 渲染 PDF 或补页码。仅在 HTML 不可用、公式 / 图表缺失或解析有歧义、需核对版式或用户明确要求时，回到对应 PDF 部分。已写入项目 AGENTS.md，优先于通用 PDF skill 的 visual-review 建议。
- “现场编写脚本”指先前工具调用中临时生成并执行的 Python（写正文、检查结构 / 链接 / hash、记录时间等），未保存成可复用脚本；这是 Codex 的实现选择，ARIS 没有要求每篇重新编写此类代码。
- 最新用户任务（2026-10-14）：再入库一篇符合原排除条件的论文，实测并记录每步时间。已完成 ReOPD `2607.04763v3`：`research-wiki/papers/liao2026_multiturn_onpolicy_distillation.md`；原论文 PDF：`papers/reopd-2607.04763v3.pdf`。重点读 §§3-6，PDF pp. 12、14、15、16、19 目视核对。计时原始记录：`_meta/timing/second-paper-ingest.json`；阅读记录与分阶段耗时见 `research-wiki/ingest-timing-reopd.md`。
- 历史样例阶段曾有2篇papers、2条指向G1的关系；当前数量以上方本轮完成记录为准。继续使用ARIS wiki，旧card pipeline仍停用。
- 最新用户决定（2026-10-14）：在 agentic-opd **停用 Research workflow，保留 ARIS wiki**。已在项目 AGENTS.md 覆盖根默认规则：不自动调用 `research-codex-workflow` / `autoresearch`，不默认维护 queue / L1/L2 / brief / taxonomy，也不运行 card helper；旧文件保留，其他项目不受影响。
- 验证边界：ARIS helper 处理 ingest / dedup / index / query pack；上次 wiki schema / links / dedup hash 检查来自临时 Python，未保存为项目 validator。方法、数字与局限是原文阅读判断，LINT_REPORT 是整理出的记录。上次旧 card validator 在 cards 为空时通过，对 wiki 内容无实质证明；后续不重复运行它。
- 历史任务：先后试入库TCOD与ReOPD，第二篇记录步骤耗时；本轮用户已明确调用research-lit处理全清单，单篇限制已解除。
- 样例完成：TCOD，arXiv `2604.24005v3`；paper page：`research-wiki/papers/wang2026_tcod_exploring_temporal.md`，原论文：`papers/tcod-2604.24005v3.pdf`。使用原论文 HTML / PDF，已补全 9 个待填章节，保留已有 thesis；PDF pp. 5、6、8、9、10 目视核对。
- Wiki 位于本项目 `research-wiki/`，已生成 index / query pack / log；1 篇 paper、1 条关联 G1 的 edge。Schema、相对链接、重复导入不覆盖、技能入口与 strict query-pack scan 检查通过；项目 helper validate 为 0 errors / 0 warnings（正式 cards 仍为 0）。详见 `research-wiki/LINT_REPORT.md`。
- 本轮新增安装 `research-wiki`、`wiki-enrich`，现为 7 skills + shared-references。未修改上游源码，未复现实验、导入 Zotero 或配置外部 reviewer。
- 上游已知差异：Connections 不会被当前 helper 自动回填；query pack 未实现 AGENTS.md 的 project-direction fallback。真实关系见 graph，ideation 仍需读本项目 AGENTS.md；详情与处理边界记录在 lint report。
- 用户要求在 Research 下创建 agentic-opd 并安装 ARIS。
- 检查发现目录与 ARIS 安装清单已于 2026-10-12 存在，但没有项目研究文件。
- 本次按 Research 标准模板补齐项目范围、memory、queue、收录规则、taxonomy、L1 模板与 helper。
- 初始化时沿用 5 个 ARIS Codex skills 和共享依赖；源码 commit：`26b95cfa0d8747078e9e43b42e20952709e561b8`。
- 初始化阶段未开展文献检索、旧资料迁移、idea 生成或实验；本轮已完成上述单篇 wiki 试入库，queue 和正式 cards 仍为空。

## 研究范围

- 多轮 Agent / tool-use 场景的 on-policy distillation；暂以 student rollout、teacher supervision、distillation update 为核心。
- 重点关注 prefix / state coverage、rollout depth、teacher intervention、loss allocation、action boundary、termination 和评测成本。
- 邻近分工：通用 OPD → `../opd/`；reward / policy optimization → `../agentic-rl/`；数据机制 → `../agent-data/`。
- 这些是初始化范围，后续按用户选题收窄。

## 当前入口

- `README.md`：项目与 ARIS 恢复入口，含 wiki 与 TCOD 样例链接。
- `synthesis/seed-sources.md`：已有本地资料链接；其结论需按原文重新核验。
- `research-wiki/index.md`：当前启用的知识页面入口。
- 旧 queue / acceptance rules / card helper 已停用，保留作历史参考。

## 后续工作

当前选题入口为`idea-stage/atod-ideas-2026-10-19.md`，领域入口仍为`research-wiki/gap_map.md`。用户尚未选择具体方法，不自动继续research-refine或实验。旧`idea-stage/IDEA_REPORT.md`及16个pending ideas保留为历史参考，不视为用户已接受方向。Query pack的gap部分只读取gap map前1200字符，论文部分按文件名取至多12篇再截断；不能把query pack当全量目录或排序。
