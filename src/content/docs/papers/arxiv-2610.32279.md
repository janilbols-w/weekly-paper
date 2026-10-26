---
title: "TranSAGE: Automating Spatial Accelerator Generation for Large-Scale Transformer Models"
description: "Large-scale Transformers have achieved remarkable success across NLP, computer vision, and robotics, but their growing computational and memory demands challenge efficient inference."
---

**评分：57/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.32279) · [PDF](https://arxiv.org/pdf/2610.32279)

## 一句话摘要

Large-scale Transformers have achieved remarkable success across NLP, computer vision, and robotics, but their growing computational and memory demands challenge efficient inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale Transformers have achieved remarkable success across NLP, computer vision, and robotics, but their growing computational and memory demands challenge efficient inference. Spatial accelerators offer advantages in on-chip bandwidth and energy efficiency, yet designing them for large models remains costly and time-consuming. Existing accelerator generators typically focus on single-operation support, overlooking the benefits of multi-operation pipelining, which limits throughput and energy efficiency. We propose TranSAGE, a compiler-based framework that jointly optimizes scheduling for large-scale Transformers under multi-operation pipelining and generates corresponding accelerator implementations. Our approach integrates a design space exploration (DSE) engine with multi-operation dataflow optimization and a dynamic programming-based graph partitioning algorithm to efficiently identify pipeline-friendly operation clusters and their optimal dataflow parameters. We further design spatial architecture primitives and lowering passes to automatically generate efficient RTL implementations. Evaluations on four representative LLMs demonstrate that TranSAGE achieves up to 2.41x higher throughput and 13.04x higher energy efficiency than commercial GPU/NPU baselines. Compared with state-of-the-art accelerator generators, TranSAGE achieves up to 11.33x higher throughput and 6.07x higher energy efficiency. Our code is available at https://github.com/sjtu-zhao-lab/TranSAGE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Chi Zhang, Yi Sun, Weichuang Zhang, Quan Chen, Jieru Zhao
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/sjtu-zhao-lab/TranSAGE](https://github.com/sjtu-zhao-lab/TranSAGE)
- 阅读深度：metadata
