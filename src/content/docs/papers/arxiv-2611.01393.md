---
title: "Layer-wise CPU-GPU Scheduling for LLM Inference on Memory-Limited Consumer GPUs"
description: "As large language model inference environments expand toward consumer devices, it remains challenging to efficiently run models that exceed GPU memory capacity in single-GPU settings."
---

**评分：46/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2611.01393) · [PDF](https://arxiv.org/pdf/2611.01393)

## 一句话摘要

As large language model inference environments expand toward consumer devices, it remains challenging to efficiently run models that exceed GPU memory capacity in single-GPU settings.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language model inference environments expand toward consumer devices, it remains challenging to efficiently run models that exceed GPU memory capacity in single-GPU settings. The latency of transferring weights that do not fit in GPU memory accounts for about 98\% of inference time and remains a major obstacle. In this paper, we focus on the fact that during the decode phase, layer computation time on the CPU can be shorter than weight transfer time, presenting an opportunity to hide weight transfers by utilizing this computation time. Therefore, we propose a method to hide transfer latency by executing certain layers on the CPU during the decode phase while asynchronously transferring the next layer's weights to the GPU in the background of that computation. To realize this scheduling, we formulate the placement of CPU/GPU computation and weight transfers as a latency minimization problem and perform optimization using an approximation model with relaxed temporal constraints. Evaluation results confirm that in a consumer desktop environment, our approach accelerates OPT-30B inference by 3.5x compared to HuggingFace Accelerate and 6.3x compared to DeepSpeed Zero-Inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu scheduling
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Naoto Sugiura, Yuta Tokusashi, Hiroki Matsutani
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
