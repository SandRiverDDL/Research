# Round 1 Refinement

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token 或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

## Anchor Check

- **Original bottleneck**：pass rate 丢失错误出现的位置；raw disagreement 又不能说明该分歧是否有因果后果、teacher 是否真能修复。
- **Why the revised method still addresses it**：仍以每个 prompt 的首个 action fork 和它随训练向后移动的动态为采样信号，但把“关键”从模糊 progress 改成 terminal-success paired branch value。
- **Reviewer suggestions rejected as drift**：不加入 learned value model、teacher takeover、semantic encoder 或新 action-level distillation objective；这些会把论文从 prompt acquisition 推向新的监督接口。
- **Necessary correction to the original intuition**：`earlier-is-better` 保留为必须先验证的机制假设，不进入默认 sampler。若在控制 teacher-recoverability、成本、prompt 长度和初始成功率后仍有稳定的负深度系数，再作为预注册增强项加入；否则明确报告原始直觉不成立。

## Simplicity Check

- **Dominant contribution after revision**：用 paired counterfactual terminal outcomes 定义 action-fork value，再把首次 fork 的在线后移变成 prompt acquisition signal。
- **Components removed or merged**：删除手工 execution-equivalence class；删除独立 truncation claim；删除模糊短程 progress oracle；删除主公式中的 earliness 项。
- **Reviewer suggestions rejected as unnecessary complexity**：不训练 recoverability predictor，不做 teacher relay，不改变 OPD loss。
- **Why the remaining mechanism is the smallest adequate route**：新增部分只有 snapshot branch probe、per-prompt state table 和 sampler；action-boundary mask 在所有 sampler 对照中固定。

## Changes Made

### 1. Criticality 改成可复现的 paired terminal branch value

- **Reviewer said**：短程 progress 不等于首个关键错误，也没有定义 continuation policy、horizon、阈值和 right censoring。
- **Action**：限定首版为可 replay/snapshot、固定最大 horizon、精确 terminal verifier 的 deterministic tool environments；两个 action branch 使用同一 frozen continuation policy 和配对随机种子完成到 terminal/horizon，以 terminal success LCB 定义关键性。
- **Impact**：方法不再声称无需 oracle；它是 simulator-grounded causal acquisition。开放环境泛化属于后续工作。

### 2. Prompt sampler 删除未经验证的 earliness 因子

- **Reviewer said**：Relay-OPD 的早期介入结果不能证明 prompt-level `earlier-is-better`，深层 turn 也可能更缺训练。
- **Action**：默认 priority 只依赖 teacher branch advantage、首次关键 fork 的正向移动和实测成本。earliness 只作预注册 conditional analysis。
- **Impact**：主方法从“最早优先”变为“优先继续训练正在把关键分叉向后推、且 teacher 确实能改善该分叉的 prompt”。

### 3. Truncation 降为统一接口

- **Reviewer said**：action-boundary truncation 已被 Prune-OPD/SOD/TurnOPD/Guided-OPD/Relay-OPD 占据，独立 Claim 3 会造成拼装感。
- **Action**：所有 sampler 使用相同 action-boundary mask；只留一个 sanity ablation，不宣称 novelty。
- **Impact**：论文只剩 prompt acquisition 一条主线。

## Revised Proposal

# Research Proposal: ForkProgress-OPD——以因果 action fork 进度驱动长程 Agent Prompt Acquisition

## Problem Anchor

- **Bottom-line problem**：在长程 agent OPD 中，优先训练首次关键推理或工具选择分歧更早、且该分歧可被教师可靠修复的 prompt；分歧后在监督失真前按动作边界截断，并随学生进步动态更新 prompt 采样概率。
- **Must-solve bottleneck**：整题正确率看不到失败从哪个决策开始；但原始 teacher–student disagreement 又会把多条合法工具路径、表面 token 差异和真正导致状态分叉的错误混在一起。若执行了分歧动作，环境 observation 已改变，继续蒸馏长后缀可能监督错误的状态分支。
- **Non-goals**：不再提出一种 token-level KL 权重；不把所有 teacher–student 分歧都视为错误；不把“越早分歧越好”作为未经验证的公理；不以 teacher takeover 或轨迹重写作为主贡献。
- **Constraints**：优先复用标准 reverse-KL OPD、冻结 teacher 和现有 agent 环境；第一版不训练额外 selector/reward model；比较时固定总 student rollout token、teacher-scored token或 wall-clock；需要能识别 tool/action boundary，最好可 clone environment state。
- **Success condition**：证明首次“关键且可修复”的动作分歧位置比 prompt pass rate、平均 KL、首次 raw tool disagreement 更能预测一次 OPD 更新的收益；在相同总 teacher/student compute 下，动态 prompt sampling 改善长程 agent success，并且不会因多合法路线而造成模式坍缩。

## Technical Gap

PACED 和 ReOrder-OPD 已经证明 OPD prompt 的访问顺序/分布会影响结果；Prune-OPD、SOD、TCOD、Guided-OPD、TurnOPD 和 Relay-OPD 已覆盖 trajectory 内的可靠性、深度、截断与 teacher intervention。尚缺的是一个 agent-specific 的 prompt acquisition quantity：它不是“这题能否答对”，也不是“当前 token KL 多大”，而是“在 student 实际访问的 agent state 上，哪个 action 首次产生可验证的 terminal-outcome 分叉，以及这个位置是否随训练向后移动”。

ForkProgress-OPD 只研究这个问题。它不把 action-boundary stopping 当贡献，也不声称一般开放环境中可以免费获得因果标签。

## Method Thesis

- **One-sentence thesis**：对 snapshot-capable tool agents，prompt 的在线 OPD 价值可由 teacher 可改善的首次 action fork 及其随训练的正向移动来估计，这比整题 pass rate 或局部 disagreement 更贴近 agent state-distribution learning progress。
- **Smallest intervention**：标准 OPD 不变；只加入 branch probe、prompt state table 和采样器。
- **Dominant contribution**：causally grounded prompt acquisition；无第二方法贡献。

## Complexity Budget

- **Frozen / reused**：student/teacher、agent policy format、reverse-KL OPD、terminal verifier。
- **New trainable components**：0。
- **New nonparametric components**：JSON-schema-constrained action parser/decoder、environment snapshot/replay、priority table。
- **Explicit exclusions**：learned critic、LLM judge、teacher takeover、trajectory rewrite、new KL、hand-built semantic route taxonomy。

## Exact Setting

首版只覆盖满足以下条件的 environment：

1. 最大 interaction horizon `H` 固定；
2. 任意 pre-action state 可 snapshot，或可用确定性 action prefix replay；
3. terminal verifier `V(τ)∈{0,1}` 精确；
4. student/teacher action 均能用同一 JSON schema 约束生成；
5. tool entry 与 action close tokens 使用 full-vocabulary、或显式包含全部行为切换 token 的 decision-complete teacher support，避免 top-k 遗漏关键工具 token。

ALFWorld 可通过 replay action prefix 近似满足这一设置；先用可控 tool-DAG 做完整因果验证，再决定是否扩展到 WebShop 等更随机环境。

## Core Mechanism

### 1. Candidate action disagreement

对 prompt `x`，当前 student 生成 trajectory。在 turn `j` 的同一 pre-action history `h_j` 上：

- student 通过 schema-constrained decoding 生成 `a_j^S`；
- frozen teacher 用固定 greedy 或预先冻结的 sampling configuration 生成 `a_j^T`；
- 只做语法 canonicalization（字段顺序、空白、数字格式），不做手工语义等价映射；
- 若 canonical actions 相同，则继续 rollout；不同则进入 paired branch test。

### 2. Paired terminal branch test

在 `h_j` snapshot 上分别执行 `a_j^S` 与 `a_j^T`。两个分支随后都使用同一 frozen continuation policy `π_C`，默认取 teacher；使用相同的 `K_b` 个 sampling seeds，运行到 terminal 或原始固定 horizon `H`。

\[
\hat A_j(x)=\frac{1}{K_b}\sum_{b=1}^{K_b}
\left[V(\tau^{T}_{j,b})-V(\tau^{S}_{j,b})\right].
\]

用配对 Bernoulli difference 的 bootstrap 或 concentration bound 得到 `LCB_j`。当 `LCB_j>δ` 时，该位置定义为 **teacher-improvable critical fork**。当区间覆盖 `[-δ,δ]` 时，两种 action 对当前证据而言 outcome-equivalent，不把 raw disagreement 当错误；当 `LCB_j<−δ` 时 teacher action 更差，也不进入 OPD prompt priority。

首次满足条件的位置为：

\[
d_k(x)=\min\{j:LCB_j(x)>\delta\}.
\]

若到 `H` 均未找到，则记为 right-censored `d_k(x)=H+1`。这里 `teacher-improvable` 不等于 `student-learnable`；后者只通过 one-update gain pilot 建立，术语上不再混用。

### 3. Online fork-progress state

每个 prompt 维护：

- `d̄_k(x)`：归一化 first-fork depth `min(d,H+1)/(H+1)` 的 EMA；
- `r̄_k(x)`：首个 critical fork 的正向 terminal advantage LCB；
- `ℓ_k(x)=EMA(max(0,d̄_k(x)-d̄_prev(x)))`：首次关键 fork 向后移动的学习进度；
- `c̄_k(x)`：本 prompt probe + training 的实测 teacher tokens、student tokens、environment steps 和 wall-clock cost。

初始化阶段每个 prompt probe 一次，统一设 `ℓ_0=1/(H+1)`。right-censored prompt 设 `r̄=0`，仅通过 exploration floor 偶尔回访。若同一 prompt 长期停留在早期 fork，`ℓ` 衰减，避免把不可学 prompt 永久当“最有价值”。

### 4. Prompt acquisition

默认方法不使用裸 earliness：

\[
u_k(x)=\frac{\bar r_k(x)\,[\epsilon+\ell_k(x)]}{\bar c_k(x)},
\qquad
P_k(x)=\eta/|\mathcal D|+(1-\eta)\frac{u_k(x)}{\sum_{x'}u_k(x')}.
\]

当重新访问 prompt 后发现首次 critical fork 延后，`ℓ` 上升，prompt 获得短期继续训练的概率；若再次访问不再推进，则优先级衰减。所有 branch-probe 开销进入 `c`，所以方法不能靠额外 teacher compute 获得免费优势。

用户原始 earliness 假设作为预注册机制检验：

\[
u_k^{early}(x)=(1-\bar d_k(x))u_k(x).
\]

只有当 `d` 在控制 `r/c`、prompt 长度、初始 success 和 tool-call count 后仍稳定预测 one-update gain，才把 `u^early` 升为最终方法；否则主结论是 frontier movement，而不是 earlier-first。

### 5. Fixed action-boundary training interface

所有 sampler 使用相同接口，避免把 truncation 当额外贡献：

- 标准 reverse-KL 只作用于 student trajectory 从 prompt 到首个 critical action 完整闭合的位置；
- 执行该 action 后产生的新 environment observation 及其 suffix 不进入这条训练样本；
- 无 critical fork 时按共同最大 horizon 运行；
- action boundary 的 teacher scoring 必须 decision-complete。

该 mask 的唯一用途是让 sampler 所定义的可靠 prefix 与实际 OPD update 一致。full-rollout 只作为 sanity baseline。

## Training Algorithm

1. **Cold probe**：统一 student checkpoint 对所有 prompt 各 rollout 一次；只在 raw action disagreement 处做 paired branch test，填充 `d/r/c`。
2. **Acquire**：由 `P_k` 采样 prompt batch。
3. **Probe + rollout**：当前 student 重新 rollout；发现 candidate fork 时执行 branch test，找到 first critical fork 后停止 post-action environment suffix。
4. **OPD update**：对固定可信 prefix 做标准 reverse-KL update。
5. **Refresh**：用本次 `d/r/c` 更新 EMA 和 prompt probability；未访问 prompt 不做全池重 rollout，只通过 exploration floor 回访。
6. **Inference**：移除所有 probe/sampler/teacher，student 完整运行。

## Failure Modes and Diagnostics

- **Counterfactual oracle 太贵**：报告 probe-only cost、teacher generation、environment steps 和 wall-clock；若 acquisition overhead 超过节省，实用 claim 失败。
- **teacher continuation policy 偏置**：paired test 固定同一 `π_C`；额外只做一次 `π_C=student` sensitivity，不把多个 critic 组合进方法。
- **fork 延后由 verbosity 造成**：深度按 action turn/H 计算，并同时报告 task progress 与总 token；重复 thought 不会增加 action depth。
- **多合法路线**：不靠字符串判断；只有 terminal branch advantage 显著时才视为 critical。
- **stochastic first-fork noise**：EMA + paired seeds；核心 pilot 报告 `K_b` sensitivity 和 confidence interval。
- **support truncation 漏掉工具切换 token**：action boundary 使用 full/decision-complete support，所有方法相同。
- **prompt starvation**：固定 `η` uniform exploration，报告有效样本量与访问分布 Gini。

## Novelty and Elegance Argument

- **Against ReOrder-OPD**：ReOrder 估计 teacher 能否从平均 student prefix 正确续写，并主要做一次性 queue order；ForkProgress 在 agent action boundary 做 paired counterfactual outcome comparison，并允许同一 prompt 因 fork movement 被重复 acquisition。
- **Against Prune-OPD/SOD/TurnOPD**：它们决定已选 rollout 内怎样加权或多深；ForkProgress 的因变量是下一次选哪个 prompt。统一 action-boundary mask 不作 novelty。
- **Against Relay-OPD/Guided-OPD**：它们改变 rollout source；ForkProgress 保持纯 student rollout 和标准 OPD，只改变 data acquisition。
- **Against pass-rate curriculum**：binary outcome 不包含错误发生 turn；ForkProgress 直接建模 state-distribution fork 的位置与移动。

如果 paired first-fork statistic 在控制 teacher continuation reliability 后不能额外预测 one-update gain，则该 gap 不成立，方法应停止，而不是增加模块。

## Claim-Driven Validation Sketch

### Claim 1：paired first critical fork 捕获的是 action consequence，而非表面 disagreement

- **Minimal experiment**：可 clone tool-DAG，显式含多条等价路线；固定 prompt、student checkpoint、`π_C` 和 paired seeds，比较 raw tool disagreement、mean KL、pass rate、ReOrder-style continuation reliability 与 `d/r`。
- **Necessary evidence**：`d/r` 预测 action substitution 的 terminal uplift，并在 one-update prompt subset experiment 中优于 closest signals；raw disagreement 在等价路线中出现系统性 false positive。
- **Decisive metric**：cost-controlled partial correlation / ranking with one-update validation gain，以及 route-diversity retention。
- **Go/no-go**：若 `d/r` 在控制 teacher continuation reliability 后无增量解释力，停止项目。

### Claim 2：fork-progress acquisition 在全成本匹配下提高 agent OPD 的学习效率

- **Minimal experiment**：一个 replayable benchmark（优先 ALFWorld）上比较 uniform、`p(1-p)`、ReOrder-style reliability、static `r`、ForkProgress；同 teacher/student、同 optimizer update，并分别匹配 total teacher tokens、student tokens、environment steps 和 wall-clock。
- **Necessary evidence**：ForkProgress 的 success-vs-total-cost frontier 占优；first critical fork distribution 随训练右移；去掉 `ℓ` 后退化。
- **Sanity ablations**：统一 mask 下 full suffix vs action-boundary suffix；不作为独立 claim。

## Experiment Handoff Inputs

- **Must-prove**：paired action-fork value 的增量预测力；fork movement 不等于 verbosity；全成本前沿优势。
- **Must-run ablations**：raw vs paired fork、`r` only vs `r×ℓ`、earliness conditional analysis、decision-complete vs ordinary top-k support、fixed mask sanity。
- **Highest-risk assumptions**：snapshot/replay 与 terminal verifier 可用；branch probe 成本可承受；teacher-improvable fork 确实可通过标准 OPD 学到。

## Compute & Timeline Estimate

- **Causal pilot**：tool-DAG，1.5B–1.7B student、7B–8B teacher，约 150–300 GPU-hours；environment branch steps 单独计数；1–2 周。
- **Matched-cost benchmark**：ALFWorld，4–5 sampler、3 seeds，约 1,000–2,000 H20/A100-equivalent GPU-hours；branch probe 预计是主要新增成本。
- **Stop rule**：先冻结 `K_b/δ/H/π_C` 并跑 pilot；不通过增量预测 gate 就不做主训练。

