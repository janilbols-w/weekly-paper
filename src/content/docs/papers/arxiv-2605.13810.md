---
title: "DASHQuant: Provable Quantization with a Single Randomized Hadamard Transform"
description: "Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV cache compression."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.13810) · [PDF](https://arxiv.org/pdf/2605.13810)

## 一句话摘要

Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV cache compression.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vector quantization via random projection followed by scalar quantization is a fundamental primitive in machine learning, with applications ranging from similarity search to federated learning and KV cache compression. While dense random rotations yield clean theoretical guarantees, they require $\Theta(d^2)$ time. The randomized Hadamard transform $HD$ reduces this cost to $O(d \log d)$, but its discrete structure complicates analysis and leads to weaker or purely empirical compression guarantees. In this work, we introduce DASHQuant (Dithered Accelerated Single-Hadamard Quantization), a provable variant of this approach. Specifically, the quantizer applies $HD$ to the input vector and adds a random dithering before quantizing, injecting additional randomness at negligible cost. We prove that this approach is unbiased and provides mean squared error bounds that asymptotically match those achievable with truly random rotation matrices. In particular, we prove that a dithered version of TurboQuant, and a special case of EDEN, achieves mean squared error $\bigl(\pi\sqrt{3}/2 + o(1)\bigr) \cdot 4^{-b}$ at $b$ bits per coordinate, where the $o(1)$ term vanishes uniformly over all unit vectors and all dimensions as the number of quantization levels grows.

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

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ying Feng, Piotr Indyk, Michael Kapralov, Dmitry Krachun, Boris Prokhorov
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
