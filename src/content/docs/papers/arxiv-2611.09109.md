---
title: "DARIC: A Position-Independent KV Cache Reuse System with Distribution-Aware Recomputation"
description: "The context lengths of large language models (LLMs) are rapidly increasing in real-world applications such as agentic systems and retrieval-augmented generation (RAG)."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.09109) · [PDF](https://arxiv.org/pdf/2611.09109)

## 一句话摘要

The context lengths of large language models (LLMs) are rapidly increasing in real-world applications such as agentic systems and retrieval-augmented generation (RAG).

## 为什么值得关注

待编辑增强。

## 摘要原文

The context lengths of large language models (LLMs) are rapidly increasing in real-world applications such as agentic systems and retrieval-augmented generation (RAG). To accelerate LLM inference in these scenarios, reusing position-independent key-value (KV) caches across requests has emerged as a promising approach. This technique typically relies on recomputing a selected subset of tokens to restore cross-chunk interactions. However, existing solutions suffer from critical limitations in both algorithmic efficiency and system deployment. Algorithmically, they overlook the distribution of KV cache deviations, leading to either high token-selection overhead or degraded generation quality. At the system level, the reliance on custom LLM execution flows for recomputation complicates deployment and prevents seamless integration with highly optimized inference engines. In this paper, we propose DARIC (\textbf{D}istribution-\textbf{A}ware \textbf{R}ecomputation for \textbf{I}ndependent KV \textbf{C}ache Reuse), a novel KV cache reuse method based on system-algorithm co-design. At its core, DARIC introduces a distribution-aware token selection strategy that adaptively schedules token recomputation based on empirical KV deviation patterns, striking an optimal balance between generation quality and computational efficiency. Moreover, DARIC is built on a lightweight system architecture that enables independent KV cache generation and recomputation with minimal integration overhead, fully preserving existing system-level optimizations of standard inference engines. Comprehensive experiments across various datasets and LLMs demonstrate that DARIC consistently outperforms state-of-the-art methods, achieving a 1.1$\times$--4.5$\times$ speedup in time-to-first-token (TTFT) with negligible loss in generation quality. Code is available at https://github.com/Lenovo-ICI/DARIC.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Weikang Wang, Haiyang Liu, Xin Zhou, Jun Liu, Weifeng Zhang
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Lenovo-ICI/DARIC](https://github.com/Lenovo-ICI/DARIC)
- 阅读深度：metadata
