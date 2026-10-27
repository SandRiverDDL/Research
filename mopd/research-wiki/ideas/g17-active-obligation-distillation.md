---
type: idea
node_id: idea:g17-active-obligation-distillation
title: "未履行承诺蒸馏"
stage: proposed
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:sun2026_distill_what_you", "paper:he2026_learn_from_whoever"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L3", "provisional"]
---

# 未履行承诺蒸馏

**stage:** `proposed`  ·  **outcome:** `pending`

L3-A4；储备；未运行pilot，provisional。

## Thesis
【候选方法；L3-A4；储备】

1. 在 student 轨迹中识别早期已经作出、仍约束后续动作的承诺，如选定单位、变量绑定、算法不变量或尚未满足的输出要求；由程序规则或局部可靠 expert 标注其有效区间。
2. 在每条轨迹一个较晚位置，仅用 student 此刻最后一个 hidden state 重建仍有效的承诺集合，加入一个小型辅助 decoder loss。
3. 与普通局部 MOPD 联合更新；辅助 decoder 部署时丢弃，student 使用原有完整上下文直接作答。

最小形式：C_t 为截止 t 仍活跃的承诺，h_t 为 student 最后位置表示；L=L_MOPD+λ E_{t~sample}[−log D_φ(C_t|h_t)]。D_φ 只能读取 h_t，不能重新读取完整 prefix；梯度回传 θ。承诺已履行即移出 C_t，避免仅训练复制所有历史。

【待验证假设】【待验证】各局部 expert 的当前动作监督未必足够维持对未来仍有用的约束表示；辅助压缩活跃承诺可能使后续专长更稳定地服从前面的决定。历史原本可访问，问题不是上下文缺失，也不是 teacher 间格式转换。

【原文覆盖与候选差异】
- [Language Modeling with Latent Situations](https://aclanthology.org/2023.findings-acl.795.pdf)（§3.1 Eq.2–3, pp.3–4；Figure 2 caption）：已有覆盖：§3.1 Eq.2–3已有辅助state decoder、共享表示联合训练及推理移除decoder；这两个核心实现主张已明确覆盖。 剩余差异：候选强调未履行义务生命周期、单个最后位置瓶颈，以及MOPD跨专长交接；已读论文监督的是情境/实体状态，未证明精确包含这些结果。
- [The Belief State Transformer](https://arxiv.org/html/2410.23506v3)（§2 Architecture and Objective（页面概览）；§3.3–3.6；§4 Definition 1）：已有覆盖：训练期辅助目标塑造对未来充分的表示、部署不必提供训练辅助信息已有规划研究。 剩余差异：BST用前后向编码与previous-token目标，不是active commitments标签；不能据此否定候选的特定监督对象。
- [Relational Knowledge Distillation](https://arxiv.org/pdf/1904.05068)（§3.2 Eq.4；§3.2.1 Eq.5–8；§3.2.2 Eq.9）：已有覆盖：知识转移可使用隐藏表示和更高阶目标的一般思想已成熟。 剩余差异：它不提供活跃义务预测机制；这里只限制泛称representation distillation的新颖性。

最小证伪：在约128–256个可执行单位/绑定任务中自动产生active、all-state及已履行三类等长度标签；先核验无未来答案泄漏，再以同预算小模型比较联合成功和读出准确率是否分离。优先测试义务寿命和未见组合，不先扩成自然语言标注工程。未运行；实际GPU预算未指定，tokens估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED WITH CAUTION；新颖性评分5/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

辅助decoder预测状态再在推理移除已在ACL 2023明确出现；当前新增主要是标签定义。必须证明active而非all-state/recent-state监督具有独立可迁移价值，才能成为方法贡献。

- 【数学核查】辅助CE目标可定义；C_t必须只由截至t的可用信息确定。依据未来正确答案决定哪些义务活跃，会产生新增答案知识而不是纯记忆监督。
- 【命名风险：可读不等于会用】decoder能从h_t解码义务，不证明生成head在未来步骤利用该表示。decoder也可能即时重算当前容易信息；一次较晚位置监督未保证长程保持。
- 承诺集合需有规范化表示或明确集合损失，否则序列CE会惩罚等价顺序；候选未指定实现。单点采样如何覆盖义务生命周期亦未定义。
- 从当前完整prefix生成标签可能需要额外teacher推理；规则覆盖只在可执行任务可得。自然任务的有效区间和已履行判断不是免费oracle。
- 一般state监督可能已经提供相同改进；多teacher特异性必须来自跨专长共享义务的证据，而不能仅把相同辅助任务加在MOPD上。

停止条件：active标签对真实联合成功不优于同预算普通state supervision，或仅decoder读出提升；若标签包含额外解题信息也不能作为原机制成功。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

