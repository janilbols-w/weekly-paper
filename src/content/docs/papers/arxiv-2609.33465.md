---
title: "GSM: Efficient Language Modeling with Shared Global State"
description: "Improving language model efficiency requires not only cheaper operations but also eliminating redundant computation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.33465) · [PDF](https://arxiv.org/pdf/2609.33465)

## 一句话摘要

Improving language model efficiency requires not only cheaper operations but also eliminating redundant computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Improving language model efficiency requires not only cheaper operations but also eliminating redundant computation. We argue that effective modeling requires information accessibility and computational depth, but not repeated historical retrieval across layers. Guided by this principle, we introduce the Global State Model (GSM), a causal encoder--decoder architecture that separates historical information acquisition from deep computation. The encoder progressively aggregates long-range information through multi-stage sparse retrieval into a fixed-size shared state, while decoder layers perform successive transformations over this state without repeated historical access. This design makes decoder attention and cache costs independent of history length, while dependency-aware pruning further reduces prefill computation. Experiments across multiple model scales show that GSM achieves downstream performance comparable to matched DeepSeek-V4.1-Flash-based baselines, with improvements at some scales, while preserving long-context retrieval capabilities. GSM also improves training and inference throughput and reduces cache overhead. These results demonstrate that eliminating architectural redundancy offers an effective path toward efficient language modeling without sacrificing information accessibility or computational depth.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yunao Zheng, Bin Wen, Xiaojie Wang, Kaiyu Jiang, Xuanyu Zheng, Changyi Liu, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Jiankang Chen, Xu Wang, Tingting Gao, Han Li
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
