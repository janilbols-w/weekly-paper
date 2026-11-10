---
title: "The Sparsity Whisperer"
description: "Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.06630) · [PDF](https://arxiv.org/pdf/2608.06630)

## 一句话摘要

Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pruning reduces the inference cost of large language models, but existing criteria primarily preserve large activations or reconstruct layer outputs. We argue that this overlooks a key computation performed by particularly sparsity-sensitive neurons in the MLP up and gate projections: separating similar inputs into dissimilar outputs. This suggests that effective pruning should preserve not only activations, but also the differences between outputs more broadly. We introduce a family of difference-informed pruning methods built upon this principle. Wisp+ is a neuronwise, update-free method that prioritizes the input pairs each neuron separates most strongly relative to their distance. Wisp provides a more efficient layerwise alternative that scores weights using shared input-difference norms. Finally, Whisper extends global difference preservation to second-order reconstruction using a lightly regularized difference Hessian. Across Llama 2 and 3.1 models from 7B to 405B parameters, our second-order variant consistently improves over strong reconstruction-based baselines, while our update-free variants improve over activation-aware baselines, especially in constrained settings. The improvements over Wanda and SparseGPT extend to structured sparsity, downstream evaluations, and other model families. Augmenting stronger techniques such as RIA and ALPS with our difference-informed criteria yields further improvements, shifting the overall accuracy-runtime frontier outward at negligible additional cost. These results suggest that preserving output differences is a broadly useful and composable signal for post-training LLM sparsification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Linghao Kong, Inimai Subramanian, Micah Adler, Dan Alistarh, Dan Gutfreund, Nir Shavit
- 发布：2026-08-10；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
