---
title: "A Measurement Study of LLM Inference Trade-offs Across Edge Continuum Hardware"
description: "Large language models (LLMs) are increasingly used as backends for intelligent web services, but serving them across the edge continuum requires balancing quality, latency, model footprint, and energy."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.08307) · [PDF](https://arxiv.org/pdf/2609.08307)

## 一句话摘要

Large language models (LLMs) are increasingly used as backends for intelligent web services, but serving them across the edge continuum requires balancing quality, latency, model footprint, and energy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly used as backends for intelligent web services, but serving them across the edge continuum requires balancing quality, latency, model footprint, and energy. This paper presents a controlled measurement study of self-hosted LLM inference across edge and near-edge deployment nodes: an NVIDIA Jetson AGX Orin and a near-edge server with CPU-only and GPU-enabled inference modes. We evaluate multiple open-weight LLMs and quantization variants using a fixed question-answering workload, and compare them against GPT-4o as a cloud-hosted accuracy and latency reference. Our benchmarking pipeline reports accuracy, model footprint, per-token decoding latency, prefill latency, and overall execution energy. The results show that GPU-enabled server execution provides the lowest compute-side latency, while Jetson Orin shows lower measured energy, consistent with its lower platform power under our setup. CPU-only execution is consistently dominated in latency for our workload and shows higher measured energy. We also show that parameter count and downloaded weight-file size alone do not reliably predict observed accuracy or latency. Finally, using Pareto-frontier analysis, we study how deployment decisions may change under possible streamed-token delivery overheads, highlighting that compute-side inference metrics alone can lead to suboptimal placement for latency-sensitive interactive web services.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maysam Khatib, Moysis Symeonides, Demetris Trihinas, George Pallis, Marios D. Dikaiakos
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
