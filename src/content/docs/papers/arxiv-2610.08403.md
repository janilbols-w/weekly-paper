---
title: "SSR: Sparse Segment Reduction for Ternary GEMM Acceleration"
description: "Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.08403) · [PDF](https://arxiv.org/pdf/2610.08403)

## 一句话摘要

Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware. Ternary LLMs mitigate these demands through weight quantization via ternary values, achieving significant compression often with 50-90% sparsity. However, existing approaches have limitations: methods optimized for ternary weights, such as BitNet, redundant segment reduction (RSR), and its improved version RSR++, do not exploit sparsity structures, while conventional sparse formats neglect ternary characteristics, foregoing dual optimization opportunities. In this paper, we introduce Sparse Segment Reduction (SSR), a ternary matrix multiplication method designed to accelerate the inference of ternary LLMs and general Ternary Weight Networks (TWNs). SSR has a dedicated optimized ternary data format and an algorithm that systematically exploits sparsity patterns through computation trees that scale with the sparsity. SSR provides theoretical gains with asymptotically faster inference than RSR++ for sparsity above 50%, while practical evaluations reveal performance improvements across all sparsity levels. Evaluation results show that SSR achieves 2.1-11.3x speedup over RSR++ on ternary GEMM with 45-95% sparsity. Furthermore, SSR achieves 3.5-6.3x end-to-end speedup and 4.9% of memory saving over RSR++ on the Llama-3 1B model inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Adeline Pittet, Shien Zhu, Val\'erie Verdan, Gustavo Alonso
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
