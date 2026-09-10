# Research Proposal: ForkProgress-OPD——以已确认的因果 Action-Fork 进度驱动 Agent Prompt Acquisition

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token 或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

### Operational interpretation

`earlier-first` 是待验证 hypothesis，不是默认 sampler 的公理。主方法优先采样 teacher 替代 action 确实能改善 terminal outcome、且 first fork 已被连续观测为随训练向后移动的 prompt。只有受控 pilot 证明 earliness 在控制 branch advantage、成本和初始能力后仍预测 update gain，才加入 early multiplier。

## Technical Gap

PACED 类方法按 pass rate 选 prompt；ReOrder-OPD 按 teacher continuation reliability 排序；Prune-OPD、SOD、TCOD、Guided-OPD、TurnOPD 和 Relay-OPD 已覆盖 trajectory 内的 weighting、depth、truncation 与 teacher intervention。仍缺的量是：

> 在同一个 student-visited agent state 上，teacher alternative action 是否在配对 terminal continuation 中真正改变结果，以及这个 first action fork 是否随 OPD 训练稳定后移？

ForkProgress-OPD 只贡献这个 action-local statistic 及其 repeated prompt acquisition。标准 OPD、decision-complete teacher logits 和 action-boundary mask 在 sampler 对照中固定。

## Method Thesis

- **Thesis**：在可 replay 的 deterministic tool environment 中，teacher-continuation action advantage 可过滤表面工具分歧；其已确认的 first-fork movement 可作为 agent OPD 的 prompt acquisition signal。
- **Dominant contribution**：causally grounded repeated prompt acquisition。
- **New trainable components**：0。
- **Inference overhead**：0。

## Exact Scope and Fixed Choices

1. Environment 可 snapshot，或可由 action prefix 确定性 replay；terminal verifier `V∈{0,1}`；最大 horizon `H` 固定。
2. Student 与 teacher 使用同一 JSON action schema；只 canonicalize 空白、字段顺序和数值格式。
3. Continuation policy `π_C` 固定为 frozen teacher 的 greedy constrained decoder；两个 branch 都运行剩余 `H-j` turns。
4. Action boundary 使用 full-vocabulary teacher logits，或强制包含全部 tool-entry/stop token 的 decision-complete support；所有 sampler 相同。
5. Primary cost 是固定硬件、固定 worker 配置下的 end-to-end wall-clock seconds；teacher/student tokens、environment steps、accelerator-seconds 只作单独资源曲线。

结论明确局限为 teacher-continuation-relative、simulator-grounded，不外推为开放网页 agent 的无 oracle 方法。

## Core Mechanism

### 1. Teacher-continuation action advantage

对 prompt `x` 的 current-student trajectory，在 turn `j` 的同一 pre-action history `h_j`：

\[
a_j^S\sim\pi_S(\cdot|h_j),\qquad
a_j^T=\operatorname{Greedy}_{JSON}(\pi_T(\cdot|h_j)).
\]

若 canonical actions 相同则继续；若不同，snapshot `h_j`，分别执行 `a_j^S` 与 `a_j^T`，随后两边都由同一 greedy teacher 完成：

\[
A_j^T(x)=V(\tau[a_j^T;\pi_T])-V(\tau[a_j^S;\pi_T])\in\{-1,0,1\}.
\]

- `A_j^T=1`：teacher action 把 teacher-continuation 下的失败 branch 变成成功，定义为 teacher-improvable critical fork。
- `A_j^T=0`：两条 branch outcome-equivalent 或同败；raw tool disagreement 不进入 priority。
- `A_j^T=-1`：teacher action 更差；不把 teacher 当正确目标。

首次 `A_j^T=1` 的 turn 为 `d_k(x)`；到 `H` 均无则 right-censored 为 `H+1`。这不是 policy-independent criticality，也不等价于 student-learnability；后者必须由 one-update pilot 证明。

### 2. Confirmed fork movement

每个 prompt 维护 confirmed depth `D`、pending depth `Q`、movement EMA `L`、当前 branch-validity `R` 和 cost EMA `C`。

- 冷启动：一次 probe 后设 `D=d_0, Q=∅, L=1/(H+1)`。
- 若新 `d<D`：立即提交 regression，`D←d, Q←∅`，本次正向 movement 为 0。
- 若新 `d=D`：视为 stagnation，`Q←∅`，movement 为 0。
- 第一次出现 `d>D`：设 `Q←d`，不记正向 movement。
- 下一次连续访问仍有 `d>D`：无论 `d` 是否达到旧 `Q`，提交 `D_new←min(Q,d)`，记录
  `Δ=(D_new-D_old)/(H+1)`，随后 `Q←∅`。
- `d=H+1` 同样必须 two-hit confirmation；单次 fork 消失不算能力提升。
- `L←ρL+(1-ρ)max(0,Δ)`；regression/stagnation 使其衰减。

### 3. Prompt probability

\[
U_k(x)=\frac{R_k(x)[\epsilon+L_k(x)]}{C_k(x)},\qquad
P_k(x)=\frac{\eta}{|\mathcal D|}+(1-\eta)\frac{U_k(x)}{\sum_{x'}U_k(x')}.
\]

`R=1` 表示当前 confirmed teacher-improvable fork 仍存在；无此 fork 时 `R=0`，但 uniform exploration 保留回访。`C` 是该 prompt 最近 probe + update 的 wall-clock EMA，包括 student rollout、teacher action decode、两个 teacher continuations、environment replay/verifier 和训练。

当 fork 首次延后时只进入 pending；第二次确认后 `L` 增大，prompt 获得短期更高采样概率。之后若不再推进，`L` 衰减；fork 提前则立即提交 regression。

### 4. Fixed training interface

所有 sampler 使用同一个 probe-and-mask pipeline：

- Student rollout，teacher 在 student prefix 上给标准 reverse-KL supervision。
- Loss 保留到首个 critical structured action 闭合。
- 执行分歧 action 后的新 observation/suffix 不进入该训练样本。
- 无 critical fork 时按 `H` rollout。
- Boundary 使用 decision-complete teacher support。

这是 measurement consistency 条件，不是论文贡献。

## Training Loop

1. 对 prompt pool 做一次 cold probe。
2. 按 `P_k` 抽 batch。
3. 当前 student rollout；只在 raw canonical action 不同时执行 paired terminal branch test。
4. 找到 first `A^T=1` 后完成该 action，停止 post-action suffix。
5. 对统一 prefix 做标准 reverse-KL update。
6. 用新 `d/R/C` 更新 confirmed/pending frontier 与 sampling probability。
7. 推理时移除 sampler、branch probe 和 teacher。

## Novelty Boundary

- **vs ReOrder-OPD**：ReOrder 的变量是平均 prefix 上的 continuation reliability，主要做 queue ordering；ForkProgress 使用 action-local paired terminal advantage、confirmed movement，并 repeated-acquire 同一 prompt。
- **vs Prune-OPD/SOD/TurnOPD**：它们决定已选 trajectory 如何加权或多深；ForkProgress 只主张选哪个 prompt。Boundary mask 不作 novelty。
- **vs Relay/Guided-OPD**：它们改变 rollout source；ForkProgress 保持 student rollout 和标准 OPD。
- **vs pass-rate curriculum**：binary outcome 不定位 state fork，也不能区分 outcome-equivalent tools。

唯一不可替代的 novelty gate 是：`A^T,d,L` 在控制 ReOrder reliability、pass rate、prompt length 和 cost 后，是否额外解释 one-update gain。

## Claim-Driven Validation

### Claim 1：paired action advantage 比 raw disagreement 更接近 OPD prompt value

- **Setting**：可 clone、含多条 execution-equivalent 成功路线的 tool-DAG；固定 student checkpoint 和 teacher。
- **Compare**：pass rate、mean KL、first raw tool disagreement、teacher continuation reliability、static `A^T/d`。
- **Metric**：action-substitution terminal uplift、one-update held-out gain、cost-controlled partial ranking、route-diversity retention。
- **Gate**：若 `A^T/d` 不能在 ReOrder reliability 之外提供增量预测，停止。
- **Earliness test**：控制 `A^T`、cost、初始 success、tool count 和 horizon 后检验 `d` 的条件效应；不预设符号。

### Claim 2：confirmed fork-progress acquisition 改善全成本效率

必须分成两个对照层，避免把 probe 成本藏进共同 pipeline：

1. **Sampler attribution**：uniform-probe、`p(1-p)`-probe、ReOrder-probe、static-`A^T` 与 ForkProgress 全部使用相同 branch probe 和 boundary mask，只改变 acquisition policy。
2. **End-to-end utility**：ForkProgress 对比 vanilla no-probe uniform OPD；ForkProgress 的 cold probe、失败 candidate test、teacher continuations、replay 和 verifier 全部计入 wall-clock。

- **Primary curve**：success/score vs fixed-configuration end-to-end wall-clock。
- **Secondary curves**：teacher tokens、student tokens、environment steps、accelerator-seconds，分别报告。
- **Ablations**：去掉 `L`、去掉 two-hit confirmation；full suffix 仅作 mask sanity。
- **Evidence**：ForkProgress 在 sampler attribution 上胜出，同时相对 no-probe vanilla 仍改善 total-cost frontier，confirmed first-fork distribution 随训练右移。

## Failure Modes and Stop Rules

- Branch probe 吞掉成本：若 end-to-end frontier 不优于 no-probe uniform/ReOrder，实用 claim 失败。
- Teacher-improvable 但标准 OPD 学不动：若 one-update gain 不响应，停止，不加 action imitation objective。
- ALFWorld replay 不确定：退回 tool-DAG 做机制诊断，不能用模糊 process reward 偷换 terminal pair。
- Earliness 不成立：删除 early variant；不能倒过来挑有利分箱。
- 负 pilot 后不添加 learned estimator、teacher takeover、process judge、新 KL 或 semantic encoder。

## Compute & Timeline

- Tool-DAG causal pilot：约 150–300 GPU-hours，1–2 周。
- ALFWorld feasibility + matched-wall-clock runs：约 1,000–2,000 H20/A100-equivalent GPU-hours，取决于 branch replay 并发。
- 当前下一步只有 causal pilot；通过增量预测与 one-update responsiveness 两个 gate 后才进入完整训练。

