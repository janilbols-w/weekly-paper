---
title: "Empowering Credit Risk Detection in Weixin Pay with Billion-Scale Deep Graph Learning"
description: "Credit risk detection, particularly mitigating individual fraud, is crucial for maintaining the stability of digital financial ecosystems."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.02168) · [PDF](https://arxiv.org/pdf/2608.02168)

## 一句话摘要

Credit risk detection, particularly mitigating individual fraud, is crucial for maintaining the stability of digital financial ecosystems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Credit risk detection, particularly mitigating individual fraud, is crucial for maintaining the stability of digital financial ecosystems. Accurately identifying credit fraud among billions of users is critical for minimizing financial losses and safeguarding the sustainability of inclusive financial services. Given that credit fraud risks are often concealed within heterogeneous user-risk graphs, Graph Neural Networks (GNNs) have emerged as an effective tool for risk mining by capturing complex dependencies. To address the scalability bottleneck of industrial GNNs, distributed training based on subgraphs is indispensable. However, existing strategies often compromise topological integrity for load balancing. This can be catastrophic for risk detection, as it indiscriminately severs the long-tail evidence chains essential for risk propagation. Overlapping subgraphs can restore severed risk contexts but inevitably introduce redundancy and noise, while overlooking the representation alignment across different local subgraphs. In this paper, we propose a risk-aware overlapping subgraph learning framework for large-scale credit risk detection. We first construct base partitions to ensure load balance. Then, we perform budget-constrained sampling that selects informative long-tail nodes, thereby preserving critical risk diffusion patterns while filtering out noise. To mitigate representation inconsistency, we design a cross-subgraph consistency alignment mechanism. By enforcing alignment constraints on the overlapping nodes, we harmonize the local representations into a globally consistent latent space. Extensive experiments on Weixin Pay's production dataset demonstrate that our model significantly outperforms existing strategies for risk detection, offering a scalable and effective solution for industrial graph learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xin Liu, Xiyuan Chen, Chenglong Wu, Xuan Zong, Jun Zhou, Dawei Cheng
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
