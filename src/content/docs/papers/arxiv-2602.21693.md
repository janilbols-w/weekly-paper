---
title: "TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts"
description: "Multimodal time series forecasting has garnered significant attention for its potential to provide more accurate predictions than traditional single-modality models by leveraging rich information inherent in other modalities."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2602.21693) · [PDF](https://arxiv.org/pdf/2602.21693)

## 一句话摘要

Multimodal time series forecasting has garnered significant attention for its potential to provide more accurate predictions than traditional single-modality models by leveraging rich information inherent in other modalities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal time series forecasting has garnered significant attention for its potential to provide more accurate predictions than traditional single-modality models by leveraging rich information inherent in other modalities. However, due to fundamental challenges in modality alignment, existing methods often struggle to effectively incorporate multimodal data into predictions, particularly textual information that has a causal influence on time series fluctuations, such as emergency reports and policy announcements. In this paper, we reflect on the role of textual information in numerical forecasting and propose Time series transformers with Multimodal Mixture-of-Experts, TiMi, to unleash the causal reasoning capabilities of LLMs. Concretely, TiMi utilizes LLMs to generate inferences on future developments, which serve as guidance for time series forecasting. To seamlessly integrate both exogenous factors and time series into predictions, we introduce a Multimodal Mixture-of-Experts (MMoE) module as a lightweight plug-in to empower Transformer-based time series models for multimodal forecasting, eliminating the need for explicit representation-level alignment. Experimentally, our proposed TiMi demonstrates consistent state-of-the-art performance on sixteen real-world multimodal forecasting benchmarks, outperforming advanced baselines while offering both strong adaptability and interpretability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiafeng Lin, Yuxuan Wang, Huakun Luo, Jianmin Wang, Zhongyi Pei
- 发布：2026-08-20；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
