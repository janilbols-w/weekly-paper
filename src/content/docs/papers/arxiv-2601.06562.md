---
title: "Mosaic: Unlocking Over 30$\\times$ Context Length for Diffusion LLMs Inference via Global Memory Planning and Dynamic Peak Taming"
description: "Diffusion-based large language models (dLLMs) have emerged as a promising alternative to autoregressive models, leveraging simultaneous denoising to enable global planning and iterative refinement."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2601.06562) · [PDF](https://arxiv.org/pdf/2601.06562)

## 一句话摘要

Diffusion-based large language models (dLLMs) have emerged as a promising alternative to autoregressive models, leveraging simultaneous denoising to enable global planning and iterative refinement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion-based large language models (dLLMs) have emerged as a promising alternative to autoregressive models, leveraging simultaneous denoising to enable global planning and iterative refinement. These properties make dLLMs attractive for long-context generation. However, deploying dLLMs faces a prohibitive memory barrier, as existing inference systems are inefficient for the diffusion paradigm. We observe that current inference systems are misaligned with dLLMs. Unlike autoregressive models, whose memory footprint is dominated by the KV-Cache, dLLMs are bottlenecked by transient activations rematerialized per step. Moreover, generic memory reuse mechanisms lack the global visibility to handle dynamic memory peaks of dLLMs, which alternate between logits and feed-forward networks. To address these challenges, we present Mosaic, a memory-efficient inference system that shifts dLLM execution from local, static management to a global, dynamic paradigm. Mosaic integrates (i) a mask-only logits kernel eliminating redundant activation materialization, (ii) a lazy chunking optimizer using online heuristics to tame dynamic memory peaks, and (iii) a global memory manager leveraging virtual addressing to mitigate memory fragmentation. Evaluations show that Mosaic reduces the memory peak-to-average ratio by 2.71$\times$ on average and increases the maximum inference sequence length on identical hardware by 15.30-32.34$\times$. Crucially, Mosaic is training-free and preserves exact model outputs, while reducing end-to-end latency by 2.5%-55.4%. Our code is publicly available at https://github.com/flashserve/Mosaic.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Liang Zheng, Bowen Shi, Yitao Hu, Jiawei Zhang, Ruofan Li, Guotao Yang, Zhixin Zhao, Zhengchao Wang, Sheng Chen, Wenxin Li, Dezhi Ran, Tao Xie, Keqiu Li
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flashserve/Mosaic](https://github.com/flashserve/Mosaic)
- 阅读深度：metadata
