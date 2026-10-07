---
title: "A Shape-Adaptive Architecture with Disaggregated Quantization for Efficient LLM Serving"
description: "Large language models (LLMs) have become the backbone of modern AI applications, but pose significant challenges for efficient inference."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.07443) · [PDF](https://arxiv.org/pdf/2610.07443)

## 一句话摘要

Large language models (LLMs) have become the backbone of modern AI applications, but pose significant challenges for efficient inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have become the backbone of modern AI applications, but pose significant challenges for efficient inference. Their autoregressive generation divides execution into two phases: prefill, dominated by large GEMMs, and decoding, dominated by small GEMVs. Modern serving systems further introduce complexity through continuous batching and prefill-decoding disaggregation, leading to dynamic workloads and phase separation. However, existing accelerators remain poorly aligned with these system-level behaviors, resulting in inefficiencies in LLM serving. In this work, we present DynaCore, a unified architecture for efficient LLM serving via system-architecture co-design. We observe that the compute tile a systolic array executes, its Minimum Efficient Unit (MEU), spans all three GEMM dimensions. DynaCore reshapes the MEU along all three: spatially it trades array width against height asymmetrically, raising weight delivery while leaving the input path untouched, and temporally Split-K maps the reduction onto the array, folding partial sums through the interconnect the array already has. To exploit phase separation, we further propose disaggregated quantization, applying dual-side quantization to prefill and weight-only quantization to decoding, with an inner-product mixed-precision datapath that keeps output width invariant to precision. A runtime scheduling framework then selects an MEU per batch. Evaluation with real-world serving traces shows that DynaCore substantially reduces service-level latency over quantization and reconfigurable accelerators, improving TTFT by 3.50x and 2.97x and TPOT by 36.55x and 8.02x, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Cong Guo, Chiyue Wei, Bowen Duan, Haoxuan Shan, Benjamin F. Morris III, Yintao He, Hai "Helen" Li, Yiran Chen
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
