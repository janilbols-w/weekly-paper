---
title: "DART-ES: Difficulty-Aware Reweighting and Targeted Replay for Fine-Tuning LLMs with Evolution Strategies"
description: "Evolution Strategies (ES) enable memory efficient full parameter fine-tuning of large language models (LLMs) using only forward computation."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.06993) · [PDF](https://arxiv.org/pdf/2610.06993)

## 一句话摘要

Evolution Strategies (ES) enable memory efficient full parameter fine-tuning of large language models (LLMs) using only forward computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Evolution Strategies (ES) enable memory efficient full parameter fine-tuning of large language models (LLMs) using only forward computation. However, standard ES uniformly averages rewards across problems and compresses problem level population feedback into a single scalar, making it difficult to capture how the learning value of each problem changes with model capability. To address this limitation, we propose Difficulty-Aware Reweighting and Targeted Replay for Evolution Strategies (DART-ES). DART-ES estimates the local solvability of each problem from its pass rate across the perturbation population and aggregates historical observations to construct a dynamic difficulty state. This shared state jointly guides continuous difficulty reweighting and rare solvable sample replay, thereby improving perturbation direction evaluation and training data allocation without introducing an additional difficulty model or backpropagation. Extensive experiments show that DART-ES achieves good fine-tuning performance. DART-ES outperforms ES on all five base models and improves the average accuracy from 72.07\% to 73.53\%, exceeding the 73.26\% achieved by GRPO on GSM8K. Across five challenging mathematical reasoning benchmarks, DART-ES achieves an average accuracy of 49.20\%, compared with 48.34\% for ES and remains competitive with strong 7B models trained with RL. Further experiments show consistent gains in instruction tuning, code generation and the Countdown task with a 14B model, demonstrating strong generalization across tasks and scalability to larger models. Beyond performance gains, DART-ES also shows clear advantages in system efficiency. It reduces runtime per step by 15.2\%--50.2\% and peak memory usage per GPU by 21.1\%--51.1\% compared with GRPO. Despite performing full parameter fine-tuning, DART-ES also requires less runtime and GPU memory than GRPO+LoRA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhishen Sun, Hongzhan Wang, Sizhe Dang, Guang Dai, Haishan Ye
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
