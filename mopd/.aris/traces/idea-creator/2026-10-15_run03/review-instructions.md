# G17 candidate-level novelty verification and critical review

你是研究审阅者。只评价任务指定的候选ID，不评价自己生成的候选。读取候选原始方法、输入证据及原论文，不接受主协作者对质量的预设结论。由于当前运行时拒绝新建agent，本次复用上下文，必须记录 review_independence=same-family、acceptance_status=provisional、context_reused=true；不得宣称fresh-context或跨family接受。

## 输入与范围

- 主候选：/home/chy/notes/Research/mopd/synthesis/g17-idea-candidates.json（仅读取分配给你的四项）。
- 用户问题和已有方法边界：/home/chy/notes/Research/mopd/synthesis/g17-idea-lenses.md 的输入及L1/L2/L3；/home/chy/notes/Research/mopd/synthesis/mopd-gap-analysis.md 的G17。
- 已发现来源：/home/chy/notes/Research/mopd/synthesis/g17-novelty-evidence.md。B条目是已核对输入，N条目主要是检索线索，不是已裁决证据。须核查承重原文。
- 用户目标是可规模化方法论文，诊断服务方法。不要把benchmark缺失当作失败或方法必要性；也不要要求已跑pilot才允许给出候选。
- 不训练、不长推理、不安装软件、不读query_pack、不重建landscape、不修改其他项目或主报告/wiki/STATE。你不是唯一协作者，不覆盖他人修改。

## 逐候选任务

1. 提取3个承重技术claims（机制、信号及区别于直接baseline的增量）。对每项claim尝试至少3种针对性检索表述；可以跨候选复用相同claim的查询，但必须说明映射。覆盖当前可用web及arXiv、顶会官方来源（2025–2026和近六个月，以及必要旧工作），不要只依赖本地种子。数据库不可用需如实说明，不能伪造搜索。
2. 检索先在工具内部筛选，只阅读高相关原论文方法段，记录title/URL/section或equation及是否仅abstract。不能将二手摘要当成直接覆盖证据。每个候选给最近1–3篇工作的精确重合、剩余delta及需要验证条件。
3. 数学/实现核查：目标分布是否定义清楚，是否重复计算sampling proposal、错把已条件化/teacher-roll-in分布叫完整on-policy，是否依赖免费oracle；teacher pool是否确有信息足以联合解题，是否额外提供完整答案；不要替候选新增模块。
4. 批判审阅：最强成立理由、最强reviewer objection、最可能失败、两年后的价值/更强frontier下是否仍成立、指标可被game的方式、公平baseline与总compute。novelty与方法价值分开：邻近不是淘汰依据，简单known方法的直接复现也不能冒称新method。
5. 给每候选 novelty_verdict、novelty_score（5=有可辩护delta值得pilot）、method_value_score、pilot_information_score（0–10，仅定性排序辅助）、risk、recommendation（prioritize/reserve/deprioritize）。不要重写方法，缺陷以named risk记录。
6. Pilot 不运行。只给一个最便宜的可证伪检查，并指出实际GPU预算未指定、tokens estimates未测速；不要捏造小时或实验结果。

=== NOVELTY VERDICT LIMITS (these bound how you judge, never how widely you search) ===
Search exhaustively; judge calibrated. Two failures waste months equally:
passing an idea a published paper already contains, and killing a viable idea
because the territory has neighbors.
1. Proximity is information, not a verdict. Someone working nearby goes in the
   report; it is not by itself a reason to reject.
2. ABANDON has exactly one qualification: a specific published paper already
   contains this result — name that paper. No named paper, no ABANDON.
3. Crowded-but-deltaed is PROCEED: state the delta in one sentence a reviewer
   could verify. Thin or contested delta is PROCEED WITH CAUTION — say what
   would make it carry, not why it should die. CAUTION is not a safe middle:
   if you cannot name the specific thing that makes the delta thin, the
   verdict is PROCEED.
4. Concurrent or competing work is not a veto. That is a race — report it and
   let the user decide whether to run it.
5. A direct attack on a central problem is legitimate novelty when nobody has
   executed it well. \"This area is hot\" does not mean \"this area is taken.\"
6. This check is an early gate, never the last one — more triage, pilots, or
   external review still stand between any idea and a paper, whatever order
   this run uses. A wrongly passed idea dies cheaply at one of them; a wrongly
   killed idea is never seen again. When torn between two verdicts, choose the
   more permissive one.
Say plainly when an idea clears the check. Do not manufacture overlap.

## 输出

你只拥有本次分配的trace响应文件。完成搜索和审阅后，把完整结构化JSON保存到该文件（独占输出，不能修改共享候选或证据文件）；检查可解析。JSON schema：
{
  shard_id, assigned_ids, reviewer_model:"gpt-6-astra", review_independence:"same-family", acceptance_status:"provisional", context_reused:true,
  search_log:[{candidate_ids,claim,queries:[...],sources_checked:[url...]}],
  sources:[{source_id,title,url,anchors,read_depth:"method|abstract|full",finding}],
  reviews:[{id,core_claims:[...],closest_work:[{source_id,overlap,delta}],technical_issues:[...],novelty_verdict,novelty_score,method_value_score,pilot_information_score,risk,recommendation,best_case,strongest_objection,likely_failure,frontier_durability,metric_gaming,fair_baselines,minimum_test,kill_criterion}],
  ranking:[ids],top_choice_rationale,high_upside_choice,coverage_limits:[...]
}

最终聊天回复只给：文件路径、四项简短verdict/排序、最关键2–3个来源或发现（≤1200中文字符）。完整细节留在trace文件供主协作者直接读取，避免大量raw搜索回灌。

