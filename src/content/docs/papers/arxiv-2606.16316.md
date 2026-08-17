---
title: "RL-Index: Reinforcement Learning for Retrieval Index Reasoning"
description: "Retrieving external knowledge is crucial for real-world tasks but remains difficult when queries and relevant knowledge are linked by implicit reasoning (e.g., shared theorems or coding logic)."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2606.16316) · [PDF](https://arxiv.org/pdf/2606.16316)

## 一句话摘要

Retrieving external knowledge is crucial for real-world tasks but remains difficult when queries and relevant knowledge are linked by implicit reasoning (e.g., shared theorems or coding logic).

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieving external knowledge is crucial for real-world tasks but remains difficult when queries and relevant knowledge are linked by implicit reasoning (e.g., shared theorems or coding logic). Existing methods rely mainly on query-side reasoning, leading to high online latency and underutilizing the reasoning semantics within the knowledge corpus. In this paper, we propose $\textbf{RL-Index}$, an indexing framework that formulates retrieval index reasoning as a reinforcement learning problem. Instead of performing reasoning at query time, RL-Index shifts reasoning to the indexing stage by augmenting documents with LLM-generated rationales that explicitly encode the latent query-knowledge relationship. To optimize the quality of these rationales, we employ Group Relative Policy Optimization (GRPO) and use retrieval similarity as a proxy reward signal, enabling direct optimization of indexing decisions for retrieval effectiveness. Extensive experiments on the BRIGHT benchmark demonstrate that RL-Index consistently improves both retrieval and downstream question-answering performance, while significantly reducing online inference latency. Moreover, the learned rationale augmentation generalizes across diverse retrievers and generators, highlighting its robustness as a plug-and-play indexing strategy across different retrieval systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: online inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yongjia Lei, Nedim Lipka, Zhisheng Qi, Utkarsh Sahu, Yuchen Zhuang, Wenqi Shi, Koustava Goswami, Franck Dernoncourt, Ryan A. Rossi, Yu Wang
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
