---
title: "SLICEChat: Progressive In-Encoder Token Pruning for Whole-Slide Pathology Language Models"
description: "Whole-slide pathology images (WSIs) contain gigapixel-scale visual content, creating a major scalability challenge for slide-level multimodal large language models (MLLMs)."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.24894) · [PDF](https://arxiv.org/pdf/2609.24894)

## 一句话摘要

Whole-slide pathology images (WSIs) contain gigapixel-scale visual content, creating a major scalability challenge for slide-level multimodal large language models (MLLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Whole-slide pathology images (WSIs) contain gigapixel-scale visual content, creating a major scalability challenge for slide-level multimodal large language models (MLLMs). Existing approaches process thousands of patch tokens and typically apply compression only after slide encoding, leaving multimodal attention computationally expensive. We introduce SLICEChat, a slide-level MLLM that integrates progressive token pruning within a hybrid Mamba--Transformer slide encoder. Mamba layers enable efficient long-range propagation, while Transformer layers preserve global interactions as the sequence is progressively shortened. Between stages, language-supervised, region-aware pruning removes spatially coherent low-utility regions under a controlled keep-rate schedule, producing compact slide representations before multimodal fusion. On SlideBench VQA, SLICEChat achieves 79.84% accuracy on TCGA and 59.09% on BCNB cohorts, outperforming prior slide-level pathology MLLMs, and achieves the highest overall WSI-Bench metrics. It also provides competitive memory usage and the inference latency among the evaluated models. These results demonstrate accurate and computationally efficient multimodal reasoning over gigapixel WSIs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ali Kerem Bozkurt, Baris Cem Bakay, Ibrahim Kulac, Cigdem Gunduz-Demir, Erkut Erdem, Aykut Erdem
- 发布：2026-09-21；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ali-kerem/SLICEChat](https://github.com/ali-kerem/SLICEChat)
- 阅读深度：metadata
