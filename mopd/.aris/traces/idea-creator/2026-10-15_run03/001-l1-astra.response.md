{
  "shard_id": "g17-l1-astra",
  "model": "gpt-6-astra",
  "candidates": [
    {
      "id": "L1-A1",
      "title": "用可核验的局部结论构成联合教学目标",
      "method_steps": [
        "student 自采样完整轨迹，每条只选一个已访问前缀；两个 specialists 各提出一个短结论或纠正，并附可执行证书，不要求提供完整解。",
        "证明检查器依据原始题设检验证书；它只检验给定证书，不搜索解答。将通过检查的局部动作合并为候选集，保留其来源。",
        "在该 student 前缀处，对认证动作集合做块级蒸馏；下一轮仍由 student 独立生成。不同 teacher 的必要结论由同一 student 逐渐掌握。",
        "部署只保留 student；若任务原本允许证明检查器，则所有对照同样可用。局部证书只在训练提供。"
      ],
      "minimal_formalism": "令 C(s) 为通过证书检查的局部动作，q(c|s)∝1[c∈C(s)]·Σ_i p_i(c|s)；在 student 访问的 s 上最小化 KL(q||πθ)，C(s) 为空则跳过。动作是一条短证明语句或纠正，不能把任意全文当一个免费动作。",
      "hypothesis": "【待验证】没有整题可靠 teacher 时，各 specialist 仍能提供互补且可认证的局部结论；其联合支持集足以产生可学习的完整策略。知识来自 specialists，可信性来自只检查局部证书的确定性工具。",
      "closest_known_work": "据指定笔记：TU-OPD §3.3–3.4 使用整题可靠性门槛及 winner residual；Trust §3 已有随位置变化的监督；MAD-OPD §4 已有交互监督。局部验证、证明蒸馏方面的重合待后续查新。",
      "claimed_delta": "候选干预是把监督许可单位从整题成功或内部可靠性 proxy 改为可认证的局部动作，并联合不同 teacher 的有效动作；不主张 Trust 普遍需要整题赢家。",
      "minimum_test": "先审计100道低整题可靠性题：联合认证动作是否比最佳单 teacher 多覆盖必要推导；再用1000条 student 轨迹短训。对照适用的 TU-OPD、Trust、MAD-OPD、同证书数据的离线训练、同检查预算RL及更强单teacher。若联合覆盖没有增量，可直接推翻首要前提。数据及证明环境 availability 待核。",
      "killer_result": "即使局部认证覆盖明显增加，student 的整题成功仍不超过同预算 Trust 或 checker-RL；或者有效证书实质上依赖一个已经能解完整题的外部模型。",
      "compute_assumptions": "工作假设≤8×3090，非用户预算。1.7B student＋两个1.7B LoRA specialists；若需制备，每个teacher用1万条512-token局部样例训练2轮，共20.48M训练tokens及2万次样例验证。主阶段2万条512-token student轨迹，抽2万个前缀；teacher各生成≤128 tokens，共5.12M；共享前缀缓存后，候选评分最多15.36M输出tokens＋20.48M前缀tokens，≤4万次证书检查。100题×2teachers×16次×512 tokens的可靠性审计另计1.64M生成tokens；报告置信区间，不声称证明teacher绝不会解。",
      "risk": "MEDIUM",
      "effort": "最小验证约1–2周；完整方法验证约4–6周。",
      "so_what": "若成立，可把整题失败但局部知识可靠的模型用于教学；若失败，可定位局部正确性与完整可学性之间的缺口。",
      "dedup_key": "认证局部动作支持集上的蒸馏＋specialist生成的可检查证书"
    },
    {
      "id": "L1-A2",
      "title": "联合排错：从多个不完整的反例专家获得监督",
      "method_steps": [
        "student 对每题独立生成4个完整候选；每位 teacher 只负责指出自己擅长的一类错误，并给一个具体反例。",
        "用可执行规格检查反例是否确实使候选违反要求；无效反例不参与监督。teacher 无须知道正确完整程序。",
        "合并经过验证的否决，将 student 在候选集合中的概率质量重新分配给未被否决者；全被否决则该组不更新。未被否决不被标注为正确。",
        "持续在新的 student 自采样候选上重复；部署移除 teachers，保留一个 student。"
      ],
      "minimal_formalism": "候选y₁…y₄由当前student采样，b_m=1表示不存在已验证反例；q_m∝stopgrad(πθ(y_m|x))·b_m，最小化−Σ_m q_m logπθ(y_m|x)，Σb_m=0时跳过。",
      "hypothesis": "【待验证】不同 teacher 虽不能生成正确整题解，却能发现互不重合的致命错误；经过联合排错得到的相对监督，比单 teacher 的正答案模仿更可靠。反例正确性由规格执行验证，错误发现仍来自teachers。",
      "closest_known_work": "据指定笔记：TU-OPD从可靠赢家提取正信号；Trust使用位移proxy；MAD-OPD依赖debate及自报confidence。反例驱动学习、拒绝采样和反馈型蒸馏存在潜在重合，未裁决。",
      "claimed_delta": "将多teacher的联合信息表示为可核验的排除集合，而非联合答案或token概率平均。该机制属于反馈型MOPD；其与等预算RL的实质差异必须验证。",
      "minimum_test": "100题各取4个student候选，只用最终验证器审计过滤前后的真实正确候选占比，并记录全否决率。随后1000题短训，对比单反例teacher、Trust、MAD-OPD、适用TU-OPD、同反例数据训练、等调用预算RL和更强单teacher。若联合排错不能提升正确候选占比，核心信号假设即失败。需要可执行规格，availability待核。",
      "killer_result": "联合过滤主要留下同时逃过专家检查的错误答案，或几乎所有组都全否决；又或全部收益被相同反例预算的RL复现，无法建立独立方法价值。",
      "compute_assumptions": "工作假设≤8×3090。1.7B student＋两个1.7B反例specialists；制备按两个teacher各1万条512-token局部反例样例、2轮计20.48M训练tokens，反例需逐条执行验证。2万题×4候选×512 tokens为40.96M student生成tokens；两个teacher读取候选最多81.92M tokens，分别输出≤64-token反例另计10.24M，最多16万次规格执行。只做整候选采样，不逐状态分叉；低整题可靠性审计另约1.64M teacher生成tokens。",
      "risk": "HIGH",
      "effort": "最小验证约1周；完整验证约4–6周。",
      "so_what": "检验“知道哪些解一定错”是否足以让多个不完整专家教出会整题求解的student，并明确其相对普通RL的价值边界。",
      "dedup_key": "联合认证否决后重分配student候选概率＋specialist反例"
    },
    {
      "id": "L1-A3",
      "title": "投影答案蒸馏：让每位 teacher 只监督自己能解的部分",
      "method_steps": [
        "限定有确定性输出投影的任务，例如同一结构化答案同时包含符号关系和单位或类型。投影器只解析共享实体与字段，不求解题目。",
        "每位 specialist 只学习并评分自己负责的投影答案；完整题仍可能超出任一teacher的稳定能力。",
        "student 自采样4个完整答案；对每个答案提取所有投影，以各teacher对投影的概率乘积构成联合候选目标，再蒸馏回原student。",
        "部署student直接生成完整答案；不调用投影teachers。最终正确性验证只用于评测和公平RL对照。"
      ],
      "minimal_formalism": "给定固定解析投影φ_i及student候选y_m，q_m∝exp(Σ_i λ_i log p_i(φ_i(y_m)|x))；固定投影长度口径后，最小化−Σ_m stopgrad(q_m)logπθ(y_m|x)。λ_i在独立局部校准集上固定，不依赖整题赢家。",
      "hypothesis": "【待验证】teacher在可解投影上的概率比其完整答案概率更有信息；多个投影共同约束同一组实体时，可从student候选中识别联合有效解。主要风险是各投影分别合理却联合矛盾。",
      "closest_known_work": "据已有输入：Trust已有token分配，SMOPD已有同prompt多目标整合，AVSD已有geometric consensus，H-OPD已有信息桥接。该候选与product-of-experts及部分标签学习的重合需查新。",
      "claimed_delta": "改变teacher被要求预测的对象：学习可求解的部分答案分布，再约束同一个完整student答案；不是把多个完整解分布直接平均。",
      "minimum_test": "100道低整题可靠性题各采4个答案，检验联合投影分数是否比完整答案聚合更能识别真实正确答案；打乱跨teacher实体对应关系应破坏该收益。短训对照Trust、MAD-OPD、适用TU-OPD/SMOPD、同投影数据离线训练、同评分预算RL及获得全部局部数据的单teacher。现成任务、投影器及专长分离是否成立均待核。",
      "killer_result": "联合投影分数系统性偏好部分正确但整体非法的答案；或必须加入能够解决整题的约束求解器才能有效。",
      "compute_assumptions": "工作假设≤8×3090。1.7B student＋两个1.7B projection specialists；制备按每个1万条512-token投影样例×2轮，共20.48M训练tokens，局部样例验证成本另记录。2万题×4×512为40.96M student生成tokens；每个投影≤128 tokens，共20.48M teacher评分tokens；每题每teacher缓存一次≤512-token输入，另20.48M前缀tokens。无teacher整题生成、逐状态probe或分叉；可靠性审计另约1.64M生成tokens。",
      "risk": "HIGH",
      "effort": "最小验证约1–2周；完整验证约4–8周。",
      "so_what": "若成立，教学资格可以定义在可求解投影而非完整任务上；若失败，可给出部分答案监督不足以确定联合能力的明确反例。",
      "dedup_key": "完整student候选上的投影概率乘积蒸馏＋specialist部分答案分布"
    },
    {
      "id": "L1-A4",
      "title": "直接训练 teacher 的联合教学收益",
      "method_steps": [
        "从两个已有专长teacher出发；在同一student前缀，各输出≤128-token局部提示，不要求提供完整答案。",
        "冻结的当前student副本读取两份提示，在原student前缀上给出下一token目标；实际student不看提示，只学习该条件目标。",
        "抽取少量批次做一次临时student更新，再测未见组合题上的成功率变化；把这个真实教学增益作为两位teacher提示策略的共同奖励，更新teacher LoRA。",
        "交替优化提示策略与常规OPD；最终冻结teachers完成蒸馏，部署只保留无提示student。"
      ],
      "minimal_formalism": "q=p_stopgrad(θ)(·|s,h₁,h₂)，θ′=θ−α∇θ KL(q||πθ)；teacher消息策略通过REINFORCE最大化R=Acc_V(θ′)−Acc_V(θ)，V与产生提示的训练题分离。",
      "hypothesis": "【待验证】最会独立解题的teacher不一定最会提供联合可学信号；直接奖励共同教学增益，可使各teacher输出互补且能被student吸收的局部知识。必要知识来自初始专长训练，验证信号是实际student答案的任务检查结果，不是假设的局部oracle。",
      "closest_known_work": "据指定笔记：TU-OPD已经联合考虑teacher制备与压缩；MAD-OPD已经把交互context藏于teacher侧。已有输入还包含privileged-context蒸馏。与元教学、learning-to-teach和协作RL的重合待查。",
      "claimed_delta": "核心改变是teacher制备目标：从teacher自身的整题成功改为两个teacher共同造成的实际student学习增量；条件student副本仅是目标生成器，没有引入更强完整solver。",
      "minimum_test": "用8个meta轮次、每轮4组提示试验，比较可训练提示与固定提示在独立组合题上的配对教学增益；随后做短OPD。对照MAD-OPD、Trust、适用TU-OPD、固定提示同数据训练、获得全部局部数据的单teacher，以及把全部meta验证预算用于student RL。去掉任一teacher应使联合增益下降。任务检查器和专长样例availability待核。",
      "killer_result": "提示只帮助临时student记住训练题，不能提高未见组合；或额外student RL、更强单teacher在相同总预算下完全解释收益。",
      "compute_assumptions": "工作假设≤8×3090。1.7B student和两个1.7B LoRA teachers；初始专长制备仍按20.48M训练tokens及2万次局部样例验证计。主训练2万条512-token轨迹：teacher消息5.12M＋前缀读取20.48M tokens，条件student副本最多25.6M输入/评分tokens。64个meta轮次×4试验×16训练题的一步临时更新约2.10M训练tokens；每试验16验证题、更新前后各采一次，另4.19M生成tokens及8192次任务验证；meta消息另约1.05M生成tokens。临时更新串行复用，不假定免费双层优化。",
      "risk": "HIGH",
      "effort": "最小验证约2–3周；完整验证约6–10周。",
      "so_what": "把多teacher互补性从事后聚合属性变成可训练的教学目标；失败则能判断这种目标是否只是在昂贵地重做student RL。",
      "dedup_key": "以实际student更新后的联合泛化收益训练teacher提示策略＋任务验证器"
    }
  ]
}
