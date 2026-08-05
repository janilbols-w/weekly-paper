---
title: "Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training"
description: "Tool-using large language model (LLM) agents produce long, multi-turn trajectories, making gradient-based post-training memory-intensive."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.02391) · [PDF](https://arxiv.org/pdf/2608.02391)

## 一句话摘要

Tool-using large language model (LLM) agents produce long, multi-turn trajectories, making gradient-based post-training memory-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tool-using large language model (LLM) agents produce long, multi-turn trajectories, making gradient-based post-training memory-intensive. Evolution strategies (ES) enable memory-efficient full-parameter post-training without backpropagation and can eventually match the performance of gradient-based reinforcement learning (RL). However, resource-constrained settings typically offer only a few GPUs, so the high GPU-hour requirements of ES translate into prohibitively long training times. To address this, we introduce Cooperative Parameter-subspace Evolution Strategy (CoPES), a cooperative coevolutionary method that decomposes the full parameter space into lower-dimensional subspaces and searches over them cooperatively to improve optimization efficiency. We post-train a Qwen3.5-4B tool-using agent for the math task and evaluate it on five benchmarks of varying difficulty. Under the GPU-hour budget of full-parameter GRPO's best validation checkpoint, CoPES recovers 92% of GRPO's validation-accuracy gain, versus 67% for standard ES, while its theoretical GPU memory requirement is less than one-eighth that of full-parameter GRPO. It consistently outperforms standard ES and LoRA-based GRPO on all evaluated pass@k metrics across the five benchmarks. Additional experiments further show the advantage of CoPES on the question-answering task. These results demonstrate an improved trade-off between memory requirements and training time for agentic LLM post-training under resource constraints. The code is open-sourced in https://github.com/MetaronWang/CoPES

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhiyuan Wang, Shengcai Liu, Jiahao Wu, Ning Lu, Hui Ouyang, Shaofeng Zhang, Haoze Lv, Ke Tang
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MetaronWang/CoPES](https://github.com/MetaronWang/CoPES)
- 阅读深度：metadata
