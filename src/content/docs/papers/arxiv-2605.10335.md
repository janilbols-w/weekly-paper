---
title: "PowerStep: Memory-Efficient Adaptive Optimization via $\\ell_p$-Norm Steepest Descent"
description: "Adaptive optimizers such as Adam are standard for training Transformers, but storing gradient first and second moments incurs substantial memory overhead."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.10335) · [PDF](https://arxiv.org/pdf/2605.10335)

## 一句话摘要

Adaptive optimizers such as Adam are standard for training Transformers, but storing gradient first and second moments incurs substantial memory overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Adaptive optimizers such as Adam are standard for training Transformers, but storing gradient first and second moments incurs substantial memory overhead. We introduce PowerStep, a memory-efficient optimizer that achieves coordinate-wise adaptivity without storing second-moment statistics. Motivated by $\ell_p$-norm steepest descent, PowerStep applies a signed-power transform directly to one momentum buffer. We establish a finite-horizon stationarity bound for exact, unregularized updates, with an $O(1/\sqrt{T})$ term and a noise-dependent residual. Experiments on Transformers from 124M to 235B parameters show competitive validation quality while halving $\texttt{fp32}$ optimizer-state memory relative to AdamW. Combined with uniform $\texttt{int8}$ quantization, PowerStep remains numerically stable and reduces optimizer-state memory by $\sim8\times$ compared to $\texttt{fp32}$ AdamW. PowerStep thus provides a simple, memory-efficient alternative for large-scale training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yao Lu, Dengdong Fan, Shixun Zhang, Yonghong Tian
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
