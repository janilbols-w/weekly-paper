---
title: "Find the Fungible: Variable-Resolution Tokenization that Compacts Semantics with a Granularity Dial as a VLM \"Catalyst\""
description: "Efficient vision-language models should preserve a useful representation of the whole image, even under tight budgets."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.18690) · [PDF](https://arxiv.org/pdf/2610.18690)

## 一句话摘要

Efficient vision-language models should preserve a useful representation of the whole image, even under tight budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient vision-language models should preserve a useful representation of the whole image, even under tight budgets. However, aggressive pruning or indiscriminate merging can erase critical details and disrupt the spatial structure. We thus propose Varest, which maximizes semantic fungibility: tokens describing coherent content can be summarized together with minimal information loss. Object boundaries distilled from a visual foundation model guide grouping, while text localization protects details needed for reading. At lower budgets, Varest merges the image into coarser semantic regions, while maintaining full spatial coverage. After early language decoder layers process this representation, a learned selector prunes visual tokens that later layers no longer need, reducing repeated access to already integrated information. Across three LLaVA backbones and 13 benchmarks, Varest outperforms 10 training-free and 5 trained baselines in mean performance retention at every evaluated budget, preserving 86.10-92.33% of uncompressed performance using only 5.56% of tokens. This SOTA performance further generalizes to modern VLMs like Qwen3.8-27B.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Fu, Austin Wang, Charles Chen, Roby Aldave-Garza, Victor Xie, Xiyue Jiao, Yucheng Chen, Martin Tin
- 发布：2026-10-13；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
