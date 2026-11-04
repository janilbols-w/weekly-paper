---
title: "Quantization of Large Models with Weight Outliers and Sparsity"
description: "Post-training quantization (PTQ) reduces the memory burden of large model deployment by casting the high precision trained weights to fewer bits."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00286) · [PDF](https://arxiv.org/pdf/2611.00286)

## 一句话摘要

Post-training quantization (PTQ) reduces the memory burden of large model deployment by casting the high precision trained weights to fewer bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) reduces the memory burden of large model deployment by casting the high precision trained weights to fewer bits. While this promotes memory-efficient inference, it also incurs quantization error that impairs model performance. To compensate for quantization error, the present contribution decomposes the original trained weights into a quantized matrix, a low-rank component, and a sparse matrix that accounts for outlier rows in the weights. Due to analytical intractability and the discrete structure of the decomposition, a simulated annealing search is employed to explore candidate decompositions while avoiding poor local minima. Numerical tests demonstrate the effectiveness of this approach across a broad suite of large language models, including Llama 3.2 1B, Llama 3.2 3B, Llama 3.1 8B, and Qwen2.5 7B, evaluated on natural language generation benchmarks using 4-bit NF4 and FP4 quantizers. The novel method can markedly outperform direct quantization while incurring minimal memory overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leonidas Tsigkounakis, Abraham Jaeger Mountain, Yilang Zhang, Georgios B. Giannakis
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
