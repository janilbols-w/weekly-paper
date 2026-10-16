---
title: "HaloBlock: Faster and Better Decoding for Diffusion Large Language Models"
description: "Diffusion large language models (dLLMs) have attracted increasing research attention due to their bidirectional attention and arbitrary order decoding."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](http://arxiv.org/abs/2610.17948v1) · [PDF](https://arxiv.org/pdf/2610.17948v1)

## 一句话摘要

Diffusion large language models (dLLMs) have attracted increasing research attention due to their bidirectional attention and arbitrary order decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) have attracted increasing research attention due to their bidirectional attention and arbitrary order decoding. However, there are two issues in dLLMs inference: the decoding difficulty is dominated by the tokens on the right side of the block, and the block-wise decoding inherently suffers from boundary contextual discontinuity. To tackle these limitations, we propose HaloBlock, a difficulty-aware adaptive halo mechanism for dLLM inference. We first leverage bidirectional cumulative entropy to characterize block decoding difficulty. Then, based on the bidirectional decoding difficulty, we adaptively allocate bidirectional halo regions on both sides of each block to mitigate boundary contextual discontinuity. The difficulty-aware design of HaloBlock smooths cross-block context propagation and lowers decoding difficulty for hard tokens, yielding better generation quality and faster convergence. Evaluated on LLaDA-8B-Instruct, Dream-7B-Instruct and LLaDA-1.5 across mathematical reasoning and code generation benchmarks, HaloBlock demonstrates consistent accuracy improvements and higher inference efficiency. Source codes are publicly available at https://github.com/PolyU-VCLab/HaloBlock.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhaohui Zheng, Chenhang He, Jinrui Zhang, Ming-Ming Cheng, Lei Zhang
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/PolyU-VCLab/HaloBlock](https://github.com/PolyU-VCLab/HaloBlock)
- 阅读深度：metadata
