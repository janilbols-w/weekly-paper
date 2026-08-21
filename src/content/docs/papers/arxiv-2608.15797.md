---
title: "KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving"
description: "KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2608.15797v1) · [PDF](https://arxiv.org/pdf/2608.15797v1)

## 一句话摘要

KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history. Under aggressive budgets, this not only lowers accuracy but can also cause runaway degeneration, where the model produces incoherent or repetitive tokens until reaching the length limit. We characterize much of this loss as an information gapf caused by missing context, rather than a capability gap caused by limited model capacity. An evicted 7B model and a full-context 1.5B model make complementary errors, and an oracle choice between their answers recovers 79% of the accuracy gap to the full-KV 7B model. Based on this observation, we propose KV-Rescue, a training-free inference framework that bridges the information gap introduced by KV eviction using a lightweight full-context helper. KV-Rescue interleaves reasoning steps from the two models into a shared trajectory. An online detector uses entropy and compressibility to terminate the generation of incoherent or repetitive base-model candidates early. Across five math benchmarks with Qwen2.5-Math 7B and 72B, KV-Rescue recovers an average of 87% of the accuracy lost to eviction at eviction budget B=64. A decode-cost analysis further shows that preventing runaway degeneration cuts base-model token generation by 43% on average.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minsoo Cheong, Woosang Lim, Vincent-Daniel Yun, Sungjoo Yoo
- 发布：2026-08-16；更新：2026-08-16
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
