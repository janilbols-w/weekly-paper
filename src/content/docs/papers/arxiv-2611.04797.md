---
title: "Training Specialist LLMs on Your Phone: Forward-Only Optimization via Block-Spectral Coordinates"
description: "Large language models (LLMs) on personal devices keep user data local, but limited memory restricts their general capability."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.04797) · [PDF](https://arxiv.org/pdf/2611.04797)

## 一句话摘要

Large language models (LLMs) on personal devices keep user data local, but limited memory restricts their general capability.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) on personal devices keep user data local, but limited memory restricts their general capability. Since most user-specific tasks do not require the breadth of frontier models, a practical solution is to adapt a shared on-device model into lightweight specialists. However, backpropagation is prohibitive in memory, and users rarely provide labeled data. We present MobileSpec, a system that trains specialists with forward passes alone and learns from automatically checked task outcomes, as in reinforcement learning with verifiable rewards (RLVR). Because forward-only updates are built from random perturbations, training is efficient only when these perturbations resemble the weight changes of RLVR, which largely preserve the singular values of pretrained weights and rotate their singular vectors. The core algorithm of MobileSpec, FuRA-S, produces such perturbations while training only the block-spectral coordinates of pretrained weights, namely the singular values of their column blocks. As we show theoretically and empirically, rescaling these blocks independently shifts their relative contributions to each weight matrix and thereby rotates its singular vectors. Since this update can be rewritten as a transformation of the layer input, FuRA-S also adapts INT4 models without modifying their weights. With specialists of only 1-5 MB that update 0.015-0.05% of the parameters, MobileSpec raises the success rate of a phone-use agent from 6-23% up to 89-100% and trains a personalized 8B model on an iPhone 16 Pro overnight. On RLVR benchmarks, FuRA-S is competitive with full-parameter evolution strategies (ES) and outperforms ES over LoRA adapters and quantized ES on INT4 models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liyan Tan, Yequan Zhao, Ziyue Liu, Yupeng Su, Ruijie Zhang, Zheng Zhang
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
