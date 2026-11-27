---
title: "SVDP: Training-Free Contextual Sparsity Predictors for Fast LLM Inference"
description: "Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.14110) · [PDF](https://arxiv.org/pdf/2603.14110)

## 一句话摘要

Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Contextual sparsity is one of the approaches used to reduce computational complexity in the inference process of large language models (LLMs). Existing techniques for efficient LLM inference acceleration based on contextual sparsity with minimal accuracy degradation require training sparse pattern predictors. This paper presents a framework for accelerating inference of ReGLU-based feed-forward networks (FFNs) within LLMs. The proposed framework provides a fast, training-free method for building sparse pattern predictors using truncation-aware singular value decomposition (SVD) of the gate projection matrix, along with a threshold calibration algorithm, and inference executors supporting conditional computation on CUDA and CANN devices. Experiments on three sparse LLMs with an average activation sparsity level of 90% in the FFNs demonstrate up to a 1.8x reduction in end-to-end decoding time while maintaining less than 1% degradation in benchmark scores on tasks involving complex math and code generation. This work advances the deployment of LLMs on edge devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C. C. Korikov
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
