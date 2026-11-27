---
title: "SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference"
description: "Sparse attention reduces compute and memory bandwidth for long-context LLM inference."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.04511) · [PDF](https://arxiv.org/pdf/2606.04511)

## 一句话摘要

Sparse attention reduces compute and memory bandwidth for long-context LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention reduces compute and memory bandwidth for long-context LLM inference. However, two key challenges remain: (1) KV cache capacity still grows with sequence length, and offloading to CPU memory introduces a PCIe transfer bottleneck; (2) sparse selection during prefill retains $O(T^2)$ complexity and can dominate attention cost at long contexts. We propose SparDA, a decoupled sparse attention architecture that introduces a fourth per-layer projection, the Forecast, alongside Query, Key, and Value. The Forecast predicts the KV blocks needed by the next layer, enabling lookahead selection that overlaps CPU-to-GPU prefetch with current-layer execution. Because Forecast is decoupled from the attention query, our GQA implementation uses one Forecast head per GQA group, reducing selection overhead versus the original multi-head selector. On the evaluated 8B models, SparDA adds <0.5% parameters and trains only the Forecast projections using attention-derived supervision from the frozen backbone. On two sparse-pretrained 8B models, SparDA maintains accuracy comparable to the full-query sparse-attention baseline while delivering up to 1.25$\times$ prefill speedup and 1.7$\times$ decode speedup over the sparse-attention offload baseline. By enabling larger feasible batch sizes on a single GPU, SparDA further reaches up to 5.3$\times$ higher decode throughput than the non-offload sparse baseline on MiniCPM4.1-8B. Our adaptation to GLM-5.1 (754B MoE) also achieves accuracy comparable to native token-level DSA, extending the accuracy evaluation beyond block-sparse 8B models. Our source code is available at https://github.com/NVlabs/SparDA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yaosheng Fu, Guangxuan Xiao, Xin Dong, Song Han, Oreste Villa
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/NVlabs/SparDA](https://github.com/NVlabs/SparDA)
- 阅读深度：metadata
