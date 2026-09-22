---
title: "H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache"
description: "Speculative decoding losslessly accelerates large language model inference by having a lightweight draft model predict future tokens for verification by the target model."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.24197) · [PDF](https://arxiv.org/pdf/2609.24197)

## 一句话摘要

Speculative decoding losslessly accelerates large language model inference by having a lightweight draft model predict future tokens for verification by the target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding losslessly accelerates large language model inference by having a lightweight draft model predict future tokens for verification by the target model. Recent block diffusion drafters further reduce drafting latency by predicting multiple tokens in parallel. However, existing block drafters project target hidden states at every input position into a separate drafter-side KV cache, incurring per-request memory and KV-write overhead that grow with concurrency; directly reusing target KVs in place removes this cache but fails to sustain draft quality throughout the block. We propose a hybrid target-context injection method that complements direct target KV reuse with target hidden states only at the last input position, requiring no separate drafter-side KV cache. Building on this design, we propose H-Spec, a hybrid Mamba-attention parallel drafter that consumes the two target-context sources through complementary modules. Mamba modules are initialized with projected last-token target hidden states, while attention modules reuse target KVs in place. Despite its recurrent formulation, Mamba's parallel scan allows H-Spec to preserve block-parallel drafting. Across three target models and diverse tasks, H-Spec improves over the best baseline by 5.0--13.3% in mean accepted length and 5.3--12.6% in batch-size-1 inter-token latency speedup. Under concurrent serving, H-Spec consistently achieves higher throughput while maintaining lower KV cache utilization than baselines across evaluated concurrency levels.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Weifan Jiang, Krishna Teja Chitty-Venkata, Megan Flynn, Reed Meyerson, Zhenting Qi, Tianyu Wu, Eldar Kurtic, Minlan Yu, Alexandre Marques
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
