{
  "shard_id": "sol-object",
  "candidates": [
    {
      "lens": "supervision-object",
      "dedup_key": "effect-quotient-distillation",
      "title_zh": "按环境效果蒸馏行动等价类",
      "method_steps": [
        "在 student 自采样到达的状态 h，分别采样 teacher 和 student 的候选 tool actions，组成有限集合 A。",
        "在可恢复环境中执行候选，按相同工具返回与相同状态变化分成效果等价类 E；状态校验信息只用于训练标签。",
        "teacher 样本频率给出类分布 q_T(E)，student 将类内所有 action 的概率相加，匹配类分布。"
      ],
      "objective_or_update": "令 p_S^A(a|h)=exp(log p_S(a|h))/Σ_{b∈A}exp(log p_S(b|h))，最小化 L=-Σ_E q_T(E)logΣ_{a∈E}p_S^A(a|h)。监督对象是执行效果的概率质量，而非某条命令的逐 token 概率。",
      "hypothesis": "工具调用存在大量实现相同效果的命令、参数表达与操作顺序。效果等价类允许保留 student 已会的表达，减少模仿 teacher 表面格式造成的有效行动损失。",
      "nearest_work_and_delta": "GKD（2306.13649）匹配 student-generated sequence 上的 teacher distribution；MemOPD（2608.07068）解决 invocation 接口与 masks 对齐；CAST（2607.25308）转移 solver action value。这里转移环境效果类的分布，不依赖 solver value，也不只修正输入接口。新颖性待查。",
      "core_claims": [
        "待验证：相同 teacher 预算下，效果类目标比 action-token KL 更能保留 student 的有效替代动作。",
        "待验证：收益随可执行同义动作比例增加，而非仅来自更多候选采样。",
        "待验证：工具表面表达变化后，task success 的下降更小。"
      ],
      "minimum_experiment": "选择两个可恢复文本工具环境；比较 ordinary OPD、相同候选集但逐 action 蒸馏、效果类蒸馏。固定 rollout、teacher samples 和环境调用预算，报告 held-out success、有效替代动作保留率及全部成本。",
      "falsifier": "等价类充分存在且标签可靠时，匹配成本后仍不优于逐 action 蒸馏；或增益全部来自候选数量。",
      "required_access": "独立 teacher 的文本采样即可；student action likelihood；环境 snapshot/reset/branch；可审计的工具效果签名。隐藏状态若用于分组，不进入部署 student 输入。",
      "risk": "即时效果相同未必意味着后续语义相同；候选归一化也可能带来长度偏差。",
      "estimated_effort_and_compute": "规划假设为 0.6B–1.7B student、4B–8B teacher。先做 10^3 个状态、每状态 4–8 个候选的 pilot；主要新增成本是约 4–8 次环境分叉。接口实现预计约两周，未测量训练时长。",
      "so_what": "让 agent 学会可达到的效果，可能比复制某个 teacher 的命令习惯更适合多实现路径的工具环境。"
    },
    {
      "lens": "supervision-object",
      "dedup_key": "evidence-belief-ledger-transfer",
      "title_zh": "蒸馏有证据出处的工作状态",
      "method_steps": [
        "student 正常 rollout；在选定状态，teacher 仅根据可见历史生成紧凑 ledger：已确认事实、已改变资源、未完成条件及对应 observation 引用。",
        "student 在同一历史上通过辅助输出预测 ledger，主 actor 继续接受独立 teacher 的常规 action OPD。",
        "部署时只运行 student actor；teacher ledger 不作为额外输入。"
      ],
      "objective_or_update": "L=L_OPD+λ[-log p_S(b_T|h)]，其中 b_T 是 teacher 标注的结构化工作状态；辅助输出与 actor 共享主体表示。核心改变是增加跨 turn 状态监督，而非调整 action-token 权重。",
      "hypothesis": "长程失败常发生于行动所依据的工作状态已经过时。显式预测哪些事实仍成立、哪些要求尚未满足，可使 action policy 更稳定地使用工具反馈。",
      "nearest_work_and_delta": "MemOPD（2608.07068）保证 memory rewrite 后 token distribution 的输入接口一致；此方法增加 teacher 的语义状态目标。GKD 提供 action OPD 基线。ledger 的价值与原创性均待验证，不以 memory 对齐本身为贡献。",
      "core_claims": [
        "待验证：辅助 ledger 提高长交互任务成功率，而不只是 ledger 预测准确率。",
        "待验证：收益集中在资源变化、证据冲突与多条件完成任务。",
        "待验证：部署不增加 teacher 调用，actor 单次推理开销可维持基线水平。"
      ],
      "minimum_experiment": "固定 action OPD 数据，比较无辅助任务、等长普通摘要辅助任务、证据 ledger 辅助任务；匹配训练 tokens，测长程 success、过时事实导致的行动错误及 observation 引用准确率。",
      "falsifier": "ledger 预测显著改善但 task success 不变；或等长普通摘要获得相同收益。",
      "required_access": "独立 text teacher；完整可见工具历史；支持共享主体辅助输出的 student 训练。无需环境分叉或隐藏状态。",
      "risk": "teacher ledger 可能遗漏或误判状态；固定字段也可能只适用于特定工具域。",
      "estimated_effort_and_compute": "上述模型规模假设下，先标注 10^3–10^4 个 student 状态；每状态新增一次短 teacher 输出与辅助 CE。预计一至两周完成最小实现，训练成本由 ledger 长度决定。",
      "so_what": "将 teacher 的监督推进到行动依据本身，为多轮 agent 提供跨 turn 的状态学习信号。"
    },
    {
      "lens": "supervision-object",
      "dedup_key": "temporal-contract-trajectory-supervision",
      "title_zh": "用跨轮时序契约监督轨迹",
      "method_steps": [
        "teacher 在 student 当前状态输出少量可执行时序条件，例如先取得证据再引用、写入后验证、满足某前提后才能提交。",
        "从该状态采样 student 的短期真实轨迹，依据工具日志自动判定每条轨迹是否满足契约。",
        "用满足与违反契约的轨迹对更新 student；保留普通 OPD 作为基础监督。"
      ],
      "objective_or_update": "L=L_OPD+λΣ_{(y+,y-)}log(1+exp[-β(ℓ_S(y+|h)-ℓ_S(y-|h))])，其中 ℓ_S 只计算 action likelihood，y+ 与 y- 分别满足、违反 teacher 契约。没有可比较轨迹对时不产生该辅助项。",
      "hypothesis": "逐 turn KL 无法直接表达两个动作之间的必要依赖；关系监督允许多条不同操作路径满足同一个跨轮正确性条件。",
      "nearest_work_and_delta": "AC-OPD（2609.22254）调整 continuation 监督长度；FutureBridge（2608.01953）选择 teacher bridge。这里 teacher 传递可检验的时序关系，而非指定 continuation。与 trajectory preference、结构化 imitation 的关系需要进一步查证。",
      "core_claims": [
        "待验证：时序契约减少跨 turn 依赖违规。",
        "待验证：相同动作样本下，关系目标优于独立 turn KL。",
        "待验证：允许多种满足契约的方案，有助于保留 student 的有效路径。"
      ],
      "minimum_experiment": "在两个已有文本 agent 环境中选取自然存在的验证、引用与前置条件任务；比较 OPD、teacher continuation CE、契约偏好目标。匹配 rollout tokens，分别报告 success 与契约违规率。",
      "falsifier": "违规率下降但 success 不变或恶化；或收益可由等量 teacher continuation 完全解释。",
      "required_access": "独立 teacher 的结构化文本输出；短期环境分叉；可解析工具日志。契约只能依赖 student 可见信息。",
      "risk": "teacher 将个人操作偏好误写成必要条件，会压制正确的替代路径；正负轨迹对也可能稀缺。",
      "estimated_effort_and_compute": "先做约 10^3 个状态、每状态 2–4 条短分支。契约 parser 与日志接口预计两周左右；新增环境成本与短分支数线性相关。",
      "so_what": "让监督直接表达长程 agent 必须遵守的行动关系，而不只是每一步像不像 teacher。"
    },
    {
      "lens": "supervision-object",
      "dedup_key": "counterfactual-observation-action-contrast",
      "title_zh": "蒸馏工具反馈改变行动的条件差异",
      "method_steps": [
        "在 student 发起工具调用的状态，取得两种可实际产生的返回，例如成功与可恢复失败。",
        "teacher 为两种 observation 分别指定下一行动 a1、a2，并明确反馈变化是否应引起行动切换。",
        "student 学习同一前缀下 observation 与 action 的匹配关系。"
      ],
      "objective_or_update": "对于应切换的反馈对，L_pair=-logσ(ℓ_S(a1|h,o1)-ℓ_S(a2|h,o1))-logσ(ℓ_S(a2|h,o2)-ℓ_S(a1|h,o2))，与普通 OPD 相加。监督对象是反馈引起的行动差异，不是某条完整 teacher 路径。",
      "hypothesis": "agent 容易延续已计划的操作而忽略新工具反馈。成对条件差异监督可迫使 student 使用 observation 中真正改变决策的信息。",
      "nearest_work_and_delta": "FutureBridge（2608.01953）比较 bridge continuations；AC-OPD 调整 teacher continuation 长度。这里比较共享前缀、不同真实反馈下的 action 对应关系，不以单条 bridge 的优劣为目标。新颖性待核。",
      "core_claims": [
        "待验证：提高对工具失败、空结果及资源变化的响应准确率。",
        "待验证：比相同 observation-action 样本上的独立 CE 更有效。",
        "待验证：收益可以迁移到未见过的返回措辞。"
      ],
      "minimum_experiment": "使用允许真实成功/失败分支的两个工具环境；比较独立 CE、成对反馈对比、普通 OPD。匹配 teacher 标注与分支数，测成功率和反馈被忽略的比例。",
      "falsifier": "成对目标不优于相同样本的独立 CE，或仅适用于训练时的返回字符串。",
      "required_access": "独立 text teacher；student action likelihood；可控制合法工具返回分支的 resettable 环境。不得伪造不可能的世界状态。",
      "risk": "工具分支缺少现实可比性；有限候选 action 可能让 student 学会局部辨别而不改善完整执行。",
      "estimated_effort_and_compute": "先做 10^3 个反馈对，每对两次短环境执行与两份 teacher action 标签；预计一至两周实现，训练成本接近等量 pairwise action supervision。",
      "so_what": "把工具反馈真正改变策略这一能力作为蒸馏目标，支持 agent 在环境变化后及时改道。"
    },
    {
      "lens": "interaction-transfer",
      "dedup_key": "student-draft-teacher-edit-policy",
      "title_zh": "把 teacher 的局部修正学成 student 编辑策略",
      "method_steps": [
        "student 在当前状态先生成完整 action draft。",
        "独立 teacher 以明确 edit 操作修复 draft 的工具名、参数或必要行动内容，而非重新写一套轨迹。",
        "student 学习条件编辑策略；部署时由同一个 student 先 draft、再编辑并执行。"
      ],
      "objective_or_update": "L_edit=-log p_S(e_T|h,a_draft)，e_T 为 teacher 的编辑序列；修复后 action 由确定性 patch 应用得到。draft actor 可保留普通 OPD。全部编辑标签来自独立 teacher，不用 student 自身输出作 teacher target。",
      "hypothesis": "teacher 的完整示范可能超出 student 当前执行能力；围绕 student 自己的 draft 学习可执行修正，更容易内化为部署时的纠错能力。",
      "nearest_work_and_delta": "SAGE-OPD（2606.19659）决定监督强度；OLIVE（2609.36246）提供 teacher continuation。这里转移显式编辑策略，并在部署时由 student 执行第二遍编辑。与编辑式 imitation 的重叠尚待查证。",
      "core_claims": [
        "待验证：编辑策略降低可修复工具调用错误。",
        "待验证：在同等部署推理预算下优于普通 student self-review。",
        "待验证：局部修正比完整 action 重写更少破坏已有正确内容。"
      ],
      "minimum_experiment": "比较普通 OPD、相同两遍推理预算的 self-review、teacher 全量重写蒸馏、teacher edit 蒸馏；测端到端 success、修正率与误改率。",
      "falsifier": "收益只来自第二遍推理；或编辑后的正确内容被破坏，使 success 不升。",
      "required_access": "独立 text teacher；可解析 action 格式；student 两遍推理。无需 teacher 部署调用或环境分叉。",
      "risk": "多一次 student 推理增加延迟；局部编辑不适合需要整体改换策略的错误。",
      "estimated_effort_and_compute": "先收集 10^3–10^4 个 student drafts；每个新增一次 teacher edit 输出。预计一至两周实现，必须将部署第二遍 tokens 计入成本。",
      "so_what": "teacher 不仅提供更好的动作，还留下 student 自己可调用的纠错操作。"
    },
    {
      "lens": "interaction-transfer",
      "dedup_key": "teacher-optimized-student-learning-gain",
      "title_zh": "让 teacher 为 student 学会多少而优化",
      "method_steps": [
        "在 student-visited states，teacher 采样两份候选监督 continuation。",
        "从相同 student checkpoint 各做一次等量蒸馏更新，在未参与更新的相关任务上测无 teacher 的表现变化。",
        "用学习增益偏好训练 teacher，再让该 teacher 继续提供常规 on-policy 蒸馏目标。"
      ],
      "objective_or_update": "对监督 d 定义 U(d)=R_probe(Update(S,d))-R_probe(S)。teacher 用 DPO 或采样策略梯度偏向较大 U 的监督；student 始终以独立 teacher 的 continuation CE/KL 更新。核心是将 teacher 目标改为 learner improvement。",
      "hypothesis": "teacher 自己最容易成功的路径未必最容易被小 student 学会；直接优化更新后的独立表现可选择更有教学价值的监督。",
      "nearest_work_and_delta": "SCOUT（2609.38360）按 student prefixes 上 teacher continuation 的可验证 reward 适配 teacher；这里 reward 来自 student 更新后的无辅助泛化表现。不同于 CLOOPD（2609.24141）对固定 teacher-scored batch 做多次 actor passes。新颖性待核。",
      "core_claims": [
        "待验证：teacher 自身 continuation success 与 student learning gain 并非完全一致。",
        "待验证：学习增益目标改善每单位 teacher supervision 的训练收益。",
        "待验证：改善可迁移到未用于 teacher reward 的任务。"
      ],
      "minimum_experiment": "先在小 student 上比较固定 teacher、teacher 自身 reward 适配、student learning-gain 适配；每个 outer round 保持相同两份监督、student update 数与 probe budget。",
      "falsifier": "学习增益标签无法复现，或计入临时更新与 probe 成本后不优于固定 teacher。",
      "required_access": "可训练独立 teacher；student checkpoint 临时复制或 LoRA；可验证 task reward；严格分开的 update、probe 与最终 test tasks。",
      "risk": "outer-loop reward 方差高、成本大，teacher 可能只适配一个 student checkpoint。",
      "estimated_effort_and_compute": "先做几十个 outer rounds，每 round 两次短 student 更新与固定小 probe set。预计三至四周实现；新增成本主要是临时 student 更新与评测，不给出未经测量的 GPU 小时。",
      "so_what": "把教学效果落实为 teacher 的优化目标，使 teacher–student 协作直接服务 student 的独立能力。"
    },
    {
      "lens": "interaction-transfer",
      "dedup_key": "teacher-selected-environment-counterexample",
      "title_zh": "让 teacher 用真实反例训练 student 应变",
      "method_steps": [
        "student 在其访问状态提交下一步 action 及短期后续意图。",
        "teacher 从环境允许的少量反馈分支中选择一个会暴露该意图缺陷的真实反例，例如合法空结果或暂时失败。",
        "student 在该分支继续执行；teacher 对这些 student 实际访问的新状态提供正确 action 标签。"
      ],
      "objective_or_update": "teacher 选择 c*=argmax_{c∈C_legal} violation(a_student,c)，student 最小化真实反例分支上的 L=Σ_t -log p_S(a_T,t|h_S,t)。teacher 改变交互问题，独立 teacher action 仍是训练监督；不把 teacher 变成部署执行者。",
      "hypothesis": "随机工具失败训练浪费大量无关分支；针对 student 当前意图构造合法反例，可集中教会何时放弃、重试或重新验证。",
      "nearest_work_and_delta": "Guided-OPD、DASH-OPD 改变谁执行 action；FutureBridge 插入 teacher bridge；此方法由 teacher 选择环境挑战，student 始终执行。不同于仅判断 recoverability 后回滚。与 adversarial imitation 的关系需查证。",
      "core_claims": [
        "待验证：相同反例数量下优于随机合法反馈扰动。",
        "待验证：提高自然发生工具异常时的成功率。",
        "待验证：无需 teacher 接管也能扩展 student 的恢复状态覆盖。"
      ],
      "minimum_experiment": "在具有原生异常分支的两个文本环境中，比较普通 OPD、随机分支 OPD、teacher-selected 分支 OPD；保持分支集合与调用数一致，同时评测正常和自然异常任务。",
      "falsifier": "只适用于 teacher 选择的训练扰动，不能改善自然异常；或随机分支效果相同。",
      "required_access": "独立 teacher；合法环境分支选择接口；snapshot/reset；分支后 teacher action 标注。环境不可支持的假反馈不纳入训练。",
      "risk": "teacher 可能偏爱不现实的罕见异常，牺牲正常任务性能。",
      "estimated_effort_and_compute": "先做约 10^3 个状态、每状态最多 2–3 个合法短分支；约两周接口工作。新增 teacher 判断与环境分叉成本必须分别统计。",
      "so_what": "teacher 的帮助可以体现为提出 student 必须学会应对的问题，而非替它把任务完成。"
    },
    {
      "lens": "interaction-transfer",
      "dedup_key": "teach-back-independent-teacher-target",
      "title_zh": "先让 student 复述执行，再蒸馏 teacher 修正",
      "method_steps": [
        "在 student 访问状态，teacher 给一个只依据现有可见信息的短提示。",
        "student 据提示生成可执行 action，作为其理解方式的 teach-back。",
        "teacher 依据原状态和 teach-back 输出最终正确 action 分布；student 在不含提示和 teach-back 的原历史上学习该独立 teacher target。"
      ],
      "objective_or_update": "a_b~π_S(·|h,hint_T)，随后 L=KL(q_T(·|h,hint_T,a_b)||π_S(·|h))；black-box teacher 可用其最终 action CE。训练目标始终来自独立 teacher，不使用 hinted student distribution 充当 teacher。",
      "hypothesis": "teacher 看到 student 如何误解提示后，能给出针对执行缺口的监督；擦除提示训练可将这种纠正转化为无 teacher 的行动能力。",
      "nearest_work_and_delta": "LENS-OPD（2609.33409）包含 hint、±hint student continuations 与 privileged same-student distribution 的内化；这里新增 teach-back 后的独立 teacher 修正 target，避免以 same-student distribution 蒸馏。OLIVE 直接 teacher continuation，不包含这段理解反馈。邻近性较强，新颖性未建立。",
      "core_claims": [
        "待验证：teach-back 让最终 teacher 标签比直接提示或直接 continuation 更适合当前 student。",
        "待验证：无提示部署仍保留训练收益。",
        "待验证：收益来自 teacher 针对理解缺口的修正，而非单纯增加 teacher tokens。"
      ],
      "minimum_experiment": "比较直接 teacher action、hint-conditioned teacher action、hint→student teach-back→teacher correction；所有标签都来自独立 teacher，匹配总 teacher tokens，评测 teacher-free success。",
      "falsifier": "移除 teach-back 后效果不变，或匹配 teacher tokens 后优于基线的收益消失。",
      "required_access": "独立 teacher 的两次短输出；student 一次额外训练期 action proposal；白盒分布或黑盒最终 action 均可。无需环境分叉。",
      "risk": "交互只是在更贵地重现 teacher 本来就能给出的标签；最终 target 也可能过度依赖提示措辞。",
      "estimated_effort_and_compute": "先做 10^3 个 student states；每状态约两次短 teacher 输出与一次 student teach-back。预计一至两周完成 pilot，部署维持单个无提示 student actor。",
      "so_what": "让 teacher 在训练时确认 student 的实际理解，再把纠正直接压入 student 的独立决策。"
    }
  ]
}
