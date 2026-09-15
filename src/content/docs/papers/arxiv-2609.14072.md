---
title: "Multi-Modal Tumor Survival Prediction via Graph-Guided Mixture of Experts"
description: "Large Language Models (LLMs) have displayed impressive capabilities in handling tasks that require few demonstration examples, making them effective few-shot learners."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.14072) · [PDF](https://arxiv.org/pdf/2609.14072)

## 一句话摘要

Large Language Models (LLMs) have displayed impressive capabilities in handling tasks that require few demonstration examples, making them effective few-shot learners.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have displayed impressive capabilities in handling tasks that require few demonstration examples, making them effective few-shot learners. Despite their potential, LLMs face challenges when it comes to addressing complex real-world tasks that involve multiple modalities or reasoning steps. For example, predicting cancer patients' survival period based on clinical data, cell slides, and genomics poses significant logistical complexities. Although several approaches have been proposed to tackle these challenges, they often fall short in achieving promising performance due to their inability to consider all modalities simultaneously or account for missing modalities, variations in modalities, and the integration of multi-modal data, ultimately compromising their effectiveness. This thesis proposes a novel approach for multi-modal tumor survival prediction to address these limitations. Taking inspiration from recent advancements in LLMs, particularly Mixture of Experts (MoE)-based models, a graph-guided MoE framework is introduced. This framework utilizes a graph structure to manage the predictions effectively and combines multiple models to enhance predictive power. Rather than training a single foundation model for end-to-end survival prediction, the approach leverages a MOE-guided ensemble to manage model callings as tools automatically. By leveraging the strengths of existing models and guiding them through a MOE framework, the aim is to achieve better performance and more accurate predictions in complex real-world tasks. Experiments and analysis on the TCGA-LUAD dataset show improved performance over the individual modal and vanilla ensemble models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：H Mathavan, H Liu
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
