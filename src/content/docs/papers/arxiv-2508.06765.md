---
title: "Efficient Collaborative LLM Fine-Tuning over Heterogeneous Mobile Devices via Many Backbones to One Side-Network Tuning"
description: "Collaboratively fine-tuning (FT) large language models (LLMs) over heterogeneous mobile devices fosters immense potential applications of personalized intelligence."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2508.06765) · [PDF](https://arxiv.org/pdf/2508.06765)

## 一句话摘要

Collaboratively fine-tuning (FT) large language models (LLMs) over heterogeneous mobile devices fosters immense potential applications of personalized intelligence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collaboratively fine-tuning (FT) large language models (LLMs) over heterogeneous mobile devices fosters immense potential applications of personalized intelligence. However, such a vision faces critical system challenges. Existing federated LLM fine-tuning approaches remain limited by prohibitive on-device resource overhead, straggler-prone synchronous aggregation, and the assumption of a unified pretrained backbone across heterogeneous devices. In this paper, we propose EC-MobiLLM, a novel design for efficient collaborative LLM fine-tuning across heterogeneous mobile devices and heterogeneous backbones. EC-MobiLLM adopts a server-assisted side-tuning paradigm to minimize on-device overhead and pioneers non-blocking asynchronous collaboration to accelerate training. Moreover, EC-MobiLLM introduces adaptive feature alignment to support collaboration across heterogeneous backbones, aligning with practical needs in real-world deployments. Extensive experimental results demonstrate that EC-MobiLLM can maintain robust fine-tuning performance while achieving extremely low on-device memory, with at least 95.2\% reduction in computation overhead, 93.2\% reduction in communication costs and $5.1\times$ faster convergence compared to existing methods, validating its efficacy for practical LLM adaptation over heterogeneous mobile devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: straggler
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingke Yang, Liang Li, Sicong Li, Liwei Guan, Hao Wang, Xiaoqi Qi, Jiang Liu, Xin Fu, Miao Pan
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
