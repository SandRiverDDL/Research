{
  "route": "PROVISIONAL_GO_C7_EQUIVALENCE_CLASS_OPD",
  "winner_id": "C7",
  "winner_reason": "C7 在当前七项中最好地平衡了新意、可执行性和 Findings 级故事：失败可通过训练时全工具、测试时禁用首选路线的反事实直接测量；方法可以利用环境终态自动定义效果类；单个 1.7B 学生、确定性工具 DAG 和三种子即可快速得到 go/kill 结论。它不是纯诊断的前提是目标显式保留类内首动作覆盖，而非只匹配等价类总质量。",
  "ranking": [
    {
      "id": "C7",
      "decision": "GO_CONDITIONALLY",
      "novelty_10": 6.5,
      "feasibility_10": 8.0,
      "borderline_fit_10": 7.5,
      "closest_work": [
        {"title": "On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity", "url": "https://arxiv.org/abs/2606.26091", "overlap": "已直接报告 on-policy self-distillation 的 mode-seeking 和输出多样性下降，但未研究工具路径的执行等价性及工具失效后的路线韧性。"},
        {"title": "Better State Exploration Using Action Sequence Equivalence", "url": "https://arxiv.org/abs/2110.10632", "overlap": "直接利用产生相同环境效果的动作序列等价关系，但目标是 RL 探索而非 agentic OPD。"},
        {"title": "When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation", "url": "https://arxiv.org/abs/2607.07050", "overlap": "证明局部 token 支持可遗漏决定工具行为的低概率 token；与路线坍缩相关，但不建模整条可执行路径的效果等价类。"}
      ],
      "defensible_delta": "把文本多样性下降收窄为可执行、可反事实验证的 agent failure：标准 OPD 在同等任务成功下压掉效果等价的备用工具路线，导致首选工具被禁用时骤降。核心增量应是对环境可验证的效果类做 push-forward distillation，并保留类内可用首动作覆盖，而不只是泛化的 entropy bonus。",
      "strongest_objection": "仅匹配等价类总概率并不保证类内多条路线被保留；模型仍可把全部质量放到一条路线。若必须依赖枚举所有路径或 oracle 终态标签，方法也会被批评为只适用于玩具 DAG。",
      "decisive_pilot": "构造两个确定性工具 DAG，每题有 2 至 4 条不同首工具但同终态的成功路线；用 Qwen3-1.7B 学生和约 8B 教师比较 SFT、RL、token-OPD、entropy-OPD、support-union、class-OPD。训练时所有工具可用，测试时禁用训练后概率最高的首工具；三随机种子同时报告原分布成功率、禁用后成功率、有效首动作覆盖和终态类概率。",
      "go_threshold": "标准 OPD 在原分布成功率不低于 SFT/RL 的同时，禁用首选工具后至少下降 15 个百分点；class-OPD 在两个环境族、三种子上恢复至少 10 个百分点，原分布损失不超过 2 个百分点，并领先 entropy/support-union 至少 5 个百分点。",
      "kill_threshold": "标准 OPD 未稳定降低备用路线覆盖，或简单 entropy/support-union 与 class-OPD 相差不超过 3 个百分点；或效果类只能依靠人工路径枚举、无法由执行终态自动获得。"
    },
    {
      "id": "C1",
      "decision": "PARK_AS_BACKUP",
      "novelty_10": 5.5,
      "feasibility_10": 9.0,
      "borderline_fit_10": 7.0,
      "closest_work": [
        {"title": "TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments", "url": "https://arxiv.org/abs/2605.04107", "overlap": "已用确定性编译消除工具 schema 表示差异并改善工具调用，使 canonicalization 本身不再新。"},
        {"title": "Can Agents Generalize to the Open World?", "url": "https://arxiv.org/abs/2607.01084", "overlap": "OpenAgent 已系统化 action、observation、query 和 domain shift，并采用扰动增强训练。"},
        {"title": "When Top-K Misses the Decision", "url": "https://arxiv.org/abs/2607.07050", "overlap": "已表明 token-level support 与真实工具决策不一致，逼近 C1 对表面 token KL 的批评。"}
      ],
      "defensible_delta": "可守住的增量不是 schema 编译，而是证明 token KL 对语义同构工具重命名不具不变性，并将师生分布 push-forward 到操作与参数角色空间后再蒸馏。",
      "strongest_objection": "可能只是把 TSCG 式 schema compiler 接到 OPD 上；若简单统一 prompt 或 schema augmentation 即可修复，就没有方法贡献。",
      "decisive_pilot": "对同一可执行工具集做随机重命名、参数重排、自然语言描述改写和同名语义交换；比较 token-OPD、统一编译器、schema augmentation、canonical action OPD。",
      "go_threshold": "跨至少两类 schema 变换，token-OPD 相比不蒸馏基线恶化至少 10 点，canonical OPD 恢复至少 7 点，并比统一编译器或 augmentation 高至少 5 点。",
      "kill_threshold": "统一编译或普通 schema augmentation 将差距缩至 3 点以内，或 canonical 映射需要大量人工语义标注。"
    },
    {
      "id": "C2",
      "decision": "PARK",
      "novelty_10": 6.0,
      "feasibility_10": 6.0,
      "borderline_fit_10": 6.5,
      "closest_work": [
        {"title": "GAPD", "url": "https://arxiv.org/abs/2605.29584", "overlap": "已把逻辑形式转成可执行动作序列，并用中间实体锚点对齐 on-policy 动作监督。"},
        {"title": "Sub-goal Distillation", "url": "https://arxiv.org/abs/2405.02749", "overlap": "把教师能力蒸馏到宏观 subgoal planning，再由执行器完成 primitive actions。"},
        {"title": "Can Agents Generalize to the Open World?", "url": "https://arxiv.org/abs/2607.01084", "overlap": "提供 action-space shift 的受控设定，但未解决宏工具与 primitive 序列间的蒸馏对齐。"}
      ],
      "defensible_delta": "仅当 effect-space 标签能由执行器自动产生，并支持教师宏动作与学生多步 primitive 序列的在线多对一蒸馏时，才区别于 subgoal distillation 和 GAPD。",
      "strongest_objection": "多步 effect 的归因、边界和时序对齐本身就是主要难题；oracle effect 标签会让方法看起来像人工层级监督。",
      "decisive_pilot": "在确定性工具图上把教师动作随机编译为学生的 2 至 4 步 primitive 序列，对比 raw OPD、masking、trace expansion、GAPD 式锚点和 effect-space OPD。",
      "go_threshold": "effect-space OPD 在两种图结构上比最强非 oracle 基线高至少 8 点，且自动标签覆盖率超过 90%。",
      "kill_threshold": "简单 trace expansion 或 gold-action alignment 相差不超过 3 点，或标签与序列边界必须人工指定。"
    },
    {
      "id": "C5",
      "decision": "PARK",
      "novelty_10": 5.5,
      "feasibility_10": 5.0,
      "borderline_fit_10": 6.0,
      "closest_work": [
        {"title": "AgentRewind", "url": "https://arxiv.org/abs/2608.14380", "overlap": "围绕不可恢复错误记录 agent context 与环境状态的对齐 checkpoint 并回滚。"},
        {"title": "ACRFence", "url": "https://arxiv.org/abs/2603.20625", "overlap": "刻画不可逆外部副作用以及 checkpoint-restore 的局限。"},
        {"title": "PIGDreamer", "url": "https://proceedings.mlr.press/v267/huang25ai.html", "overlap": "已有利用 privileged state 学习安全的部分可观测策略。"}
      ],
      "defensible_delta": "必须证明教师 KL 在相同分歧下不成比例地增加不可逆行为，而 recoverability-aware projection 能在不依赖运行时回滚的情况下修复。",
      "strongest_objection": "风险加权 KL 很像把 CPO、安全 RL 或 cost shaping 接到 OPD；真实不可逆操作难以安全、可重复评估。",
      "decisive_pilot": "在可快照 sandbox 中配对可逆和不可逆但表面相似的动作。",
      "go_threshold": "标准 OPD 在匹配任务成功率下使灾难率至少翻倍；方法把灾难率降低至少 50%，成功率损失不超过 3 点，并领先通用 risk-cost 基线。",
      "kill_threshold": "通用安全 RL 或 action masking 匹配结果，或风险分值只能由 oracle 快照反事实获得。"
    },
    {
      "id": "C3",
      "decision": "REJECT_AS_FRAMED",
      "novelty_10": 3.5,
      "feasibility_10": 8.5,
      "borderline_fit_10": 5.0,
      "closest_work": [
        {"title": "FutureBridge-OPD", "url": "https://arxiv.org/abs/2608.01953", "overlap": "用教师短桥接加学生续写的未来轨迹验证教师指导是否有益。"},
        {"title": "Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress", "url": "https://arxiv.org/abs/2608.19408", "overlap": "用独立 progress signal 过滤与真实进展冲突的 OPD 奖励。"},
        {"title": "OpenAgent", "url": "https://arxiv.org/abs/2607.01084", "overlap": "研究工具和环境变化下静态训练脆弱性及扰动增强。"}
      ],
      "defensible_delta": "只有把教师过时形式化为可识别的版本因果冲突，而非一般坏教师过滤，才可能留下窄缝。",
      "strongest_objection": "FutureBridge 与 progress-based filtering 已覆盖先验证教师信号再蒸馏的核心机制。",
      "decisive_pilot": "v1 教师配 v2 环境，系统改变工具语义，比较纯 RL、扰动 SFT、FutureBridge、progress filtering 和当前 gating。",
      "go_threshold": "只使用当前执行反馈的方法超过 FutureBridge、通用过滤和纯 RL 至少 8 点，同时计算成本更低。",
      "kill_threshold": "任一通用过滤或纯 RL 基线在 3 点以内，或 gating 需要短期未来 rollout。"
    },
    {
      "id": "C6",
      "decision": "REJECT_AS_FRAMED",
      "novelty_10": 3.5,
      "feasibility_10": 6.0,
      "borderline_fit_10": 4.5,
      "closest_work": [
        {"title": "SMRC-SD", "url": "https://arxiv.org/abs/2608.05219", "overlap": "直接处理参考轨迹与学生当前执行状态错配。"},
        {"title": "GAPD", "url": "https://arxiv.org/abs/2605.29584", "overlap": "用中间实体锚点匹配当前策略状态。"},
        {"title": "Provable Partially Observable Reinforcement Learning with Privileged Information", "url": "https://arxiv.org/abs/2412.00985", "overlap": "理论处理 observation aliasing、部分可观测策略和 privileged expert distillation。"}
      ],
      "defensible_delta": "必须提出比增加历史或做状态匹配更明确的 OPD 目标。",
      "strongest_objection": "基本是 POMDP belief/memory 加 state matching；最小充分 history bucket 没有可计算定义。",
      "decisive_pilot": "构造 observation 相同但 inventory、permissions 或 flag 不同的状态对，比较长上下文、belief state、SMRC-SD 和 trace bucket。",
      "go_threshold": "在未见 alias 组合上超过最强 belief/state-matching 基线至少 8 点，并用少于完整历史的表示实现。",
      "kill_threshold": "增加上下文或 SMRC-SD 即消除差距，或 bucket 需要访问测试时不可见 latent state。"
    },
    {
      "id": "C4",
      "decision": "REJECT",
      "novelty_10": 2.5,
      "feasibility_10": 4.5,
      "borderline_fit_10": 3.5,
      "closest_work": [
        {"title": "SMRC-SD", "url": "https://arxiv.org/abs/2608.05219", "overlap": "处理 privileged successful trajectory 与学生可达状态不匹配。"},
        {"title": "Anchored Residual Guidance for Privileged OPD", "url": "https://arxiv.org/abs/2606.10385", "overlap": "指出 oracle trace 的 reachability mismatch 和 hindsight shortcut。"},
        {"title": "Provable Partially Observable Reinforcement Learning with Privileged Information", "url": "https://arxiv.org/abs/2412.00985", "overlap": "研究全状态专家蒸馏到部分可观测策略的可行条件。"},
        {"title": "Belief-Aware Privileged Distillation", "url": "https://arxiv.org/abs/2605.26155", "overlap": "以 belief uncertainty 调节全状态教师到部分观测学生的蒸馏。"}
      ],
      "defensible_delta": "目前没有足够独立增量；counterfactual resampling 需要新的可识别性结果或无需 simulator 的估计器。",
      "strongest_objection": "这是成熟的 privileged policy distillation/POMDP 问题，agentic 版本也已经很近。",
      "decisive_pilot": "同一 student observation 下枚举 latent states，比较绝对模仿、anchored residual、belief-aware weighting 和 information-set averaging。",
      "go_threshold": "只有在无需额外 latent-state oracle 时，连续两类 POMDP 超过已有方法至少 8 点才重开。",
      "kill_threshold": "需要 simulator 穷举 privileged states，或已有方法在 3 点以内。"
    }
  ],
  "global_warning": "截至 2026-08-22，agentic OPD 邻域更新极快。首轮不要铺开真实 benchmark；先用不超过 24 A100-hours 的 C7 因果 pilot 检查 OPD 是否真的在匹配成功率下消灭备用路线，以及 class objective 是否胜过 entropy/support-union。任一不成立就停止。"
}
