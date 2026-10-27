# ATOD 论文驱动选题：2026-10-19 查新证据

以下为原文阅读摘要，均未独立复现实验；题目相邻不等于撞题。主论文 ATOD v6 正文§1–6、附录A–D、表1–4、图1–13均已阅读（图1–8的SVG转图检查；其余为HTML文本图）。原文HTML缓存只作本次阅读，非新paper card。

## 核对过方法节的近邻

- OG-OPD，2609.35319v1，§3：选一轮恢复环境、比较teacher action与原student action后的paired student continuation最终结果；只在teacher rescue时提高原student tokens的监督权重。teacher harm不触发降权；额外continuation不直接作训练目标。https://arxiv.org/html/2609.35319v1#S3
- GammaOPD，2609.16937v2，§3：推导sequence reverse-KL的未来log-ratio信用，折扣未来token信用；RBM把teacher项有界化，与verifiable ±1 reward结合保证标签符号。仅将未来KL累加不新。https://arxiv.org/html/2609.16937v2#S3
- RA/CoRA，2610.11519v1，§2：teacher–student probability residual作有界即时reward，减student state baseline，再response内去均值后加verifier advantage；CoRA在同一student scored batch上用verifier advantage更新teacher LoRA。零均值标签不保证梯度与RL正交。https://arxiv.org/html/2610.11519v1#S2
- JOLT，2610.10447v1，§2：理论上的reward-consistent teacher应按student自身advantage作指数倾斜；实际teacher训练用teacher rollout reward + 向student KL的surrogate。共享参数/privileged self-teacher，项目不收此类方法但查新不能排除。https://arxiv.org/html/2610.10447v1#S2
- SERL，2605.19447v1，§3：训练时teacher看environment hindsight；按step或相似state anchor放置反馈；teacher log gap有界重加权action tokens的GRPO优势，另加action-only distillation。https://arxiv.org/html/2605.19447v1#S3
- SOPD，2608.16333v1，§4：完整student rollout之后在每个记录的step起点并行生成独立teacher step；目标不改变环境轨迹，用packed attention、step-balanced CE训练。https://arxiv.org/html/2608.16333v1#S4
- ActionOPD，2610.19820v1，§2：以语义action匹配替代token模仿；每state采3个teacher/4个student回复，对student自己的reasoning+action作组相对PG，执行最高匹配action。含matcher、采样和state-selection开销。https://arxiv.org/html/2610.19820v1#S2
- ActFirst-OPD，2609.36608v1，§4：reference next observation条件下student生成fast action推进环境，失配后回退自主fast action；完整think-act回复异步生成，仅作OPD不执行。https://arxiv.org/html/2609.36608v1#S4
- GC-OPD，2609.37522v1，§3：离线teacher execution graph保留原始source history，按当前/历史state检索成功suffix相关完整record，结合student hindsight增强teacher scoring context。相同物理state不必有相同belief/history。https://arxiv.org/html/2609.37522v1#S3
- SCOUT，2609.38360v1，§3：周期性从student prefix采teacher continuation，用verifiable reward RL更新teacher，再给student作OPD。优化teacher continuation成功≠直接优化student continuation成功。https://arxiv.org/html/2609.38360v1#S3

## 仅核对摘要/元数据的覆盖提醒

- vOPD，2605.07865：在OPD policy gradient中减闭式negative reverse KL state baseline，以降低OPD梯度方差；不要误判为已经用teacher给纯task-RL构建action-dependent control variate，优化目标不同。https://arxiv.org/abs/2605.07865
- Prospective Hindsight，2610.02740：prospective prediction与retrospective evaluation的surprise重加权；覆盖误校准但不直接等于隐状态belief posterior蒸馏。https://arxiv.org/abs/2610.02740
- Q-Prop/action-dependent control variates、GAIL、potential shaping、hierarchical options为必须对照的经典机制；本次还未逐篇读完，不能主张这些机制首次提出。

## 与本项目旧候选的关系

用户此前未接受旧16项。SOL-01与旧counterfactual-observation-action-contrast/response-relation、SOL-03与effect-quotient-distillation、ASTRA-04/SOL-04与temporal-contract-trajectory-supervision、ASTRA-05/SOL-02与evidence-belief-ledger-transfer、ASTRA-06与teacher-evidence-bottleneck存在明显方向延续。可以深入，不能称为本轮全新发现，也不能用自己的旧idea作为prior-art证据。

- ThinkOPD，2609.37044v1：privileged teacher think trace与student response的兼容性、group-relative benefit共同路由。https://arxiv.org/abs/2609.37044
- STI-OPD，2610.10878：discrepancy概率介入+importance-weighted reverse KL。https://arxiv.org/abs/2610.10878
- UECR-GRPO，2609.28385：teacher/verifier路径utility混合以及entropy校准、零和且保符号的credit redistribution。https://arxiv.org/abs/2609.28385
- DiffGate，2610.04596：只在失败轨迹、按group难度加入有界teacher guidance。https://arxiv.org/abs/2610.04596
- Cal-OPD，2609.21619：通过正负privileged interventions估计teacher自身偏差区间并校准student-teacher gap。https://arxiv.org/abs/2609.21619
- IG校准搜索OPD，2610.20664：按检索后information gain校准turn监督预算和query preference，实验为多模态搜索；范围排除不意味着机制可主张新颖。https://arxiv.org/abs/2610.20664
- RouteOPD，2609.08337：student-excess到teacher-deficit token的显式pairwise probability transport。https://arxiv.org/abs/2609.08337
- Demystifying OPD，2610.19145：controlled token flips检验teacher correction收益；当前仅诊断摘要。https://arxiv.org/abs/2610.19145
- 已有wiki的DGPO、FutureBridge、TCOD、MemOPD、TurnOPD、DASH等仍为baseline候选；未把库内未收录当作全领域空白。

## ATOD 尚未分离的因素（本次解释）

1. w∈[0,1]导致轮间分配与总体OPD强度同时变化；缺同teacher梯度/同mean-weight/random-permutation对照。
2. min–max是相对排序，不是绝对可学习性/teacher可靠性；同一轮权重可因其他轮的极值改变。
3. sampled surprisal与absolute log ratio的集中界不证明任务价值；附录已明确d不是无偏KL，因此不能把这点当作者数学错误。
4. 深轮次诊断是条件在尚未结束的episode上；样本数随深度下降，训练前后组成不同。不能凭此证明深轮次因果更重要。
5. 主表按150更新步而非总compute报告；主表/消融未报告跨seed误差；Search-QA最长4轮。长度均值不等于成本或效率保证。
6. teacher可靠性、跨family、multimodal是附录已承认的局限；简单加gate/换family不构成新发现。

边界：针对性查新而非穷尽全领域；没有运行pilot；近邻预印本也可能构成prior art；所有idea仍是provisional。

## 最终审阅补充与阅读层级更新

- vOPD §3已由fresh reviewer读原文，Q-Prop核心估计式由父agent核对；两者分别是OPD state baseline与经典task-PG action-dependent control variate。不能主张control variate恒等式的新颖性。https://arxiv.org/html/2605.07865#S3 ; https://arxiv.org/abs/1611.02247
- ASL 2506.17697v3 §§3.2–3.3及相关附录由fresh reviewer核对：以S(a)=T(s,a)定义转移等价集合，使用world model预测变化与相似度近似；含teacher-reference action结合环境reward的RL及text-only实验。SOL-03仍有真实转移纠正假等价这一差异，不能主张首次效果等价蒸馏。https://arxiv.org/html/2506.17697v3#S3
- GAD 2511.10643v3 §2由fresh reviewer核对：同prompt teacher/student pair，判别器奖励，在线student负样本与GRPO。强覆盖SOL-08核心。https://arxiv.org/html/2511.10643v3#S2
- Privileged POMDP 2412.00985v3 §§3、5父agent核对：全知expert action蒸馏在部分可观测问题上的失败，belief-weighted asymmetric actor-critic与近似belief学习。不是本轮A05的直接LLM实现，但belief learning本身明确已有。https://arxiv.org/html/2412.00985v3#S3
- Meta-RL as task inference 1905.06424：仅读摘要，利用privileged信息分别学习task belief与policy，是A05必须进一步对照的经典近邻。https://arxiv.org/abs/1905.06424
- Belief-Aware GSAC 2605.26155：仅读摘要，uncertainty调节蒸馏系数；严重遮挡下ensemble预测partial observation可能漏掉缺失信息，作者提出full-state预测修正但未验证。不能把此论文误称belief posterior蒸馏的直接实现。https://arxiv.org/abs/2605.26155

最终保留A05/A03两条主候选，A01仅作靶点验证储备。父agent将所有新颖性结论保留为provisional，未沿用reviewer对MemOPD的“普通摘要”简化。最终边界与方法见`idea-stage/atod-ideas-2026-10-19.md`；旧16项用户未接受，本轮也未替用户选定课题。
