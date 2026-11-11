---
title: "Sentinel: Decoding Context Utilization via Attention Probing for Efficient LLM Context Compression"
description: "Retrieved contexts are often long, noisy, and redundant, motivating query-aware compression before answer generation."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2505.23277) · [PDF](https://arxiv.org/pdf/2505.23277)

## 一句话摘要

Retrieved contexts are often long, noisy, and redundant, motivating query-aware compression before answer generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieved contexts are often long, noisy, and redundant, motivating query-aware compression before answer generation. Native attention provides signals for context selection, but heterogeneous head behaviors complicate their direct aggregation into sentence-utility scores. We introduce Sentinel, a sentence-level compressor that learns to combine these signals through a signed linear readout across layers and heads. Only the readout is trained using existing QA evidence annotations, while the backbone remains frozen and sentence scoring requires no autoregressive generation. Across twelve LongBench tasks, Sentinel with a 0.5B backbone outperforms Full Context on multiple tasks under a 2,000-token budget with each of three readers: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, and DeepSeek V4.1 Flash. Despite English-only QA supervision, the same readout transfers to Chinese tasks without task-specific retraining. Length-stratified profiling further shows lower compression latency and GPU memory usage than LLMLingua-2 and CPC.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yong Zhang, Heng Li, Yanwen Huang, Ning Cheng, Yang Guo, Yun Zhu, Yanmeng Wang, Shaojun Wang, Jing Xiao
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
