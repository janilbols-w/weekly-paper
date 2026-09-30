---
title: "X-MoD: Practical Scaling Laws for Sparse-Depth Routing Beyond Mixture-of-Depths"
description: "Mixture-of-Depths (MoD) enables conditional computation across Transformer depth by routing only a subset of tokens through selected layers, but its original one-sparse--one-dense alternation tightly couples total capacity to active capacity and limits sparse-depth scaling."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.34212) · [PDF](https://arxiv.org/pdf/2609.34212)

## 一句话摘要

Mixture-of-Depths (MoD) enables conditional computation across Transformer depth by routing only a subset of tokens through selected layers, but its original one-sparse--one-dense alternation tightly couples total capacity to active capacity and limits sparse-depth scaling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Depths (MoD) enables conditional computation across Transformer depth by routing only a subset of tokens through selected layers, but its original one-sparse--one-dense alternation tightly couples total capacity to active capacity and limits sparse-depth scaling. We introduce X-MoD, a scalable sparse-depth architecture that decouples token sparsity from anchor stride, allowing total parameter count to grow while keeping active-equivalent capacity nearly fixed. To make deep sparse routing trainable, X-MoD combines dense anchors with variance-scaled layer-wise gating and depth-wise token balancing. To make this regime analyzable and usable, we formulate sparse-depth routing as a conditional architecture-design problem: given compute, context length, and active-equivalent backbone size, how should the routing configuration be chosen? We develop a practical scaling-law framework by fitting X-MoD relative to FLOP-matched dense baselines, yielding an interpretable law that decomposes performance into sparse-capacity gain, sparse-context correction, and anchor-stride interaction. The law predicts validation loss across routing configurations and reveals how context length, model scale, and anchor stride shape sparse-depth performance. We validate the architecture and law through pretraining sweeps, held-out scaling-law prediction, ablations, downstream evaluations, and comparisons with Dense, MoD, and representative MoE baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bowen Dong, Yilong Fan, Tengyu Pan, Yike Zhang, Zhenyu Li, Zijian Zhang, Xuewei Li, Mei Yu, Jianyong Wang
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
