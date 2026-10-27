{
  "shard_id": "g17-l2-astra",
  "model": "gpt-6-astra",
  "candidates": [
    {
      "id": "L2-A1",
      "title": "逐步撤去 teacher 前缀，让联合能力从后向前接通",
      "method_steps": [
        "A 为每道组合题生成经过验证的中间前缀，B 续写一次，保留确有联合解的训练题。",
        "先提供完整 A 前缀，让 student 自采样后续并接受强动态多 teacher 监督；随后逐轮缩短提供的前缀，让 student 自己补齐越来越多的 A 阶段。",
        "每次缩短都依据当前交接点的联合成功率；最终必须退到零前缀，在原始问题上训练和评测。"
      ],
      "minimal_formalism": "d_k(y|x)=δ(y≤k=z≤k^A)πθ(y>k|x,z≤k^A)；最小化 E_dk Σt>k KL(πθ,t‖q_dynamic,t)，仅当验证联合成功率≥τ时令k减小；k>0属于teacher roll-in混合分布，k=0才恢复完整student on-policy。",
      "hypothesis": "【待验证】先让 B 所需状态稳定出现，再学习抵达它的前缀，可以跨过 A、B 必须同时成熟的学习障碍。风险是 student 依赖提供的前缀，撤去后收益消失。",
      "closest_known_work": [
        "TrustMOPD §3、App.C.4.1：已有随位置变化的动态监督。",
        "H-OPD §3.3–3.4：已有信息桥接与逐 token 融合。",
        "邻近机制：reverse curriculum、teacher roll-in、scheduled sampling；本轮未查新。"
      ],
      "claimed_delta": "【拟验证增量】干预的是联合状态的训练起点及其撤除路径；要求在完全撤除辅助后，优于固定前缀混合及普通由易到难训练。",
      "minimum_test": "先用256题核查：单项A/B已具备、真实A前缀显著提高联合成功、普通轨迹很少到达该前缀类别。再用2k题可验证解析→执行任务测试；对比普通OPD、Trust或适配的H-OPD、普通curriculum、固定teacher-prefix mixing和完整轨迹SFT。等总student采样、teacher生成/评分及制备预算，报告无辅助联合成功、状态到达率、单项能力；另用较大student小规模检查容量解释。数据生成器需自建。",
      "killer_result": "补足状态后仅辅助条件下成功，零前缀时优势消失；或等预算固定mixing/SFT达到相同结果；或收益完全由A单项进步解释。",
      "compute_assumptions": "工作假设≤8×3090；1.7–3B student、两个3B teacher，2k×≤1024 student输出token。新增A前缀及B验证续写各≤512token/题，共≤2.05M teacher生成token；每条新轨迹仍需2次teacher整序列forward，Trust另1次reference。若无现成专长池，各预留2k×512token、1轮adapter制备，共2.05M teacher训练token；预检另256×2×512≈0.26M生成token。所有输入与重复上下文另计，制备失败则测试条件不成立。",
      "risk": "MEDIUM",
      "effort": "约2–3周完成最小实现与机制检验；未运行。",
      "so_what": "若成立，给出把训练时可达状态逐步转成独立部署能力的简单路径；否则说明teacher辅助曝光不足以解决组合学习。",
      "dedup_key": "teacher-prefix-shortening|joint-success-controlled-roll-in"
    },
    {
      "id": "L2-A2",
      "title": "在一个交接点分裂稀有成功状态",
      "method_steps": [
        "student 批量生成 A 阶段，在预先定义的 A→B 交接点用确定性验证器检查中间结果。",
        "把固定的后续采样预算分配给已到达有效状态的前缀，每个有效前缀最多生成4条独立student后续；不对所有位置分叉。",
        "A 前缀只计一次训练权重，新增后续照常接受动态多 teacher OPD；部署仍从原题独立生成。"
      ],
      "minimal_formalism": "L=E_z∼dπ L_prefix(z)+λE_z∼dπ(·|C(z)=1),u∼π(·|z) L_suffix(z,u)，每轮总生成token固定、每前缀副本数≤4；所有动作来自student，但后段占用分布经过条件化，不是原始无偏on-policy目标。",
      "hypothesis": "【待验证】稀有有效前缀一旦出现，应当承担多次 B 学习机会；普通完整rollout可能把大部分后段预算消耗在无效状态。若有效前缀几乎从不出现，本法无法启动。",
      "closest_known_work": [
        "TrustMOPD §3：同一student prefix上监督分配已有覆盖。",
        "TU-OPD §3：可解样本筛选已有覆盖，但本提案筛选student生成的中间状态。",
        "邻近机制：rare-event splitting、prioritized replay；本轮未查新。"
      ],
      "claimed_delta": "【拟验证增量】用一次可验证交接点，把已经发现的联合状态转换为更多新鲜后续，而不制备teacher前缀。价值必须超过普通成功轨迹重放和提示重采样。",
      "minimum_test": "在可生成的解析→约束执行任务上预检256题，分别测单项能力、正确中间结果条件下的B能力及自然到达率。用2k题预算对比普通OPD、强动态聚合、成功轨迹replay、按成功率采样prompt及普通curriculum；另对随机前缀做同样分裂。固定总采样token和teacher总预算，比较联合成功与每个新鲜有效状态的学习收益；用较大student核查容量。明确统计被丢弃前缀与上下文重算。",
      "killer_result": "普通训练已经充分到达有效状态；或者分裂显著增加有效后续曝光却不改善独立联合成功；或者等预算replay/随机分裂完全解释收益。",
      "compute_assumptions": "工作假设≤8×3090；1.7–3B student、两个3B teacher。总student输出预算约2.05M token，分裂消耗该预算，不额外扩张；每个后续最多4副本，重算前缀计入预算。新增teacher生成为0；每条采样分支需2次整序列teacher forward，Trust另reference，因此按实际上下文token配平。若需制备teacher，各2k×512token单轮adapter，共2.05M训练token；池预检约0.26M生成token。程序验证需自建，不使用环境重置。",
      "risk": "MEDIUM",
      "effort": "约2–3周；单检查点采样与预算控制，未运行。",
      "so_what": "若成立，稀有状态的利用效率成为可调的训练变量；否则可排除重复利用少数成功前缀这一廉价路径。",
      "dedup_key": "single-boundary-student-state-splitting|verified-reachability"
    },
    {
      "id": "L2-A3",
      "title": "把错误中间结果改配为正确的新题，提前训练 B",
      "method_steps": [
        "选用能精确反向生成题目的任务族，例如把自然语言解析成DSL，再执行DSL。student 对原题生成中间程序 z。",
        "若 z 语法有效但不符合原题，用确定性渲染器生成新题 x′，使 z 对 x′ 恰好正确；不修改 z。",
        "以 x′、z 为上下文，让 student 自采样后续并接受 B 及动态多 teacher 监督；原题仍继续普通OPD，最终只评测原始分布的完整生成。"
      ],
      "minimal_formalism": "构造R使g(R(z))=z；z∼πθ(·|x)，u∼πθ(·|R(z),z)，仅对u加入L_OPD(R(z),z,u)。z并非从πθ(·|R(z))采样，故这是显式relabelled off-policy前缀加on-policy后续。",
      "hypothesis": "【待验证】部分失败A输出已经包含可供B学习的有效状态；通过改变题目一致性而非等待A完全正确，可以减少B监督饥饿。主要风险是逆向渲染分布过窄，收益不能回到原题。",
      "closest_known_work": [
        "H-OPD §3.3：已有对teacher输入的信息桥接，本方法改变的是训练题目与student中间状态的一致性。",
        "TU-OPD §3：已有可解题覆盖，本方法尝试利用原本错误的student状态。",
        "邻近机制：hindsight relabeling、合成数据curriculum；本轮未查新。"
      ],
      "claimed_delta": "【拟验证增量】复用student自然产生的中间状态，在不替换它的情况下生成可监督的联合上下文；须优于直接训练B子任务及普通新增合成题。",
      "minimum_test": "自建可精确反演的DSL任务，留出操作关系组合与题面模板。预检256题确认单项A/B、正确前缀效应和自然状态稀缺。2k题预算比较普通OPD、强动态聚合、同一批z上的B单项训练、随机合成题curriculum、teacher-prefix off-policy mixing。配平全部生成/评分与训练token，并保持同一teacher池；报告原题联合成功、单项能力与到达率，另做较大student核查。自然任务是否存在可靠逆映射尚不确定。",
      "killer_result": "仅在渲染新题上获益，原始组合题没有改善；或B单项训练/普通合成数据达到相同效果；或逆映射必须暴露最终答案才能成立。",
      "compute_assumptions": "工作假设≤8×3090；1.7–3B student、两个3B teacher，总student输出约2.05M token，将至多25%预算分给重标记后续。确定性渲染不调用teacher，新增teacher生成为0；每个后续2次整序列forward，Trust另reference，改题后的完整上下文重新计费。若需teacher制备，各2k×512token单轮adapter，共2.05M训练token；预检约0.26M生成token。数据及逆映射需要实现和独立测试。",
      "risk": "HIGH",
      "effort": "约3–4周，主要成本是有效逆映射与分布控制；未运行。",
      "so_what": "若成立，失败轨迹可直接提供互补能力的学习机会；否则明确这类机会不能仅靠题目重标记迁回真实任务。",
      "dedup_key": "inverse-task-relabeling-of-student-prefix|exact-intermediate-consistency"
    },
    {
      "id": "L2-A4",
      "title": "用 B 能否接着完成，训练 student 抵达有用状态",
      "method_steps": [
        "student 从原题生成 A 阶段并提交不可更改的中间结果 z。",
        "只在该交接点让 B 续写一次，以执行验证得到成功回报；任务契约禁止 B 忽略或修复已提交的 z。",
        "把该回报用于更新student的A前缀策略；student自身的完整轨迹继续做动态多teacher OPD，使B最终也进入同一个student。"
      ],
      "minimal_formalism": "r_B(x,z)=V(x,z,u_B)，u_B∼π_B(·|x,z)；J_A=E_z∼πθ E_uB[r_B]，用(r_B−b(x))Σt∈A ∇logπθ(z_t|x,z<t)更新前缀，并保留L_dynamic_OPD。辅助回报来自πθ^Aπ_B^B的expert rollout，属于OPD+RL混合方法。",
      "hypothesis": "【待验证】student尚不会B时，自己的终局失败会掩盖已接近成功的A状态；B的完成结果能提前训练这些状态的可达性。若A正确性标签已提供全部信号，额外B调用可能没有价值。",
      "closest_known_work": [
        "TrustMOPD §3、H-OPD §3.4：已有当前位置动态监督，本提案加入跨交接点的完成回报。",
        "TU-OPD §3：已有teacher rollout验证，但其验证用于teacher与样本筛选。",
        "邻近机制：expert rollout imitation、policy-gradient reward shaping；本轮未查新。"
      ],
      "claimed_delta": "【拟验证增量】把第二位teacher的条件完成能力转为第一阶段的探索信号；必须证明收益超过普通A正确性奖励、student终局RL及等预算更多OPD。",
      "minimum_test": "先在256题可验证两阶段任务上检查单项A/B、自然到达率及B确实依赖提交的z。用2k题比较普通OPD、强动态聚合、OPD+A正确性奖励、OPD+student终局RL、普通curriculum/replay与teacher-prefix mixing；另将B回报在正确前缀之间打乱。等总采样、teacher制备和评分预算；报告独立联合成功及到达率，配合较大student检查容量。数据需自建；不把理想专家或可信交接验证器当现成资源。",
      "killer_result": "A正确性奖励或打乱的B回报同样有效；B通过忽略中间结果获得奖励；或只增加有效状态到达率而不提高student独立联合成功。极低到达率导致一次B rollout无法提供可用信号亦构成失败。",
      "compute_assumptions": "工作假设≤8×3090；1.7–3B student、两个3B teacher，2k×≤1024 student输出token。每题最多一次≤512token的B续写，新增≤1.024M teacher输出token及其输入前缀；无逐token probe、无环境重置。普通student轨迹仍需2次teacher整序列forward，Trust另reference。若需制备，两teacher各2k×512token单轮adapter，共2.05M训练token；预检约0.26M生成token。追加B成本从对照总预算扣齐。",
      "risk": "HIGH",
      "effort": "约3–4周；需处理稀疏回报、接口验证与OPD/RL预算匹配，未运行。",
      "so_what": "若成立，互补teacher不仅提供答案分布，也能帮助student探索到彼此发挥作用的位置；否则可界定额外专家完成调用的价值边界。",
      "dedup_key": "expert-completion-return-for-student-prefix-gradient|downstream-teacher-success"
    }
  ]
}
