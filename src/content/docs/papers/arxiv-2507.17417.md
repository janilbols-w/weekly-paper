---
title: "A Comprehensive Evaluation on Quantization Techniques for Large Language Models"
description: "For large language models (LLMs), post-training quantization (PTQ) significantly reduces memory and computational overhead."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2507.17417) · [PDF](https://arxiv.org/pdf/2507.17417)

## 一句话摘要

For large language models (LLMs), post-training quantization (PTQ) significantly reduces memory and computational overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

For large language models (LLMs), post-training quantization (PTQ) significantly reduces memory and computational overhead. Despite rapid advancements, existing papers often lack experiments on the same ground. In addition, since quantization solutions typically contain multiple components, it is important to analyze the connections among numerous existing methods to gain an in-depth understanding of this field. To bridge these gaps, we conduct an up-to-date and extensive review of the state-of-the-art methods and perform comprehensive evaluations of low-bit quantization on representative text-only LLMs on the same ground to ensure fair comparisons. To our knowledge, this fair and extensive investigation remains critically important yet significantly underexplored in the research community. To better understand the connections, we first decouple published quantization into two steps: pre-quantization transformation to reduce outliers, and quantization error mitigation to offset performance loss. Second, we extensively evaluate the impact of quantization settings, including granularity and symmetry. Third, we analyze the performance of the latest MXFP4 and NVFP4 data formats. Our experimental results first demonstrate that optimizing rotation and scaling yields the best pre-quantization transformation, while combining low-rank compensation with GPTQ occasionally outperforms using GPTQ alone. Second, we verify that finer granularity improves performance at the cost of storage and asymmetric quantization benefits activations significantly more than weights. Third, we find that the format and precision of scaling factors have a significant impact on performance; notably, rotation-based transformation is effective for INT4 but demonstrates little improvement for MXFP4 and NVFP4, inspiring further investigation in this field.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yutong Liu, Cairong Zhao, Guosheng Hu
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
