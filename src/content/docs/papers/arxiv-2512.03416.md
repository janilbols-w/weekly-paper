---
title: "TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity"
description: "The architectural shift to prefill/decode (PD) disaggregation in LLM serving improves resource utilization but struggles with the bursty nature of modern workloads."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2512.03416) · [PDF](https://arxiv.org/pdf/2512.03416)

## 一句话摘要

The architectural shift to prefill/decode (PD) disaggregation in LLM serving improves resource utilization but struggles with the bursty nature of modern workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

The architectural shift to prefill/decode (PD) disaggregation in LLM serving improves resource utilization but struggles with the bursty nature of modern workloads. Existing autoscaling policies, often retrofitted from monolithic systems like those in AIBrix and DistServe, rely on lagging indicators such as GPU utilization or coarse-grained request counts. This results in slow reactions to load spikes, leading to significant Time-to First-Token (TTFT) and Time-Per-Output-Token (TPOT) SLO violations and costly over-provisioning. We introduce TokenScale, an autoscaling framework that resolves this performance mismatch through two innovations. First, we propose Token Velocity, a novel metric that unifies the prefill, network, and decode stages by quantifying their rate of work. As a leading indicator of system backpressure, it enables proactive scaling. Second, Convertible Decoders allow decoder GPUs to dynamically execute prefill tasks during traffic spikes, creating a rapid-response buffer that absorbs bursts and eliminates the initialization latency of new prefillers. Our evaluation on a GPU cluster with production traces shows TokenScale improves SLO attainment from 50-88% to 80-96% and reduces costs by 4-14% over state-of-the-art systems, including DistServe, BlitzScale, and AIBrix. By uniting a predictive metric with a flexible system design, TokenScale significantly boosts the performance and efficiency of disaggregated LLM serving infrastructure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 9 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruiqi Lai, Hongrui Liu, Chengzhi Lu, Zonghao Liu, Siyu Cao, Siyang Shao, Yixin Zhang, Luo Mai, Dmitrii Ustiugov
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
