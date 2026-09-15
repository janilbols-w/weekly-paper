---
title: "Data Efficient Any Transformer-to-Mamba Distillation via Attention Bridge"
description: "State-space models (SSMs) have emerged as promising alternatives to Transformers for sequence modeling."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.19266) · [PDF](https://arxiv.org/pdf/2510.19266)

## 一句话摘要

State-space models (SSMs) have emerged as promising alternatives to Transformers for sequence modeling.

## 为什么值得关注

待编辑增强。

## 摘要原文

State-space models (SSMs) have emerged as promising alternatives to Transformers for sequence modeling. However, training competitive SSMs from scratch remains computationally intensive, and the ecosystem around them is far less mature than that of Transformers. Moreover, the architectural differences between SSMs and Transformers make it challenging to efficiently transfer knowledge from pretrained Transformers. In this work, we propose Cross-architecture distillation via Attention Bridge (CAB), a distillation framework that transfers attention-related representations from Transformer teachers to state-space student models. Unlike conventional knowledge distillation that supervises only final predictions, CAB enables token-level intermediate supervision through a lightweight bridge and flexible layer-wise alignment. By aligning Transformer attention-related representations with Mamba's token-dependent state projections, CAB facilitates efficient cross-architecture knowledge transfer without inference-time overhead. Experiments on image classification and language modeling demonstrate that CAB improves Transformer-to-SSM distillation, particularly under limited-supervision settings. Overall, CAB provides an efficient pathway for transferring Transformer representations to SSM-based models, helping bridge the gap between mature Transformer ecosystems and emerging SSM ecosystems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Penghao Wang, Yuhao Zhou, Mengxuan Wu, Panpan Zhang, Zhangyang Wang, Kai Wang
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
