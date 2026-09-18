---
title: "Privacy-enhanced federated learning via asynchronous aggregation and local differential perturbation"
description: "This study proposes a privacy-enhanced federated learning framework to address secure collaborative training in distributed data environments."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.15885) · [PDF](https://arxiv.org/pdf/2609.15885)

## 一句话摘要

This study proposes a privacy-enhanced federated learning framework to address secure collaborative training in distributed data environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

This study proposes a privacy-enhanced federated learning framework to address secure collaborative training in distributed data environments. The framework integrates Dynamic Differential Privacy (DDP), lightweight Homomorphic Encryption (HE), and Local Differential Privacy (LDP) mechanisms to ensure data privacy protection during model training. Additionally, the framework employs an asynchronous aggregation strategy with version control to support distributed training in asynchronous environments. Experimental validation on the CIFAR-10 and Purchase-100 benchmark datasets demonstrates that the method maintains high classification accuracy (up to 82.6%) even under stringent privacy constraints ({\epsilon} = 0.1), while reducing communication overhead by 21.3% compared to FedAvg. Experimental results demonstrate that this framework effectively balances privacy protection and model performance in distributed machine learning scenarios, providing a scalable technical foundation for large-scale distributed collaborative computing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhen Zhong, Shini Yang, Liesheng Wei
- 发布：2026-09-14；更新：2026-09-15
- 来源：arXiv RSS；Venue：Proc. SPIE 14128, Third International Conference on Big Data, Computational Intelligence, and Applications (BDCIA 2025), 141283L (2026)
- 代码：未发现
- 阅读深度：metadata
