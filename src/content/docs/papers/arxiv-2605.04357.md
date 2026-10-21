---
title: "Coral: Cost-Efficient Multi-LLM Serving over Heterogeneous Cloud GPUs"
description: "The landscape of large language models (LLMs) has become increasingly fragmented, with no single model dominating the field."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2605.04357) · [PDF](https://arxiv.org/pdf/2605.04357)

## 一句话摘要

The landscape of large language models (LLMs) has become increasingly fragmented, with no single model dominating the field.

## 为什么值得关注

待编辑增强。

## 摘要原文

The landscape of large language models (LLMs) has become increasingly fragmented, with no single model dominating the field. Meanwhile, cloud providers offer a diverse array of mid-tier and older-generation GPUs. These heterogeneous resources provide better availability and deliver comparable performance-per-dollar to top-tier hardware. To efficiently harness these GPUs for concurrent multi-LLM serving, we introduce Coral: an adaptive, heterogeneity-aware serving system. The key idea behind Coral is the joint optimization of resource allocation and replica serving strategies across all models. To keep pace with shifting throughput demands and resource availability, Coral employs a lossless, two-stage decomposition. This approach preserves joint optimality while reducing online solve times from hours to mere tens of seconds. Evaluations across 6 models and 20 GPU configurations demonstrate that Coral reduces serving costs by up to 2.79$\times$ compared to the strongest baseline, while delivering up to 2.39$\times$ higher goodput under scarce resource constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yixuan Mei, Zikun Li, Zixuan Chen, Shiqi Pan, Mengdi Wu, Xupeng Miao, Zhihao Jia, K. V. Rashmi
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
