---
title: "ICICLE: In-Context Inference for Curve-Learning Extrapolation"
description: "Freeze-thaw Bayesian optimization allocates training budget by predicting how partially observed learning curves will continue."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.24469) · [PDF](https://arxiv.org/pdf/2611.24469)

## 一句话摘要

Freeze-thaw Bayesian optimization allocates training budget by predicting how partially observed learning curves will continue.

## 为什么值得关注

待编辑增强。

## 摘要原文

Freeze-thaw Bayesian optimization allocates training budget by predicting how partially observed learning curves will continue. LC-PFN first applied prior-data fitted networks (PFNs) to learning-curve extrapolation, and FT-PFN extended this approach to configuration-aware freeze-thaw optimization with a ten-slot hyperparameter encoder. We introduce In-Context Inference for Curve-Learning Extrapolation (ICICLE), an in-context surrogate that accepts a variable number of hyperparameters through a shared set encoder and is trained on a synthetic prior covering typed hyperparameters, heavy-tailed noise, quantization, and divergence. ICICLE has 1.28 million parameters (8.7% of FT-PFN's count) and produces similar mean-regret trajectories to FT-PFN on LCBench, PD1, and TaskSet. On the 86-task Meta-Album benchmark with 33 hyperparameters, ICICLE reaches lower mean normalized regret than Quick-Tune overall and on extended, with no clear difference on mini or micro. It does so without pre-training or meta-training on Meta-Album tasks, whereas Quick-Tune is meta-trained on related Meta-Album tasks. Our release samples synthetic training tasks on the fly and provides a freeze-thaw scheduler for Ray Tune and an ONNX model for inference without JAX or PyTorch.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Laurits Fredsgaard, Michael Riis Andersen, Mikkel N. Schmidt
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/lauritsf/icicle](https://github.com/lauritsf/icicle)
- 阅读深度：metadata
