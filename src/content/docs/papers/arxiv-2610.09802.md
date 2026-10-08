---
title: "DisParQ: Self-Supervised Part Concepts for Interpretable Vision Foundation Models"
description: "Concept-based vision models represent images through an intermediate layer of human-inspectable concepts, so what a model relies on can be traced to those concepts."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.09802) · [PDF](https://arxiv.org/pdf/2610.09802)

## 一句话摘要

Concept-based vision models represent images through an intermediate layer of human-inspectable concepts, so what a model relies on can be traced to those concepts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Concept-based vision models represent images through an intermediate layer of human-inspectable concepts, so what a model relies on can be traced to those concepts. However, those models are often limited to fixed categories or depend on language to define their concepts. We introduce DisParQ (Discrete Parts with Quantized attributes), a method that learns spatially grounded, discrete concept representations from a powerful frozen vision-only self-supervised backbone. It requires no class labels and no language supervision. Each image patch is assigned to exactly one concept from a learnable prototype dictionary, and only a sparse subset of concepts may activate per image. To capture how each concept varies across images (e.g., the type of a "wheel"), we learn continuous residuals alongside the concepts and then quantize them into discrete attributes. A spatial decoder reconstructs the backbone's representation from the concepts and attributes alone, so successful reconstruction means that the discrete representation preserves the backbone's information. We evaluate DisParQ across seven datasets, from general recognition (ImageNet, PartImageNet, Places) to fine-grained benchmarks (CUB, Cars, Dogs, Flowers). We show that DisParQ closely matches its frozen DINOv2 teacher on ImageNet linear probing (83.2% top-1), achieves higher concept consistency than language-aligned models, remains competitive on fine-grained recognition, and enables cross-category part-based retrieval.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Adam Pardyl, Siddhartha Gairola, Sukrut Rao, Adam Wr\'obel, Bartosz Zieli\'nski, Bernt Schiele, Dawid Rymarczyk
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
