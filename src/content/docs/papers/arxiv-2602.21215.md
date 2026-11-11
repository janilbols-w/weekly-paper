---
title: "Inference-time Alignment via Sparse Junction Steering"
description: "Token-level steering has emerged as a pivotal approach for inference-time alignment, enabling fine-grained control over large language models (LLMs) by modulating their output distributions without parameter updates."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.21215) · [PDF](https://arxiv.org/pdf/2602.21215)

## 一句话摘要

Token-level steering has emerged as a pivotal approach for inference-time alignment, enabling fine-grained control over large language models (LLMs) by modulating their output distributions without parameter updates.

## 为什么值得关注

待编辑增强。

## 摘要原文

Token-level steering has emerged as a pivotal approach for inference-time alignment, enabling fine-grained control over large language models (LLMs) by modulating their output distributions without parameter updates. While effective, existing methods rely on dense intervention at every decoding step. This persistent manipulation not only incurs substantial computational overhead but also risks compromising generation quality by excessively drifting from the model's intrinsic distribution. In this work, we show that dense intervention is unnecessary and propose Sparse Inference-time Alignment (SIA), which performs sparse junction steering, intervening only at critical decision points along the generation trajectory. Our key insight is that high-entropy junctions are empirically consistent with pivotal decision points in the generation trajectory and are particularly susceptible to misalignment, suggesting that these points benefit from alignment-related reward signal. Extensive experiments across different model families and alignment objectives show that steering only 20%-80% of tokens achieves the superior alignment-efficiency trade-offs. For strong base models such as Qwen3, intervening on as few as 20% of tokens matches or even surpasses heavily post-trained instruct models. This sparsity enables stronger guidance while better preserving the model's native distribution, integrates seamlessly with search-based methods (e.g., Best-of-N), and improves efficiency by reducing the required sampling budget while yielding practical wall-clock speedups under matched-quality comparisons.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparse inference, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Runyi Hu, Jie Zhang, Shiqian Zhao, Jiale Meng, Jiwei Li, Jason Zeng, Ming Wu, Michael Heinrich, Yonggang Wen, Tianwei Zhang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
