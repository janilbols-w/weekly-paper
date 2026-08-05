---
title: "Orchestrating Dual-Boundaries: An Arithmetic Intensity Inspired Acceleration Framework for Diffusion Language Models"
description: "Diffusion-based large language models (dLLMs) have recently gained significant attention for their exceptional performance and inherent potential for parallel decoding."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2511.21759) · [PDF](https://arxiv.org/pdf/2511.21759)

## 一句话摘要

Diffusion-based large language models (dLLMs) have recently gained significant attention for their exceptional performance and inherent potential for parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion-based large language models (dLLMs) have recently gained significant attention for their exceptional performance and inherent potential for parallel decoding. Existing frameworks further enhance its inference efficiency by enabling KV caching. However, its bidirectional attention mechanism necessitates periodic cache refreshes that interleave prefill and decoding phases, both contributing substantial inference cost and constraining achievable speedup. Inspired by the heterogeneous arithmetic intensity of the prefill and decoding phases, we propose ODB-dLLM, a framework that orchestrates dual-boundaries to accelerate dLLM inference. In the prefill phase, we find that the predefined fixed response length introduces heavy yet redundant computational overhead, which affects efficiency. To alleviate this, ODB-dLLM incorporates an adaptive length prediction mechanism that progressively reduces prefill overhead and unnecessary computation. In the decoding phase, we analyze the computational characteristics of dLLMs and propose a dLLM-specific jump-share speculative decoding method to enhance efficiency by reducing the number of decoding iterations. Experimental results demonstrate that ODB-dLLM achieves 46-162x and 2.63-6.30x speedups over the baseline dLLM and Fast-dLLM, respectively, while simultaneously mitigating the accuracy degradation in existing acceleration frameworks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Linye Wei, Wenjue Chen, Pingzhi Tang, Xiaotian Guo, Le Ye, Runsheng Wang, Meng Li
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
