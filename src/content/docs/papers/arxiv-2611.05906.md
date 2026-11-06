---
title: "CHARM+: Cross-Hardware Attention with Re-Merge Multistream Mechanism"
description: "As sequence lengths continue to grow, distributed attention based on sequence parallel (e.g., Ring-Attention) has become a mainstream solution for large language models (LLMs)."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.05906) · [PDF](https://arxiv.org/pdf/2611.05906)

## 一句话摘要

As sequence lengths continue to grow, distributed attention based on sequence parallel (e.g., Ring-Attention) has become a mainstream solution for large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

As sequence lengths continue to grow, distributed attention based on sequence parallel (e.g., Ring-Attention) has become a mainstream solution for large language models (LLMs). Nevertheless, inherent communication dependencies limit computation-communication overlap, reducing GPU utilization. Moreover, in cross-hardware (NUMA or node) architectures, due to imbalanced communication bandwidth, frequent communication synchronization will limit overall performance. Based on these insights, we propose CHARM+, Cross-Hardware Attention with Re-Merge Multistream Mechanism. We reorganize sequential communications into several levels and achieve intra-level parallelism and computation overlap. Furthermore, we decouple cross-hardware communication from intra-hardware communication, eliminating synchronization overhead caused by bandwidth imbalance. Forward and backward algorithms were evaluated on multiple hardware architectures and consistently outperformed state-of-the-art methods. Compared to Ring-Attention, our forward and backward algorithms achieve average speedups of 1.3x and 1.7x on a dual-NUMA PCIe architecture, and 2.8x and 2.9x on a dual-node NVLink architecture, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sequence parallel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xinhang Zhang, Boning Zhang, Chengchun Liu, Chunpu Li, Lei Sun, Weifeng Zhang, Limin Xiao
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
