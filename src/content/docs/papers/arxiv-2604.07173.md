---
title: "InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models"
description: "LoRA enables efficient customization of LLMs and is widely used in multi-tenant and multi-task serving."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2604.07173) · [PDF](https://arxiv.org/pdf/2604.07173)

## 一句话摘要

LoRA enables efficient customization of LLMs and is widely used in multi-tenant and multi-task serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

LoRA enables efficient customization of LLMs and is widely used in multi-tenant and multi-task serving. However, emerging model architectures such as MoE significantly increase LoRA memory cost, making existing coupled LoRA serving designs poorly scalable and prone to tail-latency inflation. We present InfiniLoRA, a disaggregated LoRA serving system that decouples LoRA execution from base-model inference. InfiniLoRA introduces a shared LoRA Server with parallelism-aware execution, SLO-driven provisioning, and critical-path optimizations, including GPU-initiated communication and hardware-specialized LoRA kernels. Experiments show that InfiniLoRA can achieve an average $3.05\times$ increase in serviceable request rate under strict latency SLOs, and improve the percentage of LoRA adapters satisfying the SLO requirement by 54.0\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant, slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongyu Chen, Letian Ruan, Zilin Xu, Yuchen Li, Xinyu Chen, Bingsheng He, Jingwen Leng, Jieru Zhao, Shixuan Sun, Minyi Guo
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
