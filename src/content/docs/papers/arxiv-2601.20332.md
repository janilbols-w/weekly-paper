---
title: "Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching"
description: "Diffusion language models (DLMs) generate text through iterative denoising, but inference requires full-sequence attention at every iteration, resulting in substantial redundant computation on masked tokens."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.20332) · [PDF](https://arxiv.org/pdf/2601.20332)

## 一句话摘要

Diffusion language models (DLMs) generate text through iterative denoising, but inference requires full-sequence attention at every iteration, resulting in substantial redundant computation on masked tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (DLMs) generate text through iterative denoising, but inference requires full-sequence attention at every iteration, resulting in substantial redundant computation on masked tokens. Block-wise diffusion can reduce this cost, yet it typically relies on retraining and constrained update orders, limiting its direct applicability to pretrained DLMs. Our token-level analysis reveals pronounced structural locality in DLM inference. Decoding is driven by a small set of prefix-localized active tokens; the influence of distant undecoded context diminishes rapidly, and decoded tokens exhibit stage-wise temporal stability, enabling reuse of intermediate representations except for a brief post-decode transient. Motivated by these observations, we propose \textbf{\placeholder}\footnote{The source code is available at https://github.com/vhicrgit/Window-Diffusion.}, a window-based token pruning and caching method for inference. We maintain a local computation window that slides rightward as denoising progresses, and partition undecoded tokens into: (i) \textit{active tokens} that are computed online, (ii) \textit{buffer tokens} whose KV states are cached and periodically refreshed, and (iii) \textit{far-field tokens} that are pruned outside the window. Computation is restricted to active and buffer tokens within the window, while far-field tokens are omitted at each stage. Experiments on LLaDA and Dream show that, under matched compute budgets, our method achieves up to $99\times$ inference speedup while largely preserving generation performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Fengrui Zuo, Zhiwei Ke, Yiming Liu, Wenqi Lou, Chao Wang, Xuehai Zhou
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/vhicrgit/Window-Diffusion.}](https://github.com/vhicrgit/Window-Diffusion.})
- 阅读深度：metadata
