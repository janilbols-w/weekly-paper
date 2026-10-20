---
title: "Mechanism-Aligned Observability for Training Instability of Large Language Models"
description: "Frontier large language model training consumes massive accelerator fleets over long wall-clock times, making stability failures extremely costly."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2606.28116) · [PDF](https://arxiv.org/pdf/2606.28116)

## 一句话摘要

Frontier large language model training consumes massive accelerator fleets over long wall-clock times, making stability failures extremely costly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Frontier large language model training consumes massive accelerator fleets over long wall-clock times, making stability failures extremely costly. However, global symptoms such as loss divergences often emerge only after the underlying fault has already affected the training dynamics, further increasing the sunk compute. In which internal representation can a training fault become persistently and interpretably observable before it appears in global training metrics? We propose a mechanism-aligned principle for training observability: identify the internal state into which a fault is persistently written, derive the structure induced by its mechanism, and construct monitors in representations aligned with the computation of the affected module. For FlashAttention, we show that biased backward errors accumulate into a persistent low-dimensional structure in weight updates, producing spectral concentration. For MoE routers, we characterize routing dynamics through per-token routing behavior rather than parameter similarity, which may change without altering the routing function. Experiments show that the two monitors respond selectively to changes in their corresponding modules, before degradation becomes visible in global training metrics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruixuan Huang, Yipei Wang, Wenyi Fang, Hantao Huang, Ansheng You, Shuai Wang, Fan Wu, Yang Zheng
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
