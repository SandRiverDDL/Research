# Round 2 Refinement

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token 或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

## Anchor Check

- **Original bottleneck**：整题 outcome 丢失错误位置，raw tool disagreement 又把合法替代路线和因果错误混为一谈。
- **Why the revised method still addresses it**：用同一 teacher continuation policy 下的 paired terminal outcome 明确定义 teacher-improvable action fork，并用已确认的 fork 后移更新 prompt 概率。
- **Reviewer suggestion rejected as protocol drift**：不改写已冻结的用户 Problem Anchor；改在 operational thesis 中明确：`earlier-first` 是待验证子假设，默认方法以 confirmed fork progress 为准。
- **No method drift**：不增加 critic、teacher takeover、semantic encoder、新 KL 或 action imitation objective。

## Simplicity Check

- **Dominant contribution**：teacher-continuation action advantage 所定义的 fork progress，用于 repeated prompt acquisition。
- **Components removed / frozen**：不再估计模糊短程 progress；不再使用 statistical LCB 的可变实现；不再把多类成本相加；boundary mask 固定。
- **Why smallest adequate**：在线方法只有一次 student rollout、发生 raw action disagreement 时的两个 deterministic teacher continuations、一个 prompt table。

## Changes Made

### 1. Freeze branch-value semantics

- `π_C` 固定为 frozen teacher 的 greedy JSON-constrained policy。
- 两个 action branch 都运行到 terminal 或剩余 global horizon `H-j`。
- 因为 environment、decoder 和 continuation 都确定，branch value 是精确的 `{-1,0,1}`，不再需要模糊 confidence procedure。
- 方法只声称 **teacher-continuation action advantage**，不声称 policy-independent criticality。

### 2. Censoring-aware frontier confirmation

- 首次观测到 fork 延后只进入 pending 状态；下一次独立 student rollout 再次不早于该候选位置才提交正向 movement。
- `H+1` right-censoring 必须连续出现两次才能视为已越过当前 fork。
- fork 提前则立即提交 regression、清零正向 progress，避免只记录好消息。

### 3. Freeze primary cost

- sampler 和主曲线的唯一 scalar cost 是固定硬件、固定 worker 数下的 end-to-end wall-clock seconds。
- teacher/student token、environment steps 和 accelerator-seconds 作为单独 Pareto/resource axes 报告，不与 wall-clock 相加，也不承诺四者同时匹配。

## Revised Proposal

# Research Proposal: ForkProgress-OPD——以已确认的因果 Action-Fork 进度驱动 Agent Prompt Acquisition

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token 或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

### Operational interpretation

用户提出的 `earlier-first` 是待验证 hypothesis，不是默认 sampler 的公理。可执行主张是：优先采样 teacher 确实能通过替代 action 改善 terminal outcome，且该 first fork 已被连续观测为随训练向后移动的 prompt。若受控 pilot 进一步证明 earliness 在控制 branch advantage 与成本后仍预测更新收益，再加入 early multiplier。

## Technical Gap

现有工作已经覆盖 prompt pass-rate curriculum、teacher-continuation reliability ordering、trajectory 内的 divergence weighting、动态截断、turn-depth budgeting 和 teacher handoff。仍未直接研究的对象是：**同一 student-visited agent state 上，一个 teacher alternative action 是否在配对 terminal continuation 中改变结果，以及这种 first action fork 的后移能否作为 prompt-level online learning progress。**

ForkProgress-OPD 只贡献这个 acquisition statistic 及其 repeated sampling 用法。标准 OPD、decision-complete teacher logits 和 action-boundary mask 在所有对照中保持一致。

## Method Thesis

- **One-sentence thesis**：在可 replay 的 deterministic tool environment 中，teacher-continuation action advantage 能过滤表面工具分歧；其已确认的 first-fork movement 可作为 agent OPD 的 prompt acquisition signal。
- **Dominant contribution**：causally grounded repeated prompt acquisition。
- **New trainable components**：0。
- **Inference overhead**：0。

## Exact Scope and Fixed Choices

1. environment 可 snapshot 或由 action prefix 确定性 replay；terminal verifier `V∈{0,1}`；最大 horizon `H` 固定。
2. student 与 teacher 使用同一 JSON action schema；只 canonicalize 空白、字段顺序和数值格式。
3. continuation policy `π_C` 固定为 frozen teacher 的 greedy constrained decoder；两个 branch 都使用它，运行剩余 `H-j` turns。
4. action boundary 使用 full-vocabulary teacher logits，或强制包含全部 tool-entry/stop token 的 decision-complete support；所有 sampler 相同。
5. primary cost 固定为同一硬件和 worker 配置下的 end-to-end wall-clock seconds。

这些选择使第一版结论明确局限为 **teacher-continuation-relative** 和 **simulator-grounded**，不外推为开放网页 agent 的无 oracle 方法。

## Core Mechanism

### 1. Exact teacher-continuation action advantage

对 prompt `x` 的 current-student trajectory，在 turn `j` 的 pre-action history `h_j`：

\[
a_j^S\sim\pi_S(\cdot|h_j),\qquad
a_j^T=\operatorname{Greedy}_{JSON}(\pi_T(\cdot|h_j)).
\]

若 canonical actions 相同，继续。若不同，则 snapshot `h_j`，分别执行 `a_j^S` 与 `a_j^T`，然后两边都由同一 greedy teacher `π_C=π_T` 完成：

\[
A_j^T(x)=V(\tau[a_j^T;\pi_T])-V(\tau[a_j^S;\pi_T])\in\{-1,0,1\}.
\]

- `A_j^T=1`：teacher action 在 teacher continuation 下把失败 branch 变成成功，定义为 teacher-improvable critical fork。
- `A_j^T=0`：两条 branch 在该 continuation 下 outcome-equivalent 或同败；raw tool disagreement 不进入 priority。
- `A_j^T=-1`：teacher action 更差；不把 teacher 当正确目标。

首次 `A_j^T=1` 的 turn 为 `d_k(x)`；到 `H` 均无则 right-censored 为 `H+1`。这一定义不声称 teacher action 是全局最优，只声称它相对 student action在固定 teacher continuation 下有 terminal advantage。

### 2. Confirmed fork movement

每个 prompt 维护 confirmed depth `D(x)`、pending depth `Q(x)`、movement EMA `L(x)`、最近 branch advantage `R(x)` 与 cost EMA `C(x)`。

- 冷启动：一次 probe 后设 `D=d_0`、`Q=∅`、`L=1/(H+1)`。
- 若新 `d<D`：立即提交 regression `D←d`，清空 `Q`，本次 positive movement 为 0。
- 若新 `d=D`：清空不一致 pending，movement 为 0。
- 若新 `d>D`：若 `Q=∅`，设 `Q=d`，不记录 movement；若已有 `Q` 且 `d≥Q`，提交 `D←min(Q,d)`，记录 `Δ=(D_new-D_old)/(H+1)`，清空 `Q`。
- `d=H+1` 也遵循同一 two-hit confirmation，因此单次 fork 消失不会被记成能力提升。
- `L←ρL+(1-ρ)max(0,Δ)`；regression/stagnation 使其自然衰减。

### 3. Prompt probability

\[
U_k(x)=\frac{R_k(x)[\epsilon+L_k(x)]}{C_k(x)},
\qquad
P_k(x)=\frac{\eta}{|\mathcal D|}+(1-\eta)\frac{U_k(x)}{\sum_{x'}U_k(x')}.
\]

`R=1` 仅对应当前 confirmed teacher-improvable fork；无此 fork 时 `R=0`，但 uniform exploration 保留回访。`C` 是该 prompt 最近 probe + OPD update 的 wall-clock EMA，包括 student rollout、teacher action decoding、两个 teacher continuations、environment replay/verifier 与训练；固定 hardware/worker count。

当分歧第一次延后时只 pending；第二次确认后 `L` 增大，prompt 获得短期更高概率。若随后不再推进，`L` 衰减；若 fork 提前，立即降回较早状态。

### 4. Fixed training interface

sampler 之外均为 vanilla OPD：student 生成，teacher 在 student prefix 上给 reverse-KL supervision。对所有方法统一：

- loss 保留到首个 critical structured action 闭合；
- 不蒸馏执行分歧 action 后的新 observation/suffix；
- 无 critical fork 时按 `H` rollout；
- boundary 使用 decision-complete teacher support。

这是 measurement consistency 条件，不是论文贡献。

## Training Loop

1. 对 prompt pool 做一次 cold probe。
2. 按 `P_k` 抽 batch。
3. 当前 student rollout；只在 raw canonical action 不同时执行 paired terminal branch test。
4. 找到 first `A^T=1` 后完成该 action 并停止 post-action suffix。
5. 对统一 prefix 做标准 reverse-KL update。
6. 用新 `d/R/C` 更新 confirmed/pending frontier 与 sampling probability。
7. 推理时移除全部训练控制器。

## Why This Is Not a Combination Paper

- ReOrder-OPD 的变量是平均 prefix 上 teacher continuation reliability，且以 queue ordering 为主；本方法的变量是 action-local paired terminal advantage 与 confirmed movement，并 repeated-acquire 同一 prompt。
- Prune-OPD/SOD/TurnOPD 作用于已选 trajectory；本方法只主张 prompt acquisition。boundary mask 不算贡献。
- Relay/Guided-OPD 改变 rollout source；本方法保持 student rollout 和标准 OPD。
- pass-rate curriculum 不定位 state fork，也不能区分两个 outcome-equivalent tools。

唯一不可替代的 novelty test 是：`(D,R,L)` 在控制 ReOrder reliability、pass rate、prompt 长度和 cost 后，是否额外解释 one-update gain。

## Claim-Driven Validation

### Claim 1：paired action advantage 比 raw disagreement 更接近可学习的 prompt value

- **Setting**：可 clone、含多条 execution-equivalent 成功路线的 tool-DAG；固定 student checkpoint 和 teacher。
- **Compare**：pass rate、mean KL、first raw tool disagreement、teacher continuation reliability、static `A^T/d`。
- **Metric**：action-substitution terminal uplift、one-update held-out gain、cost-controlled partial ranking、route-diversity retention。
- **Gate**：`A^T/d` 若不能在 ReOrder reliability 之外提供增量预测，停止。
- **Earliness test**：只在控制 `A^T`、cost、初始 success、tool count 和 horizon 后检验 `d` 系数；不预设其符号为方法成立条件。

### Claim 2：confirmed fork-progress acquisition 改善全成本效率

- **Setting**：一个 replayable agent benchmark；优先在 ALFWorld 做小规模 replay feasibility 后再扩展。
- **Compare**：uniform、`p(1-p)`、ReOrder-style reliability、static `A^T`、ForkProgress、去掉 two-hit confirmation、去掉 `L`。
- **Primary curve**：success/score vs fixed-configuration end-to-end wall-clock。
- **Secondary resource curves**：teacher tokens、student tokens、environment steps、accelerator-seconds，分别报告而不混加。
- **Evidence**：ForkProgress 占优且 confirmed first-fork distribution 右移；probe overhead 已完整计入。

## Failure Modes / Stop Rules

- paired branch probe 吞掉 wall-clock：若全成本 frontier 不优于 ReOrder/uniform，实用 claim 失败。
- teacher-improvable 但标准 OPD 学不动：若 one-update gain 不响应，停止，不加 action imitation objective。
- ALFWorld replay 非确定：退回 tool-DAG 完成诊断论文，不能用模糊 process reward 替代 terminal pair。
- two-hit 仍噪：报告 repeated-probe agreement；不加 learned estimator。
- earliness 不成立：删除 early variant，保留/评估 progress sampler；不改结果叙事。

## Compute & Timeline

- tool-DAG causal pilot：约 150–300 GPU-hours，1–2 周。
- ALFWorld feasibility + matched-wall-clock runs：约 1,000–2,000 H20/A100-equivalent GPU-hours，取决于 branch replay 并发。
- 下一步只运行 pilot；不扩展模块和 benchmark。

