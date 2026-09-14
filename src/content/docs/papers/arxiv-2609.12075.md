---
title: "Efficient Vision-Language-Action Management and Serving for Robot Factories"
description: "Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.12075) · [PDF](https://arxiv.org/pdf/2609.12075)

## 一句话摘要

Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage. Since robots must meet strict Service-Level Objectives (SLOs) for safety, VLA inference is inherently latency-critical. Meeting these SLOs requires high-end GPUs, yet weight, cost, and power constraints preclude integrating such GPUs on-robot. Prior works offload VLA inference to edge servers that serve many robots on VLA models. However, current VLA systems lack support for multi-request, multi-model execution on a multi-GPU server under SLOs, while existing serving systems for multi-stage models are optimized for throughput and stage disaggregation across separate GPUs, which are ill-suited for the millisecond-scale stages of VLA models. We design Robion, the first VLA serving and management system for multi-robot, multi-model requests on multi-GPU edge servers that meets SLOs. Our serving engine disaggregates the VLM and ADiT stages within a GPU via two streams, dynamically restricting the SMs on VLM stream so ADiT always finds SMs to run alongside it, and co-locates multiple models by sharing these streams across them, prioritizing requests by least remaining SLO time. Our management engine enables flexible model placements on multi-GPU servers, and integrates an intelligent traffic controller that maximizes per-model batching under the chosen placement while bounding each GPU's load to meet SLOs. For individual models, Robion serves on average 6.7$\times$ and 1.5$\times$ higher robot load within 98% SLO attainment over vLLM-Omni, the most widely used multi-stage serving system, and Monolithic, which runs VLM and ADiT as a single pipeline, respectively. In a large-scale experiment of serving 8 different models on a 4-GPU server, Robion can serve up to 64 robots within 98% SLO attainment.

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

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dionysios Adamopoulos, Nattapol Chanpaisit, Basel Fakhri, Christina Giannoula
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
