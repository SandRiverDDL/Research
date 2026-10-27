# Agentic OPD 方法选题：生成上下文

2026-10-14。用户要方法论文，具体贡献应是训练目标、监督构造或 teacher–student 交互机制；诊断只服务验证。文本多轮 agent/tool-use，排除 OPSD/同模型自蒸馏、多模态/VLA、benchmark-only。独立 teacher 可以固定或适配，但不能退化为纯 RL 或离线数据工程。此文件是生成上下文，非新颖性结论。

## 已知方法（事实；复用本地24篇调研）

完整原文入口和阅读边界见 ../research-wiki/awesome-agentic-opd-review.md。

- GKD (2306.13649): student-generated sequences 上做 teacher distribution matching。MiniLLM (2306.08543): reverse KL。不能将更换 KL 或普通 on-policy supervision 当核心新颖性。
- TCOD (2604.24005v3 §3): F2B增加student horizon；B2F执行teacher prefix再交接，改变训练状态分布。
- Guided-OPD (2606.15912v2 §3): 按turn概率teacher/student混合执行，逐渐撤去介入；student turns RKL，teacher turns FKL。
- DASH-OPD (2607.29078v4 §3–4): action likelihood-ratio积累+双阈值hysteresis双向交接。
- ReOPD (2607.04763v3 §4): 重放teacher histories，student自采样当前action但不执行，early-step-biased sampling，零student训练期tool calls。
- TurnOPD (2607.05804v2): probe-based rollout depth及turn-normalized KL，预算分配已有人做。
- SOD (2605.07725v3 §4): 高discrepancy step降权，混GRPO。ATOD (2606.27814v6 §4): disagreement/uncertainty soft-OR保留高分turn，OPD逐渐切RL。SAGE-OPD (2606.19659v1 §3): environment feedback和teacher判断Skip/Weak/Strong监督，非执行接管。
- FutureBridge (2608.01953v2 §3): 分叉环境，插入teacher bridge，再让student继续，按teacher-preferred-token比例改善选择bridge；成本含多条continuations。不是独立task-return评价。
- MemOPD (2608.07068v1 §3): 精确还原memory rewrite后invocation的position/visibility/action masks，再做full-vocab KL；接口对齐本身已有人做。
- MAD-OPD (2605.01347v1 §4): 多个独立teacher在student状态debate，以confidence组合token分布。KAT-Coder/MachMind: 领域expert路由、top-k support、suffix mask等配方。
- CAST (2607.25308v1 §3): 外部游戏solver的action value变turn advantage，特定条件联系OPD；solver/value teacher不新。
- DGPO (2508.20324v4 §4): teacher cold-start，student错误时加KL，正确时保留RL探索。

## 本轮新增原论文证据（HTML摘要/引言已读；尚未完成方法细查）

- OLIVE / Learning from Teacher Continuations at Student States (2609.36246): 每轮student生成prefix，teacher自回归续写，用teacher token CE更新student，含agent实验与black-box text teacher。简单“让teacher续写错误prefix再蒸馏”已有直接工作。
  https://arxiv.org/html/2609.36246
- SCOUT / On the Off-Policy Teacher in On-Policy Distillation (2609.38360): 周期性用student prefixes上teacher continuation的可验证reward训练teacher，伴随student OPD。简单“适配teacher到student错误分布”已有人做；当前摘要证据为reasoning场景。
  https://arxiv.org/html/2609.38360
- AC-OPD / Teacher Should Think Ahead (2609.22254): informative student states上teacher continuation，按uncertainty contraction/path divergence自适应监督长度。数学/代码，不能将adaptive teacher continuation作为完全空白。
  https://arxiv.org/html/2609.22254
- R2-OPD (2608.19408): 对reasoning spans的独立progress reward与teacher reward分别排序，冲突时屏蔽KD reward。只把teacher proxy换成进展/成功率来mask并非明显新方法。
  https://arxiv.org/html/2608.19408
- Counterfactual Recoverability (2608.04408): 原arXiv摘要：错误状态teacher continuation与rollback预算匹配比较，据结果保留/回滚/普通监督。HTML 404，当前仅摘要，细节待核。不能宣称recoverability-aware intervention完全没人做。
  https://arxiv.org/abs/2608.04408
- CROP (2608.13387): 原摘要，paraphrase校准counterfactual prompt sensitivity做token selective OPD。只换token重要性评分拥挤。
  https://arxiv.org/abs/2608.13387

## 发散的两个视角（解释，非已选方向）

1. supervision-object：改变学生究竟向teacher学什么；例如有外部环境语义的行动集合、可执行的规划对象、跨turn监督。应给出可计算loss/target及其与KL/CE/DAgger/AGGREVATE/LOLS的实质关系，避免仅改权重。
2. interaction-transfer：改变teacher帮助如何转化为student独立能力；例如teacher演示与student可执行策略之间的衔接、长程技能组合或无需teacher在线部署的训练闭环。不能只改intervention阈值、复用已有续写或rollback。

跨视角允许重复，只做机械去重。生成时不判死刑；新颖性在完整候选集上查证。每个idea必须是一个可解释的核心机制，明确失败风险，避免堆模块。最近邻的存在是需要比较的事实，不是自动排除。

## 可行性假设（不是用户已确认资源）

初步按0.6B–1.7B student、独立4B–8B teacher、文本可重置环境估计，GPU资源尚未提供；不承诺两小时能完成训练。先设计小规模可证伪pilot，所有成本计入teacher采样/评分、环境分叉及评测。此研究目录不启动训练。只有仿真中可获得的隐藏state不能泄漏给部署student；必须说明环境reset/branch和reward依赖。

补充邻近工作：Prep-OPD https://arxiv.org/html/2610.04950#S3 先在固定student prefixes上RL训练teacher完成题目，再冻结用于介入和KD；Relay-OPD https://arxiv.org/html/2607.26057#S3 用teacher/student reflection-token差异触发有限teacher段再交回student；CLOOPD https://arxiv.org/abs/2609.24141 在冻结teacher-scored batch上预算化多次student更新。前两篇已读方法，后一篇摘要。
