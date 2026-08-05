---
title: "Pruning-Aware Multi-Cluster Co-Inference for Large AI Models in AI-RANs"
description: "The increasing scale and computational demands of large artificial intelligence models (LAIMs) present significant challenges for efficient inference in resource-constrained distributed environments."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03026) · [PDF](https://arxiv.org/pdf/2608.03026)

## 一句话摘要

The increasing scale and computational demands of large artificial intelligence models (LAIMs) present significant challenges for efficient inference in resource-constrained distributed environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

The increasing scale and computational demands of large artificial intelligence models (LAIMs) present significant challenges for efficient inference in resource-constrained distributed environments. In this paper, we propose a multi-cluster LAIM co-inference framework, where an edge server equipped with multiple graphics processing units (GPUs) coordinates multiple user clusters to execute inference tasks collaboratively. Within each cluster, devices capture data from diverse perspectives and employ lightweight on-device LAIMs to extract local features. These features are then transmitted to the edge server, where they are aggregated and fused to generate a more accurate inference outcome. To reveal the fundamental trade-off between model pruning and collaborative inference performance, we develop a theoretical framework that characterizes the impact of pruning ratios and device contributions using rate-distortion theory and partial information decomposition. Based on this analysis, we formulate a joint optimization problem that determines the model pruning ratio, the task scheduling strategy, the bandwidth allocation, and the transmission power, with the goal of minimizing the inference distortion while satisfying the constraints of latency, energy consumption, and server capacity. Extensive simulation results demonstrate that the proposed framework significantly outperforms existing benchmark schemes, achieving superior inference accuracy and resource efficiency in multi-cluster edge intelligence networks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaowen Cao, Zhonghao Lyu, Shicheng Chu, Zezhong Zhang, Dingzhu Wen, Guangxu Zhu, Kaibin Huang, Shuguang Cui, Jie Xu
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
