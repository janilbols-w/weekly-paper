---
title: "Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy Self-Distillation"
description: "Reasoning over text-attributed graphs (TAGs) requires large language models (LLMs) to combine a node's text with evidence distributed across its neighbourhood."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.29588) · [PDF](https://arxiv.org/pdf/2608.29588)

## 一句话摘要

Reasoning over text-attributed graphs (TAGs) requires large language models (LLMs) to combine a node's text with evidence distributed across its neighbourhood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reasoning over text-attributed graphs (TAGs) requires large language models (LLMs) to combine a node's text with evidence distributed across its neighbourhood. Existing methods fix the set of accessible neighbours before generation, forcing reasoning to operate over a static context and preventing the model from acquiring missing evidence during inference. We argue that neighbour selection should itself be part of the reasoning process. To this end, we propose Call Neighbours Yourself (CNY), a framework that enables LLMs to proactively explore graph neighbourhoods through topology-constrained graph-walk actions. Instead of reasoning over a pre-selected neighbour set, CNY exposes lightweight neighbour previews and learns when to expand candidate neighbours for additional evidence. To address the delayed-credit challenge of neighbour exploration, we introduce destination-conditioned on-policy self-distillation, which retrospectively evaluates a selected neighbour after its content is revealed and converts the resulting change in action preference into an action-level training signal. Experiments on standard TAG reasoning benchmarks under a unified raw-text setting show that CNY consistently outperforms fixed-context post-training baselines. Furthermore, the learned exploration policy transfers to unseen graphs and to a graph-level task not encountered during training. Code is available at https://github.com/superallen13/CNY.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yilun Liu, Boyu Luo, Yanran Tang, Ruihong Qiu, Zi Huang
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/superallen13/CNY](https://github.com/superallen13/CNY)
- 阅读深度：metadata
