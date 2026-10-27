# TGPO 全文精读：failure mode、方法、实验与边界

核查：2026-10-05，arXiv 2605.13230v2（2026-05-28）。此文是 L2 精读笔记，不修改旧 L1 schema 或旧正文。

原论文：https://arxiv.org/abs/2605.13230v2 。本地 PDF：`../../tmp/tgpo/tgpo-v2.pdf`；按页抽取：`../../tmp/tgpo/tgpo-v2-pages.md`；HTML 抽取：`../../tmp/tgpo/tgpo-v2-html.md`。复用 `scripts/cache_paper_sources.py` 的 fetch/pdf_to_text/html_to_text，缓存路径局部覆盖为项目内 tmp/tgpo，未写默认 home 缓存目录。已视觉核对 PDF pp.5/6/8/13 的公式、主表、退火实验和 1.5B 结果。

## 一句话与定位

事实：学生生成轨迹，teacher 在学生每个前缀上提供 top-1 下一 token；用 teacher-target cross-entropy 加 GRPO，逐步撤掉 imitation guidance。它是显式目标动作监督，不是把 teacher 分数乘进已有 advantage。训练主体是数学 RLVR；非环境反馈 OPSD。

解释：方法形式简单，与 student-state imitation / DAgger 式纠正思路相近；其论文主张集中在 RKL rejection regime 的诊断、与 RLVR 配合及退火。这里不是完整 novelty check，不据此断言被 prior art 完全覆盖。

## Failure mode 与诊断（pp.2–4；附录 A pp.11–12）

- teacher 与 student 的生成分布差异大，学生常访问 teacher 不喜欢的动作/轨迹。样本 intrinsic reward 为 log p_teacher(y) - log p_student(y)，出现大负值。
- sampled PG 更新惩罚学生实际采出的动作，没有像 hard teacher target 一样显式指定下一步替代动作；teacher 喜欢而学生几乎不采的动作难以被直接强化。
- 无界负 log-ratio 放大样本梯度，作者观察训练分数崩溃、梯度 spike、response length 逼近 8192 上限。序列级概率比会随轨迹长度累积。
- 原始诊断：Qwen2.5-Math-1.5B student，比较同家族 Qwen2.5-Math-7B teacher 与跨家族 Qwen3-30B-A3B teacher；同家族 RKL 较稳定，跨家族不稳定（Figure 2）。

边界/解释：这不是证明 RKL 梯度在数学上没有方向。完整 RKL 和其精确梯度仍提供分布匹配信号；论文批评的是 sampled log-ratio 在所测大分歧优化设置中的可用性。换 teacher 同时改变规模、训练数据、风格及能力，不是仅改变 divergence 的严格因果实验。附录展示 log-ratio 可无界及方差风险，不是 TGPO 收敛/最优性证明。

## 方法（pp.4–5）

1. 同一数学 prompt 采样 K=8 个学生完整 rollout；生成时不混入 teacher token。
2. 固定 teacher 对完整学生轨迹做一次因果前向，每位置取 a*_t = argmax_v p_T(v | x, y_<t)。这些目标均以原学生前缀为条件，不组成一条重新生成的 teacher trajectory。
3. 对规则验证器给出的结果奖励，组内中心化/标准差归一化得到 A_i。GRPO 部分使用 student/old-student token likelihood ratio，按 batch 总 token 数归一化；正文公式省略 clipping 与 reference KL，不等同于完整标准 PPO loss。
4. teacher guidance 用 L_G = E[sum_t -log p_theta(a*_t | x,y_<t)]，直接训练 teacher target 的概率。
5. 以一致的 loss 符号表达：L_total = L_RL + w_s L_G。w_s = max(0.002 - 0.00001*s, 0)，第 100 步为 0.001，第 200 步为 0，总共 300 步。

公式记号边界：论文先将 J_RL 定义为最大化的 reward surrogate，将 J_G 写成正 CE loss，Eq.3 又写 J_TGPO=J_RL+wJ_G，存在最大化/最小化符号不一致；上式是按提高 teacher target 概率的文字说明统一成最小化 loss。不能机械照抄原文符号。guidance 写为 token 求和，RL 写为总 token 归一化，故 0.002 不能解释为固定 0.2% 教师占比。

易懂例子（解释）：学生在某个前缀选 A，teacher 首选 B。sampled log-ratio PG 是对 A 加奖惩；TGPO 在同一学生前缀直接增加 B 的概率。后续 token 的 teacher targets 仍看原来带 A 的学生轨迹，不把全部 B targets 拼成 teacher 生成序列。

## 实验设置（p.5；附录 B p.12）

- 主 student：Qwen2.5-Math-7B；小 student：Qwen2.5-Math-1.5B。主 teacher：Qwen3-30B-A3B；另测 R1-Distill-Qwen-32B 和同家族 teacher。
- 统一 OpenR1-Math prompt 数据。为离线/混合 baseline 重采 teacher traces 并用 Math-Verify 过滤，得到 34975 个 prompt/trace 对。TGPO 不使用离线 trace，但 GRPO 仍需要可验证目标答案，不能将“只要 prompt”理解为无标签训练。
- RL 方法每 prompt 8 rollouts，学习率 1e-6，300 steps，8×A100，verl/vLLM。SFT 为 3 epochs、batch 64、学习率 5e-5。数学 student 扩 RoPE/context 到 16384，rollout 上限 8192；teacher/student vocabulary 维度对齐。
- ID 六个数学 benchmark：AIME24、AIME25、AMC 用 avg@32；MATH500、Minerva、OlympiadBench 用 pass@1。跨任务 OOD：ARC-c、GPQA-Diamond、MMLU-Pro；推理 temperature=0.6。
- baselines：OP Distill、KDRL；SimpleRL-Zero、PRIME-Zero、Oat-Zero、GRPO++；SFT、LUFFY。

## 结果（Table 1 p.6；Table 3 p.13）

| 7B 方法 | 六个数学 benchmark 均分 | 三个 OOD benchmark 均分 |
|---|---:|---:|
| SFT | 39.5 | 46.1 |
| LUFFY | 44.4 | 56.4 |
| GRPO++ | 43.4 | 52.1 |
| KDRL | 41.7 | 53.6 |
| OP Distill | 25.7 | 18.4 |
| TGPO 固定 guidance | 44.1 | 56.0 |
| TGPO 退火 | 45.6 | 56.8 |

- vs KDRL：ID +3.9、OOD +3.2；vs GRPO++：+2.2/+4.7；vs LUFFY：+1.2/+0.4。不是每个 benchmark 都最好，不能只拿崩溃的 OP Distill 展示优势。
- teacher 自身 ID 68.6（不限于 8192 的报告设置）/46.0（8192 cap），student 45.6；未证明超 teacher。
- 1.5B 六数学均分：TGPO 33.5、GRPO++ 32.2、LUFFY 25.7、OP Distill 16.2、KDRL 4.7。对稳定强 RL 的增益仅 +1.3；主要显著差异是避免不稳定方法崩溃。
- 均分混合 avg@32 和 pass@1 的 benchmark 分数，不是全题目 micro accuracy。分数差均按百分点/得分点表达。

## 消融与其能支持的结论（pp.7–8）

- teacher ablation（Table 2，四个选定任务均分）：No Teacher 55.0，R1-Distill-Qwen-32B 57.4，Qwen3-30B-A3B 58.0。仅两种 reasoning teachers，不是对各种 architecture 的广泛保证。
- in-family（Figure 5）：1.5B student / 7B teacher 100 steps，TGPO training reward 最好；该部分主要给训练曲线，不能当完整同家族 held-out benchmark 证明。
- fixed vs annealed 主表：44.1→45.6 ID、56.0→56.8 OOD；新增的最优性并非全部来自新 guidance，退火有可见贡献。
- Figure 6 四 schedule：constant w0=0.002；aggressive w0=0.02、delta=1e-4；continuous w0=0.002、delta≈6.7e-6（300 步归零）；ours w0=0.002、delta=1e-5（200 步归零）。ours 的最终 training reward 最好。
- 解释：early guidance 有用、持续太强会压制探索；但 aggressive 同时改变初始强度和衰减速度，是复合条件，不完全分离两因素。未证明第 200 步是跨任务最优切换点。

## 局限与缺口（阅读判断）

1. 数学训练、两个 student、少量 teacher；没有 Agent、真实工具执行、多模态或跨 tokenizer 证据。Qwen2.5→Qwen3 是 cross-family 但不意味着任意架构/词表。
2. top-1 hard target 丢掉 teacher 多解和不确定性；未见 hard vs soft、top-k guidance 的直接消融。bad prefix 上 teacher 的 top-1 仍可能不可靠，算法没有专门可靠性过滤。
3. 每 prompt 8 rollouts / 300 steps 不是计算成本严格相同：有 teacher forward，混合方法有离线 traces；未见系统性 wall-clock/teacher-token 成本收益表。
4. 未见主结果 multi-seed 均值、误差条、显著性检验；对强 baseline 的小差距需要谨慎。1.5B 崩溃方法报告 best checkpoints，但选择协议并未充分说明。
5. 超参 schedule 经经验比较，论文没有清楚的独立验证集超参选择流程；不能把 sweep 观察当理论定理。
6. RKL 诊断中的 teacher 变更有多个因素；完整 RKL、稳定化 sampled estimator 与 direct hard supervision 的区别需进一步拆分。
7. 学术 novelty 判断需要对照已有 student-state imitation/DAgger+RL；当前全文证据支持它是清晰的 failure-driven 方案，不支持仅凭名称断言全新范式。

## 结论的准确表述

事实：在所测数学跨家族 OPD/RLVR 设置中，teacher-target CE + GRPO + annealing 相比 RKL 系方法更稳定，且在多个 held-out benchmark 获得较好均分。

解释：最值得学的是将“难以靠惩罚采出替代动作”的 failure mode 对应到“直接训练替代动作”这个操作，再用诊断曲线、主结果和 schedule 消融构成证据链。它不证明所有 OPD 都该换 hard top-1，也不证明退火超参有普适最优性。
