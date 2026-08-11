---
title: "RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents"
description: "Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.04713) · [PDF](https://arxiv.org/pdf/2607.04713)

## 一句话摘要

Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of signals and the lack of fine-grained feedback. Furthermore, the model may fail to learn successful trajectories that are not sampled during training, thereby limiting its performance. Conversely, while employing customized dense process rewards provides richer signals and accelerates convergence, these surrogate rewards may exhibit potential misalignment with the ground-truth outcome rewards. This inconsistency can bias the training direction and ultimately degrade the model's final performance. In this work, we propose Reward-Swap Policy Optimization (RSPO), a method designed to leverage the rich information from dense process rewards to facilitate training with outcome rewards. By utilizing a reward-swap mechanism, RSPO ensures the diversity of sampled trajectories while guaranteeing consistency between the optimization objective and the true outcome rewards, thereby elevating the performance ceiling of the model. We conduct extensive experiments on two challenging agent benchmarks, WebShop and ALFWorld. By applying our method to various reinforcement learning algorithms, including GRPO, PPO, and GiGPO, we demonstrate that RSPO achieves consistent performance improvements across different baselines and benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiang Liu, Taian Guo, Ruizhi Qiao, Xing Sun
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
