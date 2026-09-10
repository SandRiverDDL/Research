# OPD Failure Modes — Controlled Vocab

> 卡片 frontmatter `addresses:` 字段允许的 tag 列表。**新增 tag 必须先在这里登记 + 一句话定义**。
> 否则两年后会出现 `exposure-bias` / `train-inference-mismatch` / `distribution-shift` 三个 tag 指同一件事的灾难。
> 每篇 ≤3 个 tag。

## Tag

| tag | 一句话定义 | 典型方法 |
|---|---|---|
| `exposure-bias` | student 训练时见的 prefix 分布（teacher data）和 inference 时见的（自己生成）不一致；error 沿序列复合 | GKD, MiniLLM |
| `mode-collapse-fwdkl` | forward-KL 强迫 student 覆盖 teacher 全部 mode，把概率分给 teacher 的 void region（低质量文本） | MiniLLM |
| `kld-gradient-explosion` | 标准 KLD 在 q_θ→0 时梯度系数 r_{p,q} 无界，训练不稳 | DistiLLM |
| `sgo-generation-cost` | continuous on-policy student-generated outputs 的实时 generation 占训练时间 ≥50% | DistiLLM, EOPD |
| `policy-gradient-variance` | REINFORCE 类梯度估计在 vocab 指数空间里高方差 | (待填) |
| `cross-tokenizer` | teacher / student 不共享 tokenizer，无法直接对齐 logits | DSKD |
| `teacher-staleness` | teacher 在 student 训练过程中始终固定，无法响应 student 当前能力 | iterative-distill 类 |
| `void-region-coverage` | teacher 概率近零的 token 上 student 仍被 forward-KL 约束 | MiniLLM, DistiLLM |
| `compounding-error` | 长序列 reasoning 任务中 prefix 错误对后续 token 的累积影响 | (与 exposure-bias 关联但更窄，专指 reasoning trace) |
| `reward-hacking` | RL-style 蒸馏中 student 找到 teacher 评分高但语义降级的输出 | MiniLLM |
| `api-only-teacher` | teacher 只能通过 API / 文本反馈访问，无法读取 logits、hidden states 或梯度，white-box KD 目标不可用 | Lion, GAD, OVD |
| `coarse-credit-assignment` | response-level reward / preference 把整句质量摊到所有 token，可能惩罚好 token 或奖励坏 token | AlignDistil |
| `source-divergence-mismatch` | teacher-generated 与 student-generated 数据承载的学习信号不同，但训练时使用同一种 divergence / loss | DistiLLM-2 |
| `capacity-gap` | teacher 分布相对 student 当前能力过难，直接模仿导致 mode averaging / mode collapse 或无效梯度 | TAID |
| `cliff-prompt-zero-gradient` | 一组 rollout 全部失败导致 GRPO/PG advantage 无差异，最需要学习的 prompt 反而无梯度 | HDPO |
| `entropy-collapse` | RL/OPD 后期 policy 过早变得确定，rollout 多样性与探索梯度枯竭 | Internalize-the-Temperature |
| `cross-rollout-credit` | 单条 rollout 的 teacher signal 无法利用同 prompt 下成功/失败 rollouts 的对比结构 | MOPD |
| `experience-internalization` | 交互轨迹中的经验若只放外部 memory，推理期仍需额外上下文且难以持续固化到参数 | OEL |
| `privileged-context-gap` | 训练时可用的 ground-truth / context / hint 能显著改善 teacher 分布，但推理时 student 无法访问 | OPSD |
| `flawed-prefix-trap` | student 早期错误 prefix 让 teacher 条件分布变噪，后续 token supervision 可能传播错误 | TIP, SCOPE |
| `large-policy-divergence` | teacher 与 student 分布差距过大时，RKL/log-ratio 只像事后打分，缺少可执行的方向性指导 | TGPO |
| `sampled-token-imbalance` | sampled-token OPD 只看单个采样 token，正负信号高度偏斜，局部 filler/短 continuation 容易支配更新 | Revisiting OPD |
| `special-token-mismatch` | teacher/student 对 special token 或 tokenizer 边界处理不一致，导致 sampled-token log-prob 比较被实现细节扭曲 | Revisiting OPD |
| `teacher-pattern-mismatch` | teacher 与 student 的 reasoning/thinking pattern 不兼容，teacher 分数更高也无法在 student-visited states 上提供可利用方向 | Rethinking OPD |
| `no-new-capability` | teacher 与 student 在 student 视角下分布不可区分或只重复学生已学能力，OPD 只有密集信号但没有新知识增量 | Rethinking OPD |
| `stop-gradient-bias` | OPD 为稳定性对 reward / advantage 里的 student likelihood 停梯度，导致目标或梯度估计相对真实 f-divergence objective 有偏 | OPD+ |
| `tool-call-cascade` | tool-integrated reasoning 中早期错误 tool call 会把错误观察写回上下文，使后续 student-teacher divergence 阶跃式放大 | SOD |
| `order-inconsistent-token-signal` | 聚合 token-level teacher score 与 trajectory outcome ordering 不一致，高 token 分数轨迹可能答案更差 | Uni-OPD |
| `privacy-leakage` | distillation from proprietary/sensitive teachers 可能复制 teacher training data，需要 record-level privacy guarantee | DP-OPD |
| `low-utility-token-supervision` | dense OPD 把梯度/算力长期花在高 loss 但对下游功能贡献很低的 token 或局部模式上 | Rock Tokens |
| `parameter-update-redundancy` | OPD/RL 参数更新集中在低边际收益模块或方向上，训练已经进入可外推但仍逐步小步优化的冗余区 | EffOPD |
| `structured-output-cliff` | reward extrapolation / policy sharpening 超过阈值后，near-deterministic structured output 的 parse/format contract 突然崩塌 | Extrapolation Cliff |

## 维护

- 新增 tag：先 PR 这个文件，再用到卡里
- 同义合并：发现 tag 语义重叠（如 `exposure-bias` vs 之前用过的 `train-inference-mismatch`）就保留前者，全局 sed 替换并在这里加 alias 行

## Alias

- `train-inference-mismatch` → `exposure-bias`
- `distribution-shift` → `exposure-bias`（在 OPD 语境下）
