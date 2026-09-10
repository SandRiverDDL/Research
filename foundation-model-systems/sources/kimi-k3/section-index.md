# Kimi K3 Section Index

> Navigation layer for `papers/kimi-k3/kimi-k3.pdf`. Page numbers are PDF pages.

## High-Level Map

| Topic | PDF pages | Read status | Note |
|---|---:|---|---|
| Abstract / positioning | 1-2 | read | `README.md`, `notes/claims-and-gaps.md` |
| Architecture overview | 3 | read + visual check | `notes/architecture.md` |
| KDA / Gated MLA | 4-6 | read | `notes/architecture.md` |
| Attention Residuals | 6 | read | `notes/architecture.md` |
| Stable LatentMoE / SiTU-GLU / QB | 6-9 | read | `notes/architecture.md` |
| Native vision / Per-Head Muon | 9-10 | read | `notes/architecture.md` |
| Pretraining data / scaling law / recipe | 10-12 | read | `notes/pretraining.md` |
| Long-context extension | 12 | read | `notes/pretraining.md` |
| SFT / RL / reasoning effort / GRM | 12-13 | read + visual check | `notes/post-training.md` |
| MOPD / deployment-aware post-training | 13-14 | read | `notes/post-training.md` |
| RL task synthesis / environments | 14-17 | read | `notes/agentic-environments.md` |
| KDA system co-design / KCP | 17-18 | read | `notes/infra.md` |
| 3T pretraining infra / MoonEP | 18-21 | read | `notes/infra.md` |
| 1M agentic RL / AgentENV | 21-22 | read | `notes/infra.md` |
| Inference / serving | 22-25 | read | `notes/infra.md` |
| Public eval configuration/results | 25-28 | read + Table 2 visual check | `notes/eval.md` |
| Internal capability/cyber eval | 28-31 | read | `notes/eval.md` |
| Third-party eval / cost | 31-32 | read + Table 5 visual check | `notes/eval.md` |
| Case studies / conclusion | 33-34 | skimmed | lookup only |
| References | 35-40 | indexed | lookup only |
| Author contributions | 41-43 | indexed | lookup only |
| Appendices: SiTU/QB/MoonEP proofs | 44-46 | indexed | return for method-level proof |
| Appendix: XTML / reasoning effort | 46-47 | indexed | return for interface/training query |

## If You Need...

- **“K3 为什么比 K2 大幅变强？”**：先读 2、3、6-12；注意 `2.5×` 是 aggregate scaling claim。
- **KDA 的公式与 lower-bounded decay**：4-5；系统实现看 17-18、24。
- **Attention Residuals**：6；memory/pipeline implementation 看 20、24。
- **LatentMoE / QB**：6-9；MoonEP 的 execution balance 看 19-20；proof 看 44-46。
- **native vision 为什么从零训练**：9-10；joint training / long context 看 11-12。
- **post-training 全流程**：12-14；environment/data 细节看 14-16；RL infra 看 21-22。
- **reasoning effort 如何训练**：13；API/chat representation 看 46-47。
- **“断档第一”是否成立**：26-32，并同时检查 `[aa-k3]`、`[arena-text]`、`[aisi-cyber]`。
- **开源程度**：不要只读 TR；回到 `[hf-model]` 与 `[k3-license]`。

## Visual Checks Performed

- page 3: architecture figure readable; confirms 3× KDA + 1× Gated MLA blocks, AttnRes paths and vision input。
- page 10: native vision / pretraining transition checked。
- page 13: RL scaling / partial rollout section checked。
- page 27: Table 2 columns and open-weight baseline checked。
- page 32: independent eval table and cost plots checked。
