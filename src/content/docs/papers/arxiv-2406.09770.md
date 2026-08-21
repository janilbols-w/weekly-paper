---
title: "Towards Efficient Pareto Set Approximation via Mixture of Experts Based Model Fusion"
description: "Solving multi-objective optimization problems for large deep neural networks is a challenging task due to the complexity of the loss landscape and the expensive computational cost of training and evaluating models."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2406.09770) · [PDF](https://arxiv.org/pdf/2406.09770)

## 一句话摘要

Solving multi-objective optimization problems for large deep neural networks is a challenging task due to the complexity of the loss landscape and the expensive computational cost of training and evaluating models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Solving multi-objective optimization problems for large deep neural networks is a challenging task due to the complexity of the loss landscape and the expensive computational cost of training and evaluating models. Efficient Pareto front approximation of large models enables multi-objective optimization for various tasks such as multi-task learning and trade-off analysis. Existing algorithms for learning Pareto set, including (1) evolutionary, hypernetworks, and hypervolume-maximization methods, are computationally expensive and have restricted scalability to large models; (2) Scalarization algorithms, where a separate model is trained for each objective ray, which is inefficient for learning the entire Pareto set and fails to capture the objective trade-offs effectively. Inspired by the recent success of model merging, we propose a practical and scalable approach to Pareto set learning problem via mixture of experts (MoE) based model fusion. By ensembling the weights of specialized single-task models, the MoE module can effectively capture the trade-offs between multiple objectives and closely approximate the entire Pareto set of large neural networks. Once the routers are learned and a preference vector is set, the MoE module can be unloaded, thus no additional computational cost is introduced during inference. We conduct extensive experiments on vision and language tasks using large-scale models such as CLIP-ViT and GPT-2. The experimental results demonstrate that our method efficiently approximates the entire Pareto front of large models. Using only hundreds of trainable parameters of the MoE routers, our method even has lower memory usage compared to linear scalarization and algorithms that learn a single Pareto optimal solution, and are scalable to both the number of objectives and the size of the model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anke Tang, Li Shen, Yong Luo, Shiwei Liu, Han Hu, Bo Du, Dacheng Tao
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
