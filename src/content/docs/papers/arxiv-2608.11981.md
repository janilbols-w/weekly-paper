---
title: "Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed"
description: "Small Language Models (SLMs) have emerged as a more efficient alternative to traditional Large Language Models (LLMs), offering promising potential in resource-constrained scenarios."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.11981) · [PDF](https://arxiv.org/pdf/2608.11981)

## 一句话摘要

Small Language Models (SLMs) have emerged as a more efficient alternative to traditional Large Language Models (LLMs), offering promising potential in resource-constrained scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small Language Models (SLMs) have emerged as a more efficient alternative to traditional Large Language Models (LLMs), offering promising potential in resource-constrained scenarios. Existing approaches to building SLMs typically follow two paths: training compact models from scratch, or compressing larger pre-trained models using methods such as pruning, quantization, or distillation. As language models become increasingly integrated into real-world applications, ensuring their trustworthiness has become a critical concern. However, how to build trustworthy SLMs remains an underexplored question. In this work, we present a comprehensive evaluation of SLM trustworthiness across multiple dimensions, including fairness, robustness, privacy, and ethics. We first examine the effects of pruning and quantization, and find that quantization is significantly more effective in preserving trustworthiness compared to pruning. More importantly, we demonstrate that compressing a reliable large model via quantization can produce SLMs with superior trustworthiness and adaptability compared to using small models trained from scratch. Furthermore, knowledge distillation from trustworthy teacher models can further enhance the reliability of SLMs. We hope our findings provide practical guidance and a foundation for future research into the development and deployment of trustworthy small language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haokun Lin, Kaijie Zhu, Haobo Xu, Yichen Wu, Zhichao Lu, Qingfu Zhang, Zhenan Sun
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
