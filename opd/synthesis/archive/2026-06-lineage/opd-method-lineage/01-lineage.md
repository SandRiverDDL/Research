# 01. 方法谱系

> 2026-10-06 整理：历史快照；保留原文的时间与覆盖口径，不代表当前全库。最新具体机制见 [failure-mode 诊断](../../../failure-modes/concrete-failure-modes.md)。

> 本卷回答：OPD 方法线是怎么从“student rollout + teacher logits”分叉成 trust、granularity、credit、signal interface 和 geometry 的。

## 1. 开山线：把 KD 改成 on-policy imitation

事实：GKD 将蒸馏框架化为 imitation learning。student 生成序列，teacher 在 student trajectory 上给 token-level logits；mixture rate λ 在 supervised KD 与纯 on-policy 之间连续插值，divergence choice 与 rollout source 解耦。它的作用不是发明某个特定 loss，而是把 OPD 变成可插拔框架。证据：[`notes/24_gkd.md`](../../../../notes/24_gkd.md)，anchors `pdf §3.1`, `song-2026 §2.3`。

MiniLLM 选择另一条路：用 sequence-level reverse-KL 对抗 forward-KL 的 void-region / mode-covering 问题。它把未来 token log-ratio 累进到当前 token 的 policy-gradient reward，因此在理论上更贴近 sequence objective，但也引入高方差；论文必须使用 single-step decomposition、teacher-mixed sampling、length normalization 等稳定 trick。证据：[`notes/24_minillm.md`](../../../../notes/24_minillm.md)，anchors `pdf §2.1-2.2`, `song-2026 §4.1`。

DistiLLM 则把问题定位在 KL 实现稳定性和 SGO 成本。标准 KLD 在 student probability 接近 0 时梯度系数无界；skew-KL 用 teacher/student mixture 替换分母，给梯度系数加下界。adaptive replay buffer 进一步降低实时 student-generated output 的生成成本。证据：[`notes/24_distillm.md`](../../../../notes/24_distillm.md)，anchors `pdf §2.2`, `§3.1`, `Fig 2`。

解释：这三篇构成 OPD 的基本三角：

| 路线       | 关键设计                                  | 真正解决的问题                           | 留下的问题                                        |
| -------- | ------------------------------------- | --------------------------------- | -------------------------------------------- |
| GKD      | rollout mixture + divergence-agnostic | exposure bias 和 framework 化       | teacher 在 bad prefix 上是否可靠                   |
| MiniLLM  | sequence-level reverse-KL             | mode-seeking 和 sequence coherence | policy-gradient 方差、future log-ratio coupling |
| DistiLLM | skew-KL + replay                      | KL 梯度爆炸、SGO 成本                    | divergence/source/token 的 routing 仍粗         |

## 2. Objective routing：从固定 KL 到条件分流

事实：DistiLLM-2 把 teacher-generated 和 student-generated 样本分开处理：teacher response 上用 mode-covering SKL，student response 上用 mode-seeking SRKL。这说明 divergence 不应全局固定，而应按 data source routing。证据：[`notes/25_distillm-2.md`](../../../../notes/25_distillm-2.md)。

TAID 用 detached student distribution 和 teacher distribution 在 logit 空间插值得到中间 target，让目标从接近 student 逐步移动到完整 teacher。它处理的是 capacity gap：student 一开始不一定能直接吸收 full teacher signal。证据：[`notes/25_taid.md`](../../../../notes/25_taid.md)。

EOPD 进一步把 routing 粒度推进到 token entropy。低熵位置保留 reverse-KL 的 mode-seeking；高熵 teacher distribution 额外加 forward-KL，避免把合理 continuation 全部压掉。证据：[`notes/26_eopd.md`](../../../../notes/26_eopd.md)。

解释：objective 线的进步不是“哪个 KL 最好”，而是把 loss choice 变成条件决策：

- source-level：teacher response 与 student response 信号不同。
- target-level：teacher target 难度应随 student 能力变化。
- token-level：teacher high-entropy 与 low-entropy token 不应同一处理。

边界：这些方法仍默认 teacher distribution 本身是有效目标。如果 student prefix 已经漂到 teacher 不可靠区域，adaptive KL 只会更精细地匹配错误或低价值信号。

## 3. 机制诊断线：teacher signal 不是自动可信

Revisiting OPD 把 sampled-token OPD 的几个实现级坑放到台面上：token-level estimator 相比 sequence-level reverse-KL 有 bias 但方差更低；single sampled token log-ratio 容易在长 rollout 中失真；support mismatch 和 special-token/tokenizer mismatch 会扭曲更新。它提出 top-K local support matching、top-p rollout、special-token masking，应该被当作 sampled-token OPD hygiene baseline。证据：[`notes/26_revisiting-opd.md`](../../../../notes/26_revisiting-opd.md)。

Rethinking OPD of LLMs 将 OPD 成功拆成两个条件：teacher/student thinking pattern 要兼容；teacher 还必须提供 student 没见过但可利用的新能力。它把“teacher 更强但 OPD 失败”解释为 distillability 问题，而非单纯 loss 问题。证据：[`notes/26_rethinking-opd-llm.md`](../../../../notes/26_rethinking-opd-llm.md)。

Rock Tokens 进一步反对“高 loss token 就是学习重点”。持续高 loss、高梯度范数的 token 可能是低功能贡献的阻塞点，而不是 reasoning pillar。Prune-OPD 则从 trajectory suffix 角度处理同一类问题：当 top-k overlap 显示 prefix drift 后，后续 teacher dense reward 可能不再可执行，应下调 loss 并动态截断 rollout。证据：[`notes/26_rock-tokens.md`](../../../../notes/26_rock-tokens.md), [`notes/26_prune-opd.md`](../../../../notes/26_prune-opd.md)。

TrOPD、KL Agreement Trap、Full Rollouts Necessary、ESR、Prefix Teach Suffix Fade、Supervision Fidelity Decay 共同把“长 rollout 是否值得蒸”变成核心问题。低 KL 不一定代表 student 接近 teacher；它也可能是 degraded prefix 下局部 vocabulary shift 造成的假 agreement。证据：[`notes/26_trust-region-opd.md`](../../../../notes/26_trust-region-opd.md), [`notes/26_kl-agreement-trap.md`](../../../../notes/26_kl-agreement-trap.md), [`notes/26_full-rollouts-necessary.md`](../../../../notes/26_full-rollouts-necessary.md), [`notes/26_early-stopping-rollout.md`](../../../../notes/26_early-stopping-rollout.md)。

解释：2026 机制诊断线把 OPD 的主问题从 “state mismatch” 改写为 “state coverage vs teacher reliability”。这也是后续 idea 最重要的入口。

## 4. Granularity 线：token、step、segment、trajectory 都只是候选粒度

TIP 代表 token-level selection：student entropy 捕捉不确定性，teacher-student divergence 捕捉 overconfident error，Soft-OR 选择重要 token。它适合 token-level teacher signal 仍可靠的区域。证据：[`notes/26_tip.md`](../../../../notes/26_tip.md)。

SCOPE 先按 trajectory correctness 分两条 path：错误轨迹用 teacher-perplexity-weighted KL，正确轨迹用 student-perplexity-weighted MLE。它比 TIP 粗，但更能避免坏 token 污染整条梯度。证据：[`notes/26_scope.md`](../../../../notes/26_scope.md)。

SOD 把 tool-integrated reasoning 的 step boundary 显式纳入：错误 tool call 会把 corrupted observation 注入后续上下文，因此 step-level divergence 比 token-level 更贴近故障边界。Segment-Level OPD / CHOP 将这个思路推广到 long-horizon agent 的 route segment，直接处理 local token reward 与 sequence-level return mismatch。证据：[`notes/26_sod.md`](../../../../notes/26_sod.md), [`notes/26_segment-level-opd.md`](../../../../notes/26_segment-level-opd.md)。

Near-Future Guidance 和 TRD 说明局部 high-loss token 未必是 reasoning fork。前者用短未来轨迹判断 token 是否改变后续推理；后者先 refine trajectory，再蒸馏修正后的路径。证据：[`notes/26_near-future-guidance.md`](../../../../notes/26_near-future-guidance.md), [`notes/26_trajectory-refined-distillation.md`](../../../../notes/26_trajectory-refined-distillation.md)。

解释：granularity 不应是固定超参，而应由 state transition、tool/observation boundary、future consequence 和 verifier structure 共同决定。

## 5. Credit 与 privilege 线：把 sparse outcome 转成 process signal

OPSD 用 ground-truth-conditioned context 构造 same-model privileged teacher，核心假设是 rationalization gap：看到参考解后解释为什么比从零生成更容易。HDPO 把这个机制接到 GRPO all-fail cliff prompts 上，在原本 advantage 近似为零的位置注入 JSD self-distillation。证据：[`notes/26_opsd.md`](../../../../notes/26_opsd.md), [`notes/26_hdpo.md`](../../../../notes/26_hdpo.md)。

PBSD 把 answer-conditioned privilege 写成 posterior-to-prior probability ratio，再用 Bayes rule 转成 turn-level credit signal。它不是直接模仿 privileged teacher 的每个 token，而是估计每个 intermediate turn 对最终答案的证据贡献。证据：[`notes/26_pbsd.md`](../../../../notes/26_pbsd.md)。

Many Faces 给 privilege 线加了边界：instance-specific privileged information 不一定可内化，shared latent rule 更可能转成推理期 PI-free policy。证据：[`notes/26_many-faces-opd.md`](../../../../notes/26_many-faces-opd.md)。

MOPD 和 SSOPD 则不依赖外部答案，而是从同 prompt 多 rollout 中抽结构。成功 peer、失败 peer、correct witness、wrong prefix 可以提供比单条 rollout 更丰富的 process credit。证据：[`notes/26_multi-rollout-peer.md`](../../../../notes/26_multi-rollout-peer.md), [`notes/26_ssopd.md`](../../../../notes/26_ssopd.md)。

## 6. Signal interface 线：logits 不是唯一接口

OPRD 将监督从 output-space KL 移到 hidden-state MSE。它声称 output-space OPD 的 score-function 方差在收敛时也不消失，而 hidden-state MSE gradient 的条件方差为零；同时 LM head 会压缩 teacher hidden-state 信息。证据：[`notes/26_oprd.md`](../../../../notes/26_oprd.md)。

ROPD 和 BOPD 处理 API-only teacher：前者用 structured rubrics 作为 semantic reward，后者训练动态 discriminator 区分 teacher/student response，再用 GRPO 更新 student。它们牺牲 token-level credit，换取 black-box applicability。证据：[`notes/26_ropd.md`](../../../../notes/26_ropd.md), [`notes/25_bopd.md`](../../../../notes/25_bopd.md)。

SimCT 说明 tokenizer 也是 signal interface 的一部分。cross-tokenizer exact shared-token matching 会静默丢 supervision；multi-token continuation unit 是更细的共同接口。证据：[`notes/26_simct.md`](../../../../notes/26_simct.md)。

## 7. Geometry 与 reward extrapolation 线：OPD 不只是贴近 teacher

Post-Training is About States 把 SFT、RL、OPD 统一为 state-conditioned supervision，强调 state source 与 signal source 是正交轴。Geometry OPD 与 Dense Supervision, Sparse Updates 则显示 dense teacher supervision 不等于 dense parameter rewriting；OPD 的有效更新可能是 low-rank、coordinate-sparse、spectrally concentrated。证据：[`notes/26_states-not-tokens.md`](../../../../notes/26_states-not-tokens.md), [`notes/26_geometry-opd.md`](../../../../notes/26_geometry-opd.md), [`notes/26_dense-supervision-sparse-updates.md`](../../../../notes/26_dense-supervision-sparse-updates.md)。

EffOPD 把参数动力学变成加速器：如果 OPD 早期 update direction 已接近最终方向，就可以用 validation-gated parameter extrapolation 跳过部分优化步。证据：[`notes/26_effopd.md`](../../../../notes/26_effopd.md)。

G-OPD 把标准 OPD 写成 dense KL-constrained RL 的特例，λ>1 的 ExOPD 允许 student 沿 teacher reward 方向外推。Extrapolation Cliff 则说明 structured output 中存在 sharp format-collapse threshold：外推可能提升 task reward，但 parse validity 和 contract adherence 会先崩。证据：[`notes/26_g-opd-reward-extrapolation.md`](../../../../notes/26_g-opd-reward-extrapolation.md), [`notes/26_extrapolation-cliff.md`](../../../../notes/26_extrapolation-cliff.md)。

解释：如果 OPD 的收益来自 state visitation 和 parameter subspace，而不是 token supervision 密度本身，那么简单堆更多 token-level KL 不是最有希望的研究方向。
