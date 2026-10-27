# G15 方法候选生成输入
日期：2026-10-15。用户已确认只使用 L1、L2、L5；先前“五个全部保留”已被替代。

## 研究目标与边界
研究多个 teacher 在一个可部署 student 中的学习收益兼容：A/B 的预算竞争、相对支配/抵消、获得与保留、联合与顺序整合。目标是有实质贡献、可规模化的顶会方法论文；诊断服务于方法。给定 gap 是研究问题，不是已证实瓶颈或新颖性声明。不要转向 G16 异源专长接口、G17 同题联合能力使用、G18 新teacher选择。不要跑训练、写其它项目或修改上游 skills。
跳过 Phase0/1：不加载 query_pack、不扫描全库、不重建 landscape。候选后可定向查新。

## 已有 lit 输入与已核对事实
已有背景来自 research-wiki/gap_map.md 的 G15、synthesis/mopd-gap-analysis.md 的§1和G15、synthesis/mopd-literature-review.md的跨论文综合及指标/成本口径，七篇直接论文页与同版原文相关方法段已读取。
- Open-MOPD（2608.19098v1）§3.2/§4：token-share/gap allocation/reward refresh；该3B recipe中IF prompts约20%而gradient tokens约1%。teacher token logprob极差>1nat仅0.62%，mask这些tokens/平均target无益。这不能排除参数干扰。refresh不改变已采样prefix。
- DN-MOPD（2609.35347v1）Algorithm1/App.C.6/E.2：clip(sigma_all/sigma_d,.25,4)校准logratio dispersion，不改prompt采样；response内token-average再response-average。IF初始梯度贡献高与Open不构成矛盾；9B/4B固定近似权重可比，2B动态估计更好；早期Qwen3-4B无明确收益。
- D³（2608.24987v2）§3/App.I：EMA相对KL×下降速度调prompt采样；KL反弹使未学完域预算降floor已有可选velocity-floor补丁，不能将修复KL反弹称为新。必须看single-checkpoint而非per-benchmark peaks。
- Gradients→Capabilities（2610.02179v1）§3–5：DT/DR gradient cosine .68，经同Adam state更新 .96；BF16 delta稀疏不能证明学习稀疏。局部梯度/实际更新一致性不能直接说明长期能力。
- PMOPD（2609.34605v1）§4/Table4：task ordering/cycling，block cumulative realized update的rank16子空间，双投影gradient与Adafactor update，每cycle重建memory。已覆盖顺序/历史子空间保护。
- Road（2610.13521v1）§3.3：辅助teachers在主域student trajectories评分，token agreement +逐tensor部分梯度投影+主梯度norm floor，之后AdamW。同轨迹auxiliary loss不是auxiliary本域训练loss。
- UP（2610.08398v1）§2.3/Table1：AdamW产生candidate displacement，联合QP保证各active-domain当前batch一阶loss不增；保留原optimizer state，不保证有限步或benchmark单调。general teacher用DAPO数学prompts，因此IFEval残差不能直接归因保护失败。完整step约1.42×，不能只算QP成本。
以上为作者报告/原文核对；剩余独立且高价值方法瓶颈尚未确证。强固定权重、归一化、调度、投影、更相关数据都可能足够。

## 已确认 lenses
L1 相互改变的可学性：相同数量、尺度的B监督，其边际收益是否随已学A变化，且不能由剩余能力空间解释？A/B是否改变彼此学习条件？警惕只是新proxy动态权重。
L2 自采样中的反馈闭环：B改变student后是否改变A下一轮实际看到的轨迹，使A有效学习机会减少，即便名义预算/尺度不变？只关注跨teacher改变对方监督机会，警惕普通探索/rollout freshness重命名。
L5 局部保护与全程可达性：每步保护A能否到达较好的最终A/B能力组合？暂时取舍是否必要、可恢复？区分路径限制与容量/目标真实冲突，警惕只调松UP阈值或换proxy。

## 生成规范
每个独立shard按指定lens提出3个具体方法候选，总池约9个/模型。核心一个机制、2–4个可执行步骤，可有高风险，不把有邻近工作当排除理由。不要堆新模块拯救薄弱新意；生成不排序、不淘汰。注明假设、可证伪信号、最近邻、成本与实现难点；没有实验结果不写任何收益数字。
输出紧凑JSON，字段 shard_id, model, candidates[]。每项字段 id,lens,title,method(2–4步),hypothesis,core_claims(3条，含机制/差异/可检验结果),minimum_experiment,positive_negative_null,closest_known_work,named_risk,compute_assumptions_and_estimate,effort,contribution_type,dedup_key。每项约400–650中文字。
最小实验是待运行提案；实际GPU预算未给出，不能把默认8×3090或2h当用户已有资源。可按现有1.5–3B/少步短序列给估算范围，但明确吞吐未测、完整成本含rollout/scoring/replay。不要因本目录不跑训练将idea判不可行。
不要另行联网查新、不加载其它gap、只读不写、不派子agent。
