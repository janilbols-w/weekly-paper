---
title: "DAQ: Decision-Aligned Post-Training Quantization for Spiking Transformers"
description: "Spiking transformers combine attention-based representation learning with sparse spike communication, yet their weights and membrane variables still incur substantial storage and computation overhead."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.22611) · [PDF](https://arxiv.org/pdf/2611.22611)

## 一句话摘要

Spiking transformers combine attention-based representation learning with sparse spike communication, yet their weights and membrane variables still incur substantial storage and computation overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking transformers combine attention-based representation learning with sparse spike communication, yet their weights and membrane variables still incur substantial storage and computation overhead. Post-training quantization (PTQ) offers a practical way to reduce these overheads, but preserving neuronal firing under weight and membrane quantization remains challenging. In this paper, we propose Decision-Aligned Post-Training Quantization (DAQ), a method that calibrates the quantizers to align neuronal firing decisions with those of a floating-point reference. We analyze how errors from these quantizers affect firing at decision boundaries and how they propagate over time steps in recurrent neurons. Based on this analysis, we formulate an objective that encourages quantized membrane variables to remain within the reference firing regions along the quantized model's own state trajectory. Experiments across multiple spiking transformer architectures on image classification, semantic segmentation, and event-based tracking demonstrate the effectiveness of DAQ with 4-bit weights and membrane variables. On FE108, DAQ achieves 58.8\% AUC and 90.9\% PR with SDTrack, while reducing energy by 66.2\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jialin Chen, Xiaochen Zhao, Aili Wang
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
