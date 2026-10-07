---
title: "Investigating Model Compression for Neural Machine Translation in the Biomedical Domain"
description: "Large-scale pretrained transformer models have achieved state-of-the-art performance across diverse machine translation tasks, including multilingual settings."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.07032) · [PDF](https://arxiv.org/pdf/2610.07032)

## 一句话摘要

Large-scale pretrained transformer models have achieved state-of-the-art performance across diverse machine translation tasks, including multilingual settings.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale pretrained transformer models have achieved state-of-the-art performance across diverse machine translation tasks, including multilingual settings. Knowledge distillation has emerged as a sustainable approach for model compression, transferring knowledge from large teacher models to smaller, more efficient student models. Similarly, quantization, which reduces the numerical precision of model weights and activations (e.g., from 32-bit to 8-bit representations) is widely used to accelerate inference, enabling models to run several times faster during deployment. However, both techniques face limitations when applied to specialized domain data, particularly under low-resource conditions. In knowledge distillation, the effectiveness of transfer is often constrained by the scarcity of domain-specific parallel data, while quantization can lead to performance degradation as bit precision decreases. In this work, we investigate the combined application of knowledge distillation and quantization for French-to-English biomedical translation, a domain characterized by specialized terminology and limited parallel resources. We develop and compare multiple fine-tuning strategies to adapt compressed student models to this challenging setting. Our experiments demonstrate that a collaboratively distilled and quantized student model achieves a 69% reduction in size, a 98.21% increase in inference speed, and a 98.46% reduction in CO2 emissions compared to the original baseline all without sacrificing translation quality. These results indicate that jointly optimized compression techniques can yield efficient, high-performance models suitable for translation service providers operating under resource constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maria Zafar, Souhail Bakkali, Rejwanul Haque
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
