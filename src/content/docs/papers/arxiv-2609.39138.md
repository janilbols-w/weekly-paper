---
title: "MoSE: Mode-Switching Expander for Mixed LLM Training and Inference"
description: "AI clusters increasingly run large language model (LLM) inference and training on the same fabric."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2609.39138) · [PDF](https://arxiv.org/pdf/2609.39138)

## 一句话摘要

AI clusters increasingly run large language model (LLM) inference and training on the same fabric.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI clusters increasingly run large language model (LLM) inference and training on the same fabric. Prefill-decode (P-D) disaggregation creates key-value (KV) cache transfers between prefill and decode groups, whereas training collectives and all-to-all traffic benefit from near-uniform global connectivity. A static sparse topology can therefore be poorly matched to one of the two traffic patterns. We present Mode-Switching Expander (MoSE), a reconfigurable expander that treats topology design as a fixed-degree edge-allocation problem. MoSE reallocates the same sparse edge budget toward direct P-D connectivity in inference-heavy modes and restores a uniform random regular expander in training-heavy modes. We evaluate MoSE using a 1024-group flow-level topology model, shortest-path routing, and two mixed workloads. Across 20 seeds, MoSE reduces average and 95th-percentile (P95) load-aware KV communication cost by 90.8\% and 91.9\% relative to Static-Training in the inference-heavy mode. In the training-heavy mode, it reduces average and P95 training communication cost by 22.7\% and 27.6\% relative to stale Static-Inference. These results show that coarse-grained topology switching can support both workload modes without additional ports or routing changes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefill-decode
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fan Yang, Ying Zhou, Binglei Wang, Zhenjie Zhou, Jialong Li
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
