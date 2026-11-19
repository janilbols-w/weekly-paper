---
title: "SilverSpoon-KD: A General-Purpose Toolkit for Knowledge Distillation"
description: "Knowledge distillation transfers deep learning representations from a teacher model to a student model, typically reducing model size or inference cost."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.22842) · [PDF](https://arxiv.org/pdf/2611.22842)

## 一句话摘要

Knowledge distillation transfers deep learning representations from a teacher model to a student model, typically reducing model size or inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation transfers deep learning representations from a teacher model to a student model, typically reducing model size or inference cost. However, knowledge distillation tooling has not kept pace with the breadth of research methods: existing toolkits typically support only a limited subset of techniques and use cases. We present SilverSpoon-KD, an open-source PyTorch toolkit that unifies different distillation paradigms and architectural relationships across workloads and applications behind a single API. Moreover, SilverSpoon-KD offers the first general-purpose blockwise knowledge distillation implementation with unique scalability features. We validate its versatility across vision, masked language model, and causal language models on tasks spanning homogeneous, heterogeneous, and quantization distillation across paradigms. We also evaluate SilverSpoon-KD by comparing its performance, including throughput and GPU memory usage, with existing toolkits. Despite extensive support for convenience, metric calculation, and tracking, we have found SilverSpoon-KD's performance to be on par with or better than existing toolkits.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xaver R. Davey, David Broman
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
