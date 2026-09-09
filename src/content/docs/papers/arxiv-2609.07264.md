---
title: "Dense Structural Compression of Transformers via Gauge-Correct Channel Removal"
description: "Inference energy per token drives the cost and carbon footprint of deployed transformers."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.07264) · [PDF](https://arxiv.org/pdf/2609.07264)

## 一句话摘要

Inference energy per token drives the cost and carbon footprint of deployed transformers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference energy per token drives the cost and carbon footprint of deployed transformers. It is dominated by dense matrix products that incur fused multiply-accumulate (FMA) operations and memory traffic. To reduce these computations while retaining dense tensors for high GPU throughput, we develop a methodology from first principles to adapt structural complexity during training to maximize inference utility per unit compute. Channel penalties drive entire tensor slices to zero to enable physical removal while preserving density and the network function. The natural approach, penalizing the norm of operator components acting through each channel, is provably destabilized by gauge freedom. We resolve this pathology with GaugeLasso: additive symmetric group-lasso penalties that recover a monotone function of product-norms when the network converges to gauge balance. Our equilibrium analysis enables per-channel calibration to correctly suppress slices that under-perform in inference utility per unit compute. Under adaptive pressure, the network reorganizes into depth-dependent structural profiles that can be far smaller than the architecture required to learn the task. On polynomial long division over $\mathbb{F}_{31}$, compute compresses from 148 to 255 times with perfect accuracy. On character-level language modeling, compressed models outperform the hand-designed baseline at equal FMA. On masked autoencoding, a compression trial exposes which axes were over-provisioned and which saturated, guiding a better second design. Compaction also accelerates training monotonically as the model progresses. Post-hoc pruning with the same utility ranking cannot reach these structures, showing that sustained pressure is central to discovery of efficient models. Retraining a discovered architecture recovers baseline quality on our statistical tasks, but fails on our exact algorithmic task.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jed A. Duersch, Na\"im Es-Sebbani, Nathana\"el Haas, Zied Bouraoui
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
