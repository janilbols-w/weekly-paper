---
title: "From Layers to Submodules: Rethinking Granularity in Replacement-Based LLM Compression"
description: "Post-training compression of Large Language Models (LLMs) removes entire architectural components, either deleting them or replacing them with fitted modules."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.02559) · [PDF](https://arxiv.org/pdf/2606.02559)

## 一句话摘要

Post-training compression of Large Language Models (LLMs) removes entire architectural components, either deleting them or replacing them with fitted modules.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training compression of Large Language Models (LLMs) removes entire architectural components, either deleting them or replacing them with fitted modules. Existing replacement-based methods share two design constraints: full-layer granularity and contiguous selection. We argue that this is overly restrictive: in fact, redundancy in pretrained transformers is not confined to contiguous regions, nor does it evenly distribute between Attention and FeedForward outputs, implying that different strategies best approximate different submodule types and that removable components need not cluster within contiguous depth ranges. Based on this intuition, we introduce SubFit (Submodule-level Fitted residual replacement), which compresses LLMs at the submodule level: Attention and FeedForward submodules are selected non-contiguously, and each receives its own lightweight fitted residual bypass. SubFit operates post-training and requires only calibration data. Across ten LLMs (five base, five instruction-tuned), five sparsity levels from 12.5% to 37.5%, and four replacement-based baselines, SubFit achieves the best aggregate perplexity-accuracy trade-off across the evaluated sparsity levels, with larger gains under aggressive compression. At 25% sparsity, it retains 84.6% of dense downstream accuracy and incurs 2.42x perplexity degradation, against 81.6% and 4.34x for the strongest baselines, while delivering measurable inference speedup and KV-cache savings. Code is available at https://github.com/eliacunegatti/SubFit.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Elia Cunegatti, Marcus Vukojevic, Erik Nielsen, Giovanni Iacca
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/eliacunegatti/SubFit](https://github.com/eliacunegatti/SubFit)
- 阅读深度：metadata
