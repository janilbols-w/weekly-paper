---
title: "CAFE: Conducting-Cell-Aware Adaptive Differential Encoding for Robust DNN Inference in FeFET-Based Compute-in-Memory"
description: "Ferroelectric field-effect transistor (FeFET)-based compute-in-memory (CIM) promises energy-efficient deep neural network (DNN) inference, but device variation can severely degrade bit-sliced CIM accuracy."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.19697) · [PDF](https://arxiv.org/pdf/2610.19697)

## 一句话摘要

Ferroelectric field-effect transistor (FeFET)-based compute-in-memory (CIM) promises energy-efficient deep neural network (DNN) inference, but device variation can severely degrade bit-sliced CIM accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ferroelectric field-effect transistor (FeFET)-based compute-in-memory (CIM) promises energy-efficient deep neural network (DNN) inference, but device variation can severely degrade bit-sliced CIM accuracy. Prior works either rely on hardware modifications or treat such variation as generic noise, overlooking a key FeFET asymmetry: negligible off-state leakage makes errors dominated by conducting on-state cells. This asymmetry is amplified by two's-complement sign extension, which maps small negative values to high-significance bit slices and magnifies their errors during shift-and-add reconstruction. In this paper, we propose CAFE, a conducting-cell-aware adaptive differential encoding framework built upon this FeFET-specific asymmetry. CAFE introduces C$^2$AM, a bit-significance-weighted conducting-cell activity metric that predicts output deviation and inference accuracy degradation under FeFET device variation. Guided by C$^2$AM, CAFE applies differential weight and activation encoding to eliminate sign-extension-induced conducting-cell amplification. To balance robustness and cost, CAFE performs type-wise encoding enumeration, layer-wise NSGA-II search, and post-GA pruning to allocate robust encodings where the robustness-cost trade-off is favorable. Across representative vision and language workloads, CAFE reduces C$^2$AM by up to $28.6\times$; in the main deployment study, it improves accuracy over two's-complement CIM by more than 87 percentage points and approaches full-differential robustness at $1.86$-$2.78\times$ normalized cost, compared with $3.06\times$ for uniform full-differential encoding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wenshuai Yao, Wenyong Zhou, Hanyong Shao, Zhiyuan Ning, Ru Huang, Kechao Tang
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
