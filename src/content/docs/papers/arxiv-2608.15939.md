---
title: "Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents"
description: "Stateful language agents assume a rejected branch can be taken back by clearing it from the application transcript."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2608.15939v1) · [PDF](https://arxiv.org/pdf/2608.15939v1)

## 一句话摘要

Stateful language agents assume a rejected branch can be taken back by clearing it from the application transcript.

## 为什么值得关注

待编辑增强。

## 摘要原文

Stateful language agents assume a rejected branch can be taken back by clearing it from the application transcript. We show this breaks when the serving session retains key/value (KV) state across the logical abort: the model can continue attending to content the application believes it discarded. We formalize the missing guarantee as rollback consistency: a complete abort must restore the state the model attends, not just the transcript. The key failure is cross-layer: a correct logical rollback need not compose with retained inference state, and the gap can remain invisible to the application. To isolate cache effects from text effects, we introduce a same-token/different-cache audit that holds decision-step tokens identical while varying only whether the cached prefix is stale or rebuilt from committed state. Across seven open-weight families (3.8B-36B), retained KV alone flips a typed protected effect in 25 of 63 audited cells, while attacker tokens are absent from the served request in all 63; rebuilding the cache closes every cell. The channel reproduces in an end-to-end session application, on the default Hugging Face Transformers cache-reuse path, and under LangGraph time-travel, where verified logical rollback can still leave attended KV stale. Susceptibility varies across models, but the underlying attended-state integrity violation is structural. We rule out position and length confounds, generalize across protected effects, policy structures, and a cache-isolated Mixture-of-Experts model, and show that transaction-local cache restoration closes the channel without requiring a global cache flush. All headline results are deterministic and reproducible from released artifacts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 4 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guijia Zhang, Harry Yang
- 发布：2026-08-16；更新：2026-08-16
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
