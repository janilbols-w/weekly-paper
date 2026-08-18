---
title: "HieraSparse: Hierarchical Semi-Structured Sparse KV Attention"
description: "The deployment of long-context Large Language Models (LLMs) poses significant challenges due to the intense computational cost of self-attention and the substantial memory overhead of the Key-Value Cache (KV Cache)."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.16864) · [PDF](https://arxiv.org/pdf/2604.16864)

## 一句话摘要

The deployment of long-context Large Language Models (LLMs) poses significant challenges due to the intense computational cost of self-attention and the substantial memory overhead of the Key-Value Cache (KV Cache).

## 为什么值得关注

待编辑增强。

## 摘要原文

The deployment of long-context Large Language Models (LLMs) poses significant challenges due to the intense computational cost of self-attention and the substantial memory overhead of the Key-Value Cache (KV Cache). In this paper, we introduce \textit{HieraSparse}, a hierarchical KV Cache compression framework with acceleration kernels that leverage GPU sparse tensor cores to speed up semi-structured KV Cache attention for both the prefill and decode phases. With the hierarchical design, our method allows for a flexible quality-sparsity trade-off and successfully converts sparsity into efficiency. Compared to the state-of-the-art decode method that utilizes unstructured sparsity, \textit{HieraSparse} achieves $\mathbf{1.2\times}$ KV compression ratio and $\mathbf{4.57\times}$ attention speedup at the same sparsity level. Furthermore, we extended the semi-structured KV Cache pruning to the prefill stage, which demonstrated up to $\mathbf{1.85\times}$ attention speedup at the highest sparsity. Lastly, we evaluate the generation quality of \textit{HieraSparse} with a simple magnitude-based pruning method, and the results show that $\mathbf{1.34\times}$ prefill and $\mathbf{1.71\times}$ decode attention speedup can be achieved without significant quality drop. The codebase can be found at https://github.com/psl-ntu/HieraSparse.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Haoxuan Wang, Chen Wang
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/psl-ntu/HieraSparse](https://github.com/psl-ntu/HieraSparse)
- 阅读深度：metadata
