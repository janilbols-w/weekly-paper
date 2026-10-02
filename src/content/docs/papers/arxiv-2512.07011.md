---
title: "Block Sparse Flash Attention"
description: "Block Sparse Flash Attention 先计算精确 query-key 相似度，再以校准阈值筛选每个 query 的 top-k value block，跳过约一半被裁剪块的计算与内存传输，并提供可替换 FlashAttention 的 CUDA kernel。摘要报告 Llama-3.1-8B 在 LongBench 上最高端到端加速 1.13 倍、准确率下降 1.1%，在 Needle-in-a-Haystack 上最高加速 1.24 倍、准确率下降 1%，kernel 最高加速 1.38 倍。"
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2512.07011) · [PDF](https://arxiv.org/pdf/2512.07011)

## 一句话摘要

Block Sparse Flash Attention 先计算精确 query-key 相似度，再以校准阈值筛选每个 query 的 top-k value block，跳过约一半被裁剪块的计算与内存传输，并提供可替换 FlashAttention 的 CUDA kernel。摘要报告 Llama-3.1-8B 在 LongBench 上最高端到端加速 1.13 倍、准确率下降 1.1%，在 Needle-in-a-Haystack 上最高加速 1.24 倍、准确率下降 1%，kernel 最高加速 1.38 倍。

## 为什么值得关注

该方法不依赖训练或预先预测重要性，以精确注意力分数换取更稳健的块筛选，并通过 drop-in CUDA 实现降低现有长上下文推理栈的接入成本；这为质量可控的稀疏注意力提供了直接工程路径。

## 摘要原文

Modern large language models increasingly require long contexts for reasoning and multi-document tasks, but attention's quadratic complexity creates a severe computational bottleneck. We present Block Sparse Flash Attention (BSFA), a drop-in replacement that accelerates long-context inference while preserving model quality. Unlike methods that predict importance before computing scores, BSFA computes exact query-key similarities to select the top-k most important value blocks for each query. By comparing per-block maximum scores against calibrated thresholds, we skip approximately 50% of the computation and memory transfers for pruned blocks. Our training-free approach requires only a one-time threshold calibration on a small dataset to learn the per-layer and per-head attention score distributions. We provide a CUDA kernel implementation that can be used as a drop-in replacement for FlashAttention. On Llama-3.1-8B, BSFA achieves up to 1.13x end-to-end speedup on LongBench with only a 1.1% accuracy drop, and up to 1.24x on Needle-in-a-Haystack retrieval at a 1% accuracy drop. The attention kernel itself accelerates by up to 1.38x. We compare BSFA against five recent sparse attention baselines (SpargeAttention, MInference, FlexPrefill, XAttention, and BLASST), and verify the method on Qwen2.5-7B and on A6000 and H100 GPUs. The implementation is available at https://github.com/Danielohayon/Block-Sparse-Flash-Attention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, flash attention
- quantitative claim detected
- code/artifact link detected
- 限制：方法仍需完整计算 query-key 相似度，节省主要来自被裁剪 value block 的后续计算与传输，因此端到端最高加速相对有限。阈值需要一次数据校准，且摘要已显示约 1% 的精度损失；收益也依赖稀疏率、序列长度、模型和 GPU。

## 元数据

- 作者：Daniel Ohayon, Itay Lamprecht, Itay Hubara, Israel Cohen, Daniel Soudry, Noam Elata
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Danielohayon/Block-Sparse-Flash-Attention](https://github.com/Danielohayon/Block-Sparse-Flash-Attention)
- 阅读深度：abstract
