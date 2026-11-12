---
title: "MNN-Pocket-0.3B Technical Report"
description: "This technical report presents MNN-Pocket-0.3B, a compact 300M-parameter dense language model designed for efficient on-device deployment and supporting context lengths of up to 32K tokens."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.12311) · [PDF](https://arxiv.org/pdf/2611.12311)

## 一句话摘要

This technical report presents MNN-Pocket-0.3B, a compact 300M-parameter dense language model designed for efficient on-device deployment and supporting context lengths of up to 32K tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

This technical report presents MNN-Pocket-0.3B, a compact 300M-parameter dense language model designed for efficient on-device deployment and supporting context lengths of up to 32K tokens. With an INT4 deployment footprint of only 173 MB and decoding throughput of up to 466 tokens/s on iPad Pro M5 (Metal), it can be seamlessly integrated into applications on edge devices such as smartphones and smart glasses. MNN-Pocket-0.3B is developed through the co-design of its architecture, data, training pipeline, and inference system. Hardware-aware architecture selection and dependency-aware vocabulary pruning balance model capability with on-device memory and compute constraints. A four-stage pre-training pipeline covering approximately 4.1 trillion high-quality Chinese and English tokens equips the model with broad knowledge and reasoning capabilities. This is followed by a three-stage post-training pipeline comprising instruction fine-tuning, multi-teacher on-policy distillation, and quantization-aware training. Finally, hardware-specific optimizations in the MNN inference engine enable fast, memory-efficient inference and long-context processing. Extensive evaluations demonstrate that MNN-Pocket-0.3B achieves frontier-level performance among models of comparable size, with particularly strong results in Chinese and English knowledge and reasoning, mathematics, coding, and instruction following. It consistently outperforms similarly sized open-source models and even surpasses several 0.5B-parameter models on instruction-following benchmarks. We release MNN-Pocket-0.3B with open weights and ready-to-use MNN deployment packages. We hope it will provide a practical foundation for capable, responsive, and memory-efficient edge applications while advancing research and development in on-device language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：MNN Team
- 发布：2026-11-10；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
