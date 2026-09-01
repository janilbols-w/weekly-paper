---
title: "DIP: Dynamic In-Context Planner For Diffusion Language Models"
description: "Diffusion language models (DLMs) have shown strong potential for general natural language tasks with in-context examples."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2601.03199) · [PDF](https://arxiv.org/pdf/2601.03199)

## 一句话摘要

Diffusion language models (DLMs) have shown strong potential for general natural language tasks with in-context examples.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) have shown strong potential for general natural language tasks with in-context examples. Existing In-Context Learning (ICL) approaches largely inherit the practice of autoregressive language models (ARLMs), incorporating all examples into a fixed prompt. However, applying this rigid, static-prompt paradigm to DLMs incurs substantial computational overhead, as the model must evaluate the maximum context length at every step. We address this inefficiency with a key discovery: the block-wise KV-cache mechanism inherent to DLM inference enables the \textit{low-cost dynamic adjustment of the context}. Following this intuition, our core idea is to start generation with a minimal prompt and progressively insert additional examples on the fly only when the generated tokens are of low confidence. Through rigorous empirical evaluations, we observe that average verified token confidence correlates strongly with generation accuracy, making it a reliable and computationally efficient signal of token quality. Formally, we propose \textbf{D}ynamic \textbf{I}n-Context \textbf{P}lanner (DIP), a context-optimization algorithm based on average verified confidence that dynamically ranks and inserts in-context examples during generation, rather than providing all examples up front. Experimental results on math and coding benchmarks with LLaDA-1.5 and LLaDA-8B-Instruct show that DIP achieves up to $1.59\times$ and $1.36\times$ speedups, respectively, while largely preserving the generation quality of the fixed-prompt baseline. Code: https://github.com/wmd3i/DIP

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yang Li, Han Meng, Chenan Wang, Zhenyu Bi, Xuan Wang, Haipeng Chen
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/wmd3i/DIP](https://github.com/wmd3i/DIP)
- 阅读深度：metadata
