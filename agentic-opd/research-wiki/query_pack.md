# Research Wiki Query Pack

_Auto-generated. Do not edit._

## Open Gaps
# Gap Map

2026-10-15 重建。依据现有24篇论文；以下是库内证据支持的开放问题，不是全领域查新结论，也不是已选定的idea。原16个pending ideas不作为证据。

## 当前摘要

五个方法层面的gap，编号保留历史兼容性，顺序不代表排名：

- **G1｜错误恢复与交互成本。** 低成本prefix replay／短rollout与真实student错误状态覆盖之间，仍缺少可靠的兼顾方式；最终要改善自主恢复能力。
- **G2｜纠错与自主探索。** disagreement、confidence、teacher preference不能直接判定何时该纠错、何时该保留有效探索；选择性监督已有方法，剩余问题是让选择服务实际任务收益。
- **G5｜跨轮任务信用。** token／turn匹配、深度加权及OPD＋RL已有覆盖；开放问题是无专用solver时，如何把延迟任务后果变成有效的teacher监督，而非只更像teacher。
- **G6｜新程序知识迁移。** teacher会做不等于student能通过OPD学会；不同有效操作路径可能造成负迁移。需要区分已有规划模式强化与新技能获取。
- **G7｜多专家能力整合。** 路由、debate和顺序蒸馏已有覆盖；仍需在有限student容量与训练预算下，兼顾新增能力、旧能力保留和跨域组合。

**G3**拆为监督接口前提与G7，不再混作一个方法gap；**G4**改作全体gap共同的成本／评测约束。G1/G2有多篇直接方法证据；G6/G7有受控机制证据但真实环境外推有限；G5更偏研究假设。均不预设逐状态probe、环境分叉或额外judge是解法。

完整论据、已有覆盖、降级条件及24篇对应关系见下文；压缩query pack不能替代正文。

## 范围与判断口径

- **对象固定：** 19篇方法／技术报告、1篇框架、4篇基础背景，名单见[wiki索引](index.md)及[原调研](awesome-agentic-opd-review.md)。CAST是solver-teacher边界工作；Cross-Domain Hybrid OPD间接相关。4篇背景仅有摘要级阅读，不承担多轮机制结论。
- **证据层级：** 【事实】指作者方法或报告的观察；【解释】是本次跨论文判断；【开放问题】尚待验证。实验未复现；“库内未建立证据”不推出“无人做过”。
- **本次核查：** 阅读24页已有方法与边界记录，并回查TCOD、ReOPD、SAGE、ATOD、FutureBridge、TurnOPD、CAST、MemOPD、Top-K Drift、Planning Physics的原HTML相关章节。其余沿用wiki阅读记录。新增的Planning Physics §5.3知识错配证据直接
## Key Papers (29 total)
- [paper:agarwal2023_onpolicy_distillation_language] On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes: 【作者方法】GKD 在 student 自生成序列上查询 teacher，并允许选择不同 divergence 或与 RL 结合。
- [paper:chen2026_branching_onpolicy_distillation] Branching On-Policy Distillation: 【作者方法】BranchOPD 在高不确定／高分歧位置分叉 student 接续，复用前缀扩大监督覆盖，并以 PBR 修复协议边界。
- [paper:chen2026_crossdomain_hybrid_opd] Cross-Domain Hybrid OPD for Generalizable Search Agents: 【作者方法】Cross-Domain Hybrid OPD 将搜索 GRPO 与数学／代码／逻辑／科学专家 OPD 混合；专家先用中等难度 curriculum，再扩展全难度。
- [paper:chen2026_look_ahead_before] Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation: 【作者方法】FutureBridge-OPD 恢复候选 turn 的环境，插入 teacher bridge，并比较两条 student continuation 的 teacher-preferred token ratio，仅接受改善该代理指标的 bridge。
- [paper:gu2023_minillm_onpolicy_distillation] MiniLLM: On-Policy Distillation of Large Language Models: 【作者方法】MiniLLM 使用 reverse KL 与 on-policy 优化，将较大白盒 teacher 的分布迁移给小 student。
- [paper:huang2026_katcoderv25_technical_report] KAT-Coder-V2.5 Technical Report: 【作者方法】KAT-Coder-V2.5 先做 expert-trajectory cold start，再按领域路由 reverse-KL OPD；依据 teacher/student top-k overlap 降权或屏蔽漂移后缀，使用 length-stratified batching。
- [paper:kotoge2025_can_compact_language] Can Compact Language Models Search Like Agents? Distillation-Guided Policy Optimization for Preserving Agentic RAG Capabilities: 【作者方法】DGPO 先从独立 teacher 的正确轨迹做 cold-start KD；RL 阶段仅对错误预测加入 teacher KL guidance，保留成功 student 的探索。
- [paper:li2026_katcoderv2_technical_report] KAT-Coder-V2 Technical Report: 【作者方法】KAT-Coder-V2 将分别 SFT/RL 的五个领域专家按任务路由到 student rollout，返回 sampled-token log-prob，联合优化 RL 和 OPD。
- [paper:li2026_onpolicy_distillation_curriculum] On-Policy Distillation with Curriculum Turn-level Guidance for Mult
## Recent Relationships (92 total)
  idea:grounded-belief-retraction-operator --inspired_by--> paper:tan2026_atod_annealed_turnaware
  idea:grounded-belief-retraction-operator --addresses_gap--> gap:G2
  idea:transition-effect-equivalence-distillation --inspired_by--> paper:tan2026_atod_annealed_turnaware
  idea:transition-effect-equivalence-distillation --addresses_gap--> gap:G2
  idea:teacher-evidence-posterior-potential-credit --inspired_by--> paper:tan2026_atod_annealed_turnaware
  idea:teacher-evidence-posterior-potential-credit --addresses_gap--> gap:G5
  idea:amortized-external-teacher-correction-model --inspired_by--> paper:tan2026_atod_annealed_turnaware
  idea:amortized-external-teacher-correction-model --addresses_gap--> gap:G2
  idea:reversible-error-inoculation-on-policy --inspired_by--> paper:tan2026_atod_annealed_turnaware
  idea:reversible-error-inoculation-on-policy --addresses_gap--> gap:G1
  idea:blackb
