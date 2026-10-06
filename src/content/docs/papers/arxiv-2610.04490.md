---
title: "BARQ: Balanced Codebook Refinement for Low-Bit LLM Quantization"
description: "As large language models (LLMs) grow in parameter count, model storage and parameter memory traffic have become major bottlenecks to efficient deployment."
---

**评分：55/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.04490) · [PDF](https://arxiv.org/pdf/2610.04490)

## 一句话摘要

As large language models (LLMs) grow in parameter count, model storage and parameter memory traffic have become major bottlenecks to efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) grow in parameter count, model storage and parameter memory traffic have become major bottlenecks to efficient deployment. Codebook-based weight quantization reduces these costs, but imbalanced nearest-codeword assignments during fitting can leave some codewords insufficiently updated, limiting effective codebook utilization. To address this limitation, we propose Balanced Assignment Refinement for Quantization (BARQ), which improves quantization quality through balanced fitting of existing codebooks. Specifically, we first compute joint soft assignments between weight blocks and codewords through entropically regularized optimal transport with uniform marginals and curvature-weighted reconstruction costs, ensuring equal positive fitting mass for every codeword in the exact solution. We then refine the codewords through an assignment-weighted barycentric update, which we prove minimizes the fitting objective for fixed assignments. For finite Sinkhorn iterations, the implemented update retains this optimality provided all codeword masses exceed the denominator floor. Finally, we discard the soft assignments and use the refined codebook for standard hard nearest-codeword encoding, with our analysis establishing sufficient conditions for reducing hard-quantization distortion and evaluation loss. Across multiple LLMs, BARQ achieves lower perplexity and higher mean zero-shot accuracy than the evaluated baselines at comparable bit budgets. The code is available at https://github.com/chenhangcuisg-code/BARQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chenhang Cui, Xu Xie, Linrui Xu, Xiaohao Liu, Xingyu Zhu, Fei Shen, Tat-Seng Chua
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/chenhangcuisg-code/BARQ](https://github.com/chenhangcuisg-code/BARQ)
- 阅读深度：metadata
