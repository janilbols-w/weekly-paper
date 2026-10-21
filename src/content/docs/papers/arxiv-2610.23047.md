---
title: "DIFFLET: A Fast Inference Engine for Diffusion Transformer Models on AWS Trainium"
description: "On AWS Trainium2, every component of a diffusion model runs as a program compiled ahead of time for fixed shapes, while pipelines differ across models, prompt lengths across requests, and caching decisions across denoising steps."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.23047) · [PDF](https://arxiv.org/pdf/2610.23047)

## 一句话摘要

On AWS Trainium2, every component of a diffusion model runs as a program compiled ahead of time for fixed shapes, while pipelines differ across models, prompt lengths across requests, and caching decisions across denoising steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

On AWS Trainium2, every component of a diffusion model runs as a program compiled ahead of time for fixed shapes, while pipelines differ across models, prompt lengths across requests, and caching decisions across denoising steps. We present Difflet, a serving engine in which five model pipelines share one compilation backend, joint attention is split across cores by attention head, and a host controller decides at each denoising step whether to run the denoiser or reuse its earlier output. A small probe program computes the caching signal on the device and returns one number per step, and a resident model process keeps every program loaded across requests. Across five image and video model families, fused attention accelerates denoiser steps by 1.2-4.3x over the same framework using PyTorch/XLA attention, and at 32.8k visual tokens it is the only attention that compiles. On four of the five models, resident serving is 1.5-3.4x faster than standalone runs that reload weights from a warm file cache for each generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Bin Ma, Min Yu, Vijay Kodamalla, Jialin Liu, Dong Li
- 发布：2026-10-19；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
