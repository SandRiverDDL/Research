# 03. Failure Modes 与证据可信度

> 2026-10-06 整理：历史快照；保留原文的时间与覆盖口径，不代表当前全库。最新具体机制见 [failure-mode 诊断](../../../failure-modes/concrete-failure-modes.md)。

> 本卷回答：OPD 具体会坏在哪里，已有方法分别解决了什么，哪些结论可信、哪些还只是 hypothesis。

## A. State / reliability 类

### exposure-bias

症状：off-policy KD 在 teacher/offline sequences 上训练，student 推理时访问自己的 prefixes，训练/推理 state 分布不一致。

方法族：GKD、MiniLLM、DistiLLM 用 student/mixed rollout 修复；States-Not-Tokens 将其抽象为 state distribution 问题。

已解决：student prefixes 进入训练目标，OPD 相比 SeqKD 的基本动机成立。

未解决：student prefixes 进入训练后，teacher 在 bad prefix 上是否仍给可靠监督。

证据：[`notes/24_gkd.md`](../../../../notes/24_gkd.md), [`notes/24_minillm.md`](../../../../notes/24_minillm.md), [`notes/24_distillm.md`](../../../../notes/24_distillm.md), [`notes/26_states-not-tokens.md`](../../../../notes/26_states-not-tokens.md)。

### flawed-prefix-trap / compounding-error

症状：student 早期错误 prefix 把后续 context 带出 teacher 熟悉区域；teacher 仍给 dense token distribution，但这些 signal 不再可执行，甚至把 student 锁进错误路径。

方法族：

- Revisiting OPD：top-K local support matching、top-p rollout、special-token masking。
- Full Rollouts Necessary / ESR / Prefix Teach Suffix Fade / SFD：限制 rollout horizon 或后缀监督。
- Prune-OPD：top-k overlap 监控 prefix drift，动态下调 suffix loss 和 response budget。
- TrOPD / KAT：trust region、outlier masking、低 KL trap 检测。
- TRD / Near-Future：从局部 token 修正升级为 trajectory-aware correction。

已解决：长 rollout 不应默认全蒸，已经成为稳定结论。

未解决：统一的 truncate/refine/continue 判据还没有出现。KL、entropy、support overlap、verifier outcome 各自只能覆盖一部分。

可信度：中到高。核心现象有多篇互相支持；具体阈值和算法多为 2026 新论文，仍需复现。

### teacher-pattern-mismatch / capacity-gap

teacher strength 与 OPD gain 不是单调关系；mismatch 分布在 pair、data、local support 与 trajectory 四层。现有方法几乎覆盖所有局部干预位置，但训练前的 distillability prediction 与统一 routing protocol 仍缺。详见独立综合：[Teacher–student mismatch / capacity gap](../../../failure-modes/teacher-pattern-mismatch.md)。

## B. Estimator / implementation 类

### sampled-token-imbalance

症状：sampled-token surrogate 只看学生采到的 token，容易让少数正 token 或特殊 token 主导更新，多数 token 提供负 reward，信号分布极不平衡。

方法族：Revisiting OPD 诊断并修复 sampled-token support；Position-Weighted OPSD 做位置可靠性加权。

未解决：sampled-token hygiene 是否足够服务 long-horizon reasoning，仍取决于 future consequence 是否可由 local support 判断。

### policy-gradient-variance

症状：sequence-level reverse-KL 的未来 log-ratio 与当前 action 强耦合，长序列方差大；output-space OPD 的 score-function 方差可能在 late stage 仍不消失。

方法族：MiniLLM 用稳定 tricks；DistiLLM 避开 REINFORCE 改用 skew-KL；OPRD 转向 hidden-state MSE；OPD+ / TGPO / GNDPO 从 advantage 设计和归一化修正。

未解决：OPRD 的 cross-architecture projector、layer selection、teacher hidden access 成本还未成为通用 recipe。

### kld-gradient-explosion

症状：标准 KL 在 student probability 接近 0 时梯度系数无界。

方法族：DistiLLM 用 skew-KL mixture denominator；DistiLLM-2 按 data source 分配 SKL/SRKL。

可信度：高。DistiLLM 有明确公式、实验和 survey anchor。

### special-token / cross-tokenizer mismatch

症状：tokenizer 或 special-token 边界让同一文本对应不同 token 序列，sampled-token log-prob 比较被实现细节污染。

方法族：Revisiting OPD mask special tokens；SimCT 用 multi-token continuation units 作为 cross-tokenizer 共同接口。

未解决：更彻底的 architecture/cross-modal mismatch 可能需要 representation 或 alignment 方法，不是 continuation unit 能完全解决。

## C. Credit / granularity 类

### coarse-credit-assignment

症状：final answer 正误、trajectory correctness、token loss、teacher KL 不在同一粒度上，导致 dense token signal 未必对应真正的 reasoning fork。

方法族：

- TIP：token entropy + divergence。
- SCOPE：trajectory correctness 分流。
- SOD：tool step boundary。
- Near-Future / TRD：future consequence / trajectory refinement。
- Segment-Level OPD：agent segment local reward 与 sequence return 对齐。
- PBSD / SSOPD：turn-level / group-level process credit。

已解决：token-level KL 不是唯一 process signal。

未解决：缺少统一 granularity policy。不同论文在不同任务结构下各自固定粒度，实验不可比。

### cross-rollout-credit

症状：单条 rollout 看不到同 prompt 下的成功/失败结构，无法区分偶然错误、系统性错误和可修复 counterfactual。

方法族：MOPD 用成功/失败 peer 构造 teacher context；SSOPD 用 shortest correct / longest wrong 和 frontier weight；ReNIO 强调 negative trajectory 的信息价值。

未解决：多 rollout 成本、verifier 噪声、context length 开销可能抵消收益。

### privileged-context-gap

症状：ground truth、answer、hint 或 context 能增强 teacher，但推理期 student 没有这些 PI。若 PI 是 instance-specific clue，student 可能无法真正内化。

方法族：OPSD、HDPO、PBSD 使用 answer/GT conditioned teacher；Many Faces 给出 shared latent rule vs instance-specific PI 边界；On-Policy Context Distill / Online Experiential 处理 context/experience internalization。

未解决：PI 类型 taxonomy 和 benchmark 还不成熟。很多方法只展示 PI 有用，未证明 PI-free policy 真正学到了可泛化规则。

## D. Efficiency / update 类

### sgo-generation-cost

症状：student-generated output 的生成和 teacher scoring 是 OPD 训练大头。

方法族：DistiLLM replay buffer；Full Rollouts / ESR / Prune-OPD 减少无效后缀；Rock Tokens 跳过低贡献高损耗 token；EffOPD 跳过冗余优化步。

未解决：节省生成、节省 scoring、节省 optimizer steps 是不同层面的效率，不能用单一 speedup 数字比较。

### low-utility-token-supervision

症状：高 loss / 高梯度范数 token 可能不贡献 reasoning function。

方法族：Rock Tokens 检测 persistent high-loss but low-function tokens，用 window-aware reweighting/freezing 跳过。

可信度：中。机制很有启发，但主要来自特定 math reasoning 和 teacher-student pair。

### parameter-update-redundancy

症状：OPD 早期可能已锁定接近最终的 update direction，后续训练只是补 magnitude。

方法族：EffOPD validation-gated parameter extrapolation；Geometry / Dense-Sparse 分析 update subspace。

未解决：小验证集是否足以决定外推，仍是风险。

## E. Extrapolation / safety 类

### no-new-capability / teacher ceiling

症状：标准 OPD 可能只是贴近 teacher，无法超过 teacher 边界。

方法族：G-OPD/ExOPD 把 OPD 写成 KL-constrained RL，λ>1 做 reward extrapolation；KDRL/LUFFY 等把 KD 与 RL 混合。

未解决：超越 teacher 需要区分 reward quality 与 contract safety，且依赖 reference model 选择。

### structured-output-cliff

症状：λ>1 reward extrapolation 在 JSON/function-call/listwise 等 near-deterministic structured outputs 上可能突然破坏 parse/format contract。

方法族：Extrapolation Cliff 给出 λ* threshold 和 parse validity / contract adherence 指标。

可信度：中。structured-output 结论较强，但开放式 reasoning 是否存在类似 sharp threshold 不能直接外推。

## 证据可信度分层

高可信 anchor：GKD、MiniLLM、DistiLLM、DistiLLM-2、TAID、EOPD、OPSD、HDPO、TIP、SOD、ROPD、SimCT 等有 survey 覆盖、较清楚 source anchors、开源或会议信号的论文，适合作为 baseline 和谱系 anchor。

中可信机制假设：Revisiting OPD、Rethinking OPD、Rock Tokens、Prune-OPD、Full Rollouts、ESR、SFD、KAT、TrOPD、Geometry、Dense-Sparse、EffOPD、G-OPD、Extrapolation Cliff 等 2026 新论文。它们对 idea 很有价值，但很多结论仍需复现。

低到中可信但高 novelty-risk：OpenReview anonymous 或低复现状态候选，如 Capacity Gap Rethinking、Segment-Level OPD、部分 ReNIO/SSOPD 分支。不能当可靠事实唯一来源，但如果你的 idea 触及同一 failure mode，必须纳入 novelty risk。

需要谨慎：black-box/API teacher 路线常依赖闭源 teacher、LLM judge 或动态 discriminator，复现链条弱；其 novelty 重要，但证据权重要低于 white-box logit OPD anchor。
