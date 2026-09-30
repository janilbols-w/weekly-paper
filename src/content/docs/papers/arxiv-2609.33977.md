---
title: "GroupMask: Layer-Adaptive Group-wise Sparsity for Semi-Structured LLM Pruning"
description: "Semi-structured pruning compresses large language models (LLMs) while keeping a regular sparse structure, but the prevailing N:M pattern fixes the same local sparsity ratio in every layer."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.33977) · [PDF](https://arxiv.org/pdf/2609.33977)

## 一句话摘要

Semi-structured pruning compresses large language models (LLMs) while keeping a regular sparse structure, but the prevailing N:M pattern fixes the same local sparsity ratio in every layer.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semi-structured pruning compresses large language models (LLMs) while keeping a regular sparse structure, but the prevailing N:M pattern fixes the same local sparsity ratio in every layer. Layer-adaptive sparsity allocation improves unstructured pruning, yet it has been reported to be less effective under N:M sparsity, leaving open whether adaptive allocation is of limited value for semi-structured pruning in general or only under the fine-grained N:M pattern. We examine this question with group-level sparsity, which partitions each weight matrix into regular groups, retains or prunes each group as a whole, and allows each layer's sparsity ratio to vary under a global budget. We propose GroupMask, which generates the group selectors of all layers with a lightweight hypernetwork, relaxes them with a Gumbel-Sigmoid parameterization and a straight-through estimator, and learns them through sparsity-budget regularization and self-distillation while keeping the pretrained weights frozen. On LLaMA-2-7B at 50% sparsity with the same $1\times256$ group size, learned layer-adaptive allocation reduces WikiText-2 perplexity from 10.02 to 8.30 and raises the average zero-shot accuracy from 0.455 to 0.496 relative to a uniform per-layer ratio. GroupMask obtains the lowest WikiText-2 perplexity on LLaMA-2-7B and the highest average zero-shot accuracy with Alpaca calibration among the evaluated baselines on five LLaMA and Qwen models. Our code is available at https://github.com/ZhengaoLi/GroupMask.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhengao Li, Shuoqiu Li, Xiaofang Zhang, Yukai Jin, Gokcen Kestor, Yanfu Zhang, Yiming Zeng, Bin Ren, Chuxu Zhang, Shangqian Gao
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ZhengaoLi/GroupMask](https://github.com/ZhengaoLi/GroupMask)
- 阅读深度：metadata
