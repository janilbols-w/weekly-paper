---
title: "LOOP: Recovery-Aligned Iterative Layer Pruning via On-Policy Distillation"
description: "Layer-level pruning is attractive for large language model (LLM) deployment as it reduces the model size while preserving a dense architecture that can be efficiently executed on standard hardware."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.25679) · [PDF](https://arxiv.org/pdf/2610.25679)

## 一句话摘要

Layer-level pruning is attractive for large language model (LLM) deployment as it reduces the model size while preserving a dense architecture that can be efficiently executed on standard hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Layer-level pruning is attractive for large language model (LLM) deployment as it reduces the model size while preserving a dense architecture that can be efficiently executed on standard hardware. Current methods typically follow a one-shot paradigm, which first removes selected layers to reach a target model size and then performs additional training to recover model capabilities. However, pruning directly to the target size can substantially degrade reasoning capabilities, making subsequent recovery more difficult under a limited training budget. Moreover, this paradigm separates layer selection from recovery, limiting the use of recovery information to guide selection and potentially hindering the recovery of reasoning capabilities. To address these limitations, we propose LOOP, a Layer-level Recovery-Oriented On-Policy Pruning framework that interleaves pruning and recovery across multiple shots. In each shot, LOOP removes a single layer and performs short on-policy distillation, mitigating the abrupt degradation in reasoning capabilities associated with one-shot pruning. To guide layer selection in subsequent shots, LOOP reuses on-policy trajectories and optimization signals from recovery to jointly assess each remaining layer's reasoning contribution and recovery sensitivity, thereby making layer selection recovery-aware. Evaluations on several benchmarks show that LOOP consistently outperforms one-shot baselines in average accuracy across different model scales and pruning ratios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liang Xu, Shufan Shen, Zhongni Hou, Yufei Zhang, Wei Lin, Guojun Yin, Shuhui Wang
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
