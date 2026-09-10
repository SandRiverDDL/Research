# Kimi K3 Agentic Data and Environments

```yaml
---
source_id: kimi-k3
section_type: stage-note
stage: tool-agent-training
depth: working
confidence: high
need_expert_review: false
---
```

## Core Design / Innovation

- K3 不把 agentic RL environment 固定成单个 harness，而把 tool schema、system prompt、context management、skills、memory、subagents 等做成 composable white-box modules，并在训练时动态组合。[14-15]
- task discovery 通过 self-evolving hierarchical knowledge graph 控制 domain granularity 与 coverage，再检索公开材料、按 task type 合成 instances。[15]
- reward 设计尽量落到 executable/verifiable final state：kernel correctness+performance、AET hidden verifier、web build/tests、professional workflow criteria；model judge 只在难以完全 deterministic 的部分补充。[16]
- persistent personal-assistant worlds 将 trajectory 拉到多 simulated days、thousands of tool calls、millions of context tokens，迫使 training infra 保留 environment state，而不是把每轮交互 reset 成独立 episode。[16]

## Why It Matters

这是 K3 dossier 对 agent training 最有价值的部分。它把“更强 agent”具体化为四个可操作方向：scaffold diversity、coverage-controlled task synthesis、verifier-grounded environment、persistent state。模型规模是能力底座，但长轨迹泛化来自 environment distribution 和 verification loop。

## Mechanism Sketch

1. 将 Kimi Code / Claude Code / Codex / OpenClaw / Hermes 等 harness 抽象为模块组合。
2. 按 task group 动态采样不同 tool/prompt/context/skill/memory/subagent configuration。
3. 用 hierarchical KG 选择 coarse/fine concepts，检索真实公开材料，合成 knowledge/coding/vision tasks。
4. 在 sandbox 中 rollout；用 deterministic verifier、hidden tests、performance roofline 或 rubric judge 评分。
5. reward-hacking pattern 进入 safeguard / hidden verifier 的持续更新。

## Environment Families

### Verifiable Search / Professional Work / Visual Reasoning

- search task 要求逐步收集 web evidence 并产出可核验答案；professional work 覆盖 investment banking、data analysis、legal deliverables。[15-16]
- visual reasoning 在隔离 Python sandbox 中迭代 crop/zoom/transform/compute，并把 generated images 作为新 observation 回到 trajectory。[16]

### Kernel Optimization

- task 从 single operator 到 fused mega-kernel，覆盖 CUDA、Triton、CuTe DSL、Gluon、ThunderKittens、TileLang 与 BF16/FP8/FP4。[16]
- numerical error 超阈值 reward=0；达到 expert implementation 得 0.5，接近 hardware roofline 向 1 提升。[16]
- 显式检测 CUDA graph replay、input caching、precision reduction 等 reward hacking，并随开发观察持续补规则。[16]

### Persistent Personal Assistant

- mock Gmail/Notion/Slack/Canvas 保留真实语义但避免 external API/rate-limit 噪声；任务跨 apps、事件与 simulated days。[16]
- 每个 event 用 deterministic rule 或 LLM evaluator；初始 workspace 由 agents 从 web reference material 自动构造。[16]

### Autonomous Execution Tasks

- task 只给 initial state、goal、tool action space、budget 与 verification interfaces，不给 reference trajectory。[16]
- agent 与 verifier 隔离；public verifier 提供 diagnostic feedback，hidden verifier 检查 held-out scenarios；submission budget 与 penalty 限制 hacking。[16]

### Web Development

- task 覆盖 website、game、3D/WebGL、visualization、SVG、full-stack；不同 scaffold rollout 防止单一 harness overfit。[16]
- deterministic checks 验证 build、behavior、structure/pixels；失败、runtime error 或 fake artifact 直接 zero reward，model judge 再做 code/output inspection。

## Gaps / Open Questions

- 没有公开每类 environment 的 sample counts、RL mixture weights、train/eval split、contamination controls、judge models 与 exact prompts。
- “动态多 harness”可能提升 scaffold robustness，也可能把 proprietary harness behavior/distilled traces带进模型；报告没有给 leave-one-harness-out test。
- knowledge graph 的 seed、stopping criterion、node quality、retrieval source policy 和 copyright/provenance handling 未公开。
- hidden verifier 只降低已知 hacking，无法证明没有 evaluator leakage；需要 held-out environment families 与 adversarial audit。

## Transfer Hooks

- `worth-internalizing`: 把 harness 作为训练分布变量，并做 leave-one-scaffold-out evaluation。
- `worth-internalizing`: final-state verifier 优先于 self-reported completion；public feedback 与 hidden final check 分离。
- `try-at-small-scale`: persistent mock SaaS world + incremental events，比一次性 static task 更直接测 memory/state discipline。
- `try-at-small-scale`: task synthesis 的 KG coverage audit，记录 coarse/fine node 分布和 repeated concept rate。

## Evidence Anchors

- 14-15: unified white-box environment, KG-guided synthesis。
- 15-16: verifiable search/professional/vision tasks。
- 16: kernel, personal assistant, AET, web development。
- 21-22: persistent rollout/sandbox system support。
