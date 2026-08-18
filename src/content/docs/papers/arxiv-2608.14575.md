---
title: "HW-Router: Hardware-Aware Routing for Scalable Multi-LLM Serving"
description: "Modern large language model (LLM) serving platforms deploy multiple models across different GPUs, requiring routers to direct incoming queries to appropriate LLMs."
---

**评分：56/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.14575) · [PDF](https://arxiv.org/pdf/2608.14575)

## 一句话摘要

Modern large language model (LLM) serving platforms deploy multiple models across different GPUs, requiring routers to direct incoming queries to appropriate LLMs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language model (LLM) serving platforms deploy multiple models across different GPUs, requiring routers to direct incoming queries to appropriate LLMs. However, existing routing approaches primarily rely on static model attributes such as size or FLOPs to estimate serving costs. This static cost modeling fails to capture the dynamic behavior of real deployments, where the same model can exhibit vastly different inference latencies depending on hardware type (e.g., H100 vs. V100), current system load (e.g., running and waiting queue lengths), and resource contention (e.g., KV-cache usage and GPU utilization). Such hardware-agnostic routing leads to suboptimal decisions, resulting in SLO violations, queue buildup, and underutilized GPUs. To address these challenges, we present HW-Router, a dynamic routing framework that integrates real-time hardware signals into model selection to enable accurate latency prediction and intelligent, SLO-aware routing decisions. Our approach incorporates model-specific features (architecture, size, input length) alongside hardware metrics including queue lengths, KV-cache utilization, and recent TTFT/TPOT performance, and uses a lightweight latency predictor to estimate per-model-per-GPU serving time. Evaluations across diverse workloads show that HW-Router achieves 3.4-3.9x lower end-to-end latency, 46-48 percentage points higher SLO attainment, 6-8x lower GPU load skew, and a 3.1-3.4x reduction in waiting-queue fraction compared to state-of-the-art router baselines, CARROT and IRT, with only ~200 us of additional routing overhead and no loss in output quality. These results highlight the importance of real-time hardware feedback for scalable, predictable, and well-balanced multi-LLM serving. Code is available at https://github.com/UCF-ML-Research/HW-Router.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ahasan Kabir, Jiaqi Xue, Mengxin Zheng, Qian Lou
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/UCF-ML-Research/HW-Router](https://github.com/UCF-ML-Research/HW-Router)
- 阅读深度：metadata
