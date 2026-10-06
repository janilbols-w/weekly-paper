---
title: "EfficientXpert: Efficient Domain Adaptation for Large Language Models via Propagation-Aware Pruning"
description: "Deploying domain-specialized large language models on resource-constrained hardware motivates reducing both adaptation cost and the number of retained weights."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.19935) · [PDF](https://arxiv.org/pdf/2511.19935)

## 一句话摘要

Deploying domain-specialized large language models on resource-constrained hardware motivates reducing both adaptation cost and the number of retained weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying domain-specialized large language models on resource-constrained hardware motivates reducing both adaptation cost and the number of retained weights. LoRA lowers adaptation cost but leaves a dense backbone, while separate pruning can discard weights that become important during adaptation. We propose EfficientXpert, a framework that co-adapts low-rank updates and sparse support. Its ForeSight Mask scores weights through a downstream reconstruction surrogate using the evolving LoRA-augmented weights; Partial Brain Surgeon (PBS) realigns the adapter through a closed-form correction. At 40% sparsity, the strongest variant retains 98.55--108.99% of dense-LoRA aggregate performance across the evaluated LLaMA settings. On Qwen3-8B, adaptation adds 17.9--27.0% training time and at most 4.8% peak GPU memory. Our analysis connects the domain- and rank-dependent effects of PBS to its constrained reconstruction objective, providing guidance for selecting adapter recovery capacity. Together, these results demonstrate efficient production of sparse, domain-specialized experts. Code is available at https://github.com/TagoreZhao/Efficient_Domain_Adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Songlin Zhao, Michael Pitts, Zhuwei Qin
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/TagoreZhao/Efficient_Domain_Adaptation](https://github.com/TagoreZhao/Efficient_Domain_Adaptation)
- 阅读深度：metadata
