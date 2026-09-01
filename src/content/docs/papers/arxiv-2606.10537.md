---
title: "Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models"
description: "Diffusion large language models (dLLMs) re-encode the entire prefix at every denoising step, causing recomputation that scales quadratically with context length and becomes prohibitive for long-context scenarios."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.10537) · [PDF](https://arxiv.org/pdf/2606.10537)

## 一句话摘要

Diffusion large language models (dLLMs) re-encode the entire prefix at every denoising step, causing recomputation that scales quadratically with context length and becomes prohibitive for long-context scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) re-encode the entire prefix at every denoising step, causing recomputation that scales quadratically with context length and becomes prohibitive for long-context scenarios. We propose Prefilling-dLLM, a training-free prefill-decode disaggregation framework for dLLMs that partitions the prefix into N chunks, caches their KV representations once, and selects the top-K most relevant chunks with intra-chunk token sparsity for decoding, showing that sparse prefilling can outperform dense attention while reducing per-step complexity from quadratic in the full sequence length to quadratic only in the decode length. On LongBench and InfiniteBench, Prefilling-dLLM achieves state-of-the-art quality among dLLM acceleration methods, and an attention kernel that parallelizes decoding over the non-contiguously cached chunk KV yields 9.1--28.0x speedup at 8K--32K contexts. We further show that beginning-of-sequence tokens prepended to each chunk act as periodic attention anchors that eliminate the lost-in-the-middle phenomenon. Code is available at https://github.com/menik1126/Prefilling-dLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jing Xiong, Qi Han, Shansan Gong, Yunta Hsieh, Boyuan Zheng, Chengyue Wu, Chaofan Tao, Chenyang Zhao, Ngai Wong
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/menik1126/Prefilling-dLLM](https://github.com/menik1126/Prefilling-dLLM)
- 阅读深度：metadata
