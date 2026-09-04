---
title: "DynaNDE: Dynamic Near-Data Expert Scheduling for Batched MoE Inference"
description: "Mixture-of-Experts (MoE) models enable efficient scaling of large language model (LLM) inference but suffer from substantial data-movement overhead when deployed on neural processing unit (NPU)-based systems."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.00407) · [PDF](https://arxiv.org/pdf/2609.00407)

## 一句话摘要

Mixture-of-Experts (MoE) models enable efficient scaling of large language model (LLM) inference but suffer from substantial data-movement overhead when deployed on neural processing unit (NPU)-based systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models enable efficient scaling of large language model (LLM) inference but suffer from substantial data-movement overhead when deployed on neural processing unit (NPU)-based systems. Near-Data Processing (NDP) provides a promising way to mitigate this bottleneck via cooperative NPU-NDP execution. However, existing NPU-NDP MoE systems do not fully account for hardware heterogeneity, dynamic expert-level concurrency, and temporal expert reuse during batched inference. This paper presents DynaNDE, a dynamic near-data expert scheduling framework that exploits NPU-NDP collaboration to accelerate batched MoE inference. DynaNDE introduces an analytical performance model that captures hardware heterogeneity, data-movement costs, and communication-computation overlap in cooperative NPU-NDP execution. Guided by this model, DynaNDE determines per-layer expert scheduling across the NPU and NDP while accounting for expert-level concurrency. DynaNDE also incorporates a reuse-aware runtime that avoids redundant parameter movement when experts reside in NPU memory. Experimental results show that DynaNDE achieves substantial throughput improvements over the state-of-the-art NPU-NDP MoE serving framework, with average speedups of 2.6$\times$ and 2.2$\times$ for the prefill and decoding stages, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoyang Lu, Belthangady Akash Vi Narayana Pai, Xian-He Sun
- 发布：2026-08-31；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
