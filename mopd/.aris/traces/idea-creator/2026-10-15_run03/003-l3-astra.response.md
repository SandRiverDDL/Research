{
  "shard_id": "g17-l3-astra",
  "model": "gpt-6-astra",
  "candidates": [
    {
      "id": "L3-A1",
      "title": "后缀分歧回传蒸馏",
      "method_steps": [
        "Student 按常规自采样；所有 experts 对同一轨迹评分，保留可信权重及未归一化的 geometric teacher factors。",
        "把实际采到的后续 teacher log-score 与 student entropy 合成 return-to-go，使后续专长难以接续的代价影响较早决定。",
        "用同题多条完整轨迹的独立基线降低方差；不为每个状态生成额外 continuation，也不增加部署组件。"
      ],
      "minimal_formalism": "固定本轮可信权重 w_k(h)，f(h,a)=exp(Σ_k w_k(h)log q_k(a|h))，Q_seq(y|x)∝∏_t f(h_t,y_t)。最小化 KL(P_θ||Q_seq)。对 y~π_old，R_t=Σ_{u≥t}[log f(h_u,y_u)−logπ_old(y_u|h_u)]；一次 on-policy 更新最大化 Σ_t stopgrad(R_t−b_t)logπ_θ(y_t|h_t)。b_t 不依赖当前动作；多次复用须处理 importance correction。全部未来分数来自实际轨迹，不假设 oracle continuation。",
      "hypothesis": "【待验证】有限容量和有限更新预算下，只优化当前位置的条件分布，可能没有把后续跨专家不相容充分归因到上游选择；完整轨迹梯度能改善联合成功。不是断言 token 策略不能表达依赖。",
      "closest_known_work": "Off-vs-On theory 已明确 sequence geometric target 及 continuation；sequence distillation、REINFORCE、soft policy iteration 是直接近邻。Trust 提供局部权重；AVSD/TU 提供 residual；SMOPD 已结合蒸馏与 RL。以上结构的具体重合待查新。",
      "claimed_delta": "候选增量仅是可在现有 MOPD 评分流水线上计算的跨专长延迟信用更新，不声称发现 sequence objective。须进一步证明收益来自依赖信用，而非通用 sequence RL、熵或额外采样；否则只能算已有目标的应用。",
      "minimum_test": "先构造可枚举的两阶段任务，允许每个 teacher 读取完整历史，并保证各关键前缀充分出现；再用约2千道可验证 math→code 任务做小规模测试。比较 Trust、TU residual、AVSD 适配、SMOPD、同目标普通 sequence PG、单 teacher 和结果 RL；固定轨迹及 teacher 评分，并加更大 student 的容量对照。",
      "killer_result": "普通 sequence PG 等预算完全复现收益；或联合改善只随更多采样/容量出现；或局部权重近 one-hot 时未来因子没有额外信息。任何一项都削弱独立贡献。",
      "compute_assumptions": "工作假设≤8×3090；现成2个3B experts，1.5B/3B LoRA student，2048 prompts×4 rollouts×1024 tokens。Teacher 评分为2×2048×4×1024 tokens；相对复用同4条轨迹的局部基线无额外 teacher forward，相对每题1条则4倍。Trust reference 评分另计且共享；不估 GPU 小时。",
      "risk": "HIGH",
      "effort": "中：更新实现较直接，方差控制与已有 sequence 方法区分困难。",
      "so_what": "若成立，可用已经支付的 teacher 评分，把多个专长的接续后果纳入早期决策学习，而无需逐状态分叉。",
      "dedup_key": "跨时间 return-to-go 更新早期决策｜同批完整 student 轨迹的多 teacher log-prob"
    },
    {
      "id": "L3-A2",
      "title": "跨步骤交叉比蒸馏",
      "method_steps": [
        "从同题两条 student 轨迹找到两个均局部有效的早期选择 p₁、p₂，以及两个后续片段 v₁、v₂；用解析规则确定同一种依赖关系。",
        "让后续专长 teacher 在两个完整前缀下分别评分两个片段，形成2×2矩阵；仅需 teacher-forced scoring，不生成反事实 rollout。",
        "在普通 MOPD 外匹配该矩阵的交叉 log-odds，使 student 保留早期选择如何改变后续偏好；所有对照共享四种评分与样本。"
      ],
      "minimal_formalism": "s_M(i,j)=log P_M(v_j|p_i)，Δ_M=s_M(1,1)+s_M(2,2)−s_M(1,2)−s_M(2,1)。L=L_MOPD+λ E[(Δ_θ−stopgrad(clip(Δ_B,−c,c)))²]；B 为已验证局部可靠的后续 expert。优先使用等长、语法有效片段；Δ 消除可分离的行列加性偏置，但不自动证明因果性。",
      "hypothesis": "【待验证】局部可靠信号可能在有限训练中主要传递边际偏好；显式传递两个决定之间的条件偏好变化，比增加相同局部 loss 更有效。完整历史模型本可表示该关系，候选改变的是监督对象。",
      "closest_known_work": "Relational KD、contrastive distillation、结构化预测中的 interaction potentials 是直接近邻，待查新；Trust、TU residual、AVSD 保留的是局部监督及独有信号，不能据此断言它们未保留该关系。",
      "claimed_delta": "直接蒸馏跨步骤的二阶条件关系，而非再调整 teacher 权重。需证明在基线获得相同反事实评分、所有前缀均有覆盖时仍有增益，排除数据增广收益。",
      "minimum_test": "约2千道执行可验证任务，前段决定算法/单位/表示选择，后段必须相应使用；单项测试先确认能力足够。比较四项评分上的普通 KD、完整 sequence KD、匹配样本的 DPO/RL、Trust、TU、AVSD、适用 SMOPD、强单 teacher，以及更大 student；同时打乱依赖配对检验机制。",
      "killer_result": "同数据普通 KD 或 sequence preference 已达到同等联合成功；配对打乱不影响收益；或交叉片段的非自然性而非依赖关系解释全部差距。",
      "compute_assumptions": "工作假设≤8×3090；2个3B experts，1.5B/3B student；2000 prompts×2 rollouts，最长1024 tokens。仅10%题形成一对，片段≤128 tokens；两个自然配对复用原评分，新增2个交叉配对，缓存前缀时额外≤200×2×128 teacher-scored tokens；不缓存则另计每次前缀 forward。无额外 teacher 生成；student 交叉评分与更新另计。",
      "risk": "MEDIUM",
      "effort": "中：主要工作是稳定识别依赖槽位和控制反事实样本质量。",
      "so_what": "若成立，多个局部 experts 不必各自会解整题，也能通过可计算的条件关系教会 student 跨步骤配合。",
      "dedup_key": "匹配跨步骤交叉 log-odds｜已访问前缀上的2×2 teacher-forced 评分"
    },
    {
      "id": "L3-A3",
      "title": "潜在监督路径蒸馏",
      "method_steps": [
        "把监督来源设为整条轨迹上的隐变量路径 z₁:T，使用小型 Markov 转移矩阵描述持续使用与跨专家接续；所有 experts 仍读取完整 student 历史。",
        "每收到一个 student token，依据其在各 expert 下的似然更新路径后验，再计算下一位置的 teacher mixture。",
        "把该精确可计算的条件目标蒸馏进一个 student；部署时移除路径变量。转移矩阵在小型校准集上固定，并与相同切换次数的普通平滑路由对照。"
      ],
      "minimal_formalism": "r₁=ν；Q_t(a|h_t)=Σ_k r_tk q_k(a|h_t)。观测 y_t 后，r̄_tk=r_tk q_k(y_t|h_t)/Q_t(y_t|h_t)，r_{t+1,j}=Σ_k r̄_tk A_kj。L=E_{y~πθ}Σ_t KL(Q_t||πθ(·|h_t))，监督 detached。该 Q 是对完整 Markov teacher 路径求和所得的合法自回归策略；不是把 teacher 当作无记忆模型。",
      "hypothesis": "【待验证】某些互补结构需要保留监督来源的跨步骤关联，单点 reliability 权重可能在有限样本下破坏这种关联；完整路径后验可作为较便宜的归纳偏置。来源一致性并不保证任务正确性。",
      "closest_known_work": "Switching experts、HMM mixture、Bayesian model averaging、option/sequence distillation 是直接近邻，待查新。Trust 的位置变化对照、SMOPD arithmetic mixture，以及 TU/AVSD residual 必须比较。",
      "claimed_delta": "候选干预是联合监督路径及其后验，而非单独加入切换惩罚；若仅为普通路由平滑的重述则没有独立新意。还需证明允许 A→B 接续优于始终坚持一个 teacher，而非仅减少切换。",
      "minimum_test": "先在可枚举的两阶段 full-history teachers 上检查目标本身能否改善联合成功，再用约2千道双专长任务测试。对照独立 token mixture、相同切换率平滑路由、response mixture、Trust/TU/AVSD/SMOPD、普通 sequence KD、单 teacher、结果 RL；保持评分、参数量、总 compute 一致并测试更大 student。",
      "killer_result": "路径后验仅追踪文风或 token 频率；相同切换率的简单平滑已复现收益；或 Q 自身就不比局部 mixture 更能联合成功。此时不能将来源相关性包装成能力依赖。",
      "compute_assumptions": "工作假设≤8×3090；2个3B experts、1.5B/3B student；2000 prompts×2 rollouts×1024 tokens。复用全部 teacher logits，额外 teacher forward/token为0；额外过滤计算 O(TK²)，K=2。约200条校准轨迹若不能复用，另计2×200×1024 teacher-scored tokens。",
      "risk": "HIGH",
      "effort": "低至中：算法实现简单，机制成立与查新风险高。",
      "so_what": "若来源路径确实携带可迁移的依赖信息，可在几乎不增加 teacher 评分成本的条件下将其压入单 student。",
      "dedup_key": "对整条 teacher 隐变量路径求后验并蒸馏｜现有各 expert 的轨迹似然"
    },
    {
      "id": "L3-A4",
      "title": "未履行承诺蒸馏",
      "method_steps": [
        "在 student 轨迹中识别早期已经作出、仍约束后续动作的承诺，如选定单位、变量绑定、算法不变量或尚未满足的输出要求；由程序规则或局部可靠 expert 标注其有效区间。",
        "在每条轨迹一个较晚位置，仅用 student 此刻最后一个 hidden state 重建仍有效的承诺集合，加入一个小型辅助 decoder loss。",
        "与普通局部 MOPD 联合更新；辅助 decoder 部署时丢弃，student 使用原有完整上下文直接作答。"
      ],
      "minimal_formalism": "C_t 为截止 t 仍活跃的承诺，h_t 为 student 最后位置表示；L=L_MOPD+λ E_{t~sample}[−log D_φ(C_t|h_t)]。D_φ 只能读取 h_t，不能重新读取完整 prefix；梯度回传 θ。承诺已履行即移出 C_t，避免仅训练复制所有历史。",
      "hypothesis": "【待验证】各局部 expert 的当前动作监督未必足够维持对未来仍有用的约束表示；辅助压缩活跃承诺可能使后续专长更稳定地服从前面的决定。历史原本可访问，问题不是上下文缺失，也不是 teacher 间格式转换。",
      "closest_known_work": "Auxiliary-state prediction、belief-state supervision、scratchpad/representation distillation、prospective memory training 是直接近邻，待查新。Trust、TU/AVSD residual 与普通 sequence KD 都需检验是否已经达到相同效果。",
      "claimed_delta": "候选监督对象是多个局部专长共同需要维护的未完成义务，而非完整答案或全部历史；单一辅助目标直接约束其跨时间保留。是否超出通用状态重建方法仍开放。",
      "minimum_test": "先用约2千道带可执行检查的组合任务，自动抽取承诺，保证每个关键状态和单项能力充分覆盖。比较普通 MOPD、同容量历史重建头、随机标签头、通用 scratchpad、普通 sequence KD、单 teacher/RL，以及适用 Trust/TU/AVSD/SMOPD；保持参数、更新与 teacher 信息相同，检查更大 student 是否自然消除差距。",
      "killer_result": "承诺可被准确解码但联合成功不改善；任意辅助预测同样有效；或额外 teacher 标注实际提供了答案/新增解题知识。任一结果都不支持依赖保留解释。",
      "compute_assumptions": "工作假设≤8×3090；2个3B experts、1.5B/3B student；2000 prompts×2 rollouts×1024 tokens。规则可抽取场景额外 teacher forward/token为0；每轨迹一个≤32-token承诺集合，辅助 decoder新增≤12.8万训练 tokens。若扩展到自然语言并由 teacher 标注，每轨迹一次≤64-token生成，另计其全部输入评分和≤25.6万输出 tokens；标注质量须核查。",
      "risk": "MEDIUM",
      "effort": "中：辅助目标简单，承诺抽取和自然任务适用性是主要工作。",
      "so_what": "若成立，可用少量训练期状态监督帮助不同专长共享长期约束，部署仍为原来一个 student，且不增加逐状态 teacher 调用。",
      "dedup_key": "最后位置表示重建活跃承诺｜规则或局部 expert 标注的跨步骤义务集合"
    }
  ]
}
