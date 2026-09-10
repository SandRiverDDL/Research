# Research Proposal: BranchFront-OPD——面向长程工具 Agent 的首次关键分歧课程

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token 或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

## Technical Gap

现有近邻已覆盖本想法的大部分表面动作：PACED 用 pass rate 选择能力边界；SOD 用 step divergence 降低坏 step 的监督；Prune-OPD 以 top-k overlap 检测 prefix drift 并截断；TCOD、Guided-OPD 和 TurnOPD 控制 trajectory depth 或 teacher intervention；ReOrder-OPD 已经根据 teacher continuation reliability 静态或动态重排 prompt；Relay-OPD 在早期 reasoning trigger 让 teacher 短暂接管。

尚未被这些方法直接回答的问题是：**长程 agent prompt 的训练价值能否由“当前学生在第几个有因果后果的动作边界首次偏离可行教师策略”来刻画，并把这个边界的后移作为在线学习进度？**

原始版本的两个风险必须修正：

1. “越早越好”同时混合了高杠杆与不可学习。第一个 turn 就分歧，可能是最值得修复，也可能说明 prompt 完全超出 student support。
2. “tool 不同”容易观察，但不容易判错。两个不同工具或参数序列可能到达 execution-equivalent 的同一成功状态；直接监督 teacher 的工具选择会压掉有效备用路线。

### 两条候选路线

- **Route A：无学习控制器的关键分歧前沿**。在动作边界做结构化分歧检测，用环境可验证的短程后果过滤伪分歧；按首次关键分歧的位置、可修复性与历史边界移动更新 prompt 概率。动作分叉后只完成当前结构化 action 并停止该 rollout 的后续 OPD。
- **Route B：训练一个 prompt/recoverability value model**。预测每个 prompt 的首次分歧位置和更新收益，再做 bandit sampling。

选择 Route A。Route B 与已有 PCL/ReOrder-OPD 过近，又引入 predictor calibration 和额外数据闭环。Route A 更直接检验用户提出的 agentic mechanism，并保持零新增可训练模块。

## Method Thesis

- **One-sentence thesis**：长程 agent OPD 应围绕随训练向后移动的“首次可修复关键动作分歧前沿”分配 prompt 与 rollout 预算，而不是围绕整题 50% 正确率或未经语义化的局部 KL。
- **Why this is the smallest adequate intervention**：只改变 prompt sampler 和 rollout stop boundary；teacher、student、OPD objective 与 agent policy 均保持不变。
- **Why this route is timely**：已有工作分别解决 prompt ordering 与 suffix reliability，但尚未把 agent action fork 的位置、动态 prompt acquisition 和 post-fork 监督边界连成一个可检验的机制。

## Contribution Focus

- **Dominant contribution**：以首次关键动作分歧的动态后移定义 agentic OPD 的 prompt learning frontier，并据此在线分配 prompt 概率。
- **Supporting contribution**：使用 action-boundary truncation 保证 sampler 观测与实际训练预算一致；它是可靠实现条件，不宣称为独立 novelty。
- **Explicit non-contributions**：不发明新 KL、不训练新 critic、不做 teacher relay、不提出新的 agent architecture。

## Proposed Method

### Complexity Budget

- **Frozen / reused backbone**：标准 student rollout、冻结 teacher scoring、reverse-KL OPD、现有 agent benchmark 和 verifier。
- **New trainable components**：0。
- **New state**：每个 prompt 的最近首次关键分歧深度、可修复标志、访问次数和边界移动 EMA。
- **Tempting additions intentionally not used**：value model、LLM judge、learned semantic action encoder、teacher takeover、trajectory rewrite。

### System Overview

```text
prompt x ~ current sampler
    -> student interacts turn by turn
    -> at every action boundary, teacher scores the same student prefix
    -> canonicalize actions and test consequential disagreement
    -> first repairable critical fork d_x
    -> train prefix through the complete divergent action
    -> stop before post-action observation suffix is distilled
    -> update d_x / learning-progress state
    -> refresh prompt probability
```

### Core Mechanism

#### 1. 从 raw disagreement 到 critical disagreement

在第 j 个 agent state `h_j`，student 生成结构化 action `a_j^S`，teacher 在相同 prefix 上给候选 action `a_j^T`。

首先把工具名、参数和终止动作解析成 canonical action。若两者不同，不立即认定为错误；仅在以下条件满足时记为关键分歧：

1. 两个 action 不属于已知 execution-equivalent class；
2. teacher action 在环境中可执行；
3. 通过可 clone state 的短程分支测试，teacher branch 相对 student branch 有更高的可验证 progress / success，或 student action 立即 invalid。

首次满足条件的 turn 记为 `d_k(x)`。若整条轨迹没有关键分歧，令其为 horizon `T_x`；若 teacher branch 也无法改善，则标记为不可修复，而不是“最难、最高优先级”。

#### 2. Prompt priority

第一版使用可解释、无训练参数的优先级：

\[
u_k(x)=\frac{\underbrace{(1-\tilde d_k(x))}_{\text{early-fork leverage}}
\cdot\underbrace{r_k(x)}_{\text{repairability}}
\cdot\underbrace{(\epsilon+\ell_k(x))}_{\text{recent frontier movement}}}
{\underbrace{c_k(x)}_{\text{measured token / wall-clock cost}}},
\]

其中 `d` 按有效 horizon 归一化；`r` 来自环境分支验证；`ell` 是同一 prompt 最近两次访问间首次关键分歧向后移动的 EMA；`c` 是该 prompt 实际 student generation 与 teacher scoring 成本。采样分布为 uniform exploration 与归一化 `u` 的混合，避免未访问或暂时停滞的 prompt 永久饿死。

这个公式保留“早期错误的后果更大”这一动机，但不允许单靠位置获得高概率：过早且 teacher 无法修复、或长期不发生边界移动的 prompt 会被降权。若最小 pilot 显示 `1-d` 与真实 update gain 不单调，则删除 earliness 项，退化为纯 learning-progress sampler；不能为维护原直觉而保留错误项。

#### 3. Action-boundary truncation

一旦在 turn `d_k(x)` 发现关键 action fork：

- 保留此前可信 prefix 的 OPD loss；
- 继续到当前结构化 tool call 完整闭合，使 student 获得对关键 action 的监督；
- 不把执行 student action 后得到的新 observation 及其长 suffix 纳入本条 rollout 的 OPD。

因此“分歧后若干 token”不是固定 `L`，而是到最近的语义 action boundary。固定 token window 会切断 JSON/tool arguments，或越过环境 transition 后继续监督不同世界状态。

### Modern Primitive Usage

- **Primitive**：冻结 LLM teacher 作为 student-visited state 上的 action scorer；环境 verifier / clone state 作为短程反事实分支检查器。
- **Exact role**：teacher 提供候选替代动作，环境判断这个分歧是否有后果与可修复；二者职责不混用。
- **Why natural**：长程工具任务的状态转移由 action boundary 决定，直接使用环境 transition 比 token embedding 或 LLM-as-judge 更可归因。

### Integration into Base Pipeline

训练时只在 dataloader 前增加 prompt priority table，在 rollout engine 中增加 action-boundary hook 和 stop flag。模型更新仍为标准 OPD。推理时完全移除 sampler、teacher 与分歧检测器，student 按原 agent policy 运行。

### Training Plan

1. 冷启动：每个 prompt 至少 probe 一次，记录首次 raw action disagreement、首次 critical disagreement、成功率、成本。
2. 在线阶段：按混合优先级采样；对访问 prompt 更新 `d/r/ell/c`。
3. rollout：仅蒸馏到首个关键 action boundary；无关键分歧则允许完整 trajectory 或沿用统一最大 horizon。
4. 每隔固定 update 刷新长时间未访问 prompt 的 priority；不全池重 rollout，避免 ReOrder-style refresh 成本吞掉收益。

### Failure Modes and Diagnostics

- **多合法路线被错判**：比较 raw tool disagreement 与 execution-equivalence-aware disagreement；报告替代路线保留率和 tool-outage robustness。
- **越早分歧其实越不可学**：做 matched causal intervention；若 early bin 的一次更新收益不高，移除 earliness 项。
- **分歧延后只是输出变长**：使用 turn/action index 与任务进度归一化，不能只用 token position。
- **teacher action 也错**：teacher branch 必须通过环境 validity/progress；无法验证时 `r=0` 或进入 uniform exploration，不作高优先级样本。
- **priority stale / starvation**：保留固定 uniform mass 和 age bonus；记录有效样本比例及重复访问集中度。
- **截断只省计算却丢失深层能力**：与 full rollout、Prune-OPD、TurnOPD 做 matched-token 与 matched-wall-clock 对照，并报告深层 turn 成功率。

### Novelty and Elegance Argument

- 相比 PACED：不是 prompt pass rate frontier，而是 agent state tree 中的 first critical action-fork frontier。
- 相比 Prune-OPD/SOD：它们在已采样 trajectory 内截断或重加权；本方法把已观测 fork 转成下一轮 prompt acquisition 信号。
- 相比 TCOD/TurnOPD：它们控制全局或 batch-level trajectory depth；本方法维护 per-prompt、随学生变化的分歧边界。
- 相比 ReOrder-OPD：后者按 teacher continuation reliability 排序，主要验证数学/代码；本方法按 agent action fork 的位置与学习进度重复采样，并显式避免 execution-equivalent tool disagreement。
- 相比 Relay-OPD：后者在 trigger 处让 teacher 接管；本方法不修改 rollout source，重点是选择哪一个 prompt 再训练以及在哪里停止不可靠 suffix。

该故事能否成立取决于一个必要发现：first critical action-fork depth 必须比 pass rate 和局部 divergence 更能解释 OPD update gain。若这个发现不存在，当前组合会退化为 ReOrder-OPD + Prune-OPD 的增量拼接，应当停止。

## Claim-Driven Validation Sketch

### Claim 1：首次关键动作分歧是 OPD prompt value 的有效、OPD-specific 指标

- **Minimal experiment**：在一个可 clone、含多条等价工具路径的确定性 tool-DAG 环境，对同一批 prompt 记录 pass rate、平均 KL、首次 raw tool disagreement、首次 critical disagreement。分别在 divergence 处做 teacher-action substitution 与不干预的 paired rollout，并对分箱 prompt 做单次/短程 OPD 更新。
- **Baselines / ablations**：pass-rate `p(1-p)`、mean KL、raw earliest disagreement、teacher-success/reliability、random；去掉 equivalence filter、去掉 repairability gate。
- **Metric**：counterfactual success uplift、one-update validation gain、Spearman ranking、替代路线保留率。
- **Expected evidence**：只有 critical + repairable divergence depth 能稳定预测干预收益和训练收益；raw tool disagreement 在多合法路线中明显失效。

### Claim 2：动态前沿采样在固定 compute 下优于正确率课程与静态 ordering

- **Minimal experiment**：在 ALFWorld 或同等级长程 agent benchmark 上，以同一 teacher/student、总 rollout token、teacher-scored token 和 optimizer update，比较 uniform、50%-pass curriculum、ReOrder-style reliability order、static first-divergence、dynamic BranchFront。
- **Metric**：success/score 对 teacher-scored token 与 wall-clock 的曲线、达到固定 success 的成本、分歧深度随训练的右移、prompt 访问集中度。
- **Expected evidence**：动态方法产生可观测的 frontier migration，并在 matched compute 曲线上占优；仅按早期分歧静态排序不应与完整方法等价。

### Claim 3：action-boundary truncation 避免 post-fork 错误监督而非简单缩短序列

- **Minimal experiment**：full suffix、固定 token `+L`、Prune-OPD top-k truncation、立即 action-boundary stop；再加入等 token 随机截断对照。
- **Metric**：post-fork teacher continuation success、success rate、deep-turn behavior、训练 token 与 wall-clock。
- **Expected evidence**：语义边界截断在相同 token 下优于随机/固定长度，且不会出现 JSON/tool-call 截断错误。

## Experiment Handoff Inputs

- **Must-prove claims**：earliest critical fork 与真实 update gain 的关系；动态 frontier migration；matched-compute 改善。
- **Must-run ablations**：raw vs critical disagreement、earliness vs learning progress、repairability gate、equivalence filter、full vs boundary truncation。
- **Critical datasets / metrics**：先用可 clone tool-DAG 做因果 pilot，再用 ALFWorld/WebShop 类 benchmark；success、counterfactual uplift、teacher token、wall-clock、route diversity。
- **Highest-risk assumptions**：teacher alternative action 可可靠验证；environment state 可 clone；边界后移代表能力提升而不是更冗长推理。

## Compute & Timeline Estimate

- **Pilot**：1.5B–1.7B student、7B–8B teacher、单个可 clone 环境；约 100–250 GPU-hours，1–2 周完成诊断与短程更新实验。
- **主实验**：2 个 agent benchmark、4–5 个 sampler、3 seeds；依据 TurnOPD 公开配置，预计 1,000–2,000 H20/A100-equivalent GPU-hours，另需较高环境并发工程成本。
- **Go/no-go**：先只投入 pilot；若 critical divergence 对 one-update gain 的排序不稳定，或不优于 ReOrder-style reliability，不进入大规模训练。

