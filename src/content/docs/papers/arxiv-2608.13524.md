---
title: "DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees"
description: "Speculative decoding losslessly accelerates autoregressive language models by verifying multiple draft tokens in parallel."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.13524) · [PDF](https://arxiv.org/pdf/2608.13524)

## 一句话摘要

Speculative decoding losslessly accelerates autoregressive language models by verifying multiple draft tokens in parallel.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding losslessly accelerates autoregressive language models by verifying multiple draft tokens in parallel. Diffusion-based drafters further reduce proposal latency by predicting an entire token block in parallel, but their position-wise distributions are marginal rather than conditioned on tokens selected along each draft path. Existing recurrent correction incorporates causal information along a single draft chain, whereas diffusion-based tree construction broadens candidate coverage without carrying this correction along individual branches. We introduce DARTree, a training-free speculative decoding method that extends a pretrained AR correction head from chains to trees. DARTree first constructs a fixed-width candidate tree by expanding and scoring all nodes at each depth in a single batch, and then only applies best-first pruning to select the verification tree, decoupling AR-head inference from sequential heap operations. Across seven math, code, and chat benchmarks, DARTree achieves the highest average acceptance length and speedup in all four model--temperature configurations, accepting up to 12.97 tokens per verification round, 98.6\% more than DFlash and 27.9\% more than Domino in the same setting, and reaching up to 9.73$\times$ lossless speedup over locally measured autoregressive decoding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
