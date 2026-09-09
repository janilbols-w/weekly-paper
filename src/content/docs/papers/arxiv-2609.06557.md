---
title: "Hidden in Plain Sight: The Overlooked Significance of Canonical Elements for Extreme LLM Sparsity"
description: "Large language models (LLMs) are often considered fragile under aggressive sparsification, and maintaining reliable performance typically requires sticking to moderate sparsity levels."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06557) · [PDF](https://arxiv.org/pdf/2609.06557)

## 一句话摘要

Large language models (LLMs) are often considered fragile under aggressive sparsification, and maintaining reliable performance typically requires sticking to moderate sparsity levels.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are often considered fragile under aggressive sparsification, and maintaining reliable performance typically requires sticking to moderate sparsity levels. However, recent studies suggest that LLMs are more resilient to high sparsity than previously thought, reframing the problem as a design challenge rather than a fundamental limitation. In this work, we challenge the perceived limits of unstructured post-training LLM pruning by revisiting elementary pruning strategies that have remained relatively underexplored at this scale. Through a progressive sparsification framework with second-order saliency and continued training coordinated with sparsity progression, we show that pretrained LLMs can retain strong performance far beyond commonly studied sparsity regimes. Across LLaMA-2 and Qwen-3 model families, our approach improves perplexity and downstream accuracy up to 99\% sparsity, surpassing both the current state-of-the-art and representative baselines. Precisely, on LLaMA-2-7B, our approach achieves WikiText-2 perplexities of 13.48 and 19.67 at 95\% and 99\% sparsity, respectively, while delivering 3.23$\times$ decoding speedup and 6.21$\times$ memory savings at 95\% sparsity. Taken together, our results show that LLMs can be pushed into extreme sparsity while retaining strong performance, providing a foundation for further improving sparse models in this regime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hyeondo Jang, Kwanhee Lee, Dongyeop Lee, Namhoon Lee
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
