---
title: "DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference"
description: "Transformer-based large language models (LLMs) achieve strong performance across many tasks, but their Key-Value (KV) cache grows linearly with sequence length, creating a severe memory bottleneck for long-context inference."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.08878) · [PDF](https://arxiv.org/pdf/2608.08878)

## 一句话摘要

Transformer-based large language models (LLMs) achieve strong performance across many tasks, but their Key-Value (KV) cache grows linearly with sequence length, creating a severe memory bottleneck for long-context inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based large language models (LLMs) achieve strong performance across many tasks, but their Key-Value (KV) cache grows linearly with sequence length, creating a severe memory bottleneck for long-context inference. Existing heuristic eviction methods (e.g., H$_2$O and SnapKV) rely on static attention or positional signals that often fail to capture a token's future predictive influence. We propose DistillCache, a reinforcement learning framework that formulates KV-cache eviction as a sequential decision problem. DistillCache learns a lightweight policy network using rich internal model signals (attention statistics, value norms, entropy, and position) and trains it with REINFORCE via a per-step KL-divergence reward to preserve the full-cache output distribution. On a 7B-parameter instruction-tuned Transformer (Mistral-7B-Instruct-v0.3), DistillCache retains 94.2% of full-cache accuracy on LongBench at a 25% cache budget, outperforming both strong heuristic baselines (H$_2$O, SnapKV) by up to 2.7 absolute points and, under our re-implementations, concurrent RL-based methods (ForesightKV, RLKV) by up to 1.4 points on long-context tasks. On reasoning benchmarks, DistillCache is competitive with the best concurrent method and surpasses it under aggressive compression. It also delivers up to 2.1x full-cache throughput while maintaining competitive practical efficiency. These results highlight the effectiveness of learned, distribution-aware policies for memory-efficient long-context LLM inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Asaad Althoubi
- 发布：2026-08-09；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
