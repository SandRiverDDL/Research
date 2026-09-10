---
title: "Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding"
authors: [Hee Suk Yoon, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2606.00564
source: https://arxiv.org/abs/2606.00564
---

- **一句话**：把 VLM OPD 拆成 language prior 与 visual grounding 两个梯度子空间，再定向加强较弱的视觉更新。

- **Failure mode**

  - Monolithic compromise：标准 VLM OPD 把 language prior 与 visual grounding 合进一个 loss，更新方向被迫折中。
  - Visual under-optimization：视觉依赖越强，两类梯度越接近正交，但标准 gradient 仍保持近似固定方向，无法充分跟随视觉信号。（§3.1–§3.2；Figure 3）

- **瓶颈（作者诊断）**：当前 VLM student 的 language prior 已较成熟，visual grounding 才是主要优化瓶颈。Gradient-angle 分析与 inverse steering 共同支持这一判断，但它尚不是跨模型、跨任务共识。（§3.2；§7）

- **核心做法**

  1. 用 Bayes 分解把标准 distillation objective 拆成 language prior matching 与 visual grounding matching。
  2. 构造保留 student language prior、替换 teacher visual likelihood 的 visual target。
  3. Visual Gradient Steering 将更新方向偏向 visual subspace。
  4. Preservation regularizer 避免视觉 steering 损伤语言能力。（§3–§4）

- **方法增量**

  - 相比标准 OPD：不再把 multimodal teacher distribution 当成不可分的单一目标。
  - 相比简单 loss reweighting：先用梯度几何诊断哪个模态欠成熟，再定向改变更新方向。
  - 相比 GRPO：VGS 可作为 visual-grounding regularizer 与 reward optimization 组合。

- **关键证据与边界**

  - Qwen3-VL 8B→2B 时，七项平均 Acc@1 从 43.74% 提至 46.10%；8B→4B 提升 1.56%。（§6；Table 1）
  - Steering 到 language prior 会降低表现；与 GRPO 结合时，VGS 比标准 OPD 高 1.79% 平均 Acc@1。（§7–§8；Table 2）
  - 代价是约 1.375× 单步开销；teacher 本身 visual-blind 时退化为标准 distillation。（Appendix C；Appendix G）
