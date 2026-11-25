---
title: "Specialized Large Language Models for Markovian Reasoning: Structural Cache Compression, Transition Pretraining, and Dual-Loop Transformers"
description: "Standard autoregressive large language models attend to the growing history of generated tokens, making the key-value (KV) cache a central memory and throughput bottleneck in long-chain reasoning and multi-branch sampling."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.28285) · [PDF](https://arxiv.org/pdf/2611.28285)

## 一句话摘要

Standard autoregressive large language models attend to the growing history of generated tokens, making the key-value (KV) cache a central memory and throughput bottleneck in long-chain reasoning and multi-branch sampling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Standard autoregressive large language models attend to the growing history of generated tokens, making the key-value (KV) cache a central memory and throughput bottleneck in long-chain reasoning and multi-branch sampling. Yet an important class of reasoning problems is naturally first-order Markovian: the next step depends on a sufficient representation of the current state, rather than on the raw sequence of all earlier steps. We develop a unified design paradigm for Markovian-reasoning specialized large language models. At the cache level, the Markovian state interface transforms history-dependent KV storage into constant-size state transfer with respect to the number of reasoning steps. At the learning level, we reformulate long-chain prediction as independently trainable one-step transition objectives, with explicit state bottlenecks, distillation, invariance, and drift-consistency losses. At the architectural level, we introduce a dual-loop Transformer: an outer loop advances the reasoning state, while an inner recurrent-depth loop allocates adaptive computation to each transition through shared weights and explicit memory tokens or recurrent matrix states. We connect this architecture to a three-region cache, step-relative positions, truncated backpropagation, branch-aware checkpoints, and a transition-centric evaluation protocol. The organizing principle is simple: the optimal reasoning system need not remember everything; it must carry forward exactly what the future needs. This principle opens a path toward specialized reasoning engines whose memory footprint is decoupled from reasoning-chain length.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haibin Tong, Liangliang Xin, Yamei Zhu, Jiang Yu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
