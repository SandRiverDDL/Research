# 04. Idea Hooks 与开放问题

> 本卷面向 idea 生成。每个 hook 都尽量避免“在已有方法上加一个权重”式增量。

## Hook 1: Trust-calibrated OPD controller

Hypothesis：OPD 需要 state-level reliability controller，联合 support overlap、teacher entropy、student entropy、near-future divergence、verifier outcome、prefix depth、token/window utility，而不是单一 KL/entropy/position rule。

为什么不是 incremental：它不是再提出一个 token weight，而是把 Revisiting、TIP、ESR、KAT、SFD、TrOPD、Prune-OPD、Near-Future 的局部判据统一为可 ablate 的 trust policy。

最小验证：固定 teacher/student/prompt，系统干预 rollout horizon、support truncation、trajectory refinement 和 trust-region masking；按 state bucket 比较 teacher signal quality、downstream reward、format validity、训练成本。

强 baseline：Revisiting OPD、TIP、SCOPE、ESR、TrOPD、Prune-OPD、KAT、Near-Future Guidance。

Reviewer 攻击点：controller 是否只是更多 heuristics；每个信号是否真的有独立贡献；frontier model 更强后 teacher reliability mismatch 是否还存在。

需要 L2 deep note：Revisiting、TrOPD、Prune-OPD、KAT、Near-Future。

## Hook 2: Distillability predictor before OPD training

Hypothesis：OPD 成败可以在训练前或前几百步通过 teacher-student pattern compatibility、shared top-token mass、student pass-rate frontier、teacher confidence decay、early update sparsity 预测。

为什么不是 incremental：它改变的是 OPD 的前置决策：是否该蒸、选哪个 teacher、选哪些 prompts、是否先 cold start，而不是提出新 loss。

最小验证：对多 teacher/student pair 做短跑 profiling，预测 full OPD 最终收益；要求能淘汰“更强但不可蒸”的 teacher。

强 baseline：TAID、Rethinking OPD、Capacity Gap Rethinking、PACED、BRTS、Geometry OPD。

Reviewer 攻击点：predictor 是否只是 dataset-specific；短跑指标是否泄露最终验证集；是否比直接跑小规模 OPD 更省。

需要 L2 deep note：Rethinking OPD、Capacity Gap Rethinking、TAID、PACED、Geometry / Dense-Sparse。

## Hook 3: Multi-granularity routing for long-horizon agents

Hypothesis：token、step、segment、trajectory 四种粒度应该由 state transition type 自动选择。纯文本 reasoning 可用 near-future route；tool agent 在 observation boundary 后转向 step/segment route；错误 path 则先 refine trajectory。

为什么不是 incremental：TIP、SCOPE、SOD、Segment-Level、TRD 各自固定粒度。这个 hook 攻击的是 granularity selection 本身。

最小验证：构造含纯文本、tool call、multi-turn planning 的 controlled benchmark；要求同一框架在不同 boundary type 下自动选择监督粒度，并报告 local credit 与 final return 的 alignment。

强 baseline：TIP、SCOPE、SOD、Segment-Level OPD、TRD、Near-Future Guidance。

Reviewer 攻击点：粒度选择是否依赖人工标注 boundary；不同任务混在一起是否让 benchmark 过于复杂；统一框架是否牺牲单任务最优性能。

需要 L2 deep note：SOD、Segment-Level/CHOP、TRD、Near-Future、TIP。

## Hook 4: Negative trajectory as structured counterfactual, not noise

Hypothesis：错误 rollout 只有在能定位可修复 counterfactual branch 时才应加权；否则应丢弃或 refine。negative trajectory 的价值不在“失败样本更多”，而在暴露 teacher-student decision boundary。

为什么不是 incremental：它不是简单利用失败样本，而是定义错误轨迹什么时候是 high-information supervision。

最小验证：同 prompt 多 rollout，标注错误类型；比较 negative-only、positive-only、correct-wrong contrast、refined-negative、counterfactual-branch weighting。

强 baseline：MOPD、SSOPD、ReNIO、TRD、BRTS。

Reviewer 攻击点：错误类型标注成本高；counterfactual branch 是否可靠；是否能超过简单 verifier-pass filtering。

需要 L2 deep note：MOPD、SSOPD、ReNIO、TRD。

## Hook 5: Privilege internalization taxonomy and benchmark

Hypothesis：PI 的可内化性取决于它是 shared latent rule、stable preference、task-specific hint，还是 instance-specific answer clue。只有前两类更可能蒸成 PI-free inference policy。

为什么不是 incremental：它把 OPSD/HDPO/PBSD 的成败边界变成可测试 taxonomy，而不是继续堆 privileged teacher。

最小验证：同一模型/任务下人工构造 PI 类型，测训练收益、PI-free 推理泛化、teacher-student aggregation collapse、对 unseen PI category 的 transfer。

强 baseline：OPSD、HDPO、PBSD、Many Faces、On-Policy Context Distill、Online Experiential。

Reviewer 攻击点：PI 分类是否主观；benchmark 是否只验证构造规则；shared latent rule 与 task distribution 是否混淆。

需要 L2 deep note：Many Faces、OPSD、HDPO、PBSD。

## Hook 6: Representation-assisted trust OPD

Hypothesis：output-space KL 在 late-stage 方差高且容易受 tokenizer/special-token 影响；hidden-state alignment 可作为 trust signal 或 auxiliary objective，但只应在 teacher/student representation compatible 的 region 使用。

为什么不是 incremental：它不是把 OPRD 全程加到 OPD 上，而是用 representation signal 参与 trust routing，避免全程 hidden MSE 变成另一个强 teacher forcing。

最小验证：比较 output-only、representation-only、trust-gated hybrid 在 same-family、cross-architecture、cross-tokenizer settings 的收益；报告 layer choice、projector 成本、tokenizer mismatch、late-stage variance。

强 baseline：OPRD、Revisiting OPD、SimCT、TrOPD、VOLD。

Reviewer 攻击点：hidden states 是否可访问；不同架构 hidden alignment 是否 meaningful；gating 是否只是过拟合。

需要 L2 deep note：OPRD、SimCT、TrOPD、VOLD。

## Hook 7: API-only process credit from rubrics

Hypothesis：black-box teacher 的 rubric/verbal feedback 可以被拆成 step-level 或 segment-level process credit，而不是只做 sequence-level reward。

为什么不是 incremental：它攻击 API-only teacher 的核心短板：没有 logits 导致 credit 粗。如果 semantic rubric 能映射到 process credit，就能连接 ROPD/BOPD 与 SOD/Segment-Level。

最小验证：API teacher 只输出 rubric 和 pairwise judgments，student 生成 multi-step trajectory；评估是否能恢复 useful token/step-level gradient，并和 dynamic discriminator、sequence-level rubric reward 对比。

强 baseline：ROPD、BOPD、Lion、SOD、Segment-Level OPD。

Reviewer 攻击点：LLM judge bias；rubric 是否泄露答案；process credit 是否稳定；API 成本是否可接受。

需要 L2 deep note：ROPD、BOPD、Lion、SOD。

## Hook 8: Contract-aware reward extrapolation

Hypothesis：reward extrapolation 需要 task-dependent safety controller：structured output 控制 λ 不越过 parse/contract threshold，开放式 reasoning 用 support overlap、format validity、verifier confidence 和 output entropy 估计外推风险。

为什么不是 incremental：不是再调 λ，而是同时建模“超越 teacher”的收益和“越界崩塌”的风险。

最小验证：在 JSON/function-call/listwise ranking 与 math/code reasoning 上做 λ sweep；同时报告 task reward、parse validity、format repair cost、teacher-student divergence、support overlap。

强 baseline：G-OPD、Extrapolation Cliff、OPD+、EOPD。

Reviewer 攻击点：structured-output cliff 能否外推到开放式 reasoning；λ threshold 是否任务特异；controller 是否牺牲 extrapolation gain。

需要 L2 deep note：G-OPD、Extrapolation Cliff、OPD+。

## 优先级建议

如果目标是提出真正新颖的顶会 idea，优先级不是按论文数量排序，而是按“能否改变问题定义”排序：

1. Trust-calibrated controller：最贴近当前 OPD 主矛盾，direct novelty risk 最高，也最可能产出主线方法。
2. Multi-granularity routing：适合 agentic / long-horizon 方向，能避开单纯 token weighting。
3. Distillability predictor：如果做得好，能变成 OPD 前置评估框架，评价价值高。
4. Privilege internalization taxonomy：更像 benchmark/taxonomy paper，适合做机制分析。
5. Representation-assisted trust：有潜力但工程依赖强。
6. API-only rubric process credit：应用价值高，证据链和 judge 风险也高。
7. Contract-aware extrapolation：适合 structured output / tool call 子方向。

下一步生成具体 idea 时，不要把 71 张卡全塞进上下文。先选一个 hook，读取本卷 + 相关 5-8 张 cards + 对应 novelty-risk candidates，再做 reviewer-mode pressure test。
