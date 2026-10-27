---
title: "Speeding up Log-Sum-Exp: Kernel Fusion at the Memory Wall, Integer Arithmetic at the Compute Wall"
description: "While the Log-Sum-Exp (LSE) function is a foundational numerical primitive for stable log-domain computation in modern machine learning, its fast and efficient computation on generic platforms (\\ie, CPUs and GPUs) has been underexplored, potentially creating execution bottlenecks for large workloads."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.33647) · [PDF](https://arxiv.org/pdf/2610.33647)

## 一句话摘要

While the Log-Sum-Exp (LSE) function is a foundational numerical primitive for stable log-domain computation in modern machine learning, its fast and efficient computation on generic platforms (\ie, CPUs and GPUs) has been underexplored, potentially creating execution bottlenecks for large workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

While the Log-Sum-Exp (LSE) function is a foundational numerical primitive for stable log-domain computation in modern machine learning, its fast and efficient computation on generic platforms (\ie, CPUs and GPUs) has been underexplored, potentially creating execution bottlenecks for large workloads. On GPU, the de facto implementation torch.logsumexp dispatches a chain of nine sub-kernels per call, incurring redundant High Bandwidth Memory (HBM) traffic and launch overhead. On CPU, exp and log operations are hardware-hungry, limiting the computing efficiency. To address these bottlenecks, we propose two drop-in kernels to significantly accelerate LSE computation on both GPUs and CPUs: FuseLSE, a single-pass fused kernel that evaluates LSE's exp and log functions on the GPU's Special Function Unit (SFU); and IntLSE, which further replaces the LSE computation with approximated integer arithmetic for CPU computation. Our experiments, validated by benchmarks across workload sizes and hardware platforms, show that both kernels are ${\sim}10-11\times$ faster than PyTorch at small workloads and ${\sim}6\times$ faster on larger ones on GPUs, where the speed-up is attributed to reduced launch overhead and HBM traffic. On CPU, where no SFU is available, LSE computation dominates the cost, allowing IntLSE to gain ${\sim}3-6\times$ execution speed over FuseLSE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fused kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lingyun Yao, Martin Andraud, Niki Loppi, Andrea Pilzer, Anji Liu, Guy Van den Broeck, Martin Trapp
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
