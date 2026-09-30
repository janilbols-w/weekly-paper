---
title: "CodeScaler: Scaling Code LLM Training and Test-Time Inference via Reward Models"
description: "Reinforcement Learning from Verifiable Rewards (RLVR) has driven recent progress in code large language models by leveraging execution-based feedback from unit tests, but its scalability is fundamentally constrained by the availability and reliability of high-quality test cases."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2602.17684) · [PDF](https://arxiv.org/pdf/2602.17684)

## 一句话摘要

Reinforcement Learning from Verifiable Rewards (RLVR) has driven recent progress in code large language models by leveraging execution-based feedback from unit tests, but its scalability is fundamentally constrained by the availability and reliability of high-quality test cases.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement Learning from Verifiable Rewards (RLVR) has driven recent progress in code large language models by leveraging execution-based feedback from unit tests, but its scalability is fundamentally constrained by the availability and reliability of high-quality test cases. We propose CodeScaler, a reward model designed to scale both reinforcement learning training and test-time inference for code generation. CodeScaler is trained on carefully curated preference data derived from verified code problems and incorporates syntax-aware code extraction and validity-preserving reward shaping to ensure stable and robust optimization. Across four coding benchmarks, CodeScaler consistently outperforms execution-based RL by +1.55 points on Qwen3-8B-Base and +4.23 points on Qwen3-14B-Base. By further scaling to 44K problems with additional synthetic data, CodeScaler yields +14.64 points improvement over the base model without requiring any test cases. At inference time, CodeScaler serves as an effective test-time scaling method, achieving performance comparable to unit test approaches while providing a 10-fold reduction in latency. Moreover, CodeScaler surpasses existing reward models on RM-Bench not only in the code domain (+3.3 points), but also in general and reasoning domains (+2.7 points on average).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiao Zhu, Xinyu Zhou, Boyu Zhu, Hanxu Hu, Mingzhe Du, Haotian Zhang, Huiming Wang, Zhijiang Guo
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
