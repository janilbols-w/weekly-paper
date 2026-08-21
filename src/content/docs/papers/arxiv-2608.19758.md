---
title: "FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving"
description: "Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.19758) · [PDF](https://arxiv.org/pdf/2608.19758)

## 一句话摘要

Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase. Our previous work, FlashPrefill, mitigates this cost through instantaneous pattern discovery and max-based dynamic thresholding; however, it remains an algorithmic prototype that is still distant from production deployment. In this paper, we present FlashPrefill V2, which evolves FlashPrefill from a prototype toward practical long-context serving along three dimensions. First, we introduce a mean correction term that effectively suppresses the approximation error, keeping performance degradation manageable even at extreme sparsity levels. Second, we redesign the sparse attention operator with PackGQA memory access, warp specialization, and pingpong pipelining, fully aligning with the latest FlashAttention-3/4 implementations and supporting FP8 inference to meet practical quantization requirements. Third, FlashPrefill V2 natively supports paged KV cache and continuous batching, allowing integration as an attention backend in modern inference frameworks such as SGLang. Extensive evaluations on NVIDIA H20 GPUs---among the most widely deployed inference accelerators---demonstrate that FlashPrefill V2 delivers up to 47.26x and 27.19x speedups over FlashAttention-2 at 128K context length under FP8 and BF16 precision, respectively, and, in FP8, still achieves a 30.49x speedup against an FA3/4-aligned dense baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Qihang Fan, Huaibo Huang, Zhiying Wu, Bingning Wang, Ran He
- 发布：2026-08-20；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
