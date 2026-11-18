---
title: "NVFP4-MLA: Unified FP4 KV-Cache Storage and Attention Computation for Multi-Head Latent Attention"
description: "Long-context reasoning and agentic workloads make key-value (KV) cache capacity and attention computation the dominant costs of serving frontier large language models."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.18972) · [PDF](https://arxiv.org/pdf/2611.18972)

## 一句话摘要

Long-context reasoning and agentic workloads make key-value (KV) cache capacity and attention computation the dominant costs of serving frontier large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context reasoning and agentic workloads make key-value (KV) cache capacity and attention computation the dominant costs of serving frontier large language models. We present NVFP4-MLA, the first design to push both KV-cache storage and attention computation of multi-head latent attention (MLA) to FP4. NVFP4-MLA co-designs the quantization algorithm with the attention kernel and the cache system. Selective residual compensation preserves model accuracy by adding NVFP4 residuals only to the quantization-sensitive channels. Two-dimensional quantization blocks make the shared latent cache compatible with the different reduction directions of the two attention batched matrix multiplications (BMMs), removing requantization between them. On DeepSeek-R1 and Kimi-K3, NVFP4-MLA matches BF16 MLA average accuracy across nine benchmarks while compressing the MLA KV cache by 3.20x and 3.05x relative to BF16 MLA. On NVIDIA Rubin GPUs, NVFP4-MLA speeds up the attention kernel over FP8 MLA by up to 2.82x on DeepSeek-R1 and 2.71x on Kimi-K3, and lowers p90 time to first token in agentic multi-turn serving by up to 3.5x and 2.1x, respectively. In disaggregated DeepSeek-R1 serving, it also raises per-GPU throughput by up to 2.30x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Chao Ni, Qi Zhang, Xiao Wang, Zongfei Jing, Mingyang Hao, Binghan Chen, Kefeng Duan, Yu-Jung Chen, Mengdi Wang, Tijmen Blankevoort, Jun Yang
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
