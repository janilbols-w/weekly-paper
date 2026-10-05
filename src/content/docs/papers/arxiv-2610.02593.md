---
title: "Fisher-Guided Submodular Data Selection for Continual Pre-Training of Large Language Models"
description: "Data selection is already a central bottleneck in large-language-model training, where web-scale corpora are noisy and token budgets are finite."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.02593) · [PDF](https://arxiv.org/pdf/2610.02593)

## 一句话摘要

Data selection is already a central bottleneck in large-language-model training, where web-scale corpora are noisy and token budgets are finite.

## 为什么值得关注

待编辑增强。

## 摘要原文

Data selection is already a central bottleneck in large-language-model training, where web-scale corpora are noisy and token budgets are finite. In continual pre-training (CPT), it becomes a forgetting-control problem: a poorly chosen target-domain corpus can overwrite capabilities encoded in the pretrained checkpoint. Existing CPT practice either scores candidates with parameter-agnostic scalars such as perplexity, or mitigates forgetting by spending many extra general-domain replay tokens. Neither strategy directly asks how training on a candidate will move the model parameters. We show that loss-based selection causes the post-CPT Fisher diagonal to drift downward on exactly the high-Fisher coordinates the pretrained model had committed to, while leaving low-Fisher coordinates largely untouched. This asymmetry exposes a parameter-space mechanism for catastrophic forgetting. Motivated by this observation, we propose a Fisher-aware CPT selector that decomposes each candidate's gradient into an anchor component, which measures perturbation along committed parameter directions, and a frontier component, which measures update capacity in unconstrained low-Fisher subspaces. We aggregate these signals with a log-determinant submodular objective and optimize it in a single pass using a scalable streaming data selection pipeline. On TinyLlama-1.1B and Llama-3.1-8B CPT over medical data, our selector improves target-domain quality while bounding forgetting on held-out pretraining benchmarks. Most importantly, it is substantially more token-efficient than forgetting-aware replay. 1B selected tokens already outperform the replay strategy trained with 10B tokens on both adaptation and forgetting, giving a 10x token-efficiency advantage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhenghao Zhao, Gaowen Liu, Zhiling Lan, Yan Yan
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
