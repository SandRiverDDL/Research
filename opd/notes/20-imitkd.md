---
title: "Autoregressive Knowledge Distillation through Imitation Learning"
authors: [Alexander Lin, et al.]
year: 2020
venue: emnlp-2020
paper_id: arxiv:2009.07253
source: https://aclanthology.org/2020.emnlp-main.494.pdf
---

- **一句话**：ImitKD 将自回归蒸馏表述为 imitation learning，让学生在自己生成的前缀上接受教师的逐 token 监督，缓解只学习静态教师序列带来的 exposure bias。（§2–3）

- **Failure mode**

  - SeqKD 在教师生成的序列上训练，但学生推理时访问自己的前缀；作者将误差累积解释为训练与推理状态分布不一致。（§2.3）
  - 教师能否在学生走偏后继续提供有效监督是关键假设。IWSLT 验证集上，RNN 独立生成为 28.6 BLEU，先由 RNN 生成再由 Transformer 接续为 31.4，Transformer 独立生成为 33.8；这只支持该设置下的纠错能力。（§3.1；Table 1）

- **核心做法**

  1. 从原始训练集或教师生成的 SeqKD 数据集取样，以概率 `1−βᵢ` 将目标序列替换为当前学生生成的序列，构成序列级混合 batch。（Algorithm 1；§3.3）
  2. 教师在这些前缀上重新给出监督：可以学习教师最优下一 token 的 NLL，也可以最小化完整教师分布对学生分布的交叉熵，后者对学生优化等价于 forward KL。（§3.2，Eq. 5–6）
  3. 每个 batch 做一次梯度更新；采用指数衰减的 `βᵢ` 逐渐增加学生序列。用 batch 内替换避免 DAgger 的累计数据集持续膨胀。（§3.2–3.3）
  4. 可每隔 M 步生成一个池，分配给后续 M 个 batch，以降低生成成本；代价是使用最多约 M 步前的学生轨迹。（§3.4）

- **方法增量**

  - 相对 SeqKD：从模仿静态教师序列，变为在学生实际访问的前缀上查询教师。
  - 相对 scheduled sampling：前缀变化后重算教师标签，避免继续使用已不匹配的原始目标 token。（§4）
  - 相对 DAgger：采用序列级混合、batch 内替换和在线梯度更新，教师不必每轮自回归生成完整示范。（§3.2–3.3）

- **关键证据与边界**

  - IWSLT、3-layer SRU、greedy BLEU：SeqKD + Full 为 34.3，ImitKD + Full 为 34.8；二者同用完整教师分布，区别主要在训练前缀。不能把相对 Vanilla 的全部收益都归于 on-policy 数据。（Table 3，PDF p.7）
  - WMT 全量数据上，基础 ImitKD 的 greedy BLEU 为 24.6，低于 SeqKD 的 24.9；方法并非每个变体都占优。减少数据 25 倍时，ImitKD* 为 18.6，SeqKD 为 17.1。（Table 5，PDF p.7）
  - 证据来自翻译与摘要、Transformer 教师和较小学生；不能直接外推至现代长链推理或工具 agent。DAgger 的理论讨论依赖损失等假设，并不是对非凸神经网络的无条件保证。（§3.1；§5）
  - 准入：[判断] 属于 OPD 的经典机制来源，按经典论文项收录；EMNLP 2020 身份由 [ACL Anthology](https://aclanthology.org/2020.emnlp-main.494/) 核验。原论文方法、算法与表格已回查，代码入口为 [asappresearch/imitkd](https://github.com/asappresearch/imitkd)。
