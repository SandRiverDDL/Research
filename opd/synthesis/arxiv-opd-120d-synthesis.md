# 近 120 天 arXiv OPD 趋势总结

证据入口：[`arxiv-opd-120d-radar.md`](arxiv-opd-120d-radar.md)。本总结基于 103 篇聚焦候选的 metadata，并窄读代表论文摘要；它反映研究潮流，不把 arXiv claim 当作已证实事实。

## 结论

OPD 没有 idea 枯竭，而是已经从“是否用 student rollout + KL”快速转向更细的核心问题：

> teacher signal 在什么 student state、token、turn 和 trajectory 上仍然可信、可学且值得计算？

最近的论文大多围绕这个问题做条件化：选择、过滤、重加权、curriculum、trust region、teacher handoff 或换一种监督接口。真正尚未稳定解决的不是“再设计一个权重”，而是**如何知道失败发生在哪里，以及局部 teacher 信号是否因果上正确**。

## 热点与瓶颈

| 热点 | 当前瓶颈 | 代表论文 | 判断 |
|---|---|---|---|
| Signal reliability | disagreement、entropy、KL 都只是 proxy，不能保证 teacher 在当前 prefix 上真的能纠错。 | TIP、Uni-OPD、Token Teachability、Supervision Fidelity Decay | 当前最拥挤的主线。继续做静态 reweighting 很容易 incremental。 |
| State / support mismatch | student 进入 teacher 数据和能力支持之外后，dense logits 仍可能很“自信”但无效。 | Rethinking OPD、Extrapolation Cliff、States Not Tokens、Trust Region | 比 token weighting 更底层，仍值得研究。 |
| Long-horizon agents | 错误跨 turn 累积；完整 rollout 昂贵，后段监督变弱，trajectory KL 被浅层 token 主导。 | TCOD、SOD、Prune-OPD、ATOD、TurnOPD、Prefix Replay、Pass the Baton | 与大厂 agent 工作最匹配，但实验周期较长。 |
| Causal credit localization | 最终 outcome 会混淆局部 agreement/disagreement；不知道哪一步使轨迹不可恢复。 | Near-Future Guidance、Tool-Call Boundary Drift、Outcome-Confounded Local Supervision、Pass the Baton | 最新且最有研究空间的方向。 |
| Stability / objective gaming | length inflation、truncation、padding、policy drift 和 KL agreement 都可能让 loss 变好而行为变差。 | StableOPD、KL Agreement Trap、Position Bias、Demystifying OPD、PowerOPD | 现象真实，但单纯 clipping/normalization 已高度拥挤。 |
| Throughput / async | 严格同步生成让 GPU 等待；异步又带来 stale policy 与 off-policy drift。 | Near-Policy、Full Rollouts、AsyncOPD、EasyOPD | 实用价值高；需要系统实验和较强 infra。 |
| Teacher ceiling / capability isolation | 模仿 teacher 绝对分布会继承其错误与无关能力，甚至压制 student 原有优势。 | MAD-OPD、DOPD、MOPD、OPD²、Direct-OPD | “超过 teacher”多半来自新监督、teacher ensemble 或 policy delta，并非凭空自我提升。 |
| Cross-model / multimodal transfer | tokenizer、modality、privileged context 与多 teacher 的接口不一致。 | SimCT、Tokenizer Barrier、BPM、ViCuR、Decomposed OPD | 适合有明确应用场景和数据资源的团队。 |

## 最近四个月的变化

- **4 月：建立诊断框架。** 重点是 thinking-pattern mismatch、token importance、calibration、length collapse 和 agent trajectory instability。
- **5 月：方法爆发。** 43 篇候选集中出现，主要 pattern 是 filter/reweight/curriculum/trust-region，以及把 OPD 扩展到 agent、MLLM 和 black-box teacher。
- **6 月：从 token 转向结构。** position、geometry、sparse effective updates、turn-level guidance、async staleness、cross-tokenizer 与 multi-teacher 开始成为显式研究对象。
- **7 月：开始质疑局部信号本身。** Outcome-Confounded、Tool-Call Boundary Drift、Pass the Baton 把问题推进到“局部 KL 是否能定位真正错误”；OPD²、Direct-OPD 则开始蒸馏 teacher 的增量而非绝对行为。

## 反复出现的 idea pattern

1. **先证明 vanilla signal 在某个条件下失真，再做条件化。**  
   例：entropy/position/turn/outcome-conditioned weighting。

2. **把监督单位从 token 提升到结构单元。**  
   token → step → turn → branch → trajectory → reusable skill。

3. **只蒸馏 teacher 的有用增量。**  
   teacher 相对 base 的 delta、RL 前后 policy shift、debate 后 collective signal。

4. **用少量 teacher intervention 修复关键分叉。**  
   prefix replay、near-future continuation、teacher handoff，而不是全程 teacher forcing。

5. **用近似 on-policy 换吞吐。**  
   异步 rollout、stale sample filtering、短 rollout、selective packing。

这些 pattern 已经很常见。仅把新 proxy 塞进同一套加权公式，通常不够支撑强 idea。

## 关键矛盾

- **OPD 是否突破 teacher ceiling？**  
  Demystifying OPD 将其视为不扩展 ceiling 的 exploration catalyst；MAD-OPD、TCOD、Direct-OPD 等报告超过 teacher。两者并不一定冲突：后者常引入 debate、环境反馈、teacher checkpoint pair 或跨任务 generalization，监督信息已经不等于单一固定 teacher。

- **agreement/disagreement 能否定位学习信号？**  
  TIP 等工作把 entropy/divergence 当有效 proxy；Outcome-Confounded 表明局部 proxy 会被最终 outcome 混淆。当前更可靠的结论是：proxy 能筛选相关位置，但不能单独证明这些位置是错误原因。

- **完整 rollout 是必要信息还是浪费？**  
  全轨迹保持 on-policy state coverage；但后段可能已不可恢复、信号低质且计算昂贵。最近方法倾向动态决定 rollout depth，而不是固定全长或固定截断。

- **Token selection 是否真的提高效率？**  
  TIP 先在完整 teacher/student logits 上以 `no_grad` 分块计算 entropy/divergence，再只为 selected tokens 建立 reverse-KL backward graph；它主要节省 full-vocabulary KL 的 autograd workspace，不节省 rollout、teacher/student Transformer forward 或完整序列 activation。论文的 peak-memory 收益不能等价为端到端吞吐收益，而且会随 fused/chunked KL 实现显著变化。

- **Privileged information 到底内化了什么？**  
  需要区分三类混淆：RLCSD 的 PI presence vs correctness（容易学成长度/风格变化）；Many Faces 的 instance information vs reusable capability（instance-specific PI 缺失时只能聚合多个 conditioned teachers）；Illusion of Certainty 的 teacher conditional success vs student deployment uncertainty（容易学成过度自信）。只有可从输入推断或跨实例共享的规则型 PI，才较可能稳定提升无 PI 推理能力。

## 对选题的直接建议

最值得从以下顺序学习：

1. **Causal failure localization**：Outcome-Confounded → Near-Future Guidance → Pass the Baton。  
   它直接挑战大量 reweighting 工作的共同假设，空间最大。

2. **Long-horizon agent supervision boundary**：TCOD → TurnOPD → Tool-Call Boundary Drift。  
   与大厂 agent 工作匹配，而且“在哪个 turn 介入”比再改 token loss 更容易形成清晰故事。

3. **Async / stale OPD**：Near-Policy → AsyncOPD。  
   实用且竞争相对集中，但更依赖 infra 和严谨吞吐对比。

暂不建议把第一篇工作押在“再提出一个 entropy/KL/advantage 权重”上：最近 120 天这类论文已经过密，novelty 和 reviewer defensibility 都差。

## 可信度边界

- 103 篇大多是非常新的 arXiv，引用与独立复现尚不足。
- 本总结只对代表论文核对了摘要，没有逐篇验证代码可运行性或实验公平性。
- “超过 teacher”“单机可复现”“显著加速”等 headline claim 只能当待验证线索。
- 下一步深读不应覆盖 103 篇；优先回查上述三个建议方向中的 8–12 篇原文，再决定是否抽正式卡。
