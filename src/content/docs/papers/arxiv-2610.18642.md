---
title: "MultiAlloc: Budget-Aware Precision Allocation for KV Cache Quantization"
description: "The Key-Value (KV) cache constitutes a dominant source of memory consumption during large language model (LLM) inference, particularly in long-context and complex reasoning scenarios."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.18642v1) · [PDF](https://arxiv.org/pdf/2610.18642v1)

## 一句话摘要

The Key-Value (KV) cache constitutes a dominant source of memory consumption during large language model (LLM) inference, particularly in long-context and complex reasoning scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Key-Value (KV) cache constitutes a dominant source of memory consumption during large language model (LLM) inference, particularly in long-context and complex reasoning scenarios. Existing KV cache quantization methods have explored different compression granularities, including layer-wise precision adjustment and token-level information preservation. In practical deployment, however, the key challenge is not merely compression, but how to allocate limited quantization resources among heterogeneous precision preservation strategies under a fixed KV cache memory budget. We propose MultiAlloc, a profiling-guided precision allocation framework for KV cache quantization that adaptively distributes limited quantization resources between layer-wise precision enhancement and token-wise preservation. MultiAlloc employs lightweight offline profiling to characterize layer sensitivity and token importance, enabling adaptive precision allocation under a fixed memory constraint. Guided by the profiled memory--accuracy trade-off, it automatically derives an effective precision allocation strategy without online allocation search, and applies the resulting policy during inference. Extensive experiments on reasoning and long-context benchmarks demonstrate that MultiAlloc consistently improves over layer-wise, token-wise, and recent multi-granularity KV cache quantization methods under matched memory budgets across diverse models, including Mistral, Llama, DeepSeek-Qwen, and QwQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yangchengyu Zhou, Zhiping Wu, Runchang Jiang, Dongdong Ren, Youfang Han, Wei Zhao, Dongqi Cai, Wenbin Li
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/RL-MIND/MultiAlloc](https://github.com/RL-MIND/MultiAlloc)
- 阅读深度：metadata
