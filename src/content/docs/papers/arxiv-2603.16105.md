---
title: "Frequency Matters: Fast Model-Agnostic Data Curation for Pruning and Quantization"
description: "Post-training model compression is essential for enhancing the portability of Large Language Models (LLMs) while preserving their performance."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.16105) · [PDF](https://arxiv.org/pdf/2603.16105)

## 一句话摘要

Post-training model compression is essential for enhancing the portability of Large Language Models (LLMs) while preserving their performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training model compression is essential for enhancing the portability of Large Language Models (LLMs) while preserving their performance. While several compression approaches have been proposed, less emphasis has been placed on selecting the most suitable set of data (the so-called \emph{calibration data}) for finding the compressed model configuration. The choice of calibration data is a critical step in preserving model capabilities both intra- and inter-tasks. In this work, we address the challenge of identifying high-performance calibration sets for both pruning and quantization by analyzing intrinsic data properties rather than model-specific signals. We introduce ZipCal, a model-agnostic data curation strategy that maximizes lexical diversity based on Zipfian power laws. Experiments demonstrate that our method outperforms standard uniform random sampling across various pruning benchmarks. Notably, it also performs on par, in terms of downstream performance, with a state-of-the-art method that relies on model perplexity. The latter becomes prohibitively expensive for large-scale models and datasets, while ZipCal is on average $\sim$240$\times$ faster due to its tractable linear complexity. We make the code and the experiments available at https://github.com/FrancescoMonaco/ZipCal.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model, pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Francesco Pio Monaco, Elia Cunegatti, Flavio Vella, Giovanni Iacca
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/FrancescoMonaco/ZipCal](https://github.com/FrancescoMonaco/ZipCal)
- 阅读深度：metadata
