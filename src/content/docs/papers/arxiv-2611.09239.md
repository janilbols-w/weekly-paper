---
title: "DUET: Dual-Sparse Inference for Block Diffusion Language Models"
description: "Diffusion language models (DLMs) enable parallel token generation through iterative denoising, yet their inference remains costly due to repeated attention over a growing historical prefix and repeated processing of the entire current generation block."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.09239) · [PDF](https://arxiv.org/pdf/2611.09239)

## 一句话摘要

Diffusion language models (DLMs) enable parallel token generation through iterative denoising, yet their inference remains costly due to repeated attention over a growing historical prefix and repeated processing of the entire current generation block.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) enable parallel token generation through iterative denoising, yet their inference remains costly due to repeated attention over a growing historical prefix and repeated processing of the entire current generation block. Historical attention becomes increasingly expensive as generation progresses, while all current-block positions are propagated through the Transformer at every denoising step even though only a small fraction are typically resolved at that step. In this paper, we introduce Duet, a training-free dual-sparse inference framework that addresses these challenges through prefix Key-Value (KV) sparsity and early query sparsity, respectively. Specifically, Duet exploits the concentration and cross-step stability of historical attention within each generation block to construct a compact historical KV subset that is reused across denoising steps. For query sparsity, Duet predicts update positions from shallow representations and propagates only the corresponding queries through the suffix Transformer layers, avoiding deep computation at positions unlikely to be updated in the current step. Experiments show that Duet maintains competitive accuracy while achieving 1.34$\times$/2.83$\times$ end-to-end/per-step speedups on LLaDA2.1-mini and 2.41$\times$/4.72$\times$ on SDAR-8B-Chat-b32 at a 32K context length.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparse inference, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siyuan Yan, Shen Gu, Xiaoxing Ma, Chun Cao, Jingwei Xu
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
