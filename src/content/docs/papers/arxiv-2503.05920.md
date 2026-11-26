---
title: "On the Efficiency of Structured Pruning in Small Language Model Pretraining"
description: "Companies that deploy generative language models on edge devices often need to train small models from scratch due to legal, data-governance, or product-customization requirements."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2503.05920) · [PDF](https://arxiv.org/pdf/2503.05920)

## 一句话摘要

Companies that deploy generative language models on edge devices often need to train small models from scratch due to legal, data-governance, or product-customization requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Companies that deploy generative language models on edge devices often need to train small models from scratch due to legal, data-governance, or product-customization requirements. An alternative approach is to train an enlarged model and compress it to the target size via structured pruning, but this advantage becomes unclear once the cost of pretraining the enlarged model is included. We introduce the enlarge-and-prune framework to study this question under full-cost accounting, and show that conventional enlarge-and-prune pipelines -- which train the enlarged model, prune it, and recover in separate stages -- do not consistently outperform direct small-model training under the same total token budget. To overcome this limitation, we propose IDEA Prune, an integrated enlarge-and-prune pipeline that unifies enlarged model pretraining, iterative structured pruning, and recovery under a single cosine annealing learning rate schedule. In controlled experiments compressing 2.8B models to 1.3B with up to 2T tokens on the same dataset, IDEA Prune consistently outperforms conventional pipelines and modestly improves overall performance relative to the scratch baseline, improving MMLU accuracy to 46.4%, compared with 31.4-33.4% for conventional pipelines. These advantages are preserved after downstream supervised fine-tuning, where IDEA Prune matches or outperforms all baselines of the same size on instruction following, math reasoning, and code generation. Our analysis further reveals that intermediate checkpoints provide more favorable pruning starting points than fully converged ones, and that an enlargement factor of approximately 2.6x yields the best pruned models in the tested regime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yixiao Li, Xianzhi Du, Ajay Jaiswal, Tao Lei, Tuo Zhao, Chong Wang, Jianyu Wang
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
