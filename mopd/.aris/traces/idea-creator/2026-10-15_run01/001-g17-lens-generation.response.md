{
  "shard_id": "g17-lenses-astra",
  "candidates": [
    {
      "lens_id": "L1",
      "dedup_key": "g17_whole_problem_correctness_as_supervision_gate",
      "name": "整题正确是否是必要门槛",
      "question": "把提问从“哪位 teacher 会解这道题”改为“多个 teacher 拥有的信息是否足以共同教会这道题”。隐含假设是：有价值的监督必须由至少一位整题成功的 teacher 背书。",
      "structure": "【高风险假设】各 teacher 分别掌握必要能力，却没有任何一位稳定完成整题；部分知识存在可验证的相容关系。这研究监督是否充分及如何识别其有效性，不按数学、代码或任务阶段分类。",
      "prior_boundary": "TU-OPD §3.3–3.4 明确只蒸馏至少一位 teacher 达到成功率门槛的 prompt，winner residual 已保护独有模式。Trust、H-OPD 不采用相同整题成功门槛；SMOPD 还包含在线 RL。因此，TU 的适用边界不能被写成所有 MOPD 的共同失败。",
      "method_opportunity_condition": "必须发现实际且有价值的情形：各 teacher 的有效信息足以支持联合成功，现有整合在公平预算下仍不能利用，原因也不是 teacher pool 根本缺少必要知识。随后才有理由探索不依赖完整成功示范、且监督成本可承受的方法。",
      "falsifier": "现有 Trust、H-OPD 或适用的其他强基线已充分利用这些信息；或者所谓互补信息无法可靠辨别、不能拼成有效解答，增益只能来自额外 RL 探索或更强 teacher。"
    },
    {
      "lens_id": "L2",
      "dedup_key": "g17_joint_state_accessibility",
      "name": "联合能力需要的状态能否到达",
      "question": "把提问从“当前位置该向谁学习”改为“student 是否会走到能学到另一项专长的位置”。隐含假设是：student 自采样足以暴露联合使用所需的学习机会。",
      "structure": "【待验证假设】某位 teacher 的独特价值，只有另一项能力先得到正确执行后才显现；早期 student 很少到达这些状态，导致互补监督长期不可见。关键对象是学习过程中的状态可达性，而不是任务由几步组成。",
      "prior_boundary": "Trust 和 H-OPD 已在同一 student prefix 上动态分配监督，不能说它们忽略生成阶段。现有材料尚未证明，联合状态访问不足是否构成独立于监督质量和容量的瓶颈；TU-OPD 的可解题覆盖也不能回答这一问题。",
      "method_opportunity_condition": "必须发现联合状态的缺失确实限制能力整合，并与局部反馈错误、训练量不足及容量不足区分开；改变这种限制带来的收益应超过普通增加数据或训练量，且不依赖昂贵的逐状态 probe 或分叉 rollout。",
      "falsifier": "普通 on-policy 训练已充分访问关键状态；或者补足状态后仍无联合能力收益，失败主要来自错误监督、能力本身未学会或 student 容量。"
    },
    {
      "lens_id": "L3",
      "dedup_key": "g17_local_supervision_versus_trajectory_dependencies",
      "name": "局部好信号能否形成完整策略",
      "question": "把提问从“每个 token 的监督是否可信”改为“这些可信信号合在一起，是否保留成功所需的跨步骤依赖”。隐含假设是：局部监督质量足以代表整条策略的可执行性。",
      "structure": "【待验证假设】互补价值存在于多个决定之间的关系：前面的选择决定后续哪些专长仍然可用，单独看都合理的选择不一定共同完成目标。这里讨论成功依赖是否保留；逐 token 聚合当然仍可定义合法的自回归分布。",
      "prior_boundary": "Trust 的 response-level 对照已有位置变化的收益证据，但不能据此推断所有长程依赖都已解决。TU-OPD、AVSD 已保护独有 residual，SMOPD 已使用 arithmetic mixture；因此，“避免平均冲淡独有模式”本身不足以构成新问题。",
      "method_opportunity_condition": "必须发现一种可复现的关系性损失：单项能力、局部监督可靠性和关键状态覆盖均足够，联合成功仍因跨步骤依赖未保留而受限。方法贡献需要解释并改善这种损失，而不只是更换已有聚合形式或再加权。",
      "falsifier": "控制单项能力和监督质量后，联合成功随局部改进自然提升；或者现有聚合与 residual 方法已保留所需依赖，剩余差距可由容量和优化解释。"
    },
    {
      "lens_id": "L4",
      "dedup_key": "g17_semantic_interoperability_of_specialized_skills",
      "name": "专长能否接受彼此的中间结果",
      "question": "把提问从“student 有没有学到两项能力”改为“学到的一项能力，能否消费另一项能力产生的有效中间结果”。隐含假设是：分别可用的能力天然具有兼容的使用条件。",
      "structure": "【待验证假设】A 的有效输出进入 B 的处理范围后，B 的专长不再可靠；问题可能来自中间表示、默认前提或推理约定的不一致。同源、同 tokenizer 的 teachers 也可能出现，因此不把问题归结为 G16 的模型来源或接口差异。",
      "prior_boundary": "H-OPD 已通过 description 桥接 VL/text 信息，MAD-OPD 已让 teachers 读取共同历史；信息桥接及跨 teacher 交互均已有覆盖。仍需证实的是：各项能力已经学会后，语义上有效的中间结果是否仍不能被另一项能力稳定使用。",
      "method_opportunity_condition": "必须发现可替换的正确中间结果会系统性破坏后续专长，而且这一现象确实阻碍同一 student 联合使用能力。若存在方法空间，应体现可复用能力之间的兼容原则，而非为每种任务增加一个专用转换模块。",
      "falsifier": "控制中间结果正确性后，后续能力对来源和表述已经稳健；或者简单格式统一、普通 prompt 清理就消除了主要差距，无须新的能力整合机制。"
    },
    {
      "lens_id": "L5",
      "dedup_key": "g17_train_time_interaction_deployable_compression",
      "name": "训练时的协作能否被独立复现",
      "question": "把提问从“teachers 协作后给出的监督更好吗”改为“协作带来的增量，有多少能变成 student 独立执行的能力”。隐含假设是：更强的训练期协作结果，会自然变成更强的部署期单模型行为。",
      "structure": "【高风险假设】互补性来自往返作用：一方的信息改变另一方的判断，后者又促使前者修正；有用知识存在于这种相互作用，而非某位 teacher 原先的固定答案。研究对象是协作增量的可压缩性。",
      "prior_boundary": "MAD-OPD §4 已让 teachers debate、让 student 在看不到 debate 的情况下学习最终监督，因此“用交互 teachers 教单 student”不是空白。AVSD 的 privileged views、H-OPD 的 description 也说明训练与部署的信息条件需要明确区分。",
      "method_opportunity_condition": "必须发现在部署输入足以支持任务、容量和计算均有合理对照时，确有一部分有价值的协作增量不能被现有蒸馏稳定吸收；并找到这种差距的具体原因。潜在方法还必须在包含 K×R 调用和 context 成本后仍有价值。",
      "falsifier": "现有 MAD-OPD 或其他适用基线已能按成本有效复现协作收益；或者差距主要来自 student 部署时根本没有的信息、更大的总推理预算，或容量不足，而非整合机制。"
    },
    {
      "lens_id": "L6",
      "dedup_key": "g17_reusable_composition_versus_seen_combination_fit",
      "name": "学到的是组合规则还是组合样例",
      "question": "把提问从“训练过的联合任务是否做得更好”改为“已学专长能否在新的关系中继续联合使用”。隐含假设是：在若干混合任务上成功，就代表获得了可复用的组合能力。",
      "structure": "【待验证假设】各项能力都已见过，但它们之间的依赖关系、使用条件或排列发生变化；需要迁移的是能力间的关系，而不是增加一种未学过的能力。这是泛化对象的选择，不是另列一组组合任务名称。",
      "prior_boundary": "Trust 的 MultiCap 已包含 math+IF、code+IF、math+code，不能声称没有联合训练；但汇总 recovery 不是同题端到端组合率。六篇材料也不足以断言已有方法不能关系泛化，缺少专门 benchmark 只能构成证据缺口。",
      "method_opportunity_condition": "必须先发现稳定、重要的组合泛化差距，排除单项能力下降、难度变化和数据量不足；进一步证明仅扩充组合样例的成本或效果存在实质限制，才支持寻找让专长更可复用的方法。",
      "falsifier": "现有 MOPD 在公平的关系变化下已能泛化；或者差距随常规数据覆盖或更强初始化自然消失，不能支持独立的方法必要性。"
    }
  ],
  "cross_cutting_controls": [
    "六个视角分别追问监督充分性、学习机会、跨步骤依赖、能力兼容、协作压缩和关系泛化；它们可以共同解释一个现象，但不能把同一现象重复计作六个已成立瓶颈。",
    "明确区分作者报告、现有本地综合与待验证假设。当前证据没有证明普遍组合失败，也没有证明任一新方法必不可少。",
    "评价同一个部署 student 的整题联合成功，同时报告单项能力与可解样本覆盖；不能用逐域平均、oracle union 或 benchmark-wise envelope 替代联合使用证据。",
    "容量不足、初始化、优化、一般数据覆盖、监督错误和额外信息优势均是竞争解释；不能预设任何一项就是根因。",
    "保留与具体结构匹配的强已有方法，并将多 teacher 的贡献与更强单 teacher、额外在线 RL、额外数据和更大训练预算区分。",
    "总成本包含 teacher 制备、验证、description 或 debate、teacher/reference scoring、student rollout 与更新；不默认逐状态 probe、环境重置或分叉 rollout。",
    "方法机会需要一个可解释、可规模化的核心机制；新增 gate、模块或复杂流程不能替代对限制原因的证据。",
    "更强基础模型若能低成本消除现象，应重新判断研究价值；规模变化必须用于检验机制边界，不能只报告某个小模型的差距。"
  ],
  "scope_note": "本次遵循 idea-creator-from-gap 覆盖规则，跳过 Phase 0、1，仅生成 Phase 2 的 analytic lenses。输入为 G17、synthesis/mopd-gap-analysis.md 第1节与③G17节、指定六篇 paper pages，以及主协作者提供的版本一致 HTML 定点核查边界。未展开其他 gap、旧 ideas 或 query_pack；未检索、写文件或运行训练。未生成具体方法候选，未进行新颖性裁决或 pilot。六个 lenses 未排序、未淘汰，均为同 family 探索的 provisional 结果，须待用户确认后才能进入方法候选生成。"
}
