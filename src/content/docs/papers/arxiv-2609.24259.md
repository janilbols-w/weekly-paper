---
title: "MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents"
description: "The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.24259) · [PDF](https://arxiv.org/pdf/2609.24259)

## 一句话摘要

The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response.

## 为什么值得关注

待编辑增强。

## 摘要原文

The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory appropriately. They frequently over-use or under-use memory rather than matching each proposition's actual use to its target level, leading to biased, low-quality responses. Experiments with common post-training algorithms, including group relative policy optimization and on-policy self-distillation, further reveal a clear directional skew: trained models improve in one direction while deteriorating in the other. We therefore propose MemCalib-RL, an ordered bidirectional counterfactual credit-assignment algorithm that separates over- and under-use signals and localizes their credit to response tokens through exact atom ablation. Results across model families and scales (Qwen3-8B, Ministral-3-8B-Instruct, and Qwen3.5-35B-A3B) show that MemCalib-RL achieves the best overall performance while better balancing over-use and under-use, with gains generalizing beyond MemCalib in external benchmark evaluation. Further experiments support its design choices and robustness and provide insight into its training dynamics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruike Cao, Fanyu Zhao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, Yifei Zhao, Han Zhang, Li Xiao
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
