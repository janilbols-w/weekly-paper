---
title: "Benford's Law as a Distributional Prior for Post-Training Quantization of Large Language Models"
description: "Post-training quantization (PTQ) is a practical way to reduce the memory footprint of large language models, but low-bit quantization is sensitive to mismatches between the quantization codebook and the empirical weight/activation distributions."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.00165) · [PDF](https://arxiv.org/pdf/2602.00165)

## 一句话摘要

Post-training quantization (PTQ) is a practical way to reduce the memory footprint of large language models, but low-bit quantization is sensitive to mismatches between the quantization codebook and the empirical weight/activation distributions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) is a practical way to reduce the memory footprint of large language models, but low-bit quantization is sensitive to mismatches between the quantization codebook and the empirical weight/activation distributions. We revisit Benford-like leading-digit statistics as a lightweight diagnostic of scale-broad behavior in transformer tensors. Across several model families, we observe a consistent functional dichotomy: transformational nn.Linear weights tend to be Benford-like, whereas LayerNorm parameters systematically deviate. Motivated by this observation, we propose BenQ, a data-free PTQ codebook that uses a simple log-spaced grid as a proxy for scale-broad distributions and applies it selectively to transformational layers while keeping stability-critical parameters in higher precision. In 4-bit group-wise PTQ, BenQ consistently improves over uniform RTN and trades wins with NF4 across architectures and tasks, while remaining substantially simpler than optimization-based methods. We additionally report dynamic activation quantization as an exploratory stress test: the results show that log-spaced grids can reduce RTN failures in some families, but also reveal that outlier handling remains essential for reliable low-bit activation PTQ. Code is available at https://github.com/ufopcsilab/benford-quant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Arthur Negr\~ao, Pedro Silva, Vander L. S. Freitas, Gladston Moreira, Eduardo Luz
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ufopcsilab/benford-quant](https://github.com/ufopcsilab/benford-quant)
- 阅读深度：metadata
