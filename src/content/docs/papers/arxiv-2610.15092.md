---
title: "VLCQ: Post-training quantization for deep neural networks using variable length coding"
description: "Quantization plays a crucial role in efficiently deploying deep learning models on resource-constrained devices."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.15092v1) · [PDF](https://arxiv.org/pdf/2610.15092v1)

## 一句话摘要

Quantization plays a crucial role in efficiently deploying deep learning models on resource-constrained devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization plays a crucial role in efficiently deploying deep learning models on resource-constrained devices. Post-training quantization does not require access to the original dataset or retraining the full model. Current methods that achieve high performance close to baseline results typically require INT8 fixed-point integers. However, achieving higher model compression with lower bit-widths often leads to significant performance degradation. In this paper, we propose VLCQ, a post-training quantization method that relaxes the fixed-point encoding constraint, enabling more flexible exploration of quantization techniques through variable-length encoding. This approach achieves competitive or improved performance while reducing bit-widths, without requiring access to training data or model fine-tuning. Extensive experiments on image classification, segmentation, and object detection demonstrate that VLCQ improves model compression and accuracy compared with state-of-the-art post-training quantization approaches. For per-channel quantization, VLCQ surpasses FP32 accuracy and Piece-Wise Linear Quantization (PWLQ) on most evaluated models, achieving up to 6x compression compared with FP32 and up to 1.7x compared with PWLQ. When prioritizing compression with limited accuracy loss, VLCQ achieves up to 12.25x compression compared with FP32 with less than 4% performance degradation. For per-tensor quantization, VLCQ is competitive with Data-Free Quantization (DFQ), while providing greater flexibility to achieve lower bit rates across different tasks and models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Reem Abdel-Salam, Ahmed H. Abdel-Gawad, Amr G. Wassal
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：Reem Abdel-Salam, Ahmed H. Abdel-Gawad, and Amr G. Wassal. VLCQ: Post-training quantization for deep neural networks using variable length coding. Future Generation Computer Systems, 166, 107654, 2025
- 代码：未发现
- 阅读深度：metadata
