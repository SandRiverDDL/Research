---
type: idea
node_id: idea:g17-certified-local-actions
title: "用可核验的局部结论构成联合教学目标"
stage: archived
outcome: pending
added: 2026-10-15T13:48:25Z
based_on: ["paper:xu2026_who_teaches_which", "paper:lu2026_beyond_best_teacher"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L1", "provisional"]
---

# 用可核验的局部结论构成联合教学目标

**stage:** `archived`  ·  **outcome:** `pending`

L1-A1；原优先2，2026-10-17已撤回；未运行pilot，provisional。

【2026-10-17判断修订】创新性与训练吞吐／框架侵入性的理由不足，撤回推荐并归档；不是文献完整覆盖或实验否定，outcome保持pending。当前判断见[报告顶部修订](../../synthesis/g17-idea-report.md)。

## Thesis
【候选方法；L1-A1；原优先2，2026-10-17已撤回】

1. student 自采样完整轨迹，每条只选一个已访问前缀；两个 specialists 各提出一个短结论或纠正，并附可执行证书，不要求提供完整解。
2. 证明检查器依据原始题设检验证书；它只检验给定证书，不搜索解答。将通过检查的局部动作合并为候选集，保留其来源。
3. 在该 student 前缀处，对认证动作集合做块级蒸馏；下一轮仍由 student 独立生成。不同 teacher 的必要结论由同一 student 逐渐掌握。
4. 部署只保留 student；若任务原本允许证明检查器，则所有对照同样可用。局部证书只在训练提供。

最小形式：令 C(s) 为通过证书检查的局部动作，q(c|s)∝1[c∈C(s)]·Σ_i p_i(c|s)；在 student 访问的 s 上最小化 KL(q||πθ)，C(s) 为空则跳过。动作是一条短证明语句或纠正，不能把任意全文当一个免费动作。

【待验证假设】【待验证】没有整题可靠 teacher 时，各 specialist 仍能提供互补且可认证的局部结论；其联合支持集足以产生可学习的完整策略。知识来自 specialists，可信性来自只检查局部证书的确定性工具。

【原文覆盖与候选差异】
- [Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning](https://arxiv.org/html/2609.15404v2)（§3.2 Eq.4–5；§3.3 Eq.6；§3.4 Eq.8–10）：已有覆盖：VG-OPD 已以 criterion 局部优势许可多专家，整题成功并非必要条件；因此取消整题门槛已被部分直接覆盖。 剩余差异：候选改为认证 student 当前前缀上的具体动作，并蒸馏认证块的有限支持集；VG-OPD 的原题 probe 和 disagreement mask 不提供这种动作证书。
- [Process-Verified Reinforcement Learning for Theorem Proving via Lean](https://arxiv.org/html/2606.20068)（§3.2 Tactic-Level MDP；§4.1 Define Tactic-level Rewards；§4.2；§5.3 Reward Strategy）：已有覆盖：确定性验证局部 tactics 并用过程反馈训练已有明确方法。 剩余差异：候选从多个 specialists 取得有方向的认证动作目标，区别于对 student 自生成 tactics 赋过程奖励。
- [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs](https://arxiv.org/html/2609.02548v1)（§4.3 Eq.4–5；§4.4 Eq.6–7）：已有覆盖：已有多teacher纠错反馈压缩入单student。 剩余差异：MT-SDPO 的整题资格与词面 sanitizer 不等于具体局部结论的形式认证。

最小证伪：未运行。只做32道已有形式证明题的信号审计：每题选择一个实际student前缀，两位teacher各交一个短动作及证书；已知证明仅用于离线评估动作对目标的贡献，不提供给teacher。比较联合认证集合相对最佳单teacher是否新增可连接的有用动作，并统计非法前缀与无关动作率。实际GPU预算未指定，token估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED；新颖性评分6/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

它是否只是多来源的经过验证 SFT 数据？VG-OPD 已放弃整题赢家假设，过程验证 RL 已训练局部 tactics；候选必须说明新增动作知识如何在相同检查与数据预算下超出这两类强基线。

- R1-CERTIFIED-IS-NOT-PROGRESS：检查器证明结论成立不等于动作推进原始目标。重复题设、恒真命题、冗余 have 均可能认证通过；动作支持集不保证存在通往完整证明的可学路径。不能用通过率代替有用覆盖率。
- R1-STATE-SOUNDNESS：任意 student 文本前缀未必对应合法 proof state。原方法虽要求根据原始题设核验证书，仍须定义错误前缀上的纠正如何成为下一动作；不能把不可信先前断言当公理，也不能假设检查器负责搜索修复。
- R1-FINITE-ACTION-TARGET：若 C(s) 指本轮生成后通过检查的有限去重动作，q 可归一化且块级交叉熵可算；若指所有可认证动作则没有可计算枚举。动作是否含证书、块终止符及不同形式证明是否视为同一动作必须固定，否则概率权重可被表示长度和重复证书改变。
- R1-ONPOLICY-BOUNDARY：监督起点来自 student，成立；teacher 生成块内较晚 token 的前缀则是 teacher-forced，不是全部 token 都来自 student 自采样。应如实记为 student-visited state 上的块级混合蒸馏，而非宣称完整轨迹严格 on-policy。
- R1-INFORMATION-AND-COST：两个 specialists 必须确有互补信息，且制备样例不能隐含完整证明教师。Cross-scoring 每个认证候选的两个 teacher 概率、前缀读取、证书执行和无效提案均须计费。现有 token 数是估算，非实测。

停止条件：若在该任务分布上联合集合没有稳定新增有用动作，或有效动作证书实际依赖完整解生成器，则核心监督充分性前提被推翻。局部有增量但等数据SFT/过程RL完全复现时，方法价值下调，而非据邻近文献直接ABANDON。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

