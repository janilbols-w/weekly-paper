---
title: "Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation"
description: "The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.01601) · [PDF](https://arxiv.org/pdf/2609.01601)

## 一句话摘要

The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context.

## 为什么值得关注

待编辑增强。

## 摘要原文

The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context. Since real-world repositories often exceed the input length limits of LLMs, existing approaches commonly adopt retrieval-augmented generation (RAG) to provide repository-specific context. Despite improving repository-context retrieval, existing methods typically provide context as task-level support, without explicitly identifying the critical tokens that require fine-grained repository context during generation. During the autoregressive generation process of LLMs, errors often concentrate at a small number of decisive positions: once such tokens are generated incorrectly, subsequent code may follow an incorrect semantic path and eventually lead to functional failure. We refer to these positions as "critical tokens". In this paper, we propose ACToR, an adaptive critical token-aware retrieval framework for repository-level code generation. ACToR identifies critical tokens during generation and triggers targeted retrieval on demand to provide repository context at these decisive positions. In addition, we design a position-aware weighting method for dense retrievers to prioritize context that is more informative for generation. We evaluate ACToR on two representative repository-level benchmarks, RepoExec and CoderEval. Experimental results show that ACToR consistently outperforms state-of-the-art methods, achieving relative improvements of 8.4% on RepoExec and 15.4% on CoderEval. Beyond performance gains, we systematically quantify the impact of critical tokens, revealing their central role in major generation failures and highlighting the necessity of targeted retrieval strategies. We provide the code and data at https://github.com/DeepSoftwareAnalytics/ACToR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Kefeng Duan, Dewu Zheng, Yanlin Wang, Terry Yue Zhuo, Mingwei Liu, Jianxing Yu, Jiachi Chen, Ensheng Shi, Xilin Liu, Yuchi Ma, Zibin Zheng
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/DeepSoftwareAnalytics/ACToR](https://github.com/DeepSoftwareAnalytics/ACToR)
- 阅读深度：metadata
