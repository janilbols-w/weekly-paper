---
title: "D-Quant: Driftable Entropy Coding for KV Cache Quantization"
description: "The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.19880) · [PDF](https://arxiv.org/pdf/2609.19880)

## 一句话摘要

The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

The KV cache has become a major bottleneck in deploying LLMs, as its memory footprint grows linearly with sequence length and batch size, imposing substantial pressure on both memory capacity and bandwidth. Among various KV cache compression techniques, quantization is particularly attractive due to its effectiveness and ease of deployment. However, most existing methods rely on fixed-width quantization, where a $b$ bit representation is inherently limited to $2^b$ quantization levels. As the bit width decreases, the number of available levels shrinks exponentially, leading to severe information loss and rapid performance degradation. We further observe that fixed-width quantization fails to exploit the highly non-uniform distribution of KV cache. After rotation and normalization, KV values approximately follow a normal distribution, with most values concentrated near the center and only a small fraction appearing in the tails. Nevertheless, fixed-width coding allocates the same number of bits to frequent and rare symbols. Entropy coding naturally exploits such non-uniformity by assigning shorter codewords to frequent symbols and longer ones to rare symbols, substantially reducing the average number of bits required for representation. However, its variable-length output is not suited to highly parallel attention kernels, where efficient dequantization and computation rely on regular memory layouts and fixed-stride accesses. To bridge this gap, we propose \textbf{D-Quant}, a flexible KV cache quantization framework that introduces a \textbf{drift} mechanism to convert entropy-coded representations of each token into fixed-size bitstreams, enabling regular memory access and parallel dequantization within attention kernels.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Su, Hong Liu, Guanghua Yu, Jianchen Zhu
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
