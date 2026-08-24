---
title: "SPICE: Speculative Prefetching with Low-Rank Expert Surrogates and Heterogeneous Orchestration for MoE Inference Acceleration"
description: "Mixture-of-Experts (MoE) models are increasingly used in LLMs because sparse activation decouples model capacity from compute cost."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2608.21240) · [PDF](https://arxiv.org/pdf/2608.21240)

## 一句话摘要

Mixture-of-Experts (MoE) models are increasingly used in LLMs because sparse activation decouples model capacity from compute cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models are increasingly used in LLMs because sparse activation decouples model capacity from compute cost. However, the large expert parameter footprint often exceeds GPU memory capacity, making inference latency dominated by the host-to-device PCIe transfers for expert loading. To address these challenges, this paper presents SPICE, a speculative prefetching framework for MoE offloading that combines lightweight expert prediction with confidence-aware CPU-GPU orchestration. On one hand, SPICE builds a lightweight draft model aligned with the target MoE architecture, using a confidence-aware adaptive lookahead algorithm to prefetch high-confidence experts. On the other hand, when speculative predictions miss, SPICE switches to a cost-aware CPU-GPU heterogeneous orchestration: low-confidence misses are approximated by the resident shared expert with low rank expert (LoRE) surrogates, while exact residual work is offloaded to the CPU and executed asynchronously in parallel with ongoing GPU computation. Evaluated on DeepSeek-V2-Lite and Qwen2-57B-A14B across diverse GPU platforms, SPICE achieves up to 3.12 speedup in Time Per Output Token (TPOT) with minimal quality loss, showing that effective MoE offloading requires not only predicting future experts, but also deciding which misses deserve approximation, which require exact recovery, and where exact residual work should execute.

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

- 作者：Yongxiang Lyu, Ning Li, Bonian Jia
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
