---
title: "Riemannian Graph Tokenizer for Structural Knowledge Transfer"
description: "Foundation models are at the forefront of artificial intelligence."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.15427v1) · [PDF](https://arxiv.org/pdf/2610.15427v1)

## 一句话摘要

Foundation models are at the forefront of artificial intelligence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Foundation models are at the forefront of artificial intelligence. A tokenizer, converting the raw input into discrete representations that the model can understand, plays an important role to the success of foundation models. Unlike the text tokenizer that is well studied in large language models, graph tokenizer is still at its early stage, facing the challenges of tackling the non-Euclidean structures and capturing the structural semantics. How to design a graph tokenizer for structural knowledge transfer? To this end, we propose a Riemannian Graph Tokenizer (RGT) that bridges the structural knowledge and quantized representations to support cross-domain structural knowledge transfer. The connection is established by Riemannian geometry. Specifically, we first define the geometric vocabulary (trees, cycles and sequences), which captures fundamental structural patterns and reflects the intrinsic geometry of graph. Second, we construct a Riemannian quantizer with Riemannian Straight-Through Estimator to tokenise graph structures across multiple domains into discrete tokens. To ensure consistency and transferability across diverse geometric spaces, RGT further incorporates a geometry-aligned decoder that projects manifold-specific tokens into a unified tangent space. The theoretical analysis and geometric interpretations are provided to support the effectiveness of our proposed method. Extensive experiments across diverse datasets demonstrate that RGT significantly enhances structural knowledge transferability across graph domains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qimin Zhou, Haibo Liu, Yujie Wang, Li Sun, Chuan Shi
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：Zhou, Qimin, et al. "Riemannian Graph Tokenizer for Structural Knowledge Transfer." Proceedings of the ACM Web Conference 2026. 2026
- 代码：未发现
- 阅读深度：metadata
