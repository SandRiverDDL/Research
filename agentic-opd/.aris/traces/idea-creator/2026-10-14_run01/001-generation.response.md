{
  "shard_id": "astra-object",
  "candidates": [
    {
      "dedup_key": "successor-equivalence-mass-distillation",
      "lens": "supervision-object",
      "title_zh": "把 teacher 的下一步效应蒸馏成等价行动集合",
      "method_steps": [
        "在 student 实际访问的 h，teacher 生成少量工具行动，student 再生成若干候选；在环境副本执行这些行动。",
        "按可核验的任务可见效应分组，例如返回证据、文件变化和资源消耗；teacher 行动的经验频率定义效应分布 qT(z|h)。",
        "训练 student 给达到同一目标效应的行动集合分配概率质量，随后继续自主 rollout。"
      ],
      "objective_or_update": "L = −Σz qT(z|h) log Σ[a∈Az] πθ(a|h)。a 是包含结束符的完整工具调用；未枚举行动的概率归入 other。Az 可以同时包含 teacher 与 student 提出的行动。",
      "hypothesis": "多轮工具任务允许不同语法、路径或操作顺序产生相同有效状态；按效应聚合监督能保留 student 的可行策略，减少逐 token 模仿带来的无益替换。",
      "nearest_work_and_delta": "GKD/MiniLLM 匹配序列分布；CAST 转移 solver action value；FutureBridge 执行并选择 teacher bridge。本方法转移经过执行验证的 successor 等价类概率质量，既不提供 value target，也不要求复制某条 bridge。新颖性待查。",
      "core_claims": [
        "待验：优于同预算的逐行动 CE/KL。",
        "待验：增益集中在存在多种等价工具实现的任务。",
        "待验：增加有效行动多样性同时维持任务成功率。"
      ],
      "minimum_experiment": "先做可重置文件操作与结构化检索两个环境；比较 OLIVE 式 CE、相同候选逐条 CE、集合概率质量目标；匹配 teacher tokens、候选数和环境调用，测成功率、等价行动覆盖和总成本。",
      "falsifier": "在存在大量可验证等价行动的设置中，集合目标仍不优于相同数据的逐条 CE；或者收益只来自额外环境调用。",
      "required_access": "Black-box 独立 teacher 文本输出；student 完整行动 logprob；环境 snapshot/branch；可审计效应签名。隐藏状态可用于验证，但不能输入部署 student。",
      "risk": "效应签名可能把影响后续任务的不同状态误合并；严格签名又可能几乎没有可合并样本。",
      "estimated_effort_and_compute": "条件估算：小模型 pilot 约 1–2 人周；每状态 2 个 teacher 加 4 个 student 候选，需要最多 6 次单步分叉。训练与评测 GPU 成本取决于未确认的硬件。",
      "so_what": "如果成立，OPD 可以明确学习环境中可替代的行为，而不是把 teacher 的表达方式误当成唯一正确行为。"
    },
    {
      "dedup_key": "contingent-controller-distillation",
      "lens": "supervision-object",
      "title_zh": "蒸馏能够分支执行的短程条件控制器",
      "method_steps": [
        "在 student 访问的 h，请 teacher 生成最多两层的条件控制器：工具调用、对返回字段的条件判断、分支行动。",
        "采用受限 DSL 和确定性解释器；在具有有限 outcome schema 的环境中核验分支是否合法。",
        "student 学习生成控制器，并自主执行到控制器结束；后续 teacher 监督继续发生在 student 实际到达的状态。"
      ],
      "objective_or_update": "L = −log πθ(AST(CT)|h)，监督对象是规范化的控制器 AST。部署时 student 生成控制器，解释器根据实际工具返回执行分支。",
      "hypothesis": "单条 continuation 只展示实际发生的一条路径；条件控制器同时传递面对工具失败、空结果或冲突返回时的响应策略。",
      "nearest_work_and_delta": "OLIVE 转移 teacher continuation，AC-OPD 调整 continuation 长度，TCOD 改变交接前缀。本方法转移可执行的条件策略对象，包含尚未发生的分支。它与程序合成和层级模仿的关系需要进一步查新。",
      "core_claims": [
        "待验：在工具返回变化时减少策略失效。",
        "待验：优于同样分支数据展开后的普通 action CE。",
        "待验：保持 teacher 缺席时的自主多轮成功率。"
      ],
      "minimum_experiment": "选择有 success/empty/error 等有限返回类型的文本 API 环境；比较单轨迹 CE、所有分支展开 CE、控制器蒸馏。严格匹配 teacher 输出量和部署总推理预算，测试训练未见的返回分支组合。",
      "falsifier": "展开全部分支后的普通 CE 达到同等表现；或者收益完全来自解释器提供的手写策略。",
      "required_access": "Black-box teacher；工具 schema；受限 DSL 解释器；可控制并验证分支的文本环境。控制器只能读取部署可见的工具返回。",
      "risk": "DSL 限制了开放任务表达；teacher 生成的条件可能遗漏关键情况，分支核验成本也可能迅速增长。",
      "estimated_effort_and_compute": "条件估算：DSL 和环境适配约 2–3 人周；每状态一个 teacher 控制器，深度 2、最多 4 条验证路径，环境调用需完整计入。",
      "so_what": "如果成立，一次 teacher 监督可以传递局部反馈策略，使 student 学会根据环境变化行动。"
    },
    {
      "dedup_key": "teacher-evidence-bottleneck",
      "lens": "supervision-object",
      "title_zh": "把 teacher 的证据选择蒸馏成行动前的上下文瓶颈",
      "method_steps": [
        "在 student 历史 h 上，teacher 标注支持下一行动的少量原始 observation span IDs，并给出行动 aT；不生成额外事实。",
        "student 先预测证据指针集合 M，再仅使用任务说明与所选原始片段生成行动。",
        "持续从部署形态的 student rollout 收集新历史，用 teacher 修正证据选择和行动。"
      ],
      "objective_or_update": "L = −log πθ(MT|h) − log πθ(aT|task, extract(h,MT))。训练对证据指针做 teacher forcing；部署使用预测的 M，因此必须单独测量指针误差造成的性能损失。",
      "hypothesis": "长程 agent 的错误经常来自旧证据遗失、过时 observation 干扰或无依据状态推断；显式学习选择证据可能比直接匹配行动 logits 更容易跨任务迁移。",
      "nearest_work_and_delta": "MemOPD 对 memory rewrite 后的实际可见接口做精确 KL 对齐；这里学习的是由独立 teacher 标注的证据选择器，并让选择结果实际限制行动上下文。不是仅增加证据解释文本。",
      "core_claims": [
        "待验：长历史和干扰 observation 下增益更明显。",
        "待验：证据选择监督具有跨工具迁移能力。",
        "待验：收益来自有效瓶颈，而非更多 teacher 输出。"
      ],
      "minimum_experiment": "在检索加文件编辑任务中插入可控的过时返回和无关工具输出；比较 full-history OPD、等长摘要 OPD、证据指针瓶颈；报告自主成功率、证据遗漏率和上下文成本。",
      "falsifier": "使用 oracle 证据指针仍无收益；或者实际预测指针的误差抵消全部收益。",
      "required_access": "Teacher 文本标注；带稳定 span IDs 的历史；可控制行动输入上下文的运行时。无需 teacher logits 或环境隐藏状态。",
      "risk": "下一步所需证据可能不足以维持长期任务状态；硬瓶颈也可能删除 teacher 未注意到的信息。",
      "estimated_effort_and_compute": "条件估算：约 1–2 人周实现；每状态一次 teacher 证据与行动标注，部署增加一次短指针预测。必须同时计入检索阶段和行动阶段推理量。",
      "so_what": "如果成立，teacher 能教会 student 怎样维护决策所需的信息，而不仅是当前应该输出什么行动。"
    },
    {
      "dedup_key": "counterfactual-response-relation",
      "lens": "supervision-object",
      "title_zh": "蒸馏工具反馈改变时的决策响应关系",
      "method_steps": [
        "以 student 实际访问的 h 为锚点，通过环境合法分叉得到只改变一个工具反馈因素的 h′。",
        "对两个完整候选行动 a、b，查询独立 teacher 在 h 与 h′ 下的相对偏好。",
        "在普通 OPD 上加入成对响应关系监督，要求 student 对反馈变化产生相同方向和幅度的决策变化。"
      ],
      "objective_or_update": "定义 ℓM(h)=log πM(a|h)−log πM(b|h)。L = LOPD + λ[(ℓθ(h′)−ℓθ(h))−(ℓT(h′)−ℓT(h))]²。保留 OPD anchor，因为响应差本身不能确定绝对行动偏好。",
      "hypothesis": "工具 agent 必须理解反馈如何改变决策，例如请求失败后重试还是换策略；显式传递这种响应关系有助于避免忽略工具返回或错误坚持原计划。",
      "nearest_work_and_delta": "CROP 据当前摘要以 counterfactual prompt sensitivity 选择 token；这里将反馈导致的行为变化直接作为监督目标。GKD 的逐状态分布匹配是必要基线，关系目标是否提供额外归纳偏置尚待验证。",
      "core_claims": [
        "待验：减少对关键工具反馈不敏感的错误。",
        "待验：优于相同 h/h′ 数据上的独立 KL。",
        "待验：响应关系能迁移到未见的反馈组合。"
      ],
      "minimum_experiment": "在可控 success/failure、empty/nonempty、版本冲突环境上构造合法分叉；比较普通 OPD、两状态独立 OPD、成对关系目标，完全共享查询与训练数据。",
      "falsifier": "两状态独立 KL 达到相同表现；或者收益仅存在于人为不一致的 observation 扰动。",
      "required_access": "Teacher 与 student 对完整候选行动的 logprob；环境合法干预和分叉能力。不得直接伪造与历史矛盾的工具输出。",
      "risk": "关系目标没有增加标签信息，可能只是低效重复逐状态 KL；长行动 log-odds 的尺度也可能不稳定。",
      "estimated_effort_and_compute": "条件估算：环境可分叉时约 1–2 人周；每锚点至少两个 teacher scoring context 和两条对应分叉，训练成本约随成对状态数增长。",
      "so_what": "如果成立，OPD 可以直接教会 agent 怎样响应环境变化，而不完全依赖模型从孤立行动标签中归纳。"
    },
    {
      "dedup_key": "teacher-choice-over-student-options",
      "lens": "interaction-transfer",
      "title_zh": "让 teacher 在 student 能执行的短程方案之间教学",
      "method_steps": [
        "从 student 自主访问的 h，采样 K 个固定长度短程 option，并在环境副本中实际执行。",
        "teacher 观察这些 student 行动及其结果，给出方案选择或排序，不生成新的行动。",
        "用 teacher 的选择监督 student 对自身方案的概率分配，下一轮仍由 student 自主产生候选和轨迹。"
      ],
      "objective_or_update": "对等长轨迹 τk，pθ(k|h)=softmaxk(log πθ(τk|h))，L=−Σk qT(k|h,{τ}) log pθ(k|h)。轨迹概率只包含 policy action likelihood，不包含环境转移概率。",
      "hypothesis": "teacher 的最优演示可能依赖 student 暂时不具备的技能；在已实际执行的 student 方案之间传递偏好，可以把监督集中在当前可实现的行为改进。",
      "nearest_work_and_delta": "MAD-OPD 组合 teacher 分布；FutureBridge 引入 teacher bridge；这里 teacher 只能选择 student 自己实现的多轮方案。与轨迹 preference distillation 的重合需要认真查证，不能仅凭 agent 场景声称新颖。",
      "core_claims": [
        "待验：减少 teacher 演示可用但 student 无法复现的落差。",
        "待验：相同总成本下优于 teacher continuation CE。",
        "待验：方案支持集足够时能持续改善自主策略。"
      ],
      "minimum_experiment": "K=3、H=2 的小规模 pilot；比较 teacher continuation CE、单步候选选择、短程 option 选择。记录成功率、teacher 偏好准确性、候选支持集覆盖和全部分叉成本。",
      "falsifier": "teacher 选出的方案不能提高后续自主成功率；或者需要过大的 K 才出现可学习的优质方案。",
      "required_access": "Black-box teacher 排序；student trajectory logprob；环境分叉。训练不依赖外部 task reward，但评测需要可验证成功指标。",
      "risk": "student 候选支持集可能缺失关键策略；teacher 也可能偏好看起来合理但无法完成任务的短程方案。",
      "estimated_effort_and_compute": "条件估算：约 1–2 人周；每锚点约 K×H=6 次工具执行，加一次 teacher 比较。长观察会显著增加 teacher 输入成本。",
      "so_what": "如果成立，teacher 的帮助可以直接落在 student 已能实现的策略空间内，提升每次监督转化为自主能力的效率。"
    },
    {
      "dedup_key": "post-update-transfer-selected-demonstrations",
      "lens": "interaction-transfer",
      "title_zh": "按 student 更新后的自主收益选择 teacher 演示",
      "method_steps": [
        "在 student 访问的 h，请固定独立 teacher 提供 K 个短纠错 demonstration。",
        "对每个 demonstration，用独立的影子 adapter 做一次相同规模的蒸馏更新。",
        "在不带 teacher 帮助的独立 sibling episodes 上评估更新后策略，只把自主迁移收益最大的 demonstration 用于实际更新。"
      ],
      "objective_or_update": "θk=θ−α∇CE(dk;θ)；k*=argmaxk mean[R(πθk,E)−R(πθ,E)]；实际更新 θ←θ−α∇CE(dk*;θ)。最终 policy update 仍来自独立 teacher demonstration。",
      "hypothesis": "能救好当前任务的演示不一定最容易被 student 学会；直接选择产生实际学习迁移的演示，可以改善 assistance 到 competence 的转化。",
      "nearest_work_and_delta": "FutureBridge 依据 continuation proxy 选择执行的 bridge；SCOUT/Prep-OPD 适配 teacher。这里 teacher 固定，选择依据是 student 参数更新后的独立自主表现。CLOOPD 重用 teacher-scored batch，不等于比较候选更新的迁移效果。",
      "core_claims": [
        "待验：更新后迁移收益比当前演示成功率更能预测学习价值。",
        "待验：减少高表现但低可学性的 teacher 监督。",
        "待验：节省的正式训练样本足以补偿选择成本。"
      ],
      "minimum_experiment": "只训练小型 LoRA，K=2，每次使用 4 个独立 sibling episodes；比较随机选择、当前任务回报选择、更新后自主收益选择，并加入使用全部 demonstration 的同总预算基线。",
      "falsifier": "选择排序在独立重复中不稳定；或者计入影子更新和评测后，固定使用全部 demonstration 更有效。",
      "required_access": "Student 参数与可复制 adapter；独立 teacher；可重置任务族及可靠成功信号。选择集与最终测试集必须分开。",
      "risk": "短期更新收益噪声大，可能过拟合很小的选择集；计算成本也可能高于所得收益。",
      "estimated_effort_and_compute": "条件估算：约 2–4 人周；每锚点增加 K 次影子更新与 K×4 次自主评估。先限制 50–100 个锚点，不能预设完整训练的 GPU 时长。",
      "so_what": "如果成立，teacher supervision 的价值可以按它真正改变了多少自主能力来优化，而非按演示本身有多漂亮来估计。"
    },
    {
      "dedup_key": "teacher-waypoint-student-realization",
      "lens": "interaction-transfer",
      "title_zh": "teacher 给出可见里程碑，student 自己实现到达路径",
      "method_steps": [
        "在 student 访问的 h，teacher 于副本短程推进，提取一个任务可见、可验证的 waypoint gT，例如获得指定证据或完成某项文件修改。",
        "保持真实训练轨迹从原 h 出发，让 student 自己实现 gT；teacher 只在这些真实 student 状态上提供 goal-conditioned 行动监督。",
        "同时训练 student 从 h 预测 waypoint，部署时由 student 预测并执行，不需要 teacher 在线给目标。"
      ],
      "objective_or_update": "L = −log πθ(gT|h) + Σt KL[πT(·|ht,gT) || πθ(·|ht,gT)]，其中 ht 来自 student 对 waypoint 的实际尝试；black-box teacher 时可改为 teacher action CE。",
      "hypothesis": "长程任务中可迁移的是阶段性状态推进，而 teacher 的具体路径未必适合 student；保留 waypoint、让 student 生成实现路径可能缩小这种落差。",
      "nearest_work_and_delta": "TCOD、FutureBridge 和 Relay-OPD 的帮助包含 teacher 实际执行再交接；这里不把真实轨迹搬到 teacher 到达的状态。OLIVE 提供 continuation；这里将终点转成可学习的 waypoint，并在 student 自己的实现路径上监督。LENS 的 hint internalization 使用 same-student target，本方法的目标与行动标签均来自独立 teacher。",
      "core_claims": [
        "待验：提高无 teacher 部署时的长程任务完成率。",
        "待验：能学到不同于 teacher 路径的有效实现。",
        "待验：预测 waypoint 的误差不会抵消低层策略收益。"
      ],
      "minimum_experiment": "选择存在多条实现路径的检索加编辑任务；比较普通 OPD、teacher bridge 交接、waypoint 加 student realization。分别报告 oracle waypoint 与预测 waypoint，匹配全部 teacher 和环境预算。",
      "falsifier": "只有部署时提供 oracle waypoint 才有效；或者相同长度 teacher continuation CE 已达到同等结果。",
      "required_access": "Teacher rollout 分叉；文本或工具可见的 waypoint 表示和完成检测；student 在线访问状态的 teacher 标注。不得把部署不可见的隐藏 state 当 waypoint。",
      "risk": "teacher 选出的 waypoint 可能超出 student 能力；目标预测与目标执行的误差会相互放大。",
      "estimated_effort_and_compute": "条件估算：约 2–3 人周；每 waypoint 增加 H 次 teacher 工具推进，以及 student 实现路径上的标注。需同时计算失败尝试成本。",
      "so_what": "如果成立，可以把 teacher 的规划能力转成 student 自己能够实现的层级策略，而不是依赖训练时被 teacher 搬到好状态。"
    },
    {
      "dedup_key": "proposal-edit-operator-distillation",
      "lens": "interaction-transfer",
      "title_zh": "把 teacher 的纠错操作蒸馏为部署时的行动编辑器",
      "method_steps": [
        "student 在真实状态 h 生成尚未执行的结构化工具行动 a0；独立 teacher 对它给出最小 edit script eT，例如修改工具名或参数字段。",
        "student 的 editor mode 学习从 h、a0 直接预测 eT；训练 rollout 使用 student 自己预测的编辑，再执行最终行动。",
        "部署仍采用 proposal→student edit→execution，不调用 teacher。所有编辑标签来自独立 teacher。"
      ],
      "objective_or_update": "Ledit=−log πθ(eT|h,a0)，最终行动 a=Apply(a0,eθ)。pilot 固定 proposal policy，只训练 editor adapter，避免把 draft 改善与编辑器贡献混在一起；编辑格式限制为少量结构化操作。",
      "hypothesis": "小 student 可能已经能够提出接近正确的行动，但难以稳定发现参数、前置条件或证据引用错误；模仿 teacher 的局部纠错操作可能比重新生成完整行动更容易学会。",
      "nearest_work_and_delta": "SAGE-OPD 判断监督强弱；OLIVE 生成 continuation；这里蒸馏的是依赖 student proposal 的编辑算子，并把它保留为部署 policy 的一部分。与 LENS 不同，训练 target 不是 hint-conditioned 同一 student 的输出分布。与既有 critique/edit 方法的重合需进一步查新。",
      "core_claims": [
        "待验：局部编辑比完整行动模仿更高效地修复近正确方案。",
        "待验：编辑器能修复训练未见的 proposal 错误组合。",
        "待验：同部署推理预算下仍优于普通两次生成。"
      ],
      "minimum_experiment": "在参数约束明确的文本工具环境，固定同一 draft policy；比较独立 teacher final-action CE、teacher edit CE、相同两次推理预算的普通 OPD。报告端到端成功率、错误修复率和错误引入率。",
      "falsifier": "收益被相同推理预算的完整重生成消除；或者编辑器经常把正确 proposal 改错。",
      "required_access": "Black-box teacher；结构化行动及 edit interpreter；student adapter 训练。无需环境分叉，但需要保存执行前的 proposal 和完整可见状态。",
      "risk": "最小编辑可能无法表达真正需要的策略变化；如果允许任意重写，又可能退化为普通 action CE。",
      "estimated_effort_and_compute": "条件估算：约 1–2 人周；每训练状态一次 teacher 编辑标注，部署多一次短编辑推理。应完整计入额外延迟与 tokens。",
      "so_what": "如果成立，teacher 的在线纠错帮助可以被直接编译进 student 自身的行动流程，形成无需外部 teacher 的可部署能力。"
    }
  ]
}
