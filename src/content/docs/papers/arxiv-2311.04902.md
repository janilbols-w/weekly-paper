---
title: "Beyond Size: How Gradients Shape Pruning Decisions in Large Language Models"
description: "Large Language Models (LLMs) with billions of parameters are prime targets for network pruning, which removes some model weights without hurting performance."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2311.04902) · [PDF](https://arxiv.org/pdf/2311.04902)

## 一句话摘要

Large Language Models (LLMs) with billions of parameters are prime targets for network pruning, which removes some model weights without hurting performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) with billions of parameters are prime targets for network pruning, which removes some model weights without hurting performance. Prior approaches such as magnitude pruning, SparseGPT, and Wanda either concentrated solely on weights or integrated weights with activations for sparsity. However, they overlooked the informative gradients derived from pretrained LLMs. In this paper, we present a novel sparsity-centric pruning method for pretrained LLMs, termed Gradient-based Language Model Pruner (GBLM-Pruner). GBLM-Pruner leverages the first-order term of the Taylor expansion, operating in a training-free manner by harnessing properly normalized gradients from a few calibration samples to determine the pruning metric, and substantially outperforms competitive counterparts like SparseGPT and Wanda in multiple benchmarks. Intriguingly, by incorporating gradients, unstructured pruning with our method tends to reveal some structural patterns, which mirrors the geometric interdependence inherent in the LLMs' parameter structure. Additionally, GBLM-Pruner functions without any subsequent retraining or weight updates to maintain its simplicity as other counterparts. Extensive evaluations on LLaMA-series, Qwen-Series and Deepseek models across zero-shot, STEM-Reasoning and Coding benchmarks show that GBLM-Pruner surpasses magnitude pruning and Wanda by significant margins and performs competitively against SparseGPT which involves intensive weight updates. We further extend our approach on Vision Transformer and Vision Language Models. Our code and models are available at https://github.com/VILA-Lab/GBLM-Pruner.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Rocktim Jyoti Das, Mukul Ranjan, Mingjie Sun, Liqun Ma, Zhiqiang Shen
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/VILA-Lab/GBLM-Pruner](https://github.com/VILA-Lab/GBLM-Pruner)
- 阅读深度：metadata
