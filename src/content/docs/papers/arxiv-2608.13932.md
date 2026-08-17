---
title: "Post-training Quantization for Hybrid Iterative Generative Models"
description: "Iterative Generative Models (IGMs) span autoregressive and diffusion paradigms, and hybrid variants that couple them can achieve remarkable image-generation fidelity."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.13932) · [PDF](https://arxiv.org/pdf/2608.13932)

## 一句话摘要

Iterative Generative Models (IGMs) span autoregressive and diffusion paradigms, and hybrid variants that couple them can achieve remarkable image-generation fidelity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Iterative Generative Models (IGMs) span autoregressive and diffusion paradigms, and hybrid variants that couple them can achieve remarkable image-generation fidelity. However, their iterative inference incurs substantial computational overhead, making Post-training Quantization (PTQ) appealing for acceleration, while directly applying vanilla PTQ to hybrid IGMs can trigger model collapse. By analyzing these failures, we identify two critical challenges: Excessive Outliers (EOs) in the activations create an irreconcilable trade-off between preserving normal precision and covering EOs, resulting in severe degradation in generation quality; Amplified Anomalies (AAs) arising unpredictably from minor quantization errors, create a mismatch between calibration and inference, thus iteratively triggering model collapse. To address these challenges, we introduce HyGenQ, a PTQ framework for hybrid IGMs. HyGenQ comprises Hierarchical Cluster Decoupling (HCD) and Scaling Recalibration (SR). HCD identifies and decouples outlier channels via a multi-stage clustering process, effectively isolating EOs while maintaining normal value precision, thereby alleviating performance degradation. SR scales AAs beyond Gaussian Bound, thereby avoiding model collapse caused by aggressive truncation. Extensive experiments demonstrate that HyGenQ successfully quantizes representative hybrid IGMs to 8-bit precision (W8A8), significantly outperforming existing baselines and validating its robustness across different model families.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jing Gao, Junyi Wu, Wei Wang, Yan Yan, Yao Zhao
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
