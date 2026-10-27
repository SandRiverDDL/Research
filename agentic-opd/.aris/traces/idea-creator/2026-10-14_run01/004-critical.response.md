本次是原生成者的续接评审，**不是独立科学验证**。16 项全部保留；现有证据不足以证明某篇具名论文完整包含其中一项，因此不判 ABANDON。低优先级表示当前增量或投入产出不够有说服力，不等于“没有新颖性”。所有预期收益均是假设，尚未运行 pilot。

依据[候选全集](/home/chy/notes/Research/agentic-opd/idea-stage/candidates-2026-10-14.json)及[查新证据](/home/chy/notes/Research/agentic-opd/idea-stage/novelty-evidence-2026-10-14.md)，必须收窄三类主张：semantic EOS 已明确使用等价事件概率求和；Relational KD 已转移跨样本关系；MetaDistil 已根据蒸馏后 student 反馈学习 teacher。剩余贡献必须落到具体 agent 学习机制。

下表的 control 均要求两种配套比较：先共享状态、候选和标签隔离机制，再固定**总成本**允许 baseline 把省下的开销用于普通训练。总成本包含 teacher、student、环境分叉、临时更新、评测和固定部署工作量，不能只匹配 rollout 数。

| ID | 技术问题与最强 reviewer objection | Decisive control | 可能的研究上限 |
|---|---|---|---|
| **A1** | 绝对类概率质量可计算，但少量 teacher 样本估计类分布很噪；即时效果相同不保证长期等价。**求和不是新原则**；相对 semantic EOS，剩余增量是 student 状态上通过执行发现等价关系。 | 同一候选及效应标签，比较类质量 loss 与将类权重分给成员的逐行动 CE；同时检验后续结果是否仍等价。 | 把表面不同、环境效果相同的 agent 行为作为可替代监督，减少不必要的路径模仿。 |
| **S1** | 候选归一化只约束集合内比例：所有候选的真实概率一起降低，loss 仍可能不变。除 A1 的新颖性风险，还存在“辨别好选项却不生成好行动”的落差。 | 同一候选比较 S1、A1 与逐行动 CE；同时测候选集真实概率质量，不能只测条件排序。 | 与 A1 相同，但当前公式对部署采样的连接较弱。 |
| **A2** | AST CE 和解释器可实现；分支正确性、开放任务表达及运行时优势是主要风险。Skill-DisCo 已有 PFSM 程序技能；剩余差异是**student 状态上由 teacher 生成尚未发生的条件策略**，不是编译成功轨迹。 | 将同一控制器全部分支展开成普通 action CE，并给两组相同工具接口及总推理预算。 | 从单路径 continuation 转向可执行局部反馈策略，可能改善未见返回组合。 |
| **A3** | Teacher 指针训练、student 指针部署存在暴露偏移；硬瓶颈可能删除长期必要状态。相对 MemOPD 是学习证据选择，而非接口对齐；但“教模型压缩上下文”仍是强近邻。 | 同一证据标签比较硬瓶颈、辅助指针监督但保留完整历史、等长摘要；加入 oracle 指针检查上限。 | 同时提高长历史可靠性并降低后续上下文成本。 |
| **S2** | 辅助 ledger CE 完全可算，但共享表示是否改变 actor 尚无理由保证；部署不用 ledger，容易成为普通 multitask SFT。 | 固定 action 数据及总 token，比较 ledger 与包含相同事实的普通摘要辅助任务。 | 低部署开销地改善状态追踪；目前方法增量偏薄。 |
| **S3** | 契约可解析时可算，但可能无正负对；给定偏好式受长度影响，也可能奖励“不行动所以不违规”。最强反驳是 teacher 写奖励规则后做普通轨迹偏好训练。 | 同一轨迹池比较契约偏好与 teacher 对最终任务进展的直接偏好；同时报告成功率和违规率。 | 转移跨轮义务，比单步行动标签表达更多时序结构。 |
| **A4** | 差分 log-odds 可算，但依赖 teacher scoring，尺度随行动长度变化；关系 loss 无法识别共同偏移。相对经典 Relational KD，增量只能是合法工具干预下的响应关系；CROP 是选择 token，不是该目标。 | 同一 h/h′、同一 teacher scores，比较成对关系项与两状态独立 KL。 | 明确改善反馈敏感性；但已有逐状态标签包含所需信息，额外收益可能有限。 |
| **S4** | **给定公式就是两项条件二分类 CE，没有跨状态耦合。** 不能将目标本身宣称为新的关系蒸馏；剩余贡献主要是合法反馈对的构造。 | 用同一反馈对运行条件 binary CE，应与原式数值等价；再比较完整行动 CE。 | 可检验反馈配对数据是否有效，但当前方法论文增量较弱。 |
| **A5** | 有限 option softmax 同样不约束集合外质量；固定 turn 数也不等于相同 token 长度。最强反驳是在线 listwise preference distillation，且需要高成本分叉。AGGREVATE/LOLS 已有 learner roll-in 后比较行动后果的框架。 | 同一已执行 option 池比较 listwise loss、teacher 选中轨迹 CE 和普通轨迹偏好训练。 | 将教学限制在 student 可实现策略内，但无法突破候选支持集。 |
| **A6** | 单次小更新在少量 sibling episodes 上的收益差很可能低于评测噪声。MetaDistil 已有 post-update feedback；相对 SmartAD 的实质差异是实际学习收益，而非 student NLL。 | 同一 demonstrations 比较学习收益选择、正确性加 student NLL 选择、全部训练；把影子更新和 probes 纳入预算。 | 识别“表现好却不好学”的监督，但每次重新选择的成本难摊薄。 |
| **A7** | 目标预测与执行误差相乘，teacher waypoint 也可能不可达。Sub-goal Distillation 已有 teacher 标 subgoal、planner/executor 和无 teacher 部署；剩余差异是 student 自己实现 waypoint 时的 on-policy 监督。 | 同一 waypoints 比较 oracle-path executor 蒸馏与 student-path OPD；部署都使用预测 waypoint，并比较普通 OLIVE。 | 学到不同于 teacher 路径的层级实现；不能把 subgoal 本身作贡献。 |
| **A8** | 固定 proposal 后编辑器可训练，但局部 patch 不能解决整体策略错误；允许任意替换又接近普通 CE。SCoRe 已有 teacher 修复 student 错误；剩余差异是部署时保留显式编辑算子。 | 相同 drafts、teacher 修复结果和两遍部署预算，比较 patch CE 与完整行动重写 CE。 | 降低近正确行动的修复成本；增益必须超过第二遍推理本身。 |
| **S5** | 与 A8 同家族；draft 与 editor 同时改变时，训练分布漂移更强。不同 edit serialization 不能构成独立方法贡献。 | 同一在线 drafts 比较局部编辑、完整重写和两遍普通 OPD；报告修复与误改。 | 实用纠错 policy，但编辑式 imitation 的近邻压力很大。 |
| **S6** | Outer-loop 可实现但收益噪声、probe 过拟合和 student 非平稳性严重。MetaDistil 已覆盖 learner-feedback 教师学习原则；相对 SCOUT/Prep，差异是优化**更新后 student 自主回报**，不是 teacher continuation 回报。 | 同一候选监督比较固定 teacher、teacher 自身回报适配、student 学习收益适配；总预算包括临时 student 更新和 teacher 更新。 | 若能跨 student checkpoints 泛化，可把昂贵教学搜索摊薄到后续监督。 |
| **S7** | 合法分支选择可实现，但 violation 尚无明确标定，最大困难分支可能很不自然。最强反驳是 adversarial curriculum；相对 BranchOPD，改变的是环境反馈而非 student continuation 采样。 | 共享合法分支池，比较 teacher 选择、随机选择和普通失败筛选；在自然分支频率下评测。 | 更有效地覆盖恢复状态；可能成立，但主要贡献容易落到数据课程。 |
| **S8** | 独立 teacher target 合规；但它依赖训练输入中被擦除的 hint/teach-back，可能增加标签方差。LENS 已有 hint 内化；剩余差异是独立 teacher 根据 teach-back 再标注，不能仅以排除 self-distillation 主张方法新颖。 | 相同状态和总 teacher tokens，比较直接 teacher、teacher 自审后回答、teach-back 后回答；最终均用独立 teacher 标签。 | 如果 teach-back 暴露独特执行缺口，可能提高标签针对性；否则只是更贵地得到原本可得的标签。 |

我只推荐**两个首验家族**，不为填满三个位置而降低门槛。排序是验证投资顺序，不是投稿成功率判断。

1. **环境效应等价监督，代表 A1；同家族 S1。**  
   A1 比 S1 更值得先试，因为其绝对概率质量直接连接部署采样。它比证据辅助任务 A3/S2、编辑 A8/S5、teach-back S8 更容易把贡献定位到一个明确监督对象；也比 A4/S4 更少依赖“已有标签再加一种正则”的解释。  
   **最佳情况：**证明状态依赖、执行验证的等价监督能在相同总成本下保留更多有效策略，并改善长程成功率。论文贡献必须是这项 agent 学习结果，不能是概率求和。  
   **现实成本：**按原方案每状态最多约 6 次单步分叉，主要前提是可靠恢复和效应判定；工程估计 1–2 人周不是 GPU 时长。  
   **证伪条件：**共享效应标签的逐行动 CE 同样有效；或短期等价无法延续到后续任务，导致效应标签本身失真。

2. **可执行条件策略监督，代表 A2。**  
   这是更高风险、也更可能改变监督表达能力的一项。相比 A7 的 subgoal、A5 的方案排序、S3 的契约偏好，它直接给出工具返回到行动的执行结构。相比 S7，核心结果可以落在学到的 policy 表示，而不只是更好的训练分支。  
   **最佳情况：**同样的 branch evidence 下，条件控制器比路径展开 CE 更能组合处理未见反馈，并减少决策调用。  
   **现实成本：**受限 DSL、解释器和分支核验约 2–3 人周的条件估计；深度 2、最多 4 条验证路径也会产生明显环境成本。它不属于低风险选项。  
   **证伪条件：**完整展开分支后优势消失；或者性能主要来自解释器提供的额外策略约束，而非 student 学到控制器。

**高上限备选是 S6，与 A6 同家族，但暂不占首验名额。** 相比 A6，训练 teacher 有机会摊薄昂贵的监督搜索；相比其余局部修正，它触及“teacher 能做成”与“student 能学会”的差异。不过 MetaDistil 已占据总体原则，当前方案还没有说明为何 agent 中高噪、非平稳的学习收益足以支持高效 outer loop。其最佳情况是跨 checkpoints 的教学收益迁移；直接证伪是收益偏好不可复现，或算入全部开销后输给 SmartAD 式选择、SCOUT 式 teacher 适配或固定 teacher 的普通 OPD。硬件尚未提供，不能把这一风险误写成已确认的预算淘汰。
