---
type: idea
node_id: idea:g17-counterexample-union
title: "联合排错：从多个不完整的反例专家获得监督"
stage: archived
outcome: pending
added: 2026-10-15T13:48:25Z
based_on: ["paper:he2026_learn_from_whoever", "paper:wang2026_madopd_breaking_ceiling"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L1", "provisional"]
---

# 联合排错：从多个不完整的反例专家获得监督

**stage:** `archived`  ·  **outcome:** `pending`

L1-A2；降低本轮投入优先级；未运行pilot，provisional。

## Thesis
【候选方法；L1-A2；降低本轮投入优先级】

1. student 对每题独立生成4个完整候选；每位 teacher 只负责指出自己擅长的一类错误，并给一个具体反例。
2. 用可执行规格检查反例是否确实使候选违反要求；无效反例不参与监督。teacher 无须知道正确完整程序。
3. 合并经过验证的否决，将 student 在候选集合中的概率质量重新分配给未被否决者；全被否决则该组不更新。未被否决不被标注为正确。
4. 持续在新的 student 自采样候选上重复；部署移除 teachers，保留一个 student。

最小形式：候选y₁…y₄由当前student采样，b_m=1表示不存在已验证反例；q_m∝stopgrad(πθ(y_m|x))·b_m，最小化−Σ_m q_m logπθ(y_m|x)，Σb_m=0时跳过。

【待验证假设】【待验证】不同 teacher 虽不能生成正确整题解，却能发现互不重合的致命错误；经过联合排错得到的相对监督，比单 teacher 的正答案模仿更可靠。反例正确性由规格执行验证，错误发现仍来自teachers。

【原文覆盖与候选差异】
- [ExVerus: Verus Proof Repair via Counterexample Reasoning](https://arxiv.org/html/2603.25810)（§2.3 Definition 2.2；§3.1 Counterexample Generation with Validation；§3.2）：已有覆盖：生成、验证具体反例并据此改进程序证明已有直接机制。 剩余差异：ExVerus 做推理时修复；候选把多个专长否决集合用于训练一个无teacher部署模型。
- [Learning to Disprove: Formal Counterexample Generation with Large Language Models](https://arxiv.org/html/2603.19514)（§2 Formal Counterexample Generation；§3.1；§3.2 Multi-reward Guided Training）：已有覆盖：不依赖完整正解、生成可形式验证反例并从验证信号训练已有工作。 剩余差异：它训练反例生成器及证明器，没有本候选的多critic生存集合目标。
- [Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning](https://arxiv.org/html/2506.03136)（§3.1 Eq.1；§3.2 Theorem 3.1；§3.3 Eq.3–4）：已有覆盖：可执行测试的错误识别能力用于训练coder和tester，且不要求ground-truth code。 剩余差异：候选强调多种已认证的具体否决，CURE的coder主奖励仍基于ground-truth tests；多teacher价值和具体重加权规则尚未被该文完整包含。

最小证伪：未运行。对固定100题×4个已有student候选，只做认证反例过滤与独立隐藏规格审计；测联合否决相对最佳单critic是否提升真实正确候选比例、全否决率及共同盲区率，并比较uniform与原π加权的有效样本数。无需训练。实际GPU预算未指定，token估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分4/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。 archived仅表示本轮降低优先级，不代表被完整scoop或实验否定。

与既有反例驱动改进、测试生成和拒绝采样训练相比，剩余方法差异很薄；目前唯一具体重加权还重复使用proposal，可能只是额外自锐化而非互补能力整合。

- R2-PROPOSAL-DOUBLE-COUNTING：y_m 已按 π_old 采样，随后 q_m∝π_old(y_m)b_m 又乘一次 proposal。对保留样本重复计数的经验分布，大样本极限为 Q(y)∝π_old(y)^2 Pr(b=1|y)，而不是 π_old(y|b=1)。四样本自归一化有额外有限样本偏差。有限候选目标本身合法，但不能解释为单纯条件化或精确KL投影。
- R2-UNSUPERVISED-SHARPENING：所有候选均未被否决时仍产生偏向当前高概率输出的自强化；没有新专家证据也可能压缩熵。该效应可能制造 apparent training gains，亦可能锁定高概率错误。
- R2-SURVIVAL-NOT-SOUNDNESS：认证一个反例可以可靠否决，但没有反例不认证程序。联合critic可能留下共同盲区，或将全部组否决，导致训练停滞；原方法没有从全否决组取得方向性学习信号。
- R2-SPECIFICATION-ORACLE：必须确有可执行规格判断反例输出是否错误。普通自然语言题只有候选程序和teacher声称的expected output时，仅运行程序不能证明反例有效。完整参考程序不是唯一方式，但若使用它需计入信息与数据条件。
- R2-METHOD-VS-RL：当前增量主要是多来源测试/反例的并集。二值生存奖励、拒绝采样SFT或测试精度优化可能完全复现；不能仅凭反馈来自teacher就排除这些直接基线。

停止条件：若正确候选占比没有增加，或有效训练组稀少，核心信号假设失败；若优势仅来自π自锐化，或等反例预算RFT/RL复现，则当前独立方法价值不足。没有找到完整直接覆盖的单篇论文，故不作ABANDON。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

