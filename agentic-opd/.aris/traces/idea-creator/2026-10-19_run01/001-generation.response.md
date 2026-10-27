{
  "shard_id": "atod_ideas_astra",
  "candidates": [
    {
      "id": "ASTRA-01",
      "dedup_key": "evidence-separated-decision-target",
      "title": "切断错误 reasoning 对 teacher 决策的反向污染",
      "method": [
        "从 student rollout 构造事实视图：保留任务、实际 action 和 observation，移除未经验证的 reasoning 陈述。",
        "外部 teacher 在事实视图上给出下一步 action 目标；student 仍根据原始历史生成 reasoning 和 action。",
        "联合训练 action 蒸馏与两种上下文视图下的决策一致性，并保留 outcome RL。"
      ],
      "core_assumption": "猜测：部分低 disagreement 来自 teacher 被错误解释诱导，而非双方都缺少行动能力。",
      "atod_basis_and_gap": "事实：§1、C.6讨论错误前缀压缩 gap；§3.3仍逐 token 条件化于 student prefix。解释：提高权重不能修复已被污染的目标。",
      "nearest_work_and_overlap": "潜在重合：context distillation、MemOPD、SOD；区别需落在事实与推断分离及其因果检验，尚未查新。",
      "minimal_experiment_and_falsification": "固定真实 action/observation，仅改写错误 reasoning；测 teacher action 漂移和训练收益。若漂移很小或清理后收益消失，则否证。",
      "scaling_cost": "每 turn 一份事实视图与一次 teacher target；可用更短上下文替代原评分，避免环境分叉。",
      "main_risk": "删掉正确推断也会丢信息；不能把事实视图偷偷构造成完整可观测状态。"
    },
    {
      "id": "ASTRA-02",
      "dedup_key": "teacher-plan-portfolio-exploration",
      "title": "蒸馏可执行策略组合，而不是单一路径偏好",
      "method": [
        "每个任务由外部 teacher 提出少量不同的高层计划，使用固定长度结构表示。",
        "student 学习计划分布，自采样计划并完成全部交互；组内 outcome 分别更新计划选择和执行策略。",
        "teacher 定期纠正 student 自产计划的缺失步骤，保留多个有效计划的概率质量。"
      ],
      "core_assumption": "猜测：小 student 的探索瓶颈包含策略同质化；token 熵不能保证组内策略多样性。",
      "atod_basis_and_gap": "事实：§3.2、§5.1使用 G=8，§4只调整同一类轨迹上的梯度。解释：未直接塑造跨 rollout 的策略覆盖。",
      "nearest_work_and_overlap": "潜在重合：skill-conditioned distillation、TCOD、层次 RL；需区分 teacher prefix 接管与学生自主执行的计划分布蒸馏。",
      "minimal_experiment_and_falsification": "固定 rollout、teacher token 总额，比较成功策略覆盖与全零奖励组比例；若只增加语言多样性而不增加有效探索，则否证。",
      "scaling_cost": "每组一次短 teacher 计划生成，随计划数和长度增长；执行仍为原有 G 条 student rollout。",
      "main_risk": "计划可能束缚执行；推理时计划必须由 student 生成，避免隐含 teacher 依赖。"
    },
    {
      "id": "ASTRA-03",
      "dedup_key": "teacher-action-control-variate",
      "title": "将 teacher 从优化目标改为无偏 RL 控制变量",
      "method": [
        "共同 OPD 热身后，用实际 returns 校准 teacher log-prob，使其预测 token 或 action 的后续收益。",
        "在策略梯度中减去该动作相关预测，并加入其在 student 分布下期望的解析梯度。",
        "交叉拟合校准器，保证 teacher 主要减少估计方差，而不持续改变目标最优策略。"
      ],
      "core_assumption": "猜测：teacher 信号与回报相关但存在系统偏差，适合作为控制变量。",
      "atod_basis_and_gap": "事实：§4.1把 OPD 与 RL 相加，§4.2保留非零 teacher anchor。解释：annealing 减少偏置，不能保证消除。",
      "nearest_work_and_overlap": "潜在重合：Q-Prop、动作相关基线、reward extrapolation；必须核查语言 token 与多轮版本是否已有。",
      "minimal_experiment_and_falsification": "从相同热身 checkpoint 比较梯度方差、固定预算成功率和 teacher 错误继承；若相关性不足或方差上升，则否证。",
      "scaling_cost": "复用 teacher logits，加轻量校准器和词表期望；不增加环境 rollout，完整词表处理可能增加显存。",
      "main_risk": "全零奖励阶段无法凭无偏估计创造学习信号；不能宣称替代早期探索引导。"
    },
    {
      "id": "ASTRA-04",
      "dedup_key": "partial-order-option-distillation",
      "title": "将 teacher 指导编译为可复用的子目标依赖程序",
      "method": [
        "teacher 从已有 student 成功与失败轨迹提取子目标、前置条件和终止条件，形成小型依赖图。",
        "student 学习生成该图，并用 option policy 执行当前可满足的子目标。",
        "环境反馈更新子目标完成状态；RL 优化具体路线，teacher 只修订失效的程序片段。"
      ],
      "core_assumption": "猜测：可迁移的教师知识主要是前置关系，而非固定动作顺序。",
      "atod_basis_and_gap": "事实：§4.3按完整 turn 分配监督；D.2的清洗、移动、放置具有跨 turn 依赖。解释：turn 目标不显式保留这些关系。",
      "nearest_work_and_overlap": "潜在重合：ArCHer、option learning、计划蒸馏及技能条件化；需证明可复用依赖程序提供独立价值。",
      "minimal_experiment_and_falsification": "训练已见子目标组合，测试新顺序与新组合；对照普通计划文本。若不能提高组合泛化或减少 teacher 调用，则否证。",
      "scaling_cost": "按任务簇生成、按失败片段修订，成本随独特程序数量增长；推理期程序和执行器均由 student 提供。",
      "main_risk": "teacher 从轨迹推断的前置关系未必具有因果性，错误程序可能系统性阻止有效行为。"
    },
    {
      "id": "ASTRA-05",
      "dedup_key": "bayes-consistent-hindsight-belief-distillation",
      "title": "用回看信息蒸馏信念更新，避免蒸馏全知动作",
      "method": [
        "teacher 阅读完整真实 rollout，为少量任务相关隐变量输出带不确定性的后验标签。",
        "student 在每个历史 prefix 上预测这些变量分布，使用 proper scoring loss 学习条件信念。",
        "action policy 条件化于 student 信念，继续进行外部 teacher OPD 与 outcome RL。"
      ],
      "core_assumption": "猜测：部分深层失败来自错误信念持续传播；合理的回看监督可训练更新规则。",
      "atod_basis_and_gap": "事实：§3.1包含部分观测交互，C.6归因于错误前缀累积。解释：ATOD未区分不可知信息与已观察但未正确整合的信息。",
      "nearest_work_and_overlap": "潜在重合：MemOPD、privileged-information distillation、POMDP belief learning；区别应是后验校准与信息可得性。",
      "minimal_experiment_and_falsification": "控制关键证据出现时刻，测证据前校准和证据后更新；若提前表现为全知或仅靠答案泄漏获益，则否证。",
      "scaling_cost": "每条完成轨迹一次 teacher 标注，复用于多个 prefix；额外训练成本取决于抽样 prefix 数。",
      "main_risk": "teacher 后验错误会污染标签；不能把事后正确答案直接当成早期确定性 action target。"
    },
    {
      "id": "ASTRA-06",
      "dedup_key": "teacher-knowledge-to-evidence-demand",
      "title": "把 teacher 的参数知识转译为 student 的证据获取能力",
      "method": [
        "teacher 根据学生轨迹标出决策依赖但尚无外部证据支持的事实，生成短的证据需求。",
        "student 学习将需求转成工具查询，并为使用的事实输出真实 observation 中的引用位置。",
        "蒸馏取证和证据绑定过程；最终回答由已有 outcome reward 优化。"
      ],
      "core_assumption": "猜测：小模型无法完整内化 teacher 知识，但能学习按需检索和核对。",
      "atod_basis_and_gap": "事实：表1中 Search-QA 各尺度仍低于 teacher；D.1要求模型自行判断知识是否充足。解释：token imitation 未分离知识容量与取证能力。",
      "nearest_work_and_overlap": "潜在重合：Search-R1、检索蒸馏、evidence-grounded distillation；需核查将隐性 teacher 知识外化为取证需求的先例。",
      "minimal_experiment_and_falsification": "使用答案知识更新或长尾事实任务，匹配工具次数；若收益只来自增加搜索或直接泄漏答案，则否证。",
      "scaling_cost": "失败轨迹一次 teacher 需求标注；引用位置可机械核验，额外成本主要来自取证工具调用。",
      "main_risk": "字符串引用不能证明证据蕴含结论；teacher 可能生成不可检索的证据需求。"
    },
    {
      "id": "ASTRA-07",
      "dedup_key": "budget-neutral-random-horizon-opd",
      "title": "随机化交互预算，恢复被截断的深层学习信号",
      "method": [
        "在固定平均交互预算下，为组内 rollout 分配具有长尾的随机 horizon。",
        "记录每一步继续采样的已知概率，对深层 teacher 信号和完成回报做存活概率校正。",
        "联合优化经过校正的 OPD 与 RL，避免将被预算截断的轨迹直接视作完整失败。"
      ],
      "core_assumption": "猜测：部分深层能力缺口来自训练数据的截断机制，而非深层 turn 本身缺少权重。",
      "atod_basis_and_gap": "事实：C.3固定最大步数；C.6中弱模型接近50步上限，深层样本构成发生变化。解释：T-DUR不改变到达深层状态的采样概率。",
      "nearest_work_and_overlap": "潜在重合：randomized truncation、survival correction、horizon curriculum；区别需由预算匹配和估计目标证明。",
      "minimal_experiment_and_falsification": "固定总环境步数和 teacher token，比较长任务成功率；若优势在同等 horizon 覆盖对照下消失，则否证。",
      "scaling_cost": "期望 rollout 成本不变，但长尾 episode 增加并行等待；校正权重需要控制方差。",
      "main_risk": "若任务本身定义硬 deadline，则延长 horizon 改变任务；不能以此声称原任务收益。"
    },
    {
      "id": "ASTRA-08",
      "dedup_key": "semantic-quotient-action-distillation",
      "title": "在可证明等价的行动类上蒸馏",
      "method": [
        "利用工具 schema、参数规范化和环境规则，将等价调用归入同一 action class。",
        "将 teacher 的行动建议聚合为类分布，student 学习选类，并独立生成合法调用和 reasoning。",
        "类间进行蒸馏，类内由执行反馈优化，允许学生保留不同表述及实现。"
      ],
      "core_assumption": "猜测：部分 disagreement 来自序列实现差异，而不是决策错误。",
      "atod_basis_and_gap": "事实：§3.3、§4.3以 token 概率定义监督和差异；D.1含显式 admissible actions。解释：同效行动可能承受不必要的模仿压力。",
      "nearest_work_and_overlap": "潜在重合：structured-action distillation、semantic RL、action abstraction；若仅剩格式规范化，则贡献不足，尚待查新。",
      "minimal_experiment_and_falsification": "改变合法 alias、工具参数顺序与等价接口，测跨接口迁移；若原收益仅来自降低格式错误，则否证核心假设。",
      "scaling_cost": "有限行动集可批量评分；开放工具需采样 teacher 行动，成本随候选数增长；无需环境恢复。",
      "main_risk": "真实等价关系可能难以确定；自由文本搜索不能仅凭语义相似就合并为同一行动。"
    }
  ]
}
