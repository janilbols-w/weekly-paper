---
title: "Deep Learning-Driven Peptide Classification in Biological Nanopores"
description: "Nanopore-based single-molecule sensing is a promising route to fast, low-cost disease diagnosis and protein sequencing: as an analyte such as a peptide or protein traverses a nanoscale pore, it modulates the ionic current, producing a resistive pulse whose signature is determined by the analyte's structure and its interactions with the pore."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2509.14029) · [PDF](https://arxiv.org/pdf/2509.14029)

## 一句话摘要

Nanopore-based single-molecule sensing is a promising route to fast, low-cost disease diagnosis and protein sequencing: as an analyte such as a peptide or protein traverses a nanoscale pore, it modulates the ionic current, producing a resistive pulse whose signature is determined by the analyte's structure and its interactions with the pore.

## 为什么值得关注

待编辑增强。

## 摘要原文

Nanopore-based single-molecule sensing is a promising route to fast, low-cost disease diagnosis and protein sequencing: as an analyte such as a peptide or protein traverses a nanoscale pore, it modulates the ionic current, producing a resistive pulse whose signature is determined by the analyte's structure and its interactions with the pore. Translating these signatures into reliable molecular identities, however, is an open problem well suited for machine learning, as the signals are noisy, suffer from variations due to experimental conditions, and are difficult to featurize, which has so far limited classification accuracy. Here we translate the peptide identification problem into an image-classification task by transforming each resistive pulse into a scaleogram via the continuous wavelet transform, a representation that jointly encodes amplitude, frequency, and time in a form well suited for deep convolutional models. On a dataset of 42 peptides, recorded as six separate peptide ladders, this approach reaches a macro-averaged classification accuracy of $82\,\%$ on held-out events, an improvement of $8.6$ percentage points over the descriptor-based approach previously reported for the same dataset. We further show that the trained models tolerate substantial compression, retaining their accuracy with half of their weights set to zero and under 8-bit quantization, a prerequisite for deploying trained classifiers on embedded sensing hardware. Our results demonstrate how physically motivated signal representations can make complex single-molecule data tractable for modern learning algorithms, a step on the path towards point-of-care peptide and protein diagnostics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Julian Ho{\ss}bach, Samuel Tovey, Sandro Kuppel, Tobias Ensslen, Jan C. Behrends, Christian Holm
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
