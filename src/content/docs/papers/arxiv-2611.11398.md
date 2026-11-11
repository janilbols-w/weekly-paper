---
title: "Decomposing Earth Embeddings with Sparse Autoencoders"
description: "Earth observation foundation models produce global metre-resolution embeddings that underpin work across agriculture, ecology, hydrology, and beyond."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.11398) · [PDF](https://arxiv.org/pdf/2611.11398)

## 一句话摘要

Earth observation foundation models produce global metre-resolution embeddings that underpin work across agriculture, ecology, hydrology, and beyond.

## 为什么值得关注

待编辑增强。

## 摘要原文

Earth observation foundation models produce global metre-resolution embeddings that underpin work across agriculture, ecology, hydrology, and beyond. Yet these embeddings are opaque: each dimension entangles unrelated physical concepts, which makes them difficult to interpret and their robustness hard to assess. Here, we propose sparse autoencoders (SAEs) as a principled way to decompose Earth embeddings into sparse, approximately monosemantic features over an overcomplete dictionary. Because LLM judges of interpretations do not transfer to satellite pixels, and spatial autocorrelation matters, we introduce a tailored evaluation protocol. It scores any SAE on reconstruction at matched sparsity, alignment with reference concepts, and spatial scale, each against baselines that include an SAE whose decoder is a frozen random dictionary. On this protocol, SAEs reconstruct AlphaEarth and Tessera embeddings better than every baseline at matched sparsity. Their features align with far fewer reference concepts than raw embedding dimensions (on AlphaEarth, 88% align with at most one of 20 concept groups, most with none, against a median of 12 per raw dimension). They also carry more of their variance at fine spatial scales (23 to 32% within a 640 m patch for BatchTopK and Matryoshka, against 9%). An SAE with a frozen random decoder shares both properties, which therefore follow from sparsity, whereas only a learned dictionary reconstructs the embedding accurately: on AlphaEarth, trained SAEs leave eight times less variance unexplained. We test the sparse code on two applications, discovering land-cover sub-concepts and detecting out-of-distribution pixels by area-of-applicability estimation. Both indicate how sparse features could be used, but neither is yet reliable enough for practical use. Together, these results are a step toward Earth observation models whose features can be inspected.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vitus Benson, Fanny Yang, Markus Reichstein
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
