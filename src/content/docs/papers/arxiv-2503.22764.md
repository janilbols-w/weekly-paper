---
title: "Boosting Large Language Models with Mask Fine-Tuning"
description: "The large language model (LLM) is typically integrated into the mainstream optimization protocol."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2503.22764) · [PDF](https://arxiv.org/pdf/2503.22764)

## 一句话摘要

The large language model (LLM) is typically integrated into the mainstream optimization protocol.

## 为什么值得关注

待编辑增强。

## 摘要原文

The large language model (LLM) is typically integrated into the mainstream optimization protocol. However, it remains underexplored whether maintaining the model integrity is \textit{indispensable} for promising performance. In this work, we introduce Mask Fine-Tuning (MFT), a novel LLM fine-tuning paradigm demonstrating that carefully breaking the model's structural integrity can surprisingly improve performance without updating model weights. MFT learns and applies binary masks to well-optimized models, using the standard LLM fine-tuning objective as supervision. Based on fully fine-tuned models, MFT uses the same fine-tuning datasets to achieve consistent performance gains across domains and backbones (e.g., an average gain of 2.70/4.15 on IFEval with LLaMA2-7B/3.1-8B). Detailed ablation studies and analyses examine the proposed MFT from different perspectives, including the sparse ratio and the loss surface. Additionally, when deployed on well-trained models, MFT is compatible with other LLM optimization procedures to improve overall model performance. Furthermore, this study extends the masking operation beyond its conventional use in network pruning for model compression to encompass a broader range of model capabilities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingyuan Zhang, Yue Bai, Huan Wang, Yizhou Wang, Qihua Dong, Yitian Zhang, Yun Fu
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
