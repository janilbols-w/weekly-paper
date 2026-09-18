---
title: "QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization"
description: "Ubiquitous time series data across diverse domains enables critical applications in areas such as transportation systems and power grids."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.20156) · [PDF](https://arxiv.org/pdf/2609.20156)

## 一句话摘要

Ubiquitous time series data across diverse domains enables critical applications in areas such as transportation systems and power grids.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ubiquitous time series data across diverse domains enables critical applications in areas such as transportation systems and power grids. Recently, training foundation models on massive datasets to achieve accurate zero-shot forecasting has emerged as a major research focus. However, current studies predominantly prioritize architectural innovations while insufficiently addressing data diversity, often relying on simple data sampling strategies that fail to manage complex data distributions effectively, leading to inefficient use of training data and suboptimal performance. To address this, we propose QUALS, a large-scale time series corpus equilibrium framework. QUALS significantly enhances data efficiency, i.e., enabling existing models to achieve superior performance using only a small fraction of the original training data. Specifically, QUALS operates through two core mechanisms. First, a pattern quantization framework systematically decodes heterogeneous patterns from mixed corpora via vector quantization and uniform binning. Second, a learnability synchronization framework calibrates sampling weights for heterogeneous patterns, bridging the optimization gap between simple and complex motifs to maximize overall training efficiency. Extensive benchmarks demonstrate that pre-training on QUALS consistently achieves superior zero-shot performance, even under substantially reduced training budgets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yujie Li, Zezhi Shao, Chengqing Yu, Yisong Fu, Weijie Zhu, Yifan Du, Jilin Hu, Bin Yang, Yongjun Xu, Fei Wang
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
