---
title: "Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry"
description: "Long-context LLM inference is bottlenecked by quadratic attention computation and growing KV-cache costs."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.06849) · [PDF](https://arxiv.org/pdf/2608.06849)

## 一句话摘要

Long-context LLM inference is bottlenecked by quadratic attention computation and growing KV-cache costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM inference is bottlenecked by quadratic attention computation and growing KV-cache costs. Existing sparse attention and KV-compression methods typically decide which tokens or heads to preserve from runtime attention scores, observation windows, calibration prompts, or learned gates, making head diagnosis input-dependent and costly to deploy. We propose Autonomy-of-Heads (AoH), a data-free method that identifies retrieval and streaming heads from the spectral geometry of query-key projections. AoH defines the kernel attention operator $M_h = W_K^{h\top}W_Q^h$ and uses its effective-rank as a weight-space measure of head function: concentrated spectra indicate a small number of dominant query-key matching directions and are associated with retrieval heads, whereas diffuse spectra indicate the absence of a dominant global matching direction and are associated with streaming heads. We further derive an efficient $d_\text{head}$-dimensional computation that avoids constructing the full $d_\text{model}\times d_\text{model}$ matrix. We conducted extensive experiments across models demonstrating that at 50\% sparsity, AoH retains 96.5\% of Full Attention performance on average while reducing prefill and decode latency by up to 41.4\% and 66.0\%, respectively, and KV-cache memory by 50.0\% at 256K tokens.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yehan Yang, Junyuan Shang, Yang Li, Guanqun Zhao, Shuohuan Wang, Dianhai Yu
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
