---
title: "GateWatch: Low-Overhead LLM Monitoring with Boolean Circuits"
description: "As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.24619) · [PDF](https://arxiv.org/pdf/2611.24619)

## 一句话摘要

As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) and LLM-based agents are increasingly deployed, monitoring their behavior becomes important for detecting unsafe or unintended actions. Activation probes offer an efficient approach, but existing methods face trade-offs between accuracy, interpretability, and computational overhead. Probes on raw activations lack interpretable inputs, whereas sparse autoencoder (SAE) probes use interpretable features but often rely on additive classifiers and large SAE encoders, limiting interpretability and increasing memory overhead. We introduce GateWatch, a compact, interpretable classifier that expresses its entire decision rule as an explicit Boolean logic over a small number of binarized SAE features. We explore three approaches to constructing these circuits under a specified gate budget. For efficient deployment, GateWatchServe computes only selected SAE features, enables streaming of their binary values across layers during inference, and evaluates multiple GateWatch classifiers in parallel using compact lookup tables. Across 24 tasks on Gemma-2-9B, GateWatch achieves 80.49% mean test accuracy using only 3.8 SAE features and 3.5 logic gates per probe on average, just 1.17 percentage points below full 16K-feature SAE probes, while matching or outperforming them on 10 tasks and reducing probe memory by 99.98%. Inside vLLM, 1,000 concurrent multi-layer, multi-token GateWatch classifiers retain 97-98% of baseline throughput and 99.8% of KV-cache capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Firas Spanioli, Yaniv David
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
