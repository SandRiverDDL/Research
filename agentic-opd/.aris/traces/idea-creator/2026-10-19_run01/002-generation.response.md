{
  "shard_id": "sol",
  "candidates": [
    {
      "id": "SOL-01",
      "name": "观察差分策略蒸馏",
      "dedup_key": "observation-differential-policy-response",
      "method": [
        "从自然rollout匹配同一页面或工具状态、关键属性不同的观察对，校验可用动作兼容。",
        "让teacher输出两侧短action分布，student学习动作概率变化；对无关属性变化学习不变性。",
        "把成对训练与原有OPD、terminal RL联合，真实交互继续由student采样。"
      ],
      "core_assumption": "猜测：部分错误来自策略忽略新证据；单点模仿不足以传递正确的观察响应。",
      "atod_basis": "事实：§4.3只计算单个状态的token统计；D.2出现错size与重复点击。解释：这些诊断尚未检验策略对关键观察变化是否敏感。",
      "nearest_work_and_overlap": "ActionOPD已做语义action监督，GC-OPD利用执行证据；新增假设是跨状态响应差分，可能与反事实数据增强重合。",
      "minimum_experiment_and_falsifier": "WebShop属性选择，对比ATOD、ActionOPD及普通成对增广。若收益完全由额外样本解释，差分机制被否证。",
      "scaling_cost": "每10条轨迹抽一对，每对两次短teacher动作预测；无环境分叉，额外成本随配对率和动作候选数增长。",
      "main_risk": "观察配对可能遗漏隐藏状态；teacher差分也可能错误。",
      "related_sources": ["https://arxiv.org/abs/2610.19820", "https://arxiv.org/abs/2609.37522"]
    },
    {
      "id": "SOL-02",
      "name": "证据锚定的信念撤销蒸馏",
      "dedup_key": "grounded-belief-retraction-operator",
      "method": [
        "teacher批量标注轨迹中被当前观察推翻的旧判断，输出“撤销旧判断—引用新证据—更新判断”。",
        "只保留证据时间不晚于当前turn的标签，训练student生成短更新操作。",
        "让动作策略读取student自身更新结果，并联合OPD与环境奖励训练。"
      ],
      "core_assumption": "猜测：错误prefix压低监督价值，部分原因是模型持续沿用已经失效的内部判断。",
      "atod_basis": "事实：§1、C.6讨论错误prefix使teacher信号失真；§4仅改变监督权重。解释：未显式训练撤销与更新错误判断的操作。",
      "nearest_work_and_overlap": "MemOPD涉及memory state；OPID、GC-OPD涉及hindsight/context。新增点须落在可验证的撤销操作，不能仅换一种memory摘要。",
      "minimum_experiment_and_falsifier": "WebShop改选属性、ALFWorld错误位置判断；对比普通摘要与同长度teacher解释。若撤销标签无额外贡献，机制被否证。",
      "scaling_cost": "每条失败轨迹一次批量标注；student只在候选冲突处输出短更新。成本随失败率与标签长度增长。",
      "main_risk": "未来信息泄漏；引用存在也不能保证逻辑关系正确。",
      "related_sources": ["https://arxiv.org/abs/2606.26790", "https://arxiv.org/abs/2609.37522"]
    },
    {
      "id": "SOL-03",
      "name": "环境效果商空间蒸馏",
      "dedup_key": "transition-effect-equivalence-distillation",
      "method": [
        "从自然交互学习action到环境变化的表示，并将相同效果的动作归为上下文相关等价类。",
        "teacher提出少量action候选，监督student对效果类分配概率，而非要求选择同一表面动作。",
        "用实际后续观察拆分错误等价类，再联合terminal RL优化类内选择。"
      ],
      "core_assumption": "猜测：大量teacher disagreement对应表达或路径差异，效果层监督能保留有效探索。",
      "atod_basis": "事实：§4.3使用token差异；D.2存在重复点击。解释：token与语义action均未必刻画真正的状态改变。",
      "nearest_work_and_overlap": "ActionOPD已做语义agreement；本候选要求由真实转移学习效果等价。若其agreement已充分表达效果，则可能高度重合。",
      "minimum_experiment_and_falsifier": "WebShop及ALFWorld加入动作别名和等价路线；与ActionOPD、规范化动作基线比较。若仅别名规范化即可复现，贡献被否证。",
      "scaling_cost": "小型效果编码器复用已有转移；抽样turn生成2—4个短teacher候选，无逐状态环境试跑。",
      "main_risk": "相同即时观察可能隐藏不同长期后果，错误合并会损害规划。",
      "related_sources": ["https://arxiv.org/abs/2610.19820"]
    },
    {
      "id": "SOL-04",
      "name": "部分序目标契约蒸馏",
      "dedup_key": "partial-order-goal-contract-options",
      "method": [
        "teacher为任务生成少量带前置条件、完成条件的子目标及依赖关系，允许独立子目标交换顺序。",
        "student根据当前观察识别已满足契约，选择可执行子目标，并接受条件化OPD。",
        "把可观测的契约完成作为局部训练反馈，terminal奖励决定最终策略。"
      ],
      "core_assumption": "猜测：小模型缺失的是可组合的依赖结构，单纯延长轨迹或模仿顺序难以补齐。",
      "atod_basis": "事实：§3.2把整轨advantage复制到所有token；D.2展示clean再place的依赖。解释：turn weighting未提供子目标边界或依赖监督。",
      "nearest_work_and_overlap": "ArCHer涉及层次RL，TCOD控制时间课程，GC-OPD使用执行图；须证明目标契约与已有skill层次方法的区别。",
      "minimum_experiment_and_falsifier": "ALFWorld未见目标组合、WebShop约束组合；比较线性teacher计划。若部分序结构不改善重组泛化，核心假设失败。",
      "scaling_cost": "每个任务一次teacher图生成，可跨G条rollout复用；契约检测由小头或环境已有结构实现。",
      "main_risk": "契约难以自动验证；手工领域规则可能承担主要收益。",
      "related_sources": ["https://arxiv.org/abs/2604.24005", "https://arxiv.org/abs/2609.37522"]
    },
    {
      "id": "SOL-05",
      "name": "Teacher证据后验的势函数蒸馏",
      "dedup_key": "teacher-evidence-posterior-potential-credit",
      "method": [
        "在有训练答案的Search-QA中，teacher评分正确答案在少量prefix下的条件概率，训练student状态势函数。",
        "用前后势函数差形成逐turn奖励，终点势设零，并训练对应的residual critic。",
        "结合环境奖励优化查询与停止决策；每次rollout冻结势函数，保持奖励望远镜抵消。"
      ],
      "core_assumption": "猜测：teacher对证据充分性的知识比其具体查询策略更容易传递，并能改善长程credit。",
      "atod_basis": "事实：§3.2使用整轨回报；Search-QA限制4步且仍有teacher差距。解释：当前方法没有直接监督证据获取的状态价值。",
      "nearest_work_and_overlap": "与经典potential shaping、value distillation及reward extrapolation邻近；必须证明teacher证据后验提供额外价值。",
      "minimum_experiment_and_falsifier": "查询上限4/8/16，加入无关检索；比较ATOD加普通critic、teacher初始化critic。若普通critic等效，方法贡献不足。",
      "scaling_cost": "每轨迹抽两个prefix评分答案；增加小value head，无teacher环境续跑。成本随答案长度和抽样边界数增长。",
      "main_risk": "teacher先验知识可能掩盖证据作用；势函数近似误差会影响有限样本优化。",
      "related_sources": ["https://arxiv.org/abs/2602.12125"]
    },
    {
      "id": "SOL-06",
      "name": "外部Teacher纠正信号的在线摊销",
      "dedup_key": "amortized-external-teacher-correction-model",
      "method": [
        "在固定比例的完整student轨迹上查询teacher，获取真实token log-prob纠正信号。",
        "用冻结student特征训练小型纠正预测器，并以保留的teacher标签校准误差。",
        "其余轨迹使用预测信号；优先刷新高预测误差轨迹，同时保留随机teacher查询下限。"
      ],
      "core_assumption": "猜测：teacher纠正信号具有可压缩结构，足以用低成本模型覆盖常见状态。",
      "atod_basis": "事实：Algorithm 1先计算teacher相关统计再gating。解释：较低turn权重本身不减少取得teacher信号的成本。",
      "nearest_work_and_overlap": "邻近proxy-teacher、active distillation和GC-OPD的复用机制；目标始终来自外部teacher，须避免漂成自生成监督。",
      "minimum_experiment_and_falsifier": "固定总teacher FLOPs比较ATOD抽样查询、随机缓存和在线摊销；若预测误差累积使收益消失，压缩假设失败。",
      "scaling_cost": "teacher计算约为原来的查询比例f，加全轨迹小预测头；扫描长prefix的成本仍须实测。",
      "main_risk": "student持续变化造成分布漂移；预测器置信度可能无法识别系统误差。",
      "related_sources": ["https://arxiv.org/abs/2609.37522"]
    },
    {
      "id": "SOL-07",
      "name": "可逆错误的交互式免疫训练",
      "dedup_key": "reversible-error-inoculation-on-policy",
      "method": [
        "teacher从环境暴露的可逆动作中选择一次有教学价值的偏离，如错误选项或绕路。",
        "在少量真实student轨迹中执行该偏离，随后由student自主恢复并接受teacher监督。",
        "注入动作不进入actor loss；根据实际恢复成功率调整错误类型，持续保留正常rollout。"
      ],
      "core_assumption": "猜测：自然on-policy采样对稀有、可恢复错误覆盖不足，导致部署时恢复能力脆弱。",
      "atod_basis": "事实：C.6深turn主要来自已经偏离的轨迹；D.2有错误后恢复案例。解释：ATOD接受自然错误分布，未主动组织恢复经验。",
      "nearest_work_and_overlap": "DASH、STI-OPD、TCOD使用teacher介入或课程；FutureBridge检验续接。新增点是有预算的可逆错误教学，可能与recovery curriculum重合。",
      "minimum_experiment_and_falsifier": "未见错误组合与正常成功率双测；等环境步数比较随机扰动。若随机扰动等效或正常表现下降，教学假设失败。",
      "scaling_cost": "例如10%轨迹额外2—4步；无需reset分叉，成本由注入率和恢复长度控制。",
      "main_risk": "表面可逆不代表任务预算内可恢复；teacher可能挑选过易错误。",
      "related_sources": ["https://arxiv.org/abs/2610.10878", "https://arxiv.org/abs/2604.24005"]
    },
    {
      "id": "SOL-08",
      "name": "黑盒Teacher的条件密度比蒸馏",
      "dedup_key": "blackbox-conditional-action-density-ratio",
      "method": [
        "在抽样student状态上取得少量teacher短action，与同状态student动作组成来源分类数据。",
        "训练条件判别器，使用其logit近似teacher与当前student的action密度比。",
        "以该比值提供OPD信号并结合真实奖励；随student更新刷新负样本，监督作用于可执行action。"
      ],
      "core_assumption": "猜测：分布层监督能保留teacher的多种有效策略，并支持无logits、异tokenizer教师。",
      "atod_basis": "事实：§3.3 Eq.6依赖teacher token概率，实验使用同模型家族。解释：黑盒teacher下的有效监督形式尚未检验。",
      "nearest_work_and_overlap": "ActionOPD已解决黑盒语义监督；GAIL已有密度比判别。新增价值须来自低查询预算的条件分布估计，重合风险较高。",
      "minimum_experiment_and_falsifier": "同teacher样本预算比较ActionOPD、teacher-action SFT及密度比方法；若模式覆盖与成功率无收益，分布匹配假设失败。",
      "scaling_cost": "仅抽样状态请求1—2个短action，加小判别器；不执行teacher续轨，成本随查询率线性增长。",
      "main_risk": "判别器可能识别语言风格而非决策质量；稀疏状态监督造成比值偏差。",
      "related_sources": ["https://arxiv.org/abs/2610.19820", "https://arxiv.org/abs/1606.03476"]
    }
  ]
}
