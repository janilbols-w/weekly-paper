---
title: "Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs"
description: "Large Language Model (LLM) inference has become the dominant workload in modern AI systems, requiring serving infrastructures to maximize throughput while meeting strict latency Service-Level Objectives (SLOs)."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2610.05305) · [PDF](https://arxiv.org/pdf/2610.05305)

## 一句话摘要

Large Language Model (LLM) inference has become the dominant workload in modern AI systems, requiring serving infrastructures to maximize throughput while meeting strict latency Service-Level Objectives (SLOs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) inference has become the dominant workload in modern AI systems, requiring serving infrastructures to maximize throughput while meeting strict latency Service-Level Objectives (SLOs). Since state-of-the-art LLMs exceed the compute and memory capacity of a single GPU, inference is commonly distributed across multiple GPUs using tensor parallelism (TP), pipeline parallelism (PP), or hybrid parallelism (HB). However, selecting the most effective parallelism strategy remains challenging due to complex interactions among computation, communication, pipeline utilization, sequence length, batch size, and model architecture. Existing approaches largely rely on empirical evaluation and provide limited analytical insight into the trade-offs among these strategies, particularly across the distinct prefill and decoding phases of inference. In this paper, we present a unified analytical framework for modeling distributed LLM inference under TP, PP, and HB. The framework decomposes end-to-end latency into computation, inter-GPU communication, and pipeline bubble overhead, and derives analytical models that capture TP collective communication, PP point-to-point communication, and pipeline utilization as functions of hardware, model, and workload characteristics. The model further characterizes the differing execution behavior of prefill and decoding, explaining why PP-oriented configurations favor compute-intensive prefill while TP-oriented configurations reduce decoding latency by eliminating pipeline bubbles. Experiments with modern LLMs on multi-GPU platforms validate the model and confirm the fundamental compute-communication trade-off across parallelism strategies. The framework provides practical guidance for parallelism selection, capacity planning, and optimization of future LLM serving systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Javad Mirzaei, Jeebak Mitra
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
