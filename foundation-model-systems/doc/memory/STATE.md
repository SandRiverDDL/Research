# Foundation Model Systems — Current State

> Codex hot memory。只保留 compact / 新 task 后继续工作必需的信息；稳定规则见 `AGENTS.md`，历史理由见 `DECISIONS.md`。

Last updated: 2026-10-22

## 2026-10-23 独立 chat：RL 中 MTP 冻结与训练的文献调研

- 用户要求：调研 RL 中 MTP 应冻结还是训练，覆盖领域经典、重点方法和近期顶会录用研究；沿用本 chat 已明确纳入 EAGLE 类草稿模块、在线适配和 RL rollout 加速的范围。
- 交付方式：聊天内文献矩阵与跨论文判断；不自动创建 dossier、导入 Zotero、运行训练或生成实验方案。下方其他 chat 的任务与历史时间限制不适用于本次调研。
- 已核实的关键区分：冻结 MTP 参数、训练头但截断 MTP→backbone 梯度、MTP 辅助损失反传 backbone、RL 后冻结 backbone 做 healing/boosting，是不同设置。
- 核心原文：FastGRPO（ICLR 2026）；MTP-RL（ACL 2026 Findings，Eq.5 允许辅助损失影响主模型）；OCC（EMNLP 2026 Findings，本地日程记录；数学 RL）；Bebop 2606.12370（预 RL e2e TV + rejection sampling 后冻结头）；GrowMTP 2609.16648（RL 内从零训头、detach）；NVIDIA co-training 2609.07108（detach，扩至122B）；ReSpec（MLSys 2026，周期性 reward-weighted KD）。Bebop、GrowMTP、NVIDIA co-training 本轮仅确认 arXiv/technical report；索引未命中不代表拒稿。
- 补充反证：2604.26779 §3.3/Table 5 中良好 DAPO 初始化的 EAGLE-3 offline/online speedup 1.77/1.78，弱初始化1.51/1.63；不能统一声称在线训练必需。无训练替代：EfficientRollout（NeurIPS 2026）、DAS（MLSys 2026）、BubbleSpec（ICML 2026）。
- 当前进度：调研完成，聊天内交付训练模式矩阵、经典基础、核心七篇及冻结反证、Nemotron healing/boosting 阶段区别和近期录用对照。核心论文已定点读方法与消融，会议记录来自本地2026-10-16快照及官方 proceedings（补MLS​​ys）；未做复现，非穷尽系统综述。Composer-2/GLM-5 本次打开的原文未独立确认 RL 中 MTP detach 细节，不沿用 OCC 相关工作里的二手断言。

## Current Goal

核查 MAI-Thinking-1 TR 首次公开时间及微软 MAI-2 / MAI-Base-2 的公开训练进展；聊天内回答。

## Confirmed Task Contract

- 2026-10-22 用户评价 MAI-Thinking-1“没什么意思，不够 frontier 又不够开源”；本轮询问报告日期、微软是否正在训练 MAI 2。不据此自动删除 dossier 或改写既有优先级清单。

- 2026-10-19 follow-up：用户询问上述循环是否有 TR 提及；区分 RL→在 midtrained checkpoint 上做 SFT→RL，与轨迹直接混入 midtraining corpus。不新增 dossier / comparison 或 Zotero 入库。

- 2026-10-19 用户补充：需要 TR；来源必须为大厂、基模组或至少合作。新增问题是如何判断 agent 轨迹正确／高质量。沿用近半年优先与禁止 2024/2025 的限制。前轮纯学术候选不再进入本轮主推荐；Apple PROOF-Gen 属工业来源。

- 2026-10-19 用户纠正时间范围：“最好是这半年内的，且禁止24 25论文和tr”。本轮优先 2026-04-19 至 2026-10-19，一律排除 2024/2025 论文/TR，不能把旧文新修订当新论文。

- 2026-10-19 当前请求：找上述三类具体做法；区分 teacher 明确披露与未公开，benchmark 分布对齐与 test contamination。不自动新增 dossier、下载或 Zotero 入库。

- 2026-10-19 follow-up：用户核查推荐论文是否来自大厂 / frontier lab，并提到 Qwen AgentWorld；需明确区分 Qwen-AgentWorld（Qwen，2606.24597）、Agent-World（人大 + ByteDance Seed，2604.18292）与 AWM（Snowflake 合作，2602.10090），不据此扩展 dossier 清单。

- 2026-10-19 follow-up：用户问 env scaling 有哪些公开较清楚的论文 / TR，认为 LongCat TR 太早；优先较新原始材料，区分 environment diversity、task instances 与并发副本。

- 2026-10-19 follow-up：用户要四类行为的具体例子、TR code training datasets 披露，以及可用于训练的开源 code/terminal tasks；关心避免在 benchmark test set 上训练。

- 2026-10-19 follow-up：用户要求概括 2610.00890 主要内容，确认其训练数据集是否开源；未要求下载或 Zotero 入库。

- 2026-10-19 follow-up：用户质疑 Kimi 已充分后训练，为何 2610.00890 仅 LoRA 仍能大幅涨分；本轮做论文证据审计与机制解释，不新建 dossier / comparison。

- 2026-10-19 follow-up：用户追问 Qwen3-Coder-Next 如何训练、SWE 为何单列 expert、是否按题型划分；同时要求核查 Kimi K2.7 Code 是否有 TR。

- 2026-10-19 用户要求：“目前这些tr里，对code能力，或者code专家模型是怎么训练的”，按时间降序，新出的在上面。

- 2026-10-07 OLMo 3 后续重点：pretraining 数据处理、pretraining/midtraining mixture 的实验选择、LR/batch/schedule/epoch，以及超参选择证据边界；增补现有 pretraining-data note。

- 2026-10-07 用户要求总结 OLMo 3 主要内容：先确认已有 notes，重点解释完整训练流程、架构设计及其对既有成熟设计的继承；复用现有 sources/olmo-3/，不新建 source。

- 2026-10-07 用户纠正近期 TR 推荐标准：关注 frontier model systems；Instella-MoE 不纳入本轮常规 follow / 总结清单。OLMo 3 与 Qwen 小模型的能力比较仍是问答，不代表授权新增 dossier 或总结。

- 用户确认的第二优先级只有：Qwen3.5 → Qwen3.6 / Qwen3.7、MiniMax M3、Kimi K2.7 Code、OLMo 3.1。
- Open-R1 与 Skywork-OR1 是 assistant 从旧候选列表误扩展的额外资料，不属于上述第二优先级，也不得计入指定交付。
- Lens、comparison、跨模型 summary 只有用户明确要求时才生成；补 dossier、stage note 或 release delta 不自动授权综合产物。
- 2026-07-29 用户明确要求：进入 foundation-model-systems，为最近的 Kimi K3 建立 dossier；该 source 很重要，并重点核验其是否为“断档第一”的开源模型能力。
- 2026-07-31 用户明确要求：查基模后训练 dossiers 的 OPD 具体 recipe，判断 sampled-token OPD 是否适合 A3B MoE，并整理训练失败坑点与设计方案。
- `comparison/post-training-priority-expansion-2026-07.md` 是未经明确授权生成的额外产物，不是 authoritative deliverable；保留或删除等待用户决定。
- 无法从状态文件确认的优先级或模型清单不得推断；应回看用户原话，仍不明确时再询问。

## Completed

- 2026-10-22 MAI freshness 核验：MAI-Thinking-1 首次公告/TR 为 2026-06-02（PDF citation + family announcement），8/12 是 public preview 更新。微软 10/15《Frontier Pre-training at Microsoft AI》已确认 MAI-Base-2（2.8T total /80B active）预训练完成、正在后训练，MAI-Base-3 preparations underway；不能据此确认最终后训练产品叫 MAI-Thinking-2 或已达到最强 frontier。官方路径：https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/ 。

- 2026-10-19 循环训练原文核验：MAI-Thinking-1 §3.1.4 pp34–36 明确 RL rollouts→midtrained checkpoint SFT→继续 RL，最终只用 successful traces，self-distillation 时混入 midtraining data；不等同于轨迹回灌原 midtraining。ReMiT（上交+腾讯优图，2602.03075，2/3，超出近半年，仅机制补充）§3/§5.2 验证两轮 RL-guided midtraining，传递 token loss weights，非成功轨迹回灌。

- 2026-10-19 工业来源补核完成：Fara-1.5 TR 2606.20785（v1 6/18；GPT-5.4 solver→correctness/process≥.8、efficiency≥4、critical-point adherence 三门）；MiniMax-M2 TR 2605.26494（5/26，§4.1.2 AaaV execution/interaction/visual，§4.1.3 query evolution）；Nemotron 3 Ultra（6月，p17 SWE trajectory heuristic analyzer）；MAI-Thinking-1（6月，§3.3.1 tests+LLM monitor+human flagged review，anti-hacking）；Qwen《The Verification Horizon》2606.26300（v1 6/24，§3 interactive judge、§5 evaluator filtering vs ranking及RFT实验）。Microsoft+Browserbase Universal Verifier 2604.06240 首发4/5，超出近半年14天，只列显式补充，不用4/21博客日期冒充论文首发。仅核查原文，未训练/新增 dossier。

- 2026-10-19 近半年 data synthesis / closed-teacher distillation shortlist 核验完成：WebKD 2610.19834（10/14，GPT-5.5 编辑 student failures）、Apple PROOF-Gen 2608.23911（8/24，GPT-4o executor + GPT-5.1/5.4 reflector，task-level 非 template-level holdout）、DOMINO 2605.30039（5/28，soft-prompt 学 reference 分布，时间划分 reference/test）、AcquisitionSynthesis 2605.13149（5/13，acquisition rewards 训练 generator）、Programming with Data 2604.24819（4/27，知识结构定位 failure 后补数据）。原始 HTML 方法页段核验，未运行训练、下载、入库或新增 dossier。2024/2025 候选已撤出。

- 2026-10-19 代码开放补核：SETA 有 datasynth/runtime/RL 示例；AWM 有 synthesis + 1K环境/任务/数据库/verification；Agent-World 发布563/1,978环境及task synthesis、SFT数据/说明，不能称完整论文训练复现；Qwen-AgentWorld 当前29文件主要eval/prompts，公开35B权重+benchmark，未见CPT/SFT/RL完整pipeline；AutoEnvScaling 有实质代码但README仍自标private preview；Envs-FORGE所指DataArc仓库未定位论文专属pipeline，不能确认完整实现；Kimi K3/MiniMax模型发布仓库未发现对应环境生成训练代码。本轮未运行代码。

- 2026-10-19 env-scaling 检索核验完成：AutoEnvScaling 2610.14163（10/9，proposer→验证/难度校准→solver 闭环；仓库仍自标 private preview）、Envs-FORGE 2608.14312（8/14，固定100个合格环境的小规模对照）、SETA 2607.10891（7月论文、1月早期博客；4,500+ task/environment bundles，代码/数据入口）、Agent-World 2604.18292（4/20，1,978个数据库+工具集环境及数量曲线）。工业 TR 对照为 Kimi K3 §4.2 与 MiniMax-M2 §4.1.3。仅原文/仓库页面核验，未运行或新增 dossier。

- 2026-10-19 code/terminal training sources 补核：Qwen seed datasets 与 Nemotron SWE/terminal provenance 已回填原 notes；Surge 四类原文案例已回填 K2.7 note。公开训练资源核验 R2E-Gym-Subset、SWE-Gym、SWE-smith、OpenThoughts-Agent-v1-RL、Endless Terminals、SETA；NVIDIA Terminal Pivot 是 next-action records，非完整31K环境。原 SWE-bench 有 train split，但 Verified 是 test 子集，HF split 名不能替代用途核查。

- 2026-10-19 数据开放核查：2610.00890 的1,700 coding tasks 未发现公开下载/开源许可；作者明确指向 Surge 商业 catalog（surgehq.ai/ots）与团队申请，不能当作开放可复现 dataset。证据补入 K2.7 Code release note。

- 2026-10-19 Surge RL audit 完成：headline +20pp 是 SWE-Marathon 1/20→5/20，单项 p=.089；SWE-Pro +4.7pp p=.059；排除 public baselines 后 pooled p=.02。LoRA 应用于 attention/MLP，64 H200，配置约1.4万 trajectories。near-miss 解释与数据/奖励因果证据、general-capability tradeoff 未验证已区分，详见 K2.7 release note reviewer audit。

- 2026-10-19 follow-up：Qwen 四专家为 task/workflow/feedback 混合划分，已补术语澄清；K2.7 Code 官方专属完整 TR 仍未找到，但新查到 Surge AI 2026-10-01 downstream RL paper 2610.00890，已补入 parent release delta，不能当作原始训练披露。

- 2026-10-19 code training 总结证据已核验：按 TR v1 / 官方首次披露日排序；本地 release_date 混有模型发布日/修订日，本轮排序不直接复用该字段。MAI 首次披露为 6/2，8/12 是 public-preview 更新。
- 补核细节已写回 Qwen3-Coder-Next expert-distillation、Nemotron 3 post-training、OLMo 3 post-training notes；覆盖专家分工、code/SWE rewards、anti-hacking 和 consolidation。
- 本轮 validation：sources=29 issues=16 warnings=0；16 项全部是既有四个 closed-family stubs，无本轮 notes 新增问题。
- OLMo 3 已有完整 first-pass notes；2026-10-07 补 architecture、pretraining 数据/mixture/超参、Instruct warm-start、Delta Learning DPO 与 OlmoRL。Olmix 的 proxy-to-target transfer 证据与局限已补入 pretraining-data.md。
- Kimi K3 已建立 S-priority dossier。2026-07-29 的 capability 定位属于历史判断，不代表当前排名；含 source bundle、section index 与 stage notes。
- 已核对 DeepSeek-V4 full-vocab OPD、MiMo/Nemotron-Cascade 2/Kimi K3 sampled-token MOPD、Qwen3 student-on-policy logit distillation。
- Qwen3.5 已有 stage notes；Qwen3.6、MiniMax M3、Kimi K2.7 Code、OLMo 3.1 已补 release delta；Qwen3.7 仅官方 API metadata。
- DeepSeek-R1、Ling/Ring 2.6、Open-Reasoner-Zero 已有 dossier；Open-R1 与 Skywork-OR1 只算额外资料，不属于之前确认的第二优先级交付。

## Next Action

MAI 日期和第二代训练状态已核查，聊天内交付；未授权新建 MAI-Base-2 dossier 或修改既有优先级清单。

## Key Paths

- `AGENTS.md`：项目 workflow 与授权边界。
- `doc/memory/DECISIONS.md`：稳定决策及理由。
- `_meta/generated/status.md`：完整 source 状态；不要复制到本文件。
- `sources/<source-id>/`：source dossier 与 evidence anchors。
- `sources/kimi-k3/`：Kimi K3 dossier；默认从 `README.md` 与 `notes/claims-and-gaps.md` 进入。

## Relevant Decisions

- `2026-07-21: Keep project memory minimal; no compact hook`
- `2026-07-21: Synthesis artifacts require explicit authorization`
