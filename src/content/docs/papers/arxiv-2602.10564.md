---
title: "SplitCom: Communication-efficient Split Federated Fine-tuning of LLMs via Temporal Compression"
description: "Federated fine-tuning of on-device large language models (LLMs) mitigates privacy concerns by preventing raw data sharing."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2602.10564) · [PDF](https://arxiv.org/pdf/2602.10564)

## 一句话摘要

Federated fine-tuning of on-device large language models (LLMs) mitigates privacy concerns by preventing raw data sharing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Federated fine-tuning of on-device large language models (LLMs) mitigates privacy concerns by preventing raw data sharing. However, the intensive computational and memory demands pose significant challenges for resource-constrained edge devices. To overcome these limitations, split federated learning (SFL) emerges as a promising solution that partitions the model into lightweight client-side and compute-intensive server-side sub-models, thus offloading the primary training workload to a powerful server. Nevertheless, the high-dimensional activation exchanges in SFL lead to excessive communication overhead. To overcome this, we propose SplitCom, a communication-efficient SFL framework for LLMs that exploits temporal redundancy in activations across consecutive training epochs. Inspired by video compression, the core innovation of our framework lies in selective activation uploading only when a noticeable deviation from previous epochs occurs. To balance communication efficiency and learning performance, we introduce two adaptive threshold control schemes based on 1) bang-bang control or 2) deep deterministic policy gradient (DDPG)-based reinforcement learning. Moreover, we implement dimensionality reduction techniques to alleviate client-side memory requirements. Furthermore, we extend SplitCom to the U-shape architecture, ensuring the server never accesses clients' labels. Extensive simulations and laboratory experiments demonstrate that SplitCom reduces uplink communication costs by up to 98.8\,\% in its standard configuration and total communication costs by up to 95.8\,\% in its U-shape variant without noticeably compromising model performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tao Li, Yulin Tang, Yiyang Song, Cong Wu, Xihui Liu, Pan Li, Xianhao Chen
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
