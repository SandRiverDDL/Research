---
type: idea
node_id: idea:opd-20260822-c06-state-alias-transition
title: "Transition-Identifiable OPD under State Aliasing"
stage: archived
outcome: pending
added: 2026-08-21T16:36:05Z
based_on: []
target_gaps: []
tags: ["opd", "agentic-opd", "state-aliasing", "archived"]
---

# Transition-Identifiable OPD under State Aliasing

**stage:** `archived`  ·  **outcome:** `pending`

相同 observation 对应不同 latent state 时，以可区分转移的最小历史做监督。

## Thesis
把 textual prefix 当 state 会把不同 latent transitions 混入同一 teacher context。

## Key risks
可能只是 belief state、memory 或 state matching；若加长 context 即解决则停止。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

