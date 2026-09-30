---
title: "BitsMoE: Cost-Aware Bit Allocation in Spectral Space for MoE LLM Quantization"
description: "Mixture-of-Experts (MoE) large language models incur substantial memory costs due to their large expert parameter counts."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.00079) · [PDF](https://arxiv.org/pdf/2606.00079)

## 一句话摘要

Mixture-of-Experts (MoE) large language models incur substantial memory costs due to their large expert parameter counts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) large language models incur substantial memory costs due to their large expert parameter counts. Mixed-precision quantization reduces these costs by allocating different bit-widths to experts or linear blocks according to their importance. However, assigning a single precision within each expert or linear block overlooks its internal structural heterogeneity. This limitation motivates two key questions: (1) how to define a fine-grained unit for quantization within a linear transformation; and (2) how to characterize the quantization cost of each unit under actual activation patterns and different bit-widths. To address these two questions, we propose BitsMoE, a cost-aware mixed-precision quantization framework built on two complementary techniques: (1) Shared-basis Spectral Decomposition (SSD) separates expert weights into a shared basis and expert-specific spectral components, defining structural quantization units while exploiting cross-expert redundancy. (2) Factorized Quantization Cost Modeling (FQCM) estimates component-wise costs from output reconstruction loss by combining intrinsic spectral importance, activation-dependent importance, and bit-width-dependent distortion. Using these component-wise costs, we formulate bit allocation as an integer linear program (ILP) that minimizes total modeled quantization cost under a fixed memory budget. On Qwen3-30B-A3B at 2-bit, BitsMoE achieves 64.29% average accuracy over seven downstream tasks, outperforming the evaluated MoE-specific methods, including those using ILP-based bit allocation, and exceeding GEMQ by 2.80 percentage points. Under the same setting, it achieves a $16.47\times$ end-to-end offline quantization speedup over GEMQ. It also achieves up to $6.46\times$ the decode throughput of GPTQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiayu Zhao, Zihan Teng, Minhao Fan, Tianrui Ma, Wentao Ren, Song Chen, Weichen Liu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
