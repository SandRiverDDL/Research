# G15 L1 定向查新证据（2026-10-15）

来源：只读agent `/root/g15_gen_l1_astra`。事实/锚点与未确认边界，不含novelty verdict或排序。

## 各候选证据

**C01** claims：函数保持改变后续响应Q01/02/05；监督不变且运输optimizer历史Q03/26/27；当前能力不变时等预算收益Q04/06/25。
- [COST NeurIPS25正式版](https://papers.nips.cc/paper_files/paper/2025/file/fa30825df7ceaba452d5533538ea29c2-Paper-Conference.pdf) §4.1/4.3 pp5–7 Eq7–13：LoRA以task loss变化惩罚近似保持loss、随机扰动sharpness近似gradient maximization；cos(teleport位移,旧梯度)调Adam历史系数。不是精确函数对称或moments坐标运输。
- [Improving Learning to Optimize Using Parameter Symmetries](https://arxiv.org/html/2504.15399v1) §3/§4.2 Alg2已先对称变换、再梯度步、按步后loss元训练变换。C01不能仅以“精确函数保持＋lookahead”主张新意；剩余delta是双teacher最弱域有限步收益及等范数控制，尚未证实价值。

**C02** claims：另一teacher有限步收益Q07/08/09；元梯度而非采样份额Q07/10/28；匹配起点后交叉收益Q04/29/30。
- [MER](https://arxiv.org/html/1810.11910) §2/3 Eq4/Alg1以未来transfer/interference为目标，Reptile/replay促进梯度对齐；[La-MAML](https://arxiv.org/html/2007.13904) §4.1–4.2/Alg1在当前任务inner更新后以新旧meta-batch评估，学习参数和逐参数学习率；[Efficient MER](https://arxiv.org/html/2508.01908) §3.2 Eq1周期参数插值用于LLM持续预训练。
- 分析：若投影P消除同点起点query梯度，则P∇(L_before−L_after)=−P∇L_after，投影后的元收益等价于投影终点loss元梯度。完整A/B对称、起点控制组合未在已读文献确认，但不能靠减起点loss声称新机制。

**C03** claims：存成功更新功能响应Q13/14/16；当前Jacobian重建而非保护旧方向Q15/31/32；恢复等起点效率Q04/33/34，追加Q63–66。
- [ONG 2508.17169v3](https://arxiv.org/html/2508.17169v3) §4/Alg1先Fisher逆预条件再投影历史方向，记忆变体在当前模型重算旧样本方向；§6将parallel transport列为未来工作，不是已实现结果。[OGD AISTATS20](https://proceedings.mlr.press/v108/farajtabar20a.html)保护旧样本输出，不保存成功学习响应。
- 未找到直接实现“保存J_old v，再求J_new u≈J_old v，并用u促进未来B学习”的已读原文。ICLR26 OGD+/OPGD检索命中但原文入口验证阻挡；function-space/Jacobian matching及该近邻仍有查新缺口，不能以此断言全新。

**C10** claims：按A后B收益学共享P Q09/11/12；改变几何Q10/35/36；起点/范数匹配交叉收益Q29/30/37。
- [GAP](https://arxiv.org/html/2304.01552) 扩展版§III-A Alg1 Eq7–9元学正对角参数，重标定梯度矩阵奇异值，适应后validation loss训练初始化与preconditioner；La-MAML覆盖持续学习meta学习率。候选剩余delta为B-only/A→B配对、起点条件化目标；需排除仅通用预条件加速，loss分桶不证明能力空间完全匹配。

**C11** claims：保护残差可用切向空间Q17/18/19；保核非预测Q20/38/39；谱与真实收益Q04/33/40。
- [C-CHAIN ICML25](https://arxiv.org/html/2506.00592v1) §4.1–4.3 Eq2–11正则参考输出变化平方，并分析NTK非对角项及步长；不是teacher残差核谱保持。[PLATE ICML26](https://arxiv.org/html/2602.03846v1) §4.1 Alg1固定B/Q后训练ΔW=BAQᵀ，控制旧分布functional drift；不是在线残差核保持。
- [Dynamical Isometry ICML26](https://arxiv.org/html/2606.09762v1) §4 Eq16–20 Gram正交正则与AdamO防传输退化，task-agnostic塑性保持。
- [Learning Dynamics of Continual Learning 2026-09](https://arxiv.org/html/2609.33620v1) §5 Eq7用task-force方向归一化readout Rayleigh quotient衡量未来传输，训练会衰减其他task方向，readout恢复改善后续学习；同时保已有能力与恢复plasticity明确不在诊断scope。目标条件可学性已有直接机制证据，完整Jacobian正则跨teacher方法价值仍未证实。

**C12** claims：另一teacher后续收益改目标Q21/22/24；内容而非预算尺度Q23/41/42；A收益匹配后B更易学Q29/43/44。
- [MetaDistil ACL22](https://aclanthology.org/2022.acl-long.485.pdf) §3.2 Eq2–3 Alg1 pp4–5：复制student虚拟KD，独立quiz loss反传teacher，再丢副本用更新teacher训练原student。未见A监督后B学习、按B边际收益训练A目标修正器的完整链；若只是quiz域换B或增加元验证，则delta薄。MetaDistiller仅摘要，全文未核，不作确定覆盖。

## 实际查询清单

```text
Q01 function preserving symmetry transformation plasticity COST optimizer history 2025
Q02 "plasticity" "reparameterization" "optimizer" "symmetry"
Q03 "COST" "symmetry" "meta" learning
Q04 "continual learning" "plasticity" "same" "loss" learning speed
Q05 "Continual Optimization with Symmetry Teleportation"
Q06 "function-preserving" "learning" "plasticity" 2025 2026
Q07 "meta experience replay" "transfer" "gradient"
Q08 "continual learning" "learning progress" "meta-gradient"
Q09 "meta learning" "adaptation gain" "continual"
Q10 "La-MAML" "learning rates" "interference"
Q11 "meta learned preconditioner" "continual learning"
Q12 "cross-task" "preconditioner" "meta-learning"
Q13 "continual learning" "tangent" "transport"
Q14 "Jacobian" "transport" "learning" "functional"
Q15 "continual learning" "response" "preconditioner"
Q16 "learning directions" "transport" "neural"
Q17 "CHAIN" "NTK" "plasticity"
Q18 "plasticity" "target" "kernel" regularization
Q19 "continual learning" "Jacobian" "spectrum"
Q20 "PLATE" "Plasticity-Tunable"
Q21 "meta distillation" "teacher" "student feedback"
Q22 "knowledge distillation" "meta-learning" "soft targets"
Q23 "multi-teacher" "learning progress" distillation
Q24 "teacher logits" "bilevel" "transfer"
Q25 "plasticity" "same function" "learning"
Q26 "function preserving" "optimizer state"
Q27 "multi-task" "teleportation" "meta-learning"
Q28 "meta-learning" "learning gain" "gradient projection"
Q29 "continual learning" "matched" "initial performance" plasticity
Q30 "cross-task" "learning efficiency" "meta-learning"
Q31 "continual learning" "functional response" "transport"
Q32 "gradient transport" "continual learning"
Q33 "plasticity" "Jacobian" "learning speed"
Q34 "neural" "tangent transport" preconditioner
Q35 "meta-learned" "positive definite" "preconditioner"
Q36 "continual learning" "meta-learning" "update geometry"
Q37 "meta-learning" "preconditioner" "transfer" "continual"
Q38 "target residual" "neural tangent" "plasticity"
Q39 "kernel regularization" "plasticity" "continual"
Q40 "plasticity" "same loss" "Jacobian"
Q41 "multi-teacher distillation" "meta-learning"
Q42 "soft labels" "bilevel" "cross-task"
Q43 "teacher" "future learning" "distillation"
Q44 "knowledge distillation" "student learning gain"
Q45 site:arxiv.org after:2026-04-15 before:2026-10-16 "plasticity" "symmetry"
Q46 site:arxiv.org after:2026-04-15 before:2026-10-16 "continual learning" "meta-gradient"
Q47 site:arxiv.org after:2026-04-15 before:2026-10-16 "gradient transport"
Q48 site:arxiv.org after:2026-04-15 before:2026-10-16 "plasticity" "kernel"
Q49 site:arxiv.org after:2026-04-15 before:2026-10-16 "meta-learning" "preconditioner"
Q50 site:arxiv.org after:2026-04-15 before:2026-10-16 "distillation" "meta-learning" "teacher"
Q51 site:openreview.net "ICLR 2025" "plasticity" "geometry"
Q52 site:openreview.net "ICLR 2026" "plasticity" "Jacobian"
Q53 site:proceedings.mlr.press/v267 plasticity meta learning preconditioner
Q54 site:proceedings.mlr.press/v306 plasticity tangent kernel distillation
Q55 site:openreview.net "NeurIPS 2025" "meta" "distillation"
Q56 site:openreview.net "NeurIPS 2026" "plasticity"
Q57 site:openreview.net "ICLR 2026" "loss of plasticity"
Q58 site:openreview.net "ICLR 2025" "loss of plasticity"
Q59 "ONG: Orthogonal Natural Gradient"
Q60 "Meta-Learning With a Geometry-Adaptive Preconditioner"
Q61 "Improving Learning to Optimize Using Parameter Symmetries"
Q62 "meta distillation" "multiple teachers"
Q63 "Jacobian matching" "continual learning"
Q64 "function space" "gradient transport" neural
Q65 "output changes" "continual learning" "Jacobian"
Q66 "OGD+" "gradients" update
```

检索主要限制一手arXiv/OpenReview/PMLR/NeurIPS，蒸馏加ACL/CVF；Scholar/S2搜索域无新增可核验技术原文。覆盖近六个月与2025/26会议公开索引不等于穷举。NeurIPS26无新增核验结果，部分OpenReview验证阻挡；正式COST已核，其他版本间一致性及未读附录不默认确认。
