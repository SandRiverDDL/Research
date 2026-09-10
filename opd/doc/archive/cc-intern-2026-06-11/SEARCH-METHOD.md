# OPD Autoresearch 搜索方法学

> 2026-06-11 总结。下一轮 search 前必读。
> 这一轮跑 27→31 张 L1 卡的过程中暴露的全部教训。

## 核心流程（修正版）

### 1. 三源必须串行（不要并发）

```
arXiv（最全 superset，含 preprint + 工业 report）
  ↓ python dedup（title 归一化 + arxiv_id 匹配）
OpenReview enrich（顶会接收版 + reviews + 评分）
  ↓
Semantic Scholar enrich（citation graph 反向爬）
```

**为什么不并发**：顶会论文 99% 都挂 arXiv，OpenReview 主要补"接收状态 + review 分数"，S2 补"被引 / citation graph"。并发会让同一篇 paper 走两路 disambiguate 出怪 slug（实测 `zhang-2025-aligndistil-aligndistil` 这种垃圾名）。

**arXiv 优先理由**：
- preprint 比顶会接收快几个月
- 工业 tech report（NV / Google / Meta）只挂 arXiv 不投会
- API 稳定 / 无 rate limit / 全文可下载

OpenReview 只用于：(1) 验证某篇 ICLR/NeurIPS/ICML 是否接收，(2) 抓 review 分数加 confidence。S2 只用于：(1) 反向爬已确认 S 类论文的 citation graph 找漏，(2) 验证作者机构。

### 2. Domain filter 必加

```python
arxiv_search(
    query="\"online policy distillation\"",
    categories=["cs.CL", "cs.LG", "cs.AI"],   # ← 必填
)
```

不加的代价（这一轮亲历）：
- "policy distillation" 撞 cs.RO 机器人 paper
- 撞 eess.SY 控制论 paper
- 撞 nuScenes 自动驾驶 paper（`26_rl-policy-distill.md` 误进）

LLM topic 默认三个 category：`cs.CL / cs.LG / cs.AI`。RLHF 类加 `stat.ML`。Vision 类加 `cs.CV`。

### 3. 综述 seed 必须爬 reference 全表

**错误做法**（这一轮做的）：取综述 must-read top-25 当 seed → 漏 OPSD（被 6+ 卡片引用的祖先）。

**正确做法**：
1. 综述 reference list 全爬（不挑），50-200 篇
2. 综述 must-read top-N **加 priority 1 标签**（高优先写卡）
3. 其他 reference 走标准 4-class triage
4. 综述明确点名"key prior work / foundational"的特别标记

**why**：综述作者主观选 top-N 时口味会偏，关键 baseline（如 OPSD 这种"大家都在引但综述没特别强调"的）会漏。

### 4. 综述 seed 不进 L1

**错误做法**（这一轮做的）：把 DeepSeek-R1（综述 must-read seed）灌进 L1 写卡片。

**问题**：DeepSeek-R1 是 RL 训练 recipe + offline SFT 蒸馏，不是 OPD 方法 paper。综述把它列为 must-read 是因为"理解 RL distillation 必读"，不是"OPD 方法 representative"。

**正确做法**：综述 must-read seed 单独路径
- topic-match 强的 → 标准 triage
- topic-match 弱的 backbone reading → 标 `scope: background-reading` 或单独目录 `_meta/background/`
- 不进对比表，不污染 grep

## Triage 4-class 实战修正

| Class | 原定义 | 实战补丁 |
|---|---|---|
| **S** | T1/T2 大厂 first_author | OK，但**清华 / 北大 / Stanford / MIT** 应升 S（Qwen / DeepSeek / Kimi 同理）。原 confidence=3 但实际质量等同 S |
| **A** | 接受版 + 开源 OR 高引 | 加一条：**citation 不可达**时（太新/preprint），看 GitHub stars > 100 也算 A |
| **B** | 当年 arxiv + 主题 match | OK |
| **C** | 其他 | 加一条：**自动驾驶 / 机器人 / 信号处理 domain mismatch** 直接 C，不进 B |

method 类不开源 code 默认降级——除非 citation > 100 视为高影响力 arxiv 保留 A。

## Cross-check 必做项

每轮 phase 3 写完 L1 后，phase 4 必须 sonnet think hard 跑一遍，扫：

1. **scope 误进** — 自动驾驶 / 机器人 / 综述 seed 灌入 / topic 不符
2. **lang 失衡** — TL;DR 或 Core Idea 大段英文（应中文为主）
3. **decisions suspicious** — 正文方法写清楚但 decisions 字段全 unknown（sonnet 偷懒）
4. **跨卡片 mention 但本体无卡** — 如 "vs OPSD" 但没 26_opsd.md → 漏 candidate
5. **可疑数字** — 明显高于综述报告的 baseline
6. **跨卡片矛盾** — "X > Y" vs "Y > X"

输出 `_review-checklist.md`，chy 决定补哪些 / 移哪些。

## 单卡 token 预算

| 情况 | 预算 | 措施 |
|---|---|---|
| 全新 paper 写 L1（必读 PDF） | 25-30k | Read offset/limit 限 §1+§3+§4，不读全文（节省 50%） |
| 修字段 / 改 frontmatter | 5-8k | 只 Read 卡片 body，不读 PDF |
| Cross-check 单张卡 | 3-5k | sonnet think hard，纯判断 |
| 综述 reference 抽 | 30-50k | 分两步抄 + 校验，避免 last-name 复用 |

公司代理 burst 限流：**>15 并发触发 400**，10 并发实测稳定。

## 命名 / dedup 权威值

- slug：`<year2>_<method-shortname>.md`（kebab-case）
  - ✓ `26_lightning-opd.md` / `24_minillm.md` / `25_distillm-2.md`
  - ✗ `agarwal-2024-online-distill.md`（旧 author-year）
  - ✗ `OnlineDistillation_2024.md`（CamelCase）
- 撞名加 `-v2`（`26_taid-v2.md`）
- dedup key：`firstauthor + 标题归一化（lowercase + 去标点 + 去 stopword）`，**不靠 arxiv_id**（接受版常没）

## 这一轮的具体漏点

下一轮 search 前自查清单：

- [ ] 综述 reference 全表爬完了？（不只 must-read top-N）
- [ ] domain filter 加了 cs.CL/cs.LG/cs.AI？
- [ ] arXiv 三源串行，不并发？
- [ ] 综述 must-read seed 单独路径，不灌 L1？
- [ ] OPSD-like 祖先 paper 是否在 27+ 卡里都有 cross-ref 但本体无卡？grep 一遍 `vs OPSD` `vs SDFT` `vs <baseline-name>` 找漏
- [ ] 高频 cross-ref 的"vs X"全部建本体卡？

## 已知漏的卡（待补）

每轮发现的"漏 candidate"在这里登记，避免下轮再漏。

- ✅ OPSD (2601.18734) — 已补 `26_opsd.md`
- ✅ Lightning OPD (2604.13010) — 已补 `26_lightning-opd.md`（NV affiliation 确认）
- ✅ REOPOLD (2603.11137) — 已补 `26_reopold.md`
- ✅ EOPD (2603.07079) — 已补 `26_eopd.md`
- ⏳ "Revisiting OPD" — 用户记忆中有，cross-check 没找到含 "Revisiting" 的 OPD paper。最接近 REOPOLD（"Relaxed"）。**待 chy 确认是否记错**

## 覆盖 gap（下一轮重点）

cross-check Phase 3 发现的覆盖空白：

| 轴 | 当前 | 缺什么 |
|---|---|---|
| signal | logit 15 篇过载 | preference / PRM step-level 几乎空白 |
| rollout | student-only 12 篇 / mixed 4 / offline 2 | EMA teacher / self-evolving teacher 0 篇 |
| iteration | 分布均匀 | — |
| filter | none / verifier-pass 各 7、2 | hardness/curriculum 仅 2-4，trajectory-level 仅 1 |

下轮 search query 应针对性加：
- `"preference distillation"` `"DPO distillation"` `"step-level reward distillation"`
- `"EMA teacher distillation"` `"self-evolving teacher"`
- `"curriculum distillation"` `"hard example mining distillation"`
