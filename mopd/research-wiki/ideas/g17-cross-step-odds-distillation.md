---
type: idea
node_id: idea:g17-cross-step-odds-distillation
title: "跨步骤交叉比蒸馏"
stage: archived
outcome: pending
added: 2026-10-15T13:48:26Z
based_on: ["paper:sun2026_distill_what_you", "paper:di2026_understanding_off_onpolicy"]
target_gaps: ["gap:G17"]
tags: ["MOPD", "G17", "L3", "provisional"]
---

# 跨步骤交叉比蒸馏

**stage:** `archived`  ·  **outcome:** `pending`

L3-A2；原优先1，2026-10-17已撤回；未运行pilot，provisional。

【2026-10-17判断修订】创新性与训练吞吐／框架侵入性的理由不足，撤回推荐并归档；不是文献完整覆盖或实验否定，outcome保持pending。当前判断见[报告顶部修订](../../synthesis/g17-idea-report.md)。

## Thesis
【候选方法；L3-A2；原优先1，2026-10-17已撤回】

1. 从同题两条 student 轨迹找到两个均局部有效的早期选择 p₁、p₂，以及两个后续片段 v₁、v₂；用解析规则确定同一种依赖关系。
2. 让后续专长 teacher 在两个完整前缀下分别评分两个片段，形成2×2矩阵；仅需 teacher-forced scoring，不生成反事实 rollout。
3. 在普通 MOPD 外匹配该矩阵的交叉 log-odds，使 student 保留早期选择如何改变后续偏好；所有对照共享四种评分与样本。

最小形式：s_M(i,j)=log P_M(v_j|p_i)，Δ_M=s_M(1,1)+s_M(2,2)−s_M(1,2)−s_M(2,1)。L=L_MOPD+λ E[(Δ_θ−stopgrad(clip(Δ_B,−c,c)))²]；B 为已验证局部可靠的后续 expert。优先使用等长、语法有效片段；Δ 消除可分离的行列加性偏置，但不自动证明因果性。

【待验证假设】【待验证】局部可靠信号可能在有限训练中主要传递边际偏好；显式传递两个决定之间的条件偏好变化，比增加相同局部 loss 更有效。完整历史模型本可表示该关系，候选改变的是监督对象。

【原文覆盖与候选差异】
- [Distillation as Probability Transport: Routed On-Policy Distillation (RouteOPD)](https://arxiv.org/html/2609.08337v1)（§3.1–3.3, Eq.3–12；§3.3 shared bounded token potential；§2 action-space versus temporal selection）：已有覆盖：pairwise log-odds和可共同实现的teacher目标已有OPD方法，必须成为强对照。 剩余差异：RouteOPD的pair位于一个state的词表；本候选约束两个不同prefix间的条件偏好变化，且对象可为多token片段。此delta具体可检验。
- [Relational Knowledge Distillation](https://arxiv.org/pdf/1904.05068)（§3.2 Eq.4；§3.2.1 Eq.5–8；§3.2.2 Eq.9）：已有覆盖：关系potential蒸馏、传递高阶结构并消去低阶属性已有一般框架。 剩余差异：候选的条件log-prob四项差分不是RKD的距离/角度实例结果；须证明这一特定potential的任务价值，不能宣称关系蒸馏本身新。
- [Knowledge Amalgamation for Multi-Label Classification via Label Dependency Transfer (ANT)](https://ojs.aaai.org/index.php/AAAI/article/view/26190/25962)（Proposed Method: ANT, pp.3–4；Transfer Indicator；Knowledge Transfer Module；Figure 3）：已有覆盖：多个partial teachers的依赖知识能够进入同一student已有直接方法。 剩余差异：ANT通过共享label调整teacher条件预测；候选针对自回归prefix×suffix的关系，方法目标与数据对象不同。

最小证伪：先离线构建约128个可执行的2×2配对，保留部分重叠三suffix组，检查B的Δ是否预测真实配合、是否存在clip循环冲突；再以小型参数化student固定同四格监督比较KD与关系loss的未见关系泛化。这是便宜且直接的证伪路线，不需要先跑2k题LLM训练。未运行；实际GPU预算未指定，tokens估算未测速。

完整比较与成本见[本轮报告](../../synthesis/g17-idea-report.md)，原始版本见[候选集](../../synthesis/g17-idea-candidates.json)。

## Key risks
本轮有限查新：PROCEED；新颖性评分6/10仅供排队。同模型交叉审阅，结论provisional。未运行pilot，outcome保持pending。

这是RKD的一种potential加反事实数据增广；如果在同一四格评分上的普通KD或sequence preference已经达到同样效果，专门交叉比损失没有方法必要性。

- 【数学核查】Δ确实消除任意行偏置a_i及列偏置b_j，但仅是条件关联，不自动具有因果解释。不同prefix之外的任务信息、文风或token长度差异仍可产生大Δ。
- 【命名风险：不可共同实现的截断】对重叠配对分别clip(Δ_B)可能破坏关系恒等式。例如固定p1/p2、三个suffix时，未截断D13=D12+D23；若D12=D23=0.8c，分别clip后D13=c而两者和=1.6c。候选没有定义如何处理冲突；不能把零loss可实现性当保证。
- 【采样分布】p1、p2可来自student，但v2放到p1之后形成未按该条件采样的状态。因此整体是on-policy MOPD加反事实off-policy scoring辅助loss，不是完整无偏on-policy目标。
- 仅匹配Δ允许四个候选suffix的绝对概率都很小；普通MOPD承担边际学习。关系误差下降不能替代部署成功。
- B在自然配对上的局部可靠性不认证它在交叉组合上的可靠性；语法有效和等长也不能保证语义有意义。验证与配对成本须计入，禁止默认免费oracle。

停止条件：若B的条件关系不对应执行依赖，或打乱配对/同数据普通KD完全复现联合收益，则该具体方法主张不成立；发现局部clip冲突则记录原方法数学缺陷，不在本审阅中替它新增修复模块。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

