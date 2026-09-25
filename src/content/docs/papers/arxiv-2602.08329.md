---
title: "Near-Oracle KV Selection via Pre-hoc Sparsity for Long-Context Inference"
description: "A core bottleneck in large language model (LLM) inference is the cost of attending over the ever-growing key-value (KV) cache."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.08329) · [PDF](https://arxiv.org/pdf/2602.08329)

## 一句话摘要

A core bottleneck in large language model (LLM) inference is the cost of attending over the ever-growing key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

A core bottleneck in large language model (LLM) inference is the cost of attending over the ever-growing key-value (KV) cache. Although near-oracle top-k KV selection can preserve the quality of dense attention while sharply reducing computation and bandwidth, existing sparse methods generally rely on posterior heuristics, i.e., selectors conditioned on observed attention or proxy scores. Such conditioning introduces posterior bias: it tends to distort true token importance and miss salient tokens, thereby impairing long-range reasoning. To tackle this problem, we propose Pre-hoc Sparsity (PrHS), which selects KV entries before attention scoring and provides explicit accuracy control. Let the attention mass of discarded entries be delta (the dropped mass). Through a marginal-to-mutual-information analysis, we derive an upper bound on the mutual-information loss that depends only on the dropped mass. This relation explains failure modes of posterior heuristics and enables verifiable guarantees by controlling the dropped mass in advance. Within PrHS, we instantiate three orthogonal pre-hoc selectors along the axes of time, depth, and layer. Extensive experiments on LLaMA and Mistral families validate PrHS. Across GSM8K and CoQA, PrHS reduces retrieval overhead by over 90%, achieving 3x higher retrieval sparsity than HShare at matched or better accuracy. It incurs under 1% average degradation on LongBench, lowers attention FLOPs by about 15% versus prior sparse baselines, and yields a 9.9x speedup in attention-operator latency and 2.8x higher throughput on NVIDIA A100-80GB GPUs than the dense baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yifei Gao, Lei Wang, Rong-Cheng Tu, Qixin Zhang, Jun Cheng, Dacheng Tao
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
