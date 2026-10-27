# OPD 已抽卡方法地图：短版

> 2026-10-06 整理：阅读导航；保留原文的时间与覆盖口径，不代表当前全库。最新具体机制见 [failure-mode 诊断](../failure-modes/concrete-failure-modes.md)。

更新：2026-09-28。覆盖现有 77 张正式卡片，完整的一句话分类见[方法索引](opd-method-catalog.md)。下面的八条路线是**本次综合解释**，不是原论文共同认可的分类，也不表示它们彼此互斥。

理解 OPD，可以先抓住一个问题：**学生走到自己的状态上之后，老师提供什么信号，学生又该怎样使用？** GKD 明确以 student 自生成序列接受 teacher 反馈，并允许不同 divergence；因此 OPD 不等于一种固定 KL loss。[原论文摘要](https://arxiv.org/abs/2306.13649)

| 路线 | 核心问题 | 代表与区别 |
|---|---|---|
| **1. 改目标与梯度** | 如何把分布差异转成稳定更新？ | GKD 提供框架，MiniLLM 推导 reverse-KL 更新；DistiLLM 稳定 divergence，EOPD 按熵混合目标，OPD+ 检查梯度估计。 |
| **2. 选监督位置** | 哪些 prompt、轨迹、token 值得学？ | PACED 选能力边界的题，FiRe-OPD 先筛轨迹再加权 token，TIP 兼顾不确定和自信但错误的位置。 |
| **3. 管轨迹与成本** | rollout 多长、坏路径如何修复？ | ESR/Prune-OPD 缩短或动态截断；TRD 先修路径；Lightning OPD 复用离线轨迹，EffOPD 减少参数更新步数。 |
| **4. 构造 context teacher** | 没有外部强老师时，额外信息能否变成监督？ | OPSD 用参考解，OPCD/SDFT 用上下文或示范；MOPD/SSOPD 利用 student 多次采样的成功与失败。 |
| **5. 结合 RL** | 如何兼顾模仿、探索与结果反馈？ | KDRL 合并奖励与蒸馏，TGPO 逐步减弱指导；HDPO 补全失败组的信号，ExOPD 调节 teacher reward 强度。 |
| **6. 改监督接口** | 没有标准 logits、tokenizer 不同或受隐私约束怎么办？ | BOPD 用判别器，ROPD 用 rubric，OPRD 对齐表征，SimCT 对齐短 continuation，DP-OPD 约束更新。 |
| **7. 对齐 agent 结构** | token 信号如何对应步骤、回合和最终成功？ | SOD 调整 step 强度，CHOP 做 segment routing，TurnOPD 管 horizon 与 turn loss，PBSD 构造 turn credit。 |
| **8. 处理多模态与具身** | 老师看见什么、指导什么？ | VOLD/X-OPD 跨模态传递推理信号；Decomposed OPD 分离视觉与语言目标；ViCuR 用可恢复视觉提示；FA-OPD 指导动作与奖励。 |

**最有用的比较方式，是比较“改了哪个环节”。** TIP 与 PACED 都在挑学习内容，但分别控制 token 与 prompt；ESR 与 TurnOPD 都管生成长度，但后者还处理 turn 结构与 loss 分配；OPSD 与 BOPD 都改变监督来源，却分别涉及特权上下文和黑盒访问。不能因为同叫 OPD，就当作互相替代的 baseline。各项机制入口见[完整分类表](opd-method-catalog.md)。

**另有两组材料要分开读。** AKL、TAID、SPIN、LUFFY、HPD 等是邻近机制；尤其 HPD 明确采用离线数据加轻量近似 on-policy sampling，不能等同于完整 student rollout。[HPD 摘要](https://arxiv.org/abs/2604.20244) Geometry、Many Faces、States Not Tokens 等主要帮助理解边界与现象，不应全算作新算法。

**证据边界**：八条路线归纳自现有卡片，不是对全部论文的新一轮精读。我们能据此定位要读哪些方法，不能据此判断谁最强、哪条路线已解决问题。不同 teacher、信息权限、验证器、生成预算和任务会改变比较结果；开源和机构信息尚未统一审计。
