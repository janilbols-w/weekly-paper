---
title: "TIDE: Temporal Incremental Draft Engine for Self-Improving LLM Inference"
description: "Speculative decoding can substantially accelerate LLM inference, but realizing its benefits in practice is challenging due to evolving workloads."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2602.05145) · [PDF](https://arxiv.org/pdf/2602.05145)

## 一句话摘要

Speculative decoding can substantially accelerate LLM inference, but realizing its benefits in practice is challenging due to evolving workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding can substantially accelerate LLM inference, but realizing its benefits in practice is challenging due to evolving workloads. We present TIDE (Temporal Incremental Draft Engine), a serving-engine-native framework that integrates online draft adaptation directly into high-performance LLM inference systems. TIDE reuses target model's intermediate hidden states generated during inference as training signals for draft adaptation, thereby avoiding additional target model computation and serving-time overhead. It employs adaptive runtime control to activate speculation and draft model training only when beneficial. TIDE exploits heterogeneous clusters by mapping inference and training to appropriate GPU classes. Across diverse real-world workloads, TIDE achieves up to 1.66$\times$ throughput over no-speculation baselines while recovering performance on misaligned workloads where static draft models degrade throughput. TIDE also reduces training time by up to 3.02$\times$ and storage requirements by 24$\times$ compared to existing draft training approaches, and improves system throughput by up to 1.22$\times$ on heterogeneous GPU clusters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiyoung Park, Hankyu Jang, Changseok Song, Wookeun Jung
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
