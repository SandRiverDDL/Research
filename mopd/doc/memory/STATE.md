# MOPD 当前状态

> 更新：2026-10-16。当前用户要求优先于历史综合与自动摘要。

> 本文件包含 G15、G17 的不同 chat 记录；恢复任务时按当前用户指定的 gap 读取，不把另一 chat 的“本轮”或助手建议当作当前授权。

## 方法地图、阅读顺序与同期对照核查（2026-10-16，已完成）

- 用户询问已收集MOPD方法主要内容、如何高效阅读，以及是否实际对比同期MOPD方法。复用36篇现有笔记和综合，不生成新idea或实验方案。
- 交付：`synthesis/mopd-methods-and-reading-guide.md`，含共同训练骨架、36篇按主要贡献归组、5篇首轮关键段路线与按问题补读、10分钟差异阅读模板，以及6篇论文的明确同期实验对照。阅读预算是建议，不是实测时间；排序是覆盖机制，不是质量或novelty排名。
- 本轮36/36版本化原文HTML访问成功，只做表格/baseline段定点检索，未全文精读。原文已确认：Router/PMOPD/UP比Open-MOPD；UCMOPD比CaMOPD；Road比Open/Ca；SF在视觉语言8B block比Open等。Trust使用Open代码实现的MOPD行不自动算完整Open改进对比；DN的Dynamic router不自动等于Trust/Router复现；IM主要比较初始化/merge timing。UP Table 2星号引用数与本地复现须分清。
- 证据：`notes/mopd-baseline-audit.json`、`notes/mopd-baseline-table-checks.json`。机械候选已修正Math-OPD误匹配H-OPD；候选中的引用/abstract命中不是实测关系。未列出的比较保持未核实，不断言不存在；不跨设置比较recovery百分比。
- 新鲜验证PASS：36篇各归组一次、6条比较表行、全部本地链接有效。没有改论文页、写新idea/实验计划或运行实验，环境无语音命令。

## 会议索引下载与录用复核（2026-10-16，已完成）

- 用户要求下载今年顶会索引，并直接在索引中检索已有MOPD论文，同时检查会议版改标题的可能性。当前覆盖与项目直接相关的ICLR/ICML/NeurIPS/ACL/EMNLP 2026；复用共享 `../literature-index/tmp/` 的已有官方缓存，补充下载和匹配产物保存在本项目，不修改共享脚本或已有缓存。
- 已下载10份官方JSON/XML/CSV至 `notes/conference-index-2026/raw/`，无最终下载失败或旧缓存fallback；规范化索引 `papers.jsonl` 共28,278条去重记录：ICLR 5,575、ICML 6,563、NeurIPS 6,070、ACL 4,459、EMNLP 5,611。特殊track/Findings分别标注，workshop合集未下载。本机共享papers.sqlite不存在，共享脚本和旧缓存未修改。
- 已按完整标题规范化、可用arXiv标识符和作者/近似候选复核36篇。确认3篇主会Poster：AVSD（NeurIPS，fRtcETLCZ2）、H-OPD（EMNLP，572-MAIN）、CaMOPD（EMNLP，6445-MAIN）。已更新 `synthesis/mopd-publication-status.md`；此前1篇官方+1篇作者标注的统计已被本轮替代。
- 新下载NeurIPS metadata包含旧缓存没有的AVSD；EMNLP官方日程补足H-OPD主会类别及CaMOPD录用证据。代表性作者/近似误匹配已区分：Trust/Data-Free OPD vs SimCT、IM-MOPD vs MTM、Consolidating RLVR vs EffOPD、Video-MOPD vs MosaicAudio。未确认额外改名录用，33篇保持未确认；EMNLP无作者/摘要、每篇仅保留少量近似候选，不能完全排除改名漏检。4个定向OpenReview notes API请求403，已记录，不当作否定证据。
- 复用入口：`notes/conference-index-2026/README.md`；下载/本地检索脚本 `scripts/check-conference-acceptance.py`；36篇匹配候选 `mopd-matches.json`；来源/哈希 `sources.json`。验证PASS：10来源哈希、28,278唯一记录、36输入、3完整标题命中，检索H-OPD/AVSD各返回正确记录。所有36篇论文页未改，环境无可用语音命令。

## 33篇首次发布与投稿状态复核（2026-10-16，已完成）

- 用户要求解释33篇未确认主会录用论文是新发布/待录用还是投稿未中。已核对33/33 arXiv v1日期（UTC提交时间口径）：5月2、6月3、7月2、8月6、9月13、10月7；20/33于9–10月首次提交，31/33晚于5月25日。arXiv发布时间不等于会议投稿时间，不能仅按deadline推断未投或被拒。
- 已查公开OpenReview search API（21次查询，无失败）：18篇ICLR 2027 Submission、1篇ARR 2026 October Submission；Uni-OPD及Rethinking Self-Distillation for Multi-Teacher Capability Merging为ICLR 2027 Desk Rejected Submission；MOPD原论文及ACLArena有workshop记录，尚未独立核对workshop decision；其余10篇会议状态未核实，其中Every Coin Has Two Sides仅作者标注Under Review。未找到可确认的外审Reject记录，不等于证明历史无拒稿。
- 交付：`synthesis/mopd-release-and-submission-status.md`，33篇逐项v1日期、当前状态和来源；原publication-status报告已链接本次结果。证据缓存：`notes/conference-index-2026/arxiv-first-release.json`、`submission-status-search.json`、`release-and-submission-summary.json`。公开forum网页有浏览器验证/读取失败，状态取官方公开API元数据，不声称读过decision全文或猜desk rejection原因。验证PASS：33唯一论文/v1日期、月份总数33、状态18+1+2+2+10=33，本地链接通过；论文页未改。
- 用户进一步希望用ICLR评分参考录用前景。已核对ICLR 2027官方Reviewer Guide：初评计划2026-11-05释出、作者讨论11-05至11-18、reviewer最终推荐11-25。截至10-16尚未到计划释出时间，未取得公开评分，不给18篇作评分排序或把未知当零分。TrustMOPD公开forum notes API返回403，search API只返回submission元数据，无rating；不能将访问失败说成逐篇无评审。报告已补此时间边界，未创建提醒或自动任务。

## 论文录用状态核查（2026-10-16，上一轮结果待索引复核更新）

- 用户询问已收集MOPD论文的录用与顶会情况；范围为36篇现有论文，不扩展搜集、不进入idea流程。
- 逐篇核对最新arXiv元数据，并与NeurIPS/ICLR 2026官方目录、ACL 2026论文集按完整标题匹配及定向检索。1篇官方记录：AVSD，NeurIPS 2026 Poster；1篇作者侧标注：H-OPD，EMNLP2026，录用及Main/Findings尚未独立确认；其余34篇未核实录用，其中2篇arXiv明示Under Review。未知不等于未录用或被拒。
- 交付：`synthesis/mopd-publication-status.md`，含36篇逐项状态、来源和覆盖限制。ICML完整目录及AVSD独立poster页抓取失败，EMNLP可读主会页无论文表，Findings尝试路径404；不声称全部会议穷尽核查。36篇论文页未改，报告36个唯一arXiv ID与1/1/34统计检查通过。环境无可用语音命令。

## G15 idea 生成（2026-10-15，已完成）

- 用户调用 `idea-creator-from-gap`，基于既有lit为G15「多teacher学习收益兼容」生成方法idea。最新明确选择 **L1＋L2＋L5**，替代此前全选/暂停讨论；不包含L3/L4独立分支，不扩展到G16–G18。
- 已按patch跳过Phase 0/1：未加载query_pack、未扫全库、未重建landscape。复用G15 gap map、主报告完整分析、综述及七篇直接论文页，并定点核对原文方法与边界。
- 生成与评估完成：Astra和GPT-6.1-sol分别按三个lenses生成18候选，机械合并13组；全部进入定向查新和fresh Astra xhigh审阅，没有质量预筛或完整覆盖意义上的ABANDON。最终 **C07修复算子终点保护 → C03学习方向输运 → C04-S4机会质量约束**；前两项主推荐，S4须先通过区域定义/概率估计有效性门槛。A4不能继承S4判定；C02分数经终评由3校准为4，不因子机制等价判完整候选已覆盖。
- 主报告：`synthesis/g15-idea-report.md`；证据/章节/查询缺口：`synthesis/g15-novelty-evidence.md`。18原始变体、完整生成/审阅请求与输出、查新记录和验证：`.aris/traces/idea-creator/2026-10-15_run02/`。审阅为same-family provisional，非独立外部同行确认。
- Wiki helper已登记13组：3 proposed、10 archived，全部outcome=pending；archived仅表示本轮未优先，不是负实验或永久禁选。连接已有paper IDs与G15，未新造paper/gap IDs。未改36篇论文页。
- 新鲜结构检查PASS：15份G15报告/wiki页面、61条本地链接；候选13组/18变体完整，graph无重复/悬空，36论文页哈希未变。详情 `g15-validation.json`。共享wiki统计还包含另一chat的idea，不把全局总数算作G15产出。
- **Pilot未运行，训练GPU使用0小时，资源/吞吐未确认。** 所有科学前提与规模收益待验证；报告给出最低判别设计和条件成本公式，不是完整实验计划。当前任务已交付；尚未授权训练、跨目录实验或完整方案细化。只修改当前任务必要产物，保留G17 chat内容。环境无可用语音命令，无法语音通知。

## G17 任务与完成状态（2026-10-15）

- **2026-10-17最新反馈与修订：** 用户认为此前几个候选主要是student/teacher续写或额外局部监督，缺乏足够创新，且修改训练框架、影响吞吐。已撤回L3-A2、L1-A1的优先推荐和L1-A4的高风险储备推荐；目前无合格主推荐，不从其余候选自动补位。优先兼容既有rollout及批量teacher评分流程，把吞吐和框架侵入性前置筛选；不擅自扩大为用户要求绝对零新增计算／零改动。
- 本次只修正报告与三条wiki状态，不启动新idea生成或实验。三条改为archived、outcome仍pending，原因是方法价值与工程代价不匹配，非完整scoop、实验失败或吞吐实测。报告顶部的2026-10-17判断优先于下方历史排序。

- 当前任务（2026-10-15）：用户明确调用 `idea-creator-from-gap`，基于 G17 及已有 lit 成果生成有实质贡献、可规模化的顶会方法 idea；区分可解样本覆盖与同题联合使用。给定 gap 不视为已证实或已通过查新。
- 本次跳过上游 Phase 0/1，不加载 query_pack、不扫描本地论文库、不重建 landscape；保留已有 lit 输入准备、后续定向查新及审阅。用户要求先生成 lenses 并确认使用哪些，再生成具体方法候选；该确认条件来自用户调用的 patch skill。
- 输入准备已完成：读取状态、索引、G17 gap map、`synthesis/mopd-gap-analysis.md` 第1节及G17、六篇直接证据论文页；定点核对 Trust v3、TU-OPD v1、H-OPD v3、SMOPD v2、AVSD v1、MAD-OPD v1 的原文 HTML 方法。Trust另核对eval、response-level对照及限制。非全文复读、非候选查新。Off-vs-On理论仅补读已有笔记。
- 已由 GPT-6-Astra（xhigh、fresh secondary agent）生成六个 analytic lenses：L1整题正确门槛、L2联合状态可达性、L3跨步骤依赖保留、L4专长间中间结果兼容、L5协作增量压缩、L6关系组合泛化。完整输入、边界和反证条件：`synthesis/g17-idea-lenses.md`；原始输出与trace：`.aris/traces/idea-creator/2026-10-15_run01/`。
- 最新用户确认（2026-10-15）：选择 G17 的 L1、L2、L3；L4–L6 不作为本轮独立生成 lenses。该选择对应的方法生成、机械去重、定向查新、批判审阅、推荐报告及必要 wiki 写回均已完成。Pilot 不运行；训练、跨目录实验和完整方案细化/实验规划仍未授权。
- 本轮交付：`synthesis/g17-idea-report.md`；原始12项 `synthesis/g17-idea-candidates.json`；承重原文与边界 `synthesis/g17-novelty-evidence.md`；完整trace `.aris/traces/idea-creator/2026-10-15_run03/`。三个 Astra xhigh生成分支各4项，机械去重后仍12项、无质量预筛；三个交叉审阅分支日志共136条查询（含追踪检索）并核承重方法段，12/12完成查新与审阅。
- 排序：优先L3-A2跨步骤交叉比蒸馏、L1-A1认证局部动作联合蒸馏；L1-A4联合教学增益作为高风险储备。其余具体安排见报告。两项PROCEED、十项CAUTION，无ABANDON；不存在普遍组合失败或顶会贡献已成立的结论。
- Wiki已通过ARIS helper记录12项，8 proposed、4 archived，全部outcome=pending；archived仅表示本轮降低投入优先级，不是实验否定或完整scoop。没有新增实验或已证实claim。第二生成模型本轮未成功启动；三个已有Astra上下文交叉审阅，context_reused=true，same-family provisional；不能恢复成双模型生成或fresh/cross-family接受。
- 查新收窄：VG-OPD本已按criterion许可，不要求整题正确；TCOD-B2F/BranchOPD覆盖前缀撤除与共享前缀分支，HIR包含中间输出重标记，γOPD包含return-to-go。两个优先候选仍须分别排除同数据KD收益、错误交叉关系，以及无关但正确的局部动作；原交叉比clip还可能破坏目标兼容性。
- 本轮新鲜验证PASS：12/12审阅覆盖、12条idea outcome均pending、本地链接及143条graph关系通过；107条原关系保留、9篇直接输入论文页未改。记录见run03/validation.json。未做实验或外部链接整站验证。
- 关键证据边界：TU-OPD要求至少一个teacher整题达到可靠性阈值，但Trust/H-OPD没有相同门槛；Trust已有位置变化和组合训练证据，其98% recovery不是同题端到端组合率；H-OPD信息桥接、SMOPD多目标、AVSD residual与MAD-OPD交互监督均须视为已有覆盖。普遍组合失败及新方法必要性仍未成立。
- 已按用户确认的多 teacher 相关性筛选完成修订，主报告与入口均收敛为四个问题主题；本地结构、链接与派生摘要检查通过。
- 处理规则：原1/6剔除；原2/3只保留跨 teacher 相互作用并合并；原4仅保留多来源专长兼容组合；原5保留并区分覆盖与同题联合使用；原7保留新增 teacher 的边际价值，删除泛化成本统计诉求。
- “MOPD特有”仅指关键问题来自多个 teacher 的选择、交互或整合；可与离线多教师蒸馏、模型合并共享。四项仅通过相关性筛选，尚未认定为高价值 gap。①②仍需限定条件，③④多 teacher 属性更直接。
- 上一轮仅确认范围修订；本轮已明确选择上述互补使用问题并授权 idea 生成，后续对助手添加的 lenses 确认环节提出质疑。未运行方案细化、实验规划或训练。

## 当前交付与判断

- 主报告：synthesis/mopd-gap-analysis.md。保留36篇文献图景，当前四个问题主题为 G15–G18：①多 teacher 学习收益兼容；②多来源专长兼容组合；③互补能力在单一 student 中的使用；④新增 teacher 的边际价值。
- G前缀沿用wiki ID约定，不代表已成立的gap；不作优先级、方法必要性或novelty声明。
- G1–G14及旧graph边均保留历史语义。原七项G8–G14已退出当前集合；报告文末保留处理表与旧锚点。不能从历史边或历史log恢复旧七项为当前gap。
- 同步入口：research-wiki/gap_map.md、research-wiki/topics/multi-teacher-opd.md、synthesis/mopd-literature-review.md、README.md；关系与query_pack使用ARIS helper维护。
- 通用OPD、持续学习、接口迁移和成本比较仍可作为背景或对照，不因保留相关论文而自动成为核心gap。

## 四主题修订的历史来源与验证边界

- 文献图景来自先前对36篇本地论文页（15 seed、21补搜）的综合；本次按用户提供的筛选结论修订，未重新逐篇阅读。论文页为先前的二手阅读笔记，36篇不是穷尽覆盖。
- 区分作者报告、本地解释与待验证假设。引用到本地页及其中已有原文章节/公式/图表入口；本次没有新原文核查、远端链接验证或实验复现。
- 本次新鲜验证PASS：四个当前主题及摘要一致；报告仍引用36/36论文，36篇论文页哈希未变；本地链接/锚点无失效；107条graph关系无重复/悬空，原95条逐字保留、新增12条当前部分覆盖关系。详情见research-wiki/LINT_REPORT.md；历史.source-check-report.json与.wiki-coverage-report.json均不冒充本次新鲜核查。
- query_pack由helper按gap_map前1200字符截取；必须包含全部四个当前主题，不表示重要性排序。完整判断以gap_map与报告为准。

## 后续授权边界

- 原始任务已授权按 `idea-creator-from-gap` 生成候选、定向查新、审阅和必要报告/wiki 写回；后续须执行 patch 中的 lenses 确认步骤。本次另明确授权修改根目录的该 patch skill；尚未授权训练、其他跨目录写入或完整方案细化/实验规划。Pilot 不运行，须标注未验证。
- 继续研究时使用本项目ARIS wiki，不启用另一套queue/card pipeline；只修改当前任务所需的项目文件，不修改论文页、上游skills或其他主题。
