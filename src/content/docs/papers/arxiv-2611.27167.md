---
title: "BusemannFormer: Horospherical Self-Attention for Hyperbolic Graph Transformers"
description: "Hyperbolic neural networks excel on hierarchical graph data, yet existing hyperbolic Transformers largely adapt conventional attention without explicitly exploiting the ideal boundary, a geometric structure closely tied to tree hierarchy."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.27167) · [PDF](https://arxiv.org/pdf/2611.27167)

## 一句话摘要

Hyperbolic neural networks excel on hierarchical graph data, yet existing hyperbolic Transformers largely adapt conventional attention without explicitly exploiting the ideal boundary, a geometric structure closely tied to tree hierarchy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hyperbolic neural networks excel on hierarchical graph data, yet existing hyperbolic Transformers largely adapt conventional attention without explicitly exploiting the ideal boundary, a geometric structure closely tied to tree hierarchy. We propose Horospherical Self-Attention (HSA): each query selects an ideal-boundary direction and scores keys by their Busemann depth along that direction, yielding a token-to-token hyperbolic attention kernel. We establish a flat-limit connection to dot-product attention, characterize score level sets as horospheres, and bound key-side gradients. HSA is integrated into BusemannFormer, a fully hyperbolic graph Transformer, with a log-depth variant that uses query depth to modulate attention concentration. We further introduce a finite-boundary-dictionary extension supporting linear-complexity global attention. Experiments on hierarchical and citation graphs show that BusemannFormer-LD outperforms the evaluated baselines on several node-classification benchmarks and achieves competitive performance across diverse graph structures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Youheng Yao, Ziyao Zeng, Wenbo Liao, Tianqi Wang
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
