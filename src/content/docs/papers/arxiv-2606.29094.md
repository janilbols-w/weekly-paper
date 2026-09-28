---
title: "TeDiServe: High SLO Attainment Serving for Diffusion Language Models"
description: "Diffusion language models (DLMs) have recently emerged as a promising alternative to conventional autoregressive language models."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2606.29094) · [PDF](https://arxiv.org/pdf/2606.29094)

## 一句话摘要

Diffusion language models (DLMs) have recently emerged as a promising alternative to conventional autoregressive language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) have recently emerged as a promising alternative to conventional autoregressive language models. By generating multiple tokens in parallel during each denoising step, they offer higher inference throughput while maintaining competitive quality. However, realizing these throughput gains while meeting latency SLOs in a serving system requires addressing challenges introduced by DLMs' unique characteristics. These include navigating the speed-quality tradeoff created by confidence-based denoising, choosing appropriate parallelization levels across model instances under fluctuating load, and coordinating approximate KV caching mechanisms that introduce non-uniform per-step costs. To address these challenges, we present TeDiServe, a cluster-level serving system for DLMs. TeDiServe enables deadline-aware scheduling and adaptive load control through confidence-threshold adjustment, and dynamically reconfigures the cluster by solving a quality-aware optimization problem, while explicitly modeling the step-level heterogeneity introduced by approximate KV caching. Across multiple benchmarks and real-world traces, TeDiServe improves SLO attainment by up to 56.6 percentage points and reduces end-to-end request latency by up to 46\% while incurring less than 1\% accuracy drop.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tzu-Tao Chang, Benjamin Yuanyang Hong, Kiet Pham, Shivaram Venkataraman
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
