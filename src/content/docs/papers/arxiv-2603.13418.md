---
title: "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models"
description: "Structured pruning is widely applied to compress large language models (LLMs), but its performance depends heavily on how neuron importance is estimated."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.13418) · [PDF](https://arxiv.org/pdf/2603.13418)

## 一句话摘要

Structured pruning is widely applied to compress large language models (LLMs), but its performance depends heavily on how neuron importance is estimated.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning is widely applied to compress large language models (LLMs), but its performance depends heavily on how neuron importance is estimated. Most existing methods rely on activation statistics from a single calibration set, which introduces calibration bias and degrades downstream cross-task generalization. We observe that neurons exhibit heterogeneous distribution sensitivity, ranging from maintaining relatively stable rankings across calibration datasets to showing substantially larger cross-dataset variation. Ignoring this heterogeneity, existing methods rank all neurons in shared spaces with a uniform scoring source, so calibration-specific neurons dominate the ranking and weakly-activated neurons are scored unreliably. To address this, we propose GPrune-LLM, a structured pruning framework that reduces calibration bias by measuring and exploiting the cross-distribution behavior of neurons for fair comparison. Specifically, we restructure the neuron ranking space into behavior-consistent local spaces, adapt the scoring source where the calibration signal is unreliable, and learn per-module sparsity allocation under a global budget. Experiments across multiple models and downstream tasks show that GPrune-LLM improves the generalization of its base pruning metrics, with gains most pronounced at high sparsity, and reduces dependence on the choice of importance metric.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoyun Liu, Divya Saxena, Jiannong Cao, Yuqing Zhao, Yiying Dong, Penghui Ruan
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
